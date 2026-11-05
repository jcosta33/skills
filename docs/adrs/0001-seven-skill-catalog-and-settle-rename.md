---
type: adr
id: adr-0001
status: accepted
created: 2026-11-05
---

# ADR-0001 - Cut the catalog to seven skills; ask-user becomes settle

## Context

The catalog held twelve skills: ask-user, bulletproof, debloat, demolition, dissect, drill, panel,
promote, remember, revolver, settle and triple-check. Several overlapped, and some lines restated
what a frontier model already does unprompted.

## Decision

1. The catalog is seven skills: bulletproof, debloat, dissect, drill, panel, revolver and settle.
2. The old settle merged into ask-user. The merged skill is then renamed settle, and its
   description leads with resolving ambiguity by evidence. Asking the user is the exception.
3. demolition is cut.
4. The design docs collapse into AGENTS.md, README.md and docs/sources.md. scripts/lint.sh and
   scripts/test-lint.sh replace the old gates.

## Rationale

- A skill line stays only if it makes a fresh model do something it does not do from a one-line
  instruction.
- "ask-user" named the exception, not the job. Most ambiguity is settled from code, tests,
  precedent or docs, and only the remainder goes to the user as a structured choice.

## Evidence

- Bare-model tests, one real task per skill. Criteria were written before the runs; one-line
  instruction against skill text. Recorded in [c3d4b25](https://github.com/jcosta33/skills/commit/c3d4b25) and [2315dfc](https://github.com/jcosta33/skills/commit/2315dfc).
- Proposal: [skills-shape.md](../research/skills-shape.md).

## Status

Accepted (2026-11-05).
