---
id: positron
title: Positron
kind: elementary
origin: forced
status: formal
confidence: high
pdgid: -11
charge_e: 1
mass_si: 9.1093837139e-31
mass_text: 510.99895069 keV/c²
spin_text: 1/2
statistics: fermion
lifetime_si:
identity_source: PDG 2026; CODATA 2022
description: Antiparticle of the electron; pair-production product witnessed by the 511 keV annihilation line.
updated: 2026-08-17
---

# Positron

### 1. Name

Positron (*e*⁺). PDG MC ID −11. Same mass as [`electron`](electron.md); opposite charge.

### 2. Taken specifications

- Charge +*e*. Mass 510.99895069 keV/*c*² (PDG 2026); 9.1093837139×10⁻³¹ kg (CODATA 2022).
- Spin 1/2 fermion. Not a laboratory-stable free population in these files; the witness is annihilation.

### 3. Forced by

- [`pair-production`](../pair-production.md) — product of the 2*m_e c*² gate, plus the 511 keV line.

### 4. Consumed as

- `energy-gate` — `product`

### 5. Open

*m_e* is taken (`pair-production:consistency_gap:underived-me`). This card does not derive it.

### 6. Contrast

Not a second electron. Not a stored pair. The gate still fails in empty space even above 1.022 MeV.
