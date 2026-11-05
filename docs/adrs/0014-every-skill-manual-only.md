---
type: adr
id: adr-0014
status: accepted
created: 2026-11-05
---

# ADR-0014 - Every skill is manual-only

## Context

The method skills could trigger on their own. Their descriptions were tuned for that in
[ADR-0008](./0008-descriptions-in-the-users-words.md), and settle's description said "ALWAYS use …
before asking the user anything". José ruled that none of these skills should trigger by itself:
each is invoked by hand, in response to a failure, not as a means to prevent one.

## Decision

1. Every skill sets `disable-model-invocation: true` and ships `agents/openai.yaml` with
   `allow_implicit_invocation: false`. This adds bulletproof, debloat, dissect, drill, panel,
   revolver and settle to the micro skills.
2. Every description says "Use only when the user …", for Gemini CLI, which honours neither flag.
   Clauses that invited proactive use ("even when …", "before a claim is relied on") are gone.
3. settle's description is user-invoked. The every-turn rule it carried, to settle by evidence
   before asking, stays in the owner's global AGENTS.md Authority section.
4. scripts/lint.sh fails any SKILL.md without the flag, the YAML, or the phrase. Mutations in
   scripts/test-lint.sh prove each check fires.
5. The trigger-eval rates from [2ce1ab0](https://github.com/jcosta33/skills/commit/2ce1ab0) now
   matter only for how the descriptions read in the `/name` menu. The AGENTS.md trigger eval
   applies again only if a skill becomes model-invocable.
6. revolver's description changes under this ruling. Its method stays frozen
   ([ADR-0004](./0004-revolver-frozen.md)).

## Rationale

- José's ruling.
- **The second-pass evaluation measured the real use.** These skills act as follow-ups after an
  answer falls short ([ADR-0010](./0010-skills-measured-as-second-passes.md),
  [evals/second-pass](../../evals/second-pass/README.md)).
- **First-party guidance routes every-turn rules away from skills.** A rule that must hold every
  time belongs in a hook or in always-loaded instructions
  ([research-skills.md](../research/research-skills.md), settle row; Claude Code hooks docs).
- **Auto-invocation is unreliable anyway.** In one vendor eval the skill was not invoked in 56% of
  cases ([engineering-meaning-empirical.md](../research/engineering-meaning-empirical.md)).

## Evidence

- [evals/second-pass](../../evals/second-pass/README.md).
- [research-skills.md](../research/research-skills.md).
- [docs/sources.md](../sources.md): Claude Code hooks and skills.

## Status

Accepted (2026-11-05). Narrows ADR-0008: description changes no longer need the trigger eval while
no skill is model-invocable.
