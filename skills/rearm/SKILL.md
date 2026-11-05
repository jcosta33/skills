---
name: rearm
description: Refresh rules and working state, then resume the current task. Use only when the user asks to re-read the rules or get back up to speed.
disable-model-invocation: true
---

# Rearm

Fetch, then re-read latest main's agent instructions (AGENTS.md or its equivalent), the skills and
goal or campaign file they name for this work, and any brief path the user named.
Read the current branch's commits and uncommitted changes against its base, plus what changed on
main that touches it.
Restate every decision in force for this work as one full list, each with its source.
Before editing inherited work, say where one likely change would go and why, then check that
against the code.
State in one line each rule you were not following and the next step, then continue.
