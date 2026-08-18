---
origin: application
device: one metal film whose connected-to-island transition kills specular R and conducting-plate attraction together
updated: 2026-08-17
envelope: MEMS / thin-film lab; packaged clutch would be the later consumer form
---

# Application: Percolation dual switch

**Device.** A single metal film (Ag, Au, Al class) used as both a visible reflector and one face of a sub-μm conducting-plate gap. The device is the **shared starve**: below percolation, or above the plasma / interband edge, specular *R* and the conducting-plate Casimir class die together.
**QSA machines.** `collective-screening` (core); Casimir as supporting contrast on the same population (`predicted:casimir-force:starved-faces-kill-force`).
**Status.** Working application of `coupled-screening-failure` as a dual output, not an SPR immunoassay chip and not a Casimir metrology bench. **Not a MEMS process spec.**
**Envelope.** Thin-film / MEMS lab. Stiction is industrial; a packaged clutch is the consumer form if anyone later builds one.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** Sub-μm gaps, patch charge, and (if actuated) MEMS snap-in are ordinary lab hazards. This file is a mapping, not a clutch design.

---

## 1. Claim

`coupled-screening-failure` now names four artifacts of one starved film: ordinary *R*, transmission toward and above the plasma edge, Kretschmann SPR, and **conducting-plate Casimir contrast**. This file owns the last one as a *device output*, not as a prefactor to derive.

| Film state | Specular *R* | Conducting-plate force class |
|---|---|---|
| Continuous, *ω* < *ω<sub>p</sub>* (or Ag optical edge) | High | Present (1/*d*⁴ class if the gap is in window) |
| Islanded / below percolation | Collapsed | Should collapse (`predicted:casimir-force:starved-faces-kill-force`) |
| Continuous but plasma-transparent at that *λ* | Collapsed | Should collapse (lost conducting contrast) |
| Dielectric / no metal | Not this mirror | Different, weaker Lifshitz channel if any |

Gap *d* is **capacity of the force**, not the optical cliff. Opening the gap into the noise is Casimir’s own starve ([casimir-force](../library/casimir-force.md)); it is not a substitute for percolation.

The *π²ℏc/240* prefactor stays taken. Do not close it with a node count.

---

## 2. Theory of operation

**Optical channel.** Same buffer and clock as [thin-film-optics](thin-film-optics.md): connected depth ~ *δ*, *ω* < *ω<sub>p</sub>*.

**Force channel.** The faces still need a screening population so the gap modes are cut off. Starve that population and this attraction dies with the mirror. Localized particle plasmons and residual patch charge are different artifacts.

**Switch.** Walk thickness through percolation, or walk *n* / *ω* through the plasma edge, on **both** readouts. That is the device. An SPR chip that never measures force is [thin-film-optics](thin-film-optics.md). A torsion-balance Casimir run that never starves the film is the library effect, not this application.

---

## 3. Knobs

| Parameter | Toward a dual switch | Collapse / confound |
|---|---|---|
| Thickness / percolation | Walk through ~5–10 nm continuous / island | Only a mass-thickness series that never checks continuity |
| *n* / plasma edge | Starve *n* or drive above the edge | Identifying *φ* with *ω<sub>p</sub>* |
| Gap *d* | Hold in the 0.1–1 μm *class* while the *film* is the knob | Opening *d* and calling that “percolation” |
| Patch / roughness | Must stay below the Casimir window | Electrostatic swamping sold as Casimir |
| Coupler | SPR optional, as a third sibling | SPR-only chip |

---

## 4. Isolation sequence

0. Thickness series: *R*(*λ*), *T*(*λ*) — recover the optical cliff ([thin-film-optics](thin-film-optics.md) tests 1–2, including `predicted:surface-plasmon-resonance:island-film-no-dip` and `…:dies-above-plasma-edge` if a coupler is present).  
1. Same series as a plate (or sphere–plate) at fixed *d*: conducting-plate attraction should vanish with *R*.  
2. Continuous film, spectral walk through the plasma / interband edge: *R* and the force class should move together.  
3. Starve *n* on a TCO or doped film: IR *R* and RF *δ* move together (`predicted:skin-effect:same-n-kills-optical-and-rf`); force contrast should follow the lost metal.  
4. Photoemission on the same face: *φ* ≠ *ω<sub>p</sub>*.

---

## 5. Falsifiers

- Island film that still shows the conducting-plate 1/*d*⁴ class at the same *d*.  
- Plasma-transparent film that still mirrors.  
- SPR dip that survives after the film is plasma-transparent at that *λ*.  
- Treating the taken Casimir prefactor as a derived machine number.  
- Optical *R* that requires a hold current.

---

## 6. What this file is not

- Not an SPR immunoassay product.  
- Not a Casimir-force metrology paper.  
- Not [switchable-hydride-mirror](switchable-hydride-mirror.md) (occupancy is not the knob here).  
- Not a reason to quote 10–20 nm optical *δ* as RF skin or London *λ*.

## 7. Links

- [thin-film-optics](thin-film-optics.md) — optical / SPR calibration  
- [casimir-force](../library/casimir-force.md) — library source  
- [switchable-hydride-mirror](switchable-hydride-mirror.md) — occupancy as a different way to starve screening  
