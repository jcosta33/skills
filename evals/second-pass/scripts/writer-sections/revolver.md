## SKILL = revolver. Write 30 tasks. Set "tools": ["Agent"].
José asks for a thorough review of a real past change. Use real Sourdaw (or skills) commits that a later
commit fixed, reverted, or corrected (search history for "fix", "revert", "regression", "follow-up",
issue references). Use time travel: `at` = the buggy commit, `paths` = the files needed (changed files
plus the callers needed to see the bug), and put the commit's diff and message inline in the request.
The key is the real defect the later commit fixed (cite the fixing commit). Include some commits whose
defect is subtle (interaction with code outside the diff). Do not include fixes for pure typos/format.
