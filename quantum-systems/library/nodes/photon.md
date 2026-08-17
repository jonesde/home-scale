---
id: photon
title: Photon
kind: elementary
origin: forced
status: formal
confidence: high
pdgid: 22
charge_e: 0
mass_si: 0
mass_text: massless
spin_text: 1
statistics: boson
lifetime_si:
identity_source: PDG 2026
description: Massless boson that opens energy gates as an input and appears as the thermal EM average; not a stored record.
updated: 2026-08-17
---

# Photon

### 1. Name

Photon (γ). PDG MC ID `22`.

### 2. Taken specifications

- Charge 0. Massless. Spin 1 boson.
- No rest-mass cliff of its own. Pair production’s 1.022 MeV is 2*m_e c*² on the electron/positron side, not a photon mass.

### 3. Forced by

- [`photoelectric-threshold`](../photoelectric-threshold.md) / other energy gates — under-threshold input is non-occurrence.
- [`pair-production`](../pair-production.md) — photon plus a nearby nucleus.
- [`blackbody-spectrum`](../blackbody-spectrum.md) / [`stefan-boltzmann`](../stefan-boltzmann.md) — thermal EM average.

### 4. Consumed as

- `energy-gate` — `input`
- `collective-screening` — `input` (the drive; the film is not a written trail of the photon)
- `ensemble-average` — `average`

### 5. Open

*k* and *σ* are defined SI constants, not extracted (`defined-constants-not-extracted`). This card does not derive a photon from node rules.

### 6. Contrast

Not the plasma / interband edge (*φ* ≠ *ω_p*). Not a latch. Empty space does not convert a lone photon to a pair.
