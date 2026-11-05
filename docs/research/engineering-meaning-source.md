# Engineering Meaning (source report, as supplied by José on 2026-11-05)

Verbatim copy kept for verification. The enriched version is `engineering-meaning.md`.

## Philosophy, language, and independent judgment in human–LLM work

**Research review — 5 November 2026**

## Executive finding

The strongest version of this idea is not that developers need to become more eloquent, or replace conversational prompts with a universal pseudo-programming language. It is that **delegation through language requires deliberate control over meaning**: what is being requested, what is already agreed, what remains uncertain, what counts as evidence, and which decisions the agent is authorized to make.

The research connects five disciplines: philosophy clarifies concepts; pragmatics explains communication in context; psychology examines reliance and judgment; software engineering supplies composition and enforcement; empirical evaluation establishes whether the arrangement works.

This report distinguishes source findings from proposed applications. The examples and working methods are a synthesis, not an experimentally validated curriculum. The classical texts offer intellectual tools; they do not, by themselves, prove improvements in coding-agent performance.

## 1. Precision is selective, not exhaustive

“Make the upload system robust” is grammatical English. Its weakness is that “robust” conceals several possible requirements. A beautifully written paragraph can leave the same decisions unresolved.

A more useful statement is:

> A retry after a lost response must not create a second asset. A deliberate second upload must still work. Preserve existing permissions. Investigate the current request-identity mechanism before changing the public API.

The improvement is not literary sophistication. The sentence makes important distinctions visible while leaving implementation choices open.

There is unusually direct evidence for this distinction. Yang and colleagues’ *What Prompts Don’t Say*, published in Findings of ACL 2026, found that the tested models sometimes inferred omitted requirements, but underspecified prompts were twice as likely to regress under prompt or model changes. Crucially, explicitly adding every requirement did not consistently improve performance: requirements could conflict, and models could fail to follow the enlarged instruction set.[^1]

**The practical target is the smallest set of explicit commitments that prevents consequential misunderstanding—not the longest possible prompt.**

For engineering purposes, it helps to distinguish four different problems:

| What is unresolved? | Example | Appropriate response |
|---|---|---|
| **Ambiguity:** several readings are possible. | “Retry failed uploads” includes or excludes uploads whose outcome is unknown. | Separate the interpretations and settle the consequential difference. |
| **Underspecification:** a requirement is missing. | The retry policy says nothing about cancellation. | Discover whether cancellation matters and establish the requirement. |
| **Factual uncertainty:** the answer exists but is not known. | Does the service already support operation identifiers? | Inspect the implementation or run an experiment. |
| **Delegated discretion:** a choice is intentionally open. | Select an internal helper structure that fits existing conventions. | Let the agent choose within the agreed boundaries. |

This is a proposed working distinction. Treating all four as “bad prompting” leads either to unnecessary questions or to silent, unauthorized decisions.

A useful rhythm is **explore freely, commit explicitly, verify the consequences**. Brainstorming and execution need different levels of commitment. Tentative ideas should remain tentative until someone chooses them.

## 2. The missing layer is common ground

### Communication is an interaction, not a transmitted paragraph

Clark and Brennan’s *Grounding in Communication* describes communication as the joint establishment and updating of common ground: information participants treat as shared. Presenting a message is not the same as establishing that its intended meaning has been understood. The required level of understanding also depends on the purpose of the interaction.[^2]

Applied to agents, this changes the question from “Was my prompt clear?” to:

> What evidence do we have that the agent is operating on the same task, definitions, decisions, and revision that I am?

A reply of “Understood” provides little diagnostic information. A concrete interpretation is more useful:

> “I will treat a lost response as an unknown outcome, not a confirmed failure. I will verify that retrying preserves the operation identity and that a deliberate new upload receives a new one.”

That response can still be wrong. Its value is that it exposes a consequential distinction before implementation.

This concern is not merely theoretical. Zeng and colleagues’ ACL 2026 study examined 356 dialogues from 89 human–human, human–AI, AI–human, and AI–AI pairs performing a visual reference task. The evaluated models struggled to develop and reuse shared referring expressions smoothly. The experiment does not establish a universal limitation of coding agents, but it demonstrates that fluent dialogue and effective shared reference are different capabilities.[^3]

### A transcript is not an agreement register

An engineering application is to maintain a compact record of the current objective, settled decisions, unresolved questions, and evidence. It should distinguish an active decision from one superseded twenty messages ago.

This matters particularly when delegating to fresh agents. A new reviewer should not inherit the author’s persuasive self-assessment, but it still needs the accepted requirements. **Fresh perspective should remove endorsement, not erase the common ground needed to judge the work.**

Hila’s 2026 philosophical account describes LLMs as “asymmetrical communicative agents”: systems whose communicative behavior does not necessarily satisfy the intentional conditions of human communication. That is a philosophical position, not a settled finding about machine consciousness. Its practical relevance is that fluent exchange should not be mistaken for human-style commitment or accountability.[^4]

The working system must record and enforce those commitments rather than infer them from conversational tone.

## 3. What philosophy contributes in practice

### Definitions: identify what makes something the thing it is

In Plato’s *Meno*, Socrates pushes beyond lists of examples toward the common character that makes them instances of a concept. The transferable move is to ask what must remain true when particular examples change.[^5]

Consider a **lane**. Defining it as “a worktree, branch, draft PR, author, and reviewer” bundles one implementation. An investigation can be a useful lane without producing a PR.

A more durable definition might be:

> A bounded assignment with an identifiable owner, independent working state, and an explicit result to return.

Then the worktree and PR are mechanisms used when appropriate. A second terminal working on the same unbounded assignment is a useful counterexample: more windows do not automatically mean more lanes.

The lesson is not that software requires belief in Platonic Forms. It is that definitions should separate **essential properties from incidental packaging**.

### Practical meaning: explain what a distinction changes

Peirce’s *How to Make Our Ideas Clear* connects clarity with the conceivable practical consequences of a concept. Applied to development, “safe,” “simple,” and “production-ready” become useful only when we can explain what would count for or against them.[^6]

For example, “no duplicate uploads” is insufficient if a user is allowed to upload the same file twice. The intended distinction is between repeating an operation and intentionally starting another operation.

Writing that distinction down improves the instruction and exposes the author’s unfinished thinking. The agent did not need a more forceful adjective. The engineer needed a better account of the behavior.

### Pragmatics: provide enough context, not every available detail

Grice’s *Logic and Conversation* examines how relevance, informativeness, evidence, and manner support interpretation. It is a theory of conversation, not simply a checklist for concise prose.[^7]

Its useful engineering application is selective context. An implementation agent needs the agreed behavior, relevant constraints, and ways to inspect the code. It does not necessarily need the entire history of every abandoned idea.

Brevity is not the objective by itself. A short prompt that hides a critical exception is worse than a longer prompt that makes it visible. Conversely, a long historical transcript can obscure the decision that currently governs the work.

### Speech acts: distinguish a statement from an authorization

Searle’s classification of speech acts distinguishes different things people do through language, including asserting, directing, and committing. The same subject matter can appear in utterances with very different force.[^8]

A useful engineering adaptation is to mark the status of consequential statements:

    Observation: The second request uses a different identifier.
    Hypothesis: That difference causes the duplicate.
    Decision: Preserve the public API.
    Instruction: Reproduce the failure and investigate the identifier lifecycle.
    Authority: Edit and test locally; do not deploy.

These labels are not Searle’s taxonomy. They are a practical application of the distinction between what a sentence discusses and what it is doing.

“Probably unused” becoming “safe to delete” is a hidden change in evidential status. “We could deploy this” becoming “deploy it” is a hidden change in authority. A useful instruction system should make both changes visible.

### Argumentation: inspect the bridge between evidence and recommendation

Toulmin’s *The Uses of Argument* provides a framework for distinguishing a claim, its supporting grounds, the warrant connecting them, and qualifications or rebuttals.[^9]

Imagine an agent recommending a five-minute cache for permission checks. It supplies evidence that permissions rarely change. The missing warrant is that a five-minute delay in applying a change is acceptable. An immediate-revocation requirement defeats that warrant even if the statistics are correct.

The valuable question is therefore not only “Is the recommendation supported?” but **“Which assumption makes this evidence support that recommendation?”**

This is rhetoric serving inspection rather than persuasion. A well-arranged argument should make its weak point easier to find.

## 4. What current language research supports

### Clarify when the answer changes the work

ClarifyGPT, published at FSE 2024, investigates requirements clarification for code generation. It uses disagreement in candidate programs’ behavior to help identify ambiguity, then asks targeted questions. In its small human study, clarification improved benchmark performance. The tasks and sample were limited; it does not justify requiring a specification interview for every change.[^10]

Suri and colleagues’ Findings of ACL 2026 work makes a complementary distinction between uncertainty about the user’s specification and uncertainty in the model’s own predictions. Its clarification policy considers the expected benefit of a question against its cost.[^11]

Together, these suggest a useful rule: **ask about consequential preferences; investigate discoverable facts; preserve intentionally delegated choices**.

“Which database does this service use?” is usually a repository investigation. “May this migration discard historical records?” is a decision that cannot be manufactured from repository inspection.

### Precision often lives in small words

An instruction editor could start with ordinary linguistic hazards rather than inventing a new language. Compare “Only administrators may delete archived records” with “Administrators may delete only archived records.” The first restricts who may perform the action; the second restricts which records administrators may delete. Both are grammatical, but they express different policies.

Words such as “only,” “all,” “unless,” and “before” deserve attention because they change scope, exceptions, or ordering. Pronouns also need stable referents: “test it against the old version” leaves two objects to identify. “Run the regression test against the pre-fix commit” is more inspectable.

This is where grammar and diction become engineering tools. The useful distinction is not formal versus informal vocabulary; it is whether the sentence exposes the relationships that govern the action.

### A persona is not a reasoning procedure

Zheng and colleagues’ Findings of EMNLP 2024 study tested 162 personas across factual questions and several model families. Persona prompts did not provide a general performance improvement. A 2025 PLOS ONE study by de Araujo and Roth found that persona choices can change behavior, but their effects vary, and an apparent expert persona is not reliably the best choice.[^12][^13]

Neither study directly evaluates your multi-reviewer workflow. Their relevance is narrower: a prestigious role label is not enough to establish a useful method.

For a security stance, replace “be an exceptional security expert” with a concrete search task:

> Trace authorization at the changed entry points. Examine cross-tenant access and identifier substitution. For each finding, identify the affected path, triggering conditions, and evidence. Report no finding when the concern cannot be substantiated.

A stance should direct attention without predetermining the verdict. Otherwise “find security problems” becomes an invitation to manufacture them.

### Ambiguity diagnostics are emerging, but they are not type checking

Two recent directions are especially relevant to your proposed tooling:

**PRIG**, introduced by Ramesh and colleagues in June 2026, uses probes and attribution to locate ambiguous portions of prompts. Its evaluation includes synthetic tasks and human-written examples. Because the technique uses internal model representations, it is not a drop-in diagnostic for every hosted model.[^14]

**Detect Before You Disambiguate**, posted on 26 October 2026, studies ambiguity detection through controlled input perturbations. A key concern is that a rewriting method may choose one interpretation before ambiguity has been identified. Its experiments concern question answering, not a complete enterprise instruction language.[^15]

Both support separating diagnosis from rewriting. A prompt editor should be able to say “these two readings lead to different actions” rather than silently choosing the more plausible one.

Output agreement is also not proof of clarity: a model can consistently make the same incorrect assumption. Disagreement can reveal a problem without identifying its cause.

### Preserve useful context sensitivity

Controlled languages show what stronger guarantees require. Attempto Controlled English restricts construction and interpretation so that supported statements can map unambiguously to formal logic. Ordinary English with headings does not acquire that property merely by looking structured.[^16]

But removing all contextual inference would discard something valuable. Hota and Jokinen’s 2026 revised work on implicature-aware prompting found improvements in user evaluations when the system attended to implied communicative intent. Those evaluations concern perceived response quality, not proof of factual correctness or safe execution.[^17]

The promising division is therefore **flexible conversation for discovery, explicit commitments for consequential execution**.

Robustness still needs testing. Sclar and colleagues showed that meaning-preserving formatting changes could substantially alter performance in their evaluated settings. Semantically careful instructions are not automatically insensitive to model or presentation changes.[^18]

## 5. The psychological danger is plausible understanding

### Persuasion can outrun evidence

Two research findings complicate the idea that better prose necessarily means better reasoning.

Sharma and colleagues’ ICLR 2024 work documented sycophantic behavior in evaluated assistants and found that responses matching a user’s views could be preferred over accurate ones. Turpin and colleagues’ NeurIPS 2023 study showed that generated reasoning explanations could omit factors that actually influenced the answer.[^19][^20]

The practical risk is a feedback loop: the developer frames a favored answer, the model elaborates it fluently, and the developer treats that fluency as independent confirmation.

A better interaction makes the hypothesis contestable:

> My current explanation is that retries lose operation identity. What observation would show this explanation is wrong? Inspect that before choosing a fix.

Ask for checkable reasons—code locations, observed behavior, counterexamples, and test results. A convincing explanation is not a verified account of the model’s internal computation.

### Productive friction should be targeted

Buçinca, Malaya, and Gajos studied cognitive forcing functions in AI-assisted decision-making. Their 199-participant experiment found that interventions requiring more deliberate consideration could reduce overreliance compared with simpler explanation interfaces. The most effective interventions were not necessarily the most liked, and the study did not establish an overall human–AI team-performance improvement. This was not a coding-agent study.[^21]

More recent evidence is not uniformly positive. Ghosh and colleagues’ 2026 preprint examined assumption-checking and counterfactual prompts in AI-assisted writing with 214 participants. Although some comparisons favored assumption-checking, the corrected pairwise results did not establish a clear general advantage over no intervention, and adjusted analyses complicate the headline interpretation.[^22]

The defensible application is **selective friction at important decisions**, not forcing developers through a critical-thinking form for every small edit.

Before accepting an authorization redesign, state the governing constraint and test the proposed design against it. Before approving a straightforward rename, the ordinary diff and checks may be enough.

### Understanding requires some work by the learner

Chi and colleagues’ research on self-explanation found improved understanding when students generated explanations while studying. The experiment concerned school-level science, not professional developers, so applying it here is a teaching hypothesis rather than direct evidence.[^23]

The useful distinction is between reading the agent’s explanation and producing an explanation that you can defend. After a delegated change, predict what happens in one altered scenario, then follow the relevant code or run the case.

That is a more revealing test of understanding than asking whether the generated explanation sounded clear.

## 6. Finding the fourth option means changing the representation

An agent offers three ways to speed up a page: cache in the browser, cache at the edge, or cache in Redis.

All three share an assumption: the repeated work is necessary and should be cached. Another solution may be to eliminate a redundant request, change the query, reduce the requested data, or stop performing the operation on that interaction.

**The missing option is often outside the shared premise of the presented options.** It is not necessarily item four in a longer list of the same kind.

Peirce’s early treatment of hypothesis formation provides one philosophical foundation: propose an explanation, derive what would follow, and examine whether those consequences occur.[^24]

Cognitive psychology provides a more specific mechanism. Knoblich and colleagues’ four experiments on matchstick arithmetic supported a theory of insight involving changes to the problem representation: relaxing assumed constraints and decomposing elements previously treated as indivisible. These were laboratory problems, not software-design decisions, but they offer a concrete account of what “think outside the box” can mean.[^25]

For engineering, the corresponding questions are: Which constraints came from the requirement, and which did we add? What have we treated as one operation that could be separated? What changes if responsibility moves to another layer?

### Use analogy to transfer relationships, not surface features

Gentner’s structure-mapping theory treats useful analogy as a mapping of relationships between domains rather than superficial similarities between objects.[^26]

Your analogy between skills and software modules is valuable because both raise questions about dependencies, shared definitions, interfaces, and composition. It does not follow that skills must inherit every feature of object-oriented programming.

Similarly, triangles and squares do not logically entail that a circle is the missing answer. The useful move is to notice the category organizing the examples and explore what lies beyond it. Analogy generates candidates; evidence decides among them.

### More alternatives do not guarantee a wider search

Kostiuk, Seyfried, and Reed’s 2025 alternative-generation study found useful novel suggestions from the tested models, but also omissions relative to human advice. Its material came from advice questions and smaller models, so it is not a direct estimate of modern coding agents’ design ability.[^27]

Doshi and Hauser’s 2024 short-story experiment offers another warning: AI assistance improved judged individual creativity while reducing diversity across the resulting stories. That does not prove that architecture recommendations converge in the same way, but it motivates testing whether repeated requests for options produce genuinely different approaches.[^28]

A proposed working habit is to write a short independent account of the goal and constraints before reading the recommendation. Then identify what the offered options assume in common, propose a different causal explanation, and choose an experiment that separates them.

Sometimes the original recommendation survives that process. The objective is better judgment, not ritual disagreement with the model.

## 7. Composable skills need preserved meaning, not just reusable text

Your `delegate` and `revolver` example reveals two different engineering tasks: sharing the definition of a procedure, and preserving that definition when agents execute it.

A possible division is:

| Component | Responsibility |
|---|---|
| **Lane** | The assignment’s identity, working state, candidate revision, and relevant resources. |
| **Stance** | A focused review concern, investigation questions, and standards for a finding. |
| **Revolver** | Apply selected stances to the same candidate and combine supported findings. |
| **Delegate** | Coordinate implementation, verification, review, repair, and escalation. |

This is a proposed design, not an established standard. Its important property is that `delegate` depends on the review result’s contract, rather than containing a second independently maintained copy of `revolver`.

**Define once at the source; supply wherever needed at execution.** Several isolated reviewers may each require the same evidence standard. Repeating the authoritative definition in their separate contexts is different from maintaining several competing versions of it.

Scope matters too. A `/tldr` micro-skill should identify its source material, length target, required preservation of uncertainty, and lifetime. “Apply only to this answer” prevents a local formatting preference from quietly becoming a permanent conversational policy. Its stable property is the instruction policy, not an identical answer regardless of context.

### What should become formal?

References, arguments, versions, permissions, result shapes, and sequencing are good candidates. Substantive judgment often remains better expressed through natural language and examples.

MetaSkill, posted on 17 October 2026, formalizes ordering and data bindings between skills while leaving local instructions in natural language. Its small evaluation supports the value of explicit coordination, but does not establish that correctly ordered steps solve the right problem. SkillCompiler, posted on 29 October, likewise separates operations suitable for programmatic compilation from context-dependent reasoning. Both are recent preprints.[^29][^30]

This is compatible with rejecting “the LLM as a reliable compiler.” A runtime can enforce which reviewer sees which revision without proving that the reviewer’s conclusions are correct.

### Authority cannot depend on wording alone

The difference between an instruction and quoted data also needs technical support. StruQ, published at USENIX Security 2025, combines a structured front end with specially trained model behavior to separate instructions from data and resist prompt injection. Its results do not mean that placing Markdown labels around untrusted content provides the same protection.[^31]

A useful instruction environment would therefore distinguish **structural errors** it can establish, **meaning warnings** that need interpretation, and **behavioral failures** observed during execution. None should masquerade as the others.

## 8. A research programme worth testing

The sources reviewed here do not establish that teaching developers philosophy directly improves agent-assisted delivery. They support individual mechanisms: requirement discovery, grounding, focused clarification, assumption inspection, and better separation of instructions from data. The combined practice needs its own evaluation.

A practical investigation should compare ordinary task handoffs with three deliberately separated changes: clearer requirements using the same format; more structure without additional requirements; and a short grounding exchange that exposes interpretations before execution. This helps determine whether any improvement comes from content, presentation, or interaction rather than treating them as one intervention.

Use representative tasks containing an ambiguous requirement, an unstated constraint, an inspectable repository fact, and a legitimate open implementation choice. Keep tools and model settings comparable. Have independent reviewers establish acceptance criteria before examining results. Test held-out tasks rather than repeatedly tuning on the same examples.

The useful outcomes are accepted behavior, unauthorized decisions, missed requirements, clarification burden, human repair time, and the developer’s ability to explain the result. Token cost belongs in that comparison; it is not a substitute for it.

For the “fourth option,” compare decisions made after seeing the model’s menu with decisions preceded by an independent problem framing. Include cases where the menu omits a strong alternative and cases where the recommended option is already best. Reward correct discrimination, not the production of another idea.

For reusable skills, test combinations as well as individual components. A reviewer that behaves well alone may behave differently when another skill adds repair authority, deadline pressure, or conflicting instructions. Track the expanded instructions each agent actually receives.

This would turn the proposed discipline into an engineering practice that can improve from evidence. The question is not whether the terminology sounds philosophical. It is whether the approach produces clearer decisions, more faithful execution, and less avoidable rework.

## Conclusion

The most useful boundary is not between “casual prompting” and “formal prompting.” It is between **unexamined interpretation and inspectable meaning**.

Philosophy helps define the concepts and question the frame. Pragmatics explains how meaning becomes shared. Psychology warns that fluency, agreement, and explanation can be mistaken for understanding. Software engineering makes the enforceable parts explicit. Evaluation determines whether the whole arrangement works.

The human contribution is not merely to choose from an agent’s menu. It is to establish what problem deserves solving, distinguish evidence from assumptions, and notice when the menu is organized around the wrong question.

## References

Classical works and theoretical frameworks are identified separately from experiments, technical systems, and recent preprints. References support the attributed findings; the engineering examples and proposed practices are this report’s synthesis.

[^1]: Chenyang Yang, Yike Shi, Qianou Ma, Michael Xieyang Liu, Christian Kaestner, and Tongshuang Wu. “What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts.” Findings of ACL, 2026, pp. 9072–9101. https://aclanthology.org/2026.findings-acl.441/
[^2]: Herbert H. Clark and Susan E. Brennan. “Grounding in Communication.” In Perspectives on Socially Shared Cognition, 1991. https://web.stanford.edu/~clark/1990s/Clark%2C%20H.H.%20_%20Brennan%2C%20S.E.%20_Grounding%20in%20communication_%201991.pdf
[^3]: Peter Zeng et al. “LVLMs and Humans Ground Differently in Referential Communication.” ACL, 2026, pp. 9061–9087. https://aclanthology.org/2026.acl-long.410/
[^4]: Angjelin A. Hila. “Communicative Action in the Age of Artificial Intelligence: Theorizing LLMs as Communicative and Strategic Agents.” Philosophy & Technology 39, article 159, 2026. https://link.springer.com/article/10.1007/s13347-026-01168-4
[^5]: Plato. Meno. Trans. Benjamin Jowett. https://classics.mit.edu/Plato/meno.html
[^6]: Charles S. Peirce. “How to Make Our Ideas Clear.” Popular Science Monthly, 1878. https://web.stanford.edu/class/history34q/readings/Peirce/Peirce_MakeOurIdeasClear.html
[^7]: H. P. Grice. “Logic and Conversation.” Syntax and Semantics, vol. 3, 1975. https://web.stanford.edu/class/psych205/papers/Grice-1975.pdf
[^8]: John R. Searle. “A Classification of Illocutionary Acts.” Language in Society 5(1), 1976, pp. 1–23. https://www.cambridge.org/core/journals/language-in-society/article/abs/classification-of-illocutionary-acts1/C51AB2FEB1BFD115FE9B066A8669789D
[^9]: Stephen E. Toulmin. The Uses of Argument, ch. III, “The Layout of Arguments.” 1958; updated 2003. https://www.cambridge.org/core/books/abs/uses-of-argument/layout-of-arguments/0CF09834F2802518330E754858CC0655
[^10]: Fangwen Mu et al. “ClarifyGPT: A Framework for Enhancing LLM-Based Code Generation via Requirements Clarification.” FSE 2024. https://doi.org/10.1145/3660810
[^11]: Manan Suri, Puneet Mathur, Nedim Lipka, Franck Dernoncourt, Ryan A. Rossi, and Dinesh Manocha. “Structured Uncertainty guided Clarification for LLM Agents.” Findings of ACL, 2026. https://aclanthology.org/2026.findings-acl.2028/
[^12]: Mingqian Zheng, Jiaxin Pei, Lajanugen Logeswaran, Moontae Lee, and David Jurgens. “When ‘A Helpful Assistant’ Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models.” Findings of EMNLP, 2024. https://aclanthology.org/2024.findings-emnlp.888/
[^13]: Pedro Henrique Luz de Araujo and Benjamin Roth. “Helpful assistant or fruitful facilitator? Investigating how personas affect language model behavior.” PLOS ONE 20(6), e0325664, 2025. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0325664
[^14]: Govind Ramesh, Yao Dou, and Wei Xu. “Localizing Prompt Ambiguity in Large Language Models with Probe-Targeted Attribution.” 2026. https://arxiv.org/abs/2606.05486 ; https://aclanthology.org/2026.findings-emnlp.2103/
[^15]: Tiejin Chen et al. “Detect Before You Disambiguate: Perturbation-Based Input Ambiguity Detection in LLMs.” 26 October 2026. https://arxiv.org/abs/2610.36353
[^16]: Norbert E. Fuchs. “Attempto Controlled English.” https://nlp.stanford.edu/nlaspAbs/fuchs.shtml
[^17]: Asutosh Hota and Jussi P. P. Jokinen. “Implicature in Interaction: Implicature-Aware Prompting Improves User Evaluations of LLM Responses.” 2026. https://arxiv.org/html/2510.25426v2 ; https://doi.org/10.1080/10447318.2026.2720982
[^18]: Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. “Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design.” ICLR 2024. https://arxiv.org/abs/2310.11324
[^19]: Mrinank Sharma et al. “Towards Understanding Sycophancy in Language Models.” ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html
[^20]: Miles Turpin, Julian Michael, Ethan Perez, and Samuel R. Bowman. “Language Models Don’t Always Say What They Think.” NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html
[^21]: Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos. “To Trust or to Think.” CSCW 2021. https://arxiv.org/abs/2102.09692
[^22]: Ahana Ghosh, Advait Sarkar, Siân Lindley, and Christian Poelitz. “An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing.” 2026. https://arxiv.org/html/2601.18033v1
[^23]: Michelene T. H. Chi, Nicholas de Leeuw, Mei-Hung Chiu, and Christian LaVancher. “Eliciting Self-Explanations Improves Understanding.” Cognitive Science 18(3), 1994. https://asu.elsevierpure.com/en/publications/eliciting-self-explanations-improves-understanding/
[^24]: Charles S. Peirce. “Deduction, Induction, and Hypothesis.” Popular Science Monthly, 1878. https://en.wikisource.org/wiki/Popular_Science_Monthly/Volume_13/August_1878/Illustrations_of_the_Logic_of_Science_VI
[^25]: Günther Knoblich, Stellan Ohlsson, Hilde Haider, and Detlef Rhenius. “Constraint Relaxation and Chunk Decomposition in Insight Problem Solving.” JEP:LMC 25(6), 1999. https://doi.org/10.1037/0278-7393.25.6.1534
[^26]: Dedre Gentner. “Structure-Mapping: A Theoretical Framework for Analogy.” Cognitive Science 7(2), 1983. https://groups.psych.northwestern.edu/gentner/papers/Gentner83.2b.pdf
[^27]: Yevhen Kostiuk, Clara Seyfried, and Chris Reed. “Automating Alternative Generation in Decision-Making.” Findings of EMNLP, 2025. https://aclanthology.org/2025.findings-emnlp.1/
[^28]: Anil R. Doshi and Oliver P. Hauser. “Generative AI enhances individual creativity but reduces the collective diversity of novel content.” Science Advances 10, eadn5290, 2024. https://doi.org/10.1126/sciadv.adn5290
[^29]: Meng Shu et al. “Where Natural Language Ends in Agents: Executable Skill Composition with MetaSkill.” 17 October 2026. https://arxiv.org/abs/2610.24723
[^30]: Chengyu Yang et al. “Compile Away Uncertainty: Self-Evolving Agent Skills via Programmatic Compilation.” 29 October 2026. https://arxiv.org/abs/2610.39508
[^31]: Sizhe Chen, Julien Piet, Chawin Sitawarin, and David Wagner. “StruQ: Defending Against Prompt Injection with Structured Queries.” USENIX Security 2025. https://www.usenix.org/conference/usenixsecurity25/presentation/chen-sizhe
