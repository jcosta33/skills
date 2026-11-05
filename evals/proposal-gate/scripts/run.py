#!/usr/bin/env python3
"""Run eval arms through claude -p. Usage: run.py OUTDIR ARMS(comma) REPS WORKERS ITEMFILE... [--ids a,b]"""
import json, os, subprocess, sys, time, shutil, tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
CLAUDE = os.environ["CLAUDE_BIN"]; MODEL = "claude-opus-5-5"
ARMDIR = "/tmp/gate/arms"
PRE = ("Work only from the material in the user's message and any files in the working directory; "
       "you cannot run commands, edit files, or reach the network. If you dispatch subagents, pin an explicit "
       "model (opus, sonnet, or haiku) on each.")

def prompt_for(item, arm, skill):
    if arm == "plain": return item["request"]
    body = open(f"{ARMDIR}/{skill}.{arm}.md").read()
    return item["request"] + "\n\n---\nUse this skill for the request above:\n\n" + body

def run(item, arm, rep, outdir):
    skill = item["id"].rsplit("-", 1)[0]
    out = f"{outdir}/{item['id']}.{arm}.{rep}.json"
    if os.path.exists(out): return out, "cached"
    wd = tempfile.mkdtemp(prefix=f"{item['id']}.{arm}.{rep}.", dir="/tmp/gate/cwd")
    for p, c in (item.get("files") or {}).items():
        fp = os.path.join(wd, p); os.makedirs(os.path.dirname(fp), exist_ok=True); open(fp, "w").write(c)
    tools = list(item.get("tools") or [])
    if item.get("files"): tools += ["Read", "Grep", "Glob"]
    cmd = [CLAUDE, "-p", prompt_for(item, arm, skill), "--output-format", "stream-json", "--verbose",
           "--model", MODEL, "--setting-sources", "project", "--no-session-persistence",
           "--append-system-prompt", PRE, "--tools", ",".join(tools)]
    if tools: cmd += ["--allowedTools", ",".join(tools)]
    env = {k: v for k, v in os.environ.items() if k not in ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT")}
    t0 = time.time()
    try:
        p = subprocess.run(cmd, stdin=subprocess.DEVNULL, capture_output=True, text=True, cwd=wd, env=env,
                           timeout=1500 if "Agent" in tools else 600)
        lines = p.stdout.splitlines(); err = p.stderr[-2000:]
    except subprocess.TimeoutExpired as e:
        lines = (e.stdout or b"").decode("utf-8", "replace").splitlines() if isinstance(e.stdout, bytes) else (e.stdout or "").splitlines(); err = "TIMEOUT"
    calls, result = [], None
    for ln in lines:
        try: ev = json.loads(ln)
        except Exception: continue
        if ev.get("type") == "assistant":
            for b in ev.get("message", {}).get("content", []):
                if b.get("type") == "tool_use":
                    calls.append({"name": b["name"], "input": b.get("input"), "parent": ev.get("parent_tool_use_id")})
        elif ev.get("type") == "result": result = ev
    rec = {"id": item["id"], "arm": arm, "rep": rep, "wall_s": round(time.time() - t0, 1), "calls": calls,
           "result": (result or {}).get("result"), "duration_ms": (result or {}).get("duration_ms"),
           "usage": (result or {}).get("usage"), "modelUsage": (result or {}).get("modelUsage"),
           "cost": (result or {}).get("total_cost_usd"), "num_turns": (result or {}).get("num_turns"),
           "is_error": (result or {}).get("is_error", True), "stderr": err if not result else ""}
    json.dump(rec, open(out, "w"), indent=1); shutil.rmtree(wd, ignore_errors=True)
    return out, "ok" if result and not rec["is_error"] else "ERR"

def main():
    a = sys.argv[1:]; ids = None
    if "--ids" in a: i = a.index("--ids"); ids = set(a[i+1].split(",")); a = a[:i] + a[i+2:]
    outdir, arms, reps, workers, files = a[0], a[1].split(","), int(a[2]), int(a[3]), a[4:]
    os.makedirs(outdir, exist_ok=True)
    items = [it for f in files for it in json.load(open(f)) if ids is None or it["id"] in ids]
    jobs = [(it, arm, r) for r in range(reps) for it in items for arm in arms]
    with ThreadPoolExecutor(workers) as ex:
        fs = [ex.submit(run, it, arm, r, outdir) for it, arm, r in jobs]
        for f in as_completed(fs):
            o, s = f.result(); print(s, os.path.basename(o), flush=True)
main()
