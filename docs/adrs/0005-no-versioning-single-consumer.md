---
type: adr
id: adr-0005
status: accepted
created: 2026-11-05
---

# ADR-0005 - No versioning; one consumer

## Context

The catalog carried VERSION, CHANGELOG.md, a released-changelog gate, and release, pinning and
cutover rules. Its one consumer is the owner, who installs from main.

## Decision

1. There is no version number, changelog, tag or release.
2. Git history is the record. Commit messages carry the witnessed failure and the with/without
   result, and ADRs carry the decisions.
3. Changes are committed and pushed to main.

## Rationale

- Versioning serves consumers who pin and migrate. With one consumer installing from main, it adds
  gates and bookkeeping and protects no one.

## Evidence

- [2315dfc](https://github.com/jcosta33/skills/commit/2315dfc).

## Status

Accepted (2026-11-05).
