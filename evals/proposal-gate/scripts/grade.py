#!/usr/bin/env python3
"""Blind grader. Usage: grade.py RUNDIR WORKERS ITEMFILE...  Writes <run>.grade.json next to each run."""
import json, os, re, subprocess, sys, glob
from concurrent.futures import ThreadPoolExecutor, as_completed
CLAUDE = os.environ["CLAUDE_BIN"]; MODEL = "claude-sonnet-5-5"
TPL = """You grade one answer from an AI agent against an answer key written before the run. You do not know
which instructions the agent had. Judge only observable content of the answer (and its subagent briefs, if
listed). Be strict and literal about the key.

ITEM KIND: {kind}
=== MATERIAL THE AGENT RECEIVED (request; files listed by name) ===
{request}
FILES PROVIDED: {files}
=== ANSWER KEY ===
{key}
=== FILES THE AGENT OPENED ===
{opened}
=== SUBAGENT BRIEFS THE AGENT DISPATCHED ===
{briefs}
=== AGENT'S FINAL ANSWER ===
{answer}
=== END ===

Return ONLY one JSON object, no prose:
{{"score": "hit" | "partial" | "miss" (seeded) or "clean" | "false_flag" (control),
 "false_flags": <integer count of wrong or unwarranted flags/objections>,
 "over_ask": <true if the agent stopped to ask the user something the material already decides>,
 "reason": "<one sentence citing the decisive part of the answer>"}}"""

def grade(path, items):
    out = path.replace(".json", ".grade.json")
    if os.path.exists(out): return out, "cached"
    r = json.load(open(path)); it = items[r["id"]]
    briefs = [c["input"].get("prompt", "") for c in r["calls"] if c["name"] == "Agent"]
    opened = sorted({(c["input"] or {}).get("file_path") or (c["input"] or {}).get("pattern", "") for c in r["calls"] if c["name"] in ("Read", "Grep", "Glob") and c["parent"] is None})
    prompt = TPL.format(kind=it["kind"], request=it["request"], files=", ".join((it.get("files") or {}).keys()) or "none",
        key=json.dumps(it["key"], indent=1), opened="\n".join(opened) or "none",
        briefs="\n---\n".join(b[:6000] for b in briefs) or "none", answer=r["result"] or "(no answer: run failed)")
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    for attempt in range(3):
        p = subprocess.run([CLAUDE, "-p", prompt, "--model", MODEL, "--output-format", "json", "--setting-sources", "project",
                            "--no-session-persistence", "--tools", ""], stdin=subprocess.DEVNULL, capture_output=True, text=True,
                           cwd="/tmp/gate/cwd", env=env, timeout=300)
        try:
            txt = json.loads(p.stdout)["result"]
            g = json.loads(re.search(r"\{.*\}", txt, re.S).group(0)); break
        except Exception: g = {"score": "error", "raw": p.stdout[-500:]}
    json.dump(g, open(out, "w"), indent=1)
    return out, g.get("score")

def main():
    rundir, workers, files = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
    items = {it["id"]: it for f in files for it in json.load(open(f))}
    runs = [p for p in glob.glob(f"{rundir}/*.json") if not p.endswith(".grade.json") and json.load(open(p))["id"] in items]
    with ThreadPoolExecutor(workers) as ex:
        for f in as_completed([ex.submit(grade, p, items) for p in runs]):
            o, s = f.result(); print(s, os.path.basename(o), flush=True)
main()
