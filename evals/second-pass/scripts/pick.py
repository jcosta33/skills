import json,glob,sys,random,os
sk=sys.argv[1]; fl=[];co=[]
for f in sorted(glob.glob(f'/tmp/sp/runs/first/{sk}-*.grade.json')):
    g=json.load(open(f)); i=f.split('/')[-1].replace('.grade.json','')
    (fl if g.get('label')=='flawed' else co if g.get('label')=='correct' else []).append(i)
p=f'/tmp/sp/sel_{sk}.json'
old=json.load(open(p)) if os.path.exists(p) else {'flawed':[],'correct':[]}
rnd=random.Random(7); rnd.shuffle(fl); rnd.shuffle(co)
F=list(old['flawed'])+[x for x in fl if x not in old['flawed']][:max(0,10-len(old['flawed']))]
C=list(old['correct'])+[x for x in co if x not in old['correct']][:max(0,5-len(old['correct']))]
json.dump({'flawed':sorted(F),'correct':sorted(C)},open(p,'w'))
print(','.join(sorted(F)+sorted(C)))
