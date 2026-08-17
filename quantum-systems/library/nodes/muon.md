---
id: muon
title: Muon
kind: elementary
origin: forced
status: formal
confidence: high
pdgid: 13
charge_e: -1
mass_si: 1.883531627e-28
mass_text: 105.658 MeV/c²
spin_text: 1/2
statistics: fermion
lifetime_si: 2.197e-6
identity_source: PDG 2026
description: Unstable charged lepton that opens the muon-catalyzed-fusion nuclear gate. Not a latch. Not the electron.
updated: 2026-08-17
---

# Muon

### 1. Name

Muon (\(μ^-\)). PDG MC ID `13`. Antiparticle \(μ^+\) is `−13` and does not catalyze this cycle.

### 2. Taken specifications

- Charge −*e*. Mass 105.658 MeV/*c*² (PDG 2026); \(m_\mu/m_e \approx 206.8\).
- Spin 1/2 fermion. Mean lifetime \(2.197\times 10^{-6}\,\mathrm{s}\). Taken, not derived.
- Heavier charged lepton. Not a quasiparticle of a lattice.

### 3. Forced by

- [`muon-catalyzed-fusion`](../muon-catalyzed-fusion.md) — no muon ⇒ channel closed; \(\tau_\mu\) and sticking erase the catalyst.

### 4. Consumed as

- `energy-gate` — `input` (the node that opens the nuclear well)

### 5. Open

Mass and lifetime are PDG taken values, same class as \(m_e\) on pair production. Production cost per muon is not a node specification.

### 6. Contrast

Not the [`electron`](electron.md). Not a [`directional-moment`](directional-moment.md). A muon-free hydride is not this hardware.
