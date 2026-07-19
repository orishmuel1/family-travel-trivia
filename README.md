# Family Road Trip Travel Trivia App

An offline-first Progressive Web App (PWA) that serves educational learning points and
interactive trivia during family travel — designed to work with **zero internet** (remote
National Parks, planes, dead zones).

You add content by prompting any AI chat, dropping the result into `topics/`, and running
one Python command. See **[DESIGN.md](DESIGN.md)** for the *why*; this README is the *how*.

---

## ⚡ TL;DR — the whole loop

```bash
# 0. one-time setup
pip install -r requirements.txt          # installs PyYAML

# 1. add a topic: fill in prompt_blueprint.md's prompt, paste into ChatGPT/Gemini/Claude,
#    and save its reply as:
#        topics/<your_topic>.yaml

# 2. validate + build (also stamps the offline cache version)
python compiler.py

# 3. preview locally
python -m http.server 8080 --directory docs      # then open http://localhost:8080

# 4. publish
git add -A && git commit -m "Add <your_topic>" && git push
```

---

## 1. Prerequisites

- **Python 3.7+**
- **PyYAML** (the only hard dependency):
  ```bash
  pip install -r requirements.txt      # or: pip install pyyaml
  ```
- *(Optional)* **Pillow** — only if you want to regenerate the app icons with the icon tool:
  `pip install pillow`.

> Prefer an isolated environment? `python3 -m venv .venv` then activate it
> (`source .venv/bin/activate` on macOS/Linux, `.venv\Scripts\Activate.ps1` on Windows)
> before `pip install`.

---

## 2. Add or edit content (the main workflow)

You never hand-write the data. To add a topic:

1. Open **[prompt_blueprint.md](prompt_blueprint.md)** and copy the prompt in section 1.
2. Fill in the **`TOPIC`** line (the only required field). Optionally set `SUBCATEGORIES`,
   `EXTRA CATEGORIES`, or `NOTES` — leave them blank to let the AI choose.
3. Paste it into **ChatGPT / Gemini / Claude**. It replies with one YAML block.
4. Save that reply as **`topics/<your_topic_slug>.yaml`** (e.g. `topics/national_parks.yaml`).
   `.json` is also accepted.
5. Build:
   ```bash
   python compiler.py
   ```
   It validates every topic, **auto-fixes safe issues**, and prints plain-language
   `→ Fix:` lines for anything it can't. Fix those, re-run, done.

**Editing** an existing topic = edit its file in `topics/` and re-run `python compiler.py`.

### Other languages (e.g. Hebrew)

The visible text (titles, descriptions, facts, questions, answers) can be in **any
language** — just ask for it in the prompt's `NOTES` line (e.g. *"write everything in
Hebrew"*). The app displays right-to-left languages automatically. **One rule:** every
`id:` (topic and category) must stay in **English/Latin letters** — the AI does this for
you when using the blueprint prompt.

---

## 3. `compiler.py` — command reference

| Command | What it does |
| :--- | :--- |
| `python compiler.py` | Validate all topics → build `docs/data.json` → stamp the offline cache version in `docs/sw.js`. |
| `python compiler.py --check` | Validate everything, **write nothing** (a dry run). |
| `python compiler.py --check topics/foo.yaml` | Validate a single dropped file. |
| `python compiler.py --write-fixes` | Also save the safe auto-fixes back into the source files (as clean, ordered YAML). |

The compiler also maintains `topics/.created.json` (a small ledger of when each topic was
first added — used for "Newest/Oldest" sorting). **Commit that file too.**

---

## 4. Preview locally

The app must be served over HTTP (it fetches `data.json`), not opened as a file:

```bash
python -m http.server 8080 --directory docs
```

Open **http://localhost:8080** and click through your topics.

> **Seeing stale content while editing?** The service worker caches aggressively (that's the
> offline feature). During development, open **DevTools (F12) → Application → Service Workers**
> and tick **"Update on reload"** (or "Bypass for network"), then refresh. In normal use it
> updates on its own, because every build stamps a new cache version.

---

## 5. Publish to GitHub Pages

```bash
git add -A
git commit -m "Update content"
git push
```

One-time GitHub setup: **repo → Settings → Pages → Build and deployment → Deploy from a
branch → Branch: `main`, Folder: `/docs` → Save.**

Within a minute or two your PWA is live. Installed devices pull updates automatically,
because each build changes the cache version and the service worker evicts the old files.

---

## 6. Project layout

```
topics/                  Source content — one .yaml (or .json) per topic (FLAT, no subfolders)
  .created.json          Ledger of topic creation dates (auto-maintained; commit it)
compiler.py              Validate topics -> build docs/data.json -> stamp sw.js cache version
prompt_blueprint.md      Copy-paste AI prompt that generates a topic file
schema_template.yaml     Canonical schema reference
DESIGN.md                Intent, content model, and roadmap (source of truth)
requirements.txt         Python dependencies (PyYAML; Pillow optional)
docs/                    The compiled PWA (GitHub Pages serves this folder)
  index.html             The app (learning + trivia UI, themes, search/sort, offline load)
  data.json              Compiled database  (GENERATED — do not hand-edit)
  sw.js                  Service worker (offline cache; version stamped by compiler.py)
  manifest.json          PWA manifest
  icon-192.png / 512     Launcher icons
tools/
  generate_mock_icons.py (optional) redraw the placeholder PWA icons — needs Pillow
```

---

## 7. Optional tools

- **Regenerate the app icons** (placeholder indigo "T" icons):
  ```bash
  pip install pillow
  python tools/generate_mock_icons.py
  ```

---

## 8. How it works (in one paragraph)

Each topic is a YAML file: a **topic** has **categories**; a category has either a flat
`points` list or **`cards`** (one card per sub-item, e.g. one card per US state) plus
**`trivia`** questions. `compiler.py` validates them and compiles everything into a single
minified `docs/data.json`, and stamps a content-hash cache version into `docs/sw.js`. The
PWA (`docs/index.html`) loads `data.json`, caches it in IndexedDB, and the service worker
caches the app shell — so after one online visit it runs fully offline. Learning and trivia
are separate phases; trivia runs all questions with a running score and an optional
quiz-length chooser.
