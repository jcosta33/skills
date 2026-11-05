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
7. If the trace confirms the earlier answer, say so in one line and stop. List an `Unknown` only if
   it could change the answer.
