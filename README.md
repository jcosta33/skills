# skills

Portable Markdown skills for coding agents. Each folder under [`skills/`](./skills/) is one
`SKILL.md` that works installed alone: no runtime, scripts, or hidden dependencies.

## Install

```bash
npx skills add jcosta33/skills -g -a codex
npx skills add jcosta33/skills -g -a claude-code
npx skills add jcosta33/skills --skill revolver -g -a codex
```

Re-running `add` updates present entries but never removes skills that left the catalog. Remove
those by name with `npx skills remove <names> -g`, leaving `-a` off so the shared copy and the lock
entry go too.

## Catalog

| Skill                                          | Use                                                  | Failure it prevents                                               |
| ---------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| [`bulletproof`](./skills/bulletproof/SKILL.md) | surface and verify the assumptions behind a claim    | an unstated assumption passed off as checked                      |
| [`debloat`](./skills/debloat/SKILL.md)         | tighten prose without losing facts                   | reformatting that keeps the bloat, or cuts that drop a fact       |
| [`dissect`](./skills/dissect/SKILL.md)         | trace one code path to closure                       | "nothing calls this" from a symbol search                         |
| [`drill`](./skills/drill/SKILL.md)             | lock name, guarantee, place, slice before coding     | new code beside an existing rule it should have reused            |
| [`panel`](./skills/panel/SKILL.md)             | recommend one option from blind analyses             | one correlated pass dressed up as several perspectives            |
| [`revolver`](./skills/revolver/SKILL.md)       | rotate fresh reviewers one stance at a time, fixing  | authors reviewing their own work; findings left unresolved        |
| [`settle`](./skills/settle/SKILL.md)           | resolve ambiguity by evidence; ask only as a choice  | bare questions, guessed preferences, decisions dumped on the user |

### Micro

| Skill                                          | Use                                                  | Failure it prevents                                               |
| ---------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| [`tldr`](./skills/tldr/SKILL.md)               | decision-only short version, on request (`/tldr`)    | a summary that buries the decision under process                  |

`tldr` sets `disable-model-invocation: true`, a Claude Code field outside the Agent Skills spec.
Codex uses its own `agents/openai.yaml` instead, so outside Claude Code it can also trigger on its
description.

None of these writes a document of its own; each answers in chat or edits its target. Skills that
write Corpus artifacts ship with [Corpus](https://github.com/jcosta33/corpus). Sources behind the
skills: [`docs/sources.md`](./docs/sources.md).

## Security

Inspect instructions before installation: you are installing words into an agent's head. Payloads
are Markdown only. The shell scripts under `scripts/` lint this repository and never ship.
