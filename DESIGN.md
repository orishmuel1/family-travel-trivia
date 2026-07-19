# Family Travel Trivia — Design & Intent

This is the source-of-truth for *why* this app exists and *how* it's meant to grow.
If any older note conflicts with this file, this file wins.

---

## 1. Purpose

A lasting **learn-then-test** tool for the family and for personal use — in the car,
at bedtime, anytime. It is **not** tied to one specific trip.

The loop is always the same:

1. **Learn** — read a short, well-structured briefing on a topic (a narrative plus
   bullet-point facts).
2. **Test** — answer trivia that reinforces what was just read, and turn it into a
   game everyone can play along with.

It should work with **zero internet** (remote National Parks, planes, dead zones),
because that's exactly when a family has time to learn together.

---

## 2. Who uses it (usage model)

**Single-reader model.** One person operates the app on one device (e.g. a passenger
reads aloud while someone drives); everyone else listens and answers out loud.

- ❌ No multiplayer, no accounts, no per-person scoreboards, no backend server.
- ✅ Casual, shared, offline, one screen.

---

## 3. Experience: Learning phase vs. Trivia phase

The app keeps a **firm split** between learning and testing.

```
Home
 └─ Topic  (e.g. "Crater Lake")
     └─ Category  (e.g. "Volcanic Origins", "Hydrology")
         ├─ LEARNING PHASE  → narrative description + bullet facts (cards)
         └─ TRIVIA PHASE    → run through ALL questions in the category,
                              running score, summary at the end
```

- Picking a category opens its **Learning** view first.
- A clear control switches that category (and optionally the whole topic) into
  **Trivia** mode.
- Trivia runs through **every** question in scope (not just the first one), keeps a
  running score, and shows a summary. Optionally a "whole-topic quiz" spans all
  categories.

---

## 4. Content pipeline (the heart of the project)

The person adding content must **never hand-write raw data or debug code**. The dev
workflow (`compile → commit → push`) is fine to run; *authoring* must be turnkey.

```
 ┌─────────────────────────────────────────────────────────────────────┐
 │ 1. PROMPT   Paste prompt_blueprint.md into ChatGPT/Gemini/Claude,    │
 │             filling in the topic + the categories you care about.    │
 │                                                                       │
 │ 2. GENERATE The chat returns one structured file in our schema        │
 │             (YAML preferred, JSON also accepted).                     │
 │                                                                       │
 │ 3. DROP     Save it as topics/<slug>.yaml (or .json).                 │
 │                                                                       │
 │ 4. VALIDATE Run the compiler. The validator reports EVERY problem at  │
 │             once, in plain language ("this failed because X → fix to  │
 │             Y"), and auto-fixes safe issues (reporting what it fixed).│
 │             You fix what it points to — no debugging.                 │
 │                                                                       │
 │ 5. COMPILE  When clean, it builds docs/data.json and cache-busts the  │
 │             service worker.                                           │
 │                                                                       │
 │ 6. PUBLISH  git commit + push → GitHub Pages serves the update;       │
 │             installed PWAs pull it in the background.                 │
 └─────────────────────────────────────────────────────────────────────┘
```

**Design principle:** chat output is unreliable, so the validator is forgiving where
it safely can be (auto-fix) and crystal-clear where it can't (actionable errors,
all reported together). Content quality is trusted; only *structure* is enforced.

*(A fully-automated "type a destination → get a topic" generator via the Claude API is
a possible future add-on, but is intentionally out of scope for now — the manual
read-and-interact-with-the-chat habit is a feature, not a chore to remove.)*

---

## 5. Data model

One file per **topic** under `topics/`. The hierarchy is **Topic → Category → (Cards) →
facts + Trivia**. A category holds **either** a `cards` list (a theme with one card per
*subcategory*, e.g. one card per US state) **or** a flat `points` list (a single subject).
Every topic gets a default **"Important Facts"** category; extra categories are optional.
See `schema_template.yaml` for the canonical template and `prompt_blueprint.md` for the
generator prompt.

```yaml
id: us_states                      # unique, lowercase snake_case slug
title: US States                   # display name
description: One-sentence overview of the topic.
categories:
  - id: important_facts            # default first category (theme)
    title: Important Facts
    description: One-sentence intro (optional).      # LEARNING intro
    cards:                         # LEARNING: one card per subcategory
      - title: California
        points:                    #   1–6 bullet facts (aim for 2–4)
          - "Self-contained, interesting fact."
          - "Another fact."
      - title: Texas
        points:
          - "A fact about Texas."
    trivia:                        # TRIVIA: 1+ questions (theme-level)
      - type: multiple_choice      #   4 options, 0-based correct index
        question: "…?"
        options: ["A", "B", "C", "D"]
        correct: 1
      - type: single_qa            #   direct question + answer
        question: "…?"
        answer: "…"

  # A category may instead use a flat points list (single-subject topics):
  #   - id: volcanic_origins
  #     title: Volcanic Origins
  #     description: A narrative paragraph.
  #     points: ["Fact one.", "Fact two."]   # 2–5 facts, used INSTEAD of cards
  #     trivia: [ ... ]
```

**Creation dates:** the compiler stamps each topic with a stable `created` date via a
committed ledger (`topics/.created.json`) so the app can sort by Newest/Oldest and the
dates stay consistent across every device.

---

## 6. Repository layout

```
topics/              Source content, one .yaml/.json per topic (FLAT — no subfolders)
compiler.py          Validate topics → build docs/data.json → cache-bust sw.js
prompt_blueprint.md  Copy-paste generator prompt for the chat
schema_template.yaml Canonical schema reference
docs/                The PWA (GitHub Pages target)
  index.html         Single-page app shell (learning + trivia UI)
  data.json          Compiled database (generated — do not hand-edit)
  sw.js              Service worker (offline cache; version stamped by compiler)
  manifest.json      PWA manifest
  icon-192/512.png   Launcher icons
tools/               Helper scripts (clean, bump_version, generate_mock_icons)
```

---

## 7. Roadmap

- **Phase 1 — Content pipeline & correctness (in progress):** robust validator
  (YAML+JSON, all-errors-at-once, auto-fix, single-file check), fix Windows/compiler
  crashes, refine the generator prompt.
- **Phase 2 — Learning/Trivia UX:** rebuild the app around the phase split; trivia runs
  all questions with score + summary; forgiving Q&A answer matching.
- **Phase 3 — Offline & install hardening:** cache-first service worker, iOS install
  support, robust offline load.
- **Phase 4 — Engineering quality:** tests for the validator, GitHub Actions CI,
  versioning.

## 8. Non-goals

Multiplayer / accounts · a backend server · trip-specific one-offs · automating away
the human's learning-in-the-chat step.
