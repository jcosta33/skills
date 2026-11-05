---
type: adr
id: adr-0007
status: accepted
created: 2026-11-05
---

# ADR-0007 - Skills carry the plain procedure, never its name

## Context

Research mined philosophy, argumentation and psychology for moves that change model behaviour.
Draft skills named their provenance, such as disputatio, premortem and steelman.

## Decision

1. No SKILL.md names a philosopher, thinker, school or named method. Each ships the plain steps.
2. scripts/lint.sh rejects the vocabulary, and a mutation in scripts/test-lint.sh proves the rule
   fires.
3. Sources are credited in [docs/sources.md](../sources.md), the ADRs and
   [docs/research](../research/README.md).

## Rationale

- Expert personas do not move accuracy. Named heuristics describe expert behaviour without
  teaching it.
- What transfers is the procedure inside the method: replying to every objection, a test that can
  fail, an exhaustive division. The owner's rule is "the meat, not the veneer".

## Evidence

- [philosophy.md](../research/philosophy.md) (thesis and authoring rules).
- [philosophy-canon.md](../research/philosophy-canon.md).
- [08dda7f](https://github.com/jcosta33/skills/commit/08dda7f).

## Status

Accepted (2026-11-05).
