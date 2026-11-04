# AGENTS.md — skills

This repository ships independently installable Markdown skills. A skill that works only beside its
siblings is broken.

## Edit contract

- One `skills/<name>/SKILL.md` per skill and nothing else in the folder.
- Frontmatter holds `name` (the folder name) and a one-line `description`: the action, the real
  trigger in task language, and the nearest exclusion. Never name the skill itself or a sibling.
- Keep only lines that change what a strong model does. Cut good practice it already follows,
  slogans, and rationale.
- Change a skill only for a witnessed failure. Record the failure and the with/without result in the
  commit message.
- Skills write no document of their own: they answer in chat or edit their target.
- Use untitled inline Markdown links. Reference-style and angle-bracket links are rejected.
- Update the README catalog row with every skill addition or removal, and
  [`docs/sources.md`](docs/sources.md) when a sourced line changes or leaves.
- Released `CHANGELOG.md` sections are history; never edit them. Removing or renaming a skill is a
  major version with a cutover note in the README and the changelog. Tag every release.

## Verify

```bash
sh scripts/lint.sh
sh scripts/test-lint.sh
```
