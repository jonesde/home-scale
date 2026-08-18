# QSA analysis layer

Markdown in [`library/`](../library/) is the science source of truth. This directory is the derived analysis layer: a queryable reading of the QSA mappings, not a second wiki.

Working database: `qs-analysis.db` at the repo root. It is a local build artifact (gitignored). Commit the text: `fragments/*.jsonl`, `implication.csv`, `predicted_implication.csv`, `design*.csv`, `schema.sql`.

First load: 59 `effect` · 171 `effect_constraint` · 488 `implication` (447 extracted, 41 predicted) · 12 `design` · 11 `node` (all `forced`) · 38 `requirement` · 297 `implication_design` · 59 `design_requirement` · 141 `design_implication` (77 entails, 61 predicts, 3 incompatible) · 36 `implication_node` · 23 `design_node`. 92 pairs sit in both design junctions (evidence up *and* commitment down). Predicted rows have zero evidence-up edges.

Rebuild (stdlib Python 3 only — no pip):

```bash
python3 analysis/rebuild.py
```

That is the whole shot. It merges fragments → `implication.csv`, rebuilds `effect` from frontmatter, loads `implication.csv` plus the four design-layer CSVs, and writes `qs-analysis.db`.

Edit `fragments/*.jsonl` for extracted implications. Edit `predicted_implication.csv` for conjectures. Edit `design.csv`, `requirement.csv`, `implication_design.csv`, `design_requirement.csv`, and `design_implication.csv` for the assembled machines and the downward arrow. Do not hand-edit `implication.csv` or `seed_effect.sql`. Markdown is never generated from the database.

---

## Tables

| Table | Grain | Source |
|---|---|---|
| `effect` | one row per formal library file | frontmatter (mechanical) |
| `effect_constraint` | one row per constraint tag on an effect | frontmatter (mechanical) |
| `implication` | one atomic mapping claim (`origin` = extracted or predicted) | fragments / `implication.csv` plus `predicted_implication.csv` |
| `design` | one assembled reverse-engineered machine | curated `design.csv` |
| `implication_design` | evidence up: which extracted claims assembled the machine | curated `implication_design.csv` |
| `design_implication` | designs down: which claims the machine commits to | curated `design_implication.csv` |
| `requirement` | one demand visible only at design grain | curated `requirement.csv` |
| `design_requirement` | design imposes requirement | curated `design_requirement.csv` |
| `node` | one constituent (elementary / composite / quasiparticle) | `library/nodes/` frontmatter |
| `implication_node` | which extracted claims force / witness / contrast a node | curated `implication_node.csv` |
| `design_node` | which machines consume a node, and as what role | curated `design_node.csv` |

Table names are singular. IDs are slugs. **Design** means an assembled machine specification, not agency. **`requirement` here is not `implication.role = requirement`**: that role is what an *effect* needs from the machine; this table is what an *assembled machine* then demands.

A family is a filing spine. A design is a hypothesized machine. One implication can sit on more than one design (magnetostriction is on the latch *and* the grid). One design can pull implications from more than one family.

If a “requirement” can be restated as a single existing implication, do not create it. Only write one when the demand is a rolled-up spec, a consistency condition across members, a named closure gap, or a prediction the library does not yet contain.

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

## Design layer

Two arrows between the same entities:

- **`implication_design`** — *which extracted claims did we use to assemble this machine?* `membership`: `core` · `supporting` · `contrast`.
- **`design_implication`** — *if this machine is right, which atomic claims follow?* `relation`: `entails` · `predicts` · `incompatible`. `strength`: `must` · `should`.

A pair may exist in both tables. That is not a duplicate: one edge is evidence, the other is commitment.

Predicted implications (`origin = predicted`, `impl_key` starts with `predicted:`) are conjectures minted from a design. They appear only on the downward arrow, always as `relation = predicts`. Rebuild fails if one is used as evidence. `effect_slug` may be an existing effect (claim about a filed phenomenon) or NULL (phenomenon not in the library yet). `observed_text` on a prediction is “what would be observed if this is right.”

`implication_design.membership`: `core` (load-bearing) · `supporting` (consistent, not load-bearing) · `contrast` (bounds the machine from outside).

`requirement.kind`: `spec` · `consistency` · `prediction` · `closure`.

`requirement.status`: `open` · `satisfied` · `tension` · `untested` (curated, not computed).

`design_requirement.strength`: `must` · `should`.

A requirement with no design edge is a rebuild error. A design with no requirements is a warning. Unmapped implications are expected.

### First-wave machines

| `design_key` | Status | What it is |
|---|---|---|
| `collective-screening` | formal | Connected charged population that screens and re-radiates |
| `anisotropy-latch` | formal | Barrier-protected directional memory at zero hold-power |
| `polar-latch` | formal | Electrical twin: remnant *P* at *E* = 0 |
| `gapped-condensate` | formal | Charged protected mode; R=0 and expulsion are split artifacts |
| `chargeless-superflow` | formal | He-4 analog; not the same hardware |
| `energy-gate` | formal | Discrete conversion; N=1 per event |
| `oscillator-grid` | formal | Ion grid as coupled oscillators |
| `ensemble-average` | formal | Stable macro number from a large population |
| `exchange-pin` | draft | Ninth: nested AFM/FM pin; collapse is *T*<sub>B</sub> not FM *T*<sub>C</sub> |
| `edge-channel` | draft | Tenth: 2DEG + bulk gap + edge path; integer *R_H = h/νe²* |
| `phase-space-condensate` | draft | Eleventh: dilute BEC; \(T_c(n)\); not 0 W |
| `landauer-channel` | draft | Twelfth: 1D constriction; \(2e^2/h\); no *B* |

`quantum-hall-effect` is the **core** of draft `edge-channel`. It stays contrast on `gapped-condensate`. A quantum point contact (`2e²/h`, no *B*) is contrast on `edge-channel`, not a member. `design_node` consumes `electron` @ `edge`. Promote to formal when a second core effect (QSHE / QAHE) is filed. Do not close *R_K* with a Chern-number story.

### First-wave nodes

| `node_key` | kind | origin | Typical `design_node.role` |
|---|---|---|---|
| `electron` | elementary | forced | `population` / `single` / `average` |
| `photon` | elementary | forced | `input` / `average` |
| `muon` | elementary | forced | `input` |
| `proton` | elementary | forced | `product` |
| `neutron` | elementary | forced | `product` |
| `neutrino` | elementary | forced | `input` |
| `positron` | elementary | forced | `product` |
| `phonon` | quasiparticle | forced | `mode` |
| `ion` | composite | forced | `matrix` |
| `nucleus` | composite | forced | `recoil` |
| `directional-moment` | quasiparticle | forced | `latch-cell` |

`pdgid` follows the PDG Monte Carlo numbering scheme when the species has one (electron `11`, positron `-11`, photon `22`). Quasiparticles and class nodes leave it NULL. Identity numbers are cited from PDG 2026 / CODATA 2022, not extracted as cliffs. Do not vendor those datasets.

`implication_node.membership`: `forces` · `witnesses` · `contrast`. Cataloged nodes cannot `forces`. Predicted nodes cannot be evidence.

`design_node.role`: `population` · `single` · `average` · `recoil` · `mode` · `matrix` · `latch-cell` · `input` · `product` · `edge` · `contrast`.

### Adding a design

Add one when a cluster of implications shares a collapse and a hardware stack that no existing design owns. Do not add one for every interface or every textbook chapter.

1. Append a row to `design.csv`.
2. Attach **core** implications (scale, clock, barrier, dominant failure, output, the main gap). Attach **supporting** only when a file already names the link. Attach **contrast** only when a file uses the other effect as a bound.
3. Add `requirement` rows that are *not* restatements of a single implication. Reuse a shared `req_key` when several machines impose the same demand (`zero-hold-power`, `thermal-cliff`).
4. Add `design_requirement` edges. Rebuild. A requirement with zero edges fails the rebuild.

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

Designs that share a requirement:

```sql
SELECT req_key, design_key, strength
FROM design_requirement
WHERE req_key = 'zero-hold-power'
ORDER BY design_key;
```

Open closures on a machine:

```sql
SELECT r.req_key, r.statement
FROM requirement r
JOIN design_requirement dr ON dr.req_key = r.req_key
WHERE dr.design_key = 'gapped-condensate'
  AND r.kind = 'closure';
```

Contrast bounds on the screening engine:

```sql
SELECT i.impl_key, i.description
FROM implication_design id
JOIN implication i ON i.impl_key = id.impl_key
WHERE id.design_key = 'collective-screening'
  AND id.membership = 'contrast';
```

What a machine commits to, including conjecture:

```sql
SELECT di.relation, di.strength, i.origin, i.impl_key, i.description
FROM design_implication di
JOIN implication i ON i.impl_key = di.impl_key
WHERE di.design_key = 'collective-screening'
ORDER BY di.relation, i.origin, i.impl_key;
```

Predicted implications with no library file:

```sql
SELECT impl_key, description
FROM implication
WHERE origin = 'predicted' AND effect_slug IS NULL;
```

Which designs consume the electron, and as what:

```sql
SELECT design_key, role
FROM design_node
WHERE node_key = 'electron'
ORDER BY role, design_key;
```

---

## Future tables (not in this schema)

- **`boundary`** — one row per §4.3 measured number (the science catalog, independent of the QSA translation). Today those numbers sit in `observed_text` / `value_text` only when they load-bear an implication.
- **`implication_relation`** — pairwise edges that are *not* “same machine” or “contrast via a design.” Same-machine and contrast now join through `design`. Leave this until a query needs an implication–implication edge that has no design.
- Auto-extraction from Markdown on every edit. Extraction is interpretive; a regex pass would flatten the analysis.
- A `node_implication` downward arrow. First load hangs node conjecture off ordinary predicted implications.

---

## Rebuild notes

- `qs-analysis.db-wal` and `qs-analysis.db-shm` are transient; do not commit them.
- `seed_effect.sql` is generated. Edit frontmatter, not that file.
- Edit `fragments/*.jsonl` when an extracted mapping changes. Edit `predicted_implication.csv` and `design_implication.csv` when a downward claim changes. Then rerun `rebuild.py`.
