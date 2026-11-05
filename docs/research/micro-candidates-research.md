# Micro skills: landscape and candidates

Research for tiny user-typed skills, the kind `tldr` and `wdyt` are. Done 2026-11-05. Facts come from
docs, GitHub (`gh api`), the skills.sh search API, and the Hacker News API, all checked that day.
Every source carries a date. **F** marks first-party sources (the vendor's docs, repositories, or
staff). **C** marks community sources. Lines saying "inferred" are my own reading.

## Verification gaps (read first)

- **Reddit was not reachable.** `reddit.com/r/*/search.json` returned `HTTP Error 403: Blocked`.
  Six web searches aimed at r/ClaudeAI, r/cursor, and r/ChatGPTCoding found no Reddit threads.
  Forum evidence here is Hacker News, plus blogs and GitHub issues.
- **skills.sh install counts are noisy.** The leaderboard mixes an "8W Activity" column with an
  "Installs" column. Some forked copies of one skill each show about 950K installs, so automated
  installs probably inflate the numbers (inferred). Use those counts only to compare entries.
- Some secondary write-ups quote HN comments. Wherever I use one, I pulled the comment itself
  from the HN API. The exception is the feedough.com quotes, which are flagged.

## Sources

| ID | Kind | Source | Date |
|---|---|---|---|
| F1 | F | Claude Code skills docs, `code.claude.com/docs/en/skills` | undated; cites versions up to v2.1.309; read 2026-11-05 |
| F2 | F | Claude Code commands reference, `code.claude.com/docs/en/commands` | read 2026-11-05 |
| F3 | F | Agent Skills spec, `agentskills.io/specification` | read 2026-11-05; Anthropic opened the standard 2025-12-18 (SiliconANGLE, same day) |
| F4 | F | Skill authoring best practices, `platform.claude.com/.../agent-skills/best-practices` | read 2026-11-05 |
| F5 | F | Claude Code power-user tips, `support.claude.com/en/articles/14554000` | undated; page banner says it was updated recently; read 2026-11-05 |
| F6 | F | `anthropics/skills` (187K stars, created 2025-09-22); `discernment-nudge` added 2026-08-17 | `gh api` 2026-11-05 |
| F7 | F | `anthropics/claude-plugins-official`; `commit-commands/commands/commit.md` added 2025-11-20 | `gh api` 2026-11-05 |
| F8 | F | Codex skills doc, `learn.chatgpt.com/docs/build-skills` (redirected from `developers.openai.com/codex/skills`) | read 2026-11-05 |
| F9 | F | Codex custom-prompts page, marked deprecated; maintainer replies on `openai/codex` #15941 (March 2026) and #14459 | 2026 |
| F10 | F | Gemini CLI custom commands, `geminicli.com/docs/cli/custom-commands/` | last updated 2026-04-30 |
| F11 | F | Gemini CLI skills doc, `google-gemini/gemini-cli/docs/cli/skills.md` | read 2026-11-05 |
| F12 | F | Cursor skills doc, `cursor.com/docs/context/skills`; Cursor 2.4 changelog (skills) | 2.4 shipped 2026-01-22 |
| F13 | F | Cursor 1.6 changelog (custom slash commands) | 2025-09-12 |
| F14 | F | Codex app commands, `learn.chatgpt.com/docs/developer-commands` | read 2026-11-05 |
| F15 | F | Boris (Claude Code team) on HN, item 48296387 | 2026-05-27 |
| C1 | C | skills.sh all-time leaderboard and search API | read 2026-11-05 |
| C2 | C | `mattpocock/skills` (313K stars, created 2026-02-03) | `gh api` 2026-11-05 |
| C3 | C | re:cinq, "Grill-Me Skill: What It Does and How It Has Changed" | 2026-10-14 |
| C4 | C | `JuliusBrussee/caveman` (117K stars, created 2026-04-04); HN 47647455 (904 pts); HN 47954745, a benchmark against "be brief." | 2026-04-04 / 04-05 / 04-29 |
| C5 | C | Vercel, "AGENTS.md outperforms skills in our agent evals"; HN 46809708 | 2026-01-29 |
| C6 | C | Scott Spence, skill-activation posts (forced-eval hook) | 2025–2026; update note dated 2026-09-13 |
| C7 | C | Ivan Seleznov (Medium), "Why Claude Code Skills Don't Activate" (650 trials) | undated |
| C8 | C | Shrivu Shankar, "How I Use Every Claude Code Feature" (HN 45786738) | 2025-11-01 |
| C9 | C | `hesreallyhim/awesome-claude-code` README, at `48f765c` vs HEAD | 2025-09-30 vs 2026-11-04 |
| C10 | C | `anthropics/claude-code` #14851 (116 commands and 56 skills loaded into context) | 2025-12-20 |
| C11 | C | Ultrathink history: `anthropics/claude-code` #19098; clauding.de on v2.1.316 | 2026-01-18; 2026-10-31 |
| C12 | C | HN comments (item id, author, date given inline) | 2025-08 → 2026-11 |
| C13 | C | GitHub stars (2026-11-05): `obra/superpowers` 312K; `addyosmani/agent-skills` 113K; `blader/humanizer` 64.8K; `hardikpandya/stop-slop` 18.6K; `wshobson/commands` 2.6K (last push 2026-09-30); `qdhenry/Claude-Command-Suite` 1.3K (last push 2026-03-01); three `tldr` skill repos at ≤5 stars (created 2026-06 → 2026-10) | 2026-11-05 |
| C14 | C | Push-back prompt collections: `0xelitesystem/ai-coding-prompt-discipline`; dev.to "I tried every ChatGPT prompt list" | undated |
| C15 | C | Pre-merge quiz skills: `merge-quiz` (skills.lc), `melodic-software` `quiz-me` | undated |
| C16 | C | feedough.com, "The 7 Best Matt Pocock Skills" (quotes HN commenters) | 2026-11 |

## 1. Shortcuts that recur, ranked by adoption

The rank weighs three things: how many independent sources mention a shortcut, how recent they
are, and install or star signals. "Status" compares each shortcut with your catalog.

| # | Shortcut (common names) | Evidence (dated) | Status vs your catalog |
|---|---|---|---|
| 1 | **Interview me before building** (`grill-me`, `grilling`, `interview-me`) | C1: `grill-me` 1.5M installs (#2 all-time), `grill-with-docs` 1.3M, `grilling` 1.1M. `addyosmani` `interview-me` 64K installs (C1). F5 suggests having Claude grill you on your changes before a PR. HN: iamwil 50158650 (2026-10-19), michelb 50149140 (2026-10-19). C3: first version 2026-02-25, two sentences long. | Partly covered by `drill` (settles a change) and `ask-user` (structured choice). Neither runs a user interview with a recommended answer per question. |
| 2 | **Commit / PR** (`/commit`, `/create-pr`, `commit-push-pr`) | F7 ships `/commit` (2025-11-20). F13: Cursor's team used commands for PRs and conventional commits (2025-09-12). C9 (2025-09-30) lists `/commit`, `/commit-fast`, `/create-pr`, `/create-pull-request`. C1: `caveman-commit` 426K installs. | Out of scope. It has side effects, and your repositories route delivery through `pnpm deliver`. `caveman-commit` exists. |
| 3 | **Hand off / restart** (`handoff`, `claude-handoff`, `context-save`, "Document & Clear") | C1: `handoff` 1.1M, `claude-handoff` 455K. C8 (2025-11-01): plan to a file, `/clear`, resume. `wshobson/commands` has `context-save`/`context-restore` (C13). HN orbital-decay 50363154 (2026-11-04): a customized handoff still beats the built-in method. | **Not covered.** Candidate `handoff`. |
| 4 | **Terse mode** (`caveman`, "be brief", `tldr`) | C4: 117K stars, 610K installs, HN front page. The 2026-04-29 benchmark found "be brief." matched caveman on tokens and quality. Three small `tldr` repos (C13). | Covered by `tldr`. |
| 5 | **Review my diff** (`/review`, `/pr-review`, `/simplify`) | Built into Claude Code (F2: `/code-review`, alias `/review`, plus `/simplify`). F15 (2026-05-27): consolidating into the built-in `/code-review`. C9 (2025) lists `/pr-review`. | Covered by the harness and `revolver`. |
| 6 | **Prove it works / verify before done** | F5: "Prove to me this works." Built-in `/verify` (F2). `obra/superpowers` `verification-before-completion`. C1: `verify-and-stop` 115K, `verifying-before-done` 21K. | Covered by `bulletproof` and `verify-and-stop`. |
| 7 | **Debug / diagnose / five whys** | Built-in `/debug` (F2). C1: `diagnosing-bugs` 889K, `diagnose` 228K. C9 (2025) lists `/five`. | Covered by `investigate-first` and `dissect`. |
| 8 | **Teach / explain** (`teach`, `explain-code`) | C1: `teach` 912K. C9 (2025) lists `/explain-issue-fix`. | Mostly covered by `dissect` for code. |
| 9 | **Brainstorm options** (`brainstorming`, `design-an-interface`) | C1: `brainstorming` (superpowers) 417K, `design-an-interface` 209K. HN ElatedOwl 44984530 (2025-08-22) asks for "a few more options". HN QuiEgo 47472283 (2026-03-21): deciding between A and B. | `panel` covers choosing. Cheap one-pass generation of options is not covered. Candidate `options`. |
| 10 | **Say that again plainly** (`wait-what`, ELI5) | C1: `wait-what` 495K (C2, 7 lines). HN cjk 49378491 (2026-08-20) uses an "explain like I'm five" phrase after walls of text. `eli5` skills under 2K installs. | **Not covered.** `tldr` cuts content; this rebuilds understanding. Candidate `huh`. |
| 11 | **Capture the lesson** (update CLAUDE.md after a mistake, `retro`, `reflect`) | F5 (used after every correction). C1: `retro` 323K, `reflect` 7.5K. HN olalonde 46726730 (2026-01-23), ckdot 47028352 (2026-02-15). | Covered by `promote`. |
| 12 | **De-slop prose** (`humanizer`, `stop-slop`, `avoid-ai-writing`) | C13: 64.8K and 18.6K stars, both created 2026-01. `avoid-ai-writing` 5.4K stars (2026-03-06). | Next to `debloat`. Better as a pattern list inside `debloat` than as a new skill (inferred). |
| 13 | **Second opinion from another model** | HN thomas_witt 46404813 (2025-12-27), astrange 48053608 (2026-05-07), drbscl 50367676 (2026-11-04). C1: warp `council` 28K, `cross-critique` 22K, trailofbits `second-opinion` 5.5K. | Covered by `revolver` and `panel`. |
| 14 | **Quiz me before merge** (emerging) | F5 says not to make a PR until the user passes Claude's test. HN maximg68 50139509 (2026-10-18) built a quiz skill after a "drop in my understanding" of shipped code. HN recroad 50305937 (2026-10-30). Small community skills (C15). | **Not covered.** Candidate `quiz`. |
| 15 | **Pre-mortem / devil's advocate** (niche) | HN finnworks 48275572 (2026-05-26: Klein's premortem as a skill), avoidboringppl 49758531 (2026-09-18), unsnap_biceps 49927799 (2026-10-01), rse 48761119 (2026-07-02: a devil's-advocate command). C1: `premortem` under 1K installs. | **Not covered.** Candidate `premortem`. |

### What developers abandoned, and why

- **Custom command folders gave way to skills.** Claude Code merged `.claude/commands/` into skills
  (F1). By 2025-12-20 a user with 116 commands and 56 skills saw all of them load into context
  (C10). Steve Klabnik (HN 46873447, 2026-02-03) said Claude Code had folded commands into skills because the two were so similar.
  Codex deprecated `~/.codex/prompts`, and prompts dropped out of the menu by CLI 0.117.0 (F9,
  March 2026). Cursor's `/migrate-to-skills` (2.4+) turns commands into skills with
  `disable-model-invocation: true` (F12).
- **Big command suites lost out to small packs (inferred from C13 and C9).** `wshobson/commands`
  (2.6K stars) and `qdhenry/Claude-Command-Suite` (1.3K, no push since 2026-03-01) stalled while
  `mattpocock/skills` reached 313K. awesome-claude-code had a "Slash-Commands" section on
  2025-09-30 and none on 2026-11-04 (C9).
- **The harness absorbed some shortcuts.** `ultrathink` was deprecated around January 2026
  (C11, #19098), restored around v2.1.68, and as of v2.1.316 (2026-10-31, third-party report)
  sets xhigh effort. Personal `/review` commands give way to the built-in `/code-review` (F15).
  Built-ins now include `/btw`, `/recap`, `/goal`, `/focus`, `/simplify`, and `/verify` (F2).
- **Elaborate terse modes lost to the one-liner.** The 2026-04-29 benchmark tied caveman with
  "be brief." (C4). HN ryanschaefer 47647955 (2026-04-05) said the trigger list could be a regex
  hook.
- **Interview skills can overshoot.** Grilled plans can become "overly prescriptive" (HN pwm
  50256740, 2026-10-27). Quick "yes" answers let the model decide things nobody examined (C3).
  feedough.com quotes HN users saying scope kept growing (C16; secondary, the comments were not
  found).
- **Standing push-back rules backfire.** Persistent "push back when I'm wrong" instructions
  produced one-upmanship (HN tstrimple 50312661, 2026-10-31). That argues for an on-demand
  invocation (inferred).

## 2. Design lessons for tiny skills

### First-party facts

- **Who invokes.** In Claude Code, `disable-model-invocation: true` takes the description out of
  context and blocks Claude from calling the skill. `user-invocable: false` does the reverse (F1).
  F1 recommends the flag for side effects or "control timing". Cursor honors the same field (F12).
  Codex needs `agents/openai.yaml` with `policy.allow_implicit_invocation: false`; explicit
  `$skill` invocation still works (F8). The Gemini CLI docs list no user-only flag. Skills are
  model-activated through `activate_skill`, and custom commands are separate TOML files (F10, F11).
- **Listing cost.** Claude Code caps the skill listing at 1% of the context window. Each entry's
  `description` plus `when_to_use` is cut at 1,536 characters. On overflow, descriptions of the
  least-used skills go first. `/doctor`, `/skill-doctor`, and `skillOverrides: "name-only"`
  manage the cost (F1). Codex allows 2% of context, or 8,000 characters if the window is unknown,
  and shortens descriptions first (F8). The spec estimates about 100 tokens of metadata per skill
  (F3). A user-invoked skill in Claude Code costs nothing per turn (F1).
- **Names and collisions.** The spec allows lowercase letters, digits, and single hyphens, up to 64
  characters, and the name must match the directory (F3). The Claude API reserves `anthropic` and
  `claude` in names (F4). In Claude Code, a personal or project skill **replaces** a built-in or
  bundled command with the same name, but not its aliases (F1). Claude Code built-ins a micro skill
  could shadow include `/btw`, `/recap`, `/plan`, `/goal`, `/focus`, `/review`, `/simplify`,
  `/verify`, `/debug`, `/fork`, `/branch`, `/diff`, `/context`, `/insights`, `/stop`, and `/run`
  (F2). The Codex app has `/review`, `/plan`, `/goal`, `/init`, and `/status` (F14). Gemini
  namespaces subfolders with colons, and project commands override user ones (F10). Plugin skills
  are always namespaced (F1).
- **Where the name must go.** Claude Code recognizes a command only at the start of a message, and
  up to six can be chained (F2). HN AlexErrant 50123445 (2026-10-16) hit exactly this. Codex
  accepts a `$name` mention (F8).
- **Arguments.** If a body has no `$ARGUMENTS` placeholder, Claude Code appends
  `ARGUMENTS: <value>` (F1). A body that says "the target the user named, else X" therefore works
  in every harness without a placeholder (inferred).
- **Shared folders.** Codex reads `~/.agents/skills` (F8). Gemini reads `~/.agents/skills` and
  `.agents/skills` (F11). Cursor reads `~/.agents/skills`, `~/.claude/skills`, and
  `~/.codex/skills` (F12). Your `~/.claude/skills/*` are symlinks into `~/.agents/skills`
  (`ls -la`, 2026-11-05). So one file serves every harness, but only Claude Code and Cursor read
  `disable-model-invocation`.
- **Writing descriptions.** Use the third person, say what the skill does and when to use it, and
  put the key use case first (F4, F1). Authoring guidance puts the body under 500 lines and asks
  for evals before prose (F4).

### Community findings

- **Automatic triggering is unreliable, so a micro skill should not depend on it.** In Vercel's
  evals the skill was never invoked in 56% of cases (C5, 2026-01-29). Spence reached 84% only with
  a forced-eval hook (C6). Seleznov found hooks could *lower* activation (C7). A user-invoked skill
  avoids the problem.
- **Thin aliases.** `grill-me` is 7 lines that point at the model-invocable `grilling` (C2). That
  gives a short trigger and keeps the method reusable. The cost: the alias breaks when installed
  alone (C3, 2026-10-14), and its wording ("Call the Skill tool") is Claude-specific. For your
  multi-harness setup, self-contained 3–6 line bodies are safer (inferred).
- **Tiny skills drift.** `grill-me` went from two sentences (2026-02-25) to frontier rounds with
  sub-agents (2026-07-16) to yes-accepts phrasing (2026-10-07) (C3). Re-check copied skills
  against their source.
- **Harness absorption.** A popular shortcut tends to become a built-in (F15, C11). Before adding
  a micro skill, check `/help` in each harness, and retire skills the harness has absorbed.

### Lessons applied to the drafts below

1. Each draft is user-invoked (`disable-model-invocation: true`). For Codex, add
   `agents/openai.yaml` with `policy: {allow_implicit_invocation: false}`. For Gemini, which has no
   flag, the description says "Use only when the user asks…" so that auto-activation stays narrow.
2. No name collides with the Claude Code, Codex, or Gemini built-ins listed above. I avoided
   `recap`, `plan`, `review`, `verify`, `fork`, `focus`, `goal`, `btw`, `simplify`, and `debug`.
3. Bodies are 3–6 self-contained lines that act on "the named target, else the current
   reply/branch". They do not need `$ARGUMENTS` and do not call other skills.

## 3. Candidates not covered by your nine

Excluded because something already covers them: interview-me (`drill` + `ask-user`), commit/PR
(delivery scripts, `caveman-commit`), terse mode (`tldr`), review and second opinion (`revolver`,
`panel`), verify (`bulletproof`, `verify-and-stop`), debug (`investigate-first`, `dissect`),
lesson capture (`promote`), de-slop (add a pattern list to `debloat`).

Ranked by evidence strength, then by how clearly each differs from your catalog.

### 1. `quiz`: make sure I understand what is about to merge
Evidence: F5 (first-party tip). HN maximg68 (2026-10-18) and recroad (2026-10-30). Community
quiz skills (C15). Adjacent `teach` has 912K installs (C1). It addresses comprehension debt, which
HN users raised in 2026-10 (inferred).
```markdown
---
name: quiz
description: Quiz the user on a diff or branch before they merge it. Use only when the user asks to be quizzed on a change.
disable-model-invocation: true
---
Quiz me on the change I named, or on the current branch against its base if I named none.
Ask one question at a time about behavior that could break, not trivia, and wait for my answer.
Ground each question in a file:line I can open; after I answer, say right or wrong and cite the line.
Stop after five questions or when I say stop, then list what I missed as what to reread before merging.
Do not edit code.
```

### 2. `handoff`: write the restart brief for a fresh session
Evidence: C1 (`handoff` 1.1M, `claude-handoff` 455K, both from C2). C8 (2025-11-01). HN
orbital-decay (2026-11-04). It differs from the built-ins `/recap`, `/compact`, and `/fork`
because it writes a file another harness can read. It differs from `promote`, which writes
durable records.
```markdown
---
name: handoff
description: Write a restart brief so a fresh session or another agent can continue this work. Use only when the user asks for a handoff.
disable-model-invocation: true
---
Write a restart brief for an agent that cannot see this conversation; focus it on what I named, if anything.
Include the goal, what is done and verified, what is not, the next concrete step, open decisions, and traps found.
Point to existing files, commits, pull requests, and issues by path or URL instead of copying them.
Leave out secrets and personal data. Save it in the OS temporary directory, not the repository, and print the path.
```

### 3. `catchup`: rebuild context from the branch after `/clear`
Evidence: C8 (2025-11-01, `/clear` then `/catchup`, picked up by AI Engineering Report). C9
(2025-09-30) lists `/context-prime` and `/prime`. C1: `catchup` skills, 1.3K installs at most.
This is the reading half of `handoff`. It differs from built-in `/recap`, which summarizes the
conversation rather than git (F2).
```markdown
---
name: catchup
description: Rebuild working context from the current branch after a cleared or new session. Use only when the user asks to catch up.
disable-model-invocation: true
---
Read the current branch's commits and uncommitted changes against its base, plus any brief path I named.
Read each changed file in full, not only the diff hunks.
Then report in five lines or fewer: what the branch does, what looks finished, what looks unfinished, and the first open question.
Do not edit anything.
```

### 4. `huh`: say that again so I follow it
Evidence: C1 (`wait-what` 495K installs, 7 lines, C2). HN cjk (2026-08-20). C1: several `eli5`
skills. It is the inverse of `tldr`: it may get longer to restore context, but no more complex.
```markdown
---
name: huh
description: Re-explain the previous reply because it did not land. Use only when the user says they did not follow it.
disable-model-invocation: true
---
Your last reply did not land. Say it again for someone who has not followed the details.
Open with one sentence on what we are doing and why this point matters now.
Use plain words and the project's own terms; define any other term at first use.
Give one concrete example. Add no new claims, and drop nothing that changes a decision.
```

### 5. `scrap`: redo it the simple way with what you now know
Evidence: F5 is a first-party tip that tells Claude to throw out a mediocre first attempt and
build the elegant version. C14: "tell me if I'm overengineering this". HN Escapade5160 49303822 (2026-08-14) and
tamimio 47881618 (2026-04-23) complain of piled-on scope. It differs from built-in `/rewind`,
which restores a checkpoint without redesigning.
```markdown
---
name: scrap
description: Discard the current attempt and rebuild it the simple way using what the session has learned. Use only when the user asks to scrap and redo.
disable-model-invocation: true
---
Treat the current attempt as a throwaway draft; do not patch it.
First state in three lines what it got wrong, the simplest correct design, and what you will keep from it.
Then rewrite the change to that design, keeping the behavior I asked for and nothing else.
Rerun the checks you ran before and report any whose result changed. Do not rewrite git history.
```

### 6. `premortem`: assume it failed, then say why
Evidence: HN finnworks (2026-05-26), avoidboringppl (2026-09-18), unsnap_biceps (2026-10-01).
C1: `premortem` under 1K installs, a niche but recurring idea. It differs from `bulletproof`,
which checks stated claims, and from `revolver`, which reviews an artifact. This one imagines
failure modes before work starts.
```markdown
---
name: premortem
description: Imagine a plan or change has failed and name the likely causes before committing to it. Use only when the user asks for a premortem.
disable-model-invocation: true
---
Assume the plan or change I named (or the current one) shipped and failed badly three months later.
Name the three most likely causes, most likely first, each specific to this work; skip risks that fit any project.
For each, give the earliest sign it is happening and the cheapest check or change that would prevent it now.
```

### 7. `overreach`: list what you did that I did not ask for
Evidence: HN Escapade5160 (2026-08-14) on constant scope creep. C16 quotes HN users on scope
growth (secondary). C14 collects prompts that keep the agent in scope. Your `lean-build` and `surgical-patch` guard
scope *while* building; this one audits afterwards.
```markdown
---
name: overreach
description: List every change that goes beyond what the user asked for. Use only when the user asks for a scope or overreach check.
disable-model-invocation: true
---
Compare what I asked for in this session with everything you changed: code, behavior, dependencies, config, docs.
List each change I did not ask for, with file:line and one line on why you made it.
Mark each keep (the request needs it) or revert (optional).
Revert nothing until I answer.
```

### 8. `options`: show me real alternatives before committing
Evidence: C1 (`brainstorming` 417K, `design-an-interface` 209K). HN ElatedOwl (2025-08-22) and
QuiEgo (2026-03-21). It overlaps with `panel`, which runs independent analyses. This is the cheap
single-pass version for choices that are not consequential. If you want fewer skills, fold it
into `wdyt`.
```markdown
---
name: options
description: Lay out genuinely different approaches before committing to one. Use only when the user asks for options.
disable-model-invocation: true
---
Before choosing, give two or three approaches to what I named (or the current problem) that differ in kind, not detail.
For each, give one line each on how it works, what it costs, and what it rules out later.
Include the smallest change, or doing nothing, if either is viable.
End with your pick and the one fact that would change it.
```

### 9. `pushback` (marginal): what is wrong with what I just asked?
Evidence: C14 (a one-line trigger asking what is wrong with the request; the dev.to author called
asking for push-back their biggest upgrade). HN tstrimple (2026-10-31) found that a *standing* push-back rule caused
one-upmanship, which favors on-demand use. It is marginal because it sits close to `wdyt` and
`bulletproof`.
```markdown
---
name: pushback
description: Challenge the user's latest request before acting on it. Use only when the user asks for pushback.
disable-model-invocation: true
---
Before doing what I just asked, name the part most likely to be wrong and the decision I made without noticing.
Give the reason in one sentence and the alternative in one sentence.
If you find nothing specific, say so in one line; do not invent objections. Then wait for my answer.
```

**Portability note for every draft.** Add `agents/openai.yaml` beside each `SKILL.md`:

```yaml
policy:
  allow_implicit_invocation: false
```

Codex then keeps the skill explicit-only (F8). Claude Code and Cursor read the frontmatter flag
(F1, F12). Gemini has no documented equivalent, so it relies on the narrow description (F11).
