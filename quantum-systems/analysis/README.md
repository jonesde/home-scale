# QSA analysis layer

Markdown in [`library/`](../library/) is the science source of truth. This directory is the derived analysis layer: a queryable reading of the QSA mappings, not a second wiki.

Working database: `qs-analysis.db` at the repo root. It is a local build artifact (gitignored). Commit the text: `fragments/*.jsonl`, `implication.csv`, `schema.sql`.

First load: 49 `effect` rows, 145 `effect_constraint` rows, 386 `implication` rows (about eight per file). 144 implications carry a `value_si`. 66 are `open` or `gap`. 11 are zero-power outputs.

Rebuild (stdlib Python 3 only — no pip):

```bash
python3 analysis/rebuild.py
```

That is the whole shot. It merges `fragments/*.jsonl` → `implication.csv` when fragments are present, rebuilds `effect` / `effect_constraint` from library frontmatter, loads `implication.csv`, writes `seed_effect.sql` for inspection, and writes `qs-analysis.db`. `merge_fragments.py` still exists if you only want the CSV.

Edit the per-family files in `fragments/` (one JSON object per line). Do not hand-edit `implication.csv` or `seed_effect.sql`. The Markdown is never generated from the database. Fragments are never generated from the Markdown by regex. Extraction is interpretive.

---

## Tables

| Table | Grain | Source |
|---|---|---|
| `effect` | one row per formal library file | frontmatter (mechanical) |
| `effect_constraint` | one row per constraint tag on an effect | frontmatter (mechanical) |
| `implication` | one atomic mapping claim | curated `implication.csv` |

Table names are singular. IDs are slugs: `effect.slug` and `implication.impl_key` (`{slug}:{clause}:{short-name}`).

---

## `implication` columns

| Column | Meaning |
|---|---|
| `impl_key` | Stable primary key |
| `effect_slug` | Join to `effect.slug` |
| `source_path` | `library/{slug}.md` |
| `clause` | Which heading the claim came from |
| `role` | `requirement` / `failure` / `output` / `gap` |
| `aspect` | Kind of spec: scale, capacity, speed, latency, barrier, threshold, power, output |
| `resource` | What that spec is made of: length, energy, time, … |
| `observed_text` | Handbook / §4.3 fact |
| `implied_text` | QSA machine spec |
| `inference_kind` | `relabel` / `derived` / `envelope` / `open` |
| `description` | One or two sentences: what the system must have, fail at, or emit |
| `operator` | `eq` / `min` / `max` / `approx` / `range`, or empty |
| `value_si` | Optional single SI number (collapse edge or representative) |
| `si_unit` | SI unit of `value_si` |
| `value_text` | Human interval or symbol (`10–20 nm`, `ωp`) |
| `confidence` | Row-level; a High file can still have a Medium clause |
| `notes` | Caveats, cross-cites |
| `updated` | `YYYY-MM-DD` |

`aspect` and `resource` are two axes. Magnet latch-cell: `aspect=scale`, `resource=volume` (or `length` if the quoted size is ~30 nm). Plasma period: `aspect=latency`, `resource=time`. Plasma edge: `aspect=speed`, `resource=frequency`. Zero hold-power: `aspect=power`, `resource=energy`, `value_si=0`.

`inference_kind`:

- **relabel** — same number, QSA name (`φ` is the energy gate)
- **derived** — computed from the observed number (10–20 nm → 40–85 planes)
- **envelope** — class or inequality, not a single cliff
- **open** — mapping names the spec but has no number yet

`clause` values: `hardware_scale` · `clock_latency` · `energy_barrier` · `failure_mode` · `emergent_output` · `consistency_gap` (§4.6-only row)

Do not invent a new token without updating this file and `schema.sql`.

---

## Example queries

Every High-confidence spatial minimum:

```sql
SELECT impl_key, value_text, description
FROM implication
WHERE role = 'requirement'
  AND aspect = 'scale'
  AND resource IN ('length', 'volume', 'area')
  AND confidence = 'high'
ORDER BY value_si IS NULL, value_si;
```

Zero-power outputs:

```sql
SELECT i.impl_key, e.family, i.description
FROM implication i
JOIN effect e ON e.slug = i.effect_slug
WHERE i.aspect = 'power' AND i.value_si = 0;
```

Implications that only rename a handbook number:

```sql
SELECT impl_key, observed_text, implied_text
FROM implication
WHERE inference_kind = 'relabel';
```

Where the mapping named a spec and could not attach a number:

```sql
SELECT e.family, i.impl_key, i.description
FROM implication i
JOIN effect e ON e.slug = i.effect_slug
WHERE i.inference_kind = 'open' OR i.role = 'gap'
ORDER BY e.family, i.impl_key;
```

---

## Future tables (not in this schema)

Leave these until a query on `implication` actually hurts.

- **`boundary`** — one row per §4.3 measured number (the science catalog, independent of the QSA translation). Today those numbers sit in `observed_text` / `value_text` only when they load-bear an implication.
- **`implication_relation`** (or `related`) — edges between effects or between implication rows (same machine, contrast case, failure twin). Today those links live in each Markdown file’s Related section and in `implication.notes`.
- Auto-extraction from Markdown on every edit. Extraction is interpretive; a regex pass would flatten the analysis.

---

## Rebuild notes

- `qs-analysis.db-wal` and `qs-analysis.db-shm` are transient; do not commit them.
- `seed_effect.sql` is generated. Edit frontmatter, not that file.
- Edit `implication.csv` (or regenerate it from reviewed fragments) when a mapping changes. Then rerun `rebuild.py`.
