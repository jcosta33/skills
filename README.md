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

Every skill runs only when you call it by name (`/name` in Claude Code, `$name` in Codex), as a
follow-up when an agent's work falls short. None triggers on its own.

| Skill                                              | Use                                                 | Failure it prevents                                               |
| -------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------- |
| [`bulletproof`](./skills/bulletproof/SKILL.md)     | surface and verify the assumptions behind a claim   | an unstated assumption passed off as checked                      |
| [`debloat`](./skills/debloat/SKILL.md)             | tighten prose without losing facts                  | reformatting that keeps the bloat, or cuts that drop a fact       |
| [`despaghettify`](./skills/despaghettify/SKILL.md) | untangle dense code without changing behavior       | chained ternaries, spread pileups, and minified-looking lines     |
| [`dissect`](./skills/dissect/SKILL.md)             | trace one code path to closure                      | "nothing calls this" from a symbol search                         |
| [`drill`](./skills/drill/SKILL.md)                 | lock name, guarantee, place, slice before coding    | new code beside an existing rule it should have reused            |
| [`panel`](./skills/panel/SKILL.md)                 | recommend one option from blind analyses            | one correlated pass dressed up as several perspectives            |
| [`revolver`](./skills/revolver/SKILL.md)           | rotate fresh reviewers one stance at a time, fixing | authors reviewing their own work; findings left unresolved        |
| [`settle`](./skills/settle/SKILL.md)               | resolve ambiguity by evidence; ask only as a choice | bare questions, guessed preferences, decisions dumped on the user |

### Micro

Short skills for intents typed again and again.

| Skill                                      | Use                                                 | Failure it prevents                                             |
| ------------------------------------------ | --------------------------------------------------- | --------------------------------------------------------------- |
| [`handoff`](./skills/handoff/SKILL.md)     | paste-ready brief for a fresh agent, in chat        | a successor that redoes finished work or misses a trap          |
| [`onward`](./skills/onward/SKILL.md)       | keep going to the stop condition                    | stopping for check-ins the rules already allow                  |
| [`proper`](./skills/proper/SKILL.md)       | audit the last change for shortcuts and extra scope | stubs, masking fallbacks, and unrequested edits shipped as done |
| [`rearm`](./skills/rearm/SKILL.md)         | re-read the rules and branch state, then resume     | rules that decayed mid-session                                  |
| [`scout`](./skills/scout/SKILL.md)         | learn a target read-only, then report back          | edits made while only a report was asked for                    |
| [`sitrep`](./skills/sitrep/SKILL.md)       | status from live git, GitHub, and tests             | a status report recalled from memory                            |
| [`stepback`](./skills/stepback/SKILL.md)   | question whether the approach should exist          | polishing work that should be skipped or redone                 |
| [`tldr`](./skills/tldr/SKILL.md)           | decision-only short version                         | a summary that buries the decision under process                |
| [`wdyt`](./skills/wdyt/SKILL.md)           | judge the user's own idea to one verdict            | agreeing with an idea because it is the user's                  |
| [`whatsnext`](./skills/whatsnext/SKILL.md) | one recommended next step and why                   | a menu of options with no pick                                  |

Every skill sets `disable-model-invocation: true` and ships `agents/openai.yaml` with
`allow_implicit_invocation: false`. Claude Code, Cursor, and VS Code Copilot honour the first, Codex
the second. Gemini CLI honours neither, so each description also says "Use only when the
user". claude.ai uploads and the Skills API reject the frontmatter key.

None of these writes a document of its own; each answers in chat or edits its target. Skills that
write Corpus artifacts ship with [Corpus](https://github.com/jcosta33/corpus). Sources behind the
skills: [`docs/sources.md`](./docs/sources.md). Decisions: [`docs/adrs`](./docs/adrs/README.md).

## Security

Inspect instructions before installation: you are installing words into an agent's head. Payloads
are Markdown, plus a two-line Codex policy file in each skill. The shell scripts under `scripts/` lint this repository and never ship.
