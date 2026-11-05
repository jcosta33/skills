---
name: sitrep
description: Report where the work stands from live state. Use only when the user asks for status, an ETA, what is missing, or how far along the work is.
disable-model-invocation: true
---

# Sitrep

Report from artifacts (fresh git, GitHub, CI, test, and file state), not from memory or from a
claim that something is done. Essentials only:

- Done: merged or verified items, with PR or issue references.
- In flight: what is running now and who owns it.
- Missing: what remains before the goal is met, and any blocker.
- Promises: each earlier "I will", marked done, or dropped and why.
- ETA as a range, and one line on how this serves the broader goal.
