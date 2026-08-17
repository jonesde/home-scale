---
id: directional-moment
title: Directional moment
kind: quasiparticle
origin: forced
status: formal
confidence: high
pdgid:
charge_e:
mass_si:
mass_text: not a rest mass
spin_text: unset
statistics: unset
lifetime_si:
identity_source: library/permanent-magnet-latch.md
description: Barrier-protected directional cell of the latch machines (magnetic M or polar P). Not a Standard Model particle. No PDG ID.
updated: 2026-08-17
---

# Directional moment

### 1. Name

Directional moment. QSA latch-cell constituent: a written orientation of *M* or *P*. Not a Standard Model species. No PDG MC ID.

### 2. Taken specifications

- Not a rest mass. The barrier is *KV* (magnetic) or the polar well (ferroelectric). Hold-power is 0 W inside the envelope.
- Escape clock is *τ*₀ exp(*KV*/*kT*), not a PDG width.

### 3. Forced by

- [`permanent-magnet-latch`](../permanent-magnet-latch.md) — anisotropy barrier.
- [`curie-paramagnetism`](../curie-paramagnetism.md) — unlocked contrast (no remnant at *B* = 0).
- Polar twin on [`ferroelectric-remanence`](../ferroelectric-remanence.md) (same role, electrical well).

### 4. Consumed as

- `anisotropy-latch` — `latch-cell`
- `polar-latch` — `latch-cell`
- `exchange-pin` — `latch-cell` (the pin holds a second written direction)

### 5. Open

Technical *H_c* ≪ *H_a* and *E_c* / depolarization remain mesoscale. This card does not close them.

### 6. Contrast

Not Curie *χ* = *C*/*T*. Not a photon trail. Superparamagnetism is this cell under-provisioned in volume, not a different particle.
