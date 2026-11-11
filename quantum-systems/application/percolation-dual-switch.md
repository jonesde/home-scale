---
origin: application
device: one metal film read out as specular R, dc sheet conductance and conducting-plate attraction while its thickness is walked through percolation
updated: 2026-11-14
envelope: MEMS / thin-film lab; packaged clutch would be the later consumer form
---

# Application: Percolation dual switch

**Device.** A single metal film (Ag, Au, Al class) used as both a visible reflector and one face of a sub-μm conducting-plate gap. As first written, the device was the **shared starve**: below percolation, or above the plasma / interband edge, specular *R* and the conducting-plate Casimir class were to die together. The measurements do not show that coupled collapse (note below). What they support is a film with three readouts of which only one, dc conductance, switches.
**QSA machines.** `collective-screening` (core); Casimir as supporting contrast on the same population (`predicted:casimir-force:starved-faces-kill-force`).
**Status.** Working application of `coupled-screening-failure` as a dual output, now with that requirement contradicted as worded. Not an SPR immunoassay chip and not a Casimir metrology bench. **Not a MEMS process spec.**
**Envelope.** Thin-film / MEMS lab. Stiction is industrial; a packaged clutch is the consumer form if anyone later builds one.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** Sub-μm gaps, patch charge, and (if actuated) MEMS snap-in are ordinary lab hazards. This file is a mapping, not a clutch design.

> **Corrected 2026-11-12**, after the sourcing of [reflection](../library/reflection.md) and [casimir-force](../library/casimir-force.md). Three facts changed. (1) Specular *R* has no cliff: it falls smoothly as a continuous film thins, and passes through percolation without a step. (2) Percolation is a threshold in dc conductance. (3) The Casimir force is reduced by a thin or visibly transparent face and is not removed: a 9 nm palladium film gives a smaller force than a thick one, indium tin oxide gives 40–50 % less than gold at 50–150 nm, and a mirror switched from reflecting to transparent gave no significant change at 70–400 nm. No force measurement on an islanded film below percolation was found. The concept is kept. It is restated in §1–§5 as a test of whether the three readouts separate, which is what the measurements indicate, and the original "die together" expectation is marked where it stood.

> **Re-checked 2026-11-14** against [reflection](../library/reflection.md), [casimir-force](../library/casimir-force.md) and [requirement-audit](../library/derived/requirement-audit.md); the numbers stand. Added: what the original clutch would need to be true (§2), the size of the force change that is supported (up to about a factor of two), and a note that roughness and patch limits are unsourced.

---

## 1. Claim

`coupled-screening-failure` named four artifacts of one starved film: ordinary *R*, transmission toward and above the plasma edge, Kretschmann SPR, and **conducting-plate Casimir contrast**. This file owns the last one as a *device output*, not as a prefactor to derive.

| Film state | Specular *R* | dc sheet conductance | Conducting-plate force |
|---|---|---|---|
| Continuous and thick, *ω* below the edge | High | Bulk-like | Present. For thick Au, Cu or Al, 0.48–0.55 of the ideal-plate value at 0.1 μm |
| Continuous, thinner than the optical decay length | Lower, smoothly (Ag at 550 nm: 39 % at 10 nm, 14 % at 5 nm) | Present | Measured: reduced, not zero (9 nm Pd) |
| Islanded / below percolation | Lower; island-plasmon band; no step at the transition (measured in Au) | **Lost. This is the threshold** | Not measured. First written as "should collapse" (`predicted:casimir-force:starved-faces-kill-force`); untested |
| Continuous but transparent in the visible | Low in the visible | Present | Measured: 40–50 % below Au–Au for indium tin oxide; no significant change for a hydride mirror switched to transparent. First written as "should collapse"; contradicted |
| Dielectric / no metal | Not this mirror | None | Different, weaker Lifshitz channel if any |

Gap *d* is the **capacity of the force** and is separate from the film knob. Opening the gap lowers the force on its own power law ([casimir-force](../library/casimir-force.md)); it is not a substitute for changing the film.

The *π²ℏc/240* prefactor stays taken. Do not close it with a node count.

---

## 2. Theory of operation

**Optical channel.** Same clock as [thin-film-optics](thin-film-optics.md): *ω* below the edge. *R* scales with the thickness traversed, on the decay length *δ* = *λ*/4π*k* (Ag 12–15 nm, Al 6.6–8.3 nm), with no minimum.

**dc channel.** A deposited film conducts across the substrate only above its percolation thickness: 6–7 nm for unseeded Au, 6–12 nm for unseeded Ag, 1–3 nm on a copper seed.

**Force channel.** The force depends on the response of the faces over a wide band around *c*/2*d*, which is 0.1–1 eV for gaps of 1–0.1 μm. A face that is transparent only in the visible and near infrared has lost part of that band, which is the stated reason the measured force falls by half or less. On that account a face would have to lose its response across the infrared to lose most of the force; no measurement of that case was found. Localized particle plasmons and residual patch charge are different artifacts. No source on roughness or patch potentials was opened for the library, so the limits they set are unsourced here.

**Switch.** Walk thickness through percolation on **all three** readouts. The measurements indicate that the dc channel steps while *R* and the force change smoothly. As a switch, then, the supported device is a dc one with two analog companions, and the supported experiment is the separation of the three. The original device, *R* and force dying together at percolation, depended on a reflectance cliff that does not exist and on a force collapse that is contradicted for transparent faces and untested for islands. For the original clutch to work, a face would have to lose its conduction across the infrared band around *c*/2*d*, and the force on such a face would have to be measured; neither exists in the opened sources. What is supported is a force that differs by up to about a factor of two between a good metal and a poor or thin conductor: a trim.

An SPR chip that never measures force is [thin-film-optics](thin-film-optics.md). A torsion-balance Casimir run that never changes the film is the library effect, not this application.

---

## 3. Knobs

| Parameter | Toward the three-readout test | Confound |
|---|---|---|
| Thickness / percolation | Walk through the percolation thickness of the chosen process, checking continuity and sheet resistance at each step | A mass-thickness series that never checks continuity; reading the smooth fall of *R* as a switch |
| *n* / plasma edge | Starve *n* or drive above the edge | Identifying *φ* with *ω<sub>p</sub>*; expecting the force to follow visible transparency |
| Gap *d* | Hold in the 0.1–1 μm *class* while the *film* is the knob | Opening *d* and calling that “percolation” |
| Patch / roughness (unsourced) | Must stay small against the force at the chosen gap | Electrostatic force read as Casimir |
| Coupler | SPR optional, as a fourth readout | SPR-only chip |

---

## 4. Isolation sequence

0. Thickness series: *R*(*λ*), *T*(*λ*) and sheet resistance ([thin-film-optics](thin-film-optics.md) tests 1–2). Expect a smooth optical curve and a dc step.  
1. Same series as a plate (or sphere–plate) at fixed *d*. First written: the attraction should vanish with *R*. Measured on a continuous thin film: reduced. Expect a force that falls with thickness and persists. The open measurement is the film below percolation.  
2. Continuous film, spectral walk through the plasma / interband edge. First written: *R* and the force class should move together. Contradicted for faces transparent in the visible; the force is not a function of *R* at one wavelength.  
3. Starve *n* on a TCO or doped film: IR *R* and RF *δ* move together (`predicted:skin-effect:same-n-kills-optical-and-rf`). On the wide-band account the force should fall as infrared conduction is lost. Untested.  
4. Photoemission on the same face: *φ* ≠ *ω<sub>p</sub>*.

---

## 5. Falsifiers

- Already observed: a face that lost its visible reflectance and kept its force (hydride mirror), and a visibly transparent face with about half the force (indium tin oxide). These contradict the coupled collapse as first written.  
- Still open: an island film that shows the conducting-plate force class at the same *d*. No measurement exists; the nearest results show reduction, not loss.  
- For the restated test: a step in *R* or in the force at the percolation thickness, coincident with the dc step, would restore the original device.  
- SPR dip that survives after the film is plasma-transparent at that *λ* (see the caution in [thin-film-optics](thin-film-optics.md) §5).  
- Treating the taken Casimir prefactor as a derived machine number.  
- Optical *R* that requires a hold current.

---

## 6. What this file is not

- Not an SPR immunoassay product.  
- Not a Casimir-force metrology paper.  
- Not [switchable-hydride-mirror](switchable-hydride-mirror.md) (occupancy is not the knob here).  
- Not a reason to quote the optical decay length (Ag 12–15 nm, Al 6.6–8.3 nm) as RF skin or London *λ*.

## 7. Links

- [thin-film-optics](thin-film-optics.md) — optical / SPR case  
- [casimir-force](../library/casimir-force.md) — library source  
- [reflection](../library/reflection.md) — thickness dependence and percolation thresholds  
- [switchable-hydride-mirror](switchable-hydride-mirror.md) — occupancy as a different way to reduce screening  
