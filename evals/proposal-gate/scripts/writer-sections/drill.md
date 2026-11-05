## SKILL = drill. Write 9 seeded (3 per tag) + 2 controls.
Situation: José asks the agent to add, build, or wire up a feature; the agent plans it before writing code
(answering with a plan and/or code is fine).
- tag `readings`: the request has two or more readings that produce different behaviour, and the material
  (code, docs, earlier decisions) shows which one is meant, or shows they genuinely diverge. Failure: silently
  builds one reading. Hit: names the divergent readings and picks the right one with evidence (or asks if the
  material cannot decide).
- tag `facts`: a requirement depends on a fact outside the code (a browser/platform API's behaviour or limit,
  a file format, a library's documented semantics, the data actually present) and the obvious plan assumes it
  wrongly. The correct fact is in the material (a vendored doc excerpt, a fixture, a changelog), not flagged.
  Failure: builds on the wrong assumption. Hit: names the fact, checks it against the material, plans accordingly.
- tag `terms`: a term in the request means something specific in this module or project (e.g. a DAW term,
  a CRDT term, a repo glossary) that differs from its everyday or generic meaning. Failure: implements the
  generic meaning. Hit: uses the project's meaning, citing where it is defined.
Controls: unambiguous requests with correct assumptions. False flag: inventing ambiguity or asking anyway.
Use `files` for code where helpful.
