# Micro-skill candidates from José's agent history (aggregate summary)

Scan date: 2026-11-05. Read-only scan of 5,174 typed messages across 296 sessions, 2026-03-15 to
2026-11-04. This public copy keeps counts and short recurring phrases only. The full scan, with
verbatim example messages, stays outside this repository.

## Sources

Typed messages kept, per harness history:

- Claude Code prompt history: 2,076. Remaining Claude Code transcripts: 380.
- Codex sessions: 1,593. Codex TUI history: 89, after dedupe.
- Cursor agent transcripts: 768.
- Antigravity transcripts: 172. Orchestrator dispatch prompts were excluded.
- ZCode input history: 96.
- Gemini CLI, OpenCode, Aider Desk and Kilo Code: 0.

The filters dropped tool results, meta and sidechain turns, harness wrappers and boilerplate, slash
commands, pasted logs, and exact duplicates within one minute. Subagent transcripts were excluded.

## Method and caveats

- Intents were clustered with keyword regexes, refined by reading samples, and rechecked with
  3–5-gram counts across sessions. One message can fall into several clusters, so counts are
  approximate.
- Rank = count × the estimated words a skill call replaces. Round trips the skill would prevent are
  not in the score.

## Ranking

| # | Name | Intent | Msgs | Sessions | Range (2026) | Score |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `onward` | Keep working to the stop condition | 555 | 119 | 03-21 to 11-04 | 3,330 |
| 2 | `sitrep` | Status, ETA, what is missing | 122 | 59 | 03-21 to 11-01 | 1,464 |
| 3 | `handoff` | Paste-ready goal or handoff prompt | 61 | 23 | 04-04 to 11-01 | 1,220 |
| 4 | `rearm` | Re-read the rules, sync, resume | 58 | 32 | 04-03 to 11-04 | 1,160 |
| 5 | `scout` | Read-only recon, then report back | 82 | 51 | 03-31 to 11-04 | 1,148 |
| 6 | `proper` | Challenge the fix for hacks and shortcuts | 70 | 39 | 03-21 to 10-31 | 980 |
| 7 | `next` | One recommended next step | 130 | 60 | 03-31 to 11-01 | 910 |
| 8 | `hygiene` | Process hygiene as you go (Sourdaw) | 44 | 22 | 04-04 to 11-01 | 792 |
| 9 | `stepback` | Question the premise | 50 | 30 | 03-27 to 11-01 | 500 |
| 10 | `models` | Justify the subagent model cast | 22 | 19 | 06-13 to 10-30 | 330 |
| 11 | `pace` | Audit effort against output | 25 | 15 | 04-02 to 11-01 | 300 |
| 12 | `ship` | Commit, push, merge, clean up | 35 | 22 | 04-05 to 11-01 | 210 |
| 13 | `quickwins` | Batch the easiest fixes | 13 | 7 | 04-17 to 10-11 | 195 |
| 14 | `whatsthis` | Explain an unfamiliar artifact | 20 | 14 | 04-03 to 10-27 | 160 |
| 15 | `quiet` | Stop messaging; do the work | 14 | 11 | 06-29 to 10-26 | 112 |
| 16 | `salvage` | Keep all code and intent | 10 | 9 | 03-28 to 09-13 | 100 |

## Recurring phrases

- **onward:** a bare "continue", "carry on" or "proceed" in 327 messages across 85 sessions. The
  longer "all the way", "don't stop" or "why did you stop" forms appear in 77 messages across 37
  sessions.
- **scout:** "report back" or "get back to me" in 63 messages across 40 sessions. "learn everything
  there is to know about" in 17 messages across 14 sessions.
- **next:** "what's next?" and its variants, in about 70 messages.
- **rearm:** a pasted skill path next to a reminder to re-read AGENTS.md: 28 messages across 16
  sessions for one path, 22 across 11 for another.
- **stepback:** "in the first place" in 20 messages across 16 sessions. "take a step back" in 14
  across 8.

## Intents already covered (excluded)

| Intent | Msgs | Sessions |
| --- | --- | --- |
| Top-to-bottom, adversarial, or multi-stance review | 174 | 73 |
| Spec, requirements, acceptance work | 181 | 66 |
| "are you sure?", "did you check?", "double check" | 66 | 41 |
| "do research", "empirical" | 60 | 28 |
| "what do you think", "your assessment" | 48 | 29 |
| Complaints about wordy reports | 39 | 17 |
| Agents asking questions the user cannot answer | 14 | 11 |
| "tldr", "be brief" | 14 | 11 |
| Root-cause tracing | 19 | 16 |

## Notes

- The top eight candidates cover about 1,120 messages across most of the 296 sessions.
- For `onward`, `sitrep` and `next`, the value is the round trip prevented, not the typing saved.
- `rearm`, `hygiene` and `models` restate rules already in AGENTS.md or CLAUDE.md. Their recurrence
  shows those rules decay mid-session, and a user-invoked skill re-arms them.
