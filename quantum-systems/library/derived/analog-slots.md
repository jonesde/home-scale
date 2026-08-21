---
origin: logically-derived
not_an_effect_entry: true
updated: 2026-08-20
---

# Analog-slot map

Which **slot** on a first-wave machine is a catalog file, which is a clause on an existing file, and which is still a hole. Inherited from the effect catalog and the twelve designs. No new measurements. If this note disagrees with an effect file, the effect file wins.

A slot is a piece of machine anatomy that can have its own collapse (latch vs loop vs partition vs volume cliff). Add a file only when that collapse is sharp and is not already a clause. Pattern leftovers (magnetic maze, polar stripe vs 90° vs 180°, vortex pinning landscape) stay in §4.6, not new slugs.

Conventional handbook names that stay clauses are also listed in [`../INDEX.md`](../INDEX.md#handbook-topics-not-filed-as-effects) so a table-of-contents search still works.

---

## Latched order — `anisotropy-latch` vs `polar-latch`

This is the block [`ferroelectric-domains`](../ferroelectric-domains.md) fills.

| Slot | Magnet (`anisotropy-latch`) | Polar (`polar-latch`) | Status |
|---|---|---|---|
| Latch (net remnant at 0 W) | [`permanent-magnet-latch`](../permanent-magnet-latch.md) | [`ferroelectric-remanence`](../ferroelectric-remanence.md) | filled both |
| Write / erase loop | [`ferromagnetic-hysteresis`](../ferromagnetic-hysteresis.md) | folded into remanence (*P*–*E* loop, *E<sub>c</sub>*) | polar combined on purpose |
| Volume cliff of the *latch* | [`superparamagnetism`](../superparamagnetism.md) | superparaelectric **clause** on remanence | polar stays a clause until a portable *KV* exists |
| Partition of a large body | [`magnetic-domains`](../magnetic-domains.md) | [`ferroelectric-domains`](../ferroelectric-domains.md) | filled both |
| Geometry barrier | [`shape-anisotropy`](../shape-anisotropy.md) | slab depolarization (*E<sub>d</sub>* ~ *P*/ε) | polar not a file; [`polar-depolarization-buffer`](requirement-audit.md) stays open |
| Cancelled order | [`antiferromagnetic-order`](../antiferromagnetic-order.md) | antiferroelectric (net *P* ≈ 0, double loop) | **hole** |
| Nested pin | [`exchange-bias`](../exchange-bias.md) / draft `exchange-pin` | imprint / charged-wall addressing | polar is a clause on domains, **not** a 13th design |
| Strain channel | [`magnetostriction`](../magnetostriction.md) | [`piezoelectricity`](../piezoelectricity.md); 90° walls on domains | filled; other family (`lattice-modes`) |
| Δ*T* bound-charge pump | — | only visible via [`pyroelectric-fusion`](../pyroelectric-fusion.md) | **hole** (engine vs nuclear gate) |

Shared *kind* across the two columns: `zero-hold-power`, `thermal-cliff`. Not shared *number*. Do not quote NdFeB ~30 nm or 585 K as a ferroelectric wall or Curie figure. Polar wall width is nm-class (~0.5 nm 180°, few nm 90°), not magnetic √(*A*/*K*) tens-of-nm.

---

## Gapped coherence — `gapped-condensate` (already split on purpose)

| Slot | File | Status |
|---|---|---|
| Transport *R* = 0 | [`superconductivity`](../superconductivity.md) | filled |
| Expulsion | [`meissner`](../meissner.md) | filled (split rule) |
| Weak link | [`josephson-effect`](../josephson-effect.md) | filled |
| Quantized loop | [`flux-quantization`](../flux-quantization.md) | filled |
| Mixed-state **partition** | [`type-ii-critical-field`](../type-ii-critical-field.md) | filled — analog of domains, different family |
| Chargeless analog | [`superfluid-helium-4`](../superfluid-helium-4.md) | filled (`chargeless-superflow`) |
| Dilute leftover | [`bose-einstein-condensate`](../bose-einstein-condensate.md) → draft `phase-space-condensate` | leftover has a home |
| Edge leftover | [`quantum-hall-effect`](../quantum-hall-effect.md) → draft `edge-channel`; [`quantum-point-contact`](../quantum-point-contact.md) contrast `landauer-channel` | leftover has a home |

Pinning after *H*<sub>c1</sub> is a **clause** / open requirement (`pinning-after-hc1`), not a second mixed-state file.

---

## Collective screening — do not force a latch anatomy

Driven machine: no stored bit when the incident field is gone. Reflection / skin / plasma cutoff / SPR / TIR / Faraday / cyclotron / Casimir / Aharonov–Bohm already occupy the collapse slots that exist.

Magneto-optical Kerr is Faraday’s reflection-side twin — a clause on [`faraday-rotation`](../faraday-rotation.md) and [`reflection`](../reflection.md), listed in the INDEX handbook table.

---

## Holes worth a file later (not this note)

Same split rule as domains: distinct collapse, not already a clause.

1. **Ordinary pyroelectricity** — Δ*T*-driven face charge / current pulse. Not remanent *P*, not 2.45 MeV neutrons. Today the engine is only visible through pyroelectric-fusion and the polar beam-target application.
2. **Antiferroelectric order** — cancelled polar latch, analog of antiferromagnetic order.

Do not queue those names in INDEX until the file exists. Do not mint a seventh family for topology. Do not file superparaelectric, polar *P*–*E* as a split of remanence, polar “shape anisotropy,” optical wall motion, charged-wall nanoelectronics, Kerr, or ferroelasticity as their own effects — they are the INDEX handbook-topics table.

---

## How to use this map

1. Name the macroscopic output and its dominant collapse.
2. Find the slot in the table for that machine.
3. If the slot is **filled**, open that file; do not add a sibling.
4. If the slot is a **clause**, tighten the owning file or leave the INDEX handbook row as the table of contents.
5. If the slot is a **hole** and the collapse is sharp, that is a candidate for a new effect — INDEX row in the same change, analog-slot row flipped from hole to filled.
