# AGENTS.md — skills

This repository ships independently installable Markdown skills. A skill that works only beside its
siblings is broken.

## Edit contract

- One `skills/<name>/SKILL.md` per skill, plus `agents/openai.yaml` holding exactly
  `policy: {allow_implicit_invocation: false}` (block style). Every skill sets
  `disable-model-invocation: true` and says "Use only when the user" in its description: skills
  are manual follow-ups to a failure, never auto-triggered. Every-turn rules belong in AGENTS.md
  or hooks.
- Frontmatter holds `name` (the folder name) and a one-line `description`: the action, the real
  trigger in task language, and the nearest exclusion. Never name the skill itself or a sibling.
- Change a skill only for a witnessed failure. Record the failure and the with/without result in the
  commit message.
- Skills write no document of their own: they answer in chat or edit their target.
- Use untitled inline Markdown links. Reference-style and angle-bracket links are rejected.
- Update the README catalog row with every skill addition or removal, and
  [`docs/sources.md`](docs/sources.md) when a sourced line changes or leaves.
- Record each load-bearing decision as a new ADR in [`docs/adrs/`](docs/adrs/README.md) and add
  its index row. Never edit an accepted ADR; supersede it. Research reports live in
  [`docs/research/`](docs/research/README.md).

## Authoring rules

- Write plain steps with a checkable output. No persona lines. No thinker, school, or method names
  (philosophy, Kant, Popper, disputatio, premortem, steelman, and the like) anywhere in a skill; lint
  rejects them. Credit sources in [`docs/sources.md`](docs/sources.md).
- Keep at most 10 load-bearing rules, most important first; models favor earlier instructions.
- Write "If C, do X". No hedges or modal verbs.
- End with **Done when** plus an observable check, or with the exact output to return.
- Specify only what a model change would break; drop what the model already does by default.
- Lint with deterministic rules only. LLM ambiguity checks score near chance.
- A rewrite ships only if it beats paraphrases of the old text that keep its meaning; format alone
  swings results widely.

## Trigger eval

No skill is model-invoked, so descriptions now serve the `/name` menu. Run this eval before any
skill becomes model-invocable again, using the method of Anthropic's skill-creator (`run_eval.py`).

1. Write about 20 queries in the user's own words: half should trigger, half are near misses that
   share keywords but need another skill or none.
2. Run each query 3 times through `claude -p` with the model pinned. A should-trigger query passes
   at a trigger rate of 0.5 or more; a near miss passes below 0.5.
3. Run the old and the new description on the same set. Keep the new one only if it passes more
   queries and adds no false trigger.
4. Commit the query set and the per-query rates under [`evals/`](evals/).

## Verify

```bash
sh scripts/lint.sh
sh scripts/test-lint.sh
```
