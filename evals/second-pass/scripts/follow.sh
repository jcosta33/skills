#!/bin/sh
# follow.sh SKILL ARMS REPS [WORKERS]
cd /tmp/sp
IDS=$(python3 pick.py $1)
CLAUDE_BIN="$CLAUDE_CODE_EXECPATH" python3 sp.py follow $2 $3 items/$1.json --ids "$IDS" --workers ${4:-6} > logs_follow_$1.txt 2>&1
CLAUDE_BIN="$CLAUDE_CODE_EXECPATH" python3 grade.py follow 8 items/$1.json >> logs_follow_$1.txt 2>&1
echo DONE >> logs_follow_$1.txt
