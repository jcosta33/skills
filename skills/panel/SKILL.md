---
name: panel
description: Recommend one option after independent analyses of real alternatives. Use only when the user asks which option to pick, X or Y, or what you recommend between approaches for a consequential technical, product, or operational choice. Do not use when evidence already decides it or the user has stated a decision.
disable-model-invocation: true
---

# Panel

List the options, always including keeping the current behaviour, and name each recorded decision
(ADR, agent rule, past commit) that already bears on the choice. An option that reverses a recorded
decision is the owner's call: flag it, never recommend it.
Launch fresh subagents concurrently on the cheapest capable model; none sees another's analysis.
Answer in chat: recommendation first, a comparison table on shared criteria, the strongest surviving
dissent, and what would reverse the call. If the panel confirms an earlier recommendation, say so in
one line and stop.
