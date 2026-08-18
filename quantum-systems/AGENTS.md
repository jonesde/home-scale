# AGENTS.md — Quantum Systems Analysis (QSA)

Orientation for agents and researchers working in this directory. Read this before editing files or running cross-cutting queries.

**These are theories, mappings, and design notes — not tested protocols.** Read [SAFETY.md](SAFETY.md) before any application file. Do not treat geometries, pressures, pulse sizes, or material lists as instructions.

---

## What this is

QSA tests a finite-state-machine reading of quantum and condensed-matter phenomena. Macroscopic “laws” and stable effects are treated as the averaged, synchronized output of constrained microscopic machines. The method reverse-engineers machine specifications from **experimental collapse thresholds**: what the system cannot do, and the exact scale at which the macroscopic output fails.

Evaluation criteria are only:

1. **Utility** — does the mapping produce usable performance specs (buffer, clock, barrier, failure envelope)?
2. **Internal consistency** — do those specs form one coherent picture under the working assumptions?

No foundational or interpretive claims beyond those assumptions. No agency, purpose, programmer, or intentional-design language.

The live pipeline is:

```
effect  →  implication  →  design  →  requirement
(file)     (atomic claim)   (assembled     (demand visible
                            machine)       only at machine grain)

                 ↘  node  (constituent the machine consumes)
```

Markdown in `library/` is the **science source of truth for collapses**. Markdown in `library/nodes/` is the **science source of truth for node identity**. The SQLite database is a **query surface** rebuilt from text. Never generate library Markdown from the database. If a derived note disagrees with an effect file about a cliff, the effect file wins. If a node card and an effect file disagree about a failure envelope, the effect file wins.

---

## Locked working rules

Do not dilute these.

- Constraint reasoning only **for effects**: what the system cannot do + the threshold where the macro effect collapses.
- Effect and design language is limited to constraints, resources, synchronization, failure thresholds, and emergent output. Node cards may state taken identity specs (mass, charge, spin).
- Every quantitative claim on an effect must be traceable to an experimental boundary or a well-established measured parameter. Node identity specs may be taken from a pinned PDG / CODATA edition.
- Incomplete mappings stay incomplete. Do not fill a gap with conjecture in an *extracted* row. Conjecture belongs in `predicted_implication.csv` and only on the downward arrow (`design_implication.relation = predicts`).
- A family is a filing spine (dominant collapse type). A design is a hypothesized machine. Do not invent a seventh family to hide a mismatch; record the mismatch on the entry until several effects share the leftover collapse.
- Do not add a thirteenth design for every interface or textbook chapter. Add one only when a cluster of implications has a collapse and a hardware stack that no existing design owns. Integer QHE is draft `edge-channel`; a 1D constriction is draft `landauer-channel` (contrast, not a member). Dilute BEC is draft `phase-space-condensate`.
- Shared requirements often share a **kind** of cliff, not a **number**. Equating Curie, λ-point, melt, and blocking temperatures is a mapping error. See [library/derived/requirement-audit.md](library/derived/requirement-audit.md).
- Applications name knobs and falsifiers. They are not build sequences, pressure ratings, or lab SOPs.

---

## Terms (as used here)

These words have project-specific meanings. Do not import the everyday or software-engineering senses without checking.

### Effect

One macroscopic phenomenon with a distinct experimental failure envelope. One file in `library/{slug}.md`, one row in `effect`.

Filed by **what kind of machine behavior produces the output**, specifically by the **dominant collapse** — not by textbook domain (optics, magnetism, …). Conventional names stay on the title so the catalog stays searchable.

An effect is a self-contained artifact. It does not assert claims beyond the data and the mapping. Gaps stay visible.

**Not** a design, not an application, not a survey.

### Implication

One atomic mapping claim extracted from (or predicted about) an effect. Grain: a single clause such as “reflection needs a ~10–20 nm connected film” or “the latch dies at *T*<sub>C</sub>.”

Two origins:

| `origin` | Key shape | Meaning |
|---|---|---|
| `extracted` | `{effect_slug}:{clause}:{short-name}` | Reading of a sentence already in the library file |
| `predicted` | `predicted:{effect_slug\|design_key}:{short-name}` | Conjecture minted from a design. `observed_text` is “what would be seen if the machine is right.” |

`implication.role` is what the *effect* needs, fails at, emits, or cannot yet specify:

| Role | Meaning |
|---|---|
| `requirement` | What the effect needs from the machine (buffer, clock, barrier, …) |
| `failure` | The collapse that kills the macro output |
| `output` | The stable emergent product |
| `gap` | Named incompleteness (usually a §4.6 consistency note) |

**`implication.role = requirement` is not the `requirement` table.** See below.

### Design

An assembled reverse-engineered **machine specification** — a hypothesized hardware stack that several effects share. Twelve first-wave machines: `collective-screening`, `anisotropy-latch`, `polar-latch`, `gapped-condensate`, `chargeless-superflow`, `energy-gate`, `oscillator-grid`, `ensemble-average`, and drafts `exchange-pin`, `edge-channel`, `phase-space-condensate`, `landauer-channel`.

**Not** intentional design, not a CAD file, not an application device. The word is used because the output looks like a spec sheet (buffer, clock, barrier, hold-power, erase). No agency is implied or permitted.

One implication can sit on more than one design (magnetostriction is on the latch *and* the grid). One design can pull implications from more than one family.

Two arrows between the same entities — they are not duplicates:

| Table | Direction | Question |
|---|---|---|
| `implication_design` | evidence **up** | Which extracted claims did we use to assemble this machine? |
| `design_implication` | commitment **down** | If this machine is right, which atomic claims follow? |

A pair may exist in both junctions (evidence *and* commitment). Predicted rows have **zero** evidence-up edges; rebuild fails if one is used as evidence. On the downward arrow they are always `relation = predicts`.

### Requirement

A demand visible only at **design** grain — a rolled-up spec, a consistency condition across members, a named closure gap, or a prediction the library does not yet contain as a single implication.

**Do not create a `requirement` row if the demand can be restated as one existing implication.**

`requirement.kind`:

| Kind | Use |
|---|---|
| `spec` | A machine-level performance demand (`zero-hold-power`, `connected-spatial-buffer`) |
| `consistency` | Several members must agree (`one-plasma-clock`, `split-r0-and-expulsion`) |
| `prediction` | Coupled test already implied by the assembly (`coupled-screening-failure`) |
| `closure` | Honest open: a number or mesoscale step is taken, not derived |

`requirement.status` is **curated, not computed**: `open` · `satisfied` · `tension` · `untested`.

A requirement with no `design_requirement` edge is a rebuild error. Reuse a shared `req_key` when several machines impose the same demand (`thermal-cliff`, `zero-hold-power`).

### Node

A microscopic constituent (elementary, composite, or quasiparticle) that one or more machines consume. **Not** an effect, **not** a design, **not** a seventh family. Conventional particle names stay on the title.

| `origin` | Meaning | Evidence? |
|---|---|---|
| `forced` | A library collapse already requires this constituent | Yes (`implication_node`) |
| `cataloged` | Well-measured species, no library collapse yet | No (`forces` is a rebuild error) |
| `predicted` | Theorized species with a named would-be observation | No |

Identity specs (mass, charge, spin, lifetime, PDG MC ID) may be **taken** from a pinned edition (PDG 2026; CODATA 2022). They are not extracted cliffs. Quasiparticles (`phonon`, `directional-moment`) and class nodes (`nucleus`, host `ion`) have `pdgid` NULL.

Do not add node slugs to [`library/INDEX.md`](library/INDEX.md). Do not mint a design per species. Do not close `fluxoid-increment-2e` or `underived-rk` with a particle story. Admission for `cataloged` cards: parent/contrast of a forced node, or already named as hardware in an effect file. Do not vendor PDG or CODATA files.

### Nearby vocabulary

| Term | Meaning here |
|---|---|
| **Family** | Filing class by dominant collapse. Six only. Singular; no second primary family. |
| **Constraint tag** | Cross-cut on an effect (`spatial-buffer`, `clock-latency`, …). Not a family. |
| **Collapse / cliff** | The measured threshold that kills the macro output. The spine of the taxonomy. |
| **Buffer** | Minimum hardware scale: length, volume, connected film, coherent volume, or statistical *N*. |
| **Clock / latency** | Response time, precession rate, plasma period, or frequency cutoff. |
| **Barrier** | Activation or anisotropy energy that protects a written state. Driven machines often have *no* latch barrier. |
| **Hold-power** | Continuous watts (or volts) to *keep* the state. Many machines here are 0 W. |
| **Mapping** | The QSA translation of an effect into buffer / clock / barrier / failure / output. Confidence is per file *and* per implication row. |
| **Medium mapping** | Not a failed entry. Collapse is real and the family is assigned, but a hardware scale is statistical, mesoscale, or taken rather than derived. Prefer tightening these over adding a second wave. |
| **Relabel / derived / envelope / open** | How the implication was inferred from the handbook number. Relabel = same number, QSA name. Derived = computed (10–20 nm → 40–85 planes). Envelope = class or inequality. Open = spec named, no number yet. |
| **Application** | Device-centered use of the library. Concepts may repeat; the library remains the singular science source. |
| **Derived note** | Spec sheet or requirement audit generated from the analysis layer. **Not** an effect entry. Do not add those slugs to `INDEX.md`. |
| **Node** | Constituent a machine consumes. Own grain (`library/nodes/`). Not a family. |

---

## How to do research with this corpus

### Default path for a new question

1. **Name the macroscopic output and its dominant collapse.** If you cannot name the cliff, you do not yet have an effect.
2. **Find the family** in [library/TAXONOMY.md](library/TAXONOMY.md) / [library/INDEX.md](library/INDEX.md). Open the formal file, not only the index note.
3. **Read §4.3 then §4.5–4.6.** §4.3 is the measured envelope; §4.5 is the machine spec; §4.6 is where the mapping is still open. Confidence in the data and confidence in the mapping are different columns.
4. **Rebuild if needed** (`python3 analysis/rebuild.py`) and query `qs-analysis.db` for siblings: same `aspect`+`resource`, same `design_key`, shared `req_key`, `membership = contrast`, or shared `node_key` / `design_node.role`.
5. **Check the derived sheets** ([library/derived/design-spec-sheets.md](library/derived/design-spec-sheets.md), [requirement-audit.md](library/derived/requirement-audit.md), [operating-envelopes.md](library/derived/operating-envelopes.md), [node-types.md](library/derived/node-types.md)) before treating two designs as sharing a number.
6. **Only then** look at `application/`. An application is a claim about a device, graded against handbook cliffs. It is not additional science.

### Recommended query patterns

High-confidence spatial minima (what “buffer” actually means in numbers):

```sql
SELECT impl_key, value_text, description
FROM implication
WHERE role = 'requirement'
  AND aspect = 'scale'
  AND resource IN ('length', 'volume', 'area')
  AND confidence = 'high'
  AND origin = 'extracted'
ORDER BY value_si IS NULL, value_si;
```

Where the mapping named a spec and could not attach a number (second-pass work list):

```sql
SELECT e.family, i.impl_key, i.description
FROM implication i
JOIN effect e ON e.slug = i.effect_slug
WHERE i.origin = 'extracted'
  AND (i.inference_kind = 'open' OR i.role = 'gap')
ORDER BY e.family, i.impl_key;
```

What a machine commits to, including conjecture:

```sql
SELECT di.relation, di.strength, i.origin, i.impl_key, i.description
FROM design_implication di
JOIN implication i ON i.impl_key = di.impl_key
WHERE di.design_key = 'collective-screening'
ORDER BY di.relation, i.origin, i.impl_key;
```

Shared requirement — then **read the audit** before equating numbers:

```sql
SELECT dr.design_key, dr.strength, r.kind, r.status, r.statement
FROM design_requirement dr
JOIN requirement r ON r.req_key = dr.req_key
WHERE dr.req_key = 'thermal-cliff';
```

Predicted claims that have no library file yet (`effect_slug` may be NULL):

```sql
SELECT impl_key, description
FROM implication
WHERE origin = 'predicted' AND effect_slug IS NULL;
```

Contrast bounds (the machine is defined as much by what it is *not*):

```sql
SELECT i.impl_key, i.description
FROM implication_design id
JOIN implication i ON i.impl_key = id.impl_key
WHERE id.design_key = 'anisotropy-latch'
  AND id.membership = 'contrast';
```

Which designs consume a node, and as what:

```sql
SELECT dn.design_key, dn.role, n.origin, n.kind
FROM design_node dn
JOIN node n ON n.node_key = dn.node_key
WHERE dn.node_key = 'electron'
ORDER BY dn.role, dn.design_key;
```

What library collapse forces a node:

```sql
SELECT ino.membership, i.impl_key, i.description
FROM implication_node ino
JOIN implication i ON i.impl_key = ino.impl_key
WHERE ino.node_key = 'electron'
ORDER BY ino.membership, i.impl_key;
```

Unforced cataloged species (work list, not mappings):

```sql
SELECT node_key, title
FROM node
WHERE origin = 'cataloged'
  AND node_key NOT IN (SELECT node_key FROM implication_node)
  AND node_key NOT IN (SELECT node_key FROM design_node);
```

Electron consumed as an edge path (draft `edge-channel`):

```sql
SELECT dn.design_key, dn.role, i.impl_key
FROM design_node dn
JOIN implication_node ino ON ino.node_key = dn.node_key
JOIN implication i ON i.impl_key = ino.impl_key
WHERE dn.node_key = 'electron' AND dn.role = 'edge';
```

### Worked research moves

**“Is this the same machine?”** Do not join on family alone. Join on `design_key` via `implication_design`, then check `design_implication` for `incompatible` rows. Reflection and photoelectric share a metal surface and sit in different families *and* different designs (`collective-screening` vs `energy-gate`). The downward `incompatible` on `photoelectric-threshold:hardware_scale:single-electron` is the load-bearing fact.

**“What would falsify this mapping?”** Read the application’s isolation tests and the design’s `predicts` / `incompatible` edges. Example: if a starved Ag film loses specular *R* but keeps a Kretschmann SPR dip in the same window, `coupled-screening-failure` is wrong — and the interstitial-latch applications that treat thin-film optics as the calibration case should stop.

**“Can I reuse this number on another device?”** Check [requirement-audit.md](library/derived/requirement-audit.md). `zero-hold-power` is a true shared zero. `thermal-cliff` is a shared *kind*. Do not quote NdFeB’s 585 K as a ferroelectric or superfluid number. Do not quote 10–20 nm optical δ as London λ.

**“Should I add an effect or a clause?”** Add a new file only when the collapse is sharp and is not already a clause on an existing entry. Prefer tightening a Medium mapping (missing mesoscale step or statistical buffer) over a second wave of files.

**“Should I add a requirement?”** Only if the demand is not already one implication. Typical good requirements: a shared kind (`thermal-cliff`), a coupled prediction (`coupled-screening-failure`), or an honest closure (`mesoscale-coercivity`).

### Prefer this order of work

1. Tighten a Medium mapping on an existing formal file.
2. Attach or correct implication fragments so they still quote the file.
3. Adjust design membership / downward edges / requirements; rebuild; update derived notes to match.
4. Add a new effect file (and an INDEX row in the same change) only when the collapse is not already owned.
5. Add a new design only when the hardware stack and collapse are not already owned.
6. Add a `forced` node only when a library collapse requires that constituent. Add a `cataloged` node only under the admission filter. Do not add node slugs to `library/INDEX.md`.

---

## File location and purpose

Paths are relative to this directory (`quantum-systems/`).

### Root

| Path | Purpose |
|---|---|
| [README.md](README.md) | Methodology specification and locked 7-part library template. Start here for *rules*. |
| [SAFETY.md](SAFETY.md) | How to read the repo. Hazard classes. What applications are not. |
| [AGENTS.md](AGENTS.md) | This file: orientation, terms, file map, schema, research recipes. |
| [Summary.md](Summary.md) | Current-state handover: inventory, first-wave machines, next work. Formal library files win if they disagree. |
| `qs-analysis.db` | Local SQLite build. Gitignored. Rebuild with `python3 analysis/rebuild.py`. |
| `.gitignore` | Ignores the `.db`, WAL/SHM/journal, and `analysis/__pycache__/`. |

### Effect library — `library/`

Science source of truth. One kebab-case file per effect. Copy [_template.md](library/_template.md) to start a new one. Adding, renaming, or deleting a file means updating `INDEX.md` in the same change.

| Path | Purpose |
|---|---|
| [library/README.md](library/README.md) | Operating manual: frontmatter schema, index columns, language rules. Markdown is the science source; the analysis layer is the query surface. |
| [library/INDEX.md](library/INDEX.md) | Catalog and build list. 59 formal first-wave entries. Families are machine/collapse classes. |
| [library/TAXONOMY.md](library/TAXONOMY.md) | Family definitions, assignment rule, constraint tags. |
| [library/_template.md](library/_template.md) | Locked 7-part body + frontmatter stub. |
| `library/{slug}.md` | One effect. Body sections 4.1–4.7. Frontmatter feeds `effect` / `effect_constraint`. |
| [library/derived/README.md](library/derived/README.md) | Derived notes are **not** catalog rows. |
| [library/derived/design-spec-sheets.md](library/derived/design-spec-sheets.md) | One sheet per design: buffer, clock, barrier, hold-power, erase, open. Inherited from `design` + downward `entails`. |
| [library/derived/requirement-audit.md](library/derived/requirement-audit.md) | Shared requirements: same *kind* vs same *number*. What applications are forbidden to do. |
| [library/derived/operating-envelopes.md](library/derived/operating-envelopes.md) | Inside of each design’s cliff. Inherited; no new numbers. |
| [library/derived/node-types.md](library/derived/node-types.md) | Join view: which designs consume which nodes. Not the zoo catalog. |

### Node library — `library/nodes/`

Identity cards for constituents. **Not** effect catalog rows.

| Path | Purpose |
|---|---|
| [library/nodes/README.md](library/nodes/README.md) | Grain rules, pinned PDG 2026 / CODATA 2022, admission filter. |
| [library/nodes/INDEX.md](library/nodes/INDEX.md) | Zoo list. Update in the same change as a card. |
| [library/nodes/_template.md](library/nodes/_template.md) | Short identity card. Not the 7-part effect template. |
| `library/nodes/{key}.md` | One node. Frontmatter feeds `node`. |

First-wave families (counts from the current catalog):

| Family | *n* | Dominant collapse |
|---|---|---|
| `collective-field-response` | 10 | Spatial under-provisioning or loss of collective phase |
| `latched-order` | 8 | Thermal over-barrier, volume too small for *KV*, or lattice destroyed |
| `gapped-coherence` | 10 | Gap closure or coherence-length / *H*<sub>c</sub> / *I*<sub>c</sub> violation |
| `threshold-conversion` | 13 | Under-threshold input (conversion does not occur) |
| `lattice-modes` | 10 | Mode cutoff, mfp destroyed, or loss of crystalline order |
| `ensemble-averages` | 8 | Too few contributors, or observation faster than the averaging window |

### Analysis layer — `analysis/`

Queryable reading of the mappings. Commit the text; do not commit the `.db`.

| Path | Purpose | Edit? |
|---|---|---|
| [analysis/README.md](analysis/README.md) | Layer rules, column meanings, example SQL, first-wave machines. | yes (docs) |
| [analysis/schema.sql](analysis/schema.sql) | Canonical DDL. | only with a matching README + rebuild change |
| [analysis/rebuild.py](analysis/rebuild.py) | One-shot rebuild: merge fragments → `implication.csv`, seed effects and nodes from frontmatter, load CSVs, write `../qs-analysis.db`. Stdlib only. | code |
| [analysis/merge_fragments.py](analysis/merge_fragments.py) | Concatenate `fragments/*.jsonl` → `implication.csv`. | code |
| [analysis/seed_effect.sql](analysis/seed_effect.sql) | Generated from frontmatter. | **no** — edit library frontmatter |
| [analysis/implication.csv](analysis/implication.csv) | Generated merge of fragments. | **no** — edit fragments |
| `analysis/fragments/{family}.jsonl` | Extracted implications, one JSON object per line, grouped by family. | **yes** |
| `analysis/fragments/gold.jsonl` | Extracted rows for the three calibration effects (`reflection`, `permanent-magnet-latch`, `photoelectric-threshold`). Same schema as the family files; keys must stay unique across all jsonl. | **yes** |
| [analysis/predicted_implication.csv](analysis/predicted_implication.csv) | Conjectures. Keys must start with `predicted:`. | **yes** |
| [analysis/design.csv](analysis/design.csv) | Assembled machines. | **yes** |
| [analysis/implication_design.csv](analysis/implication_design.csv) | Evidence up (`core` / `supporting` / `contrast`). | **yes** |
| [analysis/design_implication.csv](analysis/design_implication.csv) | Commitment down (`entails` / `predicts` / `incompatible`). | **yes** |
| [analysis/requirement.csv](analysis/requirement.csv) | Design-grain demands. | **yes** |
| [analysis/design_requirement.csv](analysis/design_requirement.csv) | Design imposes requirement (`must` / `should`). | **yes** |
| [analysis/implication_node.csv](analysis/implication_node.csv) | Which extracted claims force / witness / contrast a node. | **yes** |
| [analysis/design_node.csv](analysis/design_node.csv) | Which machines consume a node, and as what role. | **yes** |

### Applications — `application/`

Device-centered uses. Not procedures. Unqualified readers stop at SAFETY.md.

| Path | Device | Machines it applies |
|---|---|---|
| [application/README.md](application/README.md) | Index of applications. | — |
| [application/thin-film-optics.md](application/thin-film-optics.md) | Mirrors, TCO, SPR chips | `collective-screening` (calibration case) |
| [application/bonded-magnets.md](application/bonded-magnets.md) | Bonded NdFeB, tape, ferrofluid | `anisotropy-latch` (handbook calibration) |
| [application/hydrogen-embrittlement.md](application/hydrogen-embrittlement.md) | Charged high-strength metal parts | Interstitial latch, no nuclear layer |
| [application/hydride-storage.md](application/hydride-storage.md) | Metal-hydride bed / tank | Capacity vs pinned H |
| [application/EM-LENR.md](application/EM-LENR.md) | Contained pulsed-coil cell (Steven E. Jones) | Defect-pinned interstitial latch; energy-gate last |
| [application/EM-CSAM.md](application/EM-CSAM.md) | Micro-railgun deposition head | Impact, skin, breakdown, magnetostriction |

Hardware notes for the railgun live outside this directory, at [`../em-csam/`](../em-csam/README.md). Do not copy those notes in as protocols.

---

## Database schema (quick reference)

Rebuild from the repo root:

```bash
python3 analysis/rebuild.py
sqlite3 qs-analysis.db
```

First-wave load (after a clean rebuild): 59 `effect` · 171 `effect_constraint` · 488 `implication` (447 extracted, 41 predicted) · 12 `design` · 11 `node` · 38 `requirement` · 297 `implication_design` · 59 `design_requirement` · 141 `design_implication` (77 entails, 61 predicts, 3 incompatible) · 36 `implication_node` · 23 `design_node`.

Table names are singular. IDs are slugs. Foreign keys are on.

```
effect (slug PK)
  ├── effect_constraint (slug, tag)
  └── implication.effect_slug          -- extracted always; predicted optional

implication (impl_key PK, origin)
  ├── implication_design  (impl_key, design_key)   -- evidence UP
  ├── design_implication  (design_key, impl_key)   -- commitment DOWN
  └── implication_node    (impl_key, node_key)     -- forces / witnesses / contrast

design (design_key PK)
  ├── implication_design
  ├── design_implication
  ├── design_requirement (design_key, req_key)
  └── design_node        (design_key, node_key)

node (node_key PK)
  ├── implication_node
  └── design_node

requirement (req_key PK)
  └── design_requirement
```

### `effect`

| Column | Values / notes |
|---|---|
| `slug` | Filename stem. Must match frontmatter `id`. |
| `title` | Conventional name, optional QSA gloss. |
| `family` | One of the six families. |
| `status` | `formal` · `draft` |
| `confidence_data` | `high` · `medium` · `low` |
| `confidence_mapping` | `high` · `medium` · `low` · `unmapped` |
| `source_path` | `library/{slug}.md` |
| `updated` | `YYYY-MM-DD` |

### `effect_constraint`

`tag` ∈ `spatial-buffer` · `clock-latency` · `energy-barrier` · `mechanical-lattice` · `field-threshold` · `thermal`.

### `implication`

| Column | Values / notes |
|---|---|
| `impl_key` | See key shapes above. |
| `origin` | `extracted` · `predicted` |
| `effect_slug` | Required if extracted; NULL allowed if predicted (no library file yet). |
| `clause` | `hardware_scale` · `clock_latency` · `energy_barrier` · `failure_mode` · `emergent_output` · `consistency_gap` |
| `role` | `requirement` · `failure` · `output` · `gap` |
| `aspect` | `scale` · `capacity` · `speed` · `latency` · `barrier` · `threshold` · `power` · `output` |
| `resource` | `length` · `area` · `volume` · `node_count` · `time` · `frequency` · `energy` · `temperature` · `e_field` · `b_field` · `current` · `mass` · `charge` · `dimensionless` · `other` |
| `observed_text` | Handbook / §4.3 fact (or “what would be observed” if predicted). |
| `implied_text` | QSA machine spec. |
| `inference_kind` | `relabel` · `derived` · `envelope` · `open` |
| `operator` | `eq` · `min` · `max` · `approx` · `range` · NULL |
| `value_si` / `si_unit` / `value_text` | Optional number, its SI unit, and the human interval or symbol. |
| `confidence` | Row-level. A High file can still have a Medium clause. |

`aspect` and `resource` are two axes. Latch cell: `aspect=scale`, `resource=volume`. Plasma period: `aspect=latency`, `resource=time`. Plasma edge: `aspect=speed`, `resource=frequency`. Zero hold-power: `aspect=power`, `resource=energy`, `value_si=0`.

### `design`

`home_family` is the family the machine sits in; membership can still cross families. `status` `formal` · `draft`. `confidence` `high` · `medium` · `low`.

### Junctions

| Table | Extra columns |
|---|---|
| `implication_design` | `membership`: `core` · `supporting` · `contrast` |
| `design_implication` | `relation`: `entails` · `predicts` · `incompatible`; `strength`: `must` · `should` |
| `design_requirement` | `strength`: `must` · `should` |
| `implication_node` | `membership`: `forces` · `witnesses` · `contrast` |
| `design_node` | `role`: `population` · `single` · `average` · `recoil` · `mode` · `matrix` · `latch-cell` · `input` · `product` · `edge` · `contrast` |

### `node`

`kind` `elementary` · `composite` · `quasiparticle`. `origin` `forced` · `cataloged` · `predicted`. Optional `pdgid` (PDG Monte Carlo ID). Identity numbers live here, not as fake implication rows.

### `requirement`

`kind` `spec` · `consistency` · `prediction` · `closure`. `status` `open` · `satisfied` · `tension` · `untested`. Same `aspect` / `resource` / numeric columns as implication.

### Rebuild guards (fail the shot)

- Unknown family, constraint tag, or `effect_slug`.
- `id` ≠ filename stem.
- Duplicate `impl_key` / `design_key` / `req_key` / `node_key`.
- Extracted key not prefixed `{slug}:`, or `source_path` ≠ `library/{slug}.md`.
- Formal effect with zero implication rows.
- Predicted key not prefixed `predicted:`.
- Predicted row used as `implication_design` evidence, or used downward with `relation ≠ predicts`.
- Requirement with no design edge.
- Unknown node `kind` / `origin` / `design_node.role` / `implication_node.membership`.
- Node `source_path` ≠ `library/nodes/{key}.md`.
- `origin = forced` node with zero `implication_node` edges.
- `origin = cataloged` used as `implication_node.membership = forces`.
- `origin = predicted` node used as `implication_node` evidence.

Warnings (do not fail): design with no requirements; design with no downward edges; effect with fewer than four implication rows; extracted implications unused as evidence; `cataloged` node with no design and no implication edge; `forced` node used by no design; predicted node with no downward predicted implication.

Not in this schema (on purpose): a `boundary` table of every §4.3 number; pairwise `implication_relation` edges that are not “same machine” or “contrast via a design”; auto-extraction from Markdown.

---

## Editing protocol

```bash
# after changing library frontmatter, node cards, fragments, predicted rows, or design-layer CSVs:
python3 analysis/rebuild.py
```

- **Science change** → edit `library/{slug}.md` (and `INDEX.md` if status/mapping/collapse/notes changed). Then edit the matching fragment row so `observed_text` still quotes the file.
- **Extracted mapping change** → edit `analysis/fragments/*.jsonl`, not `implication.csv`.
- **Conjecture** → `predicted_implication.csv` + a `design_implication` row with `relation = predicts`.
- **Machine assembly** → `design.csv` and the three junction/requirement CSVs. Then update `library/derived/` so the sheets still match.
- **New effect** → copy `_template.md`, fill all seven sections, add an INDEX row in the same change, add fragment rows (rebuild fails if a formal file has zero implications).
- **Node identity** → edit `library/nodes/{key}.md` and `library/nodes/INDEX.md`. Junctions: `implication_node.csv`, `design_node.csv`. Do not add the slug to `library/INDEX.md`.
- Do not invent a new `family`, `clause`, `role`, `aspect`, `resource`, `inference_kind`, `membership`, `relation`, constraint tag, node `kind` / `origin`, or `design_node.role` without updating `schema.sql` and `analysis/README.md` together.

---

## Language and safety reminders

- Constraints, resources, synchronization, failure thresholds, emergent output. No agency. Node cards may add taken identity specs.
- “Design” always means assembled machine spec. “Node” always means a constituent, not a particle-physics encyclopedia row.
- Numbers in application files are **classes** from the analysis or from earlier concept notes, not qualified set points.
- Hydrogen, metal powder, pressure, and pulsed current are industrial hazards even at the small sizes named. Beryllium copper is named only for shops that already control beryllium.
- Do not scale inventory, pressure, or pulse energy in search of a nuclear signature. There is no demonstrated nuclear process here.
