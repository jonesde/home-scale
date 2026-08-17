---
id: electron
title: Electron
kind: elementary
origin: forced
status: formal
confidence: high
pdgid: 11
charge_e: -1
mass_si: 9.1093837139e-31
mass_text: 510.99895069 keV/c²
spin_text: 1/2
statistics: fermion
lifetime_si:
identity_source: PDG 2026; CODATA 2022
description: Charged fermion consumed as a collective population, a single-node gate, a Fermi-surface average, or (unmapped) a QHE edge path.
updated: 2026-08-17
---

# Electron

### 1. Name

Electron. Same species in four QSA roles; the roles are not four particles.

### 2. Taken specifications

- Charge −*e*. PDG MC ID `11`.
- Mass 510.99895069 keV/*c*² (PDG 2026); 9.1093837139×10⁻³¹ kg (CODATA 2022). Taken, not derived.
- Spin 1/2 fermion. Stable on any laboratory clock here.
- Antiparticle is [`positron`](positron.md) (`pdgid` −11), not a second mass.

### 3. Forced by

- [`reflection`](../reflection.md) / [`plasma-frequency-cutoff`](../plasma-frequency-cutoff.md) — connected charged population; dies by starve or *ω > ω_p*.
- [`photoelectric-threshold`](../photoelectric-threshold.md) — *N* = 1 conversion. Contrast with the collective buffer.
- [`electron-heat-capacity`](../electron-heat-capacity.md) — Fermi-surface slice ~*T*/*T_F*.
- [`quantum-hall-effect`](../quantum-hall-effect.md) — 2DEG + perpendicular *B*. No design consumes the `edge` role yet.

### 4. Consumed as

- `collective-screening` — `population`
- `energy-gate` — `single`
- `ensemble-average` — `average`
- `gapped-condensate` — `population` (the 2*e* increment is not this node)

No `edge` design role. That is the QHE leftover.

### 5. Open

Mass, *φ*, *γ*, optical *δ*, and London *λ* are taken. This card does not close them. The 2*e* fluxoid increment is `fluxoid-increment-2e`, not an electron subspecies.

### 6. Contrast

Not the photon. Not a Cooper pair. Not the unlocked Curie moment. A single photoelectron is incompatible with treating the same surface as *N* = 1 screening.
