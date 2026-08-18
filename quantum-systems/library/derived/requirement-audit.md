---
origin: logically-derived
not_an_effect_entry: true
updated: 2026-08-17
---

# Shared-requirement audit

Which designs share a requirement, and whether they share a **number** or only a **kind**.  
Derived from `design_requirement` ⋈ `requirement`. Status is curated, not computed.

---

## Same kind, not the same number

### `thermal-cliff` — spec, satisfied, 6 designs

anisotropy-latch · polar-latch · gapped-condensate · chargeless-superflow · oscillator-grid · exchange-pin

| Design | The actual cliff |
|---|---|
| anisotropy-latch | Host *T*<sub>C</sub> (Fe 1043 K; Nd₂Fe₁₄B ~585 K) |
| polar-latch | Ferroelectric *T*<sub>C</sub> (BaTiO₃ ~393 K) |
| gapped-condensate | Superconducting *T*<sub>c</sub> (Nb 9.25 K … YBCO ~92 K) |
| chargeless-superflow | *T*λ = 2.17 K |
| oscillator-grid | *T*<sub>m</sub> (ice 273 K … W 3695 K) |
| exchange-pin | *T*<sub>B</sub> of the pin, **not** FM *T*<sub>C</sub> |

**Audit.** Kinship is real (a thermal resource destroys the ordered / coherent / crystalline population). Equating the numbers is a mapping error. EM-LENR “blocking line” is this *kind*; it is not NdFeB’s 585 K.

### `connected-spatial-buffer` — spec, satisfied, 2 designs

collective-screening · gapped-condensate

| Design | Length class |
|---|---|
| collective-screening | Optical δ ~ 10–20 nm; RF skin can be µm–mm |
| gapped-condensate | London *λ* ~ 40–50 nm (elements) |

**Audit.** Same failure class (starve the responding depth). Not the same formula. Do not quote 10 nm as London *λ*.

### `latch-cell-is-the-cliff` — consistency, satisfied, 2 designs

anisotropy-latch · polar-latch

**Audit.** Shared logic: grain / polar volume is the cliff, sample envelope is capacity. Polar side has **no portable *KV*** yet. Using 30 nm NdFeB as a ferroelectric number is over-claim.

---

## Shared number (or a true zero)

### `zero-hold-power` — spec, satisfied, 6 designs

anisotropy-latch · polar-latch · gapped-condensate · chargeless-superflow · collective-screening · exchange-pin

**Audit.** The number is actually the same: **0 W** (or 0 extra W for the mirror; 0 V for a persistent current). That is the cleanest join in the layer. “Hold-power test” in applications means: does the signature survive after the drive is dark? `phase-space-condensate` imposes the opposite spec (`not-zero-hold-power`). Do not quote 0 W as a BEC number.

### `gate-is-single-particle` — spec, satisfied, 2 designs

energy-gate (must) · collective-screening (should, as contrast)

**Audit.** *N* = 1 is a positive spec of the gate and a **negative** spec of screening. Same row, opposite machines. Photoelectric *N* = 1 is `incompatible` with collective-screening and `entails` for energy-gate.

---

## Shared closures (open on purpose)

| Requirement | Designs | What is still taken |
|---|---|---|
| `underived-penetration-depth` | screening (must), condensate (should) | δ, skin √, London *λ* |
| `mesoscale-coercivity` | anisotropy-latch (must), exchange-pin (should) | *H*<sub>c</sub> ≪ *H*<sub>a</sub>; Hex |
| `no-universal-n` | ensemble-average | Statistical buffer only |
| `underived-hall-quantum` | edge-channel | *R_K = h/e²* |
| `underived-conductance-quantum` | landauer-channel | \(2e^2/h\) |
| `phase-space-threshold-taken` | phase-space-condensate | \(n\lambda^3\simeq 2.612\) |

**Audit.** These are honest. Do not fill them with a guessed node count to make an application look closed.

---

## Tension, not a failed spec

### `bec-not-this-condensate` — consistency, **tension**, 3 designs

gapped-condensate (must) · chargeless-superflow (should) · phase-space-condensate (must)

**Audit.** Status `tension` stays: the leftover now has a home (`phase-space-condensate`) and still must not be folded into the pairing condensate or He-4. Do not “fix” the tension by inventing a gap or a 0 W hold.

---

## Predictions that are already library-true

| Requirement | Meaning for applications |
|---|---|
| `coupled-screening-failure` | A starved Ag film should lose *R*, SPR, and go plasma-transparent together |
| `average-replaced-by-order` | When a latch or gap opens, *χ* ~ 1/*T* and *γT* are the wrong readout |
| `split-r0-and-expulsion` | Type-II mixed state: *R* = 0 can outlive *χ* = −1 |
| `qpc-is-not-this-edge` | A 1D constriction’s `2e²/h` steps are not a Hall plateau |
| `hall-gap-not-pairing` | Landau / mobility gap is not 2Δ |

Use these as **coupled tests**, not as extra knobs.

---

## What this audit forbids in application files

- Quoting one thermal number across latch, superfluid, melt, and pin.
- Treating H/M or sample mass as a latch-cell cliff.
- Calling London *λ* the optical skin.
- Filing QHE or BEC as `gapped-condensate` members.
- Filing a quantum point contact as `edge-channel` (or quoting `2e²/h` as *R_K*).
- Closing *R_K* or \(2e^2/h\) with a Chern-number / Landauer derivation story.
- Quoting \(T_c(n)\) as \(T_\lambda\) or as a 0 W latch number.
- Treating defined *k* or *σ* as extracted machine constants.
