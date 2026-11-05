---
type: adr
id: adr-0011
status: accepted
created: 2026-11-05
---

# ADR-0011 - Ship the panel and bulletproof second-pass fix texts

## Context

In the second-pass eval both skills lost to a bare "Check this again."

- **panel:** fresh analysts invented compromise options instead of keeping recorded decisions, and
  reopened correct choices.
- **bulletproof:** in a read-only checkout it marked facts a source already decides as
  `Unverified` or `Blocked`, and it ended without a corrected answer.

## Decision

1. panel lists the options, always including keeping the current behaviour. It names the recorded
   decisions that bear on the choice and never recommends reversing one. If it confirms an earlier
   recommendation, it says so in one line and stops.
2. bulletproof checks the claims the conclusion rests on. An item an opened source decides is
   `Supported` or `Unsupported`, and the answer is restated with each `Unsupported` item corrected.
3. Both bodies equal the tested arm texts. Descriptions are unchanged.

## Rationale

- **panel**, reps 0–1, of 20 flawed and 10 correct runs, as fixes / churn:
  - old skill: 5.5 / 6;
  - "check again": 9 / 1;
  - fix text: 10 / 4, with 6 full fixes against 0 and 3.
- **bulletproof**, of 20 flawed and 10 correct runs, as fixes / churn:
  - old skill: 7 / 7;
  - "check again": 8 / 3;
  - fix text: 8 / 2.
- The same confirm-and-stop clause cost settle and dissect their fixes, so it was not applied
  there.

## Evidence

- [evals/second-pass](../../evals/second-pass/README.md).
- [cac192e](https://github.com/jcosta33/skills/commit/cac192e).

## Status

Accepted (2026-11-05).
