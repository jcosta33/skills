---
type: adr
id: adr-0012
status: accepted
created: 2026-11-05
---

# ADR-0012 - wdyt judges an idea the user proposes

## Context

wdyt was written to think a question through to one verdict. The owner clarified its job: it
judges an idea he proposes, not the agent's own output. Its main risk is agreeing because the idea
is his. Contrarianism toward a sound idea is the opposite failure.

## Decision

The body is the ten steps below plus a Done-when line. The description names the user's own idea
and excludes re-checking the agent's earlier answer. The skill stays user-invoked.

| Line | Rule | Grounding |
| --- | --- | --- |
| 1 | Restate the strongest form without the user's preference; judge it as a stranger's | Regenerating context without the asker's opinion (System 2 Attention); models bend toward the asker's view (Sharma et al.) |
| 2 | List and check what the proposal takes for granted | Presupposition accommodation (Lewis, "Scorekeeping"); faulty-premise code generation (FPBench) |
| 3 | Decide facts by opening a source or running a command | Matters of fact need observation; self-correction works with external tools (CRITIC) |
| 4 | Exhaustive alternatives, including the current approach and doing nothing, plus one outside the shared premise | Exhaustive division; reflective judgment finds the category; LLM and human options barely overlap (Kostiuk et al.); model outputs converge (Artificial Hivemind) |
| 5 | Five practical-reasoning questions | Critical questions for practical reasoning (Walton; critical-questions shared task) |
| 6 | Assume it was adopted and failed | Anticipatory reflection before acting (Wang et al., Findings of EMNLP 2024) |
| 7 | Answer every objection; test the shared premise when both sides hold | The reply-to-every-objection procedure; testing the premise shared by two sound-looking sides |
| 8 | More evidence the less reversible the change | Burden of proof scaled to the cost of error |
| 9 | Adopt as stated unless an unanswered objection requires a change | Second-pass churn on correct answers ([evals/second-pass](../../evals/second-pass/README.md)); case-for-and-against explanations lowered accuracy on right answers from 0.87 to 0.73 (Si et al., NAACL 2024) |
| 10 | Short argument with a numeric confidence; change only for a new fact or argument | longer explanations raised readers' confidence without improving discrimination (Steyvers et al.); asking for written-out thinking can be declined (Opus 5 prompting guide, `reasoning_extraction`); a bare "are you sure?" flips answers (FlipFlop); a challenged assertion stands until defeated (Brandom, "Asserting") |
| Done when | Verdict plus a reply to every objection | An observable end state (pragmatic maxim); checkable intent raised pass@1 (TiCoder) |

## Rationale

- The procedure targets agreement bias first (lines 1, 2 and 10) and contrarian churn second
  (line 9).
- The owner asked for the text to be grounded in the supplied research, not in a new measurement,
  so no eval ran. That is an owner exception to the AGENTS.md rule that a skill changes only for a
  witnessed failure.
- The description change skips the trigger eval because the skill is never auto-invoked.
- Line 3 says "Decide" where the supplied text said "Settle": the lint rejects a sibling's name.

## Evidence

- [engineering-meaning.md](../research/engineering-meaning.md) and its
  [theory](../research/engineering-meaning-theory.md) and
  [empirical](../research/engineering-meaning-empirical.md) supplements.
- [philosophy.md](../research/philosophy.md) moves 3–7 and 10, and
  [philosophy-canon.md](../research/philosophy-canon.md).
- [research-skills.md](../research/research-skills.md) (the Opus 5 guide row).
- URLs: [docs/sources.md](../sources.md), section wdyt.

## Status

Accepted (2026-11-05).
