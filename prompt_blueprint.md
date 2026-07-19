# Topic Generator — Copy-Paste Prompt

You never write YAML by hand. To add a topic:

1. Copy the **locked prompt** in section 1.
2. Fill in **`TOPIC`** — that's the **only required field**. Everything else is optional:
   leave `SUBCATEGORIES` / `EXTRA CATEGORIES` blank and the model chooses them for you, or
   use the free-text `NOTES` line to steer it. **Don't change anything else.**
3. Paste into ChatGPT / Gemini / Claude → it replies with one YAML code block.
4. Save it as `topics/<topic_slug>.yaml`, run `python compiler.py`, follow any `→ Fix:`
   lines it prints, then commit + push.

**The model:** every topic gets a default **"Important Facts"** category made of **cards** —
one card per *subcategory* (e.g. one card per US state), each with a few bullet facts. The
model picks sensible subcategories from just the topic; you can optionally name them
yourself or add more theme categories (e.g. *Population*, *Economics*).

---

## 1. The locked prompt (copy everything in this block)

```text
You are an educational content creator for a family road-trip trivia app. Produce ONE
strictly-formatted YAML dataset for the topic defined under "YOUR INPUT". Output nothing
but the YAML code block.

===== YOUR INPUT =====
TOPIC:            (REQUIRED — the only field you must fill in. e.g. US States)
SUBCATEGORIES:    (optional — the items to make cards for. LEAVE BLANK and you choose a good set.)
EXTRA CATEGORIES: (optional — extra themes beyond "Important Facts". LEAVE BLANK and you decide.)
NOTES:            (optional — free-text guidance: focus, tone, how many items, difficulty,
                   LANGUAGE, etc. e.g. "write all titles, facts, and questions in Hebrew")
======================

HANDLING BLANK FIELDS
- TOPIC is the only required field.
- If SUBCATEGORIES is blank: choose a strong set of subcategories for the topic — about
  8-15, or the complete set if the topic clearly implies it (e.g. all US states). Honor NOTES.
- If EXTRA CATEGORIES is blank: keep just "Important Facts", OR add 1-2 genuinely useful
  theme categories if the topic clearly benefits (your judgment).
- Always honor anything written in NOTES.

STRUCTURE TO PRODUCE
- One topic: id (snake_case slug of TOPIC), title (the topic name), and a meaningful
  2-4 sentence description that introduces the topic — what it covers and why it is
  interesting (not just one line).
- Categories:
    * ALWAYS a first category "Important Facts" (id: important_facts).
    * PLUS one category for each theme in EXTRA CATEGORIES (or the ones you chose).
- Every category contains:
    * description: a meaningful 2-3 sentence introduction to this category (read first) —
      enough to set the stage before the cards, not just one line.
    * cards: ONE card per subcategory, in a sensible order. Each card has:
        - title: the subcategory name.
        - points: 4-5 short, true, self-contained fact sentences about that subcategory,
          written for THIS category's theme (under "Population" the facts are about
          population; under "Important Facts" the most interesting general facts).
    * trivia: a GENEROUS set that tests the material well — aim for about ONE question per
      card, and never fewer than 5 when the category has several cards. Spread the questions
      across different cards and facts. Each question is either:
        - multiple_choice: EXACTLY 4 options + correct = 0-based index (0, 1, 2, or 3), or
        - single_qa: a question + a short exact answer.

OUTPUT RULES (the compiler enforces these)
- Output ONLY one YAML code block — no text before or after. 2-space indentation.
  Straight quotes ("), never smart quotes.
- All ids are lowercase snake_case in ENGLISH/Latin letters only (e.g. important_facts),
  even when the visible title/text is in another language such as Hebrew. Facts must be
  accurate and family-friendly. Wrong multiple-choice options must be plausible but clearly
  incorrect. The visible text (titles, descriptions, points, questions, answers) may be in
  any language, and the app displays right-to-left languages like Hebrew automatically.

FOLLOW THIS SHAPE EXACTLY:
id: us_states
title: US States
description: >
  A state-by-state tour of the United States, from its biggest and most populous
  states to its smallest hidden gems. Each state has its own standout facts about its
  geography, history, and culture, and the trivia lets the whole family test what they
  just learned together.
categories:
  - id: important_facts
    title: Important Facts
    description: >
      The most surprising and memorable facts about each state — the kind of things that
      make everyone say "I didn't know that!" Read these aloud before starting the trivia
      round.
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
          - "Houston is home to NASA's Johnson Space Center and Mission Control."
          - "Texas produces more wind power than any other US state."
    trivia:
      - type: multiple_choice
        question: "Which of these states is the most populous?"
        options: ["Texas", "California", "Florida", "New York"]
        correct: 1
      - type: multiple_choice
        question: "Which state produces the most wind power in the US?"
        options: ["California", "Iowa", "Texas", "Oklahoma"]
        correct: 2
      - type: single_qa
        question: "Which state was once an independent republic before joining the US?"
        answer: "Texas"
      - type: single_qa
        question: "In which state would you find Death Valley, North America's lowest point?"
        answer: "California"
```

---

## 2. Notes

- **The only *required* field is `TOPIC`.** `SUBCATEGORIES`, `EXTRA CATEGORIES`, and
  `NOTES` are optional free text — leave them blank to let the model choose. Everything
  else in the prompt is fixed.
- **Another language?** Just ask in `NOTES` — e.g. *"write all titles, descriptions, facts,
  and questions in Hebrew."* Keep `TOPIC` and every `id` in English; the app displays
  right-to-left languages like Hebrew automatically.
- After saving the reply to `topics/<slug>.yaml`, run `python compiler.py`. It validates,
  auto-fixes safe issues (id casing, smart quotes, etc.), and prints plain-language
  `→ Fix:` lines for anything it can't fix. No debugging needed.
- **Long outputs get cut off — especially on free chat accounts** (they may split the reply
  into parts). Richer descriptions + more trivia make outputs longer, so:
    * keep each generation to a size that fits one reply — fewer subcategories per file, or
      generate one category theme at a time, and save each as its own topic file
      (e.g. `us_states_west.yaml`, `us_states_south.yaml`);
    * if the chat DOES split the reply, just paste the parts back-to-back in order — it's all
      one YAML file. Then run `python compiler.py`, which will flag anything that got mangled
      at the split.

## 3. Field reference (for manual tweaks)

| Field | Where | Rule |
| :--- | :--- | :--- |
| `id`, `title`, `description` | topic | slug + name + a 2–4 sentence intro |
| `categories[]` | topic | first is `important_facts`; extras optional |
| `categories[].description` | category | a 2–3 sentence intro (recommended) |
| `categories[].cards[]` | category | one card per subcategory *(a category has cards **or** flat `points`)* |
| `cards[].title` | card | the subcategory name |
| `cards[].points[]` | card | 1–6 bullet facts (aim for 4–5) |
| `categories[].points[]` | category | 2–5 facts — only for simple, non-card categories |
| `categories[].trivia[]` | category | several questions — about one per card, at least 5 for multi-card categories (`multiple_choice` needs 4 options + 0-based `correct`; `single_qa` needs `answer`) |

## 4. Variant — a simple single-subject topic

For one place/subject (e.g. Crater Lake) instead of a collection, skip cards: list your
themes as the categories and give each a flat `points` list (2–5 facts) plus `trivia`.
The compiler accepts either shape — cards or flat points.
