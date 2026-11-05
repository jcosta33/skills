# Proposal gate: engineering-meaning §9 additions

Run 2026-11-05. It gates the ten skill additions proposed in §9 of
`corpus-review/engineering-meaning.md`. A proposal ships only if it beats both plain Opus and the
current skill on seeded items, loses nothing on clean controls, and costs an acceptable amount.

## Limitation: these verdicts are provisional

The gate measured **first-pass** behaviour. Each item went to a fresh agent as its first and only
message. That is not how these skills are used. José fires them on demand as a **second pass**,
after he has judged an agent's output to need another look under the skill's conditioning.

- **Ceiling results are expected.** An item that plain Opus solves on the first pass is one where
  José would never invoke the skill. Ceiling results do not show a skill is useless in real use.
- **"Current skill below plain" is not a rejection either.** It says nothing about the skill as a
  second pass.
- **What this does decide.** Only debloat, which acts on supplied text and has no first pass to
  improve on. Its result holds under either framing, so it ships.
- **What stays provisional.** The verdicts for settle, handoff, drill, onward, rearm, panel, sitrep,
  bulletproof and revolver are provisional, not rejections. Nothing else ships from this run.
- **A redesign is proposed, not run.** Items would be built from already-flawed first-pass outputs,
  ideally real ones. The arms would be the skill as a second pass, a bare "check again", and no
  follow-up. The measures would be fixes on flawed outputs and flips on correct ones.

## Verdicts

Points: hit = 1, partial = 0.5, miss = 0. Control columns count runs that were not clean (false
flag or partial). Per-arm tables follow below.

| Skill | Proposal (§9) | Tested | Seeded points: add / cur / plain | Controls not clean: add / cur / plain | Verdict |
| --- | --- | --- | --- | --- | --- |
| debloat | Cut rules the model follows unprompted; keep the ones that oppose defaults | alone | 13.5 / 7.5 / 10.5 of 15 | 0 / 0 / 0 of 6 | **Ship** |
| settle | Presupposition check first; check work next to an answered decision | jointly; B also alone | 11 / 6.5 / 4 of 18 (B alone: 2.5 of 12) | 4 / 1 / 0 of 18 | Provisional: no ship (control loss; A ties cur) |
| handoff | Decisions in force; moot condition; assumptions unchecked; reviewer gets requirements and target | jointly; variant add2 | 7.5 / 6 / 5 of 9 (add2: 9 of 9) | 6 / 0 / 1 of 6 (add2: 4 of 6) | Provisional: no ship (control loss) |
| drill | Readings, world facts, context of terms | jointly | 10.5 / 8.5 / 9.5 of 15 | 4 / 0 / 3 of 6 | Provisional: no ship (terms worse, control loss) |
| rearm | Say where one likely change goes, then check it against the code | alone | 11 / 10.5 / 9 of 15 | 0 / 0 / 2 of 6 | Provisional: no ship (no margin over cur) |
| onward | Report done, impossible, or moot with evidence, then stop | alone | 7 / 6.5 / 7 of 12 | 1 / 1 / 3 of 6 | Provisional: no ship (ties plain) |
| panel | Out-of-category option; distinct framings; probabilities; side effects; withhold lean | jointly | 2 / 2.5 / 2 of 3 | 4 / 1 / 3 of 6 | Provisional: no ship (7 of 8 items at ceiling) |
| sitrep | Each earlier "I will": done, or dropped and why | alone | 3 / 2 / 2.5 of 3 | 5 / 5 / 5 of 6 | Provisional: no ship (5 of 6 items at ceiling) |
| bulletproof | Judge completion claims from artifacts; check the source is in a position to know | not scored | plain 24/24 in both pilots | – | Provisional: no ship (no headroom) |
| revolver | Reviewer briefs from requirements and target only | not scored | plain 18/18 in both pilots | – | Gated only; José owns revolver |

### Notes on single verdicts

- **debloat.** The current skill scored below plain Opus (7.5 against 10.5). It merged or softened
  rules that oppose model defaults. The proposal reversed that, at the current skill's cost: about
  4.9k tokens and 14 s median per run, against 3.9k and 8 s for plain.
- **settle.** The joint text lifted the answered-decision items most (5.5 of 12, against 1 for cur
  and plain). The B line alone reached only 2.5, so the lift needs both lines together. On the
  presupposition items the proposal tied the current skill. Extra control runs (9 per arm) put the
  joint text at 4 false flags out of 18, all on settle-09, against 1 for cur and 0 for plain.
- **handoff.** The joint text raised seeded scores, but in all 6 control runs it invented a moot
  condition or "unchecked" labels on clean briefs. The variant add2 is tuned on these same items.
  It keeps only the moot and unchecked lines, written as "If C, do X". It scored 9 of 9, but still
  flagged 4 of 6 controls. The decisions and reviewer items stayed at plain ceiling after
  hardening, so those two lines were never scored.
- **revolver.** José ruled the skill untouchable, so this proposal was gated only. Plain
  single-pass Opus found every seeded defect, even with a wrong rationale in the PR text and a
  prior approval of the exact spot. Full revolver arms were not run, since no gain was measurable.

## Method

- **Items.** One blind Opus writer per skill, which never saw the proposed text, wrote 8–11 items
  from Sourdaw and skills-repo material.
  - Seeded items carry the targeted failure; two clean controls per skill expect no extra action.
  - Keys were written with the items, before any run.
  - Briefs: [`scripts/writer_common.md`](scripts/writer_common.md) and
    [`scripts/writer-sections/`](scripts/writer-sections/).
- **Pilot.** Plain Opus ran 3 times per seeded item.
  - An item solved 3/3 went back to its writer for one hardening round. Writers were told only
    what made the items easy.
  - An item still at ceiling after that round was dropped.
  - Pilot runs are in [`pilot.csv`](pilot.csv); scored runs are separate, fresh runs.

  | Skill | Seeded | At ceiling, first pilot | Still at ceiling after hardening | Scored |
  | --- | --- | --- | --- | --- |
  | settle | 8 | 8 | 2 | 6 |
  | drill | 9 | 7 | 4 | 5 |
  | handoff | 8 | 6 | 5 | 3 |
  | rearm | 6 | 6 | 1 | 5 |
  | onward | 6 | 5 | 2 | 4 |
  | panel | 8 | 8 | 7 | 1 |
  | debloat | 6 | 2 | 1 | 5 |
  | sitrep | 6 | 6 | 5 | 1 |
  | bulletproof | 8 | 8 | 8 | 0 |
  | revolver | 6 | 6 | 6 | 0 |

- **Arms.** Each run was `claude -p` 2.1.317 with Opus 5.5 (`claude-opus-5-5`).
  - Settings came from project sources only, so no user skills, CLAUDE.md or plugins loaded, and
    no session was persisted.
  - The working directory was a fresh temp dir holding the item's files. Tools were Read, Grep and
    Glob when an item had files, plus Agent for panel and revolver.
  - **plain:** the item alone. **cur:** the item plus the current skill body. **add:** the item
    plus the skill body with the proposal. Bodies are in [`arms/`](arms/).
  - Three fresh runs per item per arm.
- **Grader.** `claude -p` with Sonnet 5.5 and no tools, blind to the arm.
  - Input: the item, its key, the files the agent opened, any subagent briefs, and the final answer.
  - Output: hit / partial / miss, or clean / false_flag for controls, plus false-flag count and
    over-asking.
  - Per-run grades and reasons are in [`results.csv`](results.csv).
- **Cost measures.** Tokens are the sum over models in the run's `modelUsage`, so they include
  subagents. Wall time is measured around the process.

## Caveats

- **First-pass framing.** See the limitation above.
- **Inline transcripts are short.** They are a few thousand words, not the 100k-token sessions where
  promises and supersessions get lost. Sitrep and handoff ceilings may reflect that.
- **Same-set tuning.** Handoff add2 and settle addB were written after seeing results on the same
  items. No held-out set exists.
- **Small control sets.** Each skill has two controls, and some keys are strict. On sitrep-07, every
  arm flagged a file genuinely absent from the diff stat.
- **One grader.** No second grader checked agreement.
- **Item bodies omitted.** The JSON in [`items/`](items/) keeps requests, keys and sources. File
  bodies are replaced by sizes; each item's `source` names the Sourdaw commits they came from.

## Files

- [`results.csv`](results.csv): every scored run.
- [`pilot.csv`](pilot.csv): every pilot run.
  - `pilot_v1` holds runs on first-version items that were later hardened or dropped.
  - `pilot_v2` and `pilot` hold runs on the final versions.
- [`arms/`](arms/): the exact skill bodies per arm.
- [`items/`](items/): items and keys.
- [`scripts/`](scripts/): runner, grader, aggregation, and the writer briefs.

## Per-arm tables

### debloat

| Arm | Seeded points | Hit / partial / miss | Control runs flagged | Ask on seeded | Mean tokens | Median wall (s) |
| --- | --- | --- | --- | --- | --- | --- |
| plain | 10.5/15 | 9 / 3 / 3 | 0/6 | 0 | 3,940 | 8 |
| cur | 7.5/15 | 4 / 7 / 4 | 0/6 | 0 | 4,985 | 14 |
| add | 13.5/15 | 13 / 1 / 1 | 0/6 | 0 | 4,914 | 14 |

### drill

| Arm | Seeded points | Hit / partial / miss | Control runs flagged | Ask on seeded | Mean tokens | Median wall (s) |
| --- | --- | --- | --- | --- | --- | --- |
| plain | 9.5/15 | 7 / 5 / 3 | 3/6 | 0 | 46,162 | 27 |
| cur | 8.5/15 | 5 / 7 / 3 | 0/6 | 1 | 51,586 | 33 |
| add | 10.5/15 | 9 / 3 / 3 | 4/6 | 3 | 60,023 | 38 |

Seeded points by tag:

| Tag | plain | cur | add |
| --- | --- | --- | --- |
| facts | 2.5/3 | 2/3 | 3/3 |
| readings | 1.5/6 | 1.5/6 | 3.5/6 |
| terms | 5.5/6 | 5/6 | 4/6 |

### handoff

| Arm | Seeded points | Hit / partial / miss | Control runs flagged | Ask on seeded | Mean tokens | Median wall (s) |
| --- | --- | --- | --- | --- | --- | --- |
| plain | 5/9 | 1 / 8 / 0 | 1/6 | 0 | 5,568 | 15 |
| cur | 6/9 | 3 / 6 / 0 | 0/6 | 0 | 5,937 | 16 |
| add | 7.5/9 | 6 / 3 / 0 | 6/6 | 0 | 6,889 | 24 |
| add2 | 9/9 | 9 / 0 / 0 | 4/6 | 0 | 6,447 | 21 |

Seeded points by tag:

| Tag | plain | cur | add | add2 |
| --- | --- | --- | --- | --- |
| assumptions | 2/3 | 2/3 | 3/3 | 3/3 |
| moot | 3/6 | 4/6 | 4.5/6 | 6/6 |

### onward

| Arm | Seeded points | Hit / partial / miss | Control runs flagged | Ask on seeded | Mean tokens | Median wall (s) |
| --- | --- | --- | --- | --- | --- | --- |
| plain | 7/12 | 2 / 10 / 0 | 3/6 | 8 | 5,949 | 12 |
| cur | 6.5/12 | 1 / 11 / 0 | 1/6 | 8 | 6,471 | 16 |
| add | 7/12 | 3 / 8 / 1 | 1/6 | 6 | 6,463 | 15 |

Seeded points by tag:

| Tag | plain | cur | add |
| --- | --- | --- | --- |
| done | 4/6 | 3.5/6 | 4/6 |
| moot | 3/6 | 3/6 | 3/6 |

### panel

| Arm | Seeded points | Hit / partial / miss | Control runs flagged | Ask on seeded | Mean tokens | Median wall (s) |
| --- | --- | --- | --- | --- | --- | --- |
| plain | 2/3 | 1 / 2 / 0 | 3/6 | 0 | 8,645 | 29 |
| cur | 2.5/3 | 2 / 1 / 0 | 1/6 | 0 | 63,212 | 57 |
| add | 2/3 | 1 / 2 / 0 | 4/6 | 0 | 79,708 | 71 |

### rearm

| Arm | Seeded points | Hit / partial / miss | Control runs flagged | Ask on seeded | Mean tokens | Median wall (s) |
| --- | --- | --- | --- | --- | --- | --- |
| plain | 9/15 | 7 / 4 / 4 | 2/6 | 3 | 111,889 | 55 |
| cur | 10.5/15 | 9 / 3 / 3 | 0/6 | 0 | 101,724 | 66 |
| add | 11/15 | 9 / 4 / 2 | 0/6 | 0 | 108,350 | 59 |

### settle

| Arm | Seeded points | Hit / partial / miss | Control runs flagged | Ask on seeded | Mean tokens | Median wall (s) |
| --- | --- | --- | --- | --- | --- | --- |
| plain | 4/18 | 2 / 4 / 12 | 0/18 | 0 | 42,635 | 25 |
| cur | 6.5/18 | 5 / 3 / 10 | 1/18 | 0 | 45,854 | 26 |
| add | 11/18 | 9 / 4 / 5 | 4/18 | 1 | 51,741 | 28 |
| addB | 2.5/12 | 2 / 1 / 9 | 2/6 | 0 | 59,912 | 32 |

Seeded points by tag:

| Tag | plain | cur | add | addB |
| --- | --- | --- | --- | --- |
| answered | 1/12 | 1/12 | 5.5/12 | 2.5/12 |
| presupposition | 3/6 | 5.5/6 | 5.5/6 | – |

### sitrep

| Arm | Seeded points | Hit / partial / miss | Control runs flagged | Ask on seeded | Mean tokens | Median wall (s) |
| --- | --- | --- | --- | --- | --- | --- |
| plain | 2.5/3 | 2 / 1 / 0 | 5/6 | 0 | 6,016 | 13 |
| cur | 2/3 | 1 / 2 / 0 | 5/6 | 0 | 6,443 | 15 |
| add | 3/3 | 3 / 0 / 0 | 5/6 | 0 | 6,669 | 17 |
