---
name: proper
description: Audit the change just made for shortcuts and unrequested scope, then fix the real cause. Use only when the user asks whether this was done properly or without hacks.
disable-model-invocation: true
---

# Proper

Judge the change from its diff, the commands run, and their output, never from the claim that it
is done.
Audit it for stubs, no-op paths, fallbacks that hide a failure, type escapes, suppressed lints or
tests, count-gaming, and symptom-only fixes.
Fix each at the owning layer following repository conventions; if a shortcut is genuinely right, say
why in one line.
List every change the user did not ask for, with `path:line`, marked keep (the request needs it) or
revert. Revert nothing until the user answers.
