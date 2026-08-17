# Effect library

This directory is the QSA effect library: one Markdown file per macroscopic effect, plus the catalog and the rules for adding more.

Methodology, evaluation criteria, and the locked 7-part body template live in the [top-level README](../README.md). This file is only the operating manual for the files in `library/`.

**Browse:** [INDEX.md](INDEX.md) · [TAXONOMY.md](TAXONOMY.md) · [_template.md](_template.md)

---

## What an entry is

One file = one macroscopic effect with clear experimental boundaries and a distinct failure envelope.

Each file is a self-contained artifact. It does not assert claims beyond the data and the mapping. Gaps stay visible.

Do not mix working notes, methodology essays, or multi-effect surveys into entry files. Shared vocabulary (buffer, clock, barrier, failure envelope) stays in the top-level README until the same construct is being redefined across several entries.

---

## How to browse

1. Start at [INDEX.md](INDEX.md). Families are the QSA machine/collapse classes, not textbook chapters.
2. `formal` rows link to a finished file. `queued` rows are the worklist — intended slug and collapse note only, no file yet.
3. Conventional physics names are in the **Effect** column so search still works. The spine is the family heading.

GitHub search and local `rg` across `library/*.md` are the search tools. There is no database.

---

## File conventions

| Rule | Detail |
|---|---|
| Name | `kebab-case.md`, stable, no numeric prefixes |
| `id` | Same as the filename without `.md` |
| Title / §4.1 | Conventional name, optional QSA gloss in parentheses |
| Links | Relative Markdown only, and only to files that exist |
| Body | Locked 7-part template from the top-level README |
| Related | After the seven sections; queued slugs as `code`, not broken links |
| Status | `draft` = template not yet complete or mapping still open; `formal` = all seven sections filled and claims sourced |

Adding, renaming, or deleting a file means updating [INDEX.md](INDEX.md) in the same change. No orphan files. No index row with a link to a missing file. Queued rows have no file and no link.

Copy [_template.md](_template.md) to start a new entry.

---

## Frontmatter

Keep this schema small. Traceability belongs in §4.3 next to the numbers, not in a `sources:` blob.

```yaml
---
id: slug
title: Conventional Name (Optional QSA Gloss)
status: draft          # or formal
family: collective-field-response
constraints:
  - spatial-buffer
confidence_data: high     # high | medium | low
confidence_mapping: high  # high | medium | low | unmapped
related:
  - other-slug
updated: YYYY-MM-DD
---
```

- `family` is singular: the primary home in the index. Assignment rule is in [TAXONOMY.md](TAXONOMY.md).
- `constraints` are the cross-cuts. Allowed tags (do not invent new ones without updating this list):

  `spatial-buffer` · `clock-latency` · `energy-barrier` · `mechanical-lattice` · `field-threshold` · `thermal`

- `related` may include queued slugs. Link in the body only if that file exists.
- `confidence_mapping: unmapped` is for queued index rows and for a draft that has not yet attempted §4.5.

---

## Index discipline

[INDEX.md](INDEX.md) is both the catalog and the build list.

| Column | Meaning |
|---|---|
| Effect | Conventional name; link if the file exists |
| Slug | Stable filename stem |
| Status | `formal` / `draft` / `queued` |
| Data | Confidence in the experimental numbers |
| Mapping | Confidence in the QSA translation (`—` if unmapped) |
| Dominant collapse | The threshold that kills the macro effect |
| Notes | One-line macro fact, so the table is usable without opening a file |

When a queued row is written, flip `Status`, fill `Mapping`, and turn **Effect** into a link. Do not create empty stub files just to occupy a row.

---

## Language and evidence

Same rules as the top-level README, restated so they sit next to the files:

1. Every quantitative claim is traceable to an experimental boundary or a well-established measured parameter.
2. Language is limited to constraints, resources, synchronization, failure thresholds, and emergent output.
3. Interpretive overlays that the data do not require are omitted.
4. Incomplete mappings are stated as incomplete. No conjecture to close a gap.
5. Entries may be revised when better data or a tighter constraint analysis appears.

---

## Suggested order of work

Write one formal entry at a time. Prefer the next candidate that has (a) a sharp measured collapse and (b) a machine class not already covered, or that completes a pair with an existing file (for example plasma-frequency cutoff next to reflection, superparamagnetism next to the magnet latch).

The **Suggested next** list at the top of the index is the short queue. The family tables are the longer backlog.
