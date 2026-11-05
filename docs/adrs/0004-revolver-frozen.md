---
type: adr
id: adr-0004
status: accepted
created: 2026-11-05
---

# ADR-0004 - revolver is conceptually frozen

## Context

revolver reviews through a rotation of fresh reviewers, one risk stance at a time. Every finding is
resolved before the next reviewer starts. Research passes proposed changes to it, among them an
input rule that strips PR text and earlier verdicts from reviewer briefs.

## Decision

1. revolver's method does not change. Stances come from the target. One fresh reviewer at a time
   works on the latest fixed version. Each finding is resolved first, and the pool is rebuilt after
   a productive rotation. The run stops after a quiet rotation or three.
2. Evals report findings on revolver only. They propose no text for it.
3. Its description changed once, through the trigger eval (ADR-0008).

## Rationale

- The owner ruled the method conceptually untouchable.
- The evals found no failure the method itself causes. In the second-pass eval it ties "check
  again" on fixes and disturbs correct reviews less, at higher cost.

## Evidence

- Owner corrections in [2315dfc](https://github.com/jcosta33/skills/commit/2315dfc). Proposal tables in
  [philosophy.md](../research/philosophy.md) and [engineering-meaning.md](../research/engineering-meaning.md) §9.
- Findings: [evals/second-pass](../../evals/second-pass/README.md).
- Description change: [2ce1ab0](https://github.com/jcosta33/skills/commit/2ce1ab0).

## Status

Accepted (2026-11-05).
