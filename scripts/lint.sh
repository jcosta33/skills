#!/bin/sh
# Structural gate for this catalog. Usage: sh scripts/lint.sh [repo-root]
set -eu
export LC_ALL=C

ROOT=$(CDPATH= cd -- "${1:-$(dirname -- "$0")/..}" && pwd)

fail() {
  echo "lint: $*" >&2
  exit 1
}

# Manifest: every skill folder has exactly one README catalog row, label equal to target.
skills=$(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort)
rows=$(sed -nE 's#^\| \[`([^`]+)`\]\(\./skills/([^/]+)/SKILL\.md\).*$#\1 \2#p' "$ROOT/README.md")
catalog=$(printf '%s\n' "$rows" | awk 'NF { print ($1 == $2 ? $1 : "label-mismatch:" $1) }' | sort)
[ -n "$skills" ] || fail "skills/ is empty"
[ "$skills" = "$catalog" ] || fail "README catalog does not match skills/"

# Payload: one regular SKILL.md per folder, plus agents/openai.yaml for a user-invoked skill.
[ -z "$(find "$ROOT/skills" -mindepth 4)" ] || fail "nested payload under skills/"
[ -z "$(find "$ROOT/skills" -mindepth 3 -maxdepth 3 ! \( -type f -path '*/agents/openai.yaml' \))" ] ||
  fail "nested payload under skills/"
[ -z "$(find "$ROOT/skills" -mindepth 2 -maxdepth 2 ! \( -type f -name SKILL.md \) ! \( -type d -name agents \))" ] ||
  fail "skill folder holds something other than SKILL.md"

for name in $skills; do
  file="$ROOT/skills/$name/SKILL.md"
  [ -f "$file" ] || fail "missing $file"

  # Frontmatter: exactly name (= folder) and a one-line, YAML-safe description; optionally
  # disable-model-invocation (outside the spec; claude.ai uploads reject it). No other key.
  key=$(awk 'NR > 1 && $0 == "---" { exit } NR > 1 && !/^(name|description|disable-model-invocation): / { print; exit }' "$file")
  [ -z "$key" ] || fail "unknown frontmatter key in $name: $key"
  awk -v expected="$name" '
    NR == 1 { if ($0 != "---") exit 1; inside = 1; next }
    inside && $0 == "---" { closed = 1; exit }
    inside && /^name: / { names++; if (substr($0, 7) != expected) exit 1; next }
    inside && /^description: / {
      value = substr($0, 14); descriptions++
      if (length(value) > 1024 || value !~ /^[[:alpha:]]/ || value ~ /:[[:space:]]/ || value ~ /[[:space:]]#/ || value ~ /[<>]/) exit 1
      next
    }
    inside && /^disable-model-invocation: (true|false)$/ { invocations++; next }
    inside { exit 1 }
    END { if (!closed || names != 1 || descriptions != 1 || invocations > 1) exit 1 }
  ' "$file" || fail "invalid frontmatter: $name"

  # A user-invoked skill also tells Codex: agents/openai.yaml holds exactly the policy below.
  yaml="$ROOT/skills/$name/agents/openai.yaml"
  if grep -qx 'disable-model-invocation: true' "$file"; then
    [ -f "$yaml" ] && [ "$(cat "$yaml")" = "$(printf 'policy:\n  allow_implicit_invocation: false')" ] ||
      fail "user-invoked skill needs agents/openai.yaml with allow_implicit_invocation false: $name"
  elif [ -e "$ROOT/skills/$name/agents" ]; then
    fail "agents/ without disable-model-invocation: true: $name"
  fi

  description=$(sed -n 's/^description: //p' "$file" | head -n 1)
  if printf '%s\n' "$description" | grep -Eqi "(^|[^[:alnum:]-])$name([^[:alnum:]-]|$)"; then
    fail "description names its own skill: $name"
  fi

  # Standalone: no sibling names, no relative links out of the folder.
  for other in $skills; do
    [ "$other" = "$name" ] && continue
    if grep -Eqi "(^|[^[:alnum:]-])$other([^[:alnum:]-]|$)" "$file"; then
      fail "$name names sibling skill $other"
    fi
  done
  # Plain steps only: no thinker, school, or method names anywhere in a skill.
  if grep -Eiq "(^|[^[:alnum:]])(philosoph[a-z]*|plato(nic)?|socrat(es|ic)|aristotle|kant(ian)?|popper(ian)?|peirce|mill's|hume|stoics?|disputatio|dialectic(al|s)?|pre-?mortems?|steel-?man(ning|ned)?|devil'?s advocate|antinom(y|ies)|diairesis|toulmin|wittgenstein|grice|leibniz|descartes|hegel)([^[:alnum:]]|\$)" "$file"; then
    fail "$name names a thinker or method; ship the plain steps"
  fi
  if grep -Eq '\]\([^)#:]*\)' "$file"; then
    fail "$name has a relative link"
  fi
done

# Links: inline only, and every relative target exists.
for doc in "$ROOT/README.md" "$ROOT/AGENTS.md" "$ROOT"/docs/*.md; do
  [ -f "$doc" ] || continue
  if grep -nE '\]\[[^]]*\]|^[[:space:]]*\[[^]]+\]:|\]\(<' "$doc"; then
    fail "reference-style or angle-bracket link in $doc"
  fi
  dir=$(dirname "$doc")
  for target in $(grep -oE '\]\([^)]+\)' "$doc" | sed -E 's/^\]\(([^)#?]*).*/\1/' | grep -vE '^$|^[[:alpha:]][[:alnum:]+.-]*:'); do
    [ -e "$dir/$target" ] || fail "broken link in $doc: $target"
  done
done

echo "lint: OK ($(printf '%s\n' "$skills" | wc -l | tr -d ' ') skills)"
