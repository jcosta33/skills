# Micro skills: merged shortlist

This shortlist merges [micro-candidates-history.md](micro-candidates-history.md) and
[micro-candidates-research.md](micro-candidates-research.md), both from 2026-11-05. The history
counts cover José's typed messages: 5,174 messages across 296 sessions, 2026-03-15 → 11-04.

## Rules for every micro skill

These come from the research file §2, which cites first-party docs.

- **User-invoked only.** Set `disable-model-invocation: true` in the frontmatter. Claude Code and
  Cursor honor it, and in Claude Code a user-invoked skill costs zero context per turn. Codex needs
  `agents/openai.yaml` beside the skill containing `policy: {allow_implicit_invocation: false}`.
  The skills-repo lint must allow that one extra file. Gemini has no flag, so the description
  says "Use only when the user asks…".
- **No built-in names.** Claude Code silently replaces a built-in with a same-named personal
  skill. Avoid `recap`, `plan`, `review`, `verify`, `debug`, `fork`, `focus`, `goal`, `btw`,
  `simplify`, `status`, and `init`.
- **3–6 self-contained lines.** Each skill acts on the target the user named, else on the current
  reply or branch. It needs no `$ARGUMENTS` and calls no other skill.
- **Retire on absorption.** Once a harness ships the shortcut as a built-in, delete the skill.

## Tier A: build now

| Skill | Intent | Evidence | Built from |
| --- | --- | --- | --- |
| `tldr` | Only what bears on a decision | José's own; history 14 msgs / 11 sessions | already drafted |
| `wdyt` | Reason to a position like a judge or philosopher | José's own; history 48 / 29 | waits on the philosophy synthesis |
| `onward` | Keep going to the stop condition; skip past blockers; stop only for human-owned calls | history **555 / 119** (327 bare "continue") | history #1 |
| `next` | One recommended next step, its reason, ≤2 alternatives; start it if nothing needs José | history 130 / 60 | history #7; absorbs research `options` |
| `sitrep` | Done / in flight / missing / ETA / broader goal, from live git and GitHub state | history 122 / 59 | history #2 |
| `handoff` | Paste-ready brief for a fresh agent: goal, stop condition, done, remaining, rules to read, lanes to avoid | history 61 / 23; skills.sh `handoff` 1.1M installs | merge of history #3 and research #2 |
| `rearm` | Re-read AGENTS.md and the named goal or campaign file, sync main, read the branch state, then resume | history 58 / 32; research `catchup` | merge of history #4 and research #3 |
| `scout` | Read-only: learn the target end to end, then report state, risks, human-only questions, and a plan | history 82 / **51 sessions** (widest spread) | history #5 |
| `stepback` | Question the premise: should this exist? What is the deeper cause? Then skip, simplify (scrap and redo), or proceed | history 50 / 30; first-party "scrap" tip | merge of history #9 and research `scrap` + `pushback` |
| `proper` | Audit my change for hacks, stubs, fallbacks, type escapes, count-gaming, and changes I didn't ask for; fix the real cause; revert nothing unasked without saying so | history 70 / 39; research `overreach` | merge of history #6 and research #7 |

## Tier B: build if Tier A sticks

| Skill | Intent | Evidence | Note |
| --- | --- | --- | --- |
| `quiz` | Quiz me on the riskiest behavior in a diff before merge, one question at a time, each grounded in file:line | first-party power-user tip; HN 2026-10 | not in José's history yet; targets comprehension debt |
| `huh` | Re-explain the last reply plainly, adding no new claims | `wait-what` 495K installs; history `whatsthis` 20 / 14 | the inverse of `tldr` |
| `pace` | Effort spent vs delivered, where the waste went, shortest remaining path | history 25 / 15, mostly Codex | narrow |
| `premortem` | Assume it failed in 3 months; name the 3 likeliest causes, early signs, cheap checks | HN 2026-05→10; skills.sh <1K | may fold into `wdyt` or `bulletproof` per the philosophy synthesis |

## Not a micro skill

| Candidate | Verdict | Reason |
| --- | --- | --- |
| `hygiene` | Sourdaw repo | names `pnpm` scripts and the board; project-scoped |
| `models` | AGENTS.md rule | already written in CLAUDE.md; a skill would duplicate it |
| `ship` | skip | owned by `pnpm deliver`; low recent frequency |
| `quickwins` | skip | 13 msgs / 7 sessions |
| `quiet` | tighten `settle` and AGENTS.md | same intent as `settle` |
| `salvage` | skip | close to `bulletproof`; 10 msgs |
| `options` | merged into `next` | `panel` covers consequential choices |
| `catchup` | merged into `rearm` | — |
| `overreach` | merged into `proper` | — |
| `scrap`, `pushback` | merged into `stepback` | — |
| commit/PR, review, verify, debug, interview, de-slop | covered | harness built-ins or existing skills (research §3) |

## Signal worth acting on outside skills

`onward`, `rearm`, `proper`, `models`, and `quiet` each restate a rule José already wrote in
`~/.agents/AGENTS.md` or `CLAUDE.md`, and he still types them daily. Always-loaded rules evidently
decay mid-session. A user-invoked micro skill is the cheap way to re-arm a rule. Moving rules out of
AGENTS.md into skills would make things worse, because auto-triggering misses about half the time
(research C5).

## Drafts for the merged skills

The history file holds drafts for `onward`, `next`, `sitrep`, and `scout`, and the research file
holds drafts for `quiz` and `huh`. Below are the merged ones. Each needs
`disable-model-invocation: true` plus the Codex yaml.

```markdown
---
name: handoff
description: Write a paste-ready brief so a fresh agent can continue this work. Use only when the user asks for a handoff or goal prompt.
disable-model-invocation: true
---
Write one fenced, paste-ready prompt for an agent that cannot see this conversation; focus it on what I named, if anything.
Include: objective and stop condition; what is done and verified (with PR/issue refs); what remains, in order; open decisions; traps found; rules and skills to read first; lanes and branches to leave alone.
Point to files, commits, PRs, and issues by path or URL instead of copying them. Drop anything finished or no longer true. No secrets.
```

```markdown
---
name: rearm
description: Refresh rules and working state, then resume the current task. Use only when the user asks to re-read the rules or get back up to speed.
disable-model-invocation: true
---
Fetch, then re-read latest main's AGENTS.md, the skills and goal or campaign file it names for this work, and any brief path I named.
Read the current branch's commits and uncommitted changes against its base, plus what changed on main that touches it.
State in one line each rule you were not following and the next step, then continue.
```

```markdown
---
name: stepback
description: Question whether the current approach should exist before continuing it. Use only when the user asks to step back or questions the premise.
disable-model-invocation: true
---
Stop the current approach. State the goal it serves in one line.
Answer with code or repo evidence: does this need to exist? What breaks if we skip it? Is there a deeper cause we are patching around?
Recommend skip, simplify, or proceed. If simplify: treat the attempt as a throwaway draft, rebuild it the simplest correct way using what we learned, and rerun the same checks.
```

```markdown
---
name: proper
description: Audit the change just made for shortcuts and unrequested scope, then fix the real cause. Use only when the user asks if this is done properly.
disable-model-invocation: true
---
Audit the change for stubs, no-op paths, fallbacks that hide a failure, type escapes, suppressed lints or tests, count-gaming, and symptom-only fixes.
Fix each at the owning layer following repo conventions; if a shortcut is genuinely right, say why in one line.
List every change I did not ask for, with file:line, marked keep (the request needs it) or revert. Revert nothing until I answer.
```
