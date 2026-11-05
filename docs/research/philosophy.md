# Philosophy of instruction: synthesis and proposed skill changes

This document draws on two reports from 2026-11-05:

- [philosophy-sources.md](philosophy-sources.md): José's 15 sources, checked and read.
- [philosophy-canon.md](philosophy-canon.md): 34 thinkers and traditions, Pythagoras → Kant → Pólya,
  each with dated LLM evidence.

Labels used below:

- **Backed:** a dated LLM study supports the move.
- **Untested:** the move is plausible from the tradition, but no study exists.

## The thesis, refined

José's view: the tradition of disciplined thought teaches more about instructing LLMs than prompt
folklore does. The evidence supports it, with one sharp correction.

- **What transfers is the procedure, not the name.** Expert personas don't move accuracy (Zheng 2024;
  Basil 2025; Kim 2024). Schoenfeld found that Pólya's named heuristics describe expert behavior
  without teaching it. Many classical methods work through a constraint their name doesn't carry:
  - disputatio's force is the reply to *every* objection;
  - Popper's is that the test must be able to fail;
  - Plato's division is valuable for its exhaustiveness.

  Rule: skill bodies spell out the steps. Names live in the README as provenance, unless an A/B test
  shows the name adds something.
- **The tradition's deepest lesson for LLMs is the line between observing and reasoning.** Hume's
  fork, Leibniz's *calculemus*, the Stoic discipline of assent and Kant's limits all say the same
  thing: a matter of fact is settled by looking, not by thinking harder. Models cannot self-verify
  by re-reasoning (Huang 2023), and their stated reasons misreport their real causes (Turpin 2023).
  Methods that work check against something outside the model (CRITIC, PAL, Logic-LM). **Backed.**
- **Generic "think slowly" cues are obsolete.** Frontier models already avoid the classic intuitive
  traps (Hagendorff 2023). The remaining failures are evidential (what was actually checked) and
  dialectical (which options and objections were never considered).

## The moves that earn a line

| # | Move | From | Evidence | Lands in |
| --- | --- | --- | --- | --- |
| 1 | Settle matters of fact by opening a source, computing, or running a test; never by re-reasoning | Hume, Leibniz, Stoics | Backed | `bulletproof`, `wdyt`, `dissect` |
| 2 | Collect independent verdicts before any discussion; debate only on a split | Kahneman (noise) | Backed (Self-Consistency, Choi 2025, Smit 2024) | `panel` |
| 3 | Restate the question without the asker's preferred answer; judge before weighing that preference | Stoic assent, Kant's first maxim, Perelman | Backed (S2A 2023; Sharma 2023) | `wdyt`, `settle` |
| 4 | Say in advance what would make the answer "not determinable from here"; demand more proof the less reversible the choice | burden of proof, Wittgenstein, Kant's limits | Backed (AbstentionBench 2025) | `wdyt`, `settle` |
| 5 | Write the result that would refute the hypothesis before testing; count only tests that could fail | Popper, Peirce | Backed (POPPER 2025) | `bulletproof`, `dissect` |
| 6 | Assume the plan failed; add a check per likely cause | premortem, devil's advocate | Backed (Wang 2024) | `wdyt`; Tier B `premortem` folds in |
| 7 | Write the strongest objections before the verdict and reply to every one | disputatio, Rapoport | Indirect | `wdyt` |
| 8 | Ask only when the readings lead to different actions, and ask the single most decisive question | Grice, Peirce | Backed (Suri 2026) | `settle` |
| 9 | Generate options as an exhaustive division by one criterion, always including doing nothing, partial, and reversible options | Plato's diairesis | Backed need (Kostiuk 2025: LLM and human options barely overlap) | `panel`, `wdyt`, `next` |
| 10 | When both sides look sound, stop choosing and test the premise they share | Kant's antinomies | Untested | `wdyt` |
| 11 | Each load-bearing claim states scope, condition, and strength (possible / observed / necessary) | Kant's table of judgments | Untested | `bulletproof` |
| 12 | Claim a cause only from a difference you produced (bisect, revert, toggle) | Mill's method of difference | Indirect (Corr2Cause) | `dissect` |
| 13 | Tag report claims Seen / Think / Will / Need OK; only the user in chat authorizes | Searle, Hila | Backed (instruction-hierarchy work) | global `AGENTS.md` |

## Authoring rules for every skill

These go into the skills-repo `AGENTS.md` and replace the cut design docs.

- Give plain steps with a checkable output. No persona lines, and no method names in bodies.
- Keep at most 10 load-bearing rules, most important first; models favor earlier instructions (IFScale).
- Write "If C, do X". No hedges or modal verbs (Grice's Manner maxim; ACE).
- End with **Done when** plus an observable check (Peirce's pragmatic maxim; TiCoder +22–54 pass@1).
- Specify only what a model change would break; drop what defaults already cover.
- Lint with deterministic rules only. LLM ambiguity checks are near chance (PRIG precision 0.54;
  Chen AUROC 0.49–0.58).
- A rewrite ships only if it beats paraphrases of the old text that keep the same meaning. Format
  alone swings results up to 76 points (Sclar 2024).

## Proposed `wdyt`

This is the disputatio procedure written as plain steps (canon report, Part 3). It beat the
Kantian-maxims draft, whose lines were attitudes a grader cannot check, and the Toulmin draft, which
lays out one argument but never generates alternatives. Moves 3, 4, 6, 7, 9, and 10 are folded in.

```markdown
---
name: wdyt
description: Think a question through to one reasoned verdict. Use when the user asks what you think, or for a judgment on a design, claim, plan, or trade-off with more than one defensible answer. Do not use when one lookup, command, or test settles it.
disable-model-invocation: true
---

1. Restate the question without the asker's preferred answer. Say what evidence would settle it and whether it is reachable here.
2. Divide the possible answers by one stated criterion until they are exhaustive, including doing nothing. Name your lean.
3. Write the strongest objections to that lean, as its best opponent would. Assume it was chosen and failed: add the likeliest cause.
4. Settle matters of fact by opening sources or running commands; argue only what cannot be observed.
5. Decide, demanding more evidence the less reversible the choice. If both sides still look sound, find the premise they share and test it.
6. Reply to every objection: concede, distinguish, or refute. One you cannot answer lowers confidence or changes the verdict.
7. End with the verdict, confidence as a number, and the observation that would reverse it.
```

## Proposed changes to existing skills

| Skill | Add | Leave alone |
| --- | --- | --- |
| `bulletproof` | Moves 1, 5, 11: never self-verify; state the refuting result first; scope, condition, and strength per claim | its focus on assumptions |
| `dissect` | Moves 5, 12: predict before each probe; claim a cause only from a produced difference | its methodical trace |
| `panel` | Moves 2, 9: independent verdicts counted before any discussion; exhaustive options including do-nothing | one recommendation, strongest dissent |
| `settle` | Moves 3, 4, 8: strip the asker's preferred answer; ask only when readings diverge in action; scale proof to irreversibility | its evidence-first core |
| `drill` | **Done when** per slice | everything else |
| `debloat` | "If C, do X"; at most 10 load-bearing rules, most important first, when the text is agent instructions | its checklist loop |
| `revolver` | nothing; José ruled it conceptually untouchable | — |

## Open questions for José

1. **Recommendation first.** Buçinca 2021 and Kim (CHI 2025) find that a recommendation shown first
   anchors the person deciding. `settle` and `CLAUDE.md` both put the recommendation first. One
   option: keep recommendation-first for reversible choices, and show options before the
   recommendation for irreversible ones. Or run an experiment first.
2. **The named-method A/B test** (canon report, Part 5). It compares five arms:
   - a one-line baseline;
   - the plain procedure;
   - the name alone;
   - the name plus the procedure;
   - a placebo name plus the procedure.

   The items are 40 real decisions from José's history, each seeded with one flaw. About 600 runs and
   ~2M tokens. It decides whether names like "disputatio" or "premortem" earn a place in skill bodies.
   Until it runs, the rule above is to ship plain procedures.

## Source caveats

- The Attempto page was unreachable; a 1996 paper by the same author was read as a substitute.
- Searle and Hila were read as abstracts only.
- The Buçinca URL is dead, but the paper was verified and read.
- Some canon findings are tagged "(abstract not re-read)".
- Section numbers in the classical texts were not reopened.
- No peer-reviewed LLM study of premortem or steelman prompting exists.
