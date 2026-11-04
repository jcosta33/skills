# skills

Seven portable Markdown skills for coding agents. Each folder under [`skills/`](./skills/) is one
`SKILL.md` that works installed alone: no runtime, scripts, or hidden dependencies.

## Install

```bash
npx skills add jcosta33/skills -g -a codex
npx skills add jcosta33/skills -g -a claude-code
npx skills add jcosta33/skills --skill revolver -g -a codex
npx skills add https://github.com/jcosta33/skills/tree/<commit> -g -a codex
```

The last form pins a commit. Re-running `add` updates present entries but never removes skills that
left the catalog. Inspect `overwrites:` before confirming.

## Cutover to 7.0.0

7.0.0 merged `settle` into `ask-user`, `dissect` into `bulletproof`, `remember` into `promote`, and
`triple-check` into `revolver`, and cut `demolition`. Remove the departed names for every agent,
then re-add. Leave `-a` off `remove`: scoped to some agents, it keeps the shared copy and the lock
entry while any other agent still links them. Put skill names before any `-a`; the CLI reads every
word after `-a` as an agent.

```bash
npx skills remove settle dissect remember triple-check demolition -g
npx skills add jcosta33/skills -g -a <agent>
```

The artifact authors moved with the Suspec rename to [Corpus](https://github.com/jcosta33/corpus):

```bash
npx skills remove sus-spec sus-task sus-inventory sus-change-plan sus-audit sus-research sus-campaign -g
npx skills add jcosta33/corpus -g -a <agent>
```

## Catalog

| Skill                                          | Use                                              | Failure it prevents                                              |
| ---------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------- |
| [`ask-user`](./skills/ask-user/SKILL.md)       | decide from evidence; ask only as a choice       | bare questions, guessed preferences, decisions dumped on the user |
| [`bulletproof`](./skills/bulletproof/SKILL.md) | verify claims or a code path                     | mixed or unproven claims passed off as checked                    |
| [`debloat`](./skills/debloat/SKILL.md)         | tighten prose without losing facts               | reformatting that keeps the bloat, or cuts that drop a fact       |
| [`drill`](./skills/drill/SKILL.md)             | lock name, guarantee, place, slice before coding | new code beside an existing rule it should have reused            |
| [`panel`](./skills/panel/SKILL.md)             | recommend one option from blind analyses         | one correlated pass dressed up as several perspectives            |
| [`promote`](./skills/promote/SKILL.md)         | make a working document a project record         | copies left behind, invented homes, unchosen commits              |
| [`revolver`](./skills/revolver/SKILL.md)       | review with fresh reviewers, then fix            | authors reviewing their own work                                  |

None of these writes a document of its own; each answers in chat or edits its target. Skills that
write Corpus artifacts ship with [Corpus](https://github.com/jcosta33/corpus). Sources behind the
skills: [`docs/sources.md`](./docs/sources.md).

## Security

Inspect instructions before installation: you are installing words into an agent's head. Payloads
are Markdown only. The shell scripts under `scripts/` lint this repository and never ship.
