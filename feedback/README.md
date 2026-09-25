# In-App Feedback & Bug Reports

This folder holds incoming user feedback, content bug reports, and feature ideas submitted directly from the Family Travel Trivia PWA application.

## How it works

1. **In the App:** Users click the floating feedback button (or use the menu) on any screen.
2. **Context Captured:** The app records the sentiment (positive/negative), multiple-choice tags (e.g., Typo, Factual Error, Confusing Question), free-text notes, and automatically attaches the current Topic, Category, Question/Fact details, and timestamp.
3. **Offline-First:** All feedback is stored locally in the browser's `localStorage`.
4. **Option B (GitHub Sync):** When internet is available, tapping **Sync to GitHub** pushes the feedback entries directly to `feedback/feedback_queue.json` in this repository via the GitHub API (or creates a GitHub issue).
5. **Agent Triage:** Every time Antigravity reviews feedback, it parses `feedback/feedback_queue.json`, implements fixes for the user, and evaluates if any lesson learned should be proposed for addition to `AGENTS.md`.
