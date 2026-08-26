# skills

Portable Markdown skills for explicit decisions, evidence-bound work, and ruthless economy. Every
folder under [`skills/`](./skills/) stands alone. No runtime, registry, vendor, or hidden family
meeting required.

## Install

```bash
npx skills add jcosta33/skills -g -a codex
npx skills add jcosta33/skills -g -a claude-code
npx skills add jcosta33/skills --skill revolver -g -a codex
npx skills add https://github.com/jcosta33/skills/tree/<commit> -g -a codex
```

The last form pins a commit. Re-running `add` updates present entries but does not prune removed
names. After 6.0.0, `npx skills remove -g -a <agent> disrespec fork-me sus-audit sus-campaign
sus-change-plan sus-inventory sus-panel sus-research sus-spec sus-task`, then re-add.
Inspect `overwrites:` before confirming. Compare any existing folder with the source tree;
cancel on mismatch. Remove an installed entry absent from the source only after the same comparison.
Name alone proves nothing.

## Catalog

| Skill                                            | Use                                                  |
| ------------------------------------------------ | ---------------------------------------------------- |
| [`ask-user`](./skills/ask-user/SKILL.md)         | structure every agent-originated question            |
| [`bulletproof`](./skills/bulletproof/SKILL.md)   | actively verify load-bearing claims                  |
| [`debloat`](./skills/debloat/SKILL.md)           | remove wasted prose                                  |
| [`demolition`](./skills/demolition/SKILL.md)     | run quarantined one-sided advocacy                   |
| [`dissect`](./skills/dissect/SKILL.md)           | trace a code path and coupling to closure            |
| [`drill`](./skills/drill/SKILL.md)               | lock language, obligation, place, slice before write |
| [`panel`](./skills/panel/SKILL.md)               | recommend one option from independent analysis       |
| [`promote`](./skills/promote/SKILL.md)           | move a transient artifact into project ownership     |
| [`remember`](./skills/remember/SKILL.md)         | preserve one verified lesson                         |
| [`revolver`](./skills/revolver/SKILL.md)         | exhaust broad risk through sequential refinement     |
| [`settle`](./skills/settle/SKILL.md)             | resolve technical ambiguity from evidence            |
| [`triple-check`](./skills/triple-check/SKILL.md) | run three concurrent top-tier reviews                |

These are methods, not paperwork. None of them writes a document; each returns its result in chat and
leaves durable records to the project that owns them.

Each skill carries its own load-bearing rules. Agents assess and recommend; humans own intent,
waivers, irreversible actions, and acceptance. Catalog design and evidence live under
[`docs/`](./docs/).

Skills that author Suspec artifacts — spec, task, inventory, change plan, audit, research, and
campaign — ship with the method that defines them, in
[Suspec](https://github.com/jcosta33/suspec).

## Security

Inspect instructions before installation. You are installing words into an agent's head; act
accordingly. Payloads contain Markdown only: no scripts, executables, hooks, or network clients.
Repository shell scripts lint the source catalog.
