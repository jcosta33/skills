#!/usr/bin/env python3
"""Trigger eval adapted from Anthropic skill-creator scripts/run_eval.py.

Same detection, runs, and threshold as run_eval.py. One change: instead of a lone
.claude/commands file, the project holds the full catalog as project skills
(.claude/skills/<name>/SKILL.md), so sibling skills compete as they do when
installed. `claude -p` runs with --setting-sources project, so only these skills
and the harness built-ins are listed. The skill under test carries the
description being measured.
Usage: run_trigger.py PROJECT_DIR SKILL QUERIES.json OUT.json [runs] [workers]
"""
import json, os, select, subprocess, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed

MODEL = "claude-opus-5-5"
CLAUDE = os.environ.get("CLAUDE_BIN", "claude")
TIMEOUT = 90

def run_one(query, skill, project):
    cmd = [CLAUDE, "-p", query, "--output-format", "stream-json", "--verbose",
           "--include-partial-messages", "--model", MODEL, "--setting-sources", "project"]
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    p = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd=project, env=env)
    buf, pending, acc, start = "", None, "", time.time()
    try:
        while time.time() - start < TIMEOUT:
            if p.poll() is not None:
                rest = p.stdout.read()
                if rest: buf += rest.decode("utf-8", "replace")
            else:
                r, _, _ = select.select([p.stdout], [], [], 1.0)
                if not r: continue
                chunk = os.read(p.stdout.fileno(), 8192)
                if not chunk: break
                buf += chunk.decode("utf-8", "replace")
            while "\n" in buf:
                line, buf = buf.split("\n", 1)
                try: ev = json.loads(line)
                except json.JSONDecodeError: continue
                if ev.get("type") == "stream_event":
                    se = ev.get("event", {}); t = se.get("type", "")
                    if t == "content_block_start":
                        cb = se.get("content_block", {})
                        if cb.get("type") == "tool_use":
                            name = cb.get("name", "")
                            if name in ("Skill", "Read"):
                                pending, acc = name, ""
                            else:
                                return (False, f"tool:{name}")
                    elif t == "content_block_delta" and pending:
                        d = se.get("delta", {})
                        if d.get("type") == "input_json_delta":
                            acc += d.get("partial_json", "")
                    elif t in ("content_block_stop", "message_stop"):
                        if pending:
                            try: inp = json.loads(acc)
                            except json.JSONDecodeError: inp = {"raw": acc}
                            target = inp.get("skill") or inp.get("file_path") or inp.get("raw", "")
                            hit = (pending == "Skill" and target.split(":")[-1] == skill) or \
                                  (pending == "Read" and f"/.claude/skills/{skill}/" in target)
                            return (hit, f"{pending}:{target}")
                        if t == "message_stop":
                            return (False, "none")
                elif ev.get("type") == "result":
                    return (False, "none")
            if p.poll() is not None and not buf: break
        return (False, "timeout")
    finally:
        if p.poll() is None:
            p.kill(); p.wait()

def main():
    project, skill, qpath, out = sys.argv[1:5]
    runs = int(sys.argv[5]) if len(sys.argv) > 5 else 3
    workers = int(sys.argv[6]) if len(sys.argv) > 6 else 10
    queries = json.load(open(qpath))
    res = {i: [] for i in range(len(queries))}
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(run_one, q["query"], skill, project): i for i, q in enumerate(queries) for _ in range(runs)}
        for f in as_completed(futs):
            try: res[futs[f]].append(f.result())
            except Exception as e: res[futs[f]].append((False, f"error:{e}"))
    rows = []
    for i, q in enumerate(queries):
        hits = sum(h for h, _ in res[i]); rate = hits / len(res[i])
        ok = rate >= 0.5 if q["should_trigger"] else rate < 0.5
        rows.append({"query": q["query"], "should_trigger": q["should_trigger"], "triggers": hits,
                     "runs": len(res[i]), "rate": rate, "pass": ok, "first_calls": [w for _, w in res[i]]})
    json.dump({"skill": skill, "results": rows, "passed": sum(r["pass"] for r in rows), "total": len(rows)},
              open(out, "w"), indent=1)
    print(f"{skill}: {sum(r['pass'] for r in rows)}/{len(rows)} passed")

if __name__ == "__main__":
    main()
