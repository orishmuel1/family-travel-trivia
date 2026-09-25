# AGENTS.md — Repository Master Guidelines & Agent Instructions

This document is the master instruction set and quality standard for AI agents (Antigravity) operating in the **Family Travel Trivia & Academy** repository. It serves as both a behavioral contract and a self-check rubric for topic generation, code maintenance, and user feedback triage.

---

## 1. The Living Document Protocol (CRITICAL RULE)

> [!IMPORTANT]
> **This file is an evolving living document.**
> As the user uses the application, provides feedback, or refines preferences during our sessions, these guidelines will continuously adapt and improve.

### The Mandatory Agent Workflow for `AGENTS.md`:
1. **Continuous Evaluation:** With *every* piece of user feedback, bug report, or interaction, the agent must evaluate: *"Does this reveal a new pattern, guideline, preference, or pitfall that belongs in `AGENTS.md`?"*
2. **Explicit User Approval Gate:** **The agent must NEVER modify or append to `AGENTS.md` autonomously.**
3. **How to Propose an Addition:** If the agent identifies something worth adding or updating, it must explicitly ask the user first:
   > *"I noticed from your feedback that [observation]. Would you like me to update `AGENTS.md` with a new guideline specifying that [proposed rule]?"*
4. **Execution:** Only upon the user's explicit confirmation may the agent update this file.

---

## 2. Core App Philosophy & Context

- **App Purpose:** An offline-first Progressive Web App (PWA) for family travel trivia and engineering-level academic learning.
- **Usage Model (Single-Reader):** One person holds the device (e.g. a passenger reading aloud in a moving car, or a parent at bedtime). Everyone else listens and answers out loud.
- **Zero-Internet Guarantee:** Must function 100% offline in dead zones, airplanes, and national parks. No backend server, no user logins, no external API dependencies at runtime.
- **Two Learning Modes:**
  1. **Travel Trivia Mode:** Narrative overview + structured subcategory fact cards, followed by comprehensive trivia reinforcement.
  2. **Academic Mode:** First-principles university courses designed for curious software engineers and lifelong learners, featuring intuitive math and interactive SVG diagrams.

---

## 3. Topic Authoring Guidelines (Plain Language & Standards)

Whenever generating or revising topics in `topics/` or `academic_topics/`, the agent must strictly adhere to these quality standards.

### A. Bilingual Parity (English & Hebrew)
1. **Dual Files:** Every topic must be created as a pair:
   - `topics/<slug>_en.yaml` (English version)
   - `topics/<slug>_he.yaml` (Hebrew version)
2. **Structural Mirroring:**
   - Both files must share identical `id` values for the topic, categories, and cards (all IDs must stay in English lowercase `snake_case`).
   - The number of categories, cards, and trivia questions must match 1:1.
3. **Natural Hebrew Phrasing:**
   - Never use literal or machine-translated Hebrew. The tone must be natural, engaging, and grammatically impeccable.
4. **The Hebrew Quote Rule (Crucial YAML Safety):**
   - In Hebrew YAML strings enclosed in double quotes `"..."`, **NEVER** use standard ASCII double quotes `"` inside the string.
   - For acronyms and quotes, use Hebrew gershayim `״` (e.g., `תנ״ך`, `צה״ל`, `מכ״ם`, `ארה״ב`, `דו״ח`) or single quotes `'`. Raw double quotes break the YAML parser.

---

### B. Topic & Category Structure
1. **First Category Rule:** The first category must **always** be `Important Facts` (`id: important_facts`).
2. **Extra Categories:** Include 2 to 4 thematic categories exploring intriguing angles of the subject.
3. **Cards per Category:** Provide **8 to 12 cards** per category (each card represents a distinct subcategory entity or milestone).
4. **Facts per Card:** Exactly **4 to 5 bullet points** per card.
   - Facts must be self-contained, factually verified, and narrative-driven.
   - Avoid dry one-sentence statistics. Explain the *context*, the *mechanism*, or the *surprising story* behind the fact.

---

### C. Trivia Question Quality & Standards
1. **Volume:** Each category must contain **15 to 20 multiple-choice questions** (totaling 60–100 questions per topic file).
2. **Question Format:**
   - 100% `type: multiple_choice`.
   - Exactly **4 options** per question.
   - `correct` is a 0-based integer index (`0`, `1`, `2`, or `3`).
   - Every question must include an `explanation` field that explains why the correct answer is true, adding fun context and reinforcing the learning cards.
3. **Semantic Homogeneity of Distractors (The Golden Rule):**
   - All 4 options **must belong to the exact same semantic class**.
   - *Example (Good):* If the answer is an Apollo astronaut (Neil Armstrong), all 3 distractors must be Apollo astronauts (Buzz Aldrin, Michael Collins, Alan Shepard).
   - *Example (Bad):* Mixing an astronaut with a rocket name, a year, and a politician.
   - Never include silly, obvious, or throwaway choices ("None of the above", completely unrelated words).
4. **Fairness & Difficulty:**
   - Avoid trick questions, semantic traps, or ambiguous wording.
   - Questions should be rewarding for someone who listened to the learning cards, yet plausible enough to make listeners think.

---

### D. Academic Course Standards (`academic_topics/`)
1. **Target Persona:** An intelligent developer/engineer without domain-specific background.
2. **First Principles:** Never introduce jargon or acronyms without immediately unpacking the physical or intuitive meaning (e.g., explaining convolution through sliding memory buffers).
3. **Visual Diagrams:** Provide clean, responsive inline SVG vector diagrams with proper `viewBox` coordinates for waveforms, block diagrams, or complex plane mappings.
4. **Mathematical Typography:** Use LaTeX-style delimiters (`$...$` for inline, `$$...$$` for block formulas) with plain-language explanations of each symbol.

---

## 4. Pre-Flight Self-Check Verification Checklist

Before reporting completion on any topic creation or modification, the agent **must verify every item on this checklist**:

- [ ] **Dual Files Present:** Are both `<slug>_en.yaml` and `<slug>_he.yaml` present and aligned?
- [ ] **English IDs Maintained:** Are all `id:` fields (topic, category, card) in English `snake_case` in both files?
- [ ] **Hebrew Quote Rule Respected:** Are all Hebrew acronyms using `״` or single quotes instead of ASCII `"`?
- [ ] **Volume Satisfied:** Does each category contain 8–12 cards with 4–5 bullets each?
- [ ] **Trivia Rules Met:** Does each category have 15–20 questions, each with 4 semantically matching options and an `explanation`?
- [ ] **Compiler Clean Run:** Has `./.venv/bin/python compiler.py` been executed and reported 0 errors?
- [ ] **Cache Busted:** Has `docs/data.json` and `docs/sw.js` been updated?

---

## 5. In-App User Feedback & GitHub Workflow

1. **Feedback Ingestion:**
   - In-app feedback submitted by users is stored offline in `localStorage` and can be synced to GitHub into `feedback/feedback_queue.json` (or submitted as GitHub issues).
2. **Reviewing Feedback on Session Start:**
   - When the user asks to review feedback or start a session, check `feedback/feedback_queue.json` (or inspect recent issues).
   - Categorize items: Content typos/fixes, new topic ideas, or UI bugs.
   - Propose direct fixes for content bugs immediately.
3. **Resolution & Archiving Lifecycle:**
   - Once a feedback item has been resolved and implemented:
   - Move the resolved item out of `feedback/feedback_queue.json` and append it into `feedback/archive.json`.
   - Add a `resolvedAt` timestamp and a brief `resolution` note (e.g., `"Fixed question #3 distractor in topics/crater_lake_en.yaml"`).
   - Keep `feedback/feedback_queue.json` clean so only unhandled items remain pending.
4. **Post-Fix Reflection:**
   - After resolving user feedback, check if the root cause suggests a new guideline to add to `AGENTS.md` (and ask the user before adding it).
