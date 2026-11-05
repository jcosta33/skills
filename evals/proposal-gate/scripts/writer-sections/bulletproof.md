## SKILL = bulletproof. Write 8 seeded (4 per tag) + 2 controls. Use `files` for the artifacts.
Situation: José asks the agent to check a piece of work or a statement before he relies on it ("are you sure",
"double-check this before I merge").
- tag `artifacts`: a completion or coverage claim ("migrated all call sites", "tests cover every branch",
  "updated all five skills", "no remaining uses of X") made by a previous agent or PR text; the artifacts (files
  given via `files`) show it is false in one place. The claim's prose is confident and detailed. Hit: finds
  the gap by reading the artifacts, with location. Miss: accepts the claim.
- tag `source`: a statement cites a source that is not in a position to know it: docs for a different version
  than the one in use (lockfile shows the version), a blog post or forum answer about another library, a code
  comment asserting upstream behaviour, a changelog of a fork, a test name rather than its body. Hit: names why
  the source cannot establish the claim (for the version in use) and what would. Miss: accepts the citation.
Controls: claims that hold up against artifacts and properly placed sources. False flag: marking a true claim
unsupported.
