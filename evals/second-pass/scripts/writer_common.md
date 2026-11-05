# Task writer brief (second-pass eval)

You write hard, realistic first-pass tasks for Claude Opus agents, each with an answer key written now,
before any run. An agent will receive each task's `request` as its first message and answer it with
read-only tools. A blind grader then labels the answer correct or flawed against your key. We keep the
answers that came out flawed (plus a few correct ones) and study follow-ups on them. You never see the
follow-ups.

## Ground rules

- Do NOT open any `SKILL.md`, anything under `/tmp/gate/` or `/tmp/sp/` except your own output file and
  this brief, any file named `engineering-meaning*.md`, or the skills repo's `evals/` folder. Do not spawn
  subagents. Change nothing outside `/tmp/sp/items/`.
- Repos (read-only snapshots, use these paths when you verify keys):
  - `sd` = `/tmp/snap/sd`, Sourdaw at 95128133a2 (browser DAW: TypeScript, React, Rust→wasm, Automerge
    CRDT, Electron). Full git history available via `git -C /tmp/snap/sd ...`.
  - `sk` = `/tmp/snap/sk`, José's skills repo at e03ea04.
- Agents running your task get: Read, Grep, Glob, and Bash limited to `git log`, `git show`, `git diff`,
  `git blame`, `git grep`, `ls`, `wc`. No edits, no network, no test runs. They start in the repo root.
- Tasks must be HARD: a strong engineer answering in one pass, reasonably fast, should get something
  material wrong or incomplete about a third to a half of the time. Aim at the specific failure in your
  section. Do not plant flaws in the repo; difficulty must come from the real code and history.
- Write requests in José's voice: terse, practical. Never say "test", "eval", or hint at the trap.
- Every key must be verified by you against the snapshot (cite file:line or commit). If you cannot verify
  a key with certainty, drop the task.
- Optional time travel: set `"at": "<sha>"` and `"paths": [...]` to give the agent only those paths as
  they were at that commit, with no git history (use this when HEAD or history would reveal the answer,
  e.g. reviewing a commit that a later commit fixed). Otherwise the agent gets the full snapshot.

## Output

Write a JSON array to `/tmp/sp/items/<SKILL>.json` (valid JSON; check with
`python3 -c 'import json,sys;json.load(open(sys.argv[1]))' FILE`). Each element:

```json
{
  "id": "<SKILL>-01",
  "repo": "sd" | "sk" | null,
  "at": "<sha>" | null,
  "paths": ["src/..."] | null,
  "tools": [] | ["Agent"],
  "request": "the full first message",
  "key": {
    "correct": "what a correct answer must contain or conclude (concrete, checkable)",
    "flaws": "the specific ways an answer is wrong or materially incomplete",
    "evidence": "file:line / commit refs that prove the key"
  },
  "source": "what real material this is built from"
}
```

Finish by replying with the file path, the item count, and one line per item: what makes it hard.
