## SKILL = dissect. Write 30 tasks.
José asks to trace one code path to closure: who calls X (all callers, including indirect, dynamic
dispatch, registries, string-keyed maps, re-exports, barrels, tests excluded or not as he says), what
writes Y, every path from event E to effect F, whether Z is dead, what happens when W fails. Hard =
a plain grep misses entries (aliases, re-exports, generated code, wasm bindings, handler maps, IPC
channels, dynamic imports) or includes false ones. Key: the exact complete set / path, with file:line.
