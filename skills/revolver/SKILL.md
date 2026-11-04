---
name: revolver
description: Review code, diffs, plans, or documents with fresh independent reviewers, then fix what survives verification. Use when work needs scrutiny from someone other than its author, fast or exhaustive. Do not use to check a single claim.
---

# Revolver

- Reviewers are fresh subagents given the frozen target and one brief, never the author's reasoning
  or another reviewer's prose.
- Fast, the default: three top-tier reviewers in parallel, each attacking the whole target.
- Exhaustive, when asked: derive every materially distinct risk stance from the target and run one
  cheap reviewer per stance in sequence, each on the latest fixed version. Rotate again after any
  round that fixed something; stop after a quiet rotation or three.
