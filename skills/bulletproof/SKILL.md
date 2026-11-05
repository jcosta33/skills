---
name: bulletproof
description: Surface the assumptions and claims a piece of work rests on and verify each against direct evidence. Use only when the user asks are you sure, did you check, double-check this, or prove it. Do not use to trace how code flows or for broad risk review.
disable-model-invocation: true
---

# Bulletproof

List each claim the answer's conclusion rests on and each unstated assumption, then check each
against sources you open or commands you run. Return one table: item, `Supported` / `Unsupported` /
`Unverified` / `Blocked`, evidence. If code, a spec, or a primary document you opened decides an
item, mark it `Supported` or `Unsupported`; use `Unverified` or `Blocked` only when nothing reachable
here decides it, and name the exact gap. After the table, restate the answer with every
`Unsupported` item corrected.
