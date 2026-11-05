# Trigger eval: method-skill descriptions

Run 2026-11-05 to gate the description rewrites for `drill`, `dissect`, `bulletproof`, `revolver`, and `panel`.

## Result

All five new descriptions pass more queries than the old ones and add no false trigger, so all five ship.

| Skill | Old: queries passed | New: queries passed | Should-trigger passed, old → new | Near misses passed, old → new | Trigger rate per run, old → new | False trigger rate per run, old → new |
| --- | --- | --- | --- | --- | --- | --- |
| drill | 13/20 | 19/20 | 3/10 → 9/10 | 10/10 → 10/10 | 33% → 90% | 0% → 0% |
| dissect | 18/20 | 20/20 | 8/10 → 10/10 | 10/10 → 10/10 | 77% → 100% | 0% → 0% |
| bulletproof | 16/20 | 18/20 | 6/10 → 8/10 | 10/10 → 10/10 | 63% → 80% | 0% → 0% |
| revolver | 14/20 | 19/20 | 4/10 → 9/10 | 10/10 → 10/10 | 43% → 90% | 0% → 0% |
| panel | 19/20 | 20/20 | 9/10 → 10/10 | 10/10 → 10/10 | 90% → 100% | 0% → 0% |

## Method

- **Basis.** The method of Anthropic's skill-creator `scripts/run_eval.py`.
- **Queries.** 20 per skill: 10 should trigger and 10 are near misses. They are written in the owner's own phrasing (`corpus-review/micro-candidates-history.md`).
- **Runs.** Each query ran 3 times through `claude -p` with `--model claude-opus-5-5`. The binary was Claude Code 2.1.317; the installed 2.1.173 refuses Opus 5.5.
- **Pass rule.** A should-trigger query passes at a trigger rate of 0.5 or more; a near miss passes below 0.5.
- **Detection.** As in `run_eval.py`: a run counts as a trigger only if its first tool call is `Skill` naming the skill under test, or a `Read` of that skill's file. Any other first tool call counts as no trigger.
- **One change from `run_eval.py`.** Each arm runs in a scratch clone of this repository with the whole catalog installed as project skills, so siblings compete. `--setting-sources project` hides user-installed skills; the harness built-ins stay. Only the skill under test carries the description being measured.
- **Files.**
  - Runner: [`run_trigger.py`](run_trigger.py).
  - Query sets: `<skill>.queries.json`.
  - Candidate descriptions: [`new_descriptions.json`](new_descriptions.json).
  - Per-query rates and every run's first tool call: `<skill>.old.results.json` and `<skill>.new.results.json`.

## Caveats

- **Same author.** The same agent wrote both the queries and the new descriptions.
- **No held-out queries.** Unlike skill-creator's 60/40 split, no query set was kept back to test the new descriptions, so overfitting to these phrasings is possible.
- **First tool call only.** Runs that started with Bash or Read and might have called the skill later count as no trigger, as in `run_eval.py`.
- **panel's gain is small.** It won by one query (19 → 20).
- **Remaining collision.** `bulletproof` still takes some runs of `dissect` queries and the reverse (see `first_calls` in the result files); no near miss crossed the threshold.
