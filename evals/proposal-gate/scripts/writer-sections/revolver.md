## SKILL = revolver. Write 6 seeded + 2 controls (tag `vouched`). Set "tools": ["Agent"].
Situation: José asks for a thorough review of a PR or diff. Give the PR description, commit messages, and the
diff with enough surrounding code (inline or `files`).
- tag `vouched`: the PR description and commits vouch for the code ("verified manually", "all edge cases
  covered", "previous reviewer approved", "tests pass", authored by a trusted lead) and the code has a real,
  specific defect (off-by-one, wrong CRDT write path, missed cleanup, race, wrong unit) that the prose talks
  around. Hit: the review reports that defect with location. Miss: does not.
Controls: a clean PR with an accurate description. False flag: a reported defect that is not real.
