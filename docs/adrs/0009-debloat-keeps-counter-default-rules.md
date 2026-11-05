---
type: adr
id: adr-0009
status: accepted
created: 2026-11-05
---

# ADR-0009 - debloat cuts default-following rules and keeps counter-default ones

## Context

Given an agent instruction file that mixed generic rules with rules opposing model defaults,
debloat merged or softened the counter-default rules. It scored below plain Opus.

## Decision

1. For agent instructions, debloat cuts each rule the model follows without being told and keeps
   the rules that oppose its defaults.
2. The no-loss check exempts the rules cut in that step.

## Rationale

- Coding agents follow rules that oppose their defaults less often than other rules, and generic
  overviews do not help. Those rules are the ones worth their tokens.
- debloat acts on supplied text and has no first pass to improve on. Its gate result holds whether
  the skill is used first or as a second pass.

## Evidence

- [evals/proposal-gate](../../evals/proposal-gate/README.md): 13.5 of 15 against 7.5 for the
  current skill and 10.5 for plain Opus, with controls clean.
- Sources: Harness-IF and Evaluating AGENTS.md in [docs/sources.md](../sources.md).
- [e03ea04](https://github.com/jcosta33/skills/commit/e03ea04).

## Status

Accepted (2026-11-05).
