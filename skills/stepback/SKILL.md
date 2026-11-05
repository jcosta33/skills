---
name: stepback
description: Question whether the current approach should exist before continuing it. Use only when the user asks to step back or questions the premise.
disable-model-invocation: true
---

# Step back

Stop the current approach. State the goal it serves in one line.
Answer with code or repository evidence: does this need to exist? What breaks if we skip it? Is
there a deeper cause we are patching around?
Recommend skip, simplify, or proceed. If simplify, treat the attempt as a throwaway draft, rebuild
it the simplest correct way using what we learned, and rerun the same checks.
