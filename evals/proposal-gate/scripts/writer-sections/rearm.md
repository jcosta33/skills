## SKILL = rearm. Write 6 seeded + 2 controls (tag `location`).
Situation: the agent inherits work-in-progress written by another agent (a branch, partly done), and José says
to get back up to speed and continue. Give the repo rules (an AGENTS.md excerpt), the goal, the branch's
commits/diff, and the relevant code via `files`. The next step requires a change.
- tag `location`: the inherited structure dictates where the next change must go (a registry, an action layer,
  a dispatcher, a schema owner, a generated file's source), and the obvious spot is wrong (edits a generated
  file, writes to the document outside the action layer, duplicates an existing helper, patches the caller
  instead of the owner). Failure: plans or makes the change in the wrong place. Hit: names the correct location
  and why, grounded in the code.
Controls: inherited work where the obvious spot is right. False flag: needless restructuring or questions.
