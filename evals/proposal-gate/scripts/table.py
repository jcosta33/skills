#!/usr/bin/env python3
"""Aggregate scored runs: per skill/tag/arm points, control flags, tokens, time. Writes CSV + markdown."""
import json, glob, collections, statistics as st, sys
items = {i["id"]: i for f in glob.glob("/tmp/gate/items/*.json") for i in json.load(open(f))}
rows = []
for g in sorted(glob.glob("/tmp/gate/runs/score/*.grade.json")):
    r = json.load(open(g.replace(".grade.json", ".json"))); s = json.load(open(g)); it = items[r["id"]]
    tok = sum(m.get("inputTokens",0)+m.get("outputTokens",0)+m.get("cacheReadInputTokens",0)+m.get("cacheCreationInputTokens",0) for m in (r.get("modelUsage") or {}).values())
    rows.append(dict(id=r["id"], skill=r["id"].rsplit("-",1)[0], tag=it["tag"], kind=it["kind"], arm=r["arm"], rep=r["rep"],
        score=s.get("score"), false_flags=s.get("false_flags"), over_ask=s.get("over_ask"), tokens=tok, wall_s=r["wall_s"], reason=s.get("reason","")))
import csv
with open("/tmp/gate/results.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
P = {"hit":1,"partial":0.5,"miss":0}
agg = collections.defaultdict(lambda: collections.defaultdict(list))
for x in rows:
    agg[(x["skill"], x["arm"])]["all"].append(x)
out = []
for skill in sorted({x["skill"] for x in rows}):
    arms = sorted({a for (s,a) in agg if s==skill}, key=lambda a: ["plain","cur","add","add2","addB"].index(a))
    out.append(f"\n### {skill}\n\n| Arm | Seeded points | Hit / partial / miss | Control runs flagged | Ask on seeded | Mean tokens | Median wall (s) |\n| --- | --- | --- | --- | --- | --- | --- |")
    for a in arms:
        xs = agg[(skill,a)]["all"]; sd=[x for x in xs if x["kind"]=="seeded"]; cn=[x for x in xs if x["kind"]=="control"]
        pts=sum(P.get(x["score"],0) for x in sd)
        c=collections.Counter(x["score"] for x in sd)
        flagged=sum(1 for x in cn if x["score"]!="clean")
        out.append(f"| {a} | {pts:g}/{len(sd)} | {c['hit']} / {c['partial']} / {c['miss']} | {flagged}/{len(cn)} | {sum(1 for x in sd if x['over_ask'])} | {int(st.mean(x['tokens'] for x in xs)):,} | {st.median(x['wall_s'] for x in xs):.0f} |")
    tags = sorted({x["tag"] for x in rows if x["skill"]==skill and x["kind"]=="seeded"})
    if len(tags)>1:
        out.append("\nSeeded points by tag:\n\n| Tag | " + " | ".join(arms) + " |\n| --- |" + " --- |"*len(arms))
        for t in tags:
            cells=[]
            for a in arms:
                sd=[x for x in agg[(skill,a)]["all"] if x["kind"]=="seeded" and x["tag"]==t]
                cells.append(f"{sum(P.get(x['score'],0) for x in sd):g}/{len(sd)}" if sd else "–")
            out.append(f"| {t} | " + " | ".join(cells) + " |")
open("/tmp/gate/tables.md","w").write("\n".join(out)+"\n"); print("\n".join(out))
