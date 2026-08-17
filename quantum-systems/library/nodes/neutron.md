---
id: neutron
title: Neutron
kind: elementary
origin: forced
status: formal
confidence: high
pdgid: 2112
charge_e: 0
mass_si: 1.67492750056e-27
mass_text: 939.565 MeV/c²
spin_text: 1/2
statistics: fermion
lifetime_si: 879.4
identity_source: PDG 2026
description: Neutral nucleon. Photodisintegration product, UCN in the gravitational well, and coherent CEνNS scatterer (via the nucleus).
updated: 2026-08-17
---

# Neutron

### 1. Name

Neutron. PDG MC ID `2112`.

### 2. Taken specifications

- Charge 0. Mass \(939.565\,\mathrm{MeV}/c^{2}\) (PDG 2026). Spin \(1/2\) fermion.
- Free lifetime \(\tau_n \approx 879\,\mathrm{s}\) (beam / bottle class; the discrepancy is not this card). Bound in a nucleus it is stable on library clocks.

### 3. Forced by

- [`deuteron-photodisintegration`](../deuteron-photodisintegration.md) — product.
- [`neutron-gravitational-states`](../neutron-gravitational-states.md) — the UCN in the well.
- [`coherent-neutrino-scattering`](../coherent-neutrino-scattering.md) — \(N^{2}\) coherent amplitude tracks neutron number.

### 4. Consumed as

- `energy-gate` — `product` (photodisintegration)
- no design yet consumes the gravitational-well role (leftover, like QHE `edge`)

### 5. Open

Mass and free lifetime are taken. Bottle-versus-beam lifetime tension is not closed here.

### 6. Contrast

Not the proton. Not a phonon. A thermal neutron is not a UCN.
