#!/usr/bin/env python3
"""
PROJECT: Family Travel Trivia Application
FILE: compiler.py
PURPOSE: Validate topic files under topics/ (YAML or JSON), then compile them into
         docs/data.json and cache-bust docs/sw.js.

The validator is built for a no-debugging workflow: it reports EVERY problem at once
in plain language, auto-fixes safe issues (and tells you what it fixed), and only asks
you to hand-fix the things it genuinely can't.

Usage:
  python compiler.py                 Validate all topics, then build docs/data.json
  python compiler.py --check         Validate only (all topics), do not write anything
  python compiler.py --check FILE    Validate a single dropped file, do not write
  python compiler.py --write-fixes   Also save safe auto-fixes back into the source files
"""

import os
import sys
import json
import datetime
import hashlib
import re
from dataclasses import dataclass, field

# --- Make console output safe on Windows (default cp1252 can't encode emoji). -------
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    import yaml
except ImportError:
    print("Error: PyYAML is not installed. Please run:  pip install pyyaml")
    sys.exit(1)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOPICS_DIR = os.path.join(BASE_DIR, "topics")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
OUTPUT_FILE = os.path.join(DOCS_DIR, "data.json")
SW_FILE = os.path.join(DOCS_DIR, "sw.js")
CREATED_LEDGER = os.path.join(TOPICS_DIR, ".created.json")

VALID_TRIVIA_TYPES = ("multiple_choice", "single_qa")
MIN_POINTS, MAX_POINTS = 2, 5           # flat category points
CARD_MIN_POINTS, CARD_MAX_POINTS = 1, 6  # per-card (subcategory) bullets


# ---------------------------------------------------------------------------------
# Issue model + reporting
# ---------------------------------------------------------------------------------
@dataclass
class Issue:
    level: str          # "error" or "fix"
    location: str       # human-readable path to the problem
    message: str        # what's wrong (or what was fixed)
    hint: str = ""      # how to fix it (errors only)


@dataclass
class FileResult:
    path: str                       # repo-relative path, for display
    issues: list = field(default_factory=list)
    data: object = None             # normalized topic dict (None if unusable)

    @property
    def errors(self):
        return [i for i in self.issues if i.level == "error"]

    @property
    def fixes(self):
        return [i for i in self.issues if i.level == "fix"]


def rel(path):
    """Path relative to the repo root, using forward slashes for display."""
    try:
        return os.path.relpath(path, BASE_DIR).replace(os.sep, "/")
    except ValueError:
        return path


# ---------------------------------------------------------------------------------
# Normalization helpers (the "safe auto-fix" toolbox)
# ---------------------------------------------------------------------------------
_SMART_QUOTES = {
    "“": '"', "”": '"', "‘": "'", "’": "'",
    "–": "-", "—": "-", " ": " ",
}


def clean_str(value):
    """Trim, collapse smart quotes/dashes to ASCII. Returns (clean, changed)."""
    if not isinstance(value, str):
        return value, False
    out = value
    for bad, good in _SMART_QUOTES.items():
        out = out.replace(bad, good)
    out = out.strip()
    return out, (out != value)


def slugify(value):
    """Lowercase snake_case slug: spaces/dashes -> _, drop other punctuation."""
    s = str(value).strip().lower()
    s = re.sub(r"[\s\-]+", "_", s)
    s = re.sub(r"[^a-z0-9_]", "", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s


# ---------------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------------
def load_topic_file(path):
    """Return (data, error_message). Parses .json as JSON, everything else as YAML."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        return None, f"could not read file: {e}"

    if not text.strip():
        return None, "file is empty"

    try:
        if path.lower().endswith(".json"):
            return json.loads(text), None
        return yaml.safe_load(text), None      # YAML also accepts JSON syntax
    except yaml.YAMLError as e:
        return None, f"YAML syntax error: {e}"
    except json.JSONDecodeError as e:
        return None, f"JSON syntax error: {e}"


# ---------------------------------------------------------------------------------
# Validation + normalization for a single topic file
# ---------------------------------------------------------------------------------
def resolve_correct(correct, options):
    """
    Resolve the 'correct' field to a 0-3 index.
    Returns (index_or_None, fixed_bool, error_message_or_None).
    """
    # Already a proper integer index.
    if isinstance(correct, bool):   # bool is an int subclass; treat as invalid
        return None, False, "'correct' must be a number 0-3, not true/false."
    if isinstance(correct, int):
        if 0 <= correct <= 3:
            return correct, False, None
        return None, False, f"'correct' index {correct} is out of range."
    # A numeric string like "2".
    if isinstance(correct, str):
        s = correct.strip()
        if s.isdigit():
            idx = int(s)
            if 0 <= idx <= 3:
                return idx, True, None
            return None, False, f"'correct' index {idx} is out of range."
        # The answer text itself, instead of an index.
        for i, opt in enumerate(options):
            if isinstance(opt, str) and opt.strip().lower() == s.lower():
                return i, True, None
        return None, False, "'correct' is not a 0-3 index and doesn't match any option."
    return None, False, "'correct' is missing or not a number."


def validate_trivia(loc, trivia, issues):
    """Validate + normalize one trivia item in place. loc = location prefix."""
    if not isinstance(trivia, dict):
        issues.append(Issue("error", loc, "this trivia entry is not an object.",
                            "Each trivia item needs 'type', 'question', and its answer fields."))
        return

    # type: normalize + infer if missing
    raw_type = trivia.get("type")
    if isinstance(raw_type, str):
        norm = raw_type.strip().lower().replace(" ", "_").replace("-", "_")
        if norm != raw_type:
            trivia["type"] = norm
            issues.append(Issue("fix", loc, f"type '{raw_type}' normalized to '{norm}'."))
        raw_type = trivia.get("type")
    if not raw_type:
        if trivia.get("options") is not None:
            trivia["type"] = "multiple_choice"
            issues.append(Issue("fix", loc, "missing type inferred as 'multiple_choice' (has options)."))
        elif trivia.get("answer") is not None:
            trivia["type"] = "single_qa"
            issues.append(Issue("fix", loc, "missing type inferred as 'single_qa' (has answer)."))
        else:
            issues.append(Issue("error", loc, "trivia is missing 'type'.",
                                "Set type to 'multiple_choice' or 'single_qa'."))
            return
    t_type = trivia.get("type")
    if t_type not in VALID_TRIVIA_TYPES:
        issues.append(Issue("error", loc, f"invalid type '{t_type}'.",
                            "Use 'multiple_choice' or 'single_qa'."))
        return

    # question
    q, changed = clean_str(trivia.get("question"))
    if changed:
        trivia["question"] = q
    if not q or not str(q).strip():
        issues.append(Issue("error", loc, "trivia is missing a 'question'.",
                            "Add a question string."))

    if t_type == "multiple_choice":
        options = trivia.get("options")
        if not isinstance(options, list):
            issues.append(Issue("error", loc, "multiple_choice has no 'options' list.",
                                "Add exactly 4 options."))
            return
        # normalize each option string
        for i, opt in enumerate(options):
            c, changed = clean_str(opt)
            if changed:
                options[i] = c
        if len(options) != 4:
            issues.append(Issue("error", loc,
                                f"multiple_choice needs exactly 4 options, found {len(options)}.",
                                "Add or remove options so there are exactly 4."))
            return
        idx, fixed, err = resolve_correct(trivia.get("correct"), options)
        if err:
            issues.append(Issue("error", loc, err,
                                "Set 'correct' to the 0-based position of the right option (0, 1, 2, or 3)."))
        else:
            if fixed:
                issues.append(Issue("fix", loc,
                                    f"'correct' resolved to index {idx} ({options[idx]!r})."))
            trivia["correct"] = idx

    elif t_type == "single_qa":
        answer, changed = clean_str(trivia.get("answer"))
        if changed:
            trivia["answer"] = answer
        if not answer or not str(answer).strip():
            issues.append(Issue("error", loc, "single_qa is missing an 'answer'.",
                                "Add an 'answer' string."))


def validate_cards(cloc, cards, issues):
    """Validate + normalize a category's 'cards' list (each card = a subcategory)."""
    if not isinstance(cards, list) or not cards:
        issues.append(Issue("error", cloc, "'cards' is present but empty or not a list.",
                            "Add at least one card (a subcategory with a title and a few facts)."))
        return
    for i, card in enumerate(cards):
        cardloc = f"{cloc} -> card #{i + 1}"
        if not isinstance(card, dict):
            issues.append(Issue("error", cardloc, "this card is not an object.",
                                "Each card needs a 'title' and a 'points' list."))
            continue
        title, changed = clean_str(card.get("title"))
        if changed:
            card["title"] = title
        if not title:
            issues.append(Issue("error", cardloc, "card is missing a 'title'.",
                                "Add the subcategory name (e.g. the state or item)."))
        else:
            cardloc = f"{cloc} -> card '{title}'"
        pts = card.get("points")
        if not isinstance(pts, list):
            issues.append(Issue("error", cardloc, "card has no 'points' list.",
                                f"Add {CARD_MIN_POINTS}-{CARD_MAX_POINTS} bullet facts."))
        else:
            for j, pt in enumerate(pts):
                c, ch = clean_str(pt)
                if ch:
                    pts[j] = c
            n = len(pts)
            if n < CARD_MIN_POINTS or n > CARD_MAX_POINTS:
                issues.append(Issue("error", cardloc,
                                    f"card 'points' must have {CARD_MIN_POINTS}-{CARD_MAX_POINTS} facts, found {n}.",
                                    f"Adjust to between {CARD_MIN_POINTS} and {CARD_MAX_POINTS} facts."))


def validate_topic(path, data):
    """Validate + normalize one topic file. Returns a FileResult."""
    result = FileResult(path=rel(path))
    issues = result.issues

    if not isinstance(data, dict):
        issues.append(Issue("error", "(top level)",
                            "the top level of the file is not a topic object.",
                            "It must start with id / title / description / categories."))
        return result

    # --- topic id (derive from filename if missing; slugify if malformed) ---
    tid = data.get("id")
    if not tid:
        derived = slugify(os.path.splitext(os.path.basename(path))[0])
        data["id"] = derived
        issues.append(Issue("fix", "topic", f"missing topic id derived from filename -> '{derived}'."))
    else:
        slug = slugify(tid)
        if slug != tid:
            data["id"] = slug
            issues.append(Issue("fix", "topic", f"topic id '{tid}' normalized to '{slug}'."))
    tid = data.get("id")
    tloc = f"topic '{tid}'"

    # --- title / description ---
    title, changed = clean_str(data.get("title"))
    if changed:
        data["title"] = title
    if not title:
        issues.append(Issue("error", tloc, "topic is missing a 'title'.",
                            "Add a display title, e.g. title: Crater Lake National Park"))
    desc, changed = clean_str(data.get("description"))
    if changed:
        data["description"] = desc
    if not desc:
        issues.append(Issue("error", tloc, "topic is missing a 'description'.",
                            "Add a one-sentence overview of the topic."))

    # --- categories ---
    categories = data.get("categories")
    if not isinstance(categories, list) or not categories:
        issues.append(Issue("error", tloc, "topic has no 'categories' list.",
                            "Add at least one category with a title, description, points, and trivia."))
        return result

    seen_cat_ids = {}
    for c_index, cat in enumerate(categories):
        if not isinstance(cat, dict):
            issues.append(Issue("error", f"{tloc} -> category #{c_index + 1}",
                                "this category is not an object.",
                                "Each category needs id, title, description, points, trivia."))
            continue

        # category id (derive from title if missing)
        cid = cat.get("id")
        if not cid:
            if cat.get("title"):
                derived = slugify(cat["title"])
                cat["id"] = derived
                issues.append(Issue("fix", f"{tloc} -> category '{cat['title']}'",
                                    f"missing category id derived from title -> '{derived}'."))
            else:
                issues.append(Issue("error", f"{tloc} -> category #{c_index + 1}",
                                    "category is missing both 'id' and 'title'.",
                                    "Add at least a title."))
                continue
        else:
            slug = slugify(cid)
            if slug != cid:
                cat["id"] = slug
                issues.append(Issue("fix", f"{tloc} -> category '{cid}'",
                                    f"category id '{cid}' normalized to '{slug}'."))
        cid = cat.get("id")
        cloc = f"{tloc} -> category '{cid}'"

        if cid in seen_cat_ids:
            issues.append(Issue("error", cloc,
                                f"duplicate category id '{cid}' within this topic.",
                                "Give each category a unique id."))
        seen_cat_ids[cid] = True

        # title / description
        ctitle, changed = clean_str(cat.get("title"))
        if changed:
            cat["title"] = ctitle
        if not ctitle:
            issues.append(Issue("error", cloc, "category is missing a 'title'.",
                                "Add a display title for the category."))
        # description is optional (a short intro read before the cards/trivia)
        cdesc, changed = clean_str(cat.get("description"))
        if changed:
            cat["description"] = cdesc

        # A category holds EITHER flat 'points' OR 'cards' (subcategories). Need one.
        has_points = isinstance(cat.get("points"), list)
        has_cards = isinstance(cat.get("cards"), list)
        if not has_points and not has_cards:
            issues.append(Issue("error", cloc,
                                "category has neither 'points' nor 'cards'.",
                                "Add a 'points' list of facts, or a 'cards' list of subcategories."))
        if has_points:
            points = cat["points"]
            for i, pt in enumerate(points):
                c, changed = clean_str(pt)
                if changed:
                    points[i] = c
            n = len(points)
            if n < MIN_POINTS or n > MAX_POINTS:
                issues.append(Issue("error", cloc,
                                    f"'points' must have {MIN_POINTS}-{MAX_POINTS} facts, found {n}.",
                                    f"Adjust to between {MIN_POINTS} and {MAX_POINTS} facts."))
        if has_cards:
            validate_cards(cloc, cat["cards"], issues)

        # trivia
        trivia = cat.get("trivia")
        if not isinstance(trivia, list) or not trivia:
            issues.append(Issue("error", cloc, "category has no 'trivia' questions.",
                                "Add at least one trivia question."))
        else:
            for t_index, t in enumerate(trivia):
                validate_trivia(f"{cloc} -> trivia #{t_index + 1}", t, issues)

    # Only expose data for compilation if there are no hard errors.
    if not result.errors:
        result.data = data
    return result


# ---------------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------------
def print_report(results):
    """Print a consolidated, scannable validation report. Returns total error count."""
    total_errors = sum(len(r.errors) for r in results)
    total_fixes = sum(len(r.fixes) for r in results)

    print("\n" + "=" * 64)
    print("  CONTENT VALIDATION")
    print("=" * 64)

    for r in results:
        if not r.issues:
            print(f"  OK    {r.path}")
        else:
            mark = "FAIL" if r.errors else "OK*"
            print(f"  {mark:<5} {r.path}   ({len(r.errors)} error(s), {len(r.fixes)} auto-fix)")

    for r in results:
        if not r.issues:
            continue
        print("\n" + "-" * 64)
        print(f"  {r.path}")
        print("-" * 64)
        for issue in r.issues:
            tag = "[ERROR]     " if issue.level == "error" else "[auto-fixed]"
            print(f"  {tag} {issue.location}")
            print(f"               {issue.message}")
            if issue.hint:
                print(f"               -> Fix: {issue.hint}")

    print("\n" + "=" * 64)
    if total_errors:
        print(f"  {total_errors} error(s) and {total_fixes} auto-fix(es) across {len(results)} file(s).")
        print(f"  Fix the {total_errors} error(s) listed above, then run the compiler again.")
    else:
        note = f" ({total_fixes} auto-fix(es) applied.)" if total_fixes else ""
        print(f"  All {len(results)} file(s) valid.{note}")
    print("=" * 64 + "\n")
    return total_errors


# ---------------------------------------------------------------------------------
# Persisting auto-fixes back to source (opt-in via --write-fixes)
# ---------------------------------------------------------------------------------
def _ordered(d, key_order):
    """Return dict d with keys in key_order first, then any extras, preserving values."""
    out = {k: d[k] for k in key_order if k in d}
    for k, v in d.items():
        if k not in out:
            out[k] = v
    return out


def canonicalize(topic):
    """Rebuild a topic dict with a clean, consistent key order for readable output."""
    topic = _ordered(topic, ["id", "title", "description", "categories"])
    cats = []
    for cat in topic.get("categories", []):
        if isinstance(cat, dict):
            cat = _ordered(cat, ["id", "title", "description", "cards", "points", "trivia"])
            if isinstance(cat.get("cards"), list):
                cat["cards"] = [
                    _ordered(c, ["title", "points"]) if isinstance(c, dict) else c
                    for c in cat["cards"]
                ]
            cat["trivia"] = [
                _ordered(t, ["type", "question", "options", "correct", "answer"])
                if isinstance(t, dict) else t
                for t in cat.get("trivia", [])
            ]
        cats.append(cat)
    topic["categories"] = cats
    return topic


def write_fixes_back(path, data):
    data = canonicalize(data)
    try:
        if path.lower().endswith(".json"):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            with open(path, "w", encoding="utf-8") as f:
                yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, width=100)
        return True
    except OSError as e:
        print(f"  Warning: could not write fixes to {rel(path)}: {e}")
        return False


# ---------------------------------------------------------------------------------
# Build + cache-bust
# ---------------------------------------------------------------------------------
def build_database(topics):
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)
    trivia_count = sum(len(cat.get("trivia", []))
                       for topic in topics for cat in topic.get("categories", []))
    compiled_db = {
        "app_name": "Family Travel Trivia",
        "version": "1.0.0",
        "last_updated": datetime.date.today().isoformat(),
        "topics": topics,
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(compiled_db, f, separators=(",", ":"), ensure_ascii=False)
    return len(topics), trivia_count


def update_service_worker_version():
    if not os.path.exists(OUTPUT_FILE) or not os.path.exists(SW_FILE):
        print("  Note: data.json or sw.js missing; skipped cache-busting.")
        return None
    # Hash the shell + data so ANY change (content OR app shell) bumps the cache
    # version and forces installed devices to pull the update.
    hasher = hashlib.md5()
    for name in ("data.json", "index.html", "manifest.json"):
        p = os.path.join(DOCS_DIR, name)
        if os.path.exists(p):
            with open(p, "rb") as f:
                hasher.update(f.read())
    file_hash = hasher.hexdigest()[:8]
    with open(SW_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    new_line = f"const CACHE_NAME = 'trivia-cache-v-{file_hash}';"
    updated = re.sub(r"const\s+CACHE_NAME\s*=\s*['\"].*?['\"];", new_line, content, count=1)
    with open(SW_FILE, "w", encoding="utf-8") as f:
        f.write(updated)
    return file_hash


# ---------------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------------
def gather_files(single_file):
    if single_file:
        if not os.path.exists(single_file):
            print(f"Error: file not found: {single_file}")
            sys.exit(2)
        return [os.path.abspath(single_file)]
    if not os.path.isdir(TOPICS_DIR):
        print(f"Error: topics directory not found at: {TOPICS_DIR}")
        sys.exit(2)
    files = []
    for name in sorted(os.listdir(TOPICS_DIR)):
        if name.startswith("."):
            continue  # skip dotfiles like the .created.json ledger
        if name.lower().endswith((".yaml", ".yml", ".json")):
            files.append(os.path.join(TOPICS_DIR, name))
    return files


def stamp_created_dates(topics):
    """
    Give each topic a stable 'created' date via a committed ledger
    (topics/.created.json). New topics get today's date on first compile; existing
    topics keep theirs. The ledger is committed so dates match across all devices.
    """
    ledger = {}
    if os.path.exists(CREATED_LEDGER):
        try:
            with open(CREATED_LEDGER, "r", encoding="utf-8") as f:
                ledger = json.load(f)
        except (OSError, json.JSONDecodeError):
            ledger = {}

    today = datetime.date.today().isoformat()
    changed = False
    current_ids = set()
    for topic in topics:
        tid = topic.get("id")
        if not tid:
            continue
        current_ids.add(tid)
        if tid not in ledger:
            ledger[tid] = today
            changed = True
        topic["created"] = ledger[tid]

    # Prune ledger entries for topics that no longer exist.
    for stale in [k for k in ledger if k not in current_ids]:
        del ledger[stale]
        changed = True

    if changed:
        try:
            with open(CREATED_LEDGER, "w", encoding="utf-8") as f:
                json.dump(ledger, f, indent=2, sort_keys=True)
        except OSError as e:
            print(f"  Warning: could not update creation-date ledger: {e}")
    return ledger


def main(argv):
    check_only = "--check" in argv
    write_fixes = "--write-fixes" in argv
    positional = [a for a in argv if not a.startswith("--")]
    single_file = positional[0] if positional else None

    files = gather_files(single_file)
    if not files:
        print("No topic files found under topics/. Add a .yaml or .json file and re-run.")
        sys.exit(0 if check_only else 2)

    results = []
    seen_topic_ids = {}
    for path in files:
        data, err = load_topic_file(path)
        if err:
            r = FileResult(path=rel(path))
            r.issues.append(Issue("error", "(file)", err,
                                  "Check the file's syntax (indentation, quotes, commas)."))
            results.append(r)
            continue
        r = validate_topic(path, data)
        # cross-file duplicate topic id
        if r.data is not None:
            tid = r.data.get("id")
            if tid in seen_topic_ids:
                r.issues.append(Issue("error", "topic",
                                      f"duplicate topic id '{tid}' (also in {seen_topic_ids[tid]}).",
                                      "Give each topic file a unique id."))
                r.data = None
            else:
                seen_topic_ids[tid] = r.path
        results.append(r)

    total_errors = print_report(results)

    if write_fixes:
        fixed_any = False
        for path, r in zip(files, results):
            if r.fixes and r.data is not None:
                if write_fixes_back(path, r.data):
                    fixed_any = True
        if fixed_any:
            print("  Auto-fixes written back to source file(s).\n")

    # Building the database ALWAYS compiles the whole topics/ folder. A positional
    # single file (or --check) is validation-only and never triggers a build.
    building = single_file is None and not check_only
    if not building:
        sys.exit(1 if total_errors else 0)

    if total_errors:
        print("  Build skipped — resolve the errors above first.\n")
        sys.exit(1)

    topics = [r.data for r in results if r.data is not None]
    stamp_created_dates(topics)
    n_topics, n_trivia = build_database(topics)
    version = update_service_worker_version()

    print("=" * 64)
    print("  DATABASE COMPILATION SUCCESSFUL")
    print("=" * 64)
    print(f"  Topics compiled  : {n_topics}")
    print(f"  Trivia questions : {n_trivia}")
    print(f"  Output           : docs/data.json")
    if version:
        print(f"  SW cache version : {version}")
    print("=" * 64 + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
