#!/bin/sh
cd /tmp/sp
CLAUDE_BIN="$CLAUDE_CODE_EXECPATH" python3 sp.py first items/$1.json --workers ${2:-6} > logs_first_$1.txt 2>&1
CLAUDE_BIN="$CLAUDE_CODE_EXECPATH" python3 grade.py first 8 items/$1.json >> logs_first_$1.txt 2>&1
echo DONE >> logs_first_$1.txt
