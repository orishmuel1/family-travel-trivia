# Academic Topics Generator Blueprint & Templates

This document defines how academic topics and university-level courses are generated, structured, and validated for the application's **Academic Mode**.

---

## 1. Generation Workflows

### Option A: In-Session via Antigravity (Recommended)
You can ask Antigravity directly in this chat to generate, expand, or update any academic topic:
```text
Generate a new academic topic:
- COURSE / TOPIC: [e.g., Digital Signal Processing (DSP 101), Microeconomics 101, Organic Chemistry I]
- SYLLABUS / LESSONS: [List 4-6 curriculum modules/lessons, or leave blank to auto-curate]
- ICON: [e.g., 📡, 🔬, 📈, 🧠, ⚡, 📐]
- AUDIENCE: [family (default) or adult]
- NOTES: [Key formulas to include, diagrams, specific pedagogical focus]
```
Antigravity will automatically:
1. Write both `academic_topics/<slug>_en.yaml` and `academic_topics/<slug>_he.yaml`.
2. Ensure university-level rigor explained with crystal-clear intuition, formulas, figures, and rich multiple-choice questions.
3. Validate and compile via `./.venv/bin/python compiler.py`.
4. Stage and commit updates to git.

---

### Option B: External LLM Copy-Paste Prompt (ChatGPT / Claude / Gemini Web)
Copy the entire code box below, fill in the `YOUR INPUT` section, paste into the LLM, and save the outputs as `academic_topics/<slug>_en.yaml` and `academic_topics/<slug>_he.yaml`.

```text
You are an expert university professor and master educator. For the academic course
defined under "YOUR INPUT", produce a complete, rigorous, yet intuitively explained curriculum
in BOTH English and Hebrew — two strictly-formatted YAML datasets — followed by a short summary.

===== YOUR INPUT =====
COURSE / TOPIC:   (REQUIRED — e.g., Digital Signal Processing, Linear Algebra, Macroeconomics)
SYLLABUS/LESSONS: (optional — 4 to 6 curriculum modules. LEAVE BLANK and decide based on top university syllabi)
ICON:             (optional — a relevant emoji icon, e.g. 📡, 🔬, ⚛️, 📈, 🧠)
AUDIENCE:         (optional — "family" (default) or "adult")
NOTES:            (optional — specific focus, must-include theorems or formulas)
======================

PEDAGOGICAL & STRUCTURAL REQUIREMENTS:
1. Academic Concept: Structured as a university curriculum. Categories represent LESSONS / MODULES.
2. Conceptual Depth with Clear Intuition: Break down complex math, physics, engineering, or theory into clear, digestible principles. Explain *why* things work before diving into the formulas.
3. Flexible Cards & Points: Each Lesson category contains 3 to 6 subtopic cards. Each card can have ANY number of bullet points needed to thoroughly teach the concept (typically 3 to 8 comprehensive bullet points per card).
4. Formulas & Figures:
   - Use clean LaTeX / mathematical notation (e.g. $X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}$, $e^{j\omega}$, $f_s \ge 2 f_{\max}$) or clear ASCII/unicode math where relevant.
   - You can include inline figures/ASCII diagrams or descriptive visual blocks where diagrams enhance understanding.
5. Multiple-Choice Only Questions:
   - Provide AT LEAST 15 to 25 MULTIPLE CHOICE questions per lesson category.
   - ALL questions must be type: multiple_choice with EXACTLY 4 options and a 0-based 'correct' index (0, 1, 2, or 3).
   - Questions should test conceptual understanding, formula applications, edge cases, and core theorems.
   - Total questions per topic: 75-120 questions per language file.

WHAT TO OUTPUT:
1. An English YAML code block (lang: en, id: <slug>_en).
2. A Hebrew YAML code block — the SAME topic translated to Hebrew (lang: he, id: <slug>_he).
   - Keep all category IDs in English (snake_case).
   - Translate all pedagogical content, formulas context, questions, and options into natural, academic Hebrew.
   - HEBREW QUOTE RULE: Do NOT use raw ASCII double quotes inside double-quoted strings (use Hebrew gershayim ״ or single quotes for acronyms like מכ״ם, תנ״ך, צה״ל, LTI -> מערכות LTI).
3. After both code blocks, a short plain-text summary showing lesson card & question counts.

FOLLOW THIS YAML SHAPE:
id: dsp_101_en
type: academic
icon: "📡"
title: Digital Signal Processing (DSP 101)
description: >
  A comprehensive university-level introduction to discrete-time signals, LTI systems, transforms, and digital filter design.
lang: en
audience: family
categories:
  - id: discrete_time_foundations
    title: Foundations & Discrete-Time Systems
    description: >
      Study the foundational mathematics of discrete-time signals, linearity, time-invariance, convolution, and difference equations.
    cards:
      - title: Continuous-Time vs. Discrete-Time Signals
        points:
          - "A continuous-time signal $x(t)$ is defined for all real numbers $t$, whereas a discrete-time signal $x[n]$ is defined only at integer values of index $n$."
          - "Sampling a continuous signal at uniform intervals $T_s$ generates the discrete sequence $x[n] = x(n T_s)$, where $f_s = 1/T_s$ is the sampling frequency."
          - "Fundamental discrete-time signals include the unit impulse $\\delta[n]$ (1 at $n=0$, 0 elsewhere) and the unit step $u[n]$ (1 for $n \\ge 0$, 0 for $n < 0$)."
      - title: Linear Time-Invariant (LTI) Systems & Convolution
        points:
          - "An LTI system satisfies both linearity (superposition and scaling) and time-invariance (a shift in input produces an identical shift in output)."
          - "The behavior of any discrete LTI system is completely characterized by its impulse response $h[n]$."
          - "The output $y[n]$ is computed via the discrete convolution sum: $y[n] = (x * h)[n] = \\sum_{k=-\\infty}^{\\infty} x[k] h[n-k]$."
    trivia:
      - type: multiple_choice
        question: "What is the primary condition for a discrete-time system to be completely characterized by its impulse response?"
        options:
          - "The system must be Linear and Time-Invariant (LTI)"
          - "The system must be memoryless"
          - "The input must be strictly periodic"
          - "The sampling rate must be infinite"
        correct: 0
      - type: multiple_choice
        question: "What is the value of the unit impulse function $\\delta[n]$ at $n = 0$?"
        options:
          - "1"
          - "0"
          - "Infinity"
          - "Undefined"
        correct: 0

SUMMARY FORMAT (plain text, AFTER the two code blocks):
  Course: <title> — <N> Lessons — generated in English (_en) and Hebrew (_he)
  Then one line per lesson:
    - Lesson <#>: <lesson title> — <C> cards, <Q> questions
  Total multiple-choice questions per version: <sum>
```

---

## 2. Schema & Field Reference

| Field | Where | Type / Format | Rule |
| :--- | :--- | :--- | :--- |
| `id` | Topic | string | Snake case ending in `_en` or `_he` (e.g. `dsp_101_en`) |
| `type` | Topic | string | MUST be `academic` |
| `icon` | Topic | string | Emoji icon (e.g. `📡`, `🔬`, `📐`, `💻`) |
| `title` | Topic | string | Academic course title |
| `description` | Topic | string | 2–3 sentences summarizing course syllabus and objectives |
| `lang` | Topic | `en` \| `he` | Language code |
| `audience` | Topic | `family` \| `adult` | Default: `family` |
| `categories[]` | Topic | list | Each category is a curriculum Lesson / Module |
| `categories[].id` | Lesson | string | English lowercase snake_case (matching across EN/HE) |
| `categories[].title` | Lesson | string | Lesson / Module title |
| `categories[].description` | Lesson | string | Overview of the lesson module |
| `cards[]` | Lesson | list | Subtopics within the lesson |
| `cards[].title` | Card | string | Subtopic title |
| `cards[].points[]` | Card | list of strings | Flexible number of detailed, intuitive pedagogical facts & formulas |
| `trivia[]` | Lesson | list | Multiple-choice questions testing conceptual mastery |
| `trivia[].type` | Trivia | `multiple_choice` | MUST be `multiple_choice` (no `single_qa`) |
| `trivia[].question` | Trivia | string | Clear multiple-choice question |
| `trivia[].options` | Trivia | list of 4 strings | Exactly 4 options |
| `trivia[].correct` | Trivia | integer (0–3) | 0-based index of the correct answer |
