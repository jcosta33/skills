---
name: dissect
description: Trace one code path to closure, proving every entry, caller, branch, state change, and effect. Use when the user asks who calls this, what reaches or touches it, how it flows, whether it is dead code, or to figure out what is really happening in some code, even when a quick search seems to answer it. Do not use to check claims or assumptions, or to map a whole area.
---

# Dissect

1. Freeze one question and the repository state.
2. Find every entry: API, command, route, event, job, callback, registry, generated binding, and
   configuration key.
3. Trace callers, including dynamic dispatch, string registration, reflection, and generated call
   sites. Symbol search does not prove reachability; a negative claim needs the search command and
   its result.
4. Trace every branch to its terminal effects: retries, fallbacks, cleanup, cancellation, error
   translation, async continuations, state changes, persistence, caches, and external effects. Then
   invalid input, partial state, concurrency, time, exhaustion, dependency failure, and recovery.
5. Before each probe, write the result that would refute what you expect; count only probes that
   could fail. Claim a cause only from a difference you produced: bisect, revert, or toggle.
6. Return the question, the state, the flow from entry through decisive branches to terminal
   effects, and a table of `path:line`, proven edge, and `Unknown` with the missing proof.
