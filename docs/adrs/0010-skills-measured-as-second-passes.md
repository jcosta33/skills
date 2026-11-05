---
type: adr
id: adr-0010
status: accepted
created: 2026-11-05
---

# ADR-0010 - Skills are measured as on-demand second passes

## Context

The proposal gate measured first-pass behaviour, giving each item to a fresh agent as its only
message. The owner fires bulletproof, panel, dissect, revolver and settle after judging an answer
to need another look. A first-pass ceiling therefore says nothing about real use.

## Decision

1. A skill whose real use is a follow-up is measured as one. A plain Opus first pass on a hard task
   is followed, in the same session, by no follow-up, by "Check this again.", or by the skill.
2. Items are natural failures labelled by a blind grader against keys written before the runs.
   Flaws are never planted.
3. The measures are fixes on flawed answers, churn or flips on correct ones, tokens and wall time.
4. The owner's five core skills (bulletproof, panel, dissect, revolver and settle) stay. They are
   measured, not retired. Where one loses to "check again", the cause is found and one fix arm is
   tested.
5. Gate verdicts from first-pass runs on these skills are provisional, not rejections.

## Rationale

- The arm that matters is the one the owner would otherwise type: a bare "check again". A skill
  earns its place by fixing more, or disturbing less, than that.

## Evidence

- Limitation recorded in [evals/proposal-gate](../../evals/proposal-gate/README.md)
  ([3aee6be](https://github.com/jcosta33/skills/commit/3aee6be)).
- Method and results: [evals/second-pass](../../evals/second-pass/README.md)
  ([3900f80](https://github.com/jcosta33/skills/commit/3900f80)).

## Status

Accepted (2026-11-05).
