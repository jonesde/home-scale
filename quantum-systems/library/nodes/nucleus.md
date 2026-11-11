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
updated: 2026-11-11
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

[`proton`](proton.md) and [`neutron`](neutron.md), the parents of this class, are now `forced` cards of their own. This card does not split *Z* or *A*.

### 6. Contrast

Not empty space. Not the electron that opens only at the triplet threshold 2.044 MeV. Not a vacuum ledger.

Identity values checked against PDG 2026 ([Monte Carlo numbering scheme](https://pdg.lbl.gov/2026/reviews/rpp2026-rev-monte-carlo-numbering.pdf), nuclear-code format) and CODATA 2022 ([electron mass energy equivalent](https://physics.nist.gov/cgi-bin/cuu/Value?mec2mev), for the 1.022 and 2.044 MeV thresholds) on 2026-11-11.
