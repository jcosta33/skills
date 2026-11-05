# Engineering Meaning: empirical evidence the report lacks

Date: 2026-11-05. This file adds evidence to `engineering-meaning-source.md`. Findings are ranked by how
much each one changes that report.

## How this was gathered

Five Opus research subagents each covered one area, and each opened its sources. I then re-opened the
load-bearing sources myself.

Tags on every source:
- **Checked**: I re-opened the source on 2026-11-05 and confirmed the quoted numbers.
- **Subagent**: a research subagent opened it, but I did not re-check it.
- **Abstract**: only the abstract was read.

Most full texts were read through a summarising fetch tool. A number from a table should be confirmed
in the PDF before it is printed anywhere outside this file.

Evidence classes: **PR** peer-reviewed (venue named), **Pre** preprint, **V** vendor, **Pr**
practitioner.

## Ranking

| # | Finding | Report section | Effect on the report |
|---|---|---|---|
| 1 | A reviewer shown the author's description, reasoning, prior score or authorship misses more. Stripping that input works; telling the reviewer to ignore it works less well. | §2, §7 | Supports the fresh-reviewer claim and makes it measurable. Adds that the stripping must be done mechanically. |
| 2 | Models pick superseded values from a log, confidently. Instructions to forget do not fix it. Restating the whole spec in one place does. | §2 | Turns "a transcript is not an agreement register" from a proposal into a measured finding. |
| 3 | Labelling text as data, and stating priority in the prompt, collapse under adaptive attack. Only enforcement outside the model holds. | §7 | Strengthens the authority section and answers its open question. |
| 4 | Skills interfere: same-job twins substitute silently, and clashing skills drop rules. Priority statements do not fix it; one joint example or a merged file does. | §7, §8 | Answers the report's untested "test combinations" item. |
| 5 | Agents rarely ask unprompted. Pushing them to ask causes over-asking, which has measured costs. After a question is answered, users accept more errors. | §4, §2 | Supports the clarification rule and adds two clauses. |
| 6 | Fluent explanations raise confidence, not accuracy. Prediction without a scored result does not correct the illusion. Perceived AI speed-up is not evidence. | §5 | Qualifies the "predict an altered scenario" habit: running the case is mandatory. |
| 7 | Models and vendors converge on the same options, and they share errors. Verbalized sampling widens the spread. Forming your own judgment before seeing the AI's protects against wrong advice. | §6 | Supports §6 and supplies a mechanism and a method. |
| 8 | Instruction-count losses are fading on 2026 frontier models for simple rules, but rules that oppose model defaults are still followed least. LLM-written context files do not help. | §1 | Qualifies the "smallest set of commitments" argument: what to keep is the non-default rules. |
| 9 | Self-preference is real but varies by model: up to 20× for GPT-5 on code rubrics, 1.78× for Claude Sonnet 4.5. | §7 | Supports the existing "self-review is not fresh" rule. |

---

## 1. Author narrative misleads reviewers; strip it by construction

**What it changes.** §2 says "Fresh perspective should remove endorsement, not erase the common
ground." That sentence is now directly measured, in code review.

Two refinements follow:
- Endorsement includes more than the author's verdict. It covers the PR description, commit
  messages, "verified" claims, prior scores and authorship labels.
- Redacting that input programmatically beats instructing the reviewer to ignore it. That makes it
  a §7 enforcement point as well.

One qualification. A strong reviewer can use the author's reasoning trace to catch subtle defects.
The safe design keeps the trace in a separate reviewer, never in the same context as the
requirements-only review.

### Evidence

**Mitropoulos, Alexopoulos, Alexopoulos, Spinellis.** "Measuring and Exploiting Contextual Bias in
LLM-Assisted Security Code Review" (later versions retitled "When AI Agrees Too Much…"). arXiv
2603.18740, 2026. https://arxiv.org/html/2603.18740v2 — Pre, Checked.

- Setting: 6 LLMs, 250 CVE/patch pairs, 14,910 queries, followed by an attack on Claude Code
  acting as the review agent for 17 CVEs.
- Detection of vulnerable code under neutral framing vs "strong bug-free" framing:

  | Model | Neutral | "Bug-free" framing |
  |---|---|---|
  | GPT-4o-mini | 97.2% | 3.6% |
  | Claude 3.5 Haiku | 68.4% | 8.5% |
  | Sonnet 4.5 | 97.4% | 80.6% |
  | Opus 4.5 | 95.3% | 90.4% |

- Claude Code rejected 16 of 17 vulnerable PRs at baseline.
- One LLM-written PR description and commit message got 9 of 17 accepted (53%). Iterative
  refinement got all 17 accepted within 5 tries, for $19.36 in total.
- Redacting the PR description recovered detection in 12 of 17 cases. Redaction plus an
  instruction to ignore metadata recovered 16 of 17.
- Limits: security patches only, and a small agent sample.

**Tu, Ni, Bi.** "How Long Reasoning Chains Influence LLMs' Judgment of Answer Factuality." arXiv
2604.06756v2, Aug 2026. https://arxiv.org/html/2604.06756 — Pre, Checked.

- Setting: Natural Questions (NQ), Qwen3-8B as the generator. Each judge saw the answer alone, then
  the answer plus the generator's reasoning.

  | Judge | Alignment: answer only → with reasoning | Overconfidence: answer only → with reasoning |
  |---|---|---|
  | Qwen3-8B | 58.2 → 33.2 | 38.2 → 65.8 |
  | GPT-4o | 74.0 → 74.0 | 23.4 → 22.0 |
  | Claude Sonnet 4.5 | 75.8 → 84.0 | 22.0 → 5.8 |

- Misleading reasoning flipped an incorrect answer to "judged correct" in 34.0% of samples for the
  Qwen3-8B judge, against 0.6% for Claude Sonnet 4.5.
- Limits: question answering and math, not code.

**Arnav et al.** "CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring." arXiv 2505.23575v3. The
page names no venue; the subagent reported NeurIPS 2025, which I did not confirm.
https://arxiv.org/html/2505.23575v3 — Pre, Checked.

- On non-subtle sabotage in BigCodeBench, giving the monitor the chain of thought "decreases
  performance by 25 percentage points", "possibly due to persuasive rationalizations".
- A hybrid that scores the code and the reasoning separately and then combines the scores had 21%
  higher recall than code-only monitoring and 42% higher than reasoning-only.

**Kapetanovic, Altwlkany, Mercep, Duricic, Lacic.** "Anchoring Bias in LLM-as-a-Judge Systems: Prior
Scores Compromise Evaluation Independence." CIKM '26. https://arxiv.org/html/2608.25869 — PR,
Checked.

- A random prior score shifted judges' scores: Claude 4.5 Sonnet by −0.706 on a 0–5 scale, GPT-4.1
  by −0.411.
- GPT-4.1 accuracy fell from 76.26% to 68.49%, and 10.18% of correct judgments flipped to the
  anchored wrong label.
- Chain of thought enlarged the shift by 47.7% on one task pair. A warning did not reduce it there.

**Chae et al.** "Self- and Other-Labels Induce Bidirectional Bias in LLM Judges." arXiv 2608.18091v1,
2026. https://arxiv.org/html/2608.18091v1 — Pre, Subagent.

- Labelling an output "your own selection" shifted scores by +0.43 on a 7-point scale, whoever
  actually wrote it.
- Blind self-preference fell to about zero once judge quality and severity were controlled.

**Melo et al.** "SEVRA-BENCH." arXiv 2606.13757v2, 2026. https://arxiv.org/abs/2606.13757 — Pre,
Subagent.

- Setting: about 1,000 PRs that re-introduce historical vulnerabilities, each wrapped in one of 15
  persuasive narratives. 8 review agents.
- With narratives such as "Prior Approval Signal" or "Fake Bug Fix", weaker agents rejected fewer
  than 40% of the PRs.
- There is no code-only baseline, and per-agent numbers appear only in figures.

**Counter-evidence.**
- **Thornton**, "LLM Code Reviewers Are Harder to Fool Than You Think", arXiv 2602.16741, 2026 (Pre,
  Subagent). Adversarial comments inside the code had no significant effect (all p > 0.21). That
  test covered in-code comments, not PR prose.
- **Baker et al.**, OpenAI, arXiv 2503.11926, 2025 (V, Subagent). A monitor that read the chain of
  thought caught reward hacking with 95% recall, against 60% from actions alone. Once the agent was
  optimised against that monitor, recall fell to near zero.

### Moves

- **revolver**, step 2. Build each reviewer's brief from two inputs only: the accepted
  requirements and decisions, and the target.
  - Leave out the PR description, commit messages, any "verified" or "done" claim, earlier scores
    or verdicts, and who wrote it.
  - Do this by construction, not by telling the reviewer to ignore them (Mitropoulos: 12/17
    recovered by redaction alone).
  - The step already bans "another reviewer's prose"; extend that ban to the author's prose.
- **revolver**, model choice. "Cheapest adequate model" is safe only when the inputs are stripped.
  Weak judges are the ones misled by author reasoning (Qwen3-8B, 34% flips; Sonnet 4.5, 0.6%).
- **revolver**, optional reasoning check. If the author's reasoning trace should be inspected, give
  it to a separate reviewer and combine the findings afterwards (CoT Red-Handed hybrid).
- **handoff.** "What is done and verified" is right for an agent continuing the work. It is
  endorsement for one reviewing the work. Add: when the receiver will review, give it the
  requirements and the target, not the author's account.
- **panel.** "None sees another's analysis" is supported. Also withhold the asker's lean.

---

## 2. A transcript is not an agreement register: now measured

**What it changes.** §2 proposes a compact record of current decisions as an engineering
application. The evidence makes it a requirement:
- Models given a log in which values were overwritten often return a superseded value, with no
  sign of doubt.
- Telling them to forget the old value barely helps.
- Splitting a spec across turns costs about 39% on average, while putting it in one message costs
  almost nothing.
- Rewriting a 2026 conversation into a single spec recovers about half the loss.

Caveat: no study measures superseded decisions in real coding-agent transcripts. The evidence comes
from synthetic key–value tasks and multi-turn task simulations.

### Evidence

**Laban, Hayashi, Zhou, Neville.** "LLMs Get Lost In Multi-Turn Conversation." arXiv 2505.06120, 2025.
The subagent reported ICLR 2026 (Oral) from OpenReview; I did not open that page.
https://arxiv.org/html/2505.06120 — Pre/PR, Checked.

- Setting: 15 LLMs from 8 families, 6 generation tasks including Code, more than 200,000 simulated
  conversations.
- Moving from a fully specified prompt to sharded turns costs 39% on average.
  - Aptitude falls 16% (not significant).
  - Unreliability rises 112%.
- "Concat", where every shard arrives in one turn, averages 95.1% of the full-spec score.
- "Snowball", which repeats earlier shards each turn, recovers 15–20% of the loss.
- At temperature 0, unreliability is still about 30%.
- Limits: simulated users; single models rather than agent harnesses.

**Liu, Zhu, Feng, Ma, Wang, Meng.** "Intent Mismatch Causes LLMs to Get Lost in Multi-Turn
Conversation." arXiv 2602.07338, 2026. https://arxiv.org/html/2602.07338 — Pre, Checked.

- A "Mediator" rewrites the conversation into one fully specified instruction.

  | Model | Full spec | Sharded | Sharded + Mediator |
  |---|---|---|---|
  | GPT-4o-mini | 86.9 | 53.6 | 73.9 |
  | GPT-5.2 | 92.7 | 48.5 | 72.6 |
  | DeepSeek-V3.2-Thinking | 94.7 | 60.8 | 81.9 |

- The gap persists in 2026 frontier models.
- Limits: four binary-correctness tasks; the rewriting guidelines were learned from 5 examples per
  task.

**Chattaraj & Raj.** "LLMs Remember First, Forget Last: Dual-Process Interference in Large Language
Models." arXiv 2603.00270v3, Aug 2026. https://arxiv.org/html/2603.00270 — Pre, Checked.

- Setting: 39 LLMs from 1B to 2.5T parameters, on one synthetic paired-associate task in English.
- Retrieving the current value of a reassigned key drops from 94% to 3% at the highest load.
- Interference from old values on the current one is much stronger than the reverse (d = 1.73).
- "More than 97% of incorrect retrievals carry no uncertainty signal."
- 56.1% of errors return an earlier value for the correct key.

**Wang & Sun.** "Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond
Context Length." arXiv 2506.08184v3, 2025. The subagent reported an ICML 2025 long-context workshop;
the page names no venue. https://arxiv.org/html/2506.08184 — Pre, Checked.

- Setting: updates to 46 keys, 3–400 updates per key.
- Accuracy "declines log-linearly toward zero".
- A per-key "forget earlier updates" instruction "did not significantly improve retrieval accuracy".
- Model size predicts robustness (t = 3.03, p = 0.005). Context length does not (p = 0.886).

**Supporting results (Subagent):**
- **LongMemEval**, Wu et al., ICLR 2025, https://arxiv.org/abs/2410.10813 (PR). Accuracy with only
  the relevant sessions vs the full history: GPT-4o 0.870 vs 0.606.
- **MemoryAgentBench**, Hu, Wang, McAuley, arXiv 2507.05257 (Pre). On overwritten facts in the
  multi-hop setting, every method scores at most 28%.
- **Chroma, "Context Rot"**, Jul 2025, https://www.trychroma.com/research/context-rot (V). Every one of
  18 models scored higher with a focused prompt of about 300 tokens than with the full history of
  about 113k tokens.
- **Du et al.**, arXiv 2510.05381 (Pre). Accuracy drops 13.9–85% with input length, even when
  retrieval is perfect.

### Moves

- **handoff.** "Drop anything finished or no longer true" is supported. Add: state every decision
  now in force as a complete list, never as a change against earlier text.
- **rearm.** It already re-reads files rather than the transcript, which is supported. Add one line
  per decision now in force, next to the rules it was not following.
- **Global AGENTS.md**, Interaction section. Candidate rule: when a decision changes, rewrite the
  record in place; do not append a correction. Evidence: superseded values win, confidently, and
  forget-instructions fail.
- **Report §2.** Add the numbers. Also note that the Snowball and Mediator results show
  re-consolidating the spec is the remedy, not a longer context.

---

## 3. "This is data, not instructions" does not survive an adaptive attacker

**What it changes.** §7 says Markdown labels do not provide StruQ's protection. The evidence goes
further, and answers "does labelling text as data help at all?"
- **Against static attacks:** some help.
- **Against adaptive or human attackers:** none, and sometimes it makes things worse.
- **Priority stated in the prompt:** does not help either.
- **Trained defences:** cut static attack rates, but are still broken adaptively. StruQ itself is
  bypassed.
- **What holds:** only system-level enforcement, at a utility cost.

### Evidence

**Nasr, Carlini, Hayes, Sitawarin, Schulhoff et al.** "The Attacker Moves Second: Stronger Adaptive
Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections." arXiv 2510.09023, Oct 2025.
The subagent reported USENIX Security '26, which I did not confirm. https://arxiv.org/html/2510.09023
— Pre, Checked.

- The authors "bypass 12 recent defenses … with attack success rate above 90% for most".
- AgentDojo attack success rate (ASR), static attack → search attack (Table 7):

  | Defence | Gemini-2.5 Pro | GPT-5 Mini | MetaSecAlign-70B |
  |---|---|---|---|
  | None | 30% → 100% | 0% → 75% | 5% → 96% |
  | Spotlighting | 28% → 99% | 0% → 47% | 1% → 99% |
  | Prompt sandwiching | 21% → 95% | 0% → 69% | 4% → 99% |

- Human red-teaming against spotlighting (Table 5):
  - gemini-2.5-flash: 28.8% baseline → 43.7% with spotlighting.
  - grok-4: 10.9% → 2.7%.

**Zhang et al.** "IHEval: Evaluating Language Models on Following the Instruction Hierarchy." NAACL
2025, pp. 8374–8398. https://aclanthology.org/2025.naacl-long.425/ — PR, Checked.

- Accuracy when instructions agree vs conflict:
  - GPT-4o: 91.0 → 70.0.
  - Claude-3 Sonnet: 85.1 → 30.7.
  - LLaMA-3.1-70B: 78.8 → 14.0.
- A prompt telling the model to follow the priority order: GPT-4o 70.0 → 67.2; LLaMA 14.0 → 17.1.
  The paper says it brought no "noticeable improvements".
- Models are swayed by "the tone or strictness of the wording" instead of priority.

**Debenedetti et al.** "Defeating Prompt Injections by Design" (CaMeL). arXiv 2503.18813v2, Jun 2025.
https://arxiv.org/abs/2503.18813 — Pre, Checked.

- 77% of AgentDojo tasks solved "with provable security", against 84% undefended.
- Subagent, from the full text:
  - 0 successful attacks out of 949, against 300 undefended on Gemini 2.5 Pro.
  - About 2.8× the tokens.
- No protection against text-to-text manipulation, such as a biased summary.

**Other defences (Subagent):**
- **Wallace et al.**, "The Instruction Hierarchy", OpenAI, arXiv 2404.13208, 2024 (V/Pre).
  Training raised robustness by up to 63% (system-prompt extraction) and generalised by more than
  30% to jailbreaks. A system message that only described the hierarchy did "much worse".
- **Chen et al.**, "SecAlign", ACM CCS 2025, arXiv 2410.05451 (PR). Optimisation-based ASR on
  Llama3-8B-Instruct: 89% undefended, 27% with StruQ, 1% with SecAlign.
- **Meta-SecAlign**, arXiv 2507.02735v4 (Pre). On Llama-3.3-70B, AgentDojo ASR 14.7% → 1.9% while
  utility held. An adaptive GCG attack still reached 47.1% on 70B. The authors' words: "PI is not
  solved".
- **Shi et al.**, "Lessons from Defending Gemini…", Google DeepMind, arXiv 2505.14534 (V/Pre).
  Spotlighting ASR rose under adaptive attacks to 64.8–82.4%, from 13.0–75.2% non-adaptive.
- **Anthropic**, "Mitigating the risk of prompt injections in browser use", 24 Nov 2025,
  https://www.anthropic.com/research/prompt-injection-defenses (V). Opus 4.5 against an adaptive
  attacker: 8.0% model-only → 1.4% with RL training plus classifiers.

### Moves

- **Global AGENTS.md**, Destructive actions. The bans on `git clean`, `git reset --hard`,
  `git push --force` and `git branch -D` are wording. IHEval and Nasr show wording neither ranks
  nor protects reliably.
  - Back each ban with harness enforcement: Claude Code permission deny rules or a PreToolUse hook,
    and the equivalent in Codex and Gemini CLI configs.
  - Keep the prose as the explanation.
  - This is persistent configuration, so it needs José's go-ahead.
- **Report §7.** Add the three-way split: static benchmarks show a modest gain; adaptive attacks
  remove it; system enforcement holds at a utility cost (CaMeL 77% vs 84%). Note that StruQ, which
  the report cites, is bypassed in Nasr et al.
- **Skills.** None. A "treat as data" line in a skill is harmless, but it does not count as a
  defence.

---

## 4. Skills interfere when several are installed or loaded

**What it changes.** §8 says "test combinations as well as individual components" as an open item.
2026 measurements now exist:
- Gains shrink once a task loads 4 or more skills.
- Libraries degrade as they grow, mostly because the right skill is never loaded.
- A same-job twin takes over about one run in five, and the agent almost never says so.
- When two clashing skills are both loaded, one skill's rules are dropped wholesale.
- Telling the model which skill has priority does not fix that. One worked example that satisfies
  both skills, or a merged file, does.

### Evidence

**Li et al.** "SkillsBench." arXiv 2602.12670v4, Jun 2026. https://arxiv.org/html/2602.12670 — Pre,
Checked.

- Setting: 87 tasks, 18 model–harness configurations.
- Curated skills raise the pass rate from 33.9% to 50.5%.
- Gain by number of skills per task: one skill +18.0 pp; 2–3 skills +19.0 pp; 4 or more +10.1 pp.
- Gain by skill length: compact +19.0; standard +21.5; detailed +14.5; comprehensive +0.7.
- Self-generated skills land −8.1 to −11.5 pp below the no-skills baseline.
- Skills hurt on 13 of 87 tasks.

**Song & Wei.** "More Skills, Worse Agents? Skill Shadowing Degrades Performance When Expanding Skill
Libraries." arXiv 2605.24050, May 2026. https://arxiv.org/html/2605.24050v1 — Pre, Checked.

- Setting: Haiku 4.5 and Sonnet 4.6.
- At 202 skills, the pass rate drops by 0.21 [0.15, 0.27].
  - Shadowing accounts for 0.14, "up to 68%" of the drop.
  - Context overhead is not distinguishable from zero.
- Runs that invoke only the right skills fall from 88.0% to 52.6%. Runs that invoke no skill rise
  from 12.0% to 38.5%.

**Yan, Xu, Li, Xu, Liu, Deng, Ma.** "One Skill Too Many: How Co-Installed Skills Conflict in Coding
Agents." arXiv 2610.11647, Oct 2026. https://arxiv.org/html/2610.11647v1 — Pre, Checked.

- Setting: Claude Code 2.1.283 with Sonnet 4.6, Haiku 4.5 and Opus 5; 312 skill pairs; 6,368 runs.
- A similar co-installed skill cuts use of the installed skill by 19.9 pp; an unrelated one by 5.9
  pp.
- Task completion did not drop: +1.9 points (95% CI −1.0 to +4.9).
- Fidelity on functions only the installed skill provides fell 5.6 points.
- When the twin replaced the installed skill, the final reply named the skill actually used in 0.9%
  of runs.
- A PreToolUse hook that denies the first read of the twin made the model switch back in 96% of 179
  cases.
- 23.5% of installed skills have a same-job twin in the same installation.

**Razmara, Azizi, Aryashad.** "One Skill Takes Over: Clashing Agent Skills and a One-File Fix." arXiv
2610.25064, Oct 2026. https://arxiv.org/html/2610.25064v1 — Pre, Checked.

- Setting: 16 synthetic pairs of same-job skills; 7 models up to GPT-4.1 and Qwen3-235B.
- Rule compliance is 93–99% with one skill loaded alone, and 61–62% with both.
- One skill takes over in 45–78% of outputs.
- A priority instruction does not bring the dropped skill back: 62–71% compliance, takeover in
  36–82% of outputs.
- Ending each skill file with one example that follows both skills cuts takeover to 1–15%. A merged
  skill reaches 96–99% compliance.

**Further results (Subagent):**
- **SkillFusion**, arXiv 2610.15481 (Pre). Success with a single skill was .823; with conflicts,
  redundancy and soft conflicts combined, .631.
- **CoSA**, arXiv 2610.35082 (Pre, Abstract). Adding conflicting skills, up to 5% of the pool, raised
  policy violations from 35.02% to 58.45%. A harness guard cut them from 65.28% to 6.67%.
- **Liu, Chen, Zhang**, "Lost in Implicit Routing", arXiv 2610.18522 (Pre). With 1,000 distractor
  skills, recall of the right skill fell from 73.6% to 27.4%.
- **Vercel**, "AGENTS.md outperforms skills in our agent evals", 27 Jan 2026,
  https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals (V/Pr). The skill was not
  invoked in 56% of cases. An 8KB docs index in AGENTS.md scored 100%.

### Moves

- **Installation hygiene (global).** The skill listing in this session shows exact twins:
  - `caveman-commit` and `caveman:caveman-commit`;
  - `cavecrew` and `caveman:cavecrew`;
  - `typesafe-ai` and `typesafe:typesafe-ai`.

  It also shows same-job neighbours:
  - review: `revolver`, `caveman-review`, built-in `code-review`;
  - exploration: `scout`, `corpus-audit`, `caveman-explore`;
  - verification: `bulletproof`, `verify-and-stop`.

  Decide one owner per job and uninstall or disable the rest. Silent substitution (0.9% disclosure)
  means you would not otherwise notice which one ran.
- **Hooks for critical skills.** Where a skill must win, enforce it with a hook, not with "prefer"
  text. A deny-first-read hook restored the intended skill in 96% of cases. This is configuration,
  so it needs José's go-ahead.
- **Skill bodies.** José's skills are 10–23 lines, the "compact/standard" band, which scored best.
  Keep them there.
- **Pairs that may load together** (for example `settle`+`drill`, `revolver`+`bulletproof`). Give
  each pair one shared example that satisfies both, instead of priority wording.
- **Report §8.** Replace the hypothetical with these numbers. The SkillsBench task-level drop at 4 or
  more skills is a practical ceiling of 2–3 skills per task.

---

## 5. Clarification: agents under-ask, pushing over-asks, and answers create false safety

**What it changes.** §4's rule ("ask about consequential preferences; investigate discoverable
facts; preserve delegated choices") is supported, and it gains three things:
- The default failure is not asking at all. Preference tuning makes it worse.
- "Consequential" can be made operational: ask only questions whose possible answers would change
  the program's behaviour.
- After a user answers, they review less. Verification is still owed, and most of all near the
  decision they answered.

### Evidence

**Vijayvargiya, Zhou, Yerukola, Sap, Neubig.** "Ambig-SWE: Interactive Agents to Overcome
Underspecificity in Software Engineering." ICLR 2026, per the arXiv comments.
https://arxiv.org/abs/2502.13069 — PR, Checked.

- "Without explicit prompting, models almost never interact, even for severely underspecified
  inputs."
- Interaction improves results by "up to 74%" over non-interactive settings. It recovers 89% of
  full-spec performance for Claude Sonnet 4, and "up to 80%" for Sonnet 3.5 and Haiku 3.5.
- Agents obtained file-location information through the user on 8.96–30.70% of issues. That is
  asking about facts they could have discovered themselves.
- Detecting underspecification (subagent, Table 2) depends on the model and the prompt. Qwen 3 Coder
  stays at 0.50 (chance) under every prompt.

**Wu & Fard.** "HumanEvalComm." ACM TOSEM 2025. https://arxiv.org/html/2406.00215 — PR, Checked.

- "More than 60% of responses from Code LLMs still generate code rather than ask questions."
- The always-ask agent "Okanagan" scores 27.45% Pass@1 on the original, clear HumanEval, against
  65.58% for its ChatGPT base. The paper's explanation: it "sometimes asks questions as an initial
  response even for original problems".

**Shaikh, Gligorić, Khetan, Gerstgrasser, Yang, Jurafsky.** "Grounding Gaps in Language Model
Generations." NAACL 2024, pp. 6279–6296. https://aclanthology.org/2024.naacl-long.348/ — PR, Checked.

- LLM generations are "77.5% less likely to contain grounding acts than humans".
- On Mistral 7B, more DPO training lowers agreement with human grounding: R = −0.70 for follow-ups,
  −0.89 for acknowledgments, −0.78 for clarifications.
- Follow-up: **Shaikh et al.**, "Navigating Rifts in Human-LLM Grounding", ACL 2025,
  https://arxiv.org/html/2503.13975 (PR, Subagent).
  - LLMs clarify user instructions in 2% of turns; people clarify LLM outputs in 6%.
  - Frontier models score 23.88–26.95% on RIFTS, below a 33% random baseline.

**Fang et al.** "CONTRA: Discovering and Qualifying Behavior-Changing Questions for Selective
Clarification in LLM Code Generation." arXiv 2610.01769, Oct 2026.
https://arxiv.org/html/2610.01769v1 — Pre, Checked.

- Setting: 419 underspecified and 80 fully specified tasks. The harness comparison uses Qwen3.8-27B
  as the backbone.
- Rate of asking on fully specified tasks: Claude Code 5.00%, OpenHands 32.50%, CONTRA 5.00%.
- Question F1: 19.86 for CONTRA vs 9.63 for Claude Code. CONTRA keeps only questions whose answers
  would change the program's behaviour.
- Downstream pass@1 gains are modest (Subagent).

**Zheng, Zheng, Zhu, Ma.** "Is That Clear? The Impacts of Clarifying Questions on Human-LLM
Interaction." arXiv 2611.01087, 31 Oct 2026. https://arxiv.org/html/2611.01087 — Pre, Checked.

- Setting: N = 180, between subjects; everyday decisions, not code.
- With clarifying questions, compared with without:
  - Satisfaction rose from 4.9 to 5.3 (p = .043).
  - Review time fell (ratio 0.77, p = .003).
  - Unchanged acceptance of erroneous responses rose from 39% to 52% (p = .034).
- Errors next to a clarified sub-decision were accepted 60% of the time, against 43% elsewhere.

**Chen et al.** "Need Help? Designing Proactive AI Assistants for Programming." CHI 2025.
https://arxiv.org/html/2410.04596 — PR, Checked.

- Setting: 65 students.
- Preference for the proactive assistant over the baseline: about 90% for "Suggest", 47% for
  "Persistent Suggest". Persistent Suggest waited 5 s instead of 20 s and showed 5 suggestions
  instead of 3.
- Productivity rose in all variants, for example +18% ± 5.8% test cases passed for Suggest.

**Sehwag et al.** "ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in
LLM Agents." arXiv 2605.17324, May 2026. https://arxiv.org/abs/2605.17324 — Pre, Abstract, Checked.

- Setting: 728 scenarios, ten frontier LLMs.
- Clarification-seeking raised attack success from 1.8% to 34.0% for o3, and from 2.2% to 35.7%
  for Gemini-3-Flash.

**Further results (Subagent):**
- **Vijayvargiya, Viswanathan, Neubig**, "Asking What Matters" (CLARITI), arXiv 2604.14624 (Pre).
  It reached 36.8% with 3.0 questions, against 35.6% for GPT-5 asking 5.1 questions, and 41.6% with
  the full issue.
- **Edwards & Schuster**, "Ask or Assume?", arXiv 2603.26233, EMNLP 2026 per the arXiv comment
  (PR). A separate agent that decides when to ask brought Claude Sonnet 4.5 to 69.40%, against
  70.80% with the full spec. Cost was about $3.50 per task, against $1.80.
- **Kuo, Sergeyuk, Chen, Izadi**, IUI '26, arXiv 2601.10253 (PR). Developers engaged with 52% of
  interventions made at commit time, against 31% of those made right after declining an edit.
- **Zhang, Knox, Choi**, ICLR 2025, arXiv 2410.13788 (PR). Learned decisions on whether to clarify
  were only slightly above random: 53.7 vs 52.1. Annotators preferred "complete but presumptuous"
  answers.
- **CLAMBER**, ACL 2024 (PR). ChatGPT identified ambiguity with 54.25% accuracy.

### Moves

- **settle**, step 3. "Ask only when the plausible readings lead to different actions" matches
  CONTRA's behaviour-change filter. Keep it, and add a check after the answer: verify the work that
  sits next to the decision the user just answered, since answered decisions are where reviewers
  relax (60% vs 43%).
- **settle**, step 2. "Settle what code … can decide" is supported. Agents asked users for file
  locations on 9–31% of issues.
- **drill.** The model's own sense that something is ambiguous is unreliable (near-chance on
  CLAMBER, RIFTS and Qwen). Add one line before code: list any reading of the request that would
  produce different behaviour. Listing readings forces detection without forcing a question.
- **Global AGENTS.md.** "Ask … with options and a recommendation. Never end a turn on a question
  while work remains" is consistent with the cost of interruptions and with boundary timing. No
  change.
- **Report §4.** Add "asking also widens the injection surface" (ASPI). Treat answers that arrive
  through tools or fetched content as data.

---

## 6. Explanations and self-assessment: fluency raises confidence, not accuracy

**What it changes.** §5 proposes: predict one altered scenario, "then follow the relevant code or run
the case." Chromik shows prediction alone does not correct an inflated sense of understanding. Seeing
the scored result does. So the run is the active part, not an option.

Other changes:
- Wrong explanations push readers below the no-AI baseline.
- Long explanations add confidence without improving discrimination.
- Contrastive (for-and-against) explanations help when the AI is wrong and hurt when it is right.
- Perceived speed-up was the opposite of measured speed in 2025. The 2026 redesign cannot yet say
  how large the speed-up is.

### Evidence

**Chromik, Eiband, Buchner, Krüger, Butz.** "I Think I Get Your Point, AI! The Illusion of Explanatory
Depth in Explainable AI." IUI '21.
https://www.medien.ifi.lmu.de/pubdb/publications/pub/chromik2021iui/chromik2021iui.pdf — PR, Checked.

- Setting: 40 moderated participants and 107 crowd workers, using SHAP tables. Not LLMs.
- Self-rated understanding fell over the whole procedure for 63% and 72% of participants.
- During the prediction tasks, only 18–19% lowered their rating (not significant). In the moderated
  study, ratings rose.
- After seeing their scored results, 45% (moderated) and 67% (unmoderated) lowered their rating;
  both drops were significant.

**Si, Goyal, Wu, Zhao, Feng, Daumé III, Boyd-Graber.** "Large Language Models Help Humans Verify
Truthfulness – Except When They Are Convincingly Wrong." NAACL 2024.
https://aclanthology.org/2024.naacl-long.81.pdf — PR, Checked.

- Setting: 80 crowd workers, gpt-3.5-turbo, fact-checking claims.
- Accuracy with a ChatGPT explanation was 0.74, against 0.59 with no evidence.
- When the explanation was correct, accuracy was 0.87. When it was wrong, accuracy was 0.35, against
  0.49 with no evidence and 0.54 with retrieved passages.
- Contrastive explanations raised accuracy on wrong cases from 0.35 to 0.56, but lowered it on right
  cases (subagent: 0.87 → 0.73).

**Steyvers et al.** "What large language models know and what people think they know." Nature
Machine Intelligence, 2025. Author PDF:
https://mstrep.s3.amazonaws.com/publications/WhatLLMsKnowSteyversetal.pdf — PR, Subagent.

- How well people told right answers from wrong after reading default explanations (AUC): about
  0.59–0.60. The models' own confidence scored 0.75–0.78.
- Longer explanations raised confidence (Bayes factor 25), but did not improve discrimination.

**METR 2025.** Becker, Rush, Barnes, Rein, arXiv 2507.09089, and
https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ — Pre/V, Subagent.
- Setting: 16 experienced developers, 246 issues.
- AI-allowed issues took 19% longer.
- Developers forecast a 24% speed-up beforehand and estimated 20% afterwards.

**METR 2026.** "We are Changing our Developer Productivity Experiment Design", 24 Feb 2026,
https://metr.org/blog/2026-02-24-uplift-update/ — V, Checked.

- The early-2025 estimate is +19% time, CI +2% to +39%.
- Late-2025 estimates, with 57 developers:
  - Returning developers: −18% time, CI −38% to +9%.
  - New developers: −4%, CI −15% to +9%.
- 30–50% of developers withheld tasks they did not want to do without AI.
- METR calls this "only very weak evidence" for the size of the speed-up.

**Shen & Tamkin.** "How AI Impacts Skill Formation." arXiv 2601.20245, Jan 2026, and
https://www.anthropic.com/research/AI-assistance-coding-skills — Pre/V, Checked.

- Setting: 52 mostly junior engineers learning the Trio library, using a GPT-4o chat assistant.
- Quiz scores: 50% with AI vs 67% hand-coding (subagent: d = 0.738, p = 0.010).
- The AI group was about two minutes faster, which was not significant.
- Patterns averaging 65% or more:
  - generation-then-comprehension;
  - hybrid code-explanation;
  - conceptual inquiry.
- Patterns averaging under 40%:
  - full delegation;
  - progressive reliance;
  - iterative AI debugging.

**Lee et al.** "The Impact of Generative AI on Critical Thinking…". CHI 2025.
https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/
— PR, Subagent.

- Setting: 319 workers, 936 examples; self-reported.
- Confidence in the AI predicted less critical thinking (β = −0.69). Confidence in one's own ability
  to evaluate the output predicted more (β = 0.31).

**Rozenblit & Keil 2002**, Cognitive Science 26 (PR, Subagent). Writing a causal explanation lowered
self-rated understanding; Study 2 means went from 3.89 to 3.10.

**Reviews of automation bias (Subagent):**
- **Romeo & Conti 2025**, AI & Society (PR): 35 experiments, 19,774 participants.
  - Automation bias rose when the AI's output was shown before the person's own judgement.
  - It fell with cognitive forcing and with more verification.
  - Accountability framing "lacks empirical support".
- **Parasuraman & Manzey 2010** (PR, Abstract): automation bias "cannot be prevented by training or
  instructions".

**Reviewing AI-made code (Subagent):**
- **Tufano et al.**, arXiv 2411.11401 (Pre). Reviewers who started from an LLM review found a median
  50% of injected issues, the same as manual reviewers.
- **Kaufman et al.**, arXiv 2607.08885 (Pre). Programmers rejected only 49.0% of incorrect
  LLM-generated postconditions, with flat confidence.

### Moves

- **Report §5.** Change "follow the relevant code or run the case" to "predict, then run the case
  and compare". Prediction without a scored result left self-rated understanding unchanged, and in
  the moderated study raised it.
- **wdyt.** Step 7 already asks for a short argument with numeric confidence. That matches Steyvers
  (short, calibrated) and Si (explanations mislead when wrong). Keep step 3's opponent case for
  consequential questions only: contrastive framing costs accuracy when the lean is right (0.87 →
  0.73). wdyt is already user-invoked only, so no change.
- **tldr.** Supported: shorter output with uncertainty kept.
- **sitrep, bulletproof.** Already report from live state and direct evidence rather than the
  agent's self-assessment. Supported.
- **José's own practice, not a skill.** When a delegated change matters for understanding, ask
  conceptual questions after the code is generated; Shen & Tamkin's high-scoring patterns did this.
  Do not treat felt speed as a measure; METR 2025 measured the opposite.

---

## 7. The fourth option: option sets converge; your own judgement first

**What it changes.** §6 cites Doshi & Hauser and motivates testing whether repeated requests produce
different approaches. Now:
- Measured homogeneity across 25 models answers that question for open-ended prompts.
- Correlated errors across models mean a multi-model panel is not a set of independent samples.
- Verbalized sampling is a cheap method that widens the option set.
- A 2026 randomized trial supports the report's proposed habit of independent framing before
  reading options.

### Evidence

**Jiang et al.** "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)."
NeurIPS 2025 Datasets & Benchmarks (Oral). https://arxiv.org/html/2510.22954 — PR, Checked.

- Setting: 100 open-ended queries, 25 models, 50 responses per model per query. Not code.
- Within one model at top-p 0.9 and temperature 1.0, "in 79% of cases, the average similarity
  exceeds 0.8."
- Between different models, average pairwise similarity "ranges from 71% to 82%".

**Zhang, Yu, Chong, Sicilia, Tomz, Manning, Shi.** "Verbalized Sampling: How to Mitigate Mode
Collapse and Unlock LLM Diversity." arXiv 2510.01171 (no venue listed).
https://arxiv.org/abs/2510.01171 — Pre, Checked.

- Method: ask the model for k responses with their probabilities.
- Creative-writing diversity is 1.6–2.1× that of direct prompting.
- Subagent, from the full text: a poem-quality cost of about 5 points for the standard variant, and
  parity for the multi-turn variant.

**Yan, Dong.** "Independent judgment before viewing generative AI recommendations reduces
susceptibility to misleading advice." Frontiers in Psychology 17, Sep 2026.
https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1936522/full — PR,
Checked.

- Setting: 218 preservice teachers analysed, in 3 arms.
- When the advice was misleading: 53.5% accuracy for those who judged first, against 37.3% for those
  shown the AI first (OR 1.912, CI [1.413, 2.589]).
- When the advice was right: 65.2% vs 66.2%, not significant.
- Copying the misleading advice in full: 25.8% vs 46.8%.
- Limits: single author, scenario-based, not preregistered, fixed item order.

**Supporting results (Subagent):**
- **Kim, Garg, Peng, Garg**, "Correlated Errors in Large Language Models", ICML 2025, arXiv
  2506.07962 (PR). Models agree 60% of the time when both are wrong, against a one-in-three chance
  baseline. Same-company models agree more.
- **Wenger & Kenett**, arXiv 2501.19361 (Pre). Across 22 LLMs, responses varied far less than
  human responses on alternative-uses tasks: 0.459 vs 0.738 cosine distance. A "very creative"
  prompt raised the LLM figure only to 0.576.
- **Lee et al.**, arXiv 2503.00691 (Pre). On programming problems, humans found about 3 distinct
  algorithms where models found about 2. Pooling three vendors added little: +0.015 effective
  algorithms on AtCoder.
- **Anderson, Shah, Kreminski**, ACM Creativity & Cognition 2024 (PR). Ideas from ChatGPT users were
  more alike across the group (d = .47), but not within each person.
- **Wong & Qiu**, Educational Psychology Review 2026 (PR). A "think first, then ChatGPT" arm kept
  unassisted originality (3.42, against 2.69 for free ChatGPT use).

### Moves

- **panel.** Separate contexts do not make analyses independent, because the models' priors are
  shared.
  - Give each subagent a different framing to hold, for example one that must reject the shared
    premise of the options as listed.
  - Generate options as k alternatives with probabilities, including low-probability ones.
- **wdyt**, step 2, and **stepback.** Both already divide answers exhaustively and question the
  premise. These moves match the representation-change mechanism in §6. No change.
- **José's own practice.** Before opening a panel or wdyt result on a consequential choice, write a
  one-line answer of your own. This is the measured independent-first condition.
- **Report §6.** Replace "motivates testing" with these results. The proposed experiment remains
  useful for software design specifically; Lee et al. is the only code evidence found, and it is
  thin.

---

## 8. Instruction count: fewer losses on simple rules, but rules against defaults still fail

**What it changes.** §1 relies on Yang et al. adding requirements did not help consistently. The
evidence splits:
- Simple-rule capacity has risen sharply on 2026 frontier models (practitioner evidence only).
- Rules that oppose a model's defaults are followed 3.6–7.4 points less.
- LLM-written context files and repository overviews do not help.

So the "smallest set of commitments" should be chosen by one test: does the model already do this?
Length matters less.

### Evidence

**Jaroslawicz, Whiting, Shah, Maamari.** "How Many Instructions Can LLMs Follow at Once?" (IFScale).
arXiv 2507.11538, 2025. https://arxiv.org/html/2507.11538 — Pre, Checked.

- Setting: 20 models; the rules are keywords to include in a report, which is a weak proxy for
  behaviour.
- Accuracy at 500 instructions: gemini-2.5-pro 68.9%, gpt-4.1 48.9%, claude-opus-4 44.6%,
  claude-sonnet-4 42.9%, gpt-4o 15.4%.
- Models favour earlier instructions; this primacy bias peaks around 150–200 instructions.
- As density rises, errors are mostly omissions.

**Harada et al.** "When Instructions Multiply." Findings of EMNLP 2025, arXiv 2509.21051 (PR,
Subagent).
- Share of tasks with every instruction satisfied, at 1 vs 10 instructions: GPT-4o 0.94 → 0.21,
  Claude 3.5 Sonnet 0.95 → 0.48.
- Per-instruction success to the power n predicts those totals.
- The original "Curse of Instructions" OpenReview page could not be opened; it was blocked by a
  bot check.

**Voss (Arize AI).** "Models got an order of magnitude better at following instructions in one
year." Blog, May 2026 (Pr, Subagent). A rerun of IFScale with a larger vocabulary reports GPT 5.5 at
99% through 5,000 keyword instructions. It measures keyword inclusion only.

**Huang et al.** "Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding
Agents." arXiv 2608.11727, Aug 2026. https://arxiv.org/abs/2608.11727 — Pre, Abstract, Checked.

- Setting: 60 multi-turn coding tasks, 256 rules spread over five instruction surfaces, 12 frontier
  models.
- Overall accuracy was 72.1–85.9%.
- On rules that oppose the model's defaults, accuracy was 66.1–78.6%, 3.6–7.4 points lower (mean
  5.81).
- When instructions conflicted, system prompts, project files and user instructions outranked tool
  and skill descriptions.

**Gloaguen, Mündler-Sasahara, Müller, Raychev, Vechev.** "Evaluating AGENTS.md: Are Repository-Level
Context Files Helpful for Coding Agents?" arXiv 2602.11988v3, Sep 2026.
https://arxiv.org/html/2602.11988 — Pre, Checked.

- LLM-generated context files lowered performance in 5 of 8 settings.
- Developer-written files added 2.4% on average, which was not significant (p = 21%).
- LLM-generated files raised cost by 20% and 23%.
- Agents do follow the instructions: `uv` was used 1.6 times per instance when mentioned, against
  under 0.01 when not.
- Repository overviews did not help.

### Moves

- **debloat.** Add a test for instruction files: cut any rule the model already follows unprompted,
  and keep the ones that oppose defaults. Those are the rules that earn their place, and they are
  the ones most likely to be missed. Pairs with the existing research-skills recommendation to flag
  outdated or conflicting rules.
- **Global AGENTS.md.** At 87 lines, it is mostly non-default, decision-carrying rules, which is the
  kind Harness-IF and Gloaguen favour. Audit the Projects paragraph: keep the non-discoverable facts
  (the symlink, the single checkout, the CRDT rule) and drop any pure overview.
- **Report §1.** Add Harness-IF and Gloaguen as the coding-agent evidence for "selective, not
  exhaustive".

---

## 9. Self-preference varies widely by model

**What it changes.** This supports revolver's existing "self-review is not fresh" and the report's §2
point. It adds that the size of the bias depends on the model, and that a committee reduces it
without removing it.

### Evidence

**Pombal, Rei, Martins.** "Self-Preference Bias in Rubric-Based Evaluation of Large Language Models."
arXiv 2604.06996v3, Aug 2026. https://arxiv.org/html/2604.06996 — Pre, Checked.

- Judges can be "more than 50% more likely" to mark a failed rubric as satisfied when the output is
  their own.
- Ratio of self-overestimation on LiveCodeBench: GPT-5 20.15, GPT-oss-120B 5.97, Claude Sonnet 4.5
  1.78.
- A committee of 5 judges reduced GPT-5's ratio to 4.18 and Sonnet's to 1.29.

**Panickssery, Bowman, Feng.** "LLM Evaluators Recognize and Favor Their Own Generations." arXiv
2404.13076, 2024. Commonly cited as NeurIPS 2024; the page opened named no venue.
https://arxiv.org/html/2404.13076 — Pre/PR, Subagent.

- GPT-4 recognises its own output with 73.5% accuracy.
- GPT-4 self-preference: 0.705 on XSUM, 0.912 on CNN/DM.
- Fine-tuning self-recognition raises self-preference.

**Xu et al.** "Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement." arXiv 2402.11436 (Pre,
Subagent). GPT-4's self-bias on a translation task rose from 8.06 to 14.6 over 10 rounds of
self-refinement.

### Moves

- **revolver.** No change to the rule. When the harness offers another model family, the reviewer
  should differ from the author's family. Never tell the reviewer who wrote the target (Chae, +0.43).

---

## Corrections to earlier research files

- **`research-skills.md`, recommendation 1.** It cites SWE-Skills-Bench (arXiv 2603.15401) as "39
  of 49 public SWE skills gave zero pass-rate gain". The current v2 (27 Oct 2026) says "92 of 98
  skills have no statistically significant effect", with the pass ratio moving from 76.6% to 76.9%.
  Checked: https://arxiv.org/abs/2603.15401
- **CaMeL** is 77% with provable security vs 84% undefended (v2 abstract, Checked). The "67% vs 77%"
  in some secondary sources does not match the current paper.
- **Gloaguen et al. v3** reports developer-written files at +2.4% (not significant) and renames the
  benchmark CTXbench. Earlier versions, and secondary write-ups, give about +4% and "AGENTbench".

## Gaps and unverified items

- No study measures superseded-vs-current decisions in real coding-agent transcripts.
- No study isolates an author's self-assessment ("I verified this") from other framing for an LLM
  reviewer. The Mitropoulos PR framing includes such text, but bundles it with other framing.
- No study tests "one question, as a choice with a recommendation" against several questions.
- Not opened, so not cited:
  - Curse of Instructions (OpenReview bot check);
  - the UserBench numbers;
  - Meincke et al. (Nature Human Behaviour 2025), seen only via a press post;
  - Doshi & Hauser's newer follow-ups;
  - the Opus 4.6 system card injection numbers.
- **Instructions inside fetched pages.** Two arXiv HTML pages in this research carried text directed
  at LLM readers, and the fetch tool flagged it: arXiv 2602.07338, and arXiv 2603.26233 as reported
  by a subagent. It was not acted on. This is a live example of §7's concern inside ordinary
  research sources.
