---
type: adr
id: adr-0003
status: accepted
created: 2026-11-05
---

# ADR-0003 - dissect stays distinct from bulletproof

## Context

The first cut merged dissect into bulletproof, because both demand direct evidence over recall.

## Decision

1. dissect is its own skill. It traces one code path to closure: entries, callers including dynamic
   dispatch, branches, and effects, with a `path:line` edge table and `Unknown` rows.
2. bulletproof surfaces and verifies the claims and assumptions a piece of work rests on. The
   code-tracing lines moved out of it.
3. Each description excludes the other's job.

## Rationale

- The two answer different questions. "Is this claim true?" ends in a verdict per claim. "What
  reaches this code?" ends in a proven flow, and a negative claim needs the search command and its
  result.
- In the round-2 bare-model test, the one-liner described its searches in prose with no edge
  table. The skill text produced the table and the Unknown column.

## Evidence

- [2315dfc](https://github.com/jcosta33/skills/commit/2315dfc).
- Second-pass results for both skills: [evals/second-pass](../../evals/second-pass/README.md).

## Status

Accepted (2026-11-05).
