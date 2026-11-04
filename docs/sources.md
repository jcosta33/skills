# Sources

Each entry backs a line a skill or the edit contract still carries. Primary sources first; bound
practitioner material by its setup. Remove an entry when its line leaves, and replace a dead link.

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
- **Claude Code skill activation experiment, Ivan Seleznov.** One unpinned setup: directive
  descriptions activated more often. Backs `ALWAYS` in `settle` only.
  https://github.com/SeleznovIvan/claude-skills-test
- **Vercel skills CLI.** Global and per-agent install; `add` does not remove departed skills.
  https://github.com/vercel-labs/skills

## settle

- **ConInstruct.** AAAI 2026. Strong models detect conflicts but rarely ask the user.
  https://ojs.aaai.org/index.php/AAAI/article/view/40356
- **Choice overload meta-analysis.** Scheibehenne, Greifeneder, and Todd, JCR 2010. No universal
  optimum option count; a small set with a recommendation is a convention, not a law.
  https://doi.org/10.1086/651235

## bulletproof and panel

- **Large Language Models Cannot Self-Correct Reasoning Yet.** Huang et al., ICLR 2024. Reasoning
  without external evidence is not verification. https://arxiv.org/abs/2310.01798
- **GPT-4o-generated citations in mental-health literature reviews.** JMIR Mental Health 2025.
  Fabricated citations; check sources directly. https://mental.jmir.org/2025/1/e80371
- **Multiagent Debate.** Du et al., ICML 2024. Bounded independent analysis helps on evaluated
  tasks; more rounds are not always better. https://proceedings.mlr.press/v235/du24e.html
- **Voting or Consensus?** Findings of ACL 2025. No universal aggregation rule; keep dissent.
  https://aclanthology.org/2025.findings-acl.606/

## debloat

- **Token Reduction Is Not Cost Reduction.** Weinberger and Hozez, 2026 preprint. Lossy compression
  damaged exact anchors. https://arxiv.org/abs/2607.12161
- **An Empirical Study on Prompt Compression.** 2025 preprint. Effects are task-dependent.
  https://arxiv.org/abs/2505.00019

## drill

- **sgruetter top-down.** MIT practitioner skill: level order, behavior before machinery, reuse
  first. No `CONTEXT.md` adopted. https://github.com/sgruetter/skills/tree/main/skills/top-down

## revolver

- **Self-Preference Bias in LLM-as-a-Judge.** Wataoka et al., NeurIPS 2024 workshop. Judges favor
  their own output; reviewers must be fresh. https://arxiv.org/abs/2410.21819
- **Primers or reminders?** Spadini, Calikli, and Bacchelli, ICSE 2020. Visible prior comments steer
  later reviewers; hide peer prose. https://doi.org/10.1145/3377811.3380385
