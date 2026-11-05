import json,glob
T={'arm':[0,0,0,0.0,0],'grader':[0,0,0,0.0,0]}
for f in glob.glob('/tmp/sp/runs/*/*.json'):
    j=json.load(open(f)); k='grader' if f.endswith('.grade.json') else 'arm'
    mu=j.get('_usage' if k=='grader' else 'modelUsage') or {}
    for m in mu.values():
        T[k][0]+=m.get('inputTokens',0)+m.get('outputTokens',0); T[k][1]+=m.get('cacheCreationInputTokens',0); T[k][2]+=m.get('cacheReadInputTokens',0)
    T[k][3]+=j.get('_cost' if k=='grader' else 'cost') or 0; T[k][4]+=1
for k,v in T.items(): print(k,'runs',v[4],'in+out',f"{v[0]:,}",'cache_write',f"{v[1]:,}",'cache_read',f"{v[2]:,}",'$',round(v[3],1))
