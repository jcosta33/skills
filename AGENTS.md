# AGENTS.md — skills

This repository ships independently installable Markdown skills. A skill that works only beside its
siblings is broken.

## Edit contract

- Keep each skill complete in `skills/<name>/SKILL.md`. Ship no appendix payloads.
- Keep frontmatter `name` and directive `description`.
- Preserve standalone operation and Markdown-only payloads.
- Author no document. These skills return their result in chat; durable records belong to the
  project or method that owns them.
- Use untitled inline Markdown links with simple destinations. Reference-style, angle-wrapped,
  fragmented, and nested-parenthesis destinations are rejected.
- Update the README catalog row with every skill addition or removal.
- Update `docs/sources.md` in the same change whenever an externally grounded skill or design rule
  changes. Remove sources when their claims leave.
- Preserve released `CHANGELOG.md` history.
- Follow [catalog design](docs/README.md) for activation, body, execution, scope, self-containment,
  and existence rules.

## Verify

```bash
sh scripts/lint-current.sh
sh scripts/test-lint-current.sh
sh scripts/lint-released-changelog.sh
```
