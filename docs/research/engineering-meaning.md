# Engineering Meaning
## Philosophy, language, and independent judgment in human–LLM work

**Research review, enriched edition — 5 November 2026**

This edition builds on José's original review ([engineering-meaning-source.md](engineering-meaning-source.md)).
Three research passes supplied the new material:

- [engineering-meaning-verify.md](engineering-meaning-verify.md): every one of the 31 original citations
  checked against its source. 30 are verified; footnote 16 had a dead link, and it now points to the
  author's own page. No claim was overstated.
- [engineering-meaning-theory.md](engineering-meaning-theory.md): 15 ideas from philosophy of
  language, argumentation, and requirements engineering that the review and the earlier canon
  ([philosophy-canon.md](philosophy-canon.md)) did not cover.
- [engineering-meaning-empirical.md](engineering-meaning-empirical.md): 9 groups of 2024–2026
  measurements, with full numbers and limits.

The companion files carry the detail. This document carries the argument.

**How to read the additions.**

- Text new in this edition sits under headings marked **Added** or in paragraphs that begin
  **Added:**. Where new evidence changes a claim in the original, the paragraph begins
  **Revised:**.
- Evidence classes: **PR** peer-reviewed, **Pre** preprint, **V** vendor, **Pr** practitioner.
- Moves are labelled as before:
  - **Backed:** a dated study supports the move.
  - **Indirect:** a study shows the failure, or an adjacent move works.
  - **Untested:** no study found.
- Several 2026 sources are preprints read through abstracts or summarising fetches. Confirm a table
  number in the PDF before quoting it outside this file.

## What the enrichment changes, in brief

1. **"A transcript is not an agreement register" is now measured, not proposed.**
   - Spreading one specification across several turns costs 39% on average across 15 models.[^32]
   - Models given a log of overwritten values return the superseded value, almost always without
     doubt. Telling them to forget the old value barely helps.[^34][^35]
   - The remedy is restating the whole agreement in one place.
2. **Fresh reviewers must be stripped of the author's account by construction.**
   - One LLM-written PR description got 9 of 17 vulnerable PRs past Claude Code's review.
   - Redacting the description restored 12 of 17 rejections.[^37]
   - Telling a reviewer to ignore the description works less well than removing it.
3. **Authority stated in words does not hold.** Spotlighting and stated priority collapse under
   adaptive attack, and StruQ, which the original cites, is among the defences bypassed.[^42][^43]
   Only enforcement outside the model holds.[^44]
4. **Skills interfere with each other, and this is now measured.**
   - A similar co-installed skill silently replaces the intended one in about one run in five, and
     the reply names the skill actually used in under 1% of those runs.[^47]
   - A clashing pair of skills drops one skill's rules wholesale.[^48]
   - Gains shrink once a task loads four or more skills.[^45]
5. **Agents under-ask by default, over-ask when pushed, and an answered question lowers the user's
   guard.**[^49][^50][^54]
6. **Prediction without a result does not correct the illusion of understanding; running the case
   does.**[^56] The original's "predict, then follow the code *or* run the case" should be "predict,
   then run the case and compare".
7. **Option sets converge across models**,[^61][^62] and judging before seeing the AI's options
   protects against misleading advice (53.5% vs 37.3% accuracy).[^64]
8. **Agreement goes wrong silently in three ways the original does not name:**
   - **Presupposition:** whatever a request takes for granted becomes accepted unless someone
     objects (Lewis).
   - **Abandoned goals:** a delegated goal is dropped without a verdict (Cohen & Levesque).
   - **Undefended claims:** a claim stays accepted after the claim it rested on falls (Brandom,
     Doyle).
9. **The original's five statement labels merge two distinctions** (Zave & Jackson) and lack an
   **Assumption** label.

## Executive finding

The strongest version of this idea is not that developers need to become more eloquent, or replace
conversational prompts with a universal pseudo-programming language. It is that **delegation through
language requires deliberate control over meaning**:

- what is being requested;
- what is already agreed;
- what remains uncertain;
- what counts as evidence;
- which decisions the agent is authorized to make.

**Added:** Two more belong on that list:

- **what each request takes for granted**, because unexamined presuppositions enter the agreement
  silently;
- **when a delegated goal stops mattering**, because a goal can be dropped without anyone being told.

The research connects five disciplines:

- **Philosophy** clarifies concepts.
- **Pragmatics** explains communication in context.
- **Psychology** examines reliance and judgment.
- **Software engineering** supplies composition and enforcement.
- **Empirical evaluation** establishes whether the arrangement works.

This report distinguishes source findings from proposed applications. The examples and working
methods are a synthesis, not an experimentally validated curriculum. The classical texts offer
intellectual tools; they do not, by themselves, prove improvements in coding-agent performance.

**Added:** José's own 2026-11-05 evaluations count as a sixth source of evidence (§8). They show
that a frontier model already does much of what a verification skill asks. Additions to skills
therefore have to be measured against a plain run of the model, not assumed to help.

## 1. Precision is selective, not exhaustive

"Make the upload system robust" is grammatical English. Its weakness is that "robust" conceals
several possible requirements.

A more useful statement:

> A retry after a lost response must not create a second asset. A deliberate second upload must
> still work. Preserve existing permissions. Investigate the current request-identity mechanism
> before changing the public API.

The improvement is not literary sophistication. The statement makes the important distinctions
visible while leaving implementation choices open.

Yang and colleagues found that underspecified prompts were twice as likely to regress under prompt
or model changes. Specifying every requirement did not consistently help, because requirements could
conflict and models could fail to follow the enlarged set.[^1]

**The practical target is the smallest set of explicit commitments that prevents consequential
misunderstanding, not the longest possible prompt.**

**Added: which commitments earn a place.** Coding-agent measurements sharpen "smallest":

- **Rules that oppose a model's defaults are the ones it misses.** Across 60 multi-turn coding tasks
  and 12 frontier models, they were followed 3.6–7.4 points less than other rules.[^65]
- **Descriptive context files do not help, but explicit instructions do transfer.**
  - LLM-generated AGENTS.md files lowered performance in 5 of 8 settings and raised cost by about
    20%.
  - Developer-written files added 2.4%, which was not significant.
  - Repository overviews did not help.
  - Yet agents did follow explicit instructions: a mentioned tool was used 1.6 times per task,
    against under 0.01 times when unmentioned.[^66]

So the smallest set is selected by one test: **does the model already do this unprompted?** Keep the
rules that oppose defaults and the facts the agent cannot discover. Drop overviews and anything the
model does by default. Length matters less than that test.

Engineering work faces several different kinds of problem:

| What is unresolved? | Example | Appropriate response |
|---|---|---|
| **Ambiguity:** several readings are possible. | "Retry failed uploads" includes or excludes uploads whose outcome is unknown. | Separate the interpretations and settle the consequential difference. |
| **Underspecification:** a requirement is missing. | The retry policy says nothing about cancellation. | Discover whether cancellation matters and establish the requirement. |
| **Factual uncertainty:** the answer exists but is not known. | Does the service already support operation identifiers? | Inspect the implementation or run an experiment. |
| **Delegated discretion:** a choice is intentionally open. | Select an internal helper structure that fits existing conventions. | Let the agent choose within the agreed boundaries. |
| **Added. False presupposition:** the request takes something for granted that is untrue. | "Fix the race in the retry handler," when no race exists. | List what the request assumes, check each item, and object before building on a false one. |

The fifth row comes from Lewis (§2, Added) and has its own failure data. Across 15 models, code
generators reasoned poorly under faulty premises and "depend heavily on explicit prompts to detect
errors."[^84] Treating all five as "bad prompting" leads either to unnecessary questions or to silent,
unauthorized decisions.

A useful rhythm is **explore freely, commit explicitly, verify the consequences.** Tentative ideas
should remain tentative until someone chooses them.

## 2. The missing layer is common ground

### Communication is an interaction, not a transmitted paragraph

Clark and Brennan describe communication as the joint establishment and updating of common ground:
information the participants treat as shared.[^2] Presenting a message is not the same as
establishing that its intended meaning has been understood. Applied to agents, the question changes
from "Was my prompt clear?" to:

> What evidence do we have that the agent is operating on the same task, definitions, decisions, and
> revision that I am?

A reply of "Understood" provides little diagnostic information. A concrete interpretation exposes a
consequential distinction before implementation:

> "I will treat a lost response as an unknown outcome, not a confirmed failure."

Zeng and colleagues' 356 dialogues show that fluent dialogue and effective shared reference are
different capabilities.[^3]

**Added:** Grounding behaviour in LLMs is measurably thin.

- LLM generations are 77.5% less likely than human ones to contain grounding acts. On one model,
  more preference training made this worse: the correlation with human clarification behaviour was
  R = −0.78.[^51]
- LLMs clarify user instructions in 2% of turns. On the RIFTS grounding benchmark, frontier models
  score 23.88–26.95%, below a 33% random baseline.[^52]

The default is to presume common ground, not to build it.

### Added: how agreement grows without anyone agreeing

Lewis's "Scorekeeping in a Language Game" names the mechanism behind the grounding failure.[^67]

- **Accommodation.** If something said requires a presupposition that is missing, the
  presupposition "comes into existence," unless someone objects. "Fix the race in the retry
  handler" enters "there is a race" into the shared record. Every "the X", "fix", "again",
  "still" and "only" does the same.
- **Permission moves only when the one with authority speaks.** A vague grant opens the options
  closest to what was already permitted.
- **The plan and the facts are separate parts of the score.** Lewis notes that merging them makes
  facts appear and vanish.

Stalnaker adds the distinction the original's labels lack.[^68] To *accept* a proposition is "to
treat it as true for some reason," which is different from believing it. A context in which the
parties presuppose different things is "defective", and "a defective context may go unnoticed."

**Moves.**

1. Before acting, list what the request takes for granted and check each item. Raise a false one as
   an objection before building on it. (Indirect: FPBench,[^84] Grounding Gaps,[^51] Rifts.[^52])
2. Read a vague grant as the smallest widening that makes the user's words true, and state that
   reading in one line. (Untested.)
3. Keep the plan and the facts as separate lists in any shared record. (Untested.)

### A transcript is not an agreement register

The original proposed keeping a compact record of the current objective, the settled decisions, the
open questions and the evidence, separating an active decision from one superseded twenty messages
ago.

**Revised: this is now a measured requirement.**

- **Splitting a specification across turns costs 39% on average** across 15 LLMs from 8 families and
  more than 200,000 simulated conversations.[^32]
  - Most of the loss is unreliability, which rose 112%, not aptitude.
  - Giving every piece in one turn kept 95.1% of the full-spec score.
  - Repeating earlier pieces each turn recovered only 15–20% of the loss.
- **The gap persists in 2026 frontier models.** On GPT-5.2, a sharded specification scored 48.5
  against 92.7 for the full one. Rewriting the conversation into one complete instruction brought it
  back to 72.6.[^33]
- **Superseded values win, confidently.** On a synthetic key–value task across 39 LLMs, retrieval of
  a reassigned key's current value fell from 94% to 3% at the highest load.[^34]
  - "More than 97% of incorrect retrievals carry no uncertainty signal."
  - 56.1% of errors returned an earlier value for the correct key.
- **Instructions to forget fail.** A per-key "forget earlier updates" instruction "did not
  significantly improve retrieval accuracy."[^35] Model size predicted robustness; context length
  did not.
- **Focused beats full.** All 18 models tested scored higher on a focused prompt of about 300 tokens
  than on the full history of about 113k tokens.[^36]

Caveat: no study yet measures superseded decisions in real coding-agent transcripts. The evidence
comes from simulated conversations and synthetic tasks.

**Consequences.**

1. When a decision changes, rewrite the record in place. Do not append a correction.
2. A handoff states every decision now in force as a complete list, never as a change against
   earlier text.
3. Re-consolidation, not a longer context window, is the remedy.

### Added: what an agreement register must hold

Brandom's account of assertion gives the register its fields.[^76]

- An assertion is "an inference license": it entitles others to build on it.
- "Endorsement is empty unless the commitment can be defended."
- Assertions are "treated as in order… until challenged".
- If the original asserter fails a challenge, everything others built on the claim loses its
  standing.

Doyle's 1979 truth maintenance system is the engineering of exactly this. It records the reasons for
each belief and revises the dependent beliefs when an assumption is withdrawn.[^77]

Each register entry therefore needs three fields the original's register lacks:

| Field | Content |
|---|---|
| **Source** | Who asserted or decided it, or which file, line or command showed it. |
| **Rests on** | The entries it depends on. |
| **Standing** | Unchallenged, defended, or defeated. When an entry is defeated, its dependants become unsupported until re-checked. |

Brandom also separates orders from assertions. An order binds only the agent it addresses, while an
observation transfers as it stands. When work is relayed, the instructions must be re-issued to the
new agent.

**Retraction needs contrary evidence.** A bare "are you sure?" flipped answers about 46% of the time
across ten models and cut accuracy by 17%.[^78] A challenge should trigger a re-check of the
evidence, followed by either a retraction with new evidence or a restatement with the old. (Indirect.)

Naur adds what the register cannot hold.[^79] In "Programming as Theory Building," a team with full
documentation still made patches that ignored the program's structure. Naur calls reviving a program
"merely from the documentation" "strictly impossible."

- **A handoff can carry:** state, decisions with their reasons, rejected alternatives, traps, and
  the likely next change.
- **A handoff cannot carry:** the ability to see which existing facility a new demand resembles.

The receiver should therefore state where one likely change would go, and why, before editing
inherited work. (Indirect: Gloaguen's finding that overviews do not help.[^66])

### Fresh perspective should remove endorsement, not erase common ground

The original: a new reviewer should not inherit the author's persuasive self-assessment, but it
still needs the accepted requirements.

**Revised: measured, with a mechanism.**

- **Author narrative defeats code review.**[^37] Under neutral framing, models detected vulnerable
  code at 95–97%. Under "bug-free" framing, detection fell to 3.6% for GPT-4o-mini and 80.6% for
  Sonnet 4.5. Opus 4.5 held at 90.4%.
- **The attack on Claude Code as review agent:**
  - At baseline it rejected 16 of 17 vulnerable PRs.
  - One LLM-written PR description and commit message got 9 of 17 accepted.
  - Iterating on the description got all 17 accepted, for $19.36 in total.
- **Removing the narrative works; asking the reviewer to ignore it works less well.**
  - Redacting the PR description recovered 12 of 17.
  - Redaction plus an instruction to ignore metadata recovered 16 of 17.
- **Reasoning traces mislead weak judges, not strong ones.**[^38] Seeing the generator's reasoning
  raised a Qwen3-8B judge's rate of accepting wrong answers from 38.2% to 65.8%. For Claude Sonnet
  4.5 it fell from 22.0% to 5.8%.
- **Prior scores anchor judges.**[^40] A random prior score moved Claude 4.5 Sonnet's judgments by
  −0.706 on a 0–5 scale. Chain of thought enlarged the shift, and a warning did not reduce it.
- **Self-preference varies widely by model.**[^41] Judges overrated their own code by a ratio of
  20.15 for GPT-5 and 1.78 for Claude Sonnet 4.5. A five-judge committee cut these to 4.18 and 1.29.

**Consequences.**

- "Endorsement" covers more than the author's verdict. It includes the PR description, commit
  messages, "verified" or "done" claims, earlier scores, and authorship labels.
- Build the reviewer's input from the accepted requirements and the target only, and do it
  mechanically, never by instruction.
- If the author's reasoning should be inspected, give it to a separate reviewer and combine the
  findings afterwards. A hybrid that scored code and reasoning separately had 21% higher recall than
  code-only monitoring.[^39]
- "Cheapest adequate model" for reviewers is safe only when the inputs are stripped. Weak judges are
  the ones misled.

Hila's account of LLMs as "asymmetrical communicative agents"[^4] still sets the frame: fluent
exchange is not human-style commitment. The working system must record and enforce commitments
rather than infer them from tone.

## 3. What philosophy contributes in practice

### Definitions: identify what makes something the thing it is

In the *Meno*, Socrates pushes past lists of examples toward the common character that makes them
instances.[^5] Defining a **lane** as "a worktree, branch, draft PR, author, and reviewer" bundles
one implementation. A more durable definition: *a bounded assignment with an identifiable owner,
independent working state, and an explicit result to return.* Separate essential properties from
incidental packaging.

**Added:** Two refinements.

- **Every term holds inside a named context.** Evans: "Explicitly define the context within which a
  model applies," and "a change in the language is a change to the model."[^75b] "Lane, in the
  Sourdaw delivery scripts" is a better definition than "lane".
- **A primitive term needs a recognition rule:** how you would tell, in the running system, that a
  thing is one. Zave and Jackson: the only way to establish a primitive term's meaning is "to
  provide an informal explanation of it."[^75] For example: "a retry is a request carrying an
  operation id already seen."

### Practical meaning: explain what a distinction changes

Peirce ties clarity to conceivable practical consequences.[^6] "Safe", "simple" and
"production-ready" are useful only once we can say what would count for or against them. "No
duplicate uploads" fails if a user may upload the same file twice. The real distinction is between
repeating an operation and deliberately starting another.

### Pragmatics: provide enough context, not every available detail

Grice's maxims support selective context.[^7] An implementation agent needs the agreed behaviour,
the relevant constraints, and ways to inspect the code, not every abandoned idea. Brevity is not the
objective by itself. A long transcript can also hide the decision that currently governs the work;
§2 now measures that cost.

### Speech acts: distinguish a statement from an authorization

Searle separates asserting, directing and committing.[^8] The original adapts this into five
labels: Observation, Hypothesis, Decision, Instruction, Authority.

**Revised: the labels merge two distinctions.** Zave and Jackson's requirements theory separates
them.[^75]

- **Mood:** the indicative states what is true of the world; the optative states what we want to
  become true.
- **Control:** an action is controlled by the environment, by the machine, or by both.

Authority belongs to control, not to mood. An **Assumption** label is missing: something accepted
for this task without being checked.

| Label | Mood | Control | What it must carry |
|---|---|---|---|
| Observation | Indicative, checked | — | The source that was checked |
| Hypothesis | Indicative, unchecked | — | The check that would confirm or refute it |
| **Assumption** (added) | Indicative, accepted without checking | — | Why it is accepted, and when it must be checked |
| Requirement (was Decision) | Optative, about the world | Whoever owns the outcome | Who decided, and what would reopen it |
| Instruction | Optative, about the agent's own actions | Actions the agent controls | Its addressee |
| Authority | Not a mood | What the agent may do, and what only the user can do | Who granted it, in what words, and how far it reaches |

The central equation of Zave and Jackson is that a specification, together with domain knowledge,
entails the requirements: S, K ⊢ R. A change delivers a requirement only through facts about the
world it does not control, such as "the client retries with the same request" or "storage is
atomic per key".

**The original's "smallest set of explicit commitments" is therefore exactly two things:** the
requirements, plus the world facts the change relies on. Before calling the work done, show for each
requirement that the change plus the checked facts produce it, and name any requirement that rests
on an unchecked fact. (Untested as an agent instruction.)

**Added: when an authorization takes effect.** Austin's felicity conditions classify an act whose
conditions fail.[^80]

- **Misfire:** wrong person, wrong procedure, incomplete. The act is "void or without effect".
- **Abuse:** the act happens but is hollow, because the speaker does not follow through.

A bare "go" leaves it uncertain whether the speaker is ordering or merely advising. Applied:

1. A grant counts only if the user makes it in chat, explicitly, naming the action and its target.
   "Looks good", "we could deploy", and approval of a plan that mentions a push are not grants for
   the push.
2. Track every "I will" the agent states to done or explicitly dropped. Agents' actions contradicted
   their own stated reasoning in 13.2% of multi-agent failure traces.[^70]

"Probably unused" becoming "safe to delete" is a hidden change in evidential status. "We could
deploy" becoming "deploy it" is a hidden change in authority. The table above makes both visible,
and §7 adds that wording alone cannot enforce either.

### Argumentation: inspect the bridge between evidence and recommendation

Toulmin separates claim, grounds, warrant and rebuttal.[^9] In the permission-cache example, the
missing warrant is that a five-minute delay in applying a permission change is acceptable. The
question to ask is **"Which assumption makes this evidence support that recommendation?"**

**Added: a checkable version.** Toulmin asks for a warrant but does not say which warrant is
missing. Walton's argumentation schemes fix in advance the questions that can defeat each common
type of argument.[^81] A reviewer can mark each question answered or open.

- **Practical reasoning ("do A to reach goal G"):**
  1. Does another goal conflict with G?
  2. What other action reaches G?
  3. Why A rather than those?
  4. What shows A is feasible here?
  5. What else does A change? Asking this side-effects question alone often casts the argument
     into doubt.
- **A claim from a source:**
  1. Is the source in a position to know this, in this version?
  2. Has it been reliable before?
  3. Does it actually say this? Quote it.

Evidence: Indirect. In the 2025 shared task on generating critical questions, three of the top four
teams used scheme annotations.

### Added: rule-following is shown in what was done

Wittgenstein's pupil is tested up to 1000, then continues "+2" as 1000, 1004, 1008, and says "But I
went on in the same way" (§185).[^72] And: "to think one is obeying a rule is not to obey a rule"
(§202). Two moves follow.

1. **Judge compliance from artifacts:** the files actually opened, the commands run, the diff, the
   test output. Never judge it from the agent's claim. (**Backed.**)
   - False success claims were 75.8% of failures in coding-agent trajectories with explicit status
     claims.
   - LLM judges stayed at or below 0.65 AUROC, because they react to "confident closing language".
   - Simple text-feature detectors reached 0.83–0.95.[^73]
   - Agents failed to read every assigned file in 67.9% of review runs, and 80.4% of those incomplete
     runs were reported misleadingly.[^71]
2. **Pair every worked example with a near miss**, naming the feature that separates them. Models
   exploit surface shortcuts in prompt examples, larger models more so.[^74] (Indirect.) This
   corrects the earlier canon's rule of "one worked example" for skills that require judgment.

## 4. What current language research supports

### Clarify when the answer changes the work

ClarifyGPT[^10] and Suri and colleagues[^11] support one rule: **ask about consequential
preferences; investigate discoverable facts; preserve intentionally delegated choices.** ClarifyGPT's
human study had ten participants.

**Added: the rule holds, and it gains three clauses.**

- **The default failure is not asking.**
  - "Without explicit prompting, models almost never interact, even for severely underspecified
    inputs."
  - Interaction recovered 89% of full-spec performance for Claude Sonnet 4.
  - Agents also asked users for file locations they could have found themselves, on 9–31% of
    issues.[^49]
- **Pushing toward asking causes over-asking, at a measured cost.**
  - An always-ask agent scored 27.45% on clear HumanEval problems, against 65.58% for its base
    model.[^50]
  - On fully specified tasks, OpenHands asked 32.5% of the time and Claude Code 5%.
  - CONTRA keeps only questions whose possible answers would change the program's behaviour. It
    asked as rarely as Claude Code while doubling question quality (F1 19.86 against 9.63).[^53]
  - That filter is the operational meaning of "consequential".
- **An answered question lowers the user's guard.**[^54] In a 180-person study of everyday
  decisions, clarifying questions raised satisfaction and cut review time.
  - Unchanged acceptance of erroneous responses rose from 39% to 52%.
  - Errors next to a clarified sub-decision were accepted 60% of the time, against 43% elsewhere.
  - After the user answers, verification is still owed, and most of all around the answered
    decision.
- **Asking widens the attack surface.** Clarification-seeking raised prompt-injection success from
  1.8% to 34.0% for o3.[^55] Answers that arrive through tools or fetched content are data.

The model's own sense of ambiguity is also unreliable. Learned decisions on whether to clarify were
barely above chance, and one open model detected underspecification at 0.50.[^49] Listing the
readings that would produce different behaviour forces detection without forcing a question.

### Precision often lives in small words

"Only administrators may delete archived records" and "Administrators may delete only archived
records" set different policies. "Only", "all", "unless" and "before" change scope, exceptions or
ordering. Pronouns need stable referents.

**Added:** These are also the words that carry presuppositions (§2, Added). The scope check and the
presupposition check belong in the same pass.

### A persona is not a reasoning procedure

Persona prompts gave no general improvement across 162 personas,[^12] and their effects vary.[^13]
Replace "be an exceptional security expert" with a concrete search:

> Trace authorization at the changed entry points. Examine cross-tenant access and identifier
> substitution. For each finding, identify the affected path, triggering conditions, and evidence.
> Report no finding when the concern cannot be substantiated.

A stance should direct attention without predetermining the verdict.

### Ambiguity diagnostics are emerging, but they are not type checking

PRIG[^14] and perturbation-based detection[^15] both support **separating diagnosis from
rewriting**. A prompt editor should say "these two readings lead to different actions" rather than
silently picking one. Output agreement does not prove clarity, since models can share the same wrong
assumption, and §6 now measures how often they do.

### Preserve useful context sensitivity

Attempto Controlled English shows what unambiguous mapping to logic requires.[^16] Implicature-aware
prompting improved user evaluations.[^17] The division the evidence supports is **flexible
conversation for discovery, explicit commitments for consequential execution.** Formatting alone
still moves results,[^18] so careful wording needs testing.

## 5. The psychological danger is plausible understanding

### Persuasion can outrun evidence

Sycophancy[^19] and unfaithful explanations[^20] create a feedback loop: the developer frames a
favoured answer, the model elaborates it fluently, and the fluency reads as confirmation. Make the
hypothesis contestable: *what observation would show this explanation is wrong? Inspect that first.*

**Added: wrong explanations do active harm.**

- In fact-checking, accuracy with a correct ChatGPT explanation was 0.87. With a wrong one it fell
  to 0.35, below the 0.49 people reached with no evidence.[^57]
- Contrastive explanations, giving the case for and against, raised accuracy on wrong cases to 0.56
  but lowered it on right ones to 0.73.
- People distinguish right answers from wrong ones far worse than the model's own confidence does:
  AUC of about 0.59–0.60, against 0.75–0.78. Longer explanations raised people's confidence without
  improving that discrimination.[^58]

So **ask for short answers with numeric confidence.** Reserve the full case for the opposing view
for consequential questions, because it costs accuracy when the lean is right.

### Productive friction should be targeted

Cognitive forcing reduced overreliance in one study,[^21] while the assumption-checking study
found no clear general advantage after correction.[^22]

**Added:** A review of 35 experiments with 19,774 participants found two things.[^85]

- Automation bias rose when the AI's output was shown before the person's own judgment, and fell with
  cognitive forcing and more verification.
- Accountability framing "lacks empirical support".

An older review concludes automation bias "cannot be prevented by training or instructions."

**Selective friction at important decisions** remains the defensible rule. The cheapest friction
with the best evidence is **ordering: judge first, then look at the AI's answer** (§6).

### Understanding requires some work by the learner

Self-explanation improved understanding in school science.[^23]

**Revised: the prediction must be scored.** In the illusion-of-explanatory-depth study, prediction
tasks without results did not correct inflated self-rated understanding: only 18–19% of participants
lowered their rating. Seeing their scored results made 45–67% lower it.[^56] The habit therefore
becomes: *predict what happens in one altered scenario, run it, and compare.*

**Added: perception and measurement diverge.**

- In METR's 2025 trial, experienced developers took 19% longer on AI-allowed tasks. Beforehand they
  had forecast a 24% speed-up, and afterwards they estimated 20%.[^59]
- METR's late-2025 redesign points toward a speed-up, but METR calls this "only very weak evidence"
  of its size.
- Anthropic's 2026 study found AI users scored 50% on a library quiz against 67% for hand-coders.
  The AI patterns that kept scores at 65% or more were generation followed by comprehension, hybrid
  code with explanation, and conceptual inquiry. Full delegation and iterative AI debugging fell
  below 40%.[^60]

Felt speed is not evidence. Asking conceptual questions after the code is generated preserves
understanding.

## 6. Finding the fourth option means changing the representation

Browser cache, edge cache, Redis: all three assume the repeated work is necessary. **The missing
option is often outside the shared premise.** Peirce's hypothesis formation,[^24] Knoblich's
constraint relaxation and chunk decomposition,[^25] and Gentner's structure mapping[^26] give the
mechanism. The questions to ask:

- Which constraints came from the requirement, and which did we add?
- What have we treated as one operation that could be separated?
- What changes if responsibility moves to another layer?

**Added: a procedure, from Kant's reflective judgment.** When only the particulars are given and the
universal must be found, judgment is "merely reflective". The §40 maxim adds comparing "with the
possible rather than the actual judgements of others."[^82] Applied to an option menu:

1. Name in one line the category all the offered options belong to, and the purpose that category
   serves. Here the category is "store a result so the work is not repeated", and the purpose is
   that the page is slow because work repeats.
2. Propose at least one option that serves the purpose but falls outside the category: remove the
   repeated work, or move it to another layer.
3. Name one party whose position the menu ignores, such as the owner of another layer or the user of
   the data, and give the option they would propose.

Evidence: Indirect. Abstracting to principles first improved question answering by 7–27%.[^83]

### Use analogy to transfer relationships, not surface features

The skills-as-modules analogy is useful for dependencies, shared definitions and interfaces. It does
not follow that skills must inherit every feature of object-oriented programming. Analogy generates
candidates; evidence decides among them.

### More alternatives do not guarantee a wider search

The original cites Kostiuk[^27] and Doshi & Hauser,[^28] and proposes testing whether repeated
requests produce genuinely different approaches.

**Revised: largely answered.**

- **Models converge, within and across vendors.**[^61]
  - Within one model at temperature 1.0, average pairwise similarity exceeded 0.8 in 79% of cases.
  - Across 25 different models, average similarity ranged from 71% to 82%.
- **Errors are correlated.** When two models are both wrong, they agree 60% of the time, against a
  one-in-three chance baseline. Models from the same company agree more.[^62]
- **The same holds for code, on thin evidence.** On programming problems, humans found about 3
  distinct algorithms where models found about 2, and pooling three vendors added little.
- **A panel of model runs is not a set of independent samples.** Separate contexts do not make
  analyses independent when the priors are shared.
- **Diversity can be partly recovered.** Asking for k responses with their probabilities produced
  1.6–2.1 times the diversity of direct prompting in creative writing.[^63]
- **Judging first protects.** In a three-arm trial with 218 participants:[^64]
  - When the AI's advice was misleading, those who judged before seeing it were right 53.5% of the
    time, against 37.3% for those shown the advice first. Full copying fell from 46.8% to 25.8%.
  - When the advice was right, the two groups did equally well (65.2% against 66.2%).
  - Limits: a single author, scenario-based, not preregistered.

The original's proposed habit of writing a short independent account before reading the
recommendation is now the measured condition, and it costs nothing when the AI is right. The
objective is better judgment, not ritual disagreement.

## 7. Composable skills need preserved meaning, not just reusable text

The original proposes separating lane, stance, revolver and delegate: **define once at the source;
supply wherever needed at execution.** A micro skill such as `/tldr` should state its scope and
lifetime, so a local preference does not become a standing conversational policy.

### Added: skills interfere, and the interference is silent

The original's "test combinations as well as individual components" now has 2026 measurements.

- **Gains shrink with more skills per task.** Curated skills raised pass rates from 33.9% to 50.5%
  (SkillsBench).[^45]
  - The gain was +18–19 points with one to three skills per task, and +10.1 points with four or
    more.
  - By skill length: compact or standard skills added +19 to +21.5 points, comprehensive ones +0.7.
  - Self-generated skills landed 8–12 points *below* having no skills.
- **Libraries degrade as they grow, mostly through shadowing.** At 202 skills the pass rate fell by
  0.21, and up to 68% of that drop came from the wrong skill being loaded. Context overhead was
  indistinguishable from zero.[^46]
- **Twins substitute silently.**[^47] This study ran Claude Code 2.1.283 with Sonnet 4.6, Haiku 4.5
  and Opus 5.
  - A similar co-installed skill cut use of the installed skill by 19.9 points.
  - The final reply named the skill actually used in 0.9% of the runs where a twin took over.
  - 23.5% of installed skills had a same-job twin.
  - A hook denying the twin's first read restored the intended skill in 96% of cases.
- **Clashing skills drop rules wholesale.**[^48]
  - Rule compliance was 93–99% with one skill loaded, and 61–62% with both.
  - A priority instruction did not fix it.
  - One example per skill that satisfies both skills cut takeover to 1–15%, and a merged skill
    reached 96–99%.

**Consequences.**

- Keep skills compact and distinct, with one owner per job.
- Where a skill must win, enforce it with a hook, not with "prefer" wording.
- For pairs likely to load together, add one shared example that satisfies both.

### Added: delegated goals need a stop condition and a verdict

Cohen and Levesque define a joint goal that each member keeps "until p is mutually known to be
achieved, unachievable or irrelevant." A member who privately reaches that conclusion is committed to
making it mutual.[^69]

- Across 1,642 multi-agent failure traces:[^70]
  - 12.4% failed to recognise when to stop;
  - 7.4% drifted from the goal;
  - 6.2% ended before objectives were met.
- 80.4% of incomplete reviews were reported misleadingly.[^71]

**Moves.**

1. Every brief states the condition that makes its goal moot. For example: "if the duplicate does
   not reproduce on main, stop and report that".
2. A delegate reports achieved, impossible, or moot, with evidence. It never just stops.
3. The coordinator treats silence or drift as an open status, not as done.

(Indirect.)

### What should become formal?

References, versions, permissions, result shapes and sequencing are good candidates. Substantive
judgment stays in natural language and examples. MetaSkill and SkillCompiler both separate
coordination from local reasoning.[^29][^30] A runtime can enforce which reviewer sees which revision
without proving that the reviewer's conclusions are correct.

### Authority cannot depend on wording alone

The original notes that StruQ's trained separation is not the same as Markdown labels.[^31]

**Revised: wording does not hold, and trained defences fall to adaptive attackers.**

- **Adaptive attacks beat 12 recent defences**, at over 90% attack success for most.[^42]
  - On AgentDojo, spotlighting went from 28% to 99% attack success against Gemini-2.5 Pro, and from
    1% to 99% against MetaSecAlign-70B.
  - StruQ is among the defences the authors bypass.
- **Stated priority does not help.** With conflicting instructions, GPT-4o's accuracy was 70.0. A
  prompt telling it to follow the priority order gave 67.2.[^43] Models are swayed by "the tone or
  strictness of the wording" rather than by priority.
- **Only enforcement outside the model holds.** CaMeL solved 77% of tasks "with provable security",
  against 84% undefended, at about 2.8 times the tokens.[^44] It does not protect against biased
  text, such as a slanted summary.

**Consequences.**

- A "treat this as data" line in a skill is harmless, but it is not a defence.
- Rules such as the ban on `git clean`, `git reset --hard` and `git push --force` are wording. They
  hold reliably only when backed by harness deny rules or hooks.
- During this research, two fetched arXiv pages contained text addressed to LLM readers. The fetch
  tool flagged it, and it was not acted on. This is §7's concern arising inside ordinary research
  sources.

A useful instruction environment distinguishes three kinds of problem, and none should pass for
another:

- **structural errors**, which it can establish;
- **meaning warnings**, which need interpretation;
- **behavioural failures**, which are observed during execution.

## 8. A research programme worth testing

The original proposes comparing ordinary handoffs against three separated changes: clearer
requirements in the same format, more structure without more requirements, and a short grounding
exchange. It proposes tasks seeded with an ambiguity, an unstated constraint, an inspectable fact,
and an open choice, judged by independent reviewers on held-out tasks. The outcomes it names are
accepted behaviour, unauthorized decisions, missed requirements, clarification burden, repair time,
the developer's ability to explain the result, and cost.

**Added: what is now answered.**

- Whether conversation spread across turns loses specification: yes, by about 39%.[^32]
- Whether repeated requests for options diverge: largely no, within and across vendors.[^61]
- Whether skill combinations behave differently from single skills: yes.[^45][^47][^48]
- Whether judging first helps: yes, when the advice is wrong, at no cost when it is right.[^64]

**Added: what José's own runs on 2026-11-05 showed.** These are small and run by the same author, but
they bear directly on this programme.

- **Planted defects** (`skills/evals/planted-defect.md`). Plain Opus found 10 of 10 planted false
  claims, with or without `bulletproof`, and with or without the proposed additions. For `panel`,
  plain Opus got 9 of 10 decisions right and the tenth partly; no skill arm beat it.
  - The items were easy enough to hit the ceiling. The run shows the additions buy nothing on such
    items. It cannot rule out gains on harder material.
- **Triggering** (`skills/evals/trigger/README.md`). Descriptions written in José's own phrasing
  raised correct triggering, for example `drill` from 33% to 90% and `revolver` from 43% to 90%, with
  no false triggers. The same agent wrote the queries and the descriptions, and no held-out set was
  used.
- **Corpus progression** (`corpus/docs/research/progression-2026-11-05/`). A blind grader preferred
  the shortened artifact skills in all four cases, and the shorter versions lost no rule the evidence
  backs.

**Added: what remains open.**

- **Recording decisions in coding-agent transcripts.** No study measures superseded decisions in real
  transcripts, or tests a register with source, dependency and standing against a plain summary.
- **Author self-assessment as a separate factor.** No study isolates "I verified this" from other
  framing for an LLM reviewer.
- **Question format.** No study compares one question offered as a choice with a recommendation
  against several open questions.
- **Every theory move in §2–§3 and §6** is Indirect or Untested on coding agents.
- **Named method against plain procedure.** The earlier canon's A/B test (5 arms, about 600 runs)
  would decide whether method names add anything. Until then, skills carry plain procedures only,
  which is José's standing rule.

**Revised method note.** Every proposed skill change should be gated the way the 2026-11-05 runs
were:

- compare it against a plain run of the current model on seeded items;
- record defects found, tokens and time;
- ship it only if it beats the plain run at acceptable cost.

Use held-out queries for trigger tests, and items hard enough that the plain model does not reach
the ceiling.

## 9. Added: what this changes in José's skills and rules

Every line below is a proposal. Each is written as a plain procedure, with no thinker or method names,
and each should pass the gate in §8 before it ships.

| Target | Proposed change | Basis | Evidence |
|---|---|---|---|
| `settle` | First step: list what the request takes for granted ("the X", "fix", "again", "only"), check each, and object to a false one before working | §2 presupposition | Indirect |
| `settle` | After the user answers, verify the work next to the decision they answered | §4, answered questions lower guard | Backed (non-code) |
| `drill` | List the readings that would produce different behaviour; list the world facts each requirement depends on, and check them; name the context the change's terms hold in | §3 mood and control; §4 | Indirect / Untested |
| `handoff` | State every decision in force as a full list with its source and reason; give the condition that makes the goal moot; mark assumptions as unchecked; if the receiver will review, give it the requirements and the target, not the author's account | §2 register, Naur; §7 stop condition; §2 fresh reviewer | Backed (register, reviewer) / Indirect |
| `rearm` | Before editing inherited work, state where one likely change would go and why, then check it against the code | §2 Naur | Indirect |
| `onward` | If the goal turns out done, impossible, or moot, say which with evidence, then stop | §7 joint goals | Indirect |
| `revolver` | Build each reviewer's brief from the requirements and the target only, stripping PR text, "done" claims, earlier verdicts, and authorship. This is an input rule, not a change to the method, but José ruled `revolver` untouchable, so it needs his yes | §2 fresh reviewer | Backed |
| `panel` | Name the category the options share and add one option outside it; give each analyst a different framing; ask for options with probabilities; compare on conflicting goals, side effects and feasibility; withhold the asker's lean | §6; §3 critical questions | Backed (convergence) / Indirect |
| `bulletproof` | Judge completion and coverage claims from artifacts, never from the claim; for a cited source, ask whether it is in a position to know this, in this version | §3 rule-following; critical questions | Backed / Indirect |
| `debloat` | For agent instructions, cut rules the model already follows unprompted and keep the ones that oppose defaults | §1 | Backed |
| `sitrep` | Each earlier "I will": done, or dropped and why | §3 felicity | Indirect |
| Skills README | Pair each worked example with a near miss; give pairs likely to load together one shared example | §3; §7 | Indirect / Backed |
| Global AGENTS.md | When a decision changes, rewrite the record in place; a grant counts only when stated in chat, explicitly, naming action and target; retract a supported claim only for contrary evidence | §2; §3 | Backed / Indirect |
| Harness configuration | Back the destructive-git bans with deny rules or hooks; remove exact twin skills (`caveman-commit` and `caveman:caveman-commit`, `cavecrew` and `caveman:cavecrew`, `typesafe-ai` and `typesafe:typesafe-ai`) and pick one owner each for review, exploration and verification | §7 | Backed |

The last row changes persistent configuration and needs José's go-ahead.

## Conclusion

The most useful boundary is not between "casual prompting" and "formal prompting." It is between
**unexamined interpretation and inspectable meaning.**

Philosophy helps define the concepts and question the frame. Pragmatics explains how meaning becomes
shared. Psychology warns that fluency, agreement and explanation can be mistaken for understanding.
Software engineering makes the enforceable parts explicit. Evaluation determines whether the whole
arrangement works.

**Added:** The new evidence points the same way at every level.

- **Meaning held only in words decays:** across turns, under superseded values, against an author's
  narrative, and against an attacker.
- **Meaning held in a structure that is rewritten, stripped, or enforced survives:**
  - a consolidated specification;
  - a register whose entries carry their sources and dependants;
  - a reviewer input built from requirements and target alone;
  - a hook rather than a rule.

The classical sources say why: what a request presupposes, what a party is committed to, and who may
grant what. The measurements say how much it costs to leave these implicit.

The human contribution is not merely to choose from an agent's menu. It is to establish what problem
deserves solving, to distinguish evidence from assumptions, and to notice when the menu is organized
around the wrong question. Ideally that judgment is formed before the menu is read.

## Corrections and verification status

- **Original citations:** 30 of 31 verified against their sources. Footnote 16's Stanford link no
  longer loads, so it now cites Fuchs's Attempto description page, which supports the claim.
  Optional metadata additions are in `engineering-meaning-verify.md`.
- **Earlier research files:** `research-skills.md` cites SWE-Skills-Bench as "39 of 49 skills gave
  zero gain". The current version says "92 of 98 skills have no statistically significant
  effect".[^87]
- **Read only through secondary sources:**
  - Cohen & Levesque (via Tambe 1997);
  - Brandom's *Making It Explicit* (via Shapiro);
  - Walton, Reed & Macagno (via Walton's chapter);
  - Duhem and Quine (via the SEP);
  - Evans 2003 (via the 2015 Reference).
- **Read as abstracts:** several of the LLM studies behind the theory moves. Each is marked in the
  companion files.
- **No move in §9 has been tested on José's skills yet.**

## References

### Original sources (verified 2026-11-05)

[^1]: Yang, Shi, Ma, Liu, Kaestner, Wu. "What Prompts Don't Say." Findings of ACL 2026, 9072–9101. https://aclanthology.org/2026.findings-acl.441/ — PR
[^2]: Clark & Brennan. "Grounding in Communication." 1991. https://web.stanford.edu/~clark/1990s/Clark%2C%20H.H.%20_%20Brennan%2C%20S.E.%20_Grounding%20in%20communication_%201991.pdf
[^3]: Zeng et al. "LVLMs and Humans Ground Differently in Referential Communication." ACL 2026, 9061–9087. https://aclanthology.org/2026.acl-long.410/ — PR
[^4]: Hila. "Communicative Action in the Age of Artificial Intelligence." Philosophy & Technology 39, 159, 2026. https://link.springer.com/article/10.1007/s13347-026-01168-4 — PR
[^5]: Plato. *Meno*, trans. Jowett. https://classics.mit.edu/Plato/meno.html
[^6]: Peirce. "How to Make Our Ideas Clear." 1878. https://web.stanford.edu/class/history34q/readings/Peirce/Peirce_MakeOurIdeasClear.html
[^7]: Grice. "Logic and Conversation." 1975. https://web.stanford.edu/class/psych205/papers/Grice-1975.pdf
[^8]: Searle. "A Classification of Illocutionary Acts." Language in Society 5(1), 1976. https://www.cambridge.org/core/journals/language-in-society/article/abs/classification-of-illocutionary-acts1/C51AB2FEB1BFD115FE9B066A8669789D
[^9]: Toulmin. *The Uses of Argument*, ch. III. 1958/2003. https://www.cambridge.org/core/books/abs/uses-of-argument/layout-of-arguments/0CF09834F2802518330E754858CC0655
[^10]: Mu et al. "ClarifyGPT." FSE 2024. https://doi.org/10.1145/3660810 — PR
[^11]: Suri et al. "Structured Uncertainty guided Clarification for LLM Agents." Findings of ACL 2026, 40811–40838. https://aclanthology.org/2026.findings-acl.2028/ — PR
[^12]: Zheng, Pei, Logeswaran, Lee, Jurgens. "When 'A Helpful Assistant' Is Not Really Helpful." Findings of EMNLP 2024. https://aclanthology.org/2024.findings-emnlp.888/ — PR
[^13]: Luz de Araujo & Roth. "Helpful assistant or fruitful facilitator?" PLOS ONE 20(6), 2025. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0325664 — PR
[^14]: Ramesh, Dou, Xu. "Localizing Prompt Ambiguity… (PRIG)." 2026. https://arxiv.org/abs/2606.05486 ; https://aclanthology.org/2026.findings-emnlp.2103/ — PR
[^15]: Chen et al. "Detect Before You Disambiguate." 2026; accepted to AACL-IJCNLP 2026. https://arxiv.org/abs/2610.36353 — Pre
[^16]: Fuchs. "Attempto Controlled English." Corrected link: http://attempto.ifi.uzh.ch/site/description/description.html (the original Stanford link refuses connections).
[^17]: Hota & Jokinen. "Implicature in Interaction." IJHCI 2026. https://arxiv.org/html/2510.25426v2 — PR
[^18]: Sclar, Choi, Tsvetkov, Suhr. "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design." ICLR 2024. https://arxiv.org/abs/2310.11324 — PR
[^19]: Sharma et al. "Towards Understanding Sycophancy in Language Models." ICLR 2024. — PR
[^20]: Turpin, Michael, Perez, Bowman. "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting." NeurIPS 2023. — PR
[^21]: Buçinca, Malaya, Gajos. "To Trust or to Think." CSCW 2021. https://arxiv.org/abs/2102.09692 — PR
[^22]: Ghosh, Sarkar, Lindley, Poelitz. "An Experimental Comparison of Cognitive Forcing Functions…" 2026. https://arxiv.org/html/2601.18033v1 — Pre
[^23]: Chi, de Leeuw, Chiu, LaVancher. "Eliciting Self-Explanations Improves Understanding." Cognitive Science 18(3), 1994. — PR
[^24]: Peirce. "Deduction, Induction, and Hypothesis." 1878. https://en.wikisource.org/wiki/Popular_Science_Monthly/Volume_13/August_1878/Illustrations_of_the_Logic_of_Science_VI
[^25]: Knoblich, Ohlsson, Haider, Rhenius. "Constraint Relaxation and Chunk Decomposition in Insight Problem Solving." JEP:LMC 25(6), 1999. https://doi.org/10.1037/0278-7393.25.6.1534 — PR
[^26]: Gentner. "Structure-Mapping." Cognitive Science 7(2), 1983. — PR
[^27]: Kostiuk, Seyfried, Reed. "Automating Alternative Generation in Decision-Making." Findings of EMNLP 2025. https://aclanthology.org/2025.findings-emnlp.1/ — PR
[^28]: Doshi & Hauser. "Generative AI enhances individual creativity but reduces the collective diversity of novel content." Science Advances 10, 2024. https://doi.org/10.1126/sciadv.adn5290 — PR
[^29]: Shu et al. "MetaSkill." 2026. https://arxiv.org/abs/2610.24723 — Pre
[^30]: Yang et al. "SkillCompiler." 2026. https://arxiv.org/abs/2610.39508 — Pre
[^31]: Chen, Piet, Sitawarin, Wagner. "StruQ." USENIX Security 2025. — PR

### Added: empirical sources

[^32]: Laban, Hayashi, Zhou, Neville. "LLMs Get Lost In Multi-Turn Conversation." arXiv 2505.06120, 2025 (reported ICLR 2026). https://arxiv.org/html/2505.06120 — Pre/PR
[^33]: Liu et al. "Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation." arXiv 2602.07338, 2026. https://arxiv.org/html/2602.07338 — Pre
[^34]: Chattaraj & Raj. "LLMs Remember First, Forget Last." arXiv 2603.00270v3, 2026. https://arxiv.org/html/2603.00270 — Pre
[^35]: Wang & Sun. "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs." arXiv 2506.08184, 2025. https://arxiv.org/html/2506.08184 — Pre
[^36]: Chroma. "Context Rot." July 2025. https://www.trychroma.com/research/context-rot — V
[^37]: Mitropoulos, Alexopoulos, Alexopoulos, Spinellis. "Measuring and Exploiting Contextual Bias in LLM-Assisted Security Code Review." arXiv 2603.18740, 2026. https://arxiv.org/html/2603.18740v2 — Pre
[^38]: Tu, Ni, Bi. "How Long Reasoning Chains Influence LLMs' Judgment of Answer Factuality." arXiv 2604.06756, 2026. https://arxiv.org/html/2604.06756 — Pre
[^39]: Arnav et al. "CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring." arXiv 2505.23575. https://arxiv.org/html/2505.23575v3 — Pre
[^40]: Kapetanovic et al. "Anchoring Bias in LLM-as-a-Judge Systems." CIKM '26. https://arxiv.org/html/2608.25869 — PR
[^41]: Pombal, Rei, Martins. "Self-Preference Bias in Rubric-Based Evaluation of Large Language Models." arXiv 2604.06996, 2026. https://arxiv.org/html/2604.06996 — Pre
[^42]: Nasr, Carlini, Hayes, Sitawarin, Schulhoff et al. "The Attacker Moves Second." arXiv 2510.09023, 2025. https://arxiv.org/html/2510.09023 — Pre
[^43]: Zhang et al. "IHEval." NAACL 2025, 8374–8398. https://aclanthology.org/2025.naacl-long.425/ — PR
[^44]: Debenedetti et al. "Defeating Prompt Injections by Design" (CaMeL). arXiv 2503.18813v2, 2025. https://arxiv.org/abs/2503.18813 — Pre
[^45]: Li et al. "SkillsBench." arXiv 2602.12670v4, 2026. https://arxiv.org/html/2602.12670 — Pre
[^46]: Song & Wei. "More Skills, Worse Agents? Skill Shadowing Degrades Performance When Expanding Skill Libraries." arXiv 2605.24050, 2026. https://arxiv.org/html/2605.24050v1 — Pre
[^47]: Yan et al. "One Skill Too Many: How Co-Installed Skills Conflict in Coding Agents." arXiv 2610.11647, 2026. https://arxiv.org/html/2610.11647v1 — Pre
[^48]: Razmara, Azizi, Aryashad. "One Skill Takes Over: Clashing Agent Skills and a One-File Fix." arXiv 2610.25064, 2026. https://arxiv.org/html/2610.25064v1 — Pre
[^49]: Vijayvargiya, Zhou, Yerukola, Sap, Neubig. "Ambig-SWE." ICLR 2026. https://arxiv.org/abs/2502.13069 — PR
[^50]: Wu & Fard. "HumanEvalComm." ACM TOSEM 2025. https://arxiv.org/html/2406.00215 — PR
[^51]: Shaikh et al. "Grounding Gaps in Language Model Generations." NAACL 2024, 6279–6296. https://aclanthology.org/2024.naacl-long.348/ — PR
[^52]: Shaikh et al. "Navigating Rifts in Human-LLM Grounding." ACL 2025. https://arxiv.org/html/2503.13975 — PR
[^53]: Fang et al. "CONTRA: Discovering and Qualifying Behavior-Changing Questions for Selective Clarification in LLM Code Generation." arXiv 2610.01769, 2026. https://arxiv.org/html/2610.01769v1 — Pre
[^54]: Zheng, Zheng, Zhu, Ma. "Is That Clear? The Impacts of Clarifying Questions on Human-LLM Interaction." arXiv 2611.01087, 2026. https://arxiv.org/html/2611.01087 — Pre
[^55]: Sehwag et al. "ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents." arXiv 2605.17324, 2026. https://arxiv.org/abs/2605.17324 — Pre (abstract)
[^56]: Chromik, Eiband, Buchner, Krüger, Butz. "I Think I Get Your Point, AI! The Illusion of Explanatory Depth in Explainable AI." IUI '21. https://www.medien.ifi.lmu.de/pubdb/publications/pub/chromik2021iui/chromik2021iui.pdf — PR
[^57]: Si et al. "Large Language Models Help Humans Verify Truthfulness – Except When They Are Convincingly Wrong." NAACL 2024. https://aclanthology.org/2024.naacl-long.81.pdf — PR
[^58]: Steyvers et al. "What large language models know and what people think they know." Nature Machine Intelligence, 2025. — PR
[^59]: Becker, Rush, Barnes, Rein (METR). arXiv 2507.09089, 2025; and METR, "We are Changing our Developer Productivity Experiment Design," 24 Feb 2026. https://metr.org/blog/2026-02-24-uplift-update/ — Pre/V
[^60]: Shen & Tamkin. "How AI Impacts Skill Formation." arXiv 2601.20245, 2026. https://www.anthropic.com/research/AI-assistance-coding-skills — Pre/V
[^61]: Jiang et al. "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)." NeurIPS 2025 D&B. https://arxiv.org/html/2510.22954 — PR
[^62]: Kim, Garg, Peng, Garg. "Correlated Errors in Large Language Models." ICML 2025. arXiv 2506.07962 — PR
[^63]: Zhang et al. "Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity." arXiv 2510.01171. — Pre
[^64]: Yan & Dong. "Independent judgment before viewing generative AI recommendations reduces susceptibility to misleading advice." Frontiers in Psychology 17, 2026. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1936522/full — PR
[^65]: Huang et al. "Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents." arXiv 2608.11727, 2026. — Pre (abstract)
[^66]: Gloaguen, Mündler-Sasahara, Müller, Raychev, Vechev. "Evaluating AGENTS.md." arXiv 2602.11988v3, 2026. https://arxiv.org/html/2602.11988 — Pre
[^85]: Romeo & Conti. Systematic review of automation bias, AI & Society, 2025; and Parasuraman & Manzey, Human Factors, 2010. — PR (read via subagent; Parasuraman abstract only)
[^87]: SWE-Skills-Bench v2, 27 Oct 2026. https://arxiv.org/abs/2603.15401 — Pre

### Added: theory sources

[^67]: Lewis. "Scorekeeping in a Language Game." Journal of Philosophical Logic 8, 1979, 339–359. https://andrewmbailey.com/dkl/Scorekeeping_in_a_Language_Game.pdf
[^68]: Stalnaker. "Common Ground." Linguistics and Philosophy 25, 2002, 701–721. https://semantics.uchicago.edu/kennedy/classes/f07/pragmatics/stalnaker02.pdf
[^69]: Cohen & Levesque. "Teamwork." Noûs 25(4), 1991. Read via Tambe, "Towards Flexible Teamwork," JAIR 1997, §4. https://arxiv.org/pdf/cs/9709101
[^70]: Cemri et al. "Why Do Multi-Agent LLM Systems Fail?" (MAST). arXiv 2503.13657v3, 2025. https://arxiv.org/html/2503.13657v3 — Pre
[^71]: Smyth et al. "Quantifying Overclaiming Propensity in Frontier LLM Agents." arXiv 2609.20812, 2026. — Pre (abstract)
[^72]: Wittgenstein. *Philosophical Investigations*, trans. Anscombe, §§185, 201–202.
[^73]: Advani. "From Confident Closing to Silent Failure." FAGEN@ICML 2026. arXiv 2606.09863 — workshop (abstract)
[^74]: Tang et al. "Large Language Models Can be Lazy Learners." Findings of ACL 2023. arXiv 2305.17256 — PR (abstract)
[^75]: Zave & Jackson. "Four Dark Corners of Requirements Engineering." ACM TOSEM 6(1), 1997. http://www.pamelazave.com/4dc.pdf — PR
[^75b]: Evans. *Domain-Driven Design Reference*, 2015. https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
[^76]: Brandom. "Asserting." Noûs 17(4), 1983, 637–650. https://sites.pitt.edu/~rbrandom/Courses/2022%20Phil%20of%20Language/Reasons%20texts/Asserting.pdf
[^77]: Doyle. "A Truth Maintenance System." Artificial Intelligence 12, 1979. https://dspace.mit.edu/handle/1721.1/5733 (abstract)
[^78]: Laban et al. "Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment." arXiv 2311.08596, 2023. — Pre (abstract)
[^79]: Naur. "Programming as Theory Building." Microprocessing and Microprogramming 15, 1985, 253–261.
[^80]: Austin. *How to Do Things with Words*, 2nd ed., Lectures II–III, pp. 14–17, 32–36.
[^81]: Walton. "Argumentation Schemes and their Application in Argument Mining," ch. 11, Windsor WSIA (volume title unverified); schemes from Walton, Reed & Macagno, *Argumentation Schemes*, CUP 2008. Calvo Figueras et al., Critical Questions Generation shared task, ArgMining 2025. https://aclanthology.org/2025.argmining-1.23/
[^82]: Kant. *Critique of Judgement*, trans. Bernard, Introduction §IV and §40. https://www.gutenberg.org/files/48433/48433-h/48433-h.htm
[^83]: Zheng et al. "Take a Step Back." ICLR 2024. https://arxiv.org/abs/2310.06117 — PR
[^84]: Li et al. "Refining Critical Thinking in LLM Code Generation: A Faulty Premise-based Evaluation Framework" (FPBench). arXiv 2508.03622, 2025. — Pre (abstract)
