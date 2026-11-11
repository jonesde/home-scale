# Effect library

This directory is the QSA effect library: one Markdown file per macroscopic effect, plus the catalog and the rules for adding more. Constituents (electrons, photons, phonons, …) live in [`nodes/`](nodes/README.md). Those slugs are **not** effect catalog rows; do not add them to [`INDEX.md`](INDEX.md).

Methodology, evaluation criteria, and the locked 7-part body template live in the [top-level README](../README.md). This file is only the operating manual for the files in `library/`.

**Browse:** [INDEX.md](INDEX.md) · [TAXONOMY.md](TAXONOMY.md) · [_template.md](_template.md) · [nodes (not effect entries)](nodes/README.md) · [derived (not effect entries)](derived/README.md) · [applications](../application/README.md) · [orientation / schema](../AGENTS.md)

---

## What an entry is

One file = one macroscopic effect with clear experimental boundaries and a distinct failure envelope.

Each file is a self-contained artifact. It does not assert claims beyond the data and the mapping. Gaps stay visible.

Do not mix working notes, methodology essays, or multi-effect surveys into entry files. Shared vocabulary (buffer, clock, barrier, failure envelope) stays in the top-level README until the same construct is being redefined across several entries.

---

## How to browse

1. Start at [INDEX.md](INDEX.md). Families are the QSA machine/collapse classes, not textbook chapters.
2. Every first-wave row is `formal` and links to a file. `draft` would mean the template is incomplete; `queued` is reserved for names that do not yet have a file.
3. Conventional physics names are in the **Effect** column so search still works. The spine is the family heading.
4. Use the Mapping column before opening a file: High means the collapse translates cleanly; Medium means a recorded gap (statistical buffer, mesoscale step, or a taken rather than derived constant).

Search the files with GitHub search or local `rg` across `library/*.md`. Cross-cutting queries (shared buffers, design membership, open gaps) go through the analysis layer: `python3 analysis/rebuild.py` then `sqlite3 qs-analysis.db`. Notes and example SQL: [../analysis/README.md](../analysis/README.md). The Markdown files remain the science source of truth; the database is a query surface, not a second wiki.

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
| Sources | After Related; the table described under [Sourcing standard](#sourcing-standard) |
| Status | `draft` = template not yet complete or mapping still open; `formal` = all seven sections filled |

`formal` does not yet mean sourced. Sourcing is tracked separately: a file is **sourced** when it has a Sources table and every number in §4.3–§4.4 carries a citation key. The first-wave files were written from model recall with no references; they are being converted one family at a time, and [INDEX.md](INDEX.md) says which are done.

Adding, renaming, or deleting a file means updating [INDEX.md](INDEX.md) in the same change. No orphan files. No index row with a link to a missing file. Queued rows have no file and no link.

Copy [_template.md](_template.md) to start a new entry.

---

## Frontmatter

Keep this schema small. Traceability belongs in §4.3 next to the numbers (a `[S3]` key), with the reference itself in the Sources table at the end of the file, not in a frontmatter `sources:` blob.

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

Conventional handbook names that stay **clauses** (not files) are listed in [INDEX.md](INDEX.md#handbook-topics-not-filed-as-effects). Analog slots (latch / loop / partition / hole) are in [derived/analog-slots.md](derived/analog-slots.md).

---

## Language and evidence

Same rules as the top-level README, restated so they sit next to the files:

1. Every quantitative claim on an effect is traceable to an experimental boundary or a well-established measured parameter. Traceable means a citation key and a Sources row ([Sourcing standard](#sourcing-standard)). Node identity specs (mass, charge, spin) may be taken from a pinned PDG / CODATA edition; they are not collapse cliffs.
2. Effect language is limited to constraints, resources, synchronization, failure thresholds, and emergent output. Node cards may state identity specs without calling those a latch or a family.
3. Interpretive overlays that the data do not require are omitted.
4. Incomplete mappings are stated as incomplete. No conjecture to close a gap. A cataloged particle with no library collapse is unforced, not mapped.
5. Entries may be revised when better data or a tighter constraint analysis appears.

---

## Sourcing standard

Set by the magnet pilot of 2026-11. It exists because the first-wave numbers were recalled by a language model and some were wrong (a factor of ten in the NdFeB blocking size, kelvin written as Celsius). Three tiers stay visibly separate in every file: **sourced fact** (§4.3–§4.4), **mapping** (§4.5–§4.7), and **speculation** (predicted rows in the analysis layer, never in the effect file).

### 1. Fetch, do not recall

A number is entered only after a document that states it has been opened. A model's memory of a handbook is not a source. If the best reference cannot be opened, cite it anyway and say so in the Checked column.

### 2. Evidence tag on every §4.3 bullet

Each bullet starts with one tag. The point is to keep what an instrument read apart from what a theory produced, since this project does not take the theory as given.

| Tag | Meaning |
|---|---|
| **Measured** | Read directly off an experiment: a transition temperature, a loop shift, a resonance line. |
| **Model** (name it) | Obtained by passing measurements through a named model, such as a wall width computed from *A* and *K*. |
| **Convention** | A definition, or an agreed cut on a continuous quantity (25 *kT*, ten-year retention). |
| **Computed here** | Arithmetic done in this file from cited inputs. Show the inputs. Every such number also has a line in [`../analysis/computed_checks.py`](../analysis/computed_checks.py), and the rebuild fails if the two disagree. |

### 3. Citation keys and the Sources table

Put `[S1]`, `[S2]`, … next to the number. Keys are local to the file. The file ends with:

```markdown
## Sources

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Authors, *Journal* vol, page (year)](https://…) | full-text | One line: which numbers or statements in this file rest on it. |
```

`Checked` records how the document itself was verified when the row was written:

| Value | Meaning |
|---|---|
| `full-text` | The document was opened and the value read in it. |
| `abstract` | Only the abstract or landing page was opened; the value appears there. |
| `snippet` | Only a search-result excerpt was seen. Weak; upgrade when possible. |
| `cited-only` | Not opened (paywalled or unavailable). Cited as the standard reference, normally alongside an opened source that states the same value. |

A tertiary source (an encyclopedia, a vendor page) is allowed only when nothing better could be opened, and the Supports cell says "tertiary". A load-bearing number that rests only on `snippet` or `cited-only` rows is named in the file's Data-confidence line.

No literal `|` inside a cell. The rebuild reads this table into `source`, fails on a citation key with no row, and warns on a row that is never cited.

### 4. Threshold or crossover on every failure mode

Each bullet under "Dominant failure modes" in §4.5 is labelled.

| Label | Meaning |
|---|---|
| **Threshold** | The output switches at a definite value: a phase transition or an energy gate. Sharp in the large-system limit. |
| **Crossover** | The output falls off continuously. Give the functional form and its characteristic scale, and name the convention behind any single number quoted. |

Do not call a crossover a cliff. Most size limits in the first wave are crossovers: an exponential or power law cut at an agreed point.

### 5. The same tags in the analysis layer

Fragment rows for a sourced file carry three optional fields: `basis` (`measured` / `model` / `convention` / `computed`), `form` (`threshold` / `crossover`, failure rows only), and `sources` (a list of keys from the file's table). The rebuild fails on a key the file does not define.

### 6. Check the conclusions, not only the numbers

When a file is sourced, each predicted row and each curated requirement status that leans on it is checked against the literature. A predicted row gets a note beginning `Lit check <date>:` and one of **established** (already a measured fact, so not a prediction), **contradicted**, **untested**, or **not checkable**.

---

## Suggested order of work

The catalog is 60 formal entries. Prefer, in order:

0. Source an unsourced family to the standard above. Until that is done its numbers are unverified.
1. Tighten a Medium mapping — especially a missing mesoscale step or a statistical buffer that can be given a sharper experimental envelope.
2. Add a new file only when it has a sharp measured collapse and is not already covered as a clause on an existing entry.
3. Update [INDEX.md](INDEX.md) in the same change as the file.

Do not create empty stub files just to occupy a row.
