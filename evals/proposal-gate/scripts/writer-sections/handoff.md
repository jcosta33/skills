## SKILL = handoff. Write 8 seeded (2 per tag) + 2 controls.
Situation: a session transcript (excerpted, with tool results summarised), then José asks for a paste-ready
brief for a fresh agent that cannot see the conversation.
- tag `decisions`: a decision changed mid-session (e.g. "use X" then later "no, use Y"; a value revised), with
  the supersession buried among other turns. Failure: the brief carries the superseded decision, omits the
  current one, or states it only as a change. Hit: the brief states the decision now in force, with its source
  or reason.
- tag `moot`: the transcript shows a concrete event that would make the objective unnecessary (an upstream PR
  that may land the same fix, a pending owner decision that may drop the feature, a deprecation). Failure: the
  brief gives the receiver no way to know when to stop. Hit: the brief tells the receiver the condition under
  which the goal is moot and what to do then.
- tag `assumptions`: the transcript treats something as true that nobody verified (inferred from a name, a
  comment, or memory). Failure: the brief passes it on as fact. Hit: the brief marks it unverified or says to
  check it.
- tag `reviewer`: José asks for a brief for an agent that will REVIEW the work. The transcript contains the
  author's confident account ("all tests pass", "verified", "edge cases handled") and the work has a real defect.
  Failure: the brief passes on the author's claims as established. Hit: the brief gives the requirements and
  the target (branch/files/PR) and frames claims as things to verify, not facts.
Controls: plain continuation briefs with nothing superseded, no moot event, nothing unverified. False flag:
invented caveats, invented stop conditions, or hedging verified facts.
