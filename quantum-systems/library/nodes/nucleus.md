---
id: nucleus
title: Nucleus (recoil partner)
kind: composite
origin: forced
status: formal
confidence: high
pdgid:
charge_e:
mass_si:
mass_text: M ≫ me (class)
spin_text: unset
statistics: unset
lifetime_si:
identity_source: library/pair-production.md
description: Nearby mass that can recoil so a photon can convert to e+e-. Empty space is under-provisioned. Not one isotope.
updated: 2026-08-17
---

# Nucleus (recoil partner)

### 1. Name

Nucleus, as the momentum sink of [`pair-production`](../pair-production.md). Class node. PDG nuclear IDs (`10LZZZAAAI`) are out of scope until an effect isolates a nuclide.

### 2. Taken specifications

- *M* ≫ *m_e* for the ordinary nuclear-field threshold 2*m_e c*² = 1.022 MeV.
- Charge *Z* scales the Bethe–Heitler yield (*Z*²); that is a rate, not a second gate.
- No single `pdgid`.

### 3. Forced by

- [`pair-production`](../pair-production.md) — `failure_mode:no-recoil-partner` and `hardware_scale:photon-plus-nucleus`. Isolated photons in empty space do not convert.

### 4. Consumed as

- `energy-gate` — `recoil`

### 5. Open

Proton and neutron are the likely next `cataloged` cards (parents of this class). They are not first-wave nodes. This card does not split *Z* or *A*.

### 6. Contrast

Not empty space. Not the electron that opens only at the triplet threshold 2.044 MeV. Not a vacuum ledger.
