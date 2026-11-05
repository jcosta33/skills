---
name: drill
description: Before writing code for a new feature or change, decide its name in the project's words, what callers can rely on, where it belongs, and the smallest write that delivers it. Use only when the user asks to pin down something they want added, built, implemented, or wired up, or asks where it should live or what to call it. Do not use for a multi-stage migration that needs a staged plan with rollback.
disable-model-invocation: true
---

# Drill

Before writing, lock in order: the name in the project's words, the obligation, the place, the slice.

- **Obligation.** What a caller can now rely on that they could not before, and what must stay true;
  how each is verified and rolled back.
- **Slice.** The smallest write that keeps the obligation. Find the existing rule and call it;
  duplicate only with a named reason, and proximity is not one. End each slice with **Done when**:
  the observable check that shows its obligation holds.
