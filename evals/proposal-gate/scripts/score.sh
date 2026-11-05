#!/bin/sh
# score.sh SKILL IDS REPS : fresh runs, three arms, then grade
cd /tmp/gate
CLAUDE_BIN="$CLAUDE_CODE_EXECPATH" python3 run.py runs/score plain,cur,add $3 6 items/$1.json --ids "$2" > logs_score_$1.txt 2>&1
CLAUDE_BIN="$CLAUDE_CODE_EXECPATH" python3 grade.py runs/score 8 items/$1.json >> logs_score_$1.txt 2>&1
echo DONE >> logs_score_$1.txt
