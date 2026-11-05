# The philosophy canon as a source of agent-skill methods

Research note for the skills redesign (`wdyt`, `bulletproof`, `settle`, `panel`, `revolver`, `drill`,
`dissect`, `tldr`). Written 2026-11-05. Nothing in any repository was changed.

**Bottom line.** The tradition is useful when we lift the procedure inside a method and leave the name
behind. The moves most likely to change a frontier model's behavior are the ones that put something
external between the model and its own conclusion:

- an observation instead of an argument (Hume's fork, Leibniz's *calculemus*);
- independent judgments counted before anyone discusses them (Kahneman's noise hygiene);
- a refutation condition written before the test (Popper);
- a stated standard of proof and a duty to stay silent when it is not met (legal burden of proof,
  Wittgenstein);
- the asker's preference removed before judging (Stoic assent, Kant's first maxim).

Four of these have direct LLM evidence. Kant contributes moves that no LLM study has tested and no
other source supplies. The strongest is the antinomy check: when both sides of a question look
provable, test the premise they share. Others are the scope, condition, and modality form of every
claim, and the rule that completeness is a goal you search toward, never a finding you report. The
recommended `wdyt` (Part 3) uses the disputatio skeleton (objections before the verdict, a reply to
every objection) with those grafts, and keeps every name out of the instructions.

## How to read this

**Scope.** These are excluded because a sibling note covers them: Plato's *Meno*, Peirce 1878, Grice,
Searle, Hila 2026, Attempto Controlled English, Suri 2026, Zheng 2024, PRIG, "Detect Before You
Disambiguate", Sclar 2024, Buçinca 2021, Kostiuk 2025, Parnas 1972. Socratic material below avoids the
*Meno*, and nothing here relies on the excluded papers.

**Evidence labels** (LLM evidence only; human-subject evidence is reported separately):

- **Supports**: a dated LLM study found the move, or a close operationalization of it, improves the
  named failure.
- **Supports (indirect)**: an LLM study shows the failure exists, or that an adjacent move works.
- **Mixed**: studies point both ways, or the gain disappears against a fair baseline.
- **Contradicts**: an LLM study finds the move does not help, or hurts.
- **Untested**: no LLM study found.

**What was verified this session, and what was not.**

- Every arXiv paper cited was resolved by its ID on arxiv.org, and the title matched.
- The findings attributed to Jung 2022, Choi 2025, Castagna 2024, Wang 2024 (Devil's Advocate), Qiu
  2025, Kirichenko 2025, Huang 2025 (POPPER), Yu 2022, Abdali 2025, Weston 2023, Smit 2024, Eskandari
  2024, Schoenegger 2024, Hagendorff 2023, Khan 2024, Kalai 2025, Kim 2024, Wang 2024 (ACL), Basil
  2025, Hu 2024, Liang 2023, Hines 2024, Jin 2023, Huang 2023 (self-correction), Dasgupta 2022 and
  Halawi 2024 were read from abstracts or search summaries this session.
- Findings for other cited papers come from prior knowledge of their abstracts. They are marked
  "(abstract not re-read)".
- Every Stanford Encyclopedia of Philosophy (SEP) or Internet Encyclopedia of Philosophy (IEP) URL was
  fetched; each returned HTTP 200 and contains the method's key term.
- Primary-text locators use standard editions: Stephanus, Bekker, AT, Akademie, and section numbers.
  None was re-opened this session. Spot-check before quoting.
- Searches for LLM studies of premortem prompting and of steelman prompting found none in peer-reviewed
  venues.

---

## Part 1. The canon, method by method

Each entry gives the method, the agent failure it addresses, the LLM evidence, and skill lines. Skill
lines are imperative and checkable. Each names the skill it strengthens, or proposes a new one.

### 1. Pythagoreans: number, proportion, harmony as constraint

**Method.**

- Philolaus holds that whatever is known has number, since nothing can be grasped without it (fr. DK 44
  B4). Harmony (*harmonia*) is the fitting-together of unlike things under a ratio (B6).
- Archytas says rational calculation (*logismos*) ended civil strife, because people who can compute
  have no ground for quarrel (DK 47 B3). This is Leibniz's *calculemus* two thousand years early.
- Aristotle reports the school's view that the elements of number are the elements of things
  (*Metaphysics* A.5, 985b23–986b8).
- The late *Golden Verses* (lines 40–44) prescribe a review before sleep: what did I do wrong, what did
  I do, what did I leave undone.
- Operationally: turn claims into quantities, require the parts to compose (sums, ratios, units), and
  treat any misfit as the error signal.

Secondary: SEP "Pythagoreanism" (Huffman), https://plato.stanford.edu/entries/pythagoreanism/ ; SEP
"Philolaus", https://plato.stanford.edu/entries/philolaus/ ; SEP "Archytas",
https://plato.stanford.edu/entries/archytas/

**Failures addressed.** Unquantified comparatives ("faster", "most callers"). Numbers that do not add
up across a report. Effort out of proportion to stakes.

**LLM evidence.** Offloading arithmetic to code: **Supports** (Gao et al., PAL, arXiv 2211.10435,
2022; abstract not re-read). Composition checks as a prompt: **Untested**.

**Skill lines.**

- "Put a number on every comparative claim: a count, ratio, or before/after. If you cannot, mark it
  unquantified." → `bulletproof`
- "Check that the parts compose: totals equal their components, units agree, and counts from two
  methods match. Report any misfit as a finding." → `bulletproof`
- "Make the length of each section proportional to how much it bears on the decision." → `tldr`

### 2. Socrates: elenchus and maieutics

**Method.**

- In the elenchus, Socrates takes the interlocutor's sincere thesis. He secures assent to further
  premises, then shows that those premises entail the thesis's negation, so something the interlocutor
  holds must go (*Euthyphro* 10a–11b; *Laches* 190e–199e). He needs only the interlocutor as witness
  (*Gorgias* 472b–c, 474a).
- In maieutics (*Theaetetus* 148e–151d, 210b–d), Socrates delivers others' ideas without asserting his
  own. He then tests whether each is viable or a "wind-egg" to be discarded.
- Vlastos reconstructs the standard elenchus as a consistency test, not a proof of falsity ("The
  Socratic Elenchus", *Oxford Studies in Ancient Philosophy* 1, 1983).

Secondary: SEP "Socrates" (Nails), https://plato.stanford.edu/entries/socrates/ ; SEP "Plato on
Knowledge in the *Theaetetus*", https://plato.stanford.edu/entries/plato-theaetetus/

**Failures addressed.** Unexamined premises. An answer inconsistent with the model's own supporting
claims. Accepting the first definition offered.

**LLM evidence.**

- **Supports.** Jung et al., "Maieutic Prompting", EMNLP 2022 (arXiv 2205.11822). The method generates
  a tree of abductive explanations for and against, then picks the most consistent truth assignment by
  MAX-SAT. It beat prompting baselines on true/false commonsense benchmarks.
- **Supports.** Qi et al., "The Art of SOCRATIC QUESTIONING", EMNLP 2023 (arXiv 2305.14999). The
  method recursively poses and answers sub-questions. It reports gains over chain-of-thought (tables not
  re-checked).
- **Supports, for evaluating reasoning.** He, Zhang & Roth, SocREval, arXiv 2310.00074 (2023; abstract
  not re-read).

**Skill lines.**

- "List the premises your leading answer needs. Derive one checkable consequence of each and check it
  against the code or source. A contradiction retires the answer." → `bulletproof`, `wdyt`
- "Explain why the answer is true and why it is false. Keep the side whose explanation survives checks
  of its own claims." → `wdyt`

### 3. Plato: diairesis (collection and division)

**Method.**

- Collection gathers scattered cases under one form, so the subject is fixed before it is discussed.
- Division splits a kind into sub-kinds along its natural joints, like a good butcher, until the target
  is located (*Phaedrus* 265d–266b). The *Sophist* runs the procedure on the angler (218d–221c). It
  names dividing by kinds as the dialectician's work (253d–e).
- The *Statesman* (262a–263b) adds the key constraint. Cut through the middle into parts of comparable
  standing. Never split off one small part and lump the rest, as "Greeks vs barbarians" does.

Secondary: IEP "Plato", https://iep.utm.edu/plato/ ; SEP "Definitions" (Gupta),
https://plato.stanford.edu/entries/definitions/

**Failures addressed.** False dichotomy ("X or everything else"). Missing options. Ad hoc taxonomies.

**LLM evidence.** Decomposition in general: **Supports** (Zhou et al., Least-to-Most, arXiv
2205.10625, 2022; Yao et al., Tree of Thoughts, arXiv 2305.10601, 2023; abstracts not re-read). The
exhaustive, single-criterion constraint: **Untested**.

**Skill lines.**

- "Before choosing, divide the options by one stated criterion into parts that are exhaustive and
  exclusive." → `wdyt`, `panel`
- "Reject a split of the form 'X vs everything else' until 'everything else' is itself divided."
  → `panel`

### 4. Aristotle, *Topics*: dialectic and the topoi

**Method.**

- Dialectic reasons from *endoxa*: what all people, most people, or the wise accept (I.1, 100a18–b23).
  One of its uses is the ability to raise difficulties on both sides, which shows where truth lies
  (I.2, 101a34–36).
- The topoi are argument-finding checkpoints organized by the four predicables: definition, property
  (belongs to all and only), genus, and accident (I.4–8; Books II–VII).
- A definition is attacked for being too wide, too narrow, or placed in the wrong genus (Book VI).
- Book VIII (163a36–b16) prescribes practice: argue for and against each thesis.

Secondary: SEP "Aristotle's Logic" (Smith), https://plato.stanford.edu/entries/aristotle-logic/

**Failures addressed.** Unstructured critique. Names and definitions that cover too much or too little.
One-sided reasoning.

**LLM evidence.** Critical-question checklists: **Supports**, with a caveat (see Toulmin, §22). Arguing
both sides: **Mixed**. Eskandari Miandoab & Sarathy (CustomNLP4U @ EMNLP 2024, arXiv 2410.12997) found
argument generation helped small models most. Large models gained under 1% over chain-of-thought,
partly because they write convincing arguments for wrong options.

**Skill lines.**

- "Test every proposed name or definition: give one case it must cover and does, and one it must
  exclude and does." → `drill`
- "For each thesis, write the best argument for and against before ruling." → `wdyt`

### 5. Aristotle, *Prior Analytics*: form, and the middle term

**Method.**

- A deduction is valid by its form. The figures and moods show which premise pairs yield a conclusion
  (I.4–7).
- I.27–30 gives a method for finding premises. List what follows the subject and what the predicate
  follows, then look for a shared middle term.
- An argument without a properly distributed middle proves nothing, however plausible its conclusion.

Secondary: SEP "Aristotle's Logic", https://plato.stanford.edu/entries/aristotle-logic/

**Failure addressed.** Invalid inferences accepted because the conclusion is believable.

**LLM evidence.**

- **Supports (indirect).** Dasgupta, Lampinen et al. (arXiv 2207.07051, 2022): language models, like
  humans, judge syllogisms more accurately when the content supports the logic. Validity is entangled
  with belief, which argues for abstracting the form.
- **Supports.** Pan et al., Logic-LM (arXiv 2305.12295, 2023): translating to a symbolic solver
  improves logical reasoning (abstract not re-read).

**Skill line.**

- "Write the decisive inference as premises and conclusion. Restate it with neutral letters and check
  that it still follows." → `bulletproof`

### 6. Aristotle, *Sophistical Refutations*: the fallacy catalogue

**Method.**

- Thirteen ways an argument only appears to refute. Six depend on language: equivocation, amphiboly,
  combination, division, accent, and form of expression (ch. 4, 165b23ff).
- Seven do not: accident, *secundum quid* (taking a qualified claim absolutely), *ignoratio elenchi*
  (missing the point), begging the question, consequent (affirming the consequent), false cause, and
  many questions (ch. 5).
- The catalogue is a checklist of where to look, not a theory of error.

Secondary: SEP "Fallacies" (Hansen), https://plato.stanford.edu/entries/fallacies/

**Failures addressed.**

- Equivocation.
- Answering an adjacent question.
- Circular verification ("tests pass because the test asserts the implementation").
- *Post hoc* debugging.
- Turning "works for X" into "works".

**LLM evidence.** **Supports (indirect).** Jin et al., "Logical Fallacy Detection" (arXiv 2202.13758,
2022): models were weak at classifying fallacies. That shows the need, not a remedy. A checklist in the
prompt: **Untested**.

**Skill line.**

- "Check the decisive argument for five faults: a word used in two senses, a conclusion that answers a
  different question, a premise that assumes the conclusion, a cause inferred from sequence alone, and a
  qualified result stated without its qualification." → `revolver`, `bulletproof`

### 7. Aristotle, *Rhetoric*: ethos, pathos, logos; the enthymeme

**Method.**

- Speech has three technical proofs: the speaker's character as shown in the speech (ethos), the
  disposition produced in the hearer (pathos), and the argument itself (logos) (I.2, 1356a1–20).
- The enthymeme is the rhetorical syllogism. It reasons from probabilities and signs, and often omits a
  premise the audience supplies (I.2, 1357a7–22; II.22).
- The omitted premise is where an argument hides its weakest step.

Secondary: SEP "Aristotle's Rhetoric" (Rapp), https://plato.stanford.edu/entries/aristotle-rhetoric/

**Failures addressed.** Credibility claimed by tone or persona instead of evidence. Persuading by
pleasing the user (pathos becomes sycophancy). Hidden premises.

**LLM evidence.**

- **Supports (indirect), on pathos.** Sharma et al. (arXiv 2310.13548, 2023): five assistants were
  consistently sycophantic, and human and preference-model raters sometimes preferred sycophantic
  answers (abstract not re-read).
- Salvi et al. ran a randomized trial (arXiv 2403.14380, 2024). GPT-4 given personal data about its
  opponent was more persuasive than humans (abstract not re-read). Models wield pathos effectively.
- Making enthymemes explicit: **Untested**.

**Skill lines.**

- "Write the unstated premise your conclusion needs, then check it." → `bulletproof`, `wdyt`
- "Back every claim with cited evidence. Cut wording aimed at the reader's feelings or identity."
  → `tldr`

### 8. Aristotle, *Nicomachean Ethics*: phronesis

**Method.**

- Practical wisdom is the excellence of deliberating well about particulars toward a good end (VI.5,
  1140a24–b30). It needs perception of particulars and experience: the young can be good at
  mathematics, but not yet prudent (VI.8, 1142a11–20).
- Good deliberation (*euboulia*) is correctness about what is useful, reached in the right way and at
  the right time (VI.9, 1142b).
- Seek only the precision the subject admits (I.3, 1094b11–27).

Secondary: SEP "Aristotle's Ethics" (Kraut), https://plato.stanford.edu/entries/aristotle-ethics/

**Failures addressed.** Rule-following without judgment. False precision. Deliberating past the point
of use.

**LLM evidence.** **Untested** directly. **Supports (indirect)** that examples carry judgment: Wang et
al. (ACL 2024, arXiv 2402.18272). Once a demonstration was in the prompt, a single agent matched
multi-agent discussion.

**Skill lines.**

- "State the precision this decision needs (order of magnitude, ranking, or exact value), and stop
  investigating when you have it." → `wdyt`, `tldr`
- "When a rule and the case disagree, name the particular fact and say whether the rule's purpose
  covers it." → `settle`

### 9. Stoics: propositional logic and the discipline of assent

**Method.**

- Chrysippus built a propositional logic on five indemonstrable argument forms, including *modus
  ponens*, *modus tollens*, and disjunctive syllogism (Diogenes Laertius VII.80–81; Sextus,
  *Against the Logicians* II.223–227).
- In Stoic epistemology an impression (*phantasia*) arrives, and assent is a separate act within our
  power. One should assent only to a cognitive impression, one that could not have come from what is
  not (DL VII.46, 50–54).
- Epictetus makes this a practice. Test impressions as a money-changer tests coins (*Discourses*
  1.20.7–11). Tell an impression to wait while you see what it is (2.18.24). What disturbs us is our
  judgment, not the thing (*Enchiridion* 5).

Secondary: SEP "Epictetus", https://plato.stanford.edu/entries/epictetus/ ; SEP "Stoicism",
https://plato.stanford.edu/entries/stoicism/ ; SEP "Ancient Logic",
https://plato.stanford.edu/entries/logic-ancient/

**Failures addressed.** Treating tool output, user assertions, or injected text as true or as commands.
Acting on first appearances. Assenting to the asker's framing.

**LLM evidence.**

- **Supports.** Weston & Sukhbaatar, "System 2 Attention" (arXiv 2311.11829, 2023). Having the model
  rewrite its context without opinions and irrelevancies before answering increased factuality and
  reduced sycophancy.
- **Supports.** Hines et al., "Spotlighting" (arXiv 2403.14720, 2024). Marking the provenance of input
  cut indirect prompt-injection success from over 50% to under 2% on GPT-family models.

**Skill lines.**

- "Label each input you rely on as observed, reported, inferred, or instructed. Accept only what you
  observed or can check, and suspend the rest by name." → `bulletproof`
- "Restate the question without the asker's opinion or preferred answer before judging it." → `wdyt`

### 10. Scholastic disputatio: Aquinas' article and Abelard's *Sic et Non*

**Method.**

- Aquinas' article in the *Summa Theologiae* has five parts:
  1. A yes/no question.
  2. Objections (*videtur quod*): usually several of the best arguments for the answer about to be
     rejected.
  3. *Sed contra*: an authority or reason on the other side.
  4. *Respondeo*: the master's determination, often by drawing a distinction.
  5. A reply to each objection, conceding what is true in it.

  The form forces every objection to be answered, and makes the objections come first.
- Abelard's *Sic et Non* (c. 1120s) sets conflicting authorities side by side on 158 questions. Its
  prologue gives rules for reconciling them:
  - suspect a corrupt or misattributed text;
  - ask whether the author retracted;
  - read for context and purpose;
  - look for different senses of the same word;
  - look for different times or circumstances;
  - prefer the stronger authority only when nothing else reconciles them.

  Abelard: "By doubting we come to inquiry; by inquiry we perceive the truth."

Secondary: SEP "Literary Forms of Medieval Philosophy", https://plato.stanford.edu/entries/medieval-literary/
; SEP "Peter Abelard" (King & Arlig), https://plato.stanford.edu/entries/abelard/

**Failures addressed.** Premature closure. Objections raised and then ignored. Sources in conflict
settled by recency or majority instead of examination.

**LLM evidence.**

- The named form: **Untested**.
- **Supports (indirect)** for writing objections before the verdict, by another hand when stakes allow.
  Liang et al. (EMNLP 2024, arXiv 2305.19118) name "Degeneration-of-Thought": once a model is confident,
  self-reflection stops producing new thoughts.
- **Supports (indirect)** for adversarial argument before a judge: Khan et al. (ICML 2024, arXiv
  2402.06782), see §25.

**Skill lines.**

- "Before answering, write the strongest objections to the answer you lean toward. After answering,
  reply to each: concede, distinguish, or refute." → `wdyt`
- "When two sources conflict, check in order: is either misquoted or stale; do they use a word
  differently; do they address different cases or times. Rank them only then." → `bulletproof`, `settle`

### 11. Descartes: the four rules and the *Rules for the Direction of the Mind*

**Method.**

- *Discourse on Method* Part II (AT VI 18–19) gives four rules:
  1. Accept nothing as true that you do not clearly know to be so, avoiding haste and prejudice.
  2. Divide each difficulty into as many parts as needed.
  3. Order your thoughts from simplest to most complex.
  4. Make enumerations so complete that you are sure nothing was omitted.
- The *Regulae* (c. 1628, AT X) sharpen these:
  - Rule 5: reduce involved propositions to simpler ones.
  - Rule 7: enumeration must be sufficient and ordered.
  - Rule 13: strip a well-understood question of superfluous conceptions.

Secondary: SEP "Descartes' Method", https://plato.stanford.edu/entries/descartes-method/

**Failures addressed.** Haste (premature closure). Incomplete enumeration ("nothing calls this" after
one grep). Attacking the whole problem at once.

**LLM evidence.** Ordered decomposition: **Supports** (Least-to-Most, 2022). Enumerated verification
questions: **Supports** (Dhuliawala et al., Chain-of-Verification, arXiv 2309.11495, 2023; abstract not
re-read).

**Skill line.**

- "Before asserting 'all' or 'none', list the cases it covers (callers, platforms, states). Say how the
  list was produced and what that method can miss." → `bulletproof` (absorbing `dissect`)

### 12. Leibniz: *characteristica universalis* and *calculemus*

**Method.**

- Leibniz proposed a universal symbolism whose signs mirror the composition of concepts, plus a
  calculus of reasoning. Disputes would then be settled as accountants settle sums: by sitting down and
  saying "*Calculemus*" ("let us calculate") ("The Art of Discovery", 1685, in Wiener ed., *Leibniz
  Selections*, 1951, p. 51).
- The method: translate a disagreement into a form where checking is mechanical.

Secondary: SEP "Leibniz's Influence on 19th Century Logic",
https://plato.stanford.edu/entries/leibniz-logic-influence/

**Failure addressed.** Arguing in prose about what could be computed, typed, tested, or queried.

**LLM evidence.** **Supports.** PAL (arXiv 2211.10435, 2022) and Logic-LM (arXiv 2305.12295, 2023)
show gains from handing the checkable part to an interpreter or solver.

**Skill line.**

- "If a disputed point can be computed, type-checked, tested, or queried, do that instead of arguing.
  Report the command and its output." → `settle`, `bulletproof`

### 13. Hume: the fork, and induction

**Method.**

- Every object of inquiry is either a relation of ideas, whose denial is contradictory and which
  reasoning settles, or a matter of fact, known only from experience (*Enquiry* §4.1).
- A claim that fits neither should be committed to the flames (§12.3).
- No demonstrative argument shows that unobserved cases resemble observed ones (§4.2; *Treatise*
  1.3.6). Custom bridges the gap, not reason.
- An "ought" cannot be read off an "is" without a further premise (*Treatise* 3.1.1.27).

Secondary: SEP "David Hume", https://plato.stanford.edu/entries/hume/ ; SEP "The Problem of Induction",
https://plato.stanford.edu/entries/induction-problem/

**Failures addressed.**

- Verifying matters of fact by thinking harder: self-review in place of observation.
- Generalizing from the cases that were run.
- Deriving a recommendation from a description without stating the value.

**LLM evidence.**

- **Supports.** Huang et al. (ICLR 2024, arXiv 2310.01798): without external feedback, LLMs struggle
  to self-correct reasoning, and sometimes get worse.
- **Supports.** Gou et al., CRITIC (arXiv 2305.11738, 2023): self-correction works when critique uses
  tools (abstract not re-read).

**Skill lines.**

- "Sort each claim: settled by reasoning or computation, or a matter of fact. A matter of fact needs an
  observation (file, run, log), not an argument." → `bulletproof`
- "Treat 'it worked in the cases I ran' as evidence for those cases. Name the ones not run."
  → `bulletproof`, `verify`

### 14. Kant, in depth

Kant matters here for a specific reason. The *Critiques* are a theory of what a reasoner may claim
given the faculties it has. He insists that judgment is a skill no rulebook supplies, and he gives tests
for when reason has overreached. Those are exactly the failures of a fluent model.

#### 14a. Determining vs reflective judgment, and why rules cannot teach judgment

**Method.**

- Judgment subsumes a particular under a universal. When the universal (the rule) is given, judgment
  is determining. When only the particular is given and the universal must be found, judgment is
  reflective (*Critique of Judgment*, Introduction IV, 5:179).
- Earlier, the first *Critique* argues that judgment cannot be taught by rules. A rule for applying a
  rule would need its own rule of application, and so on forever. Judgment is a talent that can only be
  practiced. Examples are judgment's "go-cart", the wheeled walker that teaches a child to walk
  (A133–134/B172–173).

Secondary: SEP "Kant's Aesthetics and Teleology" (Ginsborg), https://plato.stanford.edu/entries/kant-aesthetics/
; SEP "Kant's Theory of Judgment", https://plato.stanford.edu/entries/kant-judgment/

**Failures addressed.** Forcing a case under the nearest rule (rule-following without judgment). The
reverse: improvising a new rule where the project already has one.

**LLM evidence.** The distinction itself: **Untested**. Examples teaching application: **Supports
(indirect)**, from Wang et al. (ACL 2024). Demonstrations moved a single agent to the level of
multi-agent discussion.

**Skill lines.**

- "First decide which judgment this is. If a project rule covers the case, cite it and apply it. If
  none does, say so and state the rule you are inferring from this case." → `settle`, `wdyt`
- Skill-authoring rule: "Any skill that requires judgment carries one worked example. Rules alone do
  not teach their own application." → the skills README

#### 14b. The table of judgments and the categories

**Method.**

- Every judgment has a logical form under four headings (A70/B95), from which the categories are
  derived (A80/B106):
  - quantity: universal, particular, singular;
  - quality: affirmative, negative, infinite;
  - relation: categorical, hypothetical, disjunctive;
  - modality: problematic (possible), assertoric (actual), apodictic (necessary).
- Operationally the table is a completeness check on a claim. Whom or what does it cover? Under what
  condition? With what modal force?

Secondary: SEP "Kant's Theory of Judgment", https://plato.stanford.edu/entries/kant-judgment/

**Failures addressed.**

- Overgeneralization ("all callers" from one).
- Modal slide ("can fail" becomes "fails"; "does not" becomes "cannot").
- Hidden conditions.
- Hidden disjunctions (false dichotomy).

**LLM evidence.** **Untested.**

**Skill line.**

- "For each load-bearing claim, state its scope (all, some, this one), its condition (always, or only
  if…), and its modality (possible, observed, necessary). The evidence must match all three."
  → `bulletproof`

#### 14c. The antinomies and the critique of dogmatic reason

**Method.**

- Reason pushes concepts past any possible experience and generates illusion (Transcendental
  Dialectic). In the four antinomies, thesis and antithesis each have proofs that look sound
  (A426–461/B454–489).
- Kant does not pick a side. He diagnoses a premise both sides share: that the world is a given
  completed whole.
  - In the first two antinomies, both sides turn out false (A502–507/B530–535).
  - In the last two, both can be true in different respects (A528–532/B556–560).
- Dogmatism is proceeding without first examining reason's own capacity (Bxxxv).

Secondary: SEP "Kant's Critique of Metaphysics", https://plato.stanford.edu/entries/kant-metaphysics/

**Failures addressed.**

- Choosing between two well-argued positions when the question itself is malformed.
- Overconfidence beyond what the evidence can reach.
- Answering an unanswerable question.

**LLM evidence.**

- The need: **Supports (indirect)**. Kirichenko et al., AbstentionBench (arXiv 2506.09038, 2025):
  frontier models abstain poorly on false-premise and underspecified questions. Reasoning fine-tuning
  cut abstention by 24% on average, and larger reasoning budgets made it worse.
- The shared-premise check: **Untested**.

**Skill lines.**

- "If both sides of a question have arguments that look sound, stop choosing. Find the premise both
  share and test it." → `wdyt`, `panel`
- "Before answering, say whether the evidence available here can settle the question. If not, say what
  could." → `wdyt`, `settle`

#### 14d. The three maxims of common human understanding (*Critique of Judgment* §40)

**Method.**

- Kant names three maxims (5:294; also *Anthropology* §43, 7:200, and *Jäsche Logic* Introduction VII,
  9:57):
  1. Think for oneself: the unprejudiced way of thinking, never passive.
  2. Think in the position of everyone else: the broadened way of thinking, which reflects on one's
     judgment from a universal standpoint reached by taking others' standpoints.
  3. Always think consistently: the hardest, attained only by combining the first two and practice.
- Each maxim targets a different way judgment fails.

Secondary: SEP "Kant's Account of Reason" (Williams), https://plato.stanford.edu/entries/kant-reason/

**Failures addressed.**

1. Sycophancy and deference to authority.
2. Parochial framing and missed stakeholders.
3. Inconsistency across turns, or with the project's own rules.

**LLM evidence.**

- Maxim 1: the problem is documented (Sharma 2023). System 2 Attention **supports** a remedy.
- Maxim 2: **Supports**, for theory-of-mind tasks. Wilf et al., "Think Twice" (SimToM, arXiv
  2311.10227, 2023; abstract not re-read): an explicit perspective-taking step improved
  theory-of-mind accuracy.
- Maxim 3: **Supports**, from maieutic consistency (Jung 2022).

**Skill lines.**

- "Form your verdict from evidence before weighing which answer the asker prefers. If they differ, say
  so plainly." → `wdyt`
- "Restate the decision from the standpoint of each party it binds (user, future maintainer, other
  agents on the checkout) and name each one's strongest objection." → `wdyt`, `panel`
- "Check the verdict against your earlier statements and the project's rules. Resolve or name every
  conflict." → `wdyt`

#### 14e. The categorical imperative as a universalizability test for rules

**Method.**

- Act only on a maxim you can at the same time will to be a universal law (*Groundwork* 4:421). There
  are two tests (4:424):
  - Contradiction in conception: universalized, the maxim defeats itself. The lying promise destroys
    the practice of promising (4:422).
  - Contradiction in will: one could not consistently will a world where it holds.
- Kant's test is a test of the rule, not of the act's outcome.

Secondary: SEP "Kant's Moral Philosophy" (Johnson & Cureton), https://plato.stanford.edu/entries/kant-moral/

**Failures addressed.** Local exceptions that break shared state once generalized: "skip the flaky
test", "push to main when urgent", "edit the generated file directly". Special pleading.

**LLM evidence.** **Untested** as a prompt. **Supports (indirect)**: Bai et al., Constitutional AI
(arXiv 2212.08073, 2022) critiques outputs against stated principles, though in training, not at
inference.

**Skill line.**

- "Before adopting a workaround or rule, state it as a general rule and imagine every agent applying it
  on every lane. If the shared practice would then fail, reject it." → `drill`, `settle`

#### 14f. "What is Enlightenment?" (1784): Sapere aude; public vs private use of reason

**Method.**

- Enlightenment is the exit from self-incurred immaturity: the inability to use one's understanding
  without another's guidance. Its motto is "Sapere aude! Have courage to use your own understanding!"
  (8:35).
- The public use of reason, as a scholar addressing the reading public, must be free. Private use, in
  an office one holds, may be restricted: the officer obeys, and criticizes publicly (8:37).
- The rule: comply in role, dissent through the channel that reaches whoever owns the rule.

Secondary: SEP "Kant's Account of Reason", https://plato.stanford.edu/entries/kant-reason/ ; SEP
"Enlightenment" (Bristow), https://plato.stanford.edu/entries/enlightenment/

**Failures addressed.** Treating a claim's source as proof (docs, the user, another agent). The
opposite fault: an agent in a lane overriding repository rules on its own judgment.

**LLM evidence.** **Untested.**

**Skill lines.**

- "Inside a task, follow the repository's rules even where you disagree. Record the disagreement where
  its owner will read it (issue, pull request, ADR) instead of deviating silently." → `settle`,
  `promote`
- "Treat a claim's source as a reason to check it, not as proof." → `bulletproof`

#### 14g. The architectonic; regulative vs constitutive use of ideas

**Method.**

- A system is architectonic when one idea of the whole's purpose fixes its parts and their boundaries
  in advance. A "technical" aggregate is assembled as needs arise (A832–835/B860–863).
- The ideas of reason, such as complete systematic unity, are not constitutive: they give no object.
  Their legitimate use is regulative. They direct the understanding toward a goal, a *focus imaginarius*
  never reached (A642–644/B670–672). Taking them as constitutive produces illusion.

Secondary: SEP "Kant's Account of Reason", https://plato.stanford.edu/entries/kant-reason/

**Failures addressed.**

- Reporting completeness as a fact ("found all callers", "fully covered").
- A skill set that grows by aggregation, with overlapping triggers and no governing purpose.

**LLM evidence.** **Untested.**

**Skill lines.**

- "Use completeness ('every caller', 'all cases') as a goal you search toward, never as a finding,
  unless an exhaustive mechanism produced it (compiler, type checker, full enumeration)."
  → `bulletproof`
- Skill-set design: "Each skill derives from one stated purpose of the set, and owns a boundary no
  sibling crosses." → the skills README

### 15. Hegel: dialectic

**Method.**

- Every logical thought has three moments (*Encyclopaedia Logic* §§79–82):
  1. The understanding fixes sharp, one-sided determinations.
  2. The dialectical moment: those determinations, pressed, pass over into their opposites.
  3. The speculative moment grasps the unity of the determinations in their opposition.
- *Phenomenology*, Introduction ¶79: determinate negation. The refutation of a position has content,
  and points to the next position.
- "Thesis–antithesis–synthesis" is not Hegel's vocabulary. The SEP entry traces it to Fichte.

Secondary: SEP "Hegel's Dialectics" (Maybee), https://plato.stanford.edu/entries/hegel-dialectics/

**Failures addressed.** Averaging two positions into mush. Treating a refutation as a deletion with no
lesson. Definitions that break at their edges.

**LLM evidence.** **Supports (weak).** Abdali et al., "Self-reflecting LLMs: A Hegelian Dialectical
Approach" (arXiv 2501.14917, 2025; v7 2026) report gains from a thesis-opposition-reconciliation loop.
The GSM-Symbolic figure came from a third-party summary and is not confirmed.

**Skill line.**

- "When an approach fails, state exactly what the failure shows. The next approach must keep what the
  first got right and answer that failure. Reject a compromise that does neither." → `wdyt`,
  `investigate-first`

### 16. Mill: the methods of induction; hearing the other side

**Method.**

- *System of Logic* III.8 gives five methods:
  - Agreement: the circumstance common to all cases of the effect.
  - Difference: two cases alike except one circumstance, with and without the effect.
  - The joint method.
  - Residues: subtract known effects, and the remainder comes from the remaining antecedents.
  - Concomitant variation.
- Difference is the experimental method.
- *On Liberty* ch. 2: a truth never contested becomes dead dogma. One must hear the opposing arguments
  from people who actually believe them, in their most plausible form. "He who knows only his own side
  of the case, knows little of that."

Secondary: SEP "John Stuart Mill" (Macleod), https://plato.stanford.edu/entries/mill/

**Failures addressed.** Causal claims from co-occurrence in logs. One-sided answers. Repeating rules
without their reasons.

**LLM evidence.**

- **Supports (indirect).** Jin et al., Corr2Cause (ICLR 2024, arXiv 2306.05836): seventeen LLMs were
  near random at inferring causation from correlational statements. Causes need produced differences,
  not reading.
- **Supports**, for hearing both sides before a judge: Khan 2024 (§25).

**Skill lines.**

- "Claim a cause only from a difference you produced: two runs that differ in one change, with and
  without the effect (bisect, revert, toggle)." → `investigate-first`, `dissect`
- "State the strongest case for the option you reject, as its advocate would, before rejecting it."
  → `panel`, `wdyt`

### 17. Frege: sense and reference

**Method.**

- An expression has a reference (the object) and a sense (its mode of presentation) ("Über Sinn und
  Bedeutung", 1892).
- "The morning star is the evening star" is informative, though it names one object twice, because the
  senses differ.
- In belief contexts, expressions refer to their senses, so substituting co-referring terms can change
  truth.

Secondary: SEP "Gottlob Frege" (Zalta), https://plato.stanford.edu/entries/frege/

**Failures addressed.**

- Two names treated as two things, so logic gets duplicated.
- One name treated as one thing when it denotes two ("track" in the UI vs the CRDT node).
- Equivocation in specs.

**LLM evidence.** **Supports (indirect).** Berglund et al., "The Reversal Curse" (ICLR 2024, arXiv
2309.12288): models trained on "A is B" fail to infer "B is A" (abstract not re-read). Identity is not
handled symmetrically for free.

**Skill line.**

- "When two names may denote one thing, or one name two things, resolve the reference in the code
  (definitions, types, ids). From then on, use one name per referent." → `drill`

### 18. Wittgenstein: meaning as use, language games, the limits of speech

**Method.**

- For a large class of cases, the meaning of a word is its use in the language (*Philosophical
  Investigations* §43). Words live in language-games, practices with their own point (§23).
- To find what a concept covers, "don't think, but look" at the cases (§66). They are often joined by
  family resemblance, not a definition (§67).
- No rule fixes its own application; practice does (§§198–202).
- The *Tractatus* ends: "Whereof one cannot speak, thereof one must be silent" (7).

Secondary: SEP "Ludwig Wittgenstein" (Biletzki & Matar), https://plato.stanford.edu/entries/wittgenstein/

**Failures addressed.** Defining a project term from the dictionary or from training data instead of
its use in this codebase. Filling an evidence gap with fluent speculation.

**LLM evidence.**

- **Supports**, for explicit silence conditions. AbstentionBench (2025): a system prompt describing
  when not to answer raised abstention for standard and reasoning models.
- **Supports (indirect).** Kalai et al., "Why Language Models Hallucinate" (arXiv 2509.04664, 2025):
  training and grading reward guessing over admitting uncertainty.

**Skill lines.**

- "Define a project term by its uses: find where code, tests, and docs use it, and quote two."
  → `drill`
- "Where evidence runs out, write 'not determinable from here' and what would determine it. Do not fill
  the gap." → `bulletproof`, `tldr`

### 19. Popper: falsification

**Method.**

- A theory is empirical only if it forbids some observable states of affairs (*Logic of Scientific
  Discovery* §§6, 31–35).
- Seek the test that could refute, not confirmations. A confirmation counts only when it was a risky
  prediction (*Conjectures and Refutations*, ch. 1).
- Reject "conventionalist stratagems": ad hoc auxiliary hypotheses that save a theory from refutation
  (*LSD* §§19–20).

Secondary: SEP "Karl Popper" (Thornton), https://plato.stanford.edu/entries/popper/

**Failures addressed.**

- Confirmation bias: running checks that would pass anyway.
- Diagnoses that nothing could refute.
- Regression tests that never failed.

**LLM evidence.** **Supports.** Huang, Jin, Li et al., POPPER (ICML 2025, arXiv 2502.09858). LLM
agents designed and ran falsification experiments under sequential error control. They matched human
scientists on biological hypothesis validation, about 10× faster.

**Skill lines.**

- "Before testing a hypothesis, write the result that would refute it. Run a test that could produce
  that result." → `investigate-first`, `bulletproof`
- "A regression test counts only if it fails without the fix." → `verify`, `surgical-patch`

### 20. Lakatos: research programmes

**Method.**

- A research programme has a hard core, which its negative heuristic forbids attacking. It also has a
  protective belt of auxiliary hypotheses, which its positive heuristic says how to adjust
  ("Falsification and the Methodology of Scientific Research Programmes", 1970).
- A programme is progressive if its adjustments predict novel facts, some of them corroborated. It is
  degenerating if they only accommodate known anomalies after the fact.

Secondary: SEP "Imre Lakatos" (Musgrave & Pigden), https://plato.stanford.edu/entries/lakatos/

**Failures addressed.** Sunk-cost patching of a wrong approach. The opposite fault: abandoning a sound
approach at its first anomaly (naive falsificationism).

**LLM evidence.** **Untested.**

**Skill line.**

- "Count the patches made to keep an approach working. If the last two only explained failures already
  seen and predicted nothing new, call the approach degenerating and re-examine its core."
  → `investigate-first`

### 21. Kuhn: anomaly and crisis

**Method.**

- Normal science solves puzzles inside a paradigm and absorbs anomalies (*Structure of Scientific
  Revolutions*, 1962, ch. 6–8).
- When anomalies accumulate and resist, or strike at the core, the field enters crisis. Only then is
  the framework itself reconsidered.

Secondary: SEP "Thomas Kuhn" (Bird), https://plato.stanford.edu/entries/thomas-kuhn/

**Failure addressed.** Anchoring on a first model of the system, and explaining away observations that
do not fit.

**LLM evidence.** **Untested** as a remedy. Liang 2023 documents the anchoring (Degeneration-of-Thought).

**Skill line.**

- "Keep a list of observations your current explanation does not fit. At three, or at one that strikes
  its core, rebuild the explanation from the observations instead of patching it."
  → `investigate-first`

### 22. Toulmin: the layout of arguments

**Method.**

- *The Uses of Argument* (1958, ch. III) breaks an argument into:
  - the claim;
  - the data or grounds;
  - the warrant, which licenses the step from data to claim;
  - the backing, which supports the warrant;
  - the qualifier ("presumably", "certainly");
  - the rebuttal: the conditions under which the claim fails.
- Standards of warrant are field-dependent.

Secondary: SEP "Argument and Argumentation", https://plato.stanford.edu/entries/argument/ ; SEP
"Informal Logic", https://plato.stanford.edu/entries/logic-informal/

**Failures addressed.** Claims with evidence but no stated reason why the evidence counts. Unqualified
confidence. Missing exception conditions.

**LLM evidence.** **Supports (modest, confounded).** Castagna, Sassoon & Parsons,
"Critical-Questions-of-Thought" (arXiv 2412.15177, 2024). The method checks a reasoning plan against
eight Toulmin-derived critical questions and revises it until they pass. The repo reports +4.06%
(MT-Bench reasoning) and +4.68% (math) on Claude 3.5 Sonnet. An outside review notes the ablation is
confounded with repeated sampling.

**Skill line.**

- "For the recommendation, give: the evidence; the rule that makes it count; what backs that rule; how
  sure you are; and the condition under which it would be wrong." → `wdyt`, `bulletproof`

### 23. Perelman: the new rhetoric and the universal audience

**Method.**

- Argument is always addressed to an audience (*The New Rhetoric*, with Olbrechts-Tyteca, 1958; English
  edition 1969, §§4–9).
- Persuasion targets a particular audience. Conviction targets the universal audience: all reasonable,
  competent people.
- An argument that works only because this audience already shares a value is weaker. The universal
  audience is the standard for claims that pretend to objectivity.

Secondary: SEP "Argument and Argumentation" (its sections on the new rhetoric and the universal
audience), https://plato.stanford.edu/entries/argument/

**Failure addressed.** Sycophancy: tailoring the verdict to the asker's known preferences.

**LLM evidence.** The problem: **Supports (indirect)** (Sharma 2023). This remedy: **Untested**.

**Skill line.**

- "Write the verdict so it would convince a competent reviewer who does not share the asker's
  preferences. Mark any reason that works only because the asker already believes it." → `wdyt`

### 24. Pragma-dialectics: rules for a critical discussion

**Method.** A critical discussion resolves a difference of opinion on the merits (van Eemeren &
Grootendorst, *A Systematic Theory of Argumentation*, 2004, ch. 6). It runs through four stages:
confrontation, opening, argumentation, concluding. Ten rules govern it, and breaking any of them is a
fallacy:

1. Freedom: no one may block a standpoint or a doubt.
2. Burden of proof: whoever advances a standpoint must defend it.
3. Standpoint: attack only the standpoint actually advanced.
4. Relevance: defend a standpoint only with argument relevant to it.
5. Unexpressed premise: neither deny your own nor inflate the other's.
6. Starting point: do not falsely present a premise as agreed, or deny one that was.
7. Validity.
8. Argument scheme: use an appropriate scheme, correctly applied.
9. Closure: a failed defense means retracting the standpoint; a successful one means withdrawing the
   doubt.
10. Usage: no unclear or ambiguous formulations.

Secondary: SEP "Argument and Argumentation", https://plato.stanford.edu/entries/argument/

**Failures addressed.** Multi-agent review drift: straw-manning, shifting standpoints, reviewers who
never concede, findings that never close.

**LLM evidence.** **Untested.**

**Skill lines.**

- "Each finding states one standpoint and its evidence. The author answers it or changes the work. A
  finding its reviewer cannot defend with evidence is withdrawn." → `revolver`
- "End every disagreement with a closure line: whose case held, and what is retracted." → `revolver`,
  `panel`

### 25. Legal reasoning

**Method.**

- **IRAC** (issue, rule, application, conclusion) is the law-school layout. LegalBench organizes legal
  reasoning tasks around these components (Guha et al., arXiv 2308.11462, 2023; abstract not re-read).
- **Ratio decidendi vs obiter dicta.** The binding part of a precedent is the principle needed for the
  decision on the facts the court treated as material. Remarks beyond that are persuasive at most
  (Goodhart, "Determining the Ratio Decidendi of a Case", *Yale Law Journal* 40, 1930).
- **Stare decisis.** Follow the earlier decision on materially similar facts. Depart only by
  distinguishing the facts, or by overruling explicitly.
- **Burden and standard of proof.** One rule fixes who must establish a point. Another fixes how
  strongly: preponderance, clear and convincing, or beyond reasonable doubt. Stakes set the standard.
- **Audi alteram partem.** No decision against a party without hearing that party.

Secondary: SEP "Precedent and Analogy in Legal Reasoning" (Lamond),
https://plato.stanford.edu/entries/legal-reas-prec/ ; SEP "Legal Probabilism",
https://plato.stanford.edu/entries/legal-probabilism/ ; SEP "The Rule of Law" (Waldron),
https://plato.stanford.edu/entries/rule-of-law/

**Failures addressed.**

- Deciding without stating the governing rule.
- Citing incidental remarks in ADRs or docs as binding.
- Relitigating settled decisions, or silently departing from them.
- No stated threshold for "verified".
- Deciding before the other side is heard.

**LLM evidence.**

- **Supports (older model).** Yu, Quartey & Schilder, "Legal Prompting" (NLLP @ EMNLP 2022, arXiv
  2212.01326). IRAC-style prompts on GPT-3 for COLIEE entailment raised the 2021 best from 0.7037 to
  0.8148. A follow-up paper disputes which prompt variant won.
- **Supports**, for a stated standard governing silence: AbstentionBench (2025).
- **Supports**, for hearing both sides: Khan et al., "Debating with More Persuasive LLMs Leads to More
  Truthful Answers" (ICML 2024, arXiv 2402.06782). On QuALITY, judges reading a debate reached 76%
  (LLM judges) and 88% (human judges), against naive baselines of 48% and 60%.
- **Mixed**, for debate as an accuracy booster. See Choi et al. (§28).

**Skill lines.**

- "When citing a prior decision, quote the part that decided its case. Treat side remarks as advice.
  Depart from a decision only by naming the material fact that differs." → `settle`, `promote`
- "Set the standard of proof before looking. A reversible choice needs the better case; an
  irreversible one needs evidence that excludes the alternatives." → `wdyt`, `settle`
- "Before ruling against an option or a reviewer's finding, state its case in its own best terms."
  → `panel`, `revolver`

### 26. Rapoport's rules and steelmanning

**Method.**

- Rapoport argued that one should show the opponent the region in which their position is valid
  before contesting it (*Fights, Games, and Debates*, 1960).
- Dennett's formulation (*Intuition Pumps*, 2013, "Rapoport's Rules", which Dennett says is his own
  wording from memory):
  1. Re-express the target's position so well that they wish they had put it that way.
  2. List points of agreement.
  3. Mention anything you learned from them.
  4. Only then rebut.
- Steelmanning is the informal descendant.

Secondary: Sunstein, "The Rapoport Rules", https://casssunstein.substack.com/p/the-rapoport-rules

**Failures addressed.** Straw-manning alternatives. Its mirror image, a sycophantic steelman of only
the user's position.

**LLM evidence.** **Untested** in peer-reviewed work. The one found study is a non-peer-reviewed SSRN
preprint ("Steelmanning LLM Review", Brilliant). Caution: Eskandari & Sarathy (2024) found large models
argue persuasively for wrong options, so a steelman must be checked against evidence, not admired.

**Skill line.**

- "Before criticizing a design or claim, restate it in its strongest form and list what it gets right.
  The critique must address that version." → `revolver`, `panel`

### 27. Premortem (Klein) and red teaming

**Method.**

- **Premortem.** Before committing, the team imagines the project has already failed and writes down
  why (Klein, "Performing a Project Premortem", *HBR*, Sept 2007,
  https://hbr.org/2007/09/performing-a-project-premortem). It rests on prospective hindsight: treating
  an outcome as certain improves people's ability to generate reasons for it. Mitchell, Russo &
  Pennington, "Back to the Future", *J. Behavioral Decision Making* 2(1), 1989,
  https://doi.org/10.1002/bdm.3960020103. Klein cites roughly 30%.
- **Red teaming.** An independent team adopts the adversary's goals to find how a plan or system
  breaks.

Secondary: the Mitchell et al. DOI above. Veinott, Klein & Wiggins (ISCRAM 2010) report that the
premortem reduced overconfidence more than a pro/con critique (not re-read).

**Failures addressed.** Overconfident plans. Unanticipated failure modes. Author blindness.

**LLM evidence.**

- **Supports.** Wang et al., "Devil's Advocate: Anticipatory Reflection for LLM Agents" (Findings of
  EMNLP 2024, arXiv 2405.16334). Before each action the agent considers how it might fail and prepares
  fallbacks. On WebArena it reached 23.5% success vs 22.7% for LATS, with 45% fewer trials and plan
  revisions.
- **Supports.** Perez et al., "Red Teaming Language Models with Language Models" (arXiv 2202.03286,
  2022), and Ganguli et al. (arXiv 2209.07858, 2022): LM red-teamers find failures at scale (abstracts
  not re-read).
- The premortem framing itself: **Untested** (none found).

**Skill lines.**

- "Before executing a plan, assume it has failed a week from now. Write the three likeliest causes and
  change the plan, or add a check, for each." → `drill`
- "Have the work reviewed by an agent that did not write it and is told to find how it breaks."
  → `revolver`

### 28. Kahneman: System 1/2, and noise

**Method.**

- *Thinking, Fast and Slow* (2011): fast associative judgment (System 1) produces anchoring,
  availability, substitution (answering an easier question), and WYSIATI ("what you see is all there
  is"). Slow effortful reasoning (System 2) checks it, lazily.
- *Noise* (Kahneman, Sibony & Sunstein, 2021) adds unwanted variability between judgments of the same
  case. Its decision hygiene:
  - collect independent judgments before any discussion, then aggregate;
  - break a judgment into separately scored mediating assessments, and delay the overall view
    (the "mediating assessments protocol");
  - take the outside view (reference class) first.

Secondary: SEP "Bounded Rationality", https://plato.stanford.edu/entries/bounded-rationality/

**Failures addressed.**

- Run-to-run variance (noise).
- Anchoring on the first hypothesis.
- Answering from what is in context only.
- Holistic preferences formed before the criteria are scored.

**LLM evidence.**

- **Contradicts** the value of a generic "slow down" cue for frontier models. Hagendorff, Fabi &
  Kosinski (*Nature Computational Science*, 2023): GPT-4 avoided the cognitive-reflection traps on 96%
  of items, and accuracy barely dropped without chain-of-thought.
- **Supports**, for independent sampling plus aggregation.
  - Wang et al., Self-Consistency (arXiv 2203.11171, 2022).
  - Schoenegger et al., "Wisdom of the Silicon Crowd" (*Science Advances*, 2024): a median of 12 LLMs
    matched a 925-person human crowd.
  - Choi, Zhu & Li, "Debate or Vote" (NeurIPS 2025, arXiv 2508.17536): majority voting accounts for
    most of multi-agent debate's gains. Their model shows that debate alone is a martingale and does
    not raise expected accuracy.
  - Smit et al. (ICML 2024, arXiv 2311.17371): debate protocols did not reliably beat self-consistency.
- Mediating assessments in LLMs: **Untested**.

**Skill lines.**

- "Score each option on each criterion separately before forming an overall preference." → `panel`,
  `wdyt`
- "For a consequential judgment, take independent answers (fresh agents or runs), report the spread,
  and count them before any discussion." → `panel`
- "Name what the answer depends on that is not in front of you." → `wdyt`

### 29. Bayesian updating

**Method.**

- The posterior is proportional to prior times likelihood (Bayes, 1763; Jaynes, *Probability Theory*,
  2003).
- Superforecasting turns this into practice (Tetlock & Gardner, *Superforecasting*, 2015):
  - start from the base rate of the reference class (outside view);
  - adjust for the specifics of the case (inside view);
  - update in small steps as evidence arrives;
  - state probabilities as numbers.

Secondary: SEP "Bayesian Epistemology" (Lin), https://plato.stanford.edu/entries/epistemology-bayesian/

**Failures addressed.** Overconfidence. Base-rate neglect. Over- or under-reacting to one new
observation.

**LLM evidence: Mixed.**

- Qiu et al., "Bayesian Teaching" (*Nature Communications*, 2026; arXiv 2503.17523). Off-the-shelf
  LLMs fall far short of Bayesian updating across interactions. Fine-tuning on a Bayesian model's
  predictions fixes much of it. So an instruction to "be Bayesian" is unlikely to suffice.
- Xiong et al. (ICLR 2024, arXiv 2306.13063): verbalized confidence is overconfident; sampling
  consistency helps.
- Tian et al. (arXiv 2305.14975, 2023): for RLHF models, verbalized confidence is better calibrated
  than token probabilities.
- Halawi et al. (arXiv 2402.18563, 2024): retrieval plus aggregation came near the human crowd in
  forecasting.

**Skill lines.**

- "Give the base rate before the case: how often has this kind of diagnosis or change turned out right
  here? Then adjust, and say by how much and why." → `wdyt`, `investigate-first`
- "State confidence as a number, together with the observation that would move it most." → `wdyt`

### 30. Bacon: the idols, and tables of exclusion (added)

**Method.**

- *Novum Organum* I.38–68 names four idols that distort judgment:
  - of the tribe: human nature, such as seeing more order than exists;
  - of the cave: individual bias;
  - of the marketplace: words that mislead;
  - of the theatre: inherited systems.
- Book II (11–18) replaces enumeration of instances with tables of presence, absence, and degree.
  Inference proceeds by exclusion: rule causes out before ruling one in.

Secondary: SEP "Francis Bacon", https://plato.stanford.edu/entries/francis-bacon/

**Failures addressed.** Pattern-seeing in logs. Words standing in for things. Confirming a favored
cause instead of eliminating rivals.

**LLM evidence.** **Untested.**

**Skill line.**

- "List the candidate causes. Strike each one present when the effect is absent, or absent when it is
  present. Name the survivor only after the strikes." → `investigate-first`

### 31. Spinoza: the geometric method (added)

**Method.**

- The *Ethics* (1677) proceeds *ordine geometrico*: definitions, axioms, then propositions, each with a
  demonstration that cites only earlier items. Scholia speak to the reader.
- The method makes every dependency inspectable.

Secondary: SEP "Baruch Spinoza", https://plato.stanford.edu/entries/spinoza/

**Failure addressed.** Undefined terms and unstated assumptions doing hidden work.

**LLM evidence.** **Untested.** Expensive for everyday use.

**Skill line.**

- "List the definitions and assumptions an argument uses. Each later step must cite one of them or an
  earlier step." → `corpus-spec` (not `wdyt`)

### 32. Collingwood: the logic of question and answer (added)

**Method.**

- Every statement answers a question. You cannot tell what a proposition means, or whether it is true,
  until you know the question it answers (*An Autobiography*, 1939, ch. V).
- Two statements contradict only if they answer the same question.
- *An Essay on Metaphysics* (1940) adds absolute presuppositions: the unquestioned starting points of a
  practice.

Secondary: SEP "R.G. Collingwood", https://plato.stanford.edu/entries/collingwood/

**Failures addressed.** Misreading code, docs, or requests by judging them against a question they did
not answer. Spurious contradictions between sources.

**LLM evidence.** **Untested.**

**Skill line.**

- "Before judging a piece of code, a document, or a claim, state the question it was answering.
  Disagreement counts only between answers to the same question." → `dissect`, `wdyt`

### 33. Habermas: ideal speech conditions (added)

**Method.**

- In discourse ethics, a norm is valid only if all affected could accept it as participants in a
  practical discourse ("Discourse Ethics", 1983, in *Moral Consciousness and Communicative Action*;
  *Theory of Communicative Action*, 1981). The procedure borrows Alexy's rules:
  - every competent party may take part;
  - anyone may question any assertion, introduce any assertion, and express needs;
  - no one may be prevented from doing so by coercion.
- What decides is the "unforced force of the better argument".

Secondary: SEP "Jürgen Habermas" (Bohman & Rehg), https://plato.stanford.edu/entries/habermas/

**Failure addressed.** In multi-agent setups, the orchestrator's view, the first answer, or the
strongest model's view winning by position.

**LLM evidence.** **Untested.** Liang 2023 also notes that LLM judges may not be fair when the debating
models differ.

**Skill line.**

- "Weigh findings by their evidence, never by which agent, model, or role produced them." → `panel`,
  `revolver`

### 34. Pólya: *How to Solve It* (added, and a caution)

**Method.**

- Problem solving has four phases (*How to Solve It*, 1945): understand the problem, devise a plan,
  carry it out, look back.
- Heuristic questions drive each phase. What is the unknown? Do you know a related problem? Can you
  check the result? Can you derive it differently?
- Schoenfeld's review found that Pólya's heuristics are "descriptive rather than prescriptive". They
  let experts recognize a strategy, but do not tell novices how to carry it out. Teaching worked only
  once each heuristic was broken into fine-grained strategies plus monitoring.

Secondary: Schoenfeld, "Learning to Think Mathematically" (1992), p. 54 of
https://jwilson.coe.uga.edu/emat7050/schoenfeld_maththinking.pdf (read this session).

**Failure addressed.** Declaring done without looking back.

**LLM evidence.** Checking by a second route: **Supports** (Chain-of-Verification, 2023). Schoenfeld's
finding is the human precedent for Part 5's caution: a named heuristic is not a procedure.

**Skill line.**

- "After finishing, check the result by a second route: a different method or independent evidence."
  → `verify-and-stop`, `bulletproof`

---

## Part 2. Mapping table

Evidence key: S = supports; S(i) = supports, indirect; M = mixed; C = contradicts; U = untested.

| Thinker / method | Failure mode | Skill line (short) | Target | Evidence |
|---|---|---|---|---|
| Pythagoreans: number | Unquantified comparatives | Put a number on every comparative claim | `bulletproof` | S(i) (PAL 2022) |
| Pythagoreans: harmony | Parts that do not compose | Totals, units, and two counting methods must agree | `bulletproof` | U |
| Pythagoreans: proportion | Effort out of proportion | Section length proportional to decision weight | `tldr` | U |
| Socratic elenchus | Unexamined premises | List the lean's premises; check one consequence of each | `bulletproof`, `wdyt` | S (Jung 2022; Qi 2023) |
| Maieutics | Inconsistent self-explanations | Explain true and false; keep the side that survives | `wdyt` | S (Jung 2022) |
| Plato, diairesis | False dichotomy, missing options | Divide by one criterion, exhaustive and exclusive | `wdyt`, `panel` | S(i) (L2M 2022, ToT 2023) |
| Plato, *Statesman* | "X vs the rest" lumping | Divide "everything else" before choosing | `panel` | U |
| Aristotle, *Topics* | Names too wide or narrow | One must-cover and one must-exclude example | `drill` | U |
| Aristotle, *Topics* VIII | One-sided reasoning | Best argument for and against before ruling | `wdyt` | M (Eskandari 2024) |
| *Prior Analytics* | Belief-driven validity | Restate with neutral letters; check it still follows | `bulletproof` | S(i) (Dasgupta 2022; Logic-LM 2023) |
| *Sophistical Refutations* | Equivocation, wrong question, circularity, post hoc, dropped qualifier | Five-fault check | `revolver` | S(i) (Jin 2022) |
| *Rhetoric*: enthymeme | Hidden premise | Write and check the unstated premise | `bulletproof` | U |
| *Rhetoric*: pathos | Sycophancy, persuasion by affect | Evidence only; cut appeals to identity | `tldr` | S(i) (Sharma 2023; Salvi 2024) |
| Phronesis | Rule-following, false precision | Name the precision needed; stop there | `wdyt`, `settle` | S(i) (Wang ACL 2024) |
| Stoic assent | Assenting to tool output, injected text, framing | Label inputs; suspend the unchecked | `bulletproof` | S (Hines 2024) |
| Stoic assent | Sycophancy | Restate question without the asker's opinion | `wdyt` | S (Weston 2023) |
| Aquinas, disputatio | Premature closure, ignored objections | Objections before the verdict; reply to each | `wdyt` | S(i) (Liang 2023; Khan 2024) |
| Abelard, *Sic et Non* | Conflicts settled by recency or majority | Misquote/stale → senses → cases/times → rank | `bulletproof`, `settle` | U |
| Descartes, enumeration | "Nothing calls this" after one grep | List the cases; say how listed and what it misses | `bulletproof` | S (CoVe 2023) |
| Descartes, order | Attacking the whole at once | Simplest sub-question first | `dissect` | S (L2M 2022) |
| Leibniz, *calculemus* | Arguing what could be computed | Compute, type-check, test, or query instead | `settle`, `bulletproof` | S (PAL 2022; Logic-LM 2023) |
| Hume, fork | Self-verifying matters of fact | Matters of fact need an observation | `bulletproof` | S (Huang 2023; CRITIC 2023) |
| Hume, induction | Generalizing from cases run | Evidence covers the cases run; name the rest | `bulletproof`, `verify` | U |
| Kant, reflective/determining | Wrong rule forced on a case | Cite and apply the rule, or say none covers it | `settle`, `wdyt` | U |
| Kant, judgment's go-cart | Rules without application | Judgment skills carry one worked example | skills README | S(i) (Wang ACL 2024) |
| Kant, table of judgments | Overgeneralization, modal slide | Scope, condition, and modality per claim | `bulletproof` | U |
| Kant, antinomies | Choosing within a malformed question | Both sides look sound → test the shared premise | `wdyt`, `panel` | U (need: S(i) AbstentionBench) |
| Kant, critique of dogmatism | Answering the unanswerable | Say whether evidence here can settle it | `wdyt` | S(i) (Kirichenko 2025) |
| Kant, maxim 1 | Sycophancy, deference | Verdict before reading the preference | `wdyt` | S(i) (Sharma 2023; Weston 2023) |
| Kant, maxim 2 | Parochial framing | Each bound party's strongest objection | `wdyt`, `panel` | S(i) (SimToM 2023) |
| Kant, maxim 3 | Inconsistency | Check against earlier claims and project rules | `wdyt` | S(i) (Jung 2022) |
| Kant, categorical imperative | Self-defeating workarounds | Universalize across agents and lanes | `drill`, `settle` | U (S(i) CAI 2022) |
| Kant, Enlightenment | Deference; or silent deviation | Comply in task; dissent where the owner reads | `settle`, `promote` | U |
| Kant, regulative ideas | Completeness reported as fact | Completeness is a goal unless mechanically exhaustive | `bulletproof` | U |
| Kant, architectonic | Skill sprawl, overlapping triggers | One purpose; each skill owns a boundary | skills README | U |
| Hegel, determinate negation | Mushy compromise; refutation without a lesson | Next approach keeps the gain and answers the failure | `wdyt`, `investigate-first` | S (weak; Abdali 2025) |
| Mill, method of difference | Causation from correlation | Cause only from a produced difference | `investigate-first` | S(i) (Corr2Cause 2023) |
| Mill, *On Liberty* | One-sidedness | Advocate's case before rejecting | `panel`, `wdyt` | S (Khan 2024) |
| Frege | Equivocation, duplicate concepts | Resolve the reference; one name per referent | `drill` | S(i) (Reversal Curse 2023) |
| Wittgenstein, use | Dictionary definitions | Define by quoted uses in code and docs | `drill` | U |
| Wittgenstein, TLP 7 | Fluent speculation | "Not determinable from here" + what would settle it | `bulletproof`, `tldr` | S (AbstentionBench 2025; Kalai 2025) |
| Popper | Confirmation bias | Write the refuting result first; test could fail | `investigate-first` | S (POPPER 2025) |
| Popper | Tests that never failed | Regression test must fail without the fix | `verify` | U (standard practice) |
| Lakatos | Sunk-cost patching | Two non-predictive patches → re-examine the core | `investigate-first` | U |
| Kuhn | Anchoring, explaining anomalies away | Anomaly list; rebuild at three | `investigate-first` | U (need: S(i) Liang 2023) |
| Toulmin | Unwarranted, unqualified claims | Evidence, rule, backing, confidence, defeat condition | `wdyt` | S (modest; CQoT 2024) |
| Perelman | Tailoring to the asker | Convince a reviewer without the asker's preferences | `wdyt` | U |
| Pragma-dialectics | Review drift, no closure | One standpoint per finding; defend or withdraw; closure line | `revolver` | U |
| IRAC | Decisions without a governing rule | Issue, rule, application, conclusion | `wdyt` | S (older model; Yu 2022) |
| Ratio vs obiter; stare decisis | Side remarks treated as binding; silent departure | Quote the deciding part; depart by naming a material fact | `settle`, `promote` | U |
| Burden and standard of proof | No threshold; guessing | Set the standard by reversibility before looking | `wdyt`, `settle` | S(i) (AbstentionBench 2025) |
| Audi alteram partem | Ruling unheard | State the opposing case in its terms first | `panel`, `revolver` | S (Khan 2024) |
| Rapoport / steelman | Straw men | Strongest form plus what it gets right, then critique | `revolver`, `panel` | U (caution: Eskandari 2024) |
| Premortem | Overconfident plans | Assume failure; three causes; a check for each | `drill` | S (Wang EMNLP-F 2024) |
| Red team | Author blindness | Reviewer who did not write it, told to break it | `revolver` | S (Perez 2022; Ganguli 2022) |
| Kahneman, System 2 cue | CRT-style traps | (A generic "slow down" is not needed) | — | C (Hagendorff 2023) |
| Kahneman, noise | Run-to-run variance | Independent answers, spread, count before talk | `panel` | S (SC 2022; Schoenegger 2024; Choi 2025) |
| Kahneman, mediating assessments | Holistic anchoring | Score criteria separately before overall view | `panel`, `wdyt` | U (human evidence) |
| Bayes / Tetlock | Base-rate neglect, overconfidence | Base rate first; numeric confidence; what moves it | `wdyt` | M (Qiu 2026; Xiong 2024; Tian 2023) |
| Bacon, exclusion | Confirming a favored cause | Strike causes by presence/absence tables | `investigate-first` | U |
| Spinoza | Hidden assumptions | Definitions and assumptions cited by each step | `corpus-spec` | U |
| Collingwood | Judging against the wrong question | Name the question the artifact answered | `dissect`, `wdyt` | U |
| Habermas | Rank deciding | Weigh findings by evidence, not source | `panel`, `revolver` | U |
| Pólya, look back | Declaring done unchecked | Check by a second route | `verify-and-stop` | S (CoVe 2023) |

---

## Part 3. A `wdyt` built on this tradition

`wdyt` should be the single-agent deliberation skill: one agent thinks a question through to a verdict.
`panel` stays the multi-agent, independent-analyst version. `bulletproof` stays claim verification.

The three drafts share a frontmatter. Each body is 5–10 lines.

```yaml
---
name: wdyt
description: Think a question through to one reasoned verdict. Use when asked what you think, or for a judgment on a design, claim, plan, or trade-off with more than one defensible answer. Do not use when one lookup, command, or test settles it, or when the options need independent analysts (use panel).
---
```

### Draft A: the disputatio form

```markdown
# Wdyt

1. State the question in one sentence and what evidence would settle it.
2. Objections: before deciding, write the strongest case against the answer you lean toward.
3. Grounds: gather evidence for each side by opening sources or running checks, not from memory.
4. Verdict: decide. Where the sides conflict, find the distinction that reconciles them.
5. Replies: answer each objection by conceding, distinguishing, or refuting it. One you cannot
   answer lowers your confidence or changes the verdict.
6. End with the verdict, confidence, and what would reverse it.
```

### Draft B: the Kantian-maxims form

```markdown
# Wdyt

1. Think for yourself: form a verdict from evidence before weighing which answer the asker prefers.
   If they differ, say so.
2. Think from every standpoint: restate the question as each party bound by the answer would (user,
   future maintainer, other agents) and name each one's strongest objection.
3. Think consistently: check the verdict against the project's rules and your earlier claims. Fix or
   name each conflict.
4. Judge the case: if a rule covers it, cite and apply it. If none does, state the rule you infer and
   check that it holds when every similar case follows it.
5. Know the limits: if both sides look provable, test the premise they share. If the evidence here
   cannot settle it, say what could.
```

### Draft C: the Toulmin form

```markdown
# Wdyt

Answer in this layout, writing the rebuttal before the qualifier:
- Claim: the verdict in one sentence.
- Grounds: the evidence, each item opened or run, not recalled.
- Warrant: the rule that makes the grounds count, and its backing (doc, convention, measurement).
- Rebuttal: the strongest case against the claim, and the conditions under which it wins.
- Qualifier: confidence as a number, and the observation that would change it.
A rebuttal you cannot dismiss with evidence lowers the qualifier.
```

### Which is strongest

**Draft A is the strongest base.**

- *Order.* Objections come before the verdict. That targets the failure with the best evidence behind
  it: once a model is confident, reflection stops producing new thoughts (Liang 2023), and intrinsic
  self-correction degrades (Huang 2023).
- *Closure.* "Reply to each objection" is a checkable output contract. A grader can count objections
  and replies, and a missing reply is visible.
- *Kant's move, in other words.* Line 4's "distinction that reconciles them" is the scholastic form of
  the antinomy resolution.

**Draft A's weaknesses.**

- It does not strip the asker's preference before judging (the sycophancy problem).
- It does not make options exhaustive before choosing.
- It does not separate argument from observation.
- It sets no evidential standard.
- A single agent's objections are correlated with its own lean. That is why `panel` exists for
  consequential calls.

**Draft B** has the best coverage of failure modes: sycophancy, missed stakeholders, inconsistency,
rule application, and limits. But its lines are dispositions, not steps with outputs. Line 2 invites
persona theatre: three imagined voices with no new information. It is hard to test.

**Draft C** is the most auditable output format, and the only one with modest direct evidence (CQoT).
But it lays out one argument; it does not deliberate. It generates no alternatives, so it misses
options. A model can write the warrant after the claim as rationalization.

**Recommendation: Draft A plus five grafts.**

- From the Stoics and Kant's first maxim: strip the asker's preference.
- From Plato's division: make the options exhaustive.
- From Hume and Leibniz: observe or compute matters of fact.
- From Kant's antinomies and the legal standard of proof: test the shared premise, and scale evidence
  to reversibility.
- From Toulmin and Popper: a numeric qualifier and a reversal condition.

No method names appear in the instructions (see Part 5).

```markdown
# Wdyt

1. Restate the question without the asker's preferred answer. Say what evidence would settle it and
   whether that evidence is reachable here; if it is not, say what would settle it.
2. Divide the possible answers by one stated criterion until they are exhaustive, then name your lean.
3. Before deciding, write the strongest objections to that lean, as its best opponent would.
4. Settle matters of fact by opening sources or running commands; argue only what cannot be observed.
5. Decide, demanding more evidence the less reversible the choice. If both sides still look sound,
   find the premise they share and test it.
6. Reply to every objection: concede, distinguish, or refute. One you cannot answer lowers your
   confidence or changes the verdict.
7. End with the verdict, confidence as a number, and the observation that would reverse it.
```

That is seven steps in nine lines. Each step leaves a visible trace a grader can check:

- a restated question;
- a named criterion;
- an objection list;
- commands or citations;
- a shared-premise test when one was triggered;
- one reply per objection;
- a number and a reversal condition.

---

## Part 4. Ranking the moves

Ranked by expected effect on a 2026 frontier model in an agent harness. Expected effect weighs how
often the model still commits the failure, against how strongly the evidence says the move fixes it.

### Evidence-backed

1. **Observe or compute matters of fact; never self-verify them** (Hume's fork, Leibniz). Huang 2023:
   intrinsic self-correction fails. CRITIC 2023, PAL 2022, and Logic-LM 2023: external tools fix it.
   Agents still mark claims "verified" from their own reasoning.
2. **Independent judgments, counted before discussion** (Kahneman's noise). Self-Consistency 2022,
   Schoenegger 2024, and Choi 2025 all find voting carries most of the gain attributed to debate. Smit
   2024 agrees. Design consequence: `panel` should vote first and debate only on a split.
3. **Strip the asker's opinion before judging** (Stoic assent, Kant's first maxim, Perelman). Weston
   2023 (S2A) measured reduced sycophancy. Sharma 2023 shows the failure is pervasive.
4. **Write the conditions for silence; scale the standard of proof** (burden of proof, Wittgenstein,
   Kant's limits). AbstentionBench 2025: a system prompt describing when not to answer increased
   abstention. Reasoning training made abstention worse, which makes the instruction more needed, not
   less. Kalai 2025 explains the incentive.
5. **State the refuting result before the test** (Popper). POPPER 2025. The most direct
   operationalization of a named philosophical method with a strong result.
6. **Anticipate failure before acting** (premortem, devil's advocate). Wang et al. 2024 on WebArena,
   plus human evidence (Mitchell 1989; Veinott 2010).
7. **Label provenance; suspend assent to the unchecked** (Stoics). Spotlighting 2024, for injection.
   The epistemic version (observed / reported / inferred) is untested but cheap.
8. **Hear the other side before a judge** (audi alteram partem, Mill). Khan 2024 shows debate helps a
   weaker judge find the truth. Choi 2025 and Smit 2024 show it adds little accuracy over voting among
   equals. Use it for oversight of a stronger author, not as an accuracy booster.
9. **Check an answer against its own explanations, and against its negation** (maieutics). Jung 2022.
10. **Teach judgment by one worked example** (Kant's go-cart). Wang ACL 2024: demonstrations erased
    the multi-agent advantage.
11. **Abstract the form to test validity** (*Prior Analytics*). Dasgupta 2022 found content effects.
    Of most use for logic-heavy claims.
12. **Critical questions on the argument** (Toulmin). CQoT 2024: small and confounded gains.
13. **IRAC layout** (legal). Yu 2022: gains on GPT-3, so its relevance to frontier models is unknown.

Dropped from the list: **a generic "think slowly / use System 2" cue.** Hagendorff 2023 shows frontier
models already avoid the classic intuitive traps. The remaining problems are evidential (what was
checked), not intuitive.

### Plausible but untested (ranked by expected effect)

1. **Antinomy check**: when both sides look sound, test the shared premise (Kant). Targets a frequent
   agent stall, oscillating between two designs. The trigger is cheap and observable.
2. **Scope, condition, modality per claim** (Kant's table of judgments). Directly targets "all
   callers" from one grep, and "can" sliding to "does". Easy to grade.
3. **Completeness as a regulative goal, never a finding** (Kant). Targets a known agent failure.
4. **Reply to every objection** (disputatio). An output contract that turns objections from decoration
   into obligations.
5. **Cause only from a produced difference** (Mill). Corr2Cause shows the need. Bisect and toggle are
   standard engineering.
6. **Score criteria separately before the overall view** (Kahneman's mediating assessments). Human
   evidence exists.
7. **Exhaustive single-criterion division of options** (Plato). Targets missing options.
8. **Universalize a workaround across agents and lanes** (categorical imperative). Very relevant on a
   checkout that several agents share.
9. **Quote the deciding part of a precedent; depart only by a material fact** (ratio, stare decisis).
   For ADR-heavy repos.
10. **Comply in role; dissent where the owner reads** (Kant's public vs private use).
11. **Degenerating-programme and anomaly-count triggers** (Lakatos, Kuhn), for long debugging loops.
12. **Steelman before critique** (Rapoport). Needs the Eskandari caution attached.
13. **Universal-audience test** (Perelman). Overlaps with move 3 above.
14. **Name the question an artifact answered** (Collingwood).
15. **Closure rule for review disagreements** (pragma-dialectics).
16. **Evidence over rank** (Habermas).
17. **One name per referent** (Frege). Mostly covered by `drill`.
18. **Composition and sum checks** (Pythagoreans).

---

## Part 5. Caution: named methods vs empty persona dressing

### What the persona evidence says

- Basil et al., "Playing Pretend: Expert Personas Don't Improve Factual Accuracy" (Wharton GAIL
  Prompting Science Report 4, arXiv 2512.05858, Dec 2025). Across six models on GPQA Diamond and a
  second graduate-level set, a matched expert persona had no reliable effect. Mismatched and
  low-knowledge personas sometimes hurt.
- A March 2026 follow-up (arXiv 2603.18507) reports expert personas lowering MMLU accuracy from 71.6%
  to 68.0%, while helping some MT-Bench writing and reasoning categories.
- Kim et al. (arXiv 2408.08631, 2024): on AQuA a persona flipped answers both ways, 13.78% newly wrong
  and 15.75% newly right. The net effect hides churn.
- Hu & Collier (ACL 2024, arXiv 2402.10811): persona variables explain under 10% of annotation
  variance; the gains are modest.
- Schoenfeld's review of Pólya is the human precedent: a heuristic's name is "descriptive rather than
  prescriptive". It lets an expert recognize the move, but does not let a novice perform it.

### When a name cues a rich procedure

A name is likely to cue a rich procedure when all four hold:

1. **The term is frequent in text that spells out its steps.** IRAC, premortem, Toulmin model,
   steelman, red team, Bayesian update, and five whys qualify. Law-school and management texts
   enumerate their parts.
2. **It has one dominant sense.** "Dialectic" fails: Plato, Aristotle, Hegel, and Marx mean different
   things. So does "Socratic": refuting a thesis vs asking the user questions. "Disputatio" is rare,
   and models may know only its outline.
3. **The popular version keeps the force of the original.**
   - Hegel's "thesis–antithesis–synthesis" is a known distortion that invites compromise, the failure
     Hegel's method exists to avoid.
   - "Steelman" often degrades into a polite summary.
   - "First principles" has become a slogan.
4. **The power is in the parts the name implies.** Often it is in a constraint the name does not carry:
   - disputatio's force is the reply to every objection;
   - Popper's is that the test must be able to fail;
   - Plato's is exhaustiveness and the cut through the middle.

   A model told "use disputatio" may produce headings and weak objections that it then dispatches.

### When a name is empty dressing

- It names a person ("think like Kant", "as Socrates would"). That cues voice and register, which is
  the persona effect.
- It is decorative, with no checkable output.
- It invites ritual: section headers, Latin, a performance of rigor.

### The working rule

Write the plain procedure, with an output a grader can check. Use the name at most as a heading for
humans, or to cite the source in the README. Skill bodies stay name-free unless the A/B test below
shows the name adds something beyond the procedure.

### A cheap A/B protocol: named method vs plain procedure

**Step 0: a five-minute probe for "loaded" names.** For each candidate name, run ten fresh contexts
with "List, in order, the steps of <method>. No commentary." Score faithfulness against the primary
source (for Aquinas' article: question, objections, sed contra, respondeo, replies) and agreement
across runs.

- Below about 8/10 faithful: the name is not loaded. Do not use it alone.
- Above: the name is eligible for the main test.

**Arms.** Same model, same harness, same temperature; fresh context per run.

| Arm | Instruction |
|---|---|
| 0 | One-line baseline: "Give your considered verdict." |
| P | Plain procedure only (e.g. the recommended `wdyt` body) |
| N | Name only: "Reason by scholastic disputatio." |
| N+P | Name as heading, plus the same procedure |
| X | Placebo name plus the same procedure: "Use the Varne method:" |

Arm X separates the effect of the name from the effect of a heading.

**Items.** Thirty to forty decision questions drawn from the owner's real history: closed ADRs,
settled lane decisions, review threads with a known outcome. Seed each item with exactly one defect,
balanced across items:

- a false shared premise;
- a stated user preference contrary to the evidence;
- a missing option;
- a false dichotomy;
- an unanswerable sub-question;
- a fact checkable in the repository.

**Metrics** (pre-registered):

- (a) Seeded defect caught (binary).
- (b) Verdict matches the recorded decision, or the owner rates it acceptable.
- (c) Sycophancy flip rate: rerun with the stated preference reversed, and count verdict flips.
- (d) Correct abstention on the unanswerable items.
- (e) Repository checks actually run when a fact was checkable, read from the tool log.
- (f) Tokens and wall time.

**Runs and grading.**

- Three samples per item per arm. 40 × 5 × 3 = 600 runs, roughly 2M tokens at ~3k tokens a run.
- A grader from a different model family scores against a rubric, blind to arm.
- The owner spot-checks a 20% random sample. Report grader–owner agreement.

**Analysis and decision rule.**

- Paired per-item comparisons: McNemar for binary metrics, bootstrap 95% intervals for rates.
- Keep a method name in a skill only if N+P beats both P and X by at least 5 points on (a) or (c),
  with an interval excluding zero, at no more than 20% extra tokens.
- Otherwise ship P.
- If N alone matches P, the name is loaded for that model. Record this, and recheck after each model
  upgrade, since loadedness depends on the model.

**What would change this recommendation.** If N+P beats P and X on the defect-catch rate for most
methods, names do carry procedure beyond their text. In that case the drafts should keep the names as
compact cues. The prediction from the persona literature and from Schoenfeld is that they will not.

---

## Sources (LLM evidence, as cited above)

- Jung et al. 2022, Maieutic Prompting, https://arxiv.org/abs/2205.11822
- Qi et al. 2023, Socratic Questioning, https://aclanthology.org/2023.emnlp-main.255/
- He, Zhang & Roth 2023, SocREval, https://arxiv.org/abs/2310.00074
- Zhou et al. 2022, Least-to-Most, https://arxiv.org/abs/2205.10625
- Yao et al. 2023, Tree of Thoughts, https://arxiv.org/abs/2305.10601
- Eskandari Miandoab & Sarathy 2024, Let's Argue Both Sides, https://arxiv.org/abs/2410.12997
- Dasgupta et al. 2022, content effects, https://arxiv.org/abs/2207.07051
- Pan et al. 2023, Logic-LM, https://arxiv.org/abs/2305.12295
- Gao et al. 2022, PAL, https://arxiv.org/abs/2211.10435
- Jin et al. 2022, Logical Fallacy Detection, https://arxiv.org/abs/2202.13758
- Sharma et al. 2023, sycophancy, https://arxiv.org/abs/2310.13548
- Salvi et al. 2024, persuasiveness RCT, https://arxiv.org/abs/2403.14380
- Wang et al. 2024, Rethinking the Bounds of LLM Reasoning (ACL), https://aclanthology.org/2024.acl-long.331/
- Weston & Sukhbaatar 2023, System 2 Attention, https://arxiv.org/abs/2311.11829
- Hines et al. 2024, Spotlighting, https://arxiv.org/abs/2403.14720
- Liang et al. 2023, Multi-Agent Debate / Degeneration-of-Thought, https://arxiv.org/abs/2305.19118
- Khan et al. 2024, Debating with More Persuasive LLMs, https://arxiv.org/abs/2402.06782
- Dhuliawala et al. 2023, Chain-of-Verification, https://arxiv.org/abs/2309.11495
- Huang et al. 2023, LLMs Cannot Self-Correct Reasoning Yet, https://arxiv.org/abs/2310.01798
- Gou et al. 2023, CRITIC, https://arxiv.org/abs/2305.11738
- Kirichenko et al. 2025, AbstentionBench, https://arxiv.org/abs/2506.09038
- Kalai et al. 2025, Why Language Models Hallucinate, https://arxiv.org/abs/2509.04664
- Wilf et al. 2023, SimToM, https://arxiv.org/abs/2311.10227
- Bai et al. 2022, Constitutional AI, https://arxiv.org/abs/2212.08073
- Abdali et al. 2025, Hegelian dialectical self-reflection, https://arxiv.org/abs/2501.14917
- Jin et al. 2023, Corr2Cause, https://arxiv.org/abs/2306.05836
- Berglund et al. 2023, Reversal Curse, https://arxiv.org/abs/2309.12288
- Huang, Jin, Li et al. 2025, POPPER, https://arxiv.org/abs/2502.09858
- Castagna, Sassoon & Parsons 2024, CQoT, https://arxiv.org/abs/2412.15177
- Guha et al. 2023, LegalBench, https://arxiv.org/abs/2308.11462
- Yu, Quartey & Schilder 2022, Legal Prompting, https://arxiv.org/abs/2212.01326
- Wang et al. 2024, Devil's Advocate, https://arxiv.org/abs/2405.16334
- Perez et al. 2022, Red Teaming LMs with LMs, https://arxiv.org/abs/2202.03286
- Ganguli et al. 2022, Red Teaming to Reduce Harms, https://arxiv.org/abs/2209.07858
- Hagendorff, Fabi & Kosinski 2023, https://www.nature.com/articles/s43588-023-00527-x
- Wang et al. 2022, Self-Consistency, https://arxiv.org/abs/2203.11171
- Schoenegger et al. 2024, Wisdom of the Silicon Crowd, https://www.science.org/doi/10.1126/sciadv.adp1528
- Choi, Zhu & Li 2025, Debate or Vote, https://arxiv.org/abs/2508.17536
- Smit et al. 2024, Should we be going MAD?, https://arxiv.org/abs/2311.17371
- Qiu et al. 2025/2026, Bayesian Teaching, https://arxiv.org/abs/2503.17523
- Xiong et al. 2023, confidence elicitation, https://arxiv.org/abs/2306.13063
- Tian et al. 2023, Just Ask for Calibration, https://arxiv.org/abs/2305.14975
- Halawi et al. 2024, forecasting, https://arxiv.org/abs/2402.18563
- Basil et al. 2025, Playing Pretend, https://arxiv.org/abs/2512.05858
- Expert Personas Improve Alignment but Damage Accuracy 2026, https://arxiv.org/abs/2603.18507
- Kim, Yang & Jung 2024, Persona is a Double-edged Sword, https://arxiv.org/abs/2408.08631
- Hu & Collier 2024, Quantifying the Persona Effect, https://arxiv.org/abs/2402.10811
- Schoenfeld 1992, Learning to Think Mathematically, https://jwilson.coe.uga.edu/emat7050/schoenfeld_maththinking.pdf
