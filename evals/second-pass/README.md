# Second pass: skills fired after an answer needs another look

Run 2026-11-05. José fires these skills on demand, after he has judged an agent's answer to need
another pass. This eval measures exactly that use. An agent answers a hard task. Then, in the same
session, it gets one of these follow-ups:

- **A**, no follow-up. This is the first-pass score.
- **B**, the bare message "Check this again."
- **C**, the current skill body.
- **C2**, the proposal from `corpus-review/engineering-meaning.md` §9, for settle and handoff only.
- **C3**, one fix arm, for a core skill that lost to B.

The follow-ups are scored on two things:

- How many flawed first answers they fix.
- How many correct first answers they disturb.

## Verdicts

The first two counts are per arm, in the order B / C / C3.

- **Fix points** score flawed runs: fixed = 1, partial = 0.5.
- **Churn + flip** counts correct runs that gained needless doubts or changes (churn) or turned wrong
  (flip).
- **in+out** is the mean uncached input plus output tokens per follow-up run, B / C.
- **Wall** is the median wall-clock seconds per follow-up run, B / C.

Panel and settle ran B and C at 3 reps and C3 at 2 reps. Their C3 column is compared on reps 0–1 of
every arm, in brackets. All other skills ran 2 reps per item and arm.

| Skill | First pass correct | Fix points B / C / C3 | Churn + flip B / C / C3 | in+out B / C | Wall B / C | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| panel | 16/30 | 13 / 9 of 30 [9 / 5.5 / **10** of 20] | 3 / 8 of 15 [1 / 6 / 4 of 10] | 5.5k / 19.4k | 33 / 76 | Stays. Loses to B on fixes, churn and cost. C3 beats current panel on both measures and ties B on fixes. C3 shipped in cac192e. |
| settle | 15/30 | 9 / **13.5** of 30 [5.5 / 8.5 / 6 of 20] | 1 / 9 of 15 [0 / 6 / 2 of 10] | 4.9k / 4.7k | 25 / 25 | Stays. Beats B on fixes at equal cost and loses on churn. C2 (12 of 30, churn 10 of 15) does not ship. C3 cut churn but lost the fixes. |
| bulletproof | 35/50 | 8 / 7 / 8 of 20 | 3 / 7 / **2** of 10 | 6.3k / 9.0k | 32 / 55 | Stays. Loses to B. C3 matches B on fixes, cuts churn to B's level and beats the current skill. C3 shipped in cac192e. |
| dissect | 32/42 | 8 / **11.5** / 7.5 of 20 | 1 / 5 / 2 of 10 | 8.0k / 13.3k | 35 / 94 | Stays as is. Beats B on fixes (6 full fixes vs 3) and loses on churn, with no flips. C3 traded the fixes away. |
| revolver | 37/45 | 2 / 2 of 16 | 4 / 1 of 10 | 15.7k / 55.8k | 49 / 343 | Stays; findings only (below). |
| drill | 19/30 | 3.5 / **7** of 20 | 2 / 5 of 10 | 24.3k / 22.1k | 89 / 50 | **Keep.** Doubles B's fixes at lower cost and time. 2 of its 5 correct-item hits are flips. |
| handoff | 36/40 | 3.5 / 3 of 8; C2 3 of 8 | 6 / 4 of 10; C2 5 | 6.6k / 5.0k | 32 / 19 | **Retire candidate.** Plain Opus writes a correct brief 9 times in 10. As a second pass the skill ties B. C2 does not ship. |

**Settle and handoff do not change.** The ship rule was that a settle or handoff proposal must beat
both the current skill and B. Neither did. After the run, José approved shipping the panel and
bulletproof C3 texts. They shipped verbatim in cac192e.

No skill fixes most flawed answers, and neither does B. The best fix rate is 0.57 (dissect C). The
best fix rate for B is 0.44 (handoff). B alone beats or ties the current skill in three places:

- panel, on every measure;
- bulletproof, on every measure;
- handoff, on fixes.

## Where a core skill lost to B, and why

The grader reasons are in `follow.csv`.

- **panel.**
  - Why it lost: the fresh analysts invent compromise or additive options (opt-in flags, a
    superseding ADR, an extra variant) instead of keeping a recorded decision. The long panel
    narrative also reopens choices that were already correct.
  - C3 change: list keeping the current behaviour as an option, name the recorded decisions that
    bear on the choice, and never recommend reversing one. If the panel confirms the earlier
    recommendation, say so in one line and stop. Text: `arms/panel.c3.md`, shipped in cac192e.
  - C3 result: fixes 10 of 20 (6 full) against B 9 and C 5.5. Churn 4 of 10 against B 1 and C 6.
    Token cost is about the same as C (21.0k against 19.4k).
- **settle.**
  - Why it lost: it wins on fixes but churns correct answers. It reframes the question and adds a
    choice question even where the evidence already decides.
  - C3 change: add "If the evidence confirms an answer already given, say so in one line, keep it,
    and ask nothing."
  - C3 result: churn fell to 2 of 10, but fixes fell to B's level and 4 runs got worse. On
    settle-02, 29 and 30 the key required escalating a choice to the owner, and the clause let the
    model declare that no question was needed.
  - Next candidate, untested: confirm in one line only when the evidence decides the question, and
    still ask when the choice belongs to the owner.
- **bulletproof.**
  - Why it lost: the checkout is read-only, with no tests, browser or network. The skill marks facts
    that code or a spec already decides as `Unverified` or `Blocked`, which retracts correct claims.
    Its long tables end without a corrected conclusion. In 2 runs it invented a counter-mechanism
    and retracted a correct finding.
  - C3 change: an item that a source you opened decides gets `Supported` or `Unsupported`, and the
    answer is restated after the table. Text: `arms/bulletproof.c3.md`, shipped in cac192e.
  - C3 result: fixes 8 of 20, matching B. Churn 2 of 10, against 7 for C. 2 runs got worse.
- **dissect.**
  - Why it lost: it lost only on churn. It adds `Unknown` rows and hedges to traces that were
    already correct, with no flips.
  - C3 change: the confirm-and-stop clause.
  - C3 result: churn fell to 2 of 10, but fixes fell from 11.5 to 7.5 with 2 worse runs. On this
    evidence, the extra churn is the price of the fix gain.

Across settle and dissect, "confirm in one line and stop" also confirms flawed answers. It helped
only in panel, where it was paired with the recorded-decision rule.

## Revolver findings

There is no proposed text here, by José's ruling.

- Plain Opus reviews were correct on 37 of 45 first passes. Only 8 items were flawed, short of the
  target of 10.
- **Missed bugs are not recovered.** 6 of the 8 flawed reviews missed the key's bug outright, and 1
  ranked it as an unverified side point. Under both B and revolver, the follow-up rotated over the same areas and did not find the missed bug.
  Revolver scored 4 partials on 3 items. B scored 0 partials.
- **The one wrong-conclusion item went the other way.** On revolver-04 the answer needed a decision
  on which half of a ratio is wrong. B checked the scheduler and fixed it in both reps. Revolver
  left it open as a convention choice in both reps.
- **Revolver disturbs correct reviews less:** churn plus flip was 1 of 10, against 4 for B.
- **Cost:** 3.6× B's input+output tokens and 7× its median wall time (343 s against 49 s).

## Method

- **Items.**
  - Real cases came first. José's Claude, Codex and Cursor transcripts held about 60 "are you sure",
    "double check" and `/settle` moments. None could be rebuilt as a replayable first pass: the
    lanes and worktrees are gone, and most hits were earlier eval artifacts. All items are
    therefore natural failures.
  - Opus writers built hard tasks from real Sourdaw and skills history. Each task had an answer key
    written before any run. Briefs are in `scripts/writer_common.md` and `scripts/writer-sections/`.
    The panel, settle, revolver and handoff writer briefs were given inline and are not saved.
  - Flaws were never planted. A first answer counts as flawed only when the blind grader labels it
    so.
- **First pass (A).**
  - Model: `claude -p` with `claude-opus-5-5` and project settings only.
  - Workspace: a read-only snapshot. Sourdaw is at 95128133a2, or at the item's own commit via
    `git archive`. Skills is at e03ea04.
  - Tools: Read, Grep and Glob, plus Bash limited to git log/show/diff/blame/grep, ls and wc. Panel
    and revolver also get Agent. Handoff items carry the transcript in the prompt and have no tools.
- **Follow-up.**
  - Each run is `--resume <first session> --fork-session` with the arm message.
  - C, C2 and C3 send "Apply this skill to your previous answer." followed by the skill body.
- **Selection.** `scripts/pick.py` uses a fixed seed. Per skill it takes up to 10 flawed and 5
  correct first answers; the selections are in `items/selection-*.json`.
- **Grading.**
  - Grader: blind Sonnet 5.5 with no tools, one call per run. It sees the key, the first answer and
    the later message, but not the arm.
  - Flawed answers are graded fixed, partial, unfixed or worse. Correct answers are graded kept,
    churn or flipped. Prompts are in `scripts/grade.py`.
- **Files.**
  - `first.csv`: one row per first pass.
  - `follow.csv`: one row per follow-up run, with the grader's reason.
  - `summary.csv`: per skill and arm, with cache tokens and list-price dollars.
  - `arms/`: the exact skill bodies sent.
  - `items/`: tasks and keys. José's email, which appears in public commit trailers, is redacted.
  - `scripts/`: the runner, grader and export scripts. They expect the `/tmp` snapshot paths named
    above.

## Cost

| Part | Runs | Input + output | Cache write | Cache read | List price |
| --- | --- | --- | --- | --- | --- |
| Opus first passes and follow-ups | 919 | 9,160,018 | 50,001,476 | 451,210,588 | $577 |
| Sonnet grader | 919 | 142,854 | 6,102,319 | 1,698,125 | $26 |

- **Not in the totals:** the item-writer agents and the transcript mining.
- **Overrun:** the run passed the planned 4M after panel and settle ran at 3 reps. The other five
  skills then dropped to 2 reps. José then set a ceiling of about 8M; the run finished at 9.3M.

## Caveats

- **Small samples.** n is 8 to 30 flawed runs per arm, and 4 flawed handoff items. A gap of 1–2 fix
  points is noise.
- **One grader, one call per run.** Churn is the grader's judgment of "needless doubts or changes".
  For dissect and bulletproof, some churn is the `Unknown` rows the skill asks for.
- **B is one wording.** Other bare follow-ups may score differently.
- **Read-only setting.** No edits, tests, browser or network were available. This handicaps
  bulletproof and dissect, which expect to run probes.
- **Unequal reps.** Panel and settle ran B, C and C2 at 3 reps, and every other arm at 2. The C3
  comparison uses reps 0–1 only.
- **Short sets.** Revolver has 8 flawed items and handoff 4, against a target of 10.
