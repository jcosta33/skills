#!/bin/sh
# pilot.sh SKILL : 3 plain runs per seeded item, then grade
cd /tmp/gate
python3 -c "import json,sys;it=json.load(open('items/$1.json'));print(','.join(i['id'] for i in it if i['kind']=='seeded'))" > /tmp/gate/ids_$1.txt
CLAUDE_BIN="$CLAUDE_CODE_EXECPATH" python3 run.py runs/pilot plain 3 8 items/$1.json --ids "$(cat ids_$1.txt)" > logs_pilot_$1.txt 2>&1
CLAUDE_BIN="$CLAUDE_CODE_EXECPATH" python3 grade.py runs/pilot 8 items/$1.json >> logs_pilot_$1.txt 2>&1
echo DONE >> logs_pilot_$1.txt
