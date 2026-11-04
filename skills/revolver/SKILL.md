---
name: revolver
description: Review code, diffs, plans, or documents through a sequential rotation of fresh reviewers, one risk stance at a time, resolving every finding before the next reviewer. Use when work needs exhaustive scrutiny across every risk the target justifies. Do not use to check a single claim.
---

# Revolver

1. Freeze the target. Derive every materially distinct risk stance from requirements, trust
   boundaries, data and control flow, changed surfaces, failure modes, users, and operating
   conditions; no fixed count, no duplicates. Give each a falsification question and order them by
   consequence and uncertainty.
2. Dispatch one fresh reviewer at a time on the cheapest adequate model with the current target and
   one stance, never another reviewer's prose. Without fresh dispatch, stop; self-review is not
   fresh.
3. Reviewers return location, consequence, evidence, and minimal fix. Resolve every finding against
   direct evidence before the next stance: fix and verify what holds, reject what does not with the
   evidence, stop for the user on a human-owned choice, and name the missing evidence when it cannot
   be settled.
4. After a rotation that fixed something, rebuild the stances against the current target and rotate
   again. Stop after a quiet rotation or three.
5. Report fixes with their verification, consequential rejections, and open decisions. For each
   decisive run give the command, working directory, repository state, exit code, and the smallest
   decisive output excerpt.
