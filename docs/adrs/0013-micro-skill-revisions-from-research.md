---
type: adr
id: adr-0013
status: accepted
created: 2026-11-05
---

# ADR-0013 - Revise the micro skills from the research

## Context

The engineering-meaning review (§9) and the philosophy authoring rules propose lines for the micro
skills. The owner asked for them to be applied where the research supports them, without new
measurements. Each skill stays a few lines, user-invoked, and free of sibling names.

## Decision

| Skill | Added | Grounding |
| --- | --- | --- |
| handoff | Every decision in force as one full list with source and reason; any condition that makes the goal moot; assumptions marked unchecked only when unverified; the likely next change and where it belongs; a reviewer gets the requirements and the target, not the author's account | a specification spread over turns costs 39%, and models return superseded values (Laban et al.; Chattaraj & Raj; Wang & Sun); assertions as defensible commitments (Brandom); joint goals end when achieved, unachievable or irrelevant (Cohen & Levesque); common ground holds only what is mutually accepted (Stalnaker); documentation cannot carry the program's theory (Naur); author framing biases reviewers (Mitropoulos et al.) |
| onward | If the goal turns out done, impossible or moot, say which with evidence, then stop | Cohen & Levesque; 12.4% of multi-agent failures missed when to stop |
| sitrep | Report from artifacts, not claims; each earlier "I will" done, or dropped and why | Rule-following is shown in what was done; a promise has conditions that can be checked (§3) |
| rearm | Restate every decision in force as a full list; before editing inherited work, say where one likely change goes and check it against the code | Brandom; Naur |
| whatsnext | Name what else the recommended step changes | Practical-reasoning critical question on side effects (Walton) |
| stepback | List what the approach takes for granted; name the category the options share and its purpose; give one option outside it | Presupposition check (Lewis; FPBench); options converge within a category (Kostiuk et al.; Artificial Hivemind) |
| proper | Judge from the diff, the commands run and their output, never from the claim that it is done | 80.4% of incomplete reviews were reported misleadingly; rule-following is shown in what was done |
| scout | Keep what was observed, with its source, apart from what is assumed and what is unknown | Provenance labels: observed, reported, inferred (untested) |
| tldr | Keep the uncertainty that bears on the decision | Selective precision: keep what changes the action |

panel, bulletproof, settle and drill are out of scope here; panel and bulletproof changed through
the second-pass eval instead. revolver is unchanged.

## Rationale

- Each line is either in the §9 proposal table or follows from the authoring rules, and each is
  phrased "if C, do X" where it is conditional.
- In the first-pass gate, the handoff additions raised false alarms on clean items: invented moot
  conditions and confirmed facts marked unchecked. So the moot condition says "any", and only
  unverified assumptions are marked.
- No eval ran, by owner instruction. That is the same exception as ADR-0012.

## Evidence

- [engineering-meaning.md](../research/engineering-meaning.md) §2, §3, §7 and §9.
- [engineering-meaning-theory.md](../research/engineering-meaning-theory.md).
- [philosophy.md](../research/philosophy.md) (authoring rules).
- Gate result for handoff: [evals/proposal-gate](../../evals/proposal-gate/README.md).
- URLs: [docs/sources.md](../sources.md), section micro skills.

## Status

Accepted (2026-11-05).
