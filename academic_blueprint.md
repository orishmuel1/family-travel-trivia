# Academic Topics Generator Blueprint & Master Pedagogy Guide

This document defines how academic topics and university-level courses are created, structured, and validated for the application's **Academic Mode**.

---

## 1. Core Pedagogical Philosophy ("First-Principles for Engineers")

Every academic topic in this application must bridge the gap between **rigorous university concepts** and **crystal-clear engineering intuition**. The goal is that any general software engineer, computer science graduate, or curious developer can understand the material deeply without needing prior domain-specific expertise.

### Key Teaching Rules:
1. **Build from First Principles**:
   - Start from fundamentals every engineer understands: time steps, memory buffers, arrays, clocks, physical waves, frequencies, and code loops.
   - Avoid throwing raw jargon without context. When introducing terms like *LTI*, *Convolution*, *Z-Transform*, *Poles/Zeros*, *ROC*, *Aliasing*, or *Butterfly Operation*, immediately define **what it actually is physically/computationally**, **how it works**, and **why an engineer cares**.
2. **Tell the Story Behind the Math**:
   - Long, rich cards are encouraged! Do not compress or rush explanations into cryptic formulas. Take the space needed to explain the physical intuition, the practical trade-offs, and real-world applications (e.g., Spotify equalizers, Shazam audio fingerprinting, Wi-Fi modems, noise cancellation, MRI scans).
3. **Formulas as Clear Mathematical Language**:
   - Formulas should illuminate the narrative rather than overwhelm it. Always provide plain-language commentary for each equation: explain what each variable ($n, k, \omega, z, T_s$) represents in reality.
4. **Visual Diagrams & Plots (SVG Figures)**:
   - Include clear, clean vector SVG diagrams and plots for architectural flowcharts, geometric mappings (e.g. pole-zero plots on the complex plane), time-vs-frequency waveforms, and algorithm signal-flow graphs.
5. **Multiple-Choice Conceptual Testing**:
   - All questions must be 4-option `multiple_choice`. Questions should test conceptual understanding, "why" mechanisms, edge cases, and engineering trade-offs.

---

## 2. Generation Workflows

### Option A: In-Session via Antigravity (Recommended)
You can ask Antigravity directly in this chat to create or update any academic topic:
```text
Generate a new academic topic:
- COURSE / TOPIC: [e.g., Digital Signal Processing (DSP 101), Linear Algebra for ML, Computer Architecture 101]
- SYLLABUS / LESSONS: [List 4-6 curriculum modules, or leave blank to auto-curate]
- ICON: [e.g., 📡, 🔬, 📈, 🧠, ⚡, 📐]
- AUDIENCE: [family (default) or adult]
- FOCUS: [Specific engineering focus, key algorithms, figures]
```

---

### Option B: External LLM Copy-Paste Prompt (ChatGPT / Claude / Gemini Web)
Copy the code block below, fill in `YOUR INPUT`, paste into the LLM, and save the resulting files into `academic_topics/<slug>_en.yaml` and `academic_topics/<slug>_he.yaml`.

```text
You are an award-winning university professor and master engineering educator. For the academic course
defined under "YOUR INPUT", produce a complete, rigorous, and deeply intuitive curriculum
in BOTH English and Hebrew — two strictly-formatted YAML datasets — followed by a short summary.

===== YOUR INPUT =====
COURSE / TOPIC:   (REQUIRED — e.g., Digital Signal Processing, Computer Architecture, Machine Learning Math)
SYLLABUS/LESSONS: (optional — 4 to 6 curriculum modules. LEAVE BLANK and decide based on top university syllabi)
ICON:             (optional — a relevant emoji icon, e.g. 📡, 🔬, ⚛️, 📈, 🧠, 💻)
AUDIENCE:         (optional — "family" (default) or "adult")
NOTES:            (optional — specific focus, must-include theorems, figures, or formulas)
======================

PEDAGOGICAL REQUIREMENTS:
1. Audience: An intelligent software/hardware engineer who does NOT have prior specialized background in this specific field.
2. First-Principles Explanation: Explain every term from the ground up. Whenever introducing a technical term or acronym (e.g., LTI, Z-transform, ROC, BIBO, Aliasing, FIR/IIR, FFT), immediately explain what it physically means in plain English/Hebrew before stating the math.
3. Rich Storytelling: Use comprehensive, well-structured cards. Take the space to explain the physical intuition, mathematical reasoning, and practical engineering trade-offs.
4. Embedded SVG Figures: Include responsive, clean SVG vector diagrams (`svg: > ...`) illustrating key physical waveforms, geometric maps, block diagrams, or signal flow graphs.
5. Multiple-Choice Only Quizzes:
   - Provide AT LEAST 15 MULTIPLE CHOICE questions per lesson module (75-100 questions per course).
   - ALL questions must be type: multiple_choice with EXACTLY 4 options and a 0-based 'correct' index (0, 1, 2, or 3).
   - Questions should test conceptual understanding, real-world trade-offs, and core theorems.

WHAT TO OUTPUT:
1. English YAML block (`lang: en`, `id: <slug>_en`).
2. Hebrew YAML block (`lang: he`, `id: <slug>_he`):
   - Keep category IDs in English (snake_case).
   - Translate all explanations, formulas context, and questions into natural, rigorous academic Hebrew.
   - HEBREW QUOTES RULE: Do NOT use raw ASCII double quotes inside double-quoted strings (use Hebrew gershayim ״ or single quotes for acronyms like מכ״ם, תנ״ך, LTI).
3. Plain-text summary showing lesson card & question counts.

YAML SCHEMA STRUCTURE:
id: dsp_101_en
type: academic
icon: "📡"
title: "Digital Signal Processing (DSP 101)"
description: >
  Course description summarizing curriculum roadmap.
lang: en
audience: family
categories:
  - id: module_1_id
    title: "1. Module Title"
    description: >
      Module overview.
    cards:
      - title: "Subtopic Title"
        figure:
          title: "Figure Caption Title"
          svg: >
            <svg viewBox="0 0 500 160" xmlns="http://www.w3.org/2000/svg">...</svg>
          caption: "Detailed figure caption."
        points:
          - "Detailed point 1 breaking down the concept from first principles..."
          - "Detailed point 2 explaining the formula $y[n] = ...$ in plain words..."
    trivia:
      - type: multiple_choice
        question: "Clear conceptual question?"
        options:
          - "Correct option"
          - "Distractor 1"
          - "Distractor 2"
          - "Distractor 3"
        correct: 0
```

---

## 3. Schema & Field Reference

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
| `cards[].figure` | Card | object (optional)| `title`, `svg` (clean vector XML), and `caption` |
| `cards[].points[]` | Card | list of strings | Rich, intuitive bullet points explaining concepts from first principles |
| `trivia[]` | Lesson | list | Multiple-choice questions testing conceptual mastery |
| `trivia[].type` | Trivia | `multiple_choice` | MUST be `multiple_choice` (no `single_qa`) |
| `trivia[].question` | Trivia | string | Clear multiple-choice question |
| `trivia[].options` | Trivia | list of 4 strings | Exactly 4 options |
| `trivia[].correct` | Trivia | integer (0–3) | 0-based index of the correct answer |
