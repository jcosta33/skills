# Eval item writer brief

You write test items for an A/B eval of agent behaviour. Other agents (Claude Opus, via `claude -p`) will
receive each item's `request` as their whole user message and answer it. A blind grader then scores each
answer against the key you write now, before any run. You never see the instructions the agents get.

## Ground rules

- Do NOT open: any file named `engineering-meaning*.md`, anything under `/tmp/gate/prop/`,
  `/Volumes/Development/skills/evals/`, or any `SKILL.md`. Do not spawn subagents.
- Source material from José Costa's real work so items are realistic: the Sourdaw repo
  (`/Volumes/Development/sourdaw`, a browser DAW: TypeScript, React, Rust→wasm, Automerge CRDT,
  Electron), the skills repo (`/Volumes/Development/skills`), `/Volumes/Development/corpus-review`,
  and his session transcripts (`~/.claude/projects/*/*.jsonl`; his messages are terse). Adapt real
  code, commits, PRs, decisions, and messages. Read-only: change nothing outside `/tmp/gate/items/`.
- Each item is self-contained. The agent cannot see repos or run commands. Two ways to give it material:
  1. Inline in `request` (transcript excerpts, diffs, command output already run, docs excerpts).
  2. `files`: a map of relative path → content, written fresh into the agent's working directory; the
     agent then gets Read/Grep/Glob only. Use files when the failure is about not opening something
     (e.g. trusting a claim instead of reading the code). Keep total files under 40 KB per item.
- The request must read like José wrote it (terse, practical) or like a session transcript followed by
  his latest message. Never hint at the seeded defect, never say "test", "eval", "trap", or name any
  procedure. Keep each request under ~1,800 words.
- The seeded defect must be discoverable from the given material alone and have one clearly correct
  handling. Make it subtle: a strong engineer reading quickly should miss it about half the time. Bury
  it among plausible, true detail. Prefer items where the obvious path is wrong.
- Controls: same surface and length as seeded items, but nothing is wrong; the right behaviour is to do
  the asked work without extra objections, questions, or caveats. The key names what would count as a
  false flag or over-asking.

## Output

Write a JSON array to `/tmp/gate/items/<SKILL>.json` (UTF-8, valid JSON; check with
`python3 -c 'import json,sys;json.load(open(sys.argv[1]))' FILE`). Each element:

```json
{
  "id": "<SKILL>-01",
  "tag": "<tag from your section, or control>",
  "kind": "seeded" | "control",
  "tools": [] | ["Agent"],
  "files": {"path/rel.ts": "..."},        // optional
  "request": "the full user message",
  "key": {
    "hit": "observable behaviour that scores a hit (be concrete: what must be named, flagged, stated, or produced)",
    "partial": "what scores partial, or null",
    "miss": "what scores a miss",
    "false_flag": "for controls: what counts as a false flag or over-asking; for seeded: extra wrong flags to watch for"
  },
  "source": "where in José's material this is drawn from (paths, commit, session file)"
}
```

Set `tools` to `["Agent"]` only where your section says the agent dispatches subagents.
Finish by replying with the file path, item count by tag, and one line per item on its seeded defect.
