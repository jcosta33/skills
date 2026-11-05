---
name: debloat
description: Tighten supplied prose without losing any fact, rule, or warning. Use only when the user asks to tighten, trim, or cut padding from a document, instruction file, or message. Do not use for source code, commit messages, or forms a repository prescribes.
disable-model-invocation: true
---

# Debloat

1. Before editing, list every fact, rule, command, identifier, warning, and required heading the text
   carries.
2. Give each item one home. Cut duplicates, recaps, hedges, pleasantries, and sentences that change no
   action or decision.
3. If the text instructs an agent, cut each rule the model follows without being told, and keep the
   rules that oppose its defaults. Write each remaining rule as "If C, do X" with no hedge, put the
   most important rules first, and flag rules that contradict each other or no longer match the code.
   If more than ten load-bearing rules remain, name the ones you would cut instead of cutting them.
4. Check the result against the list and restore anything missing, except the rules cut in step 3.
