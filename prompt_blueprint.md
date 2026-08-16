# Topic Generator — Copy-Paste Prompt

You never write YAML by hand. To add a topic:

1. Copy the **locked prompt** in section 1.
2. Fill in **`TOPIC`** — the only required field. Everything else is optional.
3. Paste into ChatGPT / Gemini / Claude. It replies with **two YAML code blocks — an
   English version and a Hebrew version of the same topic — followed by a short summary.**
4. Save the first block as `topics/<slug>_en.yaml` and the second as `topics/<slug>_he.yaml`,
   run `python compiler.py`, follow any `→ Fix:` lines, then commit + push.

**The model:** every topic gets a default **"Important Facts"** category made of **cards**
(one per subcategory, e.g. one per US state), plus any extra theme categories you ask for.
Each topic is produced in **both English and Hebrew in a single reply**; the app's Language
toggle switches between them.

---

## 1. The locked prompt (copy everything in this block)

```text
You are an educational content creator for a family road-trip trivia app. For the topic
defined under "YOUR INPUT", produce the SAME topic in BOTH English and Hebrew — two
strictly-formatted YAML datasets — followed by a short summary.

V0:
===== YOUR INPUT =====
TOPIC:            (REQUIRED — the only field you must fill in. e.g. US States)
SUBCATEGORIES:    (optional — the items to make cards for. LEAVE BLANK and you choose a good set.)
EXTRA CATEGORIES: (optional — extra themes beyond "Important Facts". LEAVE BLANK and you decide.)
AUDIENCE:         (optional — topic default: "family" (default) or "adult")
NOTES:            (optional — any other guidance: focus, tone, how many items, etc.)
======================

V1: Family fun
===== YOUR INPUT =====
TOPIC:            (REQUIRED — the only field you must fill in. e.g. US States)
SUBCATEGORIES:    (optional — the items to make cards for. LEAVE BLANK and you choose a good set.)
EXTRA CATEGORIES: (optional — extra themes beyond "Important Facts". LEAVE BLANK and you decide.)
AUDIENCE:         (optional — topic default: "family" (default) or "adult")
NOTES:            (optional — any other guidance: focus, tone, how many items, etc.)
======================

WHAT TO OUTPUT
1. An English YAML code block (lang: en, topic id ends with "_en").
2. A Hebrew YAML code block — the SAME topic translated to Hebrew (lang: he, topic id ends
   with "_he"). Same structure and same English ids; translate all VISIBLE text (titles,
   descriptions, points, questions, answers) to Hebrew.
3. After both code blocks, a short plain-text SUMMARY (see the end of this prompt).

HANDLING BLANK FIELDS
- TOPIC is the only required field.
- If SUBCATEGORIES is blank: choose a strong set (about 8-15, or the full set if the topic
  clearly implies it, e.g. all US states).
- If EXTRA CATEGORIES is blank: keep just "Important Facts", or add 1-2 genuinely useful themes.
- Honor NOTES.

STRUCTURE (each of the two YAML datasets)
- One topic: id (snake_case slug of TOPIC + "_en" or "_he"), title, and a meaningful 2-4
  sentence description.
- Topic metadata: lang ("en" or "he"); audience ("family" default, or from AUDIENCE).
- Categories:
    * ALWAYS a first category "Important Facts" (id: important_facts).
    * PLUS one category per EXTRA CATEGORY (or the ones you chose).
- Each category:
    * description: a meaningful 2-3 sentence intro.
    * audience (OPTIONAL): "family" (default) or "adult" — mark a category "adult" ONLY if it
      is not suitable for the whole family (the app hides adult categories in Family mode).
    * cards: ONE card per subcategory. Each card has a title and 4-5 short, true fact
      sentences written for this category's theme.
    * trivia: a GENEROUS set — about one question per card, never fewer than 5 for a category
      with several cards. Each is either:
        - multiple_choice: EXACTLY 4 options + correct = 0-based index (0-3), or
        - single_qa: a question + a short exact answer.

OUTPUT RULES (the compiler enforces the YAML)
- Two YAML code blocks (English first, then Hebrew), each containing nothing but YAML. Then
  the plain-text summary AFTER the code blocks.
- 2-space indentation. Straight quotes ("). All ids are lowercase snake_case in ENGLISH /
  Latin letters only (in BOTH versions) — only the visible text is translated to Hebrew.
- Facts accurate and family-friendly (unless a category is marked audience: adult). Wrong
  multiple-choice options must be plausible but clearly incorrect.

FOLLOW THIS SHAPE (English version; the Hebrew version mirrors it exactly, translated):
id: us_states_en
title: US States
description: >
  A state-by-state tour of the United States. Each state has its own standout facts, and the
  trivia lets the whole family test what they just learned.
lang: en
audience: family
categories:
  - id: important_facts
    title: Important Facts
    # audience: adult        # optional — add only for a category not for the whole family
    description: >
      The most surprising facts about each state — read these aloud before the trivia round.
    cards:
      - title: California
        points:
          - "California is the most populous US state, home to about 39 million people."
          - "It has the largest economy of any US state, bigger than most whole countries."
          - "It stretches from Death Valley, North America's lowest point, up to Mount Whitney."
          - "Silicon Valley makes it a global center of technology and innovation."
      - title: Texas
        points:
          - "Texas is the second-largest state by both area and population."
          - "It was an independent republic for almost a decade before joining the US in 1845."
          - "Houston is home to NASA's Johnson Space Center."
          - "Texas produces more wind power than any other US state."
    trivia:
      - type: multiple_choice
        question: "Which of these states is the most populous?"
        options: ["Texas", "California", "Florida", "New York"]
        correct: 1
      - type: single_qa
        question: "Which state was once an independent republic before joining the US?"
        answer: "Texas"

Then output the SAME topic again as a SECOND YAML block, in Hebrew:
  id: us_states_he, lang: he, all visible text in Hebrew, ids unchanged (English).

SUMMARY (plain text, AFTER the two code blocks — for the human, NOT part of the files):
  Topic: <title> — <N> categories — generated in English (_en) and Hebrew (_he)
  Then one line per category:
    - <category title> [<audience>] — <C> cards, <Q> questions
  Total questions per version: <sum>
```

---

## 2. Notes

- **The only required field is `TOPIC`.**
- Save the two blocks as `topics/<slug>_en.yaml` and `topics/<slug>_he.yaml`, then run
  `python compiler.py`.
- **Per-category audience:** add `audience: adult` on a category that isn't for the whole
  family. The app's **Family** filter then hides adult categories (and topics with nothing
  family-safe); **Adults** / **All** reveal them.
- **Use the summary** to sanity-check the structure (category count, cards, questions) before
  committing — if it looks thin or wrong, ask for another round.
- **Long outputs get cut off** — especially on free chat accounts (they may split the reply).
  If it splits, paste the parts back-to-back in order; the compiler flags anything mangled.

## 3. Field reference

| Field | Where | Rule |
| :--- | :--- | :--- |
| `id`, `title`, `description` | topic | slug (ends `_en`/`_he`) + name + a 2–4 sentence intro |
| `lang` | topic | `en` / `he` (auto-detected if omitted) |
| `audience` | topic | `family` (default) or `adult` |
| `categories[]` | topic | first is `important_facts`; extras optional |
| `categories[].description` | category | a 2–3 sentence intro (recommended) |
| `categories[].audience` | category | `family` / `adult` (optional; overrides the topic default) |
| `categories[].cards[]` | category | one card per subcategory *(a category has cards **or** flat `points`)* |
| `cards[].title` / `cards[].points[]` | card | subcategory name + 1–6 facts (aim for 4–5) |
| `categories[].points[]` | category | 2–5 facts — only for a simple, non-card category |
| `categories[].trivia[]` | category | ~one per card, at least 5 for multi-card (`multiple_choice` needs 4 options + 0-based `correct`; `single_qa` needs `answer`) |

## 4. Variant — a simple single-subject topic

For one place/subject (e.g. Crater Lake) instead of a collection, skip cards: give each
category a flat `points` list (2–5 facts) plus `trivia`. The compiler accepts either shape,
and the model still produces both the English and Hebrew versions.
