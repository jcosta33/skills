---
type: adr
id: adr-0008
status: accepted
created: 2026-11-05
---

# ADR-0008 - Method-skill descriptions use the user's words, gated by a trigger eval

## Context

The method skills under-triggered. On should-trigger queries the old descriptions fired in 33%
(drill), 43% (revolver), 63% (bulletproof), 77% (dissect) and 90% (panel) of runs. The model mostly
went straight to Bash or Read.

## Decision

1. Descriptions for drill, dissect, bulletproof, revolver and panel lead with the user's own
   phrasing, add an "even when" clause, and keep the nearest exclusion.
2. Every description change passes the trigger eval in AGENTS.md: about 20 queries, half near
   misses, 3 runs each, 0.5 threshold. The new description ships only if it passes more queries
   with no new false trigger.

## Rationale

- The description is the only text a model sees before it decides to load a skill. Phrasing that
  matches how the user asks is what moves the decision.

## Evidence

- [evals/trigger](../../evals/trigger/README.md). Should-trigger rates rose to 90%, 100%, 80%, 90%
  and 100%, and near misses passed 10/10 in every arm.
- [2ce1ab0](https://github.com/jcosta33/skills/commit/2ce1ab0).

## Status

Accepted (2026-11-05).
