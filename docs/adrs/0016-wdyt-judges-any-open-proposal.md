---
type: adr
id: adr-0016
status: accepted
created: 2026-11-05
supersedes: adr-0012
---

# ADR-0016 - wdyt judges an open proposal, the user's or the agent's

## Context

[ADR-0012](./0012-wdyt-judges-the-users-idea.md) scoped wdyt to an idea the user proposes and
excluded the agent's own earlier answer. The owner widened it: wdyt also covers a proposal the agent
made that the owner asks it to consider. What wdyt judges is a question that is still open. It never
defends or attacks a conclusion that has already been reached, whoever proposed it.

## Decision

- **Description.** "Judge an open proposal and return one reasoned verdict on it. Use only when the
  user asks what you think of an undecided idea, design, claim, or plan, whether they proposed it or
  you did." The exclusion becomes "re-check a finished answer", replacing "re-check your own
  earlier answer". A finished answer is the job of the second-pass skills.
- **Line 1.** Before the restatement, add: "Treat the question as open, whether the user or you
  proposed it." Strip "anyone's preference for it, yours included" in place of "the user's
  preference".
- **Other lines.** Lines 2–10 and the Done-when line are unchanged. The ADR-0012 grounding table
  still holds for them.
- **README.** The catalog row reads "judge an open proposal, the user's or yours". The failure it
  prevents is "agreeing with an idea because of who proposed it".

## Rationale

- **Two biases, one remedy.** A proposal from the user carries a pull toward agreement. A proposal
  from the agent carries a pull toward its own earlier output:
  - models rate their own generations higher than others' (Panickssery et al., 2024);
  - models correct an error they wrote far less often than the same error attributed to the user
    (Self-Correction Bench).

  Judging the proposal as a stranger's targets both. "Without anyone's preference for it, yours
  included" names the second pull explicitly.
- **Open question first.** "Treat the question as open" blocks the reply from starting with a
  verdict and arguing back to it. Lines 4–7 then do the work.
- **Owner exception to the edit contract.** The change follows the owner's correction, not a
  witnessed run, as with ADR-0012. No eval ran.
- **No trigger eval.** The skill is manual-only (ADR-0014), so the description serves the `/wdyt`
  menu.

## Evidence

- Owner's correction, 2026-11-05: wdyt "should also support the case of the agent himself proposing
  something", and the question is open-ended, "not about any foregone conclusion".
- [ADR-0012](./0012-wdyt-judges-the-users-idea.md) for lines 2–10.
- URLs: [docs/sources.md](../sources.md), section wdyt.

## Status

Accepted (2026-11-05). Supersedes ADR-0012.
