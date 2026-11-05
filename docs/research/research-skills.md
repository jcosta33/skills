# Skills research: method skills and authoring craft

Date: 2026-11-05. Scope: general method skills and skill-authoring craft (descriptions, triggering,
size, evals, failure in practice). Out of scope: artifact and spec-workflow skills (Corpus session),
micro-skill candidates (coordinating session), philosophy and argumentation theory.

Catalog under review (`jcosta33/skills` at `d598610`): `bulletproof`, `debloat`, `dissect`, `drill`,
`panel`, `revolver`, `settle`, `tldr`, plus `wdyt` (held).

Method: three Opus research subagents (first-party docs, community catalogs, developer feedback),
then my own check of the load-bearing sources. The full dated notes (first-party, community, and
feedback; one claim per line with URL and tag) stay outside this repository.

Tags: **FP** = first-party fact. **CM** = community, measured (self-reported unless stated). **CO** =
community opinion or author claim. **Checked** = I re-read the primary source on 2026-11-05.

Coverage gaps: Reddit blocks fetching, so forum opinion comes from Hacker News, GitHub, and blogs.
Seleznov's "650 trials" post returned 403; its numbers come from two secondary write-ups that
disagree on the baseline. Anthropic's "Complete Guide to Building Skills" PDF could not be
extracted. Almost every anthropics/claude-code skills issue was bot-closed without a maintainer reply.

## Top 5 recommendations

1. **Test every verification-shaped skill against Opus 5's own verification, and record tokens and
   time.** The Opus 5 prompting guide says the model "verifies its own work without being told to".
   It says to remove instructions like "use a subagent to verify", which "cause over-verification".
   It also says not to instruct re-checks it already performs. That hits `bulletproof`, `revolver`,
   and `panel` directly.
   - FP, Checked: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5 (undated).
   - CM: arXiv 2608.11888 (2026-08-12, OpenCode with Opus 4.6): 114 of 182 efficiency regressions
     came from excess procedure, 67 of them from excessive verification.
   - CM: SWE-Skills-Bench, arXiv 2603.15401 (v2, 2026-10-27): 92 of 98 skills had no
     statistically significant effect; the pass ratio moved from 76.6% to 76.9%. (Corrected from
     v1's "39 of 49 gave zero pass-rate gain"; see the corrections in
     [engineering-meaning-empirical.md](engineering-meaning-empirical.md).)
   - CM: superpowers v5.0.6 (2026-03-24) dropped subagent review loops on plans after "5 versions
     with 5 trials each showed identical quality scores" at about 25 minutes of overhead. Plans,
     not code.
   - Counterweight. The same guide says Opus 5 runs "effective writer-verifier patterns". Our round-1
     test also showed `revolver`'s method beat a one-liner on structure, not on bugs found: all arms
     found all five planted bugs.
   - Action:
     - Add tokens and wall time to the with/without record.
     - Run a planted-defect eval where a single Opus 5 pass is the baseline. Compound Engineering's
       reversed-commit harness with a blind 3-vote judge is a ready template (CM).
     - Keep a skill only where it finds more than one pass at an acceptable cost.
     - Give `bulletproof` a stakes clause, so it is for claims someone will act on.

2. **Write method-skill descriptions for under-triggering: lead with the user's own words, and say
   the skill applies even when the model could do the job alone.** Method skills lack a distinctive
   token, so the common failure is that no skill fires at all; a wrong skill firing is rare.
   - CM, Checked: addyosmani/agent-skills evals (claude-opus-5-5 pinned, page undated). One clause
     ("applies even when the diff is pasted inline") moved review fires from 7/27 to 21/27, with
     must-not-fire prompts at "0 of 27 both ways". "Describing what the skill adds did not help."
   - CM: Tessl (2026-04-15): skills activated in 41% of 2,286 tasks unforced, 98% forced.
   - CM: Coder Eval (2026-07-30, 1,001 prompts, 20 skills): an "Always invoke for [unique tokens]"
     sentence raised recall from 46% to 67%. Its cross-cutting `review` skill, with no unique token,
     stayed near 0.2.
   - FP: Anthropic's skill-creator says Claude tends to "undertrigger" and recommends "pushy"
     descriptions.
   - FP, Checked: Claude Code caps each listing entry at 1,536 characters. The listing budget is 1% of
     context, and on overflow it drops the least-invoked skills' descriptions first. Docs say to put
     "the key use case first".
   - Action:
     - Rewrite the "Use when" clause of `drill`, `dissect`, `bulletproof`, `revolver`, and `panel`
       in the user's literal phrasing ("who calls", "double-check", "review this", "which
       option").
     - Add an "even when" clause where the model believes it can do the work itself.
     - Measure each with the first-party method below before keeping the change.

3. **Adopt the first-party trigger eval as the gate for description edits.**
   - FP: skill-creator and agentskills.io: about 20 queries, half of them near-miss negatives, 3 runs
     each, a 0.5 threshold, a 60/40 train/validation split, about 5 iterations.
   - FP, Checked: Claude Code docs describe `claude plugin eval` with a `tool_used: Skill` grader.
     The skill-creator runs with/without benchmarks on pass rate, time, and tokens, and blind A/B
     version comparison.
   - Pairs to test for collisions: `bulletproof` vs `dissect` vs `revolver`; `panel` vs `settle`;
     `drill` vs `dissect`.
   - Our current with/without test checks behavior after activation, not whether the skill
     activates. This adds the missing half.

4. **Stop relying on frontmatter outside the spec, or accept that `tldr` is a Claude Code, Cursor,
   and Copilot skill.**
   - FP, Checked: claude.ai uploads, the Skills API, and `package_skill.py` accept only the six spec
     fields. Others fail with "Unexpected key(s) in SKILL.md frontmatter".
   - FP, Checked: Cursor honours `disable-model-invocation`.
   - FP: VS Code Copilot honours it too. Codex (`parser.rs`, 2026-08-17) and Gemini CLI
     (`skillLoader.ts`, 2026-10-15) read only `name` and `description` and drop the key. The
     `skills-ref` validator rejects it (PR #350 to allow it is open).
   - CM: open Claude Code bugs where a gated skill refuses an explicit `/name`: #78523 (since
     2026-07-17) and #95469.
   - The README now states this (commit `d598610`).
   - Options:
     - (a) Keep the key and write `tldr`'s description so self-invocation is harmless.
       Recommended: it already is.
     - (b) Drop the key and use the Claude Code user setting `skillOverrides` with
       `user-invocable-only` instead (FP).
   - Cheap lint additions:
     - reject `<` and `>` in descriptions (Anthropic's validator rejects them; Claude Code renders
       them as entities, FP, Checked);
     - reject any frontmatter key other than the spec fields and the one allowed key.

5. **Fill one canonical gap: hypothesis-ranked root-cause debugging.** It is the most replicated
   method skill across popular catalogs, and nothing in this catalog ranks hypotheses for an
   unknown cause. `dissect` proves how a known path flows. `bulletproof` checks stated claims.
   - CO/CM: superpowers `systematic-debugging` (v7.0.2, 2026-11-03), mattpocock `diagnosing-bugs`,
     addyosmani `debugging-and-error-recovery`, Compound Engineering `ce-debug`. The shared core:
     reproduce until a check fails, before any fix.
   - On this machine an `investigate-first` skill from another source already covers it (installed
     in `~/.agents/skills`). Decide whether to adopt, slim, or leave it outside this catalog. Do not
     write a second one.
   - Not recommended: TDD as a skill. CM: arXiv 2602.07900 (2026-02-08, SWE-bench Verified, 6
     models) found no significant effect from changing test instructions (p > 0.05). Practitioners
     report it works better as a hook or standing rule (CO).

## Q1: what to change in the existing skills

| Skill | Change | Evidence | Strength |
| --- | --- | --- | --- |
| all | No "prefer this over X" text. Keep the no-sibling-names rule. | agentskills discussion #404 (2026-05-24 to 26; 14 skills, 50 trials per query): adding "Prefer over X" cut Sonnet 4 from 100% to 85% and Haiku 4.5 from 93% to 67%. Opus 4 was unchanged. | CM, Checked |
| all | Prefer recipes over prohibitions for output shape. | Opus 5 guide: "Positive examples of the communication style you want tend to be more effective than instructions about what not to do" (FP, Checked). superpowers writing-skills (2026-10-21): prohibitions on shape produced more of the banned content (CM, no counts). | FP + CM |
| all | Exclusion clauses ("Do not use…") are unmeasured. Keep each only if a should-not-fire test shows it matters. | No measurement found in any source. | gap |
| all | Phrase rules as standing rules for the whole task. Skills are not re-read after the first turn, and after compaction only the first 5,000 tokens per skill, 25,000 in total, are re-attached. | Claude Code docs (FP, Checked). Our skills are under 30 lines, so truncation never bites. Standing phrasing does. | FP |
| `settle` | Measure trigger rate. "Before asking the user anything" is an every-turn rule, which first-party docs route to CLAUDE.md or hooks. José's global CLAUDE.md already carries the authority rule. Candidate line: ask "why" before "which". | Claude Code docs: rules that must hold every time belong in a hook (FP, Checked). superpowers v7.0.2: bare "which one?" in 8 of 8 runs before, options with a recommendation in 8 of 8 after; asking "why" first rose from 28/33 to 33/33 (CM, self-reported). | FP + CM |
| `revolver` | Keep the bar on findings in the orchestrator's verification step, not in reviewer briefs. | Opus 5 guide: a review prompt asking for only high-severity issues makes the model "report less"; "ask it to report everything and filter in a separate pass" (FP, Checked). Codex review-agent's bar ("introduced by the reviewed change", "Do not flag … pre-existing problems") fits the filter step (FP). | FP |
| `revolver`, `panel` | Consider `disable-model-invocation: true`. Both are costly and Opus 5 delegates readily. | Opus 5 guide: "Claude Opus 5 delegates to subagents more readily"; cap delegation (FP, Checked). Same portability caveat as `tldr`. | FP |
| `bulletproof` | Add a stakes clause to the description; test against Opus 5's built-in self-check. | Recommendation 1. Anthropic's new `discernment-nudge` (2026-08-17) covers the same ground for user-facing work (FP). | FP |
| `debloat` | Candidate step: flag contradictory or outdated rules, not only duplicates. | `/doctor prompt-audit` checks for "outdated or conflicting instructions" (FP). Not yet tested against our skill. | FP |
| `tldr` | Description is 200 characters, right at the conflicting claude.ai help-center limit (the help center says 200; the docs and spec say 1,024). Six other descriptions exceed 200. Only matters for claude.ai uploads. | First-party sources conflict (FP vs FP). | conflict |
| `wdyt` (held) | Do not ask for written-out reasoning or an "inner monologue" in the response. Ask for the position, the reasons, and the dissent as a short explanation. | Opus 5 guide: skills asking the model "to write its thinking or reasoning, verbatim or in a fixed format, might be declined" (`reasoning_extraction`) (FP, Checked). | FP, flag to the coordinating session |

## Q2: canonical method skills the catalog lacks

| Candidate | Who ships it | Nearest skill here | Verdict |
| --- | --- | --- | --- |
| Hypothesis-ranked debugging | superpowers, mattpocock, addyosmani, Compound Engineering | none (`dissect` traces known paths) | Gap. See recommendation 5; `investigate-first` is already installed from elsewhere. |
| Skill authoring and trigger eval | Anthropic skill-creator, Codex, Gemini CLI, Cursor | none | Gap for a skills repo, but the first-party skill-creator exists. Adopt its method in AGENTS.md rather than writing a skill. |
| Receiving review feedback (weigh incoming PR comments before applying) | superpowers `receiving-code-review` | partly `bulletproof` | Plausible. Popularity evidence only (CO). |
| Interview before building | mattpocock `grill-me` (#2 on skills.sh, 1.5M installs), superpowers brainstorming | opposite of `settle` | Deliberately absent. `settle` minimizes questions. Popularity is not effect (SWE-Skills-Bench). |
| Single-pass, defect-first diff review | Claude Code `/code-review`, Codex review-agent, Cursor `/review` | `revolver` (exhaustive) | Covered by built-ins. Not needed here. |
| Simplify, verify-by-running, security review, split into PRs | Claude Code `/simplify`, `/verify`, `/run`, `/security-review`, `/batch`; Cursor `/split-to-prs` | none | Built into the harnesses. Do not duplicate. Avoid naming a skill `verify` or `simplify`: Claude Code runs project skills with those names before commits (FP). |
| Condition-based waiting, defense in depth, root-cause tracing (backward) | superpowers (inside systematic-debugging) | none | Fold into the debugging decision; not separate skills. |
| TDD | superpowers, mattpocock, addyosmani, karpathy | none | Not a skill: no measured effect (arXiv 2602.07900). Better as a hook. |
| Session handoff, retro, throwaway prototype | mattpocock | none | Low evidence (CO). Handoff would break the no-document rule unless it answers in chat. |

## Conflicts noted

- superpowers says descriptions should be "Use when…" triggers only, with no workflow. AGENTS.md
  requires the action as well. The superpowers basis is one anecdote. The addyosmani data says
  describing what the skill adds did not help trigger rates, but did not hurt either. Keep the
  action clause until a trigger eval says otherwise.
- Compound Engineering names sibling skills in descriptions; AGENTS.md forbids it. The only
  measurement (discussion #404) is on "prefer over" text and supports the ban.
- First-party description limits: spec and docs 1,024 characters, claude.ai help center 200.
  Unresolved without a real upload.
