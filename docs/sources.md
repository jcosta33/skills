# Sources

Each entry backs a line a skill or the edit contract still carries. Primary sources first; bound
practitioner material by its setup. Remove an entry when its line leaves, and replace a dead link.
Decisions and their evidence are in [`adrs/`](adrs/README.md); the research reports behind them are
in [`research/`](research/README.md).

## Skill format and length

- **Agent Skills specification.** `SKILL.md` layout, frontmatter, description limit.
  https://agentskills.io/specification
- **Agent Skills best practices, Anthropic.** Concise bodies; evaluate against real tasks.
  https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- **Build skills, OpenAI Codex.** Discovery from descriptions; shared metadata budget.
  https://learn.chatgpt.com/docs/build-skills
- **The new rules of context engineering for Claude 5 generation models, Anthropic.** Less
  prescriptive prompts for current models; no benchmark detail disclosed.
  https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- **Same Task, Different Work: Prompt-Induced Waste in Coding Agents.** Weinberger and Hozez, 2026
  preprint. Unbounded certainty and multi-approach prompts added work without measured gains.
  https://arxiv.org/abs/2608.01347
- **Curse of Instructions.** Harada et al., ICLR 2025. Joint compliance falls as instruction count
  grows. https://openreview.net/forum?id=R6q67CDBCH
- **Claude Code hooks.** A rule that must hold every time belongs in a hook or in always-loaded
  instructions, not in a skill. Backs manual-only skills (ADR-0014). https://code.claude.com/docs/en/hooks
- **Claude Code skills.** `disable-model-invocation` keeps a skill to explicit `/name` use; claude.ai
  uploads and the Skills API reject keys outside the spec. https://code.claude.com/docs/en/skills
- **Cursor skills.** Honours `disable-model-invocation`. https://cursor.com/docs/context/skills
- **Codex `agents/openai.yaml` reference.** `policy.allow_implicit_invocation: false` keeps a skill
  out of model context until called as `$name`. Ships with Codex as
  `~/.codex/skills/.system/skill-creator/references/openai_yaml.md`.
- **Vercel skills CLI.** Global and per-agent install; `add` does not remove departed skills.
  https://github.com/vercel-labs/skills

## settle

- **ConInstruct.** AAAI 2026. Strong models detect conflicts but rarely ask the user.
  https://ojs.aaai.org/index.php/AAAI/article/view/40356
- **Choice overload meta-analysis.** Scheibehenne, Greifeneder, and Todd, JCR 2010. No universal
  optimum option count; a small set with a recommendation is a convention, not a law.
  https://doi.org/10.1086/651235
- **System 2 Attention.** Weston and Sukhbaatar, 2023 preprint. Regenerating the context without the
  asker's opinion reduced sycophantic answers. https://arxiv.org/abs/2311.11829
- **Towards Understanding Sycophancy in Language Models.** Sharma et al., 2023 preprint. Models bend
  answers toward the user's stated view. https://arxiv.org/abs/2310.13548
- **AbstentionBench.** Kirichenko et al., 2025 preprint. Models rarely say a question cannot be
  answered from what they have. https://arxiv.org/abs/2506.09038
- **Structured Uncertainty Guided Clarification for LLM Agents.** Suri et al., Findings of ACL 2026,
  pp. 40811–40838. Ask only about what changes the action, one decisive question.

## bulletproof and panel

- **Large Language Models Cannot Self-Correct Reasoning Yet.** Huang et al., ICLR 2024. Reasoning
  without external evidence is not verification. https://arxiv.org/abs/2310.01798
- **GPT-4o-generated citations in mental-health literature reviews.** JMIR Mental Health 2025.
  Fabricated citations; check sources directly. https://mental.jmir.org/2025/1/e80371
- **Multiagent Debate.** Du et al., ICML 2024. Bounded independent analysis helps on evaluated
  tasks; more rounds are not always better. https://proceedings.mlr.press/v235/du24e.html
- **Voting or Consensus?** Findings of ACL 2025. No universal aggregation rule; keep dissent.
  https://aclanthology.org/2025.findings-acl.606/

## dissect

- **POPPER.** Huang et al., 2025 preprint. Hypothesis checks that state their falsifying result
  first, with only tests that could fail. https://arxiv.org/abs/2502.09858
- **Corr2Cause.** Jin et al., ICLR 2024. Models infer causation from correlation; a cause needs an
  intervention. https://arxiv.org/abs/2306.05836

## debloat

- **IFScale.** Jaroslawicz et al., 2025 preprint. Compliance falls with instruction count, and
  models favor earlier instructions. https://arxiv.org/abs/2507.11538
- **Claude Code commands.** `/doctor prompt-audit` checks instruction files for outdated or
  conflicting instructions. https://code.claude.com/docs/en/commands
- **Harness-IF.** Huang et al., 2026 preprint. Coding agents follow rules that oppose their defaults
  3.6–7.4 points less often than other rules. https://arxiv.org/abs/2608.11727
- **Evaluating AGENTS.md.** Gloaguen et al., 2026 preprint. Agents follow repository instructions
  they would not apply unprompted; generic overviews did not help.
  https://arxiv.org/html/2602.11988

- **Token Reduction Is Not Cost Reduction.** Weinberger and Hozez, 2026 preprint. Lossy compression
  damaged exact anchors. https://arxiv.org/abs/2607.12161
- **An Empirical Study on Prompt Compression.** 2025 preprint. Effects are task-dependent.
  https://arxiv.org/abs/2505.00019

## drill

- **sgruetter top-down.** MIT practitioner skill: level order, behavior before machinery, reuse
  first. No `CONTEXT.md` adopted. https://github.com/sgruetter/skills/tree/main/skills/top-down
- **TiCoder.** Lahiri et al., 2022 preprint. Intent stated as checkable tests raised pass@1 by 22–54
  points. https://arxiv.org/abs/2208.05950

## revolver

- **Self-Preference Bias in LLM-as-a-Judge.** Wataoka et al., NeurIPS 2024 workshop. Judges favor
  their own output; reviewers must be fresh. https://arxiv.org/abs/2410.21819
- **Primers or reminders?** Spadini, Calikli, and Bacchelli, ICSE 2020. Visible prior comments steer
  later reviewers; hide peer prose. https://doi.org/10.1145/3377811.3380385

## wdyt

ADR-0012 maps lines 2–10 to these; ADR-0016 maps line 1 and the description.

- **LLM Evaluators Recognize and Favor Their Own Generations.** Panickssery et al., 2024 preprint.
  Models rate their own outputs above others'. https://arxiv.org/abs/2404.13076
- **Self-Correction Bench.** Tsui, 2025 preprint. Models fix an error less often when it is their
  own than when the same error is attributed to the user. https://arxiv.org/abs/2507.02778

- **Scorekeeping in a Language Game.** Lewis, J. Philosophical Logic 1979. Presuppositions are
  accommodated unless someone objects. https://andrewmbailey.com/dkl/Scorekeeping_in_a_Language_Game.pdf
- **FPBench.** Li et al., 2025 preprint. Code generators reason poorly under faulty premises.
  https://arxiv.org/abs/2508.03622
- **CRITIC.** Gou et al., 2023 preprint. Self-correction works when critique uses external tools.
  https://arxiv.org/abs/2305.11738
- **Automating Alternative Generation in Decision-Making.** Kostiuk, Seyfried, and Reed, Findings
  of EMNLP 2025. LLM and human options barely overlap. https://aclanthology.org/2025.findings-emnlp.1/
- **Artificial Hivemind.** Jiang et al., NeurIPS 2025 D&B. Open-ended model outputs converge.
  https://arxiv.org/abs/2510.22954
- **Critical Questions Generation shared task.** Calvo Figueras et al., ArgMining 2025. Critical
  questions for practical reasoning, after Walton, Reed, and Macagno (CUP 2008).
  https://aclanthology.org/2025.argmining-1.23/
- **Devil's Advocate: Anticipatory Reflection for LLM Agents.** Wang et al., Findings of EMNLP
  2024. Considering failure before acting raised success with fewer trials.
  https://arxiv.org/abs/2405.16334
- **LLMs Help Humans Verify Truthfulness, Except When They Are Convincingly Wrong.** Si et al.,
  NAACL 2024. For-and-against explanations lowered accuracy on right answers.
  https://aclanthology.org/2024.naacl-long.81/
- **What large language models know and what people think they know.** Steyvers et al., Nature
  Machine Intelligence 2025. Longer explanations raised confidence without better discrimination.
  https://mstrep.s3.amazonaws.com/publications/WhatLLMsKnowSteyversetal.pdf
- **Prompting Claude Opus 5, Anthropic.** Requests for written-out thinking can be declined
  (`reasoning_extraction`). https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **The FlipFlop Experiment.** Laban et al., 2023 preprint. "Are you sure?" flips answers and cuts
  accuracy. https://arxiv.org/abs/2311.08596
- **Asserting.** Brandom, Noûs 1983. An assertion stands until a challenge defeats it.
  https://sites.pitt.edu/~rbrandom/Courses/2022%20Phil%20of%20Language/Reasons%20texts/Asserting.pdf
- System 2 Attention, Towards Understanding Sycophancy (under settle), and TiCoder (under drill)
  also back wdyt lines.

## Micro skills

ADR-0013 maps each line to these.

- **LLMs Get Lost In Multi-Turn Conversation.** Laban et al., 2025 preprint. A specification spread
  over turns costs 39% on average. https://arxiv.org/abs/2505.06120
- **LLMs Remember First, Forget Last.** Chattaraj and Raj, 2026 preprint. Models return superseded
  values. https://arxiv.org/abs/2603.00270
- **Unable to Forget.** Wang and Sun, 2025 preprint. Proactive interference limits retrieval of
  updated values. https://arxiv.org/abs/2506.08184
- **Teamwork.** Cohen and Levesque, Noûs 1991, read via Tambe, JAIR 1997. A joint goal holds until
  it is known achieved, unachievable, or irrelevant. https://arxiv.org/abs/cs/9709101
- **Common Ground.** Stalnaker, Linguistics and Philosophy 2002. Only what is mutually accepted is
  shared. https://semantics.uchicago.edu/kennedy/classes/f07/pragmatics/stalnaker02.pdf
- **Programming as Theory Building.** Naur, Microprocessing and Microprogramming 1985.
  Documentation cannot carry the program's theory; state where a change goes before editing.
- **Contextual Bias in LLM-Assisted Security Code Review.** Mitropoulos et al., 2026 preprint.
  Author framing defeats review; redaction restored rejections. https://arxiv.org/abs/2603.18740
- **Why Do Multi-Agent LLM Systems Fail?** Cemri et al., 2025 preprint. 12.4% of failure traces
  missed when to stop. https://arxiv.org/abs/2503.13657
- **Quantifying Overclaiming Propensity in Frontier LLM Agents.** Smyth et al., 2026 preprint.
  80.4% of incomplete reviews were reported misleadingly. https://arxiv.org/abs/2609.20812
- Asserting (Brandom) and the critical questions (Walton) above also back micro-skill lines.

## despaghettify

ADR-0015 maps each line to these.

- **SkillsBench.** Li et al., 2026 preprint. Compact and standard skills added 19–21.5 points;
  comprehensive ones added 0.7. Backs the narrow scope and short body. https://arxiv.org/abs/2602.12670
- **Prompting Claude Opus 5, Anthropic** (under wdyt). Recipes for the wanted shape work better
  than prohibitions; backs the pattern-to-rewrite list.
