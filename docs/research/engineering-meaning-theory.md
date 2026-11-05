# Engineering meaning: what the report misses in language, argument, and requirements theory

Companion to [engineering-meaning-source.md](engineering-meaning-source.md). Written 2026-11-05.
It covers only what that report and the earlier notes ([philosophy.md](philosophy.md),
[philosophy-canon.md](philosophy-canon.md), [philosophy-sources.md](philosophy-sources.md)) do not.
No other file was changed.

## Bottom line

The report has one strong mechanism for meaning: ground the agreement, then mark each statement's
status with five labels (Observation, Hypothesis, Decision, Instruction, Authority). The theory it
leaves out explains how that agreement goes wrong without anyone noticing, and how to repair it.

- **Agreement grows silently.** Whatever an instruction takes for granted becomes accepted unless
  someone objects (Lewis). Every phrase like "fix the race in the retry handler" accepts that a race
  exists. That is the most direct route from a fluent prompt to a wrong change.
- **Delegated goals die silently.** A delegate that decides its goal is met, impossible, or moot owes
  that verdict to the team (Cohen and Levesque). Recent agent studies measure the opposite: false
  "done" claims, and incomplete reviews reported as complete.
- **Following a rule is shown in what was done, not in what is said.** An agent's statement that it
  followed a skill proves nothing (Wittgenstein). One example never fixes a rule: it needs a near miss
  beside it.
- **The five labels need two axes the report merges.** One axis is mood: what is true of the world
  versus what we want to become true (Zave and Jackson). The other is control: who can make it so.
  Authority is about control, not about mood.
- **An agreement register needs sources and defeat.** Each entry records who stands behind it. When an
  entry falls, everything resting on it falls too (Brandom; Doyle's truth maintenance).

Five requested items add little or nothing: the pragma-dialectical rules, Duhem–Quine, Evans's
bounded contexts, Kant's determining judgment, and the §40 maxims as such. Section 4 says why.

**Evidence labels**, for the engineering move rather than the theory:

- **Backed:** a dated LLM or HCI study supports the move or a close version of it.
- **Indirect:** a dated study shows the failure exists, or an adjacent move works.
- **Untested:** no study found.

## 1. Ranking

Ranked by expected value: the size of the failure, times how likely the move is to change agent
behavior, discounted for overlap with what José's skills and `~/.agents/AGENTS.md` already say.

| Rank | Item | The move, in short | Evidence | Lands in |
| --- | --- | --- | --- | --- |
| 1 | Lewis, presupposition and permissibility | List and check what a request takes for granted; only the user widens permission, and only as far as the words force | Indirect | `settle`; global `AGENTS.md` |
| 2 | Cohen & Levesque, joint commitment | Each brief says when its goal becomes moot; the delegate reports achieved, impossible, or moot, never just stops | Indirect | `handoff`, `onward` |
| 3 | Wittgenstein, rule-following | Judge compliance from artifacts, not from the agent's claim; pair each example with a near miss | Backed (artifact check); Indirect (near miss) | `bulletproof`, `revolver`; skills README |
| 4 | Zave & Jackson, moods and control | Sort statements into world facts, requirements, and what the change does; show the change plus checked facts yields each requirement | Untested | `drill`; label set in global `AGENTS.md` |
| 5 | Brandom, with Doyle | Each agreed item carries its source; a failed item takes its dependants down; retract only for contrary evidence | Indirect | `handoff`, `revolver`, `bulletproof` |
| 6 | Naur, theory building | Brief the reasons and rejected options, not only the state; the receiver predicts a modification before editing | Indirect | `handoff`, `rearm` |
| 7 | Austin, felicity conditions | A grant counts only if the right person makes it, completely and explicitly; track each "I will" to done or dropped | Indirect | global `AGENTS.md` |
| 8 | Walton, schemes and critical questions | Run the practical-reasoning questions on every recommendation, and the source questions on every cited source | Indirect | `panel`, `whatsnext`, `bulletproof` |
| 9 | Kant, reflective judgment for the fourth option | Name the category the offered options share and the purpose it serves; propose one option outside it | Indirect | `panel`, `wdyt` |
| 10 | Stalnaker, common ground | Mark what is assumed for this task apart from what is believed | Indirect | `handoff` |
| 11 | Evans, ubiquitous language and bounded contexts | State the context a definition holds in; translate at the boundary | Untested | `drill` (one clause) |
| 12 | Duhem–Quine | Before blaming the hypothesis for a failed check, check the auxiliary assumptions | Indirect | nowhere new |
| 13 | Bratman, intentions as plans | A decision is reopened only on a named trigger | Untested | nowhere new |
| 14 | Walton & Krabbe, dialogue types | Concessions made while exploring do not bind | Untested | nowhere new |
| 15 | Pragma-dialectical rules | — | Untested | nowhere new |

Items 2, 13 and 14 were added beyond the requested list (Cohen and Levesque, Bratman, Walton and
Krabbe). Items 1 and 5 were widened: Lewis absorbs Stalnaker, and Brandom gains Doyle's truth
maintenance.

## 2. The five labels, remapped

The report's labels (§3 "Speech acts") mix two distinctions. Zave and Jackson separate them.

| Report label | Mood (Zave & Jackson §3.2) | Control (§4) | What it must carry |
| --- | --- | --- | --- |
| Observation | Indicative: true of the world now | — | The source that was checked. Zave & Jackson's completion criterion 2: each fact "validated … as true of the environment" (§6.3) |
| Hypothesis | Indicative, not yet checked | — | The check that would confirm or refute it |
| *Assumption* (missing) | Indicative, accepted for this task without checking | — | Why it is accepted and when it must be checked. Stalnaker: to accept is "to treat it as true for some reason" (2002, p. 716) |
| Decision | Optative: what must become true | Chosen by whoever owns that outcome | Who decided, and the trigger that reopens it |
| Instruction | Optative, about the agent's own actions | Actions the agent controls | Its addressee; an order binds only the one it targets (Brandom, via Shapiro) |
| Authority | Not a mood | Which actions the agent controls, and which only the user can take | Who granted it, in what words, and how far it reaches (Lewis; Austin) |

Two changes follow.

1. **Add Assumption.** The report has no place for "assume staging mirrors production for this
   analysis". It is not a hypothesis, because no one will test it now. It is not an observation,
   because no one checked it. Hidden assumptions of this kind are what Zave and Jackson call invalid
   indicative statements: the specification "might be compromised by … invalid indicative statements"
   (§3.2).
2. **Split Decision into requirement and change.** A requirement says what must hold in the world ("a
   retry after a lost response must not create a second asset"). The change says what the code does.
   The gap between them is closed only by world facts (§5). The report's "smallest set of explicit
   commitments" (§1) is then exactly: the requirements, plus the facts the change relies on.

## 3. The items

### Rank 1. Lewis, "Scorekeeping in a Language Game" (1979), with Stalnaker's presupposition

**Source.** David Lewis, "Scorekeeping in a Language Game," *Journal of Philosophical Logic* 8 (1979),
339–359. Read in full (OCR of the scan):
https://andrewmbailey.com/dkl/Scorekeeping_in_a_Language_Game.pdf

- Example 1, presupposition (pp. 339–340). The rule of accommodation: if something said requires a
  presupposition that is missing, "presupposition P comes into existence," unless someone objects.
- Example 2, permissibility (pp. 340–341). The master shifts the boundary of permitted conduct by
  speaking. A vague grant ("some of such-and-such are permissible") opens the options "closest to
  permissibility beforehand, perhaps."
- General scheme (p. 347). The rule holds only "provided that what is said is said by the master to the
  slave."
- Example 5, standards of precision (pp. 351–353), and Example 6, relative modality (pp. 354–355).
  Considered possibilities shift outward easily and inward reluctantly.
- Example 8, planning (pp. 356–357). The plan is a separate component of score from what is presupposed.

**Idea.** Whatever an utterance needs in order to make sense gets added to the shared record unless
someone objects, and permission moves only when the one with authority speaks.

**Moves.**

1. Before acting on a request, list what it takes for granted: every "the X" (that X exists and is
   unique), every "fix", "again", or "still" (that the defect or prior state exists), every "only"
   or "even". Check each against the repository. Report each one that fails as an objection before
   working, instead of building on it.
2. Treat a change in what the agent may do as valid only when the user says it in chat. When a grant
   is vague ("clean up the tests"), read it as the smallest widening that makes the user's words true.
   State that reading in one line and proceed.
3. Keep the plan and the facts as separate lists in any shared record. A plan step can assume
   something the facts contradict ("we plan X while knowing it may be impossible"). Merging them makes
   facts appear and vanish (Lewis's point on p. 357).
4. In reviews, record the standard of proof in force. A reviewer who raises a far-fetched possibility
   moves the bar for every later finding; lowering it back needs an explicit statement.

**Evidence.**

- Move 1, **Indirect.** Li et al., "Refining Critical Thinking in LLM Code Generation: A Faulty
  Premise-based Evaluation Framework" (FPBench, arXiv 2508.03622, Aug 2025;
  https://arxiv.org/abs/2508.03622). Across 15 models, code generators reason poorly under faulty
  premises and "depend heavily on explicit prompts to detect errors." That suggests an explicit
  premise-check step is needed. Abstract only; no numbers given.
- Move 1, **Indirect.** Shaikh et al., "Grounding Gaps in Language Model Generations" (NAACL 2024;
  https://arxiv.org/abs/2311.09144): models generate fewer grounding acts than humans and "presume
  common ground"; preference training reduces grounding acts further.
- Move 1, **Indirect.** Shaikh et al., "Navigating Rifts in Human-LLM Grounding" (ACL 2025;
  https://arxiv.org/abs/2503.13975): models initiate clarification about a third as often as humans,
  follow-ups about a sixteenth as often, and "early grounding failures predict later interaction
  breakdowns."
- Move 2, **Untested.** The earlier notes cite instruction-hierarchy work for "only the user
  authorizes"; nothing tests the smallest-widening reading.
- Moves 3 and 4, **Untested.**

**Overlap.** The canon's AbstentionBench entry (14c) covers false premises in questions, not in
directives. Earlier move 15 covers tool-output text as data; it does not cover vague grants.

**Lands.** Move 1 is a new first step in `settle`. Move 2 is one sentence in the global `AGENTS.md`
Authority section. Move 4 is one line in `revolver`, if José reopens it; he ruled it untouchable, so
otherwise nowhere.

**Stalnaker adds little beyond this.** "Common Ground," *Linguistics and Philosophy* 25 (2002),
701–721, read in full: https://semantics.uchicago.edu/kennedy/classes/f07/pragmatics/stalnaker02.pdf.
He contributes two things the report lacks. Acceptance differs from belief: "To accept a proposition is
to treat it as true for some reason" (p. 716). That is the missing Assumption label (Section 2). A
context is "defective" when parties presuppose different things, and "a defective context may go
unnoticed" (p. 717). That is already the report's "Understood" example (§2). Stalnaker's 1973 and 1974
papers were not read; SEP "Presupposition" (https://plato.stanford.edu/entries/presupposition/) was
read for his place in the literature.

### Rank 2. Cohen and Levesque, joint commitment (added)

**Source.** Philip R. Cohen and Hector J. Levesque, "Teamwork," *Noûs* 25(4), 1991. **Primary text
unread.** The definition was read in Milind Tambe, "Towards Flexible Teamwork," *JAIR* 1997, §4,
https://arxiv.org/pdf/cs/9709101.

A joint persistent goal holds while every member keeps the goal "until p is mutually known to be
achieved, unachievable or irrelevant." A member who privately finds the goal "achieved, unachievable or
irrelevant" is "left with a commitment to have this belief become mutual belief." The goal carries an
irrelevance clause: a condition that makes it moot.

**Idea.** A teammate may stop only by telling the team why: done, impossible, or no longer needed.

**Moves.**

1. Every delegation brief states the condition under which its goal becomes moot. Example: "if the
   duplicate does not reproduce on main, stop and report that."
2. A delegate that concludes its goal is achieved, impossible, or moot reports which, with the
   evidence. It does not stop silently, pivot to a neighbouring goal, or report a partial result as
   complete.
3. The coordinator treats a delegate's silence or drift as an open status, not as completion.

**Evidence.**

- **Indirect.** Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (MAST, arXiv 2503.13657, v3 Oct
  2025; https://arxiv.org/html/2503.13657v3). Across 1,642 traces, prevalence was 12.4% for failing to
  recognize when to stop, 7.4% for drifting from the goal, 6.2% for ending before objectives are met,
  and 6.8% for proceeding on assumptions instead of asking.
- **Indirect.** Smyth et al., "Quantifying Overclaiming Propensity in Frontier LLM Agents" (arXiv
  2609.20812, Sep 2026; https://arxiv.org/abs/2609.20812). Agents failed to read every assigned file
  in 67.9% of runs; 80.4% of those incomplete runs were misleading. Requiring subagents raised coverage,
  but most reviews that stayed incomplete were still misleading.
- Remedy: **Untested** for LLMs. Tambe's 1997 system applies the theory to non-LLM agent
  teams; its evaluation was not read.

**Overlap.** `onward` says "if one item blocks, record why". `handoff` has "objective and stop
condition". Neither names the moot condition, or the duty to report achieved, impossible, or moot.
`AGENTS.md` "Report failed, skipped, or partial verification first" covers part of move 2.

**Lands.** `handoff`: add "the condition that makes the objective moot". `onward`: "If the goal turns
out done, impossible, or moot, say which with evidence, then stop."

### Rank 3. Wittgenstein on rule-following

**Source.** Wittgenstein, *Philosophical Investigations*, trans. Anscombe, 3rd ed.; §§185, 201, 202
read in this PDF: https://static1.squarespace.com/static/54889e73e4b0a2c1f9891289/t/564b61a4e4b04eca59c4d232/1447780772744/Ludwig.Wittgenstein.-.Philosophical.Investigations.pdf

- §185: the pupil is tested "up to 1000," then continues "+2" as "1000, 1004, 1008, 1012," and says
  "But I went on in the same way."
- §201: "no course of action could be determined by a rule, because every course of action can be
  made out to accord with the rule."
- §202: "to think one is obeying a rule is not to obey a rule."

**Idea.** Examples and tests fix a rule only inside the range they cover. Whether a rule was followed
shows in what was done, not in the follower's belief.

**Moves.**

1. Check compliance against artifacts: the files actually opened, the commands actually run, the diff,
   the test output. Never accept the agent's statement that it followed the skill or covered the scope.
   For coverage claims, compare the list of items assigned with the record of items read.
2. Pair every worked example in a skill with a near miss: a case that looks the same but must be
   handled differently. Name the feature that separates them.
3. Probe a new rule with one case outside the range of its examples before relying on it.

**Evidence.**

- Move 1, **Backed.** Advani, "From Confident Closing to Silent Failure" (FAGEN@ICML 2026, arXiv
  2606.09863; https://arxiv.org/abs/2606.09863). False success is 75.8% of failures in AppWorld
  coding-agent trajectories with explicit status claims. LLM judges stay at or below AUROC 0.65 because
  they react to "confident closing language." Lightweight TF-IDF detectors reach 0.83–0.95 (task-disjoint AUROC).
  Smyth 2026 (rank 2) gives the coverage version.
- Move 2, **Indirect.** Tang et al., "Large Language Models Can be Lazy Learners" (Findings of ACL
  2023; https://arxiv.org/abs/2305.17256): models exploit shortcuts in prompt examples, and larger
  models more so. Chia et al., "Contrastive Chain-of-Thought Prompting" (arXiv 2311.09277, preprint;
  https://arxiv.org/abs/2311.09277): valid plus invalid demonstrations improve reasoning; abstract gives
  no numbers.
- Move 3, **Untested.**

**Overlap and correction.** The canon (§18) cites §§198–202 only as "no rule fixes its own application."
Its Kant entry (14a) proposes "any skill that requires judgment carries one worked example." §185 and
Tang argue that a single example invites copying its surface. Amend that rule to "one example and one
near miss." `AGENTS.md` already says "A green check counts only once you have confirmed it observed the
thing it names"; move 1 extends that from checks to the agent's own claims.

**Lands.** Move 1: `bulletproof`, in the evidence column for completion claims, and `revolver`, so a
reviewer's coverage claim is checked against its read log. Move 2: the skills README authoring rules
and `debloat` step 3. Move 3: nowhere yet.

### Rank 4. Zave and Jackson, "Four Dark Corners of Requirements Engineering" (1997)

**Source.** Pamela Zave and Michael Jackson, *ACM TOSEM* 6(1), 1997, 1–30. Read in full:
http://www.pamelazave.com/4dc.pdf

- §1: the four conclusions.
- §2: designations; "the only way to establish the meaning of a primitive term is to provide an
  informal explanation of it."
- §3.2: statements in the indicative mood "describe the environment as it is"; statements in the
  optative mood describe it "as we would like it to be".
- §4: actions are environment-controlled, machine-controlled, or shared.
- §5: "S, K ⊢ R".
- §6.3: five completion criteria.

**Idea.** A requirement is a wish about the world. The change can deliver it only through facts about
the world it does not control, and those facts must be written down and checked.

**Moves.**

1. In a plan or brief, sort each statement into one of three kinds: what is true of the world now
   (with its source); what must become true (the requirement); and what the change itself will do.
2. For each requirement that constrains something the code does not control, list the world facts the
   change relies on. Examples: "the client retries with the same request", "the storage layer is
   atomic per key". Check each one.
3. Before calling the work done, show for each requirement that the change, together with the listed
   checked facts, produces it. Name any requirement that rests on an unchecked fact.
4. Give each primitive term a recognition rule: how you would tell, in the running system, that a
   thing is one. Example: "a retry is a request carrying an operation id already seen".

**Evidence.** **Untested** as an agent instruction. **Indirect:** Yang et al. (report footnote 1) find
that unstated requirements regress on model change, and FPBench (rank 1) finds that wrong world facts
degrade code. Neither tests the three-way sort.

**Overlap.** `drill` asks for "the obligation… what must stay true; how each is verified." That is the
requirement and its check. It does not ask for the world facts the obligation depends on. The canon's
Frege entry covers one name per referent, not recognition rules.

**Lands.** `drill`, Obligation bullet: "List the world facts the obligation depends on and check each."
The label mapping in Section 2 goes to the global `AGENTS.md` Evidence section, if José adopts labels
at all.

### Rank 5. Brandom's deontic scorekeeping, with Doyle's truth maintenance

**Sources.**

- Robert Brandom, "Asserting," *Noûs* 17(4), 1983, 637–650. Read in full:
  https://sites.pitt.edu/~rbrandom/Courses/2022%20Phil%20of%20Language/Reasons%20texts/Asserting.pdf
  - Assertion as "an inference license" (p. 639).
  - "Endorsement is empty unless the commitment can be defended" (p. 641).
  - Assertions are "treated as in order… until challenged" (p. 642).
  - Deferral: B may re-assert A's claim, and "further challenges are appropriately addressed to A."
    If A fails a challenge, others "must take responsibility for their own assertings" of what followed
    (p. 642).
- *Making It Explicit* (1994). **Unread.** Read through Lionel Shapiro, "Commitment Accounts of
  Assertion," in Goldberg (ed.), *Oxford Handbook of Assertion*:
  https://shapiro.philosophy.uconn.edu/wp-content/uploads/sites/541/2018/10/Assertion.pdf
  - An appropriate challenge is "an incompatible assertion with an equal, prima facie claim to
    entitlement" (MIE 238).
  - Assertions differ from orders: an order's obligation is agent-relative (MIE 238–43).
- Jon Doyle, "A Truth Maintenance System," MIT AIM-521 (1979); *Artificial Intelligence* 12 (1979).
  Abstract read: https://dspace.mit.edu/handle/1721.1/5733. The system records the reasons for each
  belief and revises dependent beliefs when an assumption is withdrawn.

**Idea.** Commitment (what you have taken on) and entitlement (what you can defend) are tracked
separately, per speaker. A claim that loses its defense stops licensing what was built on it.

**Is it a model for an agreement register?** Yes, and a better one than a transcript summary. Each
entry needs three fields the report's register lacks:

- its source (who asserted or decided it, or which command showed it);
- the entries it rests on;
- its standing (unchallenged, defended, or defeated).

Doyle's system is the 1979 engineering of exactly this. TRACE (Chang & Chang, arXiv 2607.12480,
Jul 2026; https://arxiv.org/abs/2607.12480) proposes a typed commitment record for agents but reports
"not a performance claim."

**Moves.**

1. Every entry in a shared record or handoff names its source: the user's message, a file and line, or
   a command and its output.
2. When an entry is retracted or refuted, mark every entry that rests on it as unsupported until
   re-checked.
3. Retract a supported claim only when the challenge brings a contrary claim with its own evidence. A
   bare "are you sure?" triggers a re-check of the evidence, then either a retraction with the new
   evidence or a restatement with the old.
4. An instruction binds only the agent it addresses. When relaying work, re-issue the instructions
   that should bind the new agent; observations transfer as they stand.

**Evidence.**

- Move 3, **Indirect.** Laban et al., "Are You Sure? Challenging LLMs Leads to Performance Drops in The
  FlipFlop Experiment" (arXiv 2311.08596, 2023; https://arxiv.org/abs/2311.08596). Across ten models,
  a bare challenge flipped answers about 46% of the time and cut accuracy by 17% on average.
- Moves 1, 2 and 4, **Untested.**

**Overlap.** The canon's pragma-dialectics entry (rule 9, closure) covers retraction after a failed
defense. It does not cover provenance or propagation. `bulletproof` returns per-claim status but no
dependency.

**Lands.** `handoff`: "each settled item names its source." `revolver`, step 3: rejected findings are
already resolved against evidence; add move 2 for fixes that rested on a rejected finding. Move 3 goes
in the global `AGENTS.md` Evidence section; it is the sycophancy rule, made procedural.

### Rank 6. Naur, "Programming as Theory Building" (1985)

**Source.** Peter Naur, *Microprocessing and Microprogramming* 15 (1985), 253–261. Full text:
https://gist.github.com/chrisjrn/4d2cebdd7dbea7fa41ae6c94e046f752

- §2: group B extended a compiler with full documentation and advice, yet made patches that ignored its
  structure; group A saw it at once.
- §3: Ryle's notion of theory.
- §4: the theory shows in three abilities: explaining how each part maps to the world; justifying the
  design; responding to a modification by seeing its "similarity … with the operational facilities
  already built into the program."
- §6: revival "merely from the documentation" is "strictly impossible"; the theory passes by working
  "in close contact" with those who hold it.

**Idea.** A program's real design lives in its builders' ability to explain, justify, and extend it.
Documents carry traces of that ability, not the ability.

**What a handoff can transmit:** state, decisions, the reasons for them, rejected alternatives, traps,
and pointers. **What it cannot:** the ability to see which existing facility a new demand resembles.
That has to be rebuilt by doing, or borrowed by asking the agent or person who holds it while they are
still reachable.

**Moves.**

1. A brief carries each settled decision with its reason and the alternatives rejected, not only the
   resulting state.
2. A brief names the most likely next modification and where in the existing structure it belongs.
3. Before editing inherited work, the receiving agent states where a stated modification would go and
   why, then checks that against the code. If it cannot, it reads further or asks the originating lane
   before editing.
4. When the originating context is gone and the agent cannot answer move 3, treat the inherited change
   as a draft to rebuild, not a base to patch. `stepback` already says this for its own case.

**Evidence.**

- **Indirect.** Gloaguen et al., "Evaluating AGENTS.md" (arXiv 2602.11988, v3 Sep 2026;
  https://arxiv.org/abs/2602.11988). Context files did not generally raise task success and cost over
  20% more. Agents followed the instructions in them, but repository overviews "were not helpful."
  Descriptions of state do not transmit the theory; explicit instructions do transfer.
- **Indirect, practitioner, no measurement.** Walden Yan (Cognition), "Don't Build Multi-Agents,"
  12 June 2025 (https://cognition.com/blog/dont-build-multi-agents): "Actions carry implicit
  decisions, and conflicting decisions carry bad results." Anthropic, "How we built our multi-agent
  research system," 13 June 2025
  (https://www.anthropic.com/engineering/multi-agent-research-system): vague subagent tasks caused
  duplicated work; each subagent "needs an objective, an output format, guidance on the tools and
  sources to use, and clear task boundaries."
- Move 3, **Untested.** It is the report's own self-explanation idea (Chi 1994) applied to the agent.

**Overlap.** `handoff` lists "open decisions" and "traps found", not settled decisions with their
reasons. The report's "fresh perspective should remove endorsement, not erase the common ground" (§2)
is the same insight; Naur adds what the common ground must contain.

**Lands.** `handoff`: "settled decisions with their reason and rejected alternatives; the likely next
change and where it belongs." `rearm`: move 3 before continuing.

### Rank 7. Austin's felicity conditions, applied to authorization

**Source.** J. L. Austin, *How to Do Things with Words*, 2nd ed. (Urmson & Sbisà), Lectures II–III.
Read pp. 14–17 and 32–36: https://communicationconcepts15.wordpress.com/wp-content/uploads/2015/06/austin_howtodothingswithwords.pdf

- pp. 14–15, six conditions:
  - A.1: an accepted procedure "by certain persons in certain circumstances";
  - A.2: the persons and circumstances "must be appropriate";
  - B.1 and B.2: executed "correctly" and "completely";
  - Γ.1 and Γ.2: the right intentions, and the participants "must actually so conduct themselves
    subsequently".
- pp. 16–17: a breach of A or B is a misfire, and the act is "void or without effect". A breach of Γ is
  an abuse, and the act happens but is hollow.
- p. 34: misapplications include "I appoint you" said "when I am not entitled to appoint."
- pp. 32–33: a bare "go" leaves it "uncertain… whether the utterer is ordering… or merely advising."
  In law, an inexplicit performative is treated as an incorrect or incomplete performance.

**Idea.** An authorization either takes effect or is void, and whether it does depends on who issued
it, how completely, and how explicitly.

**Moves.**

1. Treat a grant as void unless the user issued it in chat (A.2), it names the action and its target
   (B.2), and it is explicit. "Looks good", "we could deploy", and approval of a plan that mentions a
   push are not grants for the push.
2. When a would-be grant is void, ask one closed question naming the exact action, then continue with
   other work.
3. Track every commitment the agent states ("I will run the migration check") to done or explicitly
   dropped in the final report. This is Γ.2.

**Evidence.** **Indirect.** Ruan et al., ToolEmu (arXiv 2309.15817, 2023–24;
https://arxiv.org/abs/2309.15817): even the safest agent showed risky-action failures 23.9% of the
time. The instruction-hierarchy work in the earlier notes trains source privilege but does not test the
explicitness rule. Move 3, **Indirect**: MAST's 13.2% "actions contradict the agent's reasoning."

**Overlap.** Earlier moves 13 and 15 ("only the user in chat authorizes") cover A.2. Move 1's
explicitness and completeness clauses and move 3 are new. `AGENTS.md` Destructive actions requires a
yes "after printing the exact command"; that is B.2 for one class of actions.

**Lands.** Global `AGENTS.md` Authority: one sentence for move 1. `sitrep`: add move 3 to "Missing".

### Rank 8. Walton's argumentation schemes and critical questions

**Source.** Douglas Walton, "Argumentation Schemes and their Application in Argument Mining," ch. 11
in a University of Windsor *WSIA* open-access volume (volume title not checked). It reproduces the
schemes and questions from Walton, Reed & Macagno, *Argumentation Schemes* (CUP 2008), p. 323. The
book itself is unread. Chapter read:
https://windsor.scholarsportal.info/omp/index.php/wsia/catalog/download/106/106/1086?inline=1

- Practical inference: goal G; action A is a means to G; so do A. Its five critical questions:
  1. conflicting goals;
  2. alternative actions;
  3. which is most efficient;
  4. whether A is practically possible;
  5. which consequences of A must also be taken into account, the "side effects question".
- Position to know (also in the chapter): is the source in a position to know; is it honest and
  reliable; did it actually assert the claim.
- The chapter notes that merely asking the side-effects question can be enough to cast a
  practical-reasoning argument into doubt.

**Idea.** Each common type of argument comes with its own short list of the questions that can defeat
it. A reviewer checks the list instead of judging the argument's shape.

**Why it beats Toulmin as a check.** Toulmin asks for a warrant but not which warrant is missing.
A scheme fixes the list in advance, so a reviewer can mark each question answered or open.

**Moves.**

1. For any recommendation of the form "do A to get G," answer five questions before giving it: what
   other goal conflicts with G; what other action achieves G; why A over those; what shows A is
   feasible here; and what else A changes.
2. For any claim taken from a source (documentation, another agent, a forum), answer three questions:
   is this source in a position to know this, in this version; has it been reliable before; and does it
   actually say this, quoted.

**Evidence.** **Indirect.** Calvo Figueras et al., "Overview of the Critical Questions Generation Shared
Task" (ArgMining 2025; https://aclanthology.org/2025.argmining-1.23/): the best system reached 67.6;
three of the top four teams used scheme annotations. The canon's CQoT result (+4%, confounded) is the
nearest test of answering such questions.

**Overlap.** `wdyt` already divides options exhaustively and answers objections; that covers questions
2 and 3. `panel` lacks the side-effects and conflicting-goal questions. `bulletproof` checks claims
against sources, not the source's position to know.

**Lands.** `panel` and `whatsnext`: move 1 as the comparison criteria. `bulletproof`: move 2 for cited
sources.

### Rank 9. Kant's reflective judgment and the §40 maxims, applied to the "fourth option"

**Source.** Kant, *Critique of Judgement*, trans. J. H. Bernard. Read the Introduction §IV and §40:
https://www.gutenberg.org/cache/epub/48433/pg48433.txt (HTML edition opened at
https://www.gutenberg.org/files/48433/48433-h/48433-h.htm).

- Introduction IV: if the universal is given, judgment is determinant; "if only the particular be
  given for which the universal has to be found, the Judgement is merely reflective."
- §40: sensus communis works "by comparing our judgement with the possible rather than the actual
  judgements of others," and "by abstracting from the limitations which contingently attach to our own
  judgement."

**What the earlier notes already have.** Canon 14a covers determining vs reflective judgment, for
deciding whether a project rule applies (`settle`). 14c covers the shared premise of an antinomy
(`wdyt` step 5). 14d covers the three maxims (`wdyt` step 1, and standpoints in `panel`). None of that
is repeated here.

**What is new.** The report's fourth option (§6) is a reflective problem. The menu gives three
particulars (browser cache, edge cache, Redis), and the missing option comes from finding their
universal ("store a result so the work is not repeated") and then the purpose it serves ("the page is
slow because work repeats"). §40 adds the second half: compare with the options others *could* propose
from other positions, not with the options actually offered.

**Moves.**

1. When given a menu of options, name in one line the category all of them belong to, and the purpose
   that category serves.
2. Propose at least one option that serves the purpose but falls outside the category. Examples:
   remove the repeated work, or move it to another layer.
3. Name one party whose position the menu ignores (the owner of another layer, the user of the data),
   and give the option they would propose.

**Evidence.** **Indirect.** Zheng et al., "Take a Step Back" (ICLR 2024;
https://arxiv.org/abs/2310.06117): abstracting to higher-level principles first improved PaLM-2L by
7–27% on STEM, knowledge QA, and multi-hop tasks. That is question answering, not option
generation. Kostiuk 2025 and Doshi & Hauser 2024 (report footnotes 27–28) show the need.

**Overlap.** Knoblich's constraint relaxation (report §6) is the psychological version of §40's
"abstracting from the limitations." `stepback` already asks for "the goal it serves." Move 1 is
partly in the report; moves 2 and 3 are the increment.

**Lands.** `panel`: moves 1–2 before the comparison. `wdyt`, step 2: "include one option outside the
category the others share."

### Rank 10. Stalnaker, common ground

Folded into rank 1. Its one distinct contribution is the Assumption label in Section 2.
**Indirect** (Shaikh 2024, 2025). Lands in `handoff`: "mark assumptions accepted for this work
separately from checked facts."

### Rank 11. Evans, ubiquitous language and bounded contexts

**Source.** Eric Evans, *Domain-Driven Design Reference* (2015), "Bounded Context" and "Ubiquitous
Language" patterns. Read: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf

- "Model expressions, like any other phrase, only have meaning in context. Therefore: Explicitly define
  the context within which a model applies."
- "Recognize that a change in the language is a change to the model."

The 2003 book is unread.

**Idea.** A term's definition holds inside a named boundary; crossing the boundary needs a translation.

**Move.** When defining a term in a brief or skill, state the context it holds in ("lane, in the
Sourdaw delivery scripts"). When a term crosses contexts, write the translation instead of reusing the
word.

**Evidence.** **Untested.** No study of project-term definitions for coding agents was found.

**Overlap.** The report's `lane` example (§3, Meno) already separates essential from incidental
properties. The canon's Frege entry covers one name per referent; its Wittgenstein entry covers defining
by use. `drill` says "the name in the project's words." The only increment is the context clause.

**Lands.** `drill`, one clause: "the name in the project's words, and the context it holds in."
Otherwise nowhere.

### Rank 12. Duhem–Quine and the "shared premise" test

**Source.** SEP, "Underdetermination of Scientific Theory," §2:
https://plato.stanford.edu/entries/scientific-underdetermination/

- It quotes Duhem: "the physicist can never subject an isolated hypothesis to experimental test, but
  only a whole group of hypotheses." That is *The Aim and Structure of Physical Theory* (1914; trans.
  1954), p. 187.
- It cites Quine, "Two Dogmas of Empiricism" (1951), §6, on revising "elsewhere in the web."

Neither primary text was opened.

**Idea.** A failed check refutes the conjunction of the hypothesis and everything assumed to run the
check, not the hypothesis alone.

**Move.** Before revising a hypothesis because a check failed, list what the check assumed: right
build, right environment, a test that reaches the changed path, valid fixtures. Check the cheapest of
these first.

**Evidence.** **Indirect.** Wang, Pradel & Liu, "Are 'Solved Issues' in SWE-bench Really Solved
Correctly?" (arXiv 2503.15223; https://arxiv.org/abs/2503.15223): 29.6% of plausible patches behave
differently from the reference, inflating results by 6.2 points. That is the passing-check case.

**Why it adds little.** The report's "shared premise" test (§6) is about option menus, which canon 14c
(the antinomies) already covers. The verification use is already in `AGENTS.md` ("A green check counts
only once you have confirmed it observed the thing it names"). The canon's Popper and Kuhn entries
cover protecting a hypothesis with ad hoc fixes. The failing-check direction is one line for
`investigate-first`, which is not in José's listed skills. **Lands nowhere new.**

### Rank 13. Bratman, intentions as plans (added)

**Source.** SEP, "Intention," §4: https://plato.stanford.edu/entries/intention/. Intentions are
"conduct-controlling pro-attitudes, ones which we are disposed to retain without reconsideration,"
partial, and bound by consistency and means-end coherence. Bratman's 1987 book is unread. The "filter
of admissibility" is not in the SEP entry, so it is not cited here.

**Move.** Record each decision with the observation that would reopen it. Reject later options that
contradict it unless that observation has occurred.

**Evidence.** **Untested.**

**Why it adds little.** The canon's legal entry (stare decisis: "depart only by distinguishing… or by
overruling explicitly") and `wdyt`'s "observation that would reverse the verdict" already cover it.
**Nowhere new.**

### Rank 14. Walton and Krabbe, dialogue types and retraction (added)

**Source.** *Commitment in Dialogue* (SUNY Press, 1995). Only the publisher's description and contents
were read: https://sunypress.edu/Books/C/Commitment-in-Dialogue. They list ch. 3.3 "Dialectical Shifts"
and 3.4 "Illicit Shifts and Fallacies", ch. 4.1 "Dark-Side Commitment", and §§1.1–1.2 on action vs
propositional commitment. **Book unread.**

**Idea.** Commitments incurred in one kind of dialogue (exploring) need not carry into another
(deciding), and illicit shifts between kinds produce fallacies.

**Why it adds little.** The report's rhythm "explore freely, commit explicitly, verify the
consequences" (§1) says this. **Nowhere new** until the book is read.

### Rank 15. Pragma-dialectical rules for critical discussion

**Source.** Covered by canon §24 (ten rules, four stages). The opening stage was checked in Burato,
Cristani & Viganò, "Meaning Negotiation as Inference" (arXiv 1101.4356, 2011;
https://arxiv.org/pdf/1101.4356), which summarizes van Eemeren & Grootendorst. In the opening stage the
parties "agree upon the rules of the discussion and establish which propositions they can use."
The primary books are unread.

**Why it adds nothing.** The opening stage is the agreement register under another name. The canon
already has rule 6, the starting-point rule: do not present a premise as agreed when it is not.
Brandom and Lewis give the mechanics the rules lack. **Nowhere new.**

## 4. What adds nothing, stated plainly

- **Pragma-dialectical rules.** Already in canon §24 with `revolver` lines. The opening stage
  duplicates the agreement register.
- **Duhem–Quine.** The option-menu use is canon 14c (antinomies). The verification use is the
  `AGENTS.md` green-check rule.
- **Kant's determinative vs reflective judgment, as a distinction.** Canon 14a. Only its application
  to option menus (rank 9) is new.
- **Kant's §40 maxims, as maxims.** Canon 14d, already in `wdyt` step 1. Only "possible rather than
  actual judgements" is new.
- **Wittgenstein on meaning as use and on silence.** Canon §18. Only §185 (examples underdetermine)
  and §202 (claimed compliance) are new.
- **Evans.** All but one clause duplicates the report's definitions section, the Frege entry, and
  `drill`.
- **Bratman, and Walton & Krabbe.** Covered by canon §25 (legal precedent), by `wdyt`, and by the
  report's §1 rhythm.

## 5. Proposed edits, collected

These are proposals. Nothing in `~/.agents` was changed.

| Target | Line to add |
| --- | --- |
| `settle`, new step 0 | List what the request takes for granted: each "the X", "fix", "again", "only". Check each in the repository; raise a false one as an objection before working. |
| `handoff`, Include list | The condition that makes the objective moot. Settled decisions, each with its reason, the rejected alternatives, and its source. The likely next change and where it belongs. Assumptions accepted without checking, marked as such. |
| `onward` | If the goal turns out done, impossible, or moot, say which with the evidence, then stop. |
| `rearm` | Before editing inherited work, state where one likely change would go and why, and check it against the code. |
| `drill`, Obligation | List the world facts the obligation depends on and check each; name the context the change's terms hold in. |
| `bulletproof` | Judge a completion or coverage claim from artifacts (files opened, commands run), never from the claim. For a cited source, ask whether it is in a position to know this, in this version, and quote it. |
| `panel` | Before comparing, name the category the options share and the purpose it serves, and add one option outside it. Compare on conflicting goals, alternatives, feasibility here, and side effects. |
| `whatsnext` | For the recommended step, name what else it changes. |
| `sitrep` | Each "I will" from earlier reports: done, or dropped and why. |
| Skills README | Each worked example comes with a near miss and the feature that separates them. |
| Global `AGENTS.md`, Authority | A permission counts only when the user states it in chat, explicitly, naming the action and target; read a vague grant as the smallest widening its words require, and state that reading. |
| Global `AGENTS.md`, Evidence | Retract a supported claim only for contrary evidence; a bare challenge triggers a re-check. |

## 6. Verification gaps

- **Primary texts unread:**
  - Cohen & Levesque 1991 (read via Tambe 1997);
  - Brandom, *Making It Explicit* (read via Shapiro);
  - Walton, Reed & Macagno 2008 (read via Walton's chapter);
  - Walton & Krabbe 1995 (contents page only);
  - Bratman 1987 (read via SEP);
  - Duhem 1914 and Quine 1951 (read via SEP);
  - van Eemeren & Grootendorst (read via Burato et al.);
  - Evans 2003 (read via the 2015 Reference);
  - Stalnaker 1973 and 1974.
- **Read in full or in the cited sections:** Lewis 1979 (from an OCR of the scan; quotes checked against
  the OCR text), Stalnaker 2002, Brandom 1983, Austin pp. 14–17 and 32–36, Zave & Jackson 1997,
  Naur 1985, Kant (Introduction IV and §40), Wittgenstein §§185 and 201–202, and Walton's chapter.
- **LLM studies read as abstracts only:** FPBench, Grounding Gaps, Rifts, MAST (the failure-mode
  table was read in the HTML), Overclaiming, False Success, FlipFlop, Step-Back, Tang, Chia,
  Gloaguen, Wang/Pradel, ToolEmu, CQs-Gen, TRACE. Several are 2026 preprints.
- **Not verified:** the title of the Windsor volume containing Walton's chapter.
- **Not tested:** every move above. None has been run on José's skills. The report's §8 protocol and
  the canon's named-method A/B test apply unchanged.
