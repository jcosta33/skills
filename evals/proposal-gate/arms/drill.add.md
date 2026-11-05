# Drill

Before locking anything, list:

- each reading of the request that would produce different behaviour;
- the facts outside the code each requirement depends on, checked against their source;
- where each term of the change gets its meaning in this project.

Then lock in order: the name in the project's words, the obligation, the place, the slice.

- **Obligation.** What a caller can now rely on that they could not before, and what must stay true;
  how each is verified and rolled back.
- **Slice.** The smallest write that keeps the obligation. Find the existing rule and call it;
  duplicate only with a named reason, and proximity is not one. End each slice with **Done when**:
  the observable check that shows its obligation holds.
