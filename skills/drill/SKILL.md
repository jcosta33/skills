---
name: drill
description: Decide what a change is called, what it guarantees, where it lives, and its smallest write before writing code. Use when a change starts while its meaning, guarantee, or location is unsettled, or when implementation has begun without them. Do not use for a multi-stage migration that needs a staged plan with rollback.
---

# Drill

Before writing, lock in order: the name in the project's words, the obligation, the place, the slice.

- **Obligation.** What a caller can now rely on that they could not before, and what must stay true;
  how each is verified and rolled back.
- **Slice.** The smallest write that keeps the obligation. Find the existing rule and call it;
  duplicate only with a named reason, and proximity is not one. End each slice with **Done when**:
  the observable check that shows its obligation holds.
