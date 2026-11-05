---
name: despaghettify
description: Rewrite dense or tangled code into plain, readable code without changing behavior. Use only when the user asks to untangle or make code readable, such as chained ternaries, spread-heavy object building, minified-looking one-liners, or deep nesting. Do not use for prose or for changes in behavior.
disable-model-invocation: true
---

# Despaghettify

1. Work on the code the user named, else the current diff. Leave all other code alone.
2. Record behavior first: run the tests that cover the code. If none exist, record what it returns
   for representative inputs.
3. Rewrite in the project's own idioms, formatter, and lint rules:
   - A ternary nested or chained more than once becomes if/else, early returns, or a lookup table.
   - Spread used to merge more than one shallow level, or repeated in a loop, becomes explicit
     assignments or one named merge step.
   - A packed one-liner (long call chain, compound expression, several statements on one line)
     becomes one step per line with named intermediates.
   - Single-letter or abbreviated names outside tiny scopes get names from the project's vocabulary.
   - Deep nesting becomes guard clauses.
   - Control flow hidden in `&&`, `||`, or `??` side effects becomes an explicit if.
4. Keep types, public names, and behavior. Add no dependency and make no unrelated change.
5. Rerun the same checks. Treat any difference as a bug in the rewrite: fix or revert that hunk.
6. Report each change as file:line and the pattern it removed, plus anything left as it was and why.

Done when: the checks match before and after, and none of the patterns in step 3 remains in scope.
