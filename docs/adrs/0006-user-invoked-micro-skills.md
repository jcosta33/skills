---
type: adr
id: adr-0006
status: accepted
created: 2026-11-05
---

# ADR-0006 - Micro skills are user-invoked and ship agents/openai.yaml

## Context

The owner retypes the same short intents across harnesses: continue, what is next, status,
recon-and-report, a no-hacks audit, handoff, re-read the rules, question the premise, and what do
you think. Several restate always-loaded rules that decay mid-session.

## Decision

1. Each such intent becomes a micro skill: handoff, onward, proper, rearm, scout, sitrep, stepback,
   tldr, wdyt and whatsnext.
2. Each sets `disable-model-invocation: true` and ships `agents/openai.yaml` with
   `allow_implicit_invocation: false`. The lint requires the YAML if and only if the flag is set.
3. Each description also says "Use only when the user asks", for harnesses that honour neither
   flag.
4. Each stays a few lines, names no sibling, and answers in chat.

## Rationale

- A named call re-arms a rule at the moment it is needed. Auto-triggering would duplicate
  always-loaded context and fire on near misses.
- Claude Code, Cursor and VS Code Copilot honour the frontmatter flag, and Codex honours the YAML.
  Gemini CLI honours neither, and claude.ai uploads and the Skills API reject the flag.

## Evidence

- History counts: [micro-candidates-history.md](../research/micro-candidates-history.md) (aggregate),
  [micro-shortlist.md](../research/micro-shortlist.md),
  [micro-candidates-research.md](../research/micro-candidates-research.md).
- [d662daa](https://github.com/jcosta33/skills/commit/d662daa), [d598610](https://github.com/jcosta33/skills/commit/d598610), [7bf943f](https://github.com/jcosta33/skills/commit/7bf943f).

## Status

Accepted (2026-11-05).
