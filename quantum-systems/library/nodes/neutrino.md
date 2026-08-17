---
id: neutrino
title: Neutrino
kind: elementary
origin: forced
status: formal
confidence: high
pdgid: 12
charge_e: 0
mass_si:
mass_text: small (oscillation; flavor-dependent)
spin_text: 1/2
statistics: fermion
lifetime_si:
identity_source: PDG 2026
description: Neutral lepton that forces CEνNS. Flavor is not split into three cards until an effect isolates one.
updated: 2026-08-17
---

# Neutrino

### 1. Name

Neutrino (flavor class). PDG MC ID `12` (\(\nu_e\)) stands for the class; \(\nu_\mu=14\), \(\nu_\tau=16\) are not separate first-wave cards.

### 2. Taken specifications

- Charge 0. Mass small compared with every energy in this library; flavor oscillation exists and is not this card. Spin \(1/2\) fermion.

### 3. Forced by

- [`coherent-neutrino-scattering`](../coherent-neutrino-scattering.md) — no neutrino \(\Rightarrow\) no CEνNS recoil.

### 4. Consumed as

- `energy-gate` — `input`

### 5. Open

Absolute mass and the three-flavor PMNS structure are taken / out of scope. This card does not mint a dark-sector species.

### 6. Contrast

Not a neutron. Not an axion. Inverse beta decay is a different gate (1.8 MeV, not this node’s identity).
