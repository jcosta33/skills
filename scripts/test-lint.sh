#!/bin/sh
# Prove scripts/lint.sh still bites: each mutation must make it fail.
set -eu
export LC_ALL=C

ROOT=$(CDPATH= cd -- "${1:-$(dirname -- "$0")/..}" && pwd)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT HUP INT TERM

sh "$ROOT/scripts/lint.sh" "$ROOT" >/dev/null

skill=$(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort | head -n 1)
other=$(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort | sed -n 2p)
micro=$(find "$ROOT/skills" -mindepth 3 -maxdepth 3 -path '*/agents/openai.yaml' | sort | head -n 1 | awk -F/ '{ print $(NF - 2) }')
[ -n "$micro" ] || { echo "test-lint: no user-invoked skill to mutate" >&2; exit 1; }

for case in \
  'missing-skill:README catalog does not match' \
  'extra-file:holds something other than SKILL.md' \
  'nested-file:nested payload' \
  'symlink:holds something other than SKILL.md' \
  'yaml-colon:invalid frontmatter' \
  'bad-invocation:invalid frontmatter' \
  'unknown-key:unknown frontmatter key' \
  'angle-bracket:invalid frontmatter' \
  'missing-yaml:needs agents/openai.yaml' \
  'bad-yaml:needs agents/openai.yaml' \
  'stray-agents:agents/ without' \
  'agents-extra:nested payload' \
  'self-name:names its own skill' \
  'sibling-name:names sibling skill' \
  'broken-link:broken link'; do
  mutation=${case%%:*}
  expected=${case#*:}
  fixture="$TMP/$mutation"
  mkdir -p "$fixture"
  cp -R "$ROOT/README.md" "$ROOT/AGENTS.md" "$ROOT/skills" "$ROOT/scripts" "$fixture/"
  [ -d "$ROOT/docs" ] && cp -R "$ROOT/docs" "$fixture/"
  file="$fixture/skills/$skill/SKILL.md"

  case "$mutation" in
    missing-skill) rm -r "$fixture/skills/$skill" ;;
    extra-file) printf 'x\n' > "$fixture/skills/$skill/notes.md" ;;
    nested-file) mkdir "$fixture/skills/$skill/references" && printf 'x\n' > "$fixture/skills/$skill/references/x.md" ;;
    symlink) ln -s SKILL.md "$fixture/skills/$skill/alias.md" ;;
    yaml-colon) sed 's/^description: .*/description: Broken: YAML/' "$file" > "$file.tmp" && mv "$file.tmp" "$file" ;;
    bad-invocation) sed 's/^name: .*/&\
disable-model-invocation: yes/' "$file" > "$file.tmp" && mv "$file.tmp" "$file" ;;
    unknown-key) sed 's/^name: .*/&\
license: MIT/' "$file" > "$file.tmp" && mv "$file.tmp" "$file" ;;
    angle-bracket) sed 's/^description: .*/& Use for <tags>./' "$file" > "$file.tmp" && mv "$file.tmp" "$file" ;;
    missing-yaml) rm "$fixture/skills/$micro/agents/openai.yaml" ;;
    bad-yaml) printf 'policy:\n  allow_implicit_invocation: true\n' > "$fixture/skills/$micro/agents/openai.yaml" ;;
    stray-agents) mkdir "$fixture/skills/$skill/agents" && cp "$ROOT/skills/$micro/agents/openai.yaml" "$fixture/skills/$skill/agents/" ;;
    agents-extra) printf 'x\n' > "$fixture/skills/$micro/agents/notes.md" ;;
    self-name) sed "s/^description: .*/description: Use $skill now./" "$file" > "$file.tmp" && mv "$file.tmp" "$file" ;;
    sibling-name) printf '\nThen run %s.\n' "$other" >> "$file" ;;
    broken-link) printf '\n[gone](./missing.md)\n' >> "$fixture/README.md" ;;
  esac

  if output=$(sh "$fixture/scripts/lint.sh" "$fixture" 2>&1); then
    echo "test-lint: mutation survived: $mutation" >&2
    exit 1
  fi
  case "$output" in
    *"$expected"*) ;;
    *)
      echo "test-lint: $mutation failed for the wrong reason: $output" >&2
      exit 1
      ;;
  esac
done

echo "test-lint: OK (15 mutations killed)"
