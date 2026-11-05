---
type: adr
id: adr-0015
status: accepted
created: 2026-11-05
---

# ADR-0015 - Add despaghettify for dense code

## Context

José asked for a skill that prevents or fixes common unreadable code patterns: endless chained
ternaries, overuse of spread operators, and code that looks minified. debloat excludes source code,
so nothing in the catalog covers this.

## Decision

1. despaghettify rewrites the code the user named, or else the current diff, into plain code
   without changing behavior. It is manual-only, like every skill
   ([ADR-0014](./0014-every-skill-manual-only.md)).
2. Behaviour is recorded before the rewrite and checked again after it. Any difference is a bug in
   the rewrite.
3. Step 3 lists each pattern with its plain replacement, in the project's own idioms, formatter and
   lint rules.
4. The description does not contain the skill's name, which the lint rejects. It says "untangle or
   make code readable" where José's text said "despaghettify, untangle".

## Rationale

| Part | Grounding |
| --- | --- |
| Plain steps; each pattern paired with its replacement, not a ban | Opus 5 prompting guide: positive recipes work better than prohibitions ([research-skills.md](../research/research-skills.md)); authoring rules in [philosophy.md](../research/philosophy.md) |
| Checks run before and after; any difference is a bug | Judge from artifacts, not claims; count only a test that can fail ([philosophy.md](../research/philosophy.md) moves 1 and 5) |
| Scope limited to the named code or the diff; short body | Compact skills gained 19–21.5 points and comprehensive ones 0.7 (SkillsBench, [engineering-meaning.md](../research/engineering-meaning.md) §7) |
| Name | "simplify" is a Claude Code built-in; a distinct name avoids the clash |

- No eval ran. José asked for the skill to rest on the supplied research, as in
  [ADR-0012](./0012-wdyt-judges-the-users-idea.md).

## Evidence

- [docs/sources.md](../sources.md), section despaghettify.
- [research-skills.md](../research/research-skills.md), recipes-over-prohibitions row.

## Status

Accepted (2026-11-05).
