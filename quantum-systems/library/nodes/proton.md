---
id: proton
title: Proton
kind: elementary
origin: forced
status: formal
confidence: high
pdgid: 2212
charge_e: 1
mass_si: 1.67262192595e-27
mass_text: 938.272 MeV/c²
spin_text: 1/2
statistics: fermion
lifetime_si:
identity_source: PDG 2026
description: Bound nucleon; photodisintegration product of the deuteron and a constituent of the nucleus class.
updated: 2026-08-17
---

# Proton

### 1. Name

Proton. PDG MC ID `2212`.

### 2. Taken specifications

- Charge \(+e\). Mass \(938.272\,\mathrm{MeV}/c^{2}\) (PDG 2026). Spin \(1/2\) fermion. Stable on every clock in this library.

### 3. Forced by

- [`deuteron-photodisintegration`](../deuteron-photodisintegration.md) — product of the \(2.224\,\mathrm{MeV}\) unbinding.

### 4. Consumed as

- `energy-gate` — `product`

### 5. Open

Mass is taken. The proton as a QCD bound state is not derived here. Parent of the [`nucleus`](nucleus.md) class, now forced rather than merely cataloged.

### 6. Contrast

Not the neutron. Not a muon. Not the recoil *class* `nucleus`.
