---
id: phonon
title: Phonon
kind: quasiparticle
origin: forced
status: formal
confidence: high
pdgid:
charge_e:
mass_si:
mass_text: not a rest mass
spin_text: unset
statistics: boson
lifetime_si:
identity_source: library/phonon-dispersion.md
description: Lattice mode of the oscillator-grid; dies by cutoff, mean-free-path collapse, or melt. No PDG ID.
updated: 2026-08-17
---

# Phonon

### 1. Name

Phonon. Quasiparticle / allowed clock of the ion grid. No PDG MC ID — do not invent one.

### 2. Taken specifications

- Not a rest-mass species. Statistics treated as boson (mode occupation).
- Allowed clocks are the measured *ω*(**q**). Ceiling *ω_D* / *Θ_D* is taken from the Debye entry.
- Lifetime is the mean free path / scattering time of [`thermal-conductivity-phonon`](../thermal-conductivity-phonon.md), not a PDG width.

### 3. Forced by

- [`phonon-dispersion`](../phonon-dispersion.md) — allowed-clock table.
- [`debye-cutoff`](../debye-cutoff.md) — no mode above *ω_D*.
- [`thermal-conductivity-phonon`](../thermal-conductivity-phonon.md) — *ℓ* is the transport resource.

### 4. Consumed as

- `oscillator-grid` — `mode`

### 5. Open

*ω*(**q**), *Θ_D*, and *ℓ*(*T*) are taken, not derived from node anharmonicity.

### 6. Contrast

Not a latch. Not a photon. A sound field is not a zero-power memory. Melt removes the grid that carries the mode.
