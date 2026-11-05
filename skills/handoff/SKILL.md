---
name: handoff
description: Write a paste-ready brief so a fresh agent can continue this work. Use only when the user asks for a handover or goal prompt, or to pass the work to another agent.
disable-model-invocation: true
---

# Handoff

Answer in chat with one fenced, paste-ready prompt for an agent that cannot see this conversation;
write no file. Focus it on what the user named, if anything.
Include: objective, stop condition, and any condition that makes the goal moot; what is done and
verified, with PR and issue references; what remains, in order; open decisions; traps found; the
likely next change and where it belongs; rules and skills to read first; lanes and branches to
leave alone.
List every decision in force as one full list, each with its source and reason. Mark an assumption
unchecked only when this session did not verify it.
If the receiver will review the work, give it the requirements and the target, not the author's
account of the work.
Point to files, commits, PRs, and issues by path or URL instead of copying them. Drop anything
finished or no longer true. No secrets.
