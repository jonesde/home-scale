# QSA working summary

**Date:** 2026-08-17  
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

If this file disagrees with a formal library entry, the library file wins.

---

## 1. Project context

Quantum Systems Analysis (QSA) is a utility and internal-consistency instrument only.

- Quantum entities are modeled as finite state machines (or deterministic rule-bound systems).
- Full predictability is assumed once the internal rules, node states, and constraints are fully known.
- Apparent randomness is treated as incomplete knowledge.
- Macroscopic effects are the averaged, synchronized output of large numbers of constrained microscopic machines.
- Method = constraint reasoning from experimental failure thresholds + performance metrics.
- No agency, purpose, or programmer language. **Design** here means an assembled machine specification, not intention.

The methodology and library template live in this repo’s [README.md](README.md) (not an external artifact path).

---

## 2. Locked working assumptions (do not dilute)

- Quantum effects are produced by a finite-state-machine model with full predictability **IFF** fully understood.
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
| Formal effects | 59 (six families) | [library/INDEX.md](library/INDEX.md) |
| Mapping confidence | 30 High · 29 Medium · 0 Low | per-file frontmatter |
| Data confidence | High except [dielectric-breakdown](library/dielectric-breakdown.md) and [pyroelectric-fusion](library/pyroelectric-fusion.md) (Medium) | same |
| Extracted implications | 447 | `analysis/fragments/*.jsonl` |
| Predicted implications | 27 | [analysis/predicted_implication.csv](analysis/predicted_implication.csv) |
| Designs | 10 (8 formal; `exchange-pin` and `edge-channel` draft) | [analysis/design.csv](analysis/design.csv) |
| Nodes | 11 forced | [library/nodes/INDEX.md](library/nodes/INDEX.md) |
| Requirements | 33 | [analysis/requirement.csv](analysis/requirement.csv) |
| Applications | 6 | [application/README.md](application/README.md) |
| Derived notes | spec sheets + requirement audit | [library/derived/](library/derived/README.md) |

`quantum-hall-effect` is the core of draft `edge-channel` (2DEG + Landau gap + edge path). It stays **contrast** on `gapped-condensate`. A quantum point contact is contrast on `edge-channel`, not a member. The electron `edge` role is now consumed.

The two original handover sketches are now formal entries. Do not use the old preliminary numbers (in particular, reflection is ~40–85 atomic planes, not 100–200):

- [library/reflection.md](library/reflection.md) — collective screening; High mapping
- [library/permanent-magnet-latch.md](library/permanent-magnet-latch.md) — anisotropy latch; High mapping

Those two, plus [photoelectric-threshold](library/photoelectric-threshold.md), are the calibration trio in `analysis/fragments/gold.jsonl`. Applications that lean on the latch or the interstitial hypothesis should keep recovering those cliffs first ([thin-film-optics](application/thin-film-optics.md), [bonded-magnets](application/bonded-magnets.md)).

---

## 4. First-wave machines

| `design_key` | Status | One line |
|---|---|---|
| `collective-screening` | formal | Connected charged population; dies by buffer starvation or clock overrun |
| `anisotropy-latch` | formal | Barrier-protected directional memory; 0 W hold |
| `polar-latch` | formal | Electrical twin; remnant *P* at *E* = 0 |
| `gapped-condensate` | formal | Charged protected mode; *R* = 0 and expulsion are split artifacts |
| `chargeless-superflow` | formal | ⁴He analog; not the same hardware |
| `energy-gate` | formal | Discrete conversion; *N* = 1 per event |
| `oscillator-grid` | formal | Ion grid as coupled oscillators |
| `ensemble-average` | formal | Stable macro number from a large population; no universal *N* |
| `exchange-pin` | draft | Nested AFM/FM pin; collapse is *T*<sub>B</sub>, not FM *T*<sub>C</sub> |
| `edge-channel` | draft | 2DEG + bulk gap + edge path; integer *R_H = h/νe²*; QPC is contrast |

Shared requirements often share a **kind** of cliff, not a **number**. See [library/derived/requirement-audit.md](library/derived/requirement-audit.md) before quoting one thermal or length figure across machines.

---

## 5. What to do next

Prefer, in order:

1. Tighten a Medium mapping — statistical buffer, mesoscale step (*H*<sub>c</sub> ≪ *H*<sub>a</sub>, *E*<sub>c</sub>, pinning after *H*<sub>c1</sub>), or a taken rather than derived constant.
2. Correct fragment rows so `observed_text` still quotes the file; rebuild; keep derived sheets in sync.
3. Add a new effect only when the collapse is sharp and is not already a clause on an existing entry. Update [library/INDEX.md](library/INDEX.md) in the same change.
4. Add an eleventh design only when a hardware stack and collapse are not already owned. Do not invent one for every interface. Draft `edge-channel` is the QHE leftover; do not swallow QPC into it.
5. Add a `cataloged` node only under the admission filter in [library/nodes/README.md](library/nodes/README.md) (parent of a forced node, or already named as hardware). Do not vendor PDG. Proton / neutron are the likely next pair; muon and the dark-sector list stay out until a file names them.

Applications stay mappings and falsifiers, not protocols. EM-LENR waits on Steven’s review for the nuclear/configuration claim; isolate the interstitial latch first.

---

## 6. Continuity notes

- All quantitative claims must remain traceable to experimental boundaries.
- When a mapping is incomplete, state the incompleteness explicitly.
- Language discipline is non-negotiable: constraints, resources, synchronization, failure thresholds, emergent output only.
- The sole evaluation criteria remain utility of the extracted specifications and internal consistency of the mappings.
- Research recipes, term definitions, file map, and schema: [AGENTS.md](AGENTS.md).
