# Planted-defect eval: bulletproof and panel additions

Run 2026-11-05. It gates the philosophy additions: `bulletproof` moves 1, 5, and 11, and `panel` moves 2 and 9 (`corpus-review/philosophy.md`).

## Decision

Neither set of additions ships, and both skills stay as they are.

- **bulletproof:** all three arms found 10/10 planted defects. The additions find nothing that plain Opus misses. They cost more tokens and more time.
- **panel:** plain Opus found 9 of 10 decisions cleanly and one partially. No skill arm beat it.
  - On p06, the only item where plain Opus fell short, both skill arms ran their full panels. The current skill hit; the additions arm was only partial.
  - On p03, both skill arms missed. Each recommended writing a new script, when the README already documents the remove command.

## Method

- **Target.** A frozen, read-only clone of this repository at `41f20ed`.
- **Items.** Ten checkable claim sets for `bulletproof` and ten decisions for `panel`. Each carries exactly one planted defect:
  - a claim set has one false claim;
  - a decision leaves out its correct option, which the repository's own evidence shows.
- **Arms.** Each arm is a fresh Opus subagent given the item:
  - **plain:** the item alone;
  - **cur:** the current skill text plus the item;
  - **add:** the skill text with the additions, plus the item.
- **Shared rules.** Every arm got the same preamble: read-only, no Skill tool, and pin a model on any subagent, never Fable.
- **Scoring.** Each run ended with one fixed line, scored against the answer key:
  - `DEFECTS:` for claim sets. A hit means the planted claim number appears; any other number is a false flag.
  - `RECOMMENDATION:` for decisions, scored hit, partial, or miss against the omitted option.
- **Measures.** Tokens and wall time come from each subagent's completion record. For `panel`, the token count excludes the run's child subagents.

## Caveats

- **Panel runs were contaminated.** Several skill-arm runs had some or all child dispatches refused by the harness's limit of 20 concurrent subagents. They then fell back to a single pass. Each affected row is marked.
- **Panel runs left unrerun.** Rerunning the contaminated runs and the eight unrun ones (p07–p10) could not change the decision. Plain Opus already reaches the ceiling on nine items. On the tenth, both skill arms ran their full panels.
- **Ceiling.** The items were easy enough that plain Opus hit the ceiling. The eval cannot show a gain on harder material, only that these additions buy nothing here.
- **One replicate.** Each arm ran once per item (b08-cur ran twice by accident; both runs hit).
- **Side effect.** Some runs executed `scripts/test-lint.sh` on the read-only clone, which left undeletable temp directories. That failure was fixed in `b88a0e4`.

## Skill text under test

**bulletproof, current**

```text
List every load-bearing claim and every unstated assumption, then check each against sources you
open or commands you run. Return one table: item, `Supported` / `Unsupported` / `Unverified` /
`Blocked`, evidence. `Unverified` and `Blocked` name the exact gap.
```

**bulletproof, with additions**

```text
List every load-bearing claim and every unstated assumption. For each, state its scope, condition,
and strength (possible, observed, or necessary), and write the result that would refute it. Then
check each against sources you open or commands you run; never verify by re-reasoning. Return one
table: item, `Supported` / `Unsupported` / `Unverified` / `Blocked`, evidence. `Unverified` and
`Blocked` name the exact gap.
```

**panel, current**

```text
Launch fresh subagents concurrently on the cheapest capable model; none sees another's analysis.
Answer in chat: recommendation first, a comparison table on shared criteria, the strongest surviving
dissent, and what would reverse the call.
```

**panel, with additions**

```text
Divide the options by one stated criterion until they are exhaustive, including doing nothing, a
partial step, and a reversible step. Launch fresh subagents concurrently on the cheapest capable
model; none sees another's analysis. Count their verdicts before any discussion, and debate only on
a split. Answer in chat: recommendation first, a comparison table on shared criteria, the strongest
surviving dissent, and what would reverse the call.
```

## bulletproof

| Arm | Defects found | False flags | Mean tokens | Median wall time (s) | Mean wall time (s) |
| --- | --- | --- | --- | --- | --- |
| plain | 10/10 | 1 | 45,273 | 16.0 | 16.8 |
| cur | 10/10 | 0 | 46,455 | 24.6 | 28.5 |
| add | 10/10 | 0 | 47,597 | 23.7 | 42.3 |

Items; the planted false claim number is in brackets:

- **b01** [4]: Before I announce it, check this completion report for commit 7bf943f: / 1. It adds nine skills: wdyt, onward, whatsnext, sitrep, handoff, rearm, scout, stepback, proper. / 2. Each new skill ships agents/openai.yaml with allow_implicit_invocation: false. / 3. scripts/test-lint.sh now kills 15 mutations. / 4. scripts/lint.sh rejects any description longer than 200 characters.
- **b02** [3]: I'm about to tell a contributor how CI works here. Check: / 1. CI runs on pushes to main and on pull requests. / 2. CI runs scripts/lint.sh and then scripts/test-lint.sh. / 3. CI runs on macos-latest. / 4. The workflow grants only read access to repository contents.
- **b03** [3]: Here is my plan to retire a skill. Check it before I run it: / 1. Delete skills/<name>/; lint then fails until its README catalog row is removed. / 2. Remove the row; lint passes again. / 3. Re-run `npx skills add jcosta33/skills -g -a claude-code`; that removes the retired skill from the installed harnesses. / 4. No lint rule checks docs/sources.md against the skill list.
- **b04** [1]: Check these statements about docs/sources.md before I quote them: / 1. Du et al.'s Multiagent Debate is cited as ICML 2023. / 2. Seleznov's experiment backs the ALWAYS wording in settle only. / 3. Wataoka et al. (NeurIPS 2024 workshop) back revolver's fresh reviewers. / 4. Huang et al., ICLR 2024, is cited under bulletproof and panel.
- **b05** [4]: Check this history summary: / 1. Tag v7.0.0 points at commit c3d4b25. / 2. c3d4b25 cut the catalog to seven skills. / 3. 2315dfc restored dissect. / 4. The promote skill was deleted in d662daa.
- **b06** [2]: Check what I'm telling the team scripts/lint.sh enforces: / 1. A description containing a colon followed by a space is rejected. / 2. A SKILL.md longer than 100 lines is rejected. / 3. A description must start with a letter. / 4. Reference-style Markdown links in README.md, AGENTS.md, and docs/*.md are rejected.
- **b07** [2]: Here is my summary of the method skills. Check it: / 1. revolver stops after a quiet rotation or after three rotations. / 2. panel has each analyst read the others' analyses before giving a verdict. / 3. dissect requires a negative claim to carry the search command and its result. / 4. settle asks with three options, or two if the choice is binary, plus Other.
- **b08** [3]: Check these claims about scripts/test-lint.sh: / 1. It copies docs/ into each fixture only when docs/ exists. / 2. It creates its fixtures with mktemp and removes them through a trap. / 3. It mutates the alphabetically last skill folder. / 4. It first runs lint on the unmodified repository.
- **b09** [1]: Check this before I put it in the README: / 1. AGENTS.md requires every change to add a CHANGELOG.md entry. / 2. The repository has 139 commits on main. / 3. It has three tags. / 4. It is MIT licensed.
- **b10** [3]: Check this description of the micro skills: / 1. handoff answers in chat and writes no file. / 2. scout forbids commenting on issues or PRs. / 3. proper reverts every change the user did not ask for straight away. / 4. sitrep reports from fresh git, GitHub, and test state rather than memory.

| Item | plain | cur | add |
| --- | --- | --- | --- |
| b01 | `DEFECTS: 4` · 52,244 tok · 23s | `DEFECTS: 4` · 50,787 tok · 39s | `DEFECTS: 4` · 56,834 tok · 56s |
| b02 | `DEFECTS: 3` · 42,561 tok · 17s | `DEFECTS: 3` · 43,459 tok · 21s | `DEFECTS: 3` · 43,557 tok · 20s |
| b03 | `DEFECTS: 3` · 50,114 tok · 28s | `DEFECTS: 3` · 50,909 tok · 52s | `DEFECTS: 3` · 58,343 tok · 174s |
| b04 | `DEFECTS: 1` · 44,248 tok · 12s | `DEFECTS: 1` · 45,993 tok · 23s | `DEFECTS: 1` · 46,110 tok · 23s |
| b05 | `DEFECTS: 4` · 44,910 tok · 15s | `DEFECTS: 4` · 47,188 tok · 25s | `DEFECTS: 4` · 45,254 tok · 24s |
| b06 | `DEFECTS: 2` · 45,008 tok · 19s | `DEFECTS: 2` · 45,510 tok · 25s | `DEFECTS: 2` · 47,327 tok · 39s |
| b07 | `DEFECTS: 2` · 43,271 tok · 11s | `DEFECTS: 2` · 45,993 tok · 24s | `DEFECTS: 2` · 44,550 tok · 19s |
| b08 | `DEFECTS: 3` · 45,153 tok · 21s | `DEFECTS: 3` · 46,331 tok · 33s | `DEFECTS: 3` · 45,668 tok · 25s |
| b09 | `DEFECTS: 1, 3` · 42,571 tok · 13s | `DEFECTS: 1` · 44,721 tok · 25s | `DEFECTS: 1` · 44,167 tok · 23s |
| b10 | `DEFECTS: 3` · 42,647 tok · 9s | `DEFECTS: 3` · 43,659 tok · 19s | `DEFECTS: 3` · 44,164 tok · 21s |

## panel

| Arm | Hit | Partial | Miss | Not run | Runs with every child dispatched |
| --- | --- | --- | --- | --- | --- |
| plain | 9 | 1 | 0 | 0 | not applicable |
| cur | 5 | 0 | 1 | 4 | 1 |
| add | 4 | 1 | 1 | 4 | 2 |

Items; the answer key is in brackets:

- **p01** [none: lint.sh already rejects descriptions over 1024]: We want lint to catch skill descriptions over 1024 characters. Options: (a) add a Python validator script, (b) add a Node script, (c) add a GitHub Marketplace action. Which should we do?
- **p02** [none: agents/openai.yaml already blocks Codex]: Codex ignores disable-model-invocation, so our micro skills could auto-run there. Options: (a) stop installing micro skills for Codex, (b) start each micro description with 'NEVER auto-run', (c) write a Codex plugin that filters them. Which should we do?
- **p03** [`npx skills remove <names> -g`, as the README says]: Skills that left the catalog linger in the installed harness folders after we reinstall. Options: (a) rm -rf ~/.agents/skills before every install, (b) write our own prune script, (c) switch to a different installer. Which should we do?
- **p04** [none: test-lint's sibling-name mutation exists]: We want proof that the lint rule against naming sibling skills actually bites. Options: (a) add a pytest suite, (b) add a bats test suite, (c) check it by hand before each release. Which should we do?
- **p05** [none: keep reviewers blind (revolver step 2, Spadini)]: In revolver, later reviewers keep repeating earlier findings. Options: (a) give each reviewer all prior findings so it skips them, (b) give it a summary of prior findings, (c) give it only the titles of prior findings. Which should we do?
- **p06** [none: 2315dfc made git history the record]: Consumers need to know what changed between catalog updates. Options: (a) keep a CHANGELOG.md in keep-a-changelog format, (b) generate a changelog from conventional commits, (c) publish GitHub releases. Which should we do?
- **p07** [keep both (2315dfc reversed the merge)]: dissect and bulletproof look like they overlap. Options: (a) merge dissect into bulletproof, (b) merge bulletproof into dissect, (c) replace both with one new skill named verify. Which should we do?
- **p08** [answer in chat (AGENTS.md: skills write no document)]: We want the handoff skill's brief saved so it survives the session. Options: (a) write HANDOFF.md at the repository root, (b) write docs/handoff.md, (c) write .claude/handoff.md. Which should we do?
- **p09** [none: lint.sh already enforces the policy]: We want lint to ensure every user-invoked micro skill carries the Codex no-implicit-invocation policy. Options: (a) JSON Schema validation with ajv, (b) a Python YAML check, (c) document the requirement in the README only. Which should we do?
- **p10** [keep the error; add the row (AGENTS.md rule)]: We want to stop CI breaking when a skill's README catalog row is missing. Options: (a) generate the README catalog automatically in CI, (b) make the catalog check a warning instead of an error, (c) drop the catalog table from the README. Which should we do?

| Item | Arm | Score | Final line | Tokens | Wall time (s) |
| --- | --- | --- | --- | --- | --- |
| p01 | plain | hit | RECOMMENDATION: none of a-c; lint already rejects >1024; add a mutation | 48,675 | 32 |
| p01 | cur | hit | INVALID-PARTIAL(2/4) RECOMMENDATION: none; lint rejects >1024; add mutation | 53,395 | 84 |
| p01 | add | hit | INVALID-NOPANEL RECOMMENDATION: none; lint already rejects >1024; add mutation | 56,170 | 57 |
| p02 | plain | hit | RECOMMENDATION: none; openai.yaml already stops Codex; reinstall stale copies | 49,701 | 34 |
| p02 | cur | hit | INVALID-NOPANEL RECOMMENDATION: none; openai.yaml already blocks; reinstall | 58,328 | 76 |
| p02 | add | hit | VALID(3/3) RECOMMENDATION: none; openai.yaml exists; reinstall and smoke-test | 61,016 | 97 |
| p03 | plain | hit | RECOMMENDATION: none; npx skills remove jcosta33/skills -g then add | 55,553 | 60 |
| p03 | cur | miss | INVALID-PARTIAL(2/3) RECOMMENDATION: (b) source-filtered prune script | 66,892 | 142 |
| p03 | add | miss | INVALID-NOPANEL RECOMMENDATION: write read-only stale-report script printing npx skills remove | 59,354 | 80 |
| p04 | plain | hit | RECOMMENDATION: none; sibling-name mutation already in test-lint | 53,154 | 42 |
| p04 | cur | hit | INVALID-NOPANEL RECOMMENDATION: none; test-lint already proves | 51,657 | 65 |
| p04 | add | hit | INVALID-PARTIAL(1/3) RECOMMENDATION: none; sibling-name mutation exists | 52,229 | 62 |
| p05 | plain | hit | RECOMMENDATION: none; keep reviewers blind; dedupe in step 3 | 46,496 | 30 |
| p05 | cur | hit | INVALID-NOPANEL RECOMMENDATION: none; keep blind; orchestrator record | 48,539 | 59 |
| p05 | add | hit | INVALID-NOPANEL RECOMMENDATION: none; keep blind; orchestrator ledger | 48,775 | 65 |
| p06 | plain | partial | RECOMMENDATION: (b) light: commit log is the record, no file, no releases (flags catalog-is-personal tension) | 54,839 | 56 |
| p06 | cur | hit | VALID(4/4) RECOMMENDATION: none; git history is the record per 2315dfc | 62,219 | 98 |
| p06 | add | partial | VALID(3/3) RECOMMENDATION: none of a-c; git history + README removals list (partial step) | 59,087 | 97 |
| p07 | plain | hit | RECOMMENDATION: none; keep separate (merge reversed in 2315dfc) | 53,941 | 43 |
| p07 | cur | not run | | | |
| p07 | add | not run | | | |
| p08 | plain | hit | RECOMMENDATION: none; keep chat-only per AGENTS.md | 45,158 | 26 |
| p08 | cur | not run | | | |
| p08 | add | not run | | | |
| p09 | plain | hit | RECOMMENDATION: none; lint.sh already enforces the policy | 50,429 | 32 |
| p09 | cur | not run | | | |
| p09 | add | not run | | | |
| p10 | plain | hit | RECOMMENDATION: none; keep the error; make lint name the skill | 50,322 | 35 |
| p10 | cur | not run | | | |
| p10 | add | not run | | | |
