"""Export per-run data and per-arm summary for evals/second-pass."""
import json, glob, csv, collections, statistics as st, sys, os
OUT = sys.argv[1]
SK = ['panel', 'settle', 'bulletproof', 'dissect', 'revolver', 'drill', 'handoff']
REPS = {'panel': 3, 'settle': 3}  # others capped at 2
REPS_ARM = {('panel', 'C3'): 2, ('settle', 'C3'): 2}

def toks(mu):
    mu = mu or {}
    g = lambda k: sum(m.get(k, 0) for m in mu.values())
    return g('inputTokens') + g('outputTokens'), g('cacheCreationInputTokens'), g('cacheReadInputTokens')

first_rows = []
for sk in SK:
    for f in sorted(glob.glob(f'/tmp/sp/runs/first/{sk}-*.grade.json')):
        r = json.load(open(f.replace('.grade', ''))); g = json.load(open(f))
        io, cw, cr = toks(r.get('modelUsage'))
        first_rows.append(dict(skill=sk, id=os.path.basename(f).split('.')[0], label=g.get('label'),
                               io=io, cache_write=cw, cache_read=cr, usd=round(r.get('cost') or 0, 4),
                               wall_s=round(r.get('wall_s') or 0, 1), grader_reason=g.get('reason', '')))
with open(f'{OUT}/first.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(first_rows[0])); w.writeheader(); w.writerows(first_rows)

fol_rows = []
for sk in SK:
    sel = json.load(open(f'/tmp/sp/sel_{sk}.json'))
    kind = {i: 'flawed' for i in sel['flawed']}; kind.update({i: 'correct' for i in sel['correct']})
    for f in sorted(glob.glob(f'/tmp/sp/runs/follow/{sk}-*.grade.json')):
        r = json.load(open(f.replace('.grade', ''))); g = json.load(open(f))
        if r['id'] not in kind or r.get('is_error'): continue
        if int(r['rep']) >= REPS_ARM.get((sk, r['arm']), REPS.get(sk, 2)): continue
        io, cw, cr = toks(r.get('modelUsage'))
        fol_rows.append(dict(skill=sk, id=r['id'], kind=kind[r['id']], arm=r['arm'], rep=r['rep'],
                             outcome=g.get('outcome'), new_errors=g.get('new_errors', ''), io=io,
                             cache_write=cw, cache_read=cr, usd=round(r.get('cost') or 0, 4),
                             wall_s=round(r.get('wall_s') or 0, 1), grader_reason=g.get('reason', '')))
with open(f'{OUT}/follow.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(fol_rows[0])); w.writeheader(); w.writerows(fol_rows)

d = collections.defaultdict(list)
for r in fol_rows: d[(r['skill'], r['arm'], r['kind'])].append(r)
summ = []
for sk in SK:
    fl = [r for r in first_rows if r['skill'] == sk]
    for arm in ['B', 'C', 'C2', 'C3']:
        f, c = d.get((sk, arm, 'flawed'), []), d.get((sk, arm, 'correct'), [])
        if not f and not c: continue
        oc = collections.Counter(r['outcome'] for r in f); cc = collections.Counter(r['outcome'] for r in c)
        allr = f + c
        summ.append(dict(skill=sk, arm=arm, first_correct=f"{sum(r['label']=='correct' for r in fl)}/{len(fl)}",
            flawed_runs=len(f), fixed=oc['fixed'], partial=oc['partial'], unfixed=oc['unfixed'], worse=oc['worse'],
            fix_points=f"{oc['fixed'] + 0.5*oc['partial']:g}", fix_rate=round((oc['fixed'] + 0.5*oc['partial'])/len(f), 2) if f else '',
            correct_runs=len(c), kept=cc['kept'], churn=cc['churn'], flipped=cc['flipped'],
            churn_rate=round((cc['churn']+cc['flipped'])/len(c), 2) if c else '',
            mean_io=int(st.mean(r['io'] for r in allr)), mean_cache_write=int(st.mean(r['cache_write'] for r in allr)),
            mean_cache_read=int(st.mean(r['cache_read'] for r in allr)), mean_usd=round(st.mean(r['usd'] for r in allr), 3),
            median_wall_s=int(st.median(r['wall_s'] for r in allr))))
with open(f'{OUT}/summary.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(summ[0])); w.writeheader(); w.writerows(summ)
for s in summ: print(s['skill'], s['arm'], 'fix', s['fix_points'], '/', s['flawed_runs'], f"(f{s['fixed']} p{s['partial']} u{s['unfixed']} w{s['worse']})", 'churn', s['churn'], '+flip', s['flipped'], '/', s['correct_runs'], 'io', s['mean_io'], '$', s['mean_usd'], 'wall', s['median_wall_s'])
