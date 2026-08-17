# Logically derived library notes

**Origin:** logically derived from the analysis layer (`design`, `requirement`, `design_implication`).  
**Not effect entries.** Do not add these slugs to [`../INDEX.md`](../INDEX.md). They have no §4.1–4.7 experimental template.

These notes unpack what the nine machines and the shared requirements already commit to, in one place. Numbers are inherited from formal effect files or marked as class-only. If a derived note disagrees with an effect file, the effect file wins.

| File | What it is |
|---|---|
| [design-spec-sheets.md](design-spec-sheets.md) | One sheet per design: buffer, clock, barrier, hold-power, erase |
| [requirement-audit.md](requirement-audit.md) | Shared requirements: same *kind* of cliff vs same *number* |

To change a sheet, change the analysis CSVs and rebuild, then edit these notes to match. Do not invent a tenth design here.
