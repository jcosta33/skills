# `jcosta33/skills`: proposed shape

Proposal. Nothing in the repository was changed. It builds on a study map kept outside this
repository. Repo paths are relative to the repository root at `6c27a52`.

**Where the evidence stands.** The verdicts below are judgments, not measurements. Here is what backs
them:

- The failure each skill names comes from repo history, the source ledger (`docs/sources.md`), or the
  owner's own global rules (`~/.claude/CLAUDE.md`).
- Nobody has measured any skill against a bare model. The one recorded eval covered `fork-me` only
  (`git show 2395893:evals/results/2026-08-01-target.tsv`).
- The draft skills below pass the repo's frontmatter, self-name, and sibling-name checks, run by hand
  against `/tmp/skills-shape-drafts/`. The only hits were the plain verb "settle", which is harmless
  once the `settle` skill is gone.
- How to test the hypothesis properly is at the end of §1.

## Summary

12 skills become 7, and 422 lines become about 108 (2,862 words become 1,051). Merges:

- `settle` into `ask-user`
- `dissect` into `bulletproof`
- `triple-check` into `revolver`
- `remember` into `promote`

`demolition` is cut. The 7 design docs collapse into the README, `AGENTS.md`, and one trimmed
sources file. The 384-line lint shrinks to its structural core. The changelog-digest gate and `evals/`
go. The repo stays `jcosta33/skills`, with no framework brand.

## 1. Per-skill verdicts

What each skill is measured against: a frontier model given one line of instruction. A skill earns its
keep only if it names a failure that model still commits.

| Skill | Verdict | Failure a bare model commits | Grounds |
| --- | --- | --- | --- |
| `ask-user` | **Keep, shrink, absorb `settle`** | Asks the user about things evidence could answer; ends turns with "should I…?"; quietly picks product behavior instead of asking. `settle` is the other half of the same moment: decide what evidence can decide, ask only about what the user owns. | OpenCode baseline "asked a bare repository question" (`git show 6df5ae5:evals/results/2026-08-01-baseline.tsv`); owner had to add "Never end a turn on a question while work remains" (`~/.claude/CLAUDE.md`, Authority); ConInstruct: models detect conflicts but rarely ask (`docs/sources.md:102-104`) |
| `settle` | **Merge into `ask-user`** | Same moment as `ask-user`. Merging removes two `ALWAYS` triggers that fire together (`skills/ask-user/SKILL.md:3`, `skills/settle/SKILL.md:3`) | Its unique rules (evidence over popularity or agreement; the list of human-owned matters) fit in 2 lines |
| `bulletproof` | **Keep, shrink, absorb `dissect`** | Marks claims "verified" from its own reasoning; treats "couldn't find" as "false"; says "nothing calls this" after one grep; misses dynamic dispatch | Self-correction without external feedback degrades (`docs/sources.md:119-121`); models agree when wrong (`:125-127`); fabricated citations (`:135-137`). Cut: the "Implementation Proof" branch (`skills/bulletproof/SKILL.md:23-25`), a one-line restatement of generic evidence practice |
| `dissect` | **Merge into `bulletproof`** | The distinct failure: reachability inferred from symbol search, and silence taken as absence. That is one line inside a verification skill. The 8-step trace list (`skills/dissect/SKILL.md:12-23`) is what a frontier model already does when asked to trace | — |
| `debloat` | **Keep, shrink** | When compressing, silently drops a number, constraint, or warning | Lossy compression damaged exact anchors (`docs/sources.md:72-74`); compression effects vary by task (`:99-101`). The rhetoric line "Make every token command respect" (`skills/debloat/SKILL.md:8`) changes nothing; cut |
| `demolition` | **Cut** | It fires only on an explicit request (`skills/demolition/SKILL.md:3`), and the request already says "argue against it". The residual failures (adding balance, fabricating sources) are one sentence the user can say. The quarantine banner is ceremony | Sycophancy (`docs/sources.md:128-129`) argues for a stronger user prompt, not a resident skill |
| `drill` | **Keep, shrink** | Starts coding before the change is named, its guarantee stated, or its location fixed; duplicates an existing rule instead of calling it; writes a plan document instead of the next slice | Owner-authored method with a credited source (`docs/sources.md:195-197`, `6c27a52`). Trigger rewritten into task language; `ALWAYS` dropped; framework name removed (`skills/drill/SKILL.md:29`) |
| `panel` | **Keep, shrink** | Without the skill, a model answers "compare options" in one pass, anchored and correlated with itself. It does not spawn blind, concurrent analysts or keep the strongest dissent | Debate gains are bounded (`docs/sources.md:144-146`); aggregation rule matters (`:147-149`); problem drift (`:150-152`); correlated errors (`:125-127`) |
| `promote` | **Keep, shrink, absorb `remember`** | Copies transient content into the repo still carrying secrets, private absolute paths, or scratch metadata; leaves broken links; duplicates an existing record; invents a destination | The repo's own transient-artifact lifecycle (`suspec:skills/README.md:30-32`). `remember`'s personal-memory rules are mostly in the harness already (Claude Code's system prompt defines memory), so one line survives |
| `remember` | **Merge into `promote`** | Same intent, durability. `skills/remember/SKILL.md:22-24` (write team facts to project channels) already overlapped `promote` | — |
| `revolver` | **Keep, shrink, absorb `triple-check`** | Asked to "review this", the model reviews its own work in its own context: no fresh reviewer, the author's reasoning visible, prior comments priming later ones | Self-preference (`docs/sources.md:130-131`), priming (`:172-174`), self-correction limits (`:119-121`), cost of multi-agent work (`:175-178`) |
| `triple-check` | **Merge into `revolver`** | Same job, review then repair; only the dispatch differs. The Output paragraphs are identical (`skills/revolver/SKILL.md:38-40` vs `skills/triple-check/SKILL.md:28-30`). The merged skill offers "fast" (3 parallel) and "exhaustive" (sequential stances) | — |

The merges also clear the collisions found in the map:

- `settle` vs `panel`: `settle` moves into `ask-user`, and `panel`'s trigger now requires that
  "evidence alone cannot pick one".
- `promote` vs `remember`: one skill.
- `revolver` vs `triple-check`: one skill, two modes.
- The three `ALWAYS` triggers: only `ask-user` keeps one, because it must fire before the question is
  asked.

**Testing the hypothesis** (an engineering call, so decided here). Before release:

- For each survivor, take one witnessed real task.
- Run it twice in fresh sessions: once with a one-line instruction, once with the skill.
- Keep a line only if the behavior differs.
- Record the result in the commit message (see §3, `evals/`).

## 2. Draft `SKILL.md` for each survivor

Line counts: "before" is the current file(s); "after" wraps body prose at 100 columns, the repo's
habit, and keeps the description on one line as the lint requires
(`scripts/lint-current.sh:121-129`).

| Survivor | Before (lines / words) | After (lines / words) |
| --- | --- | --- |
| `ask-user` | 18 / 154 + `settle` 27 / 212 | 15 / 158 |
| `bulletproof` | 48 / 233 + `dissect` 47 / 256 | 16 / 149 |
| `debloat` | 31 / 222 | 12 / 104 |
| `drill` | 34 / 263 | 17 / 181 |
| `panel` | 37 / 290 | 14 / 131 |
| `promote` | 42 / 293 + `remember` 35 / 240 | 16 / 150 |
| `revolver` | 45 / 350 + `triple-check` 30 / 229 | 18 / 178 |
| (`demolition`, cut) | 28 / 120 | 0 |
| **Total** | **422 / 2,862** | **108 / 1,051** |

### `skills/ask-user/SKILL.md`

```markdown
---
name: ask-user
description: Decide what evidence can decide, and turn what only the user can decide into a structured choice. ALWAYS use before asking the user anything, and when work would stop for a technical question, conflicting evidence, or an unmade choice. Do not use to answer the user's own factual questions.
---

# Ask User

- Settle technical, procedural, and reversible choices yourself from code, tests, project precedent, and primary docs. Popularity and model agreement are not evidence. Act, then state the decision and its decisive evidence in one line.
- Ask only about intent, public behavior, material security or cost tradeoffs, waivers, irreversible actions, or acceptance.
- Ask as a choice: native picker, else a numbered list. Recommendation first, three options (two if binary), one reason and cost each, plus Other. Freeze only the work that depends on the answer.
- Never end a turn on "should I" or "want me to" while work remains.
```

### `skills/bulletproof/SKILL.md`

```markdown
---
name: bulletproof
description: Verify claims or trace a code path against direct evidence before anyone relies on them. Use when a statement, citation, completion claim, or story about how code flows needs proof. Do not use for broad risk review or for arguing one side.
---

# Bulletproof

- Freeze the claims or code question and the repository state. Decide what would prove and what would refute each item before looking.
- Prove only with sources you open or commands you run: primary sources for external facts, `file:line` for code. Reasoning, memory, and agreement are not proof.
- For code, include dynamic dispatch, string registration, generated code, configuration wiring, and async continuations. Symbol search does not prove reachability. "Nothing calls this" needs the search command and its result.
- Return one table: item, `Supported` / `Unsupported` / `Unverified` / `Blocked`, evidence. `Unverified` and `Blocked` name the exact gap.
```

### `skills/debloat/SKILL.md`

```markdown
---
name: debloat
description: Tighten supplied prose without losing any fact, rule, or warning. Use when a document, instruction file, or message is repetitive, hedged, or padded. Do not use for source code, commit messages, or forms a repository prescribes.
---

# Debloat

1. Before editing, list every fact, rule, command, identifier, warning, and required heading the text carries.
2. Give each item one home. Cut duplicates, recaps, hedges, pleasantries, and sentences that change no action or decision. In agent instructions, cut rules that restate default behavior.
3. Check the result against the list and restore anything missing. Edit in place; return the path.
```

### `skills/drill/SKILL.md`

```markdown
---
name: drill
description: Settle what a change is called, what it guarantees, where it lives, and its smallest write before writing code. Use when a change starts while its meaning, guarantee, or location is unsettled, or when implementation has begun without them. Do not use for a multi-stage migration that needs a staged plan with rollback.
---

# Drill

Lock one level at a time. If a higher level moves, drop the work below it. Never ask a lower-level question while a higher one is open.

1. **Language.** Name it in the project's words.
2. **Obligation.** What a caller can now rely on that they could not before, and what must stay true; how each is verified and rolled back. A guarantee does not decide its machinery.
3. **Place.** Exact files, symbols, and runtime boundary. Trace unproven coupling first.
4. **Slice.** The smallest write that keeps the obligation. Find the existing rule and call it; duplicate only with a named reason, and proximity is not one. Write, verify, then drill the next slice. Notes stay native; write no plan document.
```

### `skills/panel/SKILL.md`

```markdown
---
name: panel
description: Recommend one option after independent analyses of real alternatives. Use when a consequential technical, product, or operational choice has several defensible options and evidence alone cannot pick one. Do not use when evidence already decides it or the user has stated a decision.
---

# Panel

1. Fix one question, the evidence packet, the constraints, and who decides.
2. Launch fresh subagents concurrently on the cheapest capable model: the count the user names, else the fewest that cover every material perspective. None sees another's analysis.
3. Check load-bearing claims against direct evidence; agreement is not evidence. Settle at most one decisive conflict with one follow-up.
4. Answer in chat: recommendation first, a comparison table on shared criteria, the strongest surviving dissent, and what would reverse the call.
```

### `skills/promote/SKILL.md`

```markdown
---
name: promote
description: Make a verified lesson or a working document durable in the right place. Use when a lesson must outlive the session or a transient file must become a project record. Do not use for unverified observations or for moves between scratch locations.
---

# Promote

- Personal lesson: one claim per native memory, with its evidence and limits. Without native memory, keep nothing.
- Team fact or document: use the project's existing home (decision record, issue, test, runbook, docs). Link an existing record instead of copying it. Offer real destinations as a choice; never invent one.
- Before writing into the project, strip secrets, personal data, raw prompts, private absolute paths, and scratch-only metadata, and repair every link to the old location. If stripping guts the content, stop and ask.
- Move, not copy, unless asked. Commit only when chosen; never push. Return the durable path.
```

### `skills/revolver/SKILL.md`

```markdown
---
name: revolver
description: Review code, diffs, plans, or documents with fresh independent reviewers, then fix what survives verification. Use when work needs scrutiny from someone other than its author, fast or exhaustive. Do not use to check a single claim.
---

# Revolver

- Freeze the target. Reviewers are fresh subagents given the target and one brief, never the author's reasoning or another reviewer's prose. Without fresh subagents, stop; self-review does not count.
- Fast, the default: three top-tier reviewers in parallel, each attacking the whole target.
- Exhaustive, when asked: derive every materially distinct risk stance from the target and run one cheap reviewer per stance in sequence, each on the latest fixed version. Rotate again after any round that fixed something; stop after a quiet rotation or three.
- Reviewers return location, consequence, evidence, and minimal fix only. Check each finding against direct evidence: fix and verify what holds, reject what does not with the evidence, and stop for the user on human-owned choices.
- Report fixes with their verification, material rejections, and open decisions.
```

What the drafts drop on purpose:

- Persona slogans such as "Trust nothing", "Trace it to bedrock", "Attack without mercy".
- Restated evidence tuples (command, cwd, state id, exit) and rendering rules. These are good
  practice a frontier model follows when the skill asks for evidence.
- `promote`'s 8-step recovery-copy choreography. A model moving a file with "repair every link" and
  "move, not copy" does not need a staged transaction spelled out.
- `remember`'s four-way classification.

## 3. Repo shape

| Item | Now | Verdict | Reason |
| --- | --- | --- | --- |
| `docs/activation.md` | 18 lines | **Cut → 2 `AGENTS.md` bullets** | The surviving rules: description = action + task-language trigger + nearest exclusion; never self-name; tighten only after a witnessed miss. That is two bullets |
| `docs/body-anatomy.md` | 28 lines | **Cut → 1 `AGENTS.md` bullet** | "Keep only lines that change what a frontier model does." Its artifact-author clause is stale anyway (`docs/body-anatomy.md:14-16`) |
| `docs/execution.md` | 35 lines | **Cut** | Questions and authority now live in `ask-user`; evidence lives in `bulletproof`. Handoff rendering is default behavior |
| `docs/self-containment.md` | 20 lines | **Cut → 1 `AGENTS.md` bullet** | "One `SKILL.md`; works installed alone; names no sibling." The isolation proof it describes was never run (map Q2) |
| `docs/skill-existence-test.md` | 22 lines | **Merge into README** | The catalog table gains a "Failure it prevents" column, so the existence test is the catalog itself and cannot drift from it |
| `docs/scope.md` | 14 lines | **Cut** | README's first sentence plus "writes no document" in `AGENTS.md` cover it |
| `docs/README.md` | 13 lines | **Cut** | It indexes one file |
| `docs/sources.md` | 208 lines | **Shrink to about 40 lines, keep path** | Keep only the sources §1 cites, grouped by skill, plus 2 maintenance lines. This also clears the stale entries (map Q5 #8) |
| `scripts/lint-current.sh` | 384 lines | **Shrink to about 60 lines; rename `scripts/lint.sh`** | Keep: manifest (dirs = README rows); single Markdown `SKILL.md` per folder; frontmatter (name matches dir, one-line YAML-safe description ≤1024 chars, no self-name); no sibling names; no broken relative links. Drop: source-URL pins (they pinned the stale Codex URL, `:244`), the 31-name stale list, evidence and banner literals, artifact-type checks, `suspec-agents` patterns |
| `scripts/test-lint-current.sh` | 100 lines | **Shrink to about 30 lines; rename `scripts/test-lint.sh`** | One mutation per kept check (5), so CI proves the lint still bites |
| `scripts/lint-released-changelog.sh` | 46 lines | **Cut** | Git already preserves history. The pinned digest (`:7`) froze text without stopping lost releases (map Q5 #1), and it carries the `SUSPEC_SKILLS_HISTORY_BASE` fallback (`:8`). Keep released history by convention: one `AGENTS.md` bullet |
| `evals/` | 2 files | **Cut** | ADR-0170 retired eval matrices from this repo (`suspec:docs/adrs/0170-…:58-60`). A skill change records its witnessed failure and before/after result in the commit message, where the next reader finds it |
| `.github/workflows/method-gates.yml` | 29 lines | **Keep, rename `lint.yml`** | Two steps: lint and mutation test |
| `CHANGELOG.md` + `VERSION` | 204 + 1 | **Keep** | `npx skills add` does not prune (`README.md:16-17`), so every removal needs a cutover note somewhere users look. Released sections stay untouched |
| `README.md` | 55 lines | **Keep, rewrite to about 35** | Install, cutover, catalog with failure column, security, pointer to Corpus |
| `AGENTS.md` | 28 lines | **Keep, rewrite to about 20** | Edit contract carrying the bullets absorbed from the cut docs |
| `LICENSE`, `.gitignore` | — | Keep | — |

Tree after:

```text
.
├── .github/workflows/lint.yml
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
├── README.md
├── VERSION
├── docs/sources.md
├── scripts/lint.sh
├── scripts/test-lint.sh
└── skills/
    ├── ask-user/SKILL.md
    ├── bulletproof/SKILL.md
    ├── debloat/SKILL.md
    ├── drill/SKILL.md
    ├── panel/SKILL.md
    ├── promote/SKILL.md
    └── revolver/SKILL.md
```

Release as **7.0.0**: it removes skills, a major bump by the changelog's own rule (`CHANGELOG.md:5-7`).

## 4. Rename touchpoints (Suspec → Corpus)

The sibling repo becomes `jcosta33/corpus`, and `sus-*` becomes `corpus-*`. Under the new shape, this
repo must change:

| Touchpoint | Now | Change |
| --- | --- | --- |
| README artifact-author pointer | `README.md:47-49`, "Suspec artifacts … [Suspec](https://github.com/jcosta33/suspec)" | "Skills that write Corpus artifacts ship in [Corpus](https://github.com/jcosta33/corpus)." |
| README cutover block | `README.md:16-21` (6.0.0 removal list) | Replace with the 7.0.0 note below |
| `drill` framework name | `skills/drill/SKILL.md:29` "No Suspec artifact." | Gone in the draft; it says "write no plan document" instead |
| CHANGELOG header | `CHANGELOG.md:14-15` | Add: released sections say Suspec; the framework is now Corpus (`jcosta33/corpus`) |
| CHANGELOG `[7.0.0]` | new | Merges, the `demolition` cut, the Corpus pointer, the cutover |
| Released CHANGELOG sections | `CHANGELOG.md:19-204` | **Untouched.** Their `github.com/jcosta33/suspec/...` ADR links (`:140-141,149,173`) will rely on GitHub's rename redirect; check one after the rename |
| Gate leftovers | `scripts/lint-released-changelog.sh:8`, `scripts/lint-current.sh:375,379` | Disappear with the cut and shrunk gates |

Cutover note for README and `[7.0.0]`:

```bash
# 7.0.0 merged settle, dissect, remember, and triple-check, and cut demolition.
npx skills remove -g -a <agent> settle dissect remember triple-check demolition
npx skills add jcosta33/skills -g -a <agent>

# The artifact authors moved with the rename from Suspec to Corpus.
npx skills remove -g -a <agent> sus-spec sus-task sus-inventory sus-change-plan sus-audit sus-research sus-campaign
npx skills add jcosta33/corpus -g -a <agent>
```

**For the sibling (Corpus) session.** Corpus points at skills this proposal moves:

- `suspec:docs/reference/review-stances.md:48` deep-links `skills/triple-check`, which is gone. Point
  it at `skills/revolver`.
- `suspec:docs/reference/memory.md:21` points at the memory method; that is now `promote`.
- `suspec:docs/ADOPTING.md:25` lists the 6.0.0 removals.
- `suspec:skills/README.md:30-32`: its "Delete, Leave, or Promote" close still matches `promote`.

**Local machine.** `~/.agents/.skill-lock.json` records 7 `sus-*` installs sourced from
`jcosta33/suspec` and 12 from `jcosta33/skills`; the cutover above covers both. I have not verified
whether `npx skills add` follows GitHub repo redirects. The note uses new names, so it does not depend
on that.

## 5. Open decisions for José

Engineering calls already made above:

- Merge targets and the 3-parallel default mechanics.
- `ALWAYS` kept on `ask-user` only.
- The gates kept and cut.
- Evals replaced by commit-message evidence.
- 7.0.0.

These five are product-identity calls:

1. **Names of merged skills.**
   - (a) Keep `ask-user`, `bulletproof`, `promote`, `revolver`: no cutover for survivors; your habits
     already use them. **Recommended.**
   - (b) Verb names that say the job, e.g. `decide`, `verify`, `persist`, `review`: clearer to
     strangers, but another cutover.
   - (c) Keep the merged-away names as extra entries: contradicts "no alias" (ADR-0151).
2. **`demolition`.**
   - (a) Cut; ask for it in one line when wanted. **Recommended.**
   - (b) Keep as a 6-line skill with the banner.
   - (c) Fold "strongest dissent" advocacy into `panel` only.
3. **`revolver` default mode.**
   - (a) Fast: 3 top-tier reviewers in parallel by default, exhaustive on request. **Recommended**:
     lower cost, and multi-agent work is token-heavy (`docs/sources.md:175-178`).
   - (b) Exhaustive by default, the old `revolver` identity.
   - (c) Two skills again, which brings back the collision.
4. **Repository identity after the Corpus rename.**
   - (a) Stay `jcosta33/skills`, unbranded, outside the family. **Recommended**: matches ADR-0186's
     split, and the methods carry no framework vocabulary.
   - (b) Rebrand to `jcosta33/corpus-skills`: signals kinship, re-couples naming.
   - (c) Fold the 7 methods into `jcosta33/corpus/skills`: one install, but the "universal" claim
     ends.
5. **Audience.**
   - (a) Public catalog for anyone: keep CHANGELOG, semver, and cutover notes. **Recommended**: the
     cost is small, and `npx skills` users need prune notes.
   - (b) Personal catalog (as ADR-0186 calls it): drop CHANGELOG and VERSION, and pin by commit.

## Later (parked from the map, discuss after the shape settles)

- The changelog never recorded the additions of `settle`, `dissect`, `demolition`, `remember`, and
  `triple-check`, nor the ~30 removals. The `6c27a52` drill change is unlogged.
- Only `v1.0.0` and `v1.1.0` are tagged; 2.0.0–6.0.0 have no tags or releases.
- ADR drift: `ask-user` 2-option binary vs 0157; picker copies vs 0157; `drill` Obligation and the
  `panel` name have no ADR. This repo has no decision ledger of its own.
- Stale sources. The Codex docs URL 308-redirects; the gate pins it (`scripts/lint-current.sh:244`).
  Most of this disappears with the §3 trim.
- `docs/body-anatomy.md:14-16` stale clause, and the isolation proof that was claimed but never run.
  Both disappear with §3.
- Cross-repo dead link: `suspec:skills/README.md:16` points at deleted `suspec-cli`.
- The ADR ledger is missing back-references (0137/0186, 0157/0160+).
- Local: the lock file lists `remember`, but `~/.agents/skills/remember` is absent.
