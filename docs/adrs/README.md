# Architecture decision records

One record per load-bearing decision about this catalog: its context, the decision, the rationale,
and the evidence. Form follows the short ADRs of [Corpus](https://github.com/jcosta33/corpus/tree/main/docs/adrs).

An accepted ADR is not edited in place. A changed decision gets a new ADR that names the one it
supersedes or narrows, and this index records the new disposition.

| ADR | Decision | Status |
| --- | --- | --- |
| [ADR-0001](./0001-seven-skill-catalog-and-settle-rename.md) | Cut the catalog to seven skills; ask-user becomes settle | Accepted |
| [ADR-0002](./0002-delete-promote-remember-triple-check.md) | Delete promote, remember and triple-check | Accepted |
| [ADR-0003](./0003-dissect-distinct-from-bulletproof.md) | dissect stays distinct from bulletproof | Accepted |
| [ADR-0004](./0004-revolver-frozen.md) | revolver is conceptually frozen | Accepted |
| [ADR-0005](./0005-no-versioning-single-consumer.md) | No versioning; one consumer | Accepted |
| [ADR-0006](./0006-user-invoked-micro-skills.md) | Micro skills are user-invoked and ship agents/openai.yaml | Accepted |
| [ADR-0007](./0007-no-thinker-or-method-names.md) | Skills carry the plain procedure, never its name | Accepted |
| [ADR-0008](./0008-descriptions-in-the-users-words.md) | Method-skill descriptions use the user's words, gated by a trigger eval | Accepted |
| [ADR-0009](./0009-debloat-keeps-counter-default-rules.md) | debloat cuts default-following rules and keeps counter-default ones | Accepted |
| [ADR-0010](./0010-skills-measured-as-second-passes.md) | Skills are measured as on-demand second passes | Accepted |
| [ADR-0011](./0011-panel-and-bulletproof-fix-texts.md) | Ship the panel and bulletproof second-pass fix texts | Accepted |
| [ADR-0012](./0012-wdyt-judges-the-users-idea.md) | wdyt judges an idea the user proposes | Accepted |
| [ADR-0013](./0013-micro-skill-revisions-from-research.md) | Revise the micro skills from the research | Accepted |
