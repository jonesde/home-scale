# QSA working summary

**Date:** 2026-08-20; sourcing pilot added 2026-11-11  
**Purpose:** Current state and locked rules so work can continue without rereading the whole tree. Not a second methodology spec.

**Canonical sources**

| Need | File |
|---|---|
| Methodology and locked 7-part template | [README.md](README.md) |
| Agent / research orientation, terms, schema | [AGENTS.md](AGENTS.md) |
| Effect catalog | [library/INDEX.md](library/INDEX.md) |
| Family assignment | [library/TAXONOMY.md](library/TAXONOMY.md) |
| Analysis layer and example SQL | [analysis/README.md](analysis/README.md) |
| How to read applications | [SAFETY.md](SAFETY.md) |
| The deterministic premise against theorems and experiments | [Determinism.md](Determinism.md) |
| Sourcing rules (evidence tags, citation keys, threshold vs crossover) | [library/README.md](library/README.md#sourcing-standard) |

If this file disagrees with a formal library entry, the library file wins.

---

## 1. Project context

Quantum Systems Analysis (QSA) is a utility and internal-consistency instrument only.

- Quantum entities are modeled as finite state machines (or deterministic rule-bound systems).
- Mechanical predictability of states and behaviors: a system's internal configuration, constraints and rules together fix what it does next. This is a claim about the rules, not about what an observer can find out or forecast.
- Apparent randomness is treated as incomplete knowledge.
- Macroscopic effects are the averaged, synchronized output of large numbers of constrained microscopic machines.
- Method = constraint reasoning from experimental failure thresholds + performance metrics.
- No agency, purpose, or programmer language. **Design** here means an assembled machine specification, not intention.

The methodology and library template live in this repo’s [README.md](README.md) (not an external artifact path).

---

## 2. Locked working assumptions (do not dilute)

- Quantum effects are produced by a finite-state-machine model whose states and behaviors are mechanically predictable: the same configuration under the same constraints gives the same behavior. No claim is made that the configuration can be learned in practice.
- Constraint reasoning only: what the system cannot do + exact thresholds where the macro effect collapses.
- Emergent architecture from synchronized microscopic routines.
- Performance metrics drawn exclusively from experimental boundaries.
- Language restricted to constraints, resources, synchronization, failure thresholds, and emergent output (effect / design prose). Node cards may state taken identity specs.
- Incomplete mappings are recorded as incomplete. Extracted rows do not fill gaps with conjecture; conjecture belongs in predicted implications on the downward arrow.
- Node identity specs may be taken from a pinned PDG / CODATA edition. Collapses stay effect-owned.
- **Utility + internal consistency** are the only evaluation criteria.

---

## 3. Current inventory

Live pipeline: `effect` → `implication` → `design` → `requirement`. Markdown in `library/` is the science source of truth. `python3 analysis/rebuild.py` builds local `qs-analysis.db` (gitignored).

| Layer | Count | Where |
|---|---|---|
| Formal effects | 63 (six families; three added in the 2026-11 sourcing pass: electrical-contacts, electrical-resistivity, hydrogen-in-metals) | [library/INDEX.md](library/INDEX.md) |
| Mapping confidence | 28 High · 35 Medium · 0 Low (shape-anisotropy and reflection moved to Medium when sourced; the two new entries are Medium) | per-file frontmatter |
| Data confidence | High except [dielectric-breakdown](library/dielectric-breakdown.md) and [pyroelectric-fusion](library/pyroelectric-fusion.md) (Medium). Unverified outside the sourced files | same |
| Sourced effects | 30 of 63 (see the Sourced column of the index) | [library/INDEX.md](library/INDEX.md) |
| Extracted implications | 486 | `analysis/fragments/*.jsonl` |
| Predicted implications | 41 | [analysis/predicted_implication.csv](analysis/predicted_implication.csv) |
| Designs | 12 (8 formal; four drafts) | [analysis/design.csv](analysis/design.csv) |
| Nodes | 11 forced | [library/nodes/INDEX.md](library/nodes/INDEX.md) |
| Requirements | 38 | [analysis/requirement.csv](analysis/requirement.csv) |
| Applications | 14 | [application/README.md](application/README.md) |
| Derived notes | spec sheets + requirement audit + analog-slot map | [library/derived/](library/derived/README.md) |

`quantum-hall-effect` is the core of draft `edge-channel` (2DEG + Landau gap + edge path). It stays **contrast** on `gapped-condensate`. A quantum point contact is contrast on `edge-channel`, not a member. The electron `edge` role is now consumed.

The two original handover sketches are now formal entries. Both have since been sourced, and both lost their headline number: the reflection entry's "minimum film of 40–85 atomic planes" does not exist (reflectance falls smoothly with thickness and a collective response is measured at one atomic layer), and the magnet entry's ~30 nm blocking size was an arithmetic error (it is about 3.5 nm):

- [library/reflection.md](library/reflection.md) — collective screening; High mapping
- [library/permanent-magnet-latch.md](library/permanent-magnet-latch.md) — anisotropy latch; High mapping

Those two, plus [photoelectric-threshold](library/photoelectric-threshold.md), are the calibration trio in `analysis/fragments/gold.jsonl`. Two of the three calibration "cliffs" turned out to be crossovers when sourced, so treat calibration as recovering the sourced functional form, not a cliff. Applications that lean on the latch or the interstitial hypothesis should keep recovering those sourced dependences first ([thin-film-optics](application/thin-film-optics.md), [bonded-magnets](application/bonded-magnets.md)).

---

## 4. First-wave machines

| `design_key` | Status | One line |
|---|---|---|
| `collective-screening` | formal | Connected charged population; dies by buffer starvation or clock overrun |
| `anisotropy-latch` | formal | Barrier-protected directional memory; 0 W hold |
| `polar-latch` | formal | Electrical twin; remnant *P* at *E* = 0; a large body partitions |
| `gapped-condensate` | formal | Charged protected mode; *R* = 0 and expulsion are split artifacts |
| `chargeless-superflow` | formal | ⁴He analog; not the same hardware |
| `energy-gate` | formal | Discrete conversion; *N* = 1 per event |
| `oscillator-grid` | formal | Ion grid as coupled oscillators |
| `ensemble-average` | formal | Stable macro number from a large population; no universal *N* |
| `exchange-pin` | draft | Nested AFM/FM pin; collapse is *T*<sub>B</sub>, not FM *T*<sub>C</sub> |
| `edge-channel` | draft | 2DEG + bulk gap + edge path; integer *R_H = h/νe²*; QPC is contrast |
| `phase-space-condensate` | draft | Dilute BEC; \(T_c(n)\); not 0 W; not He-4 |
| `landauer-channel` | draft | 1D constriction; \(2e^2/h\); no *B* required |

Shared requirements often share a **kind** of cliff, not a **number**. See [library/derived/requirement-audit.md](library/derived/requirement-audit.md) before quoting one thermal or length figure across machines.

---

## 5. What to do next

First, before anything below: convert the remaining unsourced effect files (the Sourced column of the index lists them) to the [sourcing standard](library/README.md#sourcing-standard), one family at a time. The first-wave numbers were recalled by a language model. The magnet pilot found a factor-of-ten error in the NdFeB blocking size (copied into the requirement table, the spec sheets and three applications), a reversed comparison with magnetite, a Curie temperature in the wrong unit, one prediction contradicted by published experiments, and two predictions that were already measured facts. Assume the other families hold errors of the same kinds.

Then prefer, in order:

1. Tighten a Medium mapping — statistical buffer, mesoscale step (*H*<sub>c</sub> ≪ *H*<sub>a</sub>, *E*<sub>c</sub>, pinning after *H*<sub>c1</sub>), or a taken rather than derived constant.
2. Correct fragment rows so `observed_text` still quotes the file; rebuild; keep derived sheets in sync. The μCF-era design-down predicted hunt is done (41 predicted rows). Do not mint a second wave unless a new machine or a new formal file creates a coupled test that slate missed.
3. Add a new effect only when the collapse is sharp and is not already a clause on an existing entry. Update [library/INDEX.md](library/INDEX.md) in the same change.
4. Add a thirteenth design only when a hardware stack and collapse are not already owned. Do not invent one for every interface. Drafts `phase-space-condensate` and `landauer-channel` own the BEC and QPC leftovers; do not fold them into He-4 or `edge-channel`.
5. Add a `cataloged` node only under the admission filter in [library/nodes/README.md](library/nodes/README.md) (parent of a forced node, or already named as hardware). Do not vendor PDG. The dark-sector list stays out until a file names those species.

Applications stay mappings and falsifiers, not protocols. EM-LENR waits on Steven’s review for the nuclear/configuration claim; it now tests the hypothesis on two sourced objects (trapped hydrogen and the hydride transition), palladium first. Eight new device concepts (not used products) live under [application/](application/README.md); the strongest stacks are the switchable hydride mirror, the polar beam-target gate, and the extra-node muon hydrogen gate.

---

## 6. Continuity notes

- All quantitative claims must remain traceable to experimental boundaries. Traceable means a citation key and a reference that was opened.
- A limit that falls off continuously is a crossover, not a cliff. Label it and give its functional form.
- When a mapping is incomplete, state the incompleteness explicitly.
- Language discipline is non-negotiable: constraints, resources, synchronization, failure thresholds, emergent output only.
- The sole evaluation criteria remain utility of the extracted specifications and internal consistency of the mappings.
- Research recipes, term definitions, file map, and schema: [AGENTS.md](AGENTS.md).
