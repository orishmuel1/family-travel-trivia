# Topic Generator Blueprint & Templates

This document defines how new trivia topics are generated, structured, and validated for the Family Travel Trivia application.

---

## 1. Generation Workflows

### Option A: In-Session via Antigravity (Recommended)
You can ask Antigravity directly in this chat to generate, expand, or update any topic. Simply provide your inputs:
```text
Generate a new topic:
- TOPIC: [Your topic name, e.g., World Wonders / Space Exploration / Famous Scientists]
- VERSION: [V1 Family Fun (Default) / V2 Deep Dive / V3 Single-Subject]
- SUBCATEGORIES: [Optional - items to create cards for, or leave blank to auto-select]
- EXTRA CATEGORIES: [Optional - extra themes beyond Important Facts]
- AUDIENCE: [family (default) or adult]
- NOTES: [Any special focus or requests]
```
Antigravity will automatically:
1. Write both `topics/<slug>_en.yaml` and `topics/<slug>_he.yaml`.
2. Ensure full structural parity and accurate Hebrew translation.
3. Validate and compile via `./.venv/bin/python compiler.py`.
4. Stage and commit the updates to git.

---

### Option B: External LLM Copy-Paste Prompt (ChatGPT / Claude / Gemini Web)
If generating in an external LLM web interface, copy the entire code box for the version you want (**V1**, **V2**, or **V3**), fill in the `YOUR INPUT` section, paste into the LLM, and save the outputs as `topics/<slug>_en.yaml` and `topics/<slug>_he.yaml`.

---

## 2. Prompt Templates by Version

### V1: Family Fun (Rich & Comprehensive — Default)
Use for standard multi-item topics with generous depth, fun facts, and plenty of trivia questions.

```text
You are an educational content creator for a family road-trip trivia app. For the topic
defined under "YOUR INPUT", produce the SAME topic in BOTH English and Hebrew — two
strictly-formatted YAML datasets — followed by a short summary.

===== YOUR INPUT =====
TOPIC:            (REQUIRED — e.g., Famous Inventions & Discoveries, World Wonders)
SUBCATEGORIES:    (optional — items to make cards for. LEAVE BLANK and choose a generous set of 8-12 items.)
EXTRA CATEGORIES: (optional — 2-4 extra themes beyond "Important Facts". LEAVE BLANK and you decide.)
AUDIENCE:         (optional — "family" (default) or "adult")
NOTES:            (optional — any other guidance: focus, tone, how many items, etc.)
======================

VOLUME & DEPTH REQUIREMENTS:
- Structure: ALWAYS start with category "Important Facts" (id: important_facts) + 2-4 EXTRA theme categories.
- Cards: Exactly 8 to 12 cards per category (each card = 1 subcategory entity).
- Facts per card: Exactly 4-5 engaging, informative, true bullet points per card.
- Trivia: At least 15 to 20 questions per category (mix of multiple_choice with 4 options and single_qa with concise answers).
- Total questions: 60-100 questions total per language file.

WHAT TO OUTPUT:
1. An English YAML code block (lang: en, id: <slug>_en).
2. A Hebrew YAML code block — the SAME topic translated to Hebrew (lang: he, id: <slug>_he).
   - Keep all category/card IDs in English (snake_case).
   - Translate all visible text (titles, descriptions, points, questions, answers) into natural Hebrew.
   - HEBREW QUOTE RULE: Do NOT use raw ASCII double quotes inside double-quoted strings (e.g. use Hebrew gershayim ״ or single quotes for acronyms like מכ״ם, תנ״ך, צה״ל).
3. After both code blocks, a short plain-text summary showing card & question counts per category.

FOLLOW THIS YAML SHAPE:
id: sample_topic_en
title: Sample Topic
description: >
  A captivating journey through the topic. Read the fascinating facts aloud before testing your knowledge!
lang: en
audience: family
categories:
  - id: important_facts
    title: Important Facts
    description: >
      Foundational facts and essential milestones to read before the trivia round.
    cards:
      - title: Item One
        points:
          - "Engaging, true fact sentence #1."
          - "Engaging, true fact sentence #2."
          - "Engaging, true fact sentence #3."
          - "Engaging, true fact sentence #4."
      - title: Item Two
        points:
          - "Engaging, true fact sentence #1."
          - "Engaging, true fact sentence #2."
          - "Engaging, true fact sentence #3."
          - "Engaging, true fact sentence #4."
    trivia:
      - type: multiple_choice
        question: "Which item was developed first?"
        options: ["Item One", "Item Two", "Item Three", "Item Four"]
        correct: 0
      - type: single_qa
        question: "What material was used in the first prototype?"
        answer: "Wood"

SUMMARY FORMAT (plain text, AFTER the two code blocks):
  Topic: <title> — <N> categories — generated in English (_en) and Hebrew (_he)
  Then one line per category:
    - <category title> [<audience>] — <C> cards, <Q> questions
  Total questions per version: <sum>
```

---

### V2: Deep Dive / Comprehensive Encyclopedia
Use when creating exhaustive, complete collections (e.g., all 50 US States, all 45 US Presidents, complete historical timelines).

```text
You are an educational content creator for a family road-trip trivia app. For the topic
defined under "YOUR INPUT", produce an EXHAUSTIVE, deeply detailed topic in BOTH English and Hebrew — two
strictly-formatted YAML datasets — followed by a short summary.

===== YOUR INPUT =====
TOPIC:            (REQUIRED — e.g., US Presidents, US States, Israeli Prime Ministers)
SUBCATEGORIES:    (e.g., ALL members of the complete set: all 50 states, all 45 presidents, etc.)
EXTRA CATEGORIES: (3-5 rich theme categories analyzing the subject from different angles)
AUDIENCE:         (optional — "family" (default) or "adult")
NOTES:            (optional — guidance on depth, timelines, trivia style)
======================

VOLUME & DEPTH REQUIREMENTS:
- Structure: "Important Facts" covers EVERY single entity in the full collection (exhaustive set).
- Extra Categories: 3-5 curated thematic categories with 8-15 cards each.
- Facts per card: Exactly 4-5 rich, historically accurate, memorable facts per card.
- Trivia: At least 20 to 30 questions per category (balanced mix of multiple_choice with 4 options and single_qa).
- Total questions: 100+ questions total per language file.

WHAT TO OUTPUT:
1. An English YAML code block (lang: en, id: <slug>_en).
2. A Hebrew YAML code block — the SAME topic translated to Hebrew (lang: he, id: <slug>_he).
   - Keep all category/card IDs in English (snake_case).
   - Translate all visible text (titles, descriptions, points, questions, answers) into natural Hebrew.
   - HEBREW QUOTE RULE: Do NOT use raw ASCII double quotes inside double-quoted strings (e.g. use Hebrew gershayim ״ or single quotes for acronyms like מכ״ם, תנ״ך, צה״ל).
3. After both code blocks, a short plain-text summary showing card & question counts per category.

FOLLOW THIS YAML SHAPE:
id: deep_dive_topic_en
title: Deep Dive Topic
description: >
  An exhaustive, in-depth exploration covering every member and major milestone of the collection.
lang: en
audience: family
categories:
  - id: important_facts
    title: Important Facts
    description: >
      The complete chronological and biographical breakdown of all entities in the set.
    cards:
      - title: Entity One
        points:
          - "Deeply detailed, true historical fact #1."
          - "Deeply detailed, true historical fact #2."
          - "Deeply detailed, true historical fact #3."
          - "Deeply detailed, true historical fact #4."
      - title: Entity Two
        points:
          - "Deeply detailed, true historical fact #1."
          - "Deeply detailed, true historical fact #2."
          - "Deeply detailed, true historical fact #3."
          - "Deeply detailed, true historical fact #4."
    trivia:
      - type: multiple_choice
        question: "Which entity achieved this milestone first?"
        options: ["Entity One", "Entity Two", "Entity Three", "Entity Four"]
        correct: 0
      - type: single_qa
        question: "In what year was this key treaty signed?"
        answer: "1783"

SUMMARY FORMAT (plain text, AFTER the two code blocks):
  Topic: <title> — <N> categories — generated in English (_en) and Hebrew (_he)
  Then one line per category:
    - <category title> [<audience>] — <C> cards, <Q> questions
  Total questions per version: <sum>
```

---

### V3: Single-Subject Spotlight
Use for single landmarks, national parks, historical events, or focused subjects (e.g., Grand Canyon, Moon Landing, Titanic).

```text
You are an educational content creator for a family road-trip trivia app. For the topic
defined under "YOUR INPUT", produce a focused single-subject topic in BOTH English and Hebrew — two
strictly-formatted YAML datasets — followed by a short summary.

===== YOUR INPUT =====
TOPIC:            (REQUIRED — e.g., Yellowstone National Park, Apollo 11 Moon Landing)
EXTRA CATEGORIES: (4-6 thematic categories, e.g., Geography & Geology, History & Discovery, Wildlife, Surprising Quirks)
AUDIENCE:         (optional — "family" (default) or "adult")
NOTES:            (optional — any specific angles or details to cover)
======================

VOLUME & DEPTH REQUIREMENTS:
- Structure: 4 to 6 thematic categories breaking down the subject from multiple perspectives.
- Content: Each category has either flat bullet points (3-5 comprehensive facts per category) OR focused sub-theme cards (3-5 cards with 4 facts each).
- Trivia: At least 10 to 15 questions per category (mix of multiple_choice with 4 options and single_qa).
- Total questions: 40-70 questions total per language file.

WHAT TO OUTPUT:
1. An English YAML code block (lang: en, id: <slug>_en).
2. A Hebrew YAML code block — the SAME topic translated to Hebrew (lang: he, id: <slug>_he).
   - Keep all category/card IDs in English (snake_case).
   - Translate all visible text (titles, descriptions, points, questions, answers) into natural Hebrew.
   - HEBREW QUOTE RULE: Do NOT use raw ASCII double quotes inside double-quoted strings (e.g. use Hebrew gershayim ״ or single quotes for acronyms like מכ״ם, תנ״ך, צה״ל).
3. After both code blocks, a short plain-text summary showing card & question counts per category.

FOLLOW THIS YAML SHAPE (Flat Points Variant):
id: single_subject_en
title: Yellowstone National Park
description: >
  Explore the geothermal marvels, vast wildlife, and storied history of the world's first national park!
lang: en
audience: family
categories:
  - id: important_facts
    title: Important Facts
    description: >
      Core facts and iconic milestones about this incredible landmark.
    points:
      - "Established in 1872 by President Ulysses S. Grant, Yellowstone was the world's first national park."
      - "The park spans 3,472 square miles across Wyoming, Montana, and Idaho."
      - "It sits atop a massive supervolcano that powers over 500 active geysers, including Old Faithful."
      - "Yellowstone is home to the largest concentration of mammals in the lower 48 states, including bison and wolves."
    trivia:
      - type: multiple_choice
        question: "In what year was Yellowstone National Park established as the world's first national park?"
        options: ["1872", "1901", "1776", "1950"]
        correct: 0
      - type: single_qa
        question: "Which US president signed the law creating Yellowstone National Park?"
        answer: "Ulysses S. Grant"

SUMMARY FORMAT (plain text, AFTER the two code blocks):
  Topic: <title> — <N> categories — generated in English (_en) and Hebrew (_he)
  Then one line per category:
    - <category title> [<audience>] — <C> cards/points, <Q> questions
  Total questions per version: <sum>
```

---

## 3. Schema & Field Reference

| Field | Where | Type / Format | Rule |
| :--- | :--- | :--- | :--- |
| `id` | Topic | string | Snake case ending in `_en` or `_he` (e.g., `famous_inventions_discoveries_en`) |
| `title` | Topic | string | Clean title in topic's language |
| `description` | Topic | string | 2–4 engaging sentences introducing the topic |
| `lang` | Topic | `en` \| `he` | Language code |
| `audience` | Topic | `family` \| `adult` | Default: `family`. Set to `adult` only if unsuitable for kids. |
| `categories[]` | Topic | list | First category MUST be `id: important_facts`. |
| `categories[].id` | Category | string | English lowercase snake_case (same ID in both EN and HE files). |
| `categories[].title` | Category | string | Category display name. |
| `categories[].description` | Category | string | 1–3 sentence category introduction. |
| `categories[].audience` | Category | `family` \| `adult` | Optional override per category. |
| `cards[]` | Category | list | List of subcategory cards (OR flat `points[]`). |
| `cards[].title` | Card | string | Subcategory name (e.g., item, state, invention, person). |
| `cards[].points[]` | Card | list of strings | 4–5 true, educational, well-written facts. |
| `trivia[]` | Category | list | Generous list of questions (`multiple_choice` or `single_qa`). |
| `trivia[].type` | Trivia | `multiple_choice` \| `single_qa` | Question type. |
| `trivia[].question` | Trivia | string | Clear, engaging question. |
| `trivia[].options` | Trivia (MC) | list of 4 strings | Exactly 4 options. |
| `trivia[].correct` | Trivia (MC) | integer (0–3) | 0-based index of the correct option in `options`. |
| `trivia[].answer` | Trivia (QA) | string | Short, exact answer. |

---

## 4. Hebrew YAML Safety Checklist
When creating or editing Hebrew YAML files:
- Use Hebrew gershayim `״` (U+05F4) or single quotes `'` for Hebrew acronyms (e.g. `תנ״ך`, `מכ״ם`, `צה״ל`, `ארה״ב`) rather than ASCII double quotes `"` inside `"..."` strings to prevent YAML syntax errors.
- Keep all `id` values identical to the English version in ASCII lowercase snake_case.
- Keep the number and sequence of cards and trivia questions identical between English and Hebrew versions.
