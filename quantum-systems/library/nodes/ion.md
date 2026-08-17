---
id: ion
title: Ion (lattice occupant)
kind: composite
origin: forced
status: formal
confidence: medium
pdgid:
charge_e:
mass_si:
mass_text: host-dependent
spin_text: unset
statistics: unset
lifetime_si:
identity_source: library/debye-cutoff.md
description: Host ion / lattice site that provisions 3N mechanical modes; the grid stops being a grid at Tm. Class node, not one isotope.
updated: 2026-08-17
---

# Ion (lattice occupant)

### 1. Name

Ion / lattice site. Class node for the oscillator-grid matrix. Not one PDG nuclide.

### 2. Taken specifications

- Charge, mass, and chemistry are host-dependent. No single `pdgid`.
- Finite *N* ⇒ 3*N* modes ([`debye-cutoff`](../debye-cutoff.md)).

### 3. Forced by

- [`debye-cutoff`](../debye-cutoff.md) — 3*N* modes; too-few-nodes collapse.
- [`melting`](../melting.md) — Bragg / shear order gone at *T_m*.

### 4. Consumed as

- `oscillator-grid` — `matrix`
- `anisotropy-latch` / `polar-latch` — `matrix` (the lattice that hosts the well)

### 5. Open

*T_m* and the moduli are taken (`melting-not-derived`, `underived-grid-couplings`). This card does not derive them.

### 6. Contrast

Not the electron gas. Not a free ion in vacuum. Destruction of this matrix erases latches that live on it; the latch entries own that erase path.
