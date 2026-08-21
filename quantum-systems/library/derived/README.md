# Logically derived library notes

**Origin:** logically derived from the analysis layer (`design`, `requirement`, `design_implication`, `node`, `design_node`).  
**Not effect entries.** Do not add these slugs to [`../INDEX.md`](../INDEX.md). They have no §4.1–4.7 experimental template.

These notes unpack what the twelve machines and the shared requirements already commit to, in one place. Numbers are inherited from formal effect files or marked as class-only. If a derived note disagrees with an effect file, the effect file wins.

Handbook topics that stay **clauses** (not files) are listed in [`../INDEX.md`](../INDEX.md#handbook-topics-not-filed-as-effects).

| File | What it is |
|---|---|
| [design-spec-sheets.md](design-spec-sheets.md) | One sheet per design: a short prose lead-in, then buffer, clock, barrier, hold-power, erase |
| [requirement-audit.md](requirement-audit.md) | Shared requirements: same *kind* of cliff vs same *number*, plus a prose description of each row |
| [operating-envelopes.md](operating-envelopes.md) | Inside of each design’s cliff. Inherited from spec sheets |
| [node-types.md](node-types.md) | Which designs consume which nodes. Not the zoo catalog |
| [analog-slots.md](analog-slots.md) | Latch / loop / partition / leftover map: file vs clause vs hole. Not a catalog. |

To change a sheet, change the analysis CSVs and rebuild, then edit these notes to match. Do not invent a thirteenth design here.
