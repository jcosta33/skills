## SKILL = debloat. Write 6 seeded + 2 controls (tag `defaults`).
Situation: José asks the agent to tighten an agent instruction file (an AGENTS.md / CLAUDE.md section, a
skill body, a system prompt) drawn or adapted from his real files.
- tag `defaults`: the file mixes (a) rules a frontier coding model already follows without being told ("write
  clean readable code", "be helpful", "use descriptive variable names", "handle errors appropriately") with
  (b) rules that oppose model defaults ("never add code comments", "never summarise at the end", "do not
  create new files at repo root", "never run git clean", "ask nothing while work remains"). Some (b) rules are
  worded weakly or sit in padded paragraphs, so a tightener is tempted to merge or drop them. Key: list the
  (a) rules that should be cut and the (b) rules that must survive with their force. Hit: cuts most (a), keeps
  every (b). Partial: keeps every (b) but keeps most (a). Miss: drops or softens any (b).
Controls: ordinary prose for humans (README section, PR description) with padding. Right behaviour: tighten
without applying any agent-rule test. False flag: treating it as agent rules or cutting facts.
