---
type: adr
id: adr-0002
status: accepted
created: 2026-11-05
---

# ADR-0002 - Delete promote, remember and triple-check

## Context

- promote moved a transient artifact into project ownership. remember preserved one verified
  lesson; it was merged into promote in the first cut.
- triple-check ran three concurrent top-tier reviews; it was merged into revolver as a fast mode.

## Decision

1. promote leaves the catalog, and remember goes with it.
2. triple-check leaves the catalog. revolver keeps only its sequential method; there is no fast
   mode.

## Rationale

- Both removals were owner corrections to the first cut. Neither commit records a further test or
  reason for removing them.
- In the first-cut test, the bare model stripped secrets from the note unaided. The skill text
  added two things: choosing an existing home, and asking before committing.
- revolver's method is one fresh reviewer at a time on the latest fixed version. A parallel mode is
  a different method, and the owner kept the sequential one.

## Evidence

- [c3d4b25](https://github.com/jcosta33/skills/commit/c3d4b25) (merges, and the promote test) and [2315dfc](https://github.com/jcosta33/skills/commit/2315dfc) (owner
  corrections).

## Status

Accepted (2026-11-05).
