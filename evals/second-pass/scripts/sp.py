#!/usr/bin/env python3
"""Second-pass eval runner.
first  ITEMFILE... [--ids a,b] [--workers N]            : one first-pass run per item (persisted session)
follow ARMS REPS ITEMFILE... --ids a,b [--workers N]     : resume+fork each item's first-pass session with each arm
ARMS: B (\"Check this again.\"), C (current skill), C2 (proposal skill)"""
import json, os, subprocess, sys, time, uuid, glob
from concurrent.futures import ThreadPoolExecutor, as_completed
CLAUDE = os.environ["CLAUDE_BIN"]; MODEL = "claude-opus-5-5"; ROOT = "/tmp/sp"
BASH_OK = ["Bash(git log:*)", "Bash(git show:*)", "Bash(git diff:*)", "Bash(git blame:*)", "Bash(git grep:*)", "Bash(ls:*)", "Bash(wc:*)"]
PRE = ("You are working in a read-only checkout: you cannot edit files, run tests, or reach the network. "
       "Bash allows only git log/show/diff/blame/grep, ls and wc. If you dispatch subagents, pin an explicit model "
       "(opus, sonnet, or haiku) on each.")


def cwd_for(it):
    if it.get("repo") and it.get("at"):
        d = f"{ROOT}/cwd/{it['id']}"
        if not os.path.exists(d):
            os.makedirs(d)
            p1 = subprocess.Popen(["git", "-C", f"/tmp/snap/{it['repo']}", "archive", it["at"], "--"] + (it.get("paths") or []), stdout=subprocess.PIPE)
            subprocess.run(["tar", "-x", "-C", d], stdin=p1.stdout, check=True); p1.wait()
            subprocess.run(f"find {d} -mindepth 1 -exec chmod a-w {{}} +", shell=True)
        return d
    if it.get("repo"): return f"/tmp/snap/{it['repo']}"
    d = f"{ROOT}/cwd/{it['id']}"; os.makedirs(d, exist_ok=True); return d

def tool_args(it):
    if not it.get("repo"): return ["--tools", ""]
    tools = ["Read", "Grep", "Glob", "Bash"] + (["Agent"] if "Agent" in (it.get("tools") or []) else [])
    allow = ["Read", "Grep", "Glob"] + BASH_OK + (["Agent"] if "Agent" in tools else [])
    return ["--tools", ",".join(tools), "--allowedTools", ",".join(allow)]

def call(prompt, it, extra, timeout):
    cmd = [CLAUDE, "-p", prompt, "--output-format", "stream-json", "--verbose", "--model", MODEL,
           "--setting-sources", "project", "--append-system-prompt", PRE] + tool_args(it) + extra
    env = {k: v for k, v in os.environ.items() if k not in ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT")}
    t0 = time.time()
    try:
        p = subprocess.run(cmd, stdin=subprocess.DEVNULL, capture_output=True, text=True, cwd=cwd_for(it), env=env, timeout=timeout)
        lines, err = p.stdout.splitlines(), p.stderr[-1500:]
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or ""); lines, err = out.splitlines(), "TIMEOUT"
    calls, res = [], None
    for ln in lines:
        try: ev = json.loads(ln)
        except Exception: continue
        if ev.get("type") == "assistant":
            for b in ev.get("message", {}).get("content", []):
                if b.get("type") == "tool_use": calls.append({"name": b["name"], "input": b.get("input"), "parent": ev.get("parent_tool_use_id")})
        elif ev.get("type") == "result": res = ev
    res = res or {}
    return {"wall_s": round(time.time() - t0, 1), "calls": calls, "result": res.get("result"), "session_id": res.get("session_id"),
            "modelUsage": res.get("modelUsage"), "cost": res.get("total_cost_usd"), "is_error": res.get("is_error", True), "stderr": "" if res else err}

def first(it):
    out = f"{ROOT}/runs/first/{it['id']}.json"
    if os.path.exists(out) and not json.load(open(out))["is_error"]: return out, "cached"
    sid = str(uuid.uuid4())
    rec = call(it["request"], it, ["--session-id", sid], 1800 if it.get("tools") else 900); rec.update(id=it["id"], arm="A", sid=sid)
    json.dump(rec, open(out, "w"), indent=1); return out, "ERR" if rec["is_error"] else "ok"

def follow(it, arm, rep):
    skill = it["id"].rsplit("-", 1)[0]; out = f"{ROOT}/runs/follow/{it['id']}.{arm}.{rep}.json"
    if os.path.exists(out) and not json.load(open(out))["is_error"]: return out, "cached"
    fp = json.load(open(f"{ROOT}/runs/first/{it['id']}.json"))
    if arm == "B": msg = "Check this again."
    else:
        body = open(f"{ROOT}/arms/{skill}.{ {'C': 'cur', 'C2': 'add', 'C3': 'c3'}[arm] }.md").read()
        msg = "Apply this skill to your previous answer.\n\n" + body
    rec = call(msg, it, ["--resume", fp["sid"], "--fork-session"], 2400 if it.get("tools") else 900); rec.update(id=it["id"], arm=arm, rep=rep)
    json.dump(rec, open(out, "w"), indent=1); return out, "ERR" if rec["is_error"] else "ok"

def main():
    a = sys.argv[1:]; mode = a.pop(0); ids = None; workers = 6
    if "--ids" in a: i = a.index("--ids"); ids = set(a[i+1].split(",")); del a[i:i+2]
    if "--workers" in a: i = a.index("--workers"); workers = int(a[i+1]); del a[i:i+2]
    os.makedirs(f"{ROOT}/runs/first", exist_ok=True); os.makedirs(f"{ROOT}/runs/follow", exist_ok=True)
    if mode == "first":
        items = [it for f in a for it in json.load(open(f)) if ids is None or it["id"] in ids]
        for it in items: cwd_for(it)
        jobs = [(first, (it,)) for it in items]
    else:
        arms, reps = a[0].split(","), int(a[1]); items = [it for f in a[2:] for it in json.load(open(f)) if ids is None or it["id"] in ids]
        jobs = [(follow, (it, arm, r)) for r in range(reps) for it in items for arm in arms]
    with ThreadPoolExecutor(workers) as ex:
        for f in as_completed([ex.submit(fn, *args) for fn, args in jobs]):
            o, s = f.result(); print(s, os.path.basename(o), flush=True)
main()
