---
origin: application
device: gapped 2DEG used as a B-orientation inhibit, not as the SI ohm
updated: 2026-11-11
envelope: cryogenic high-B lab until higher-T graphene packaging exists
---

# Application: Orientation-inhibited edge path

**Device.** A 2DEG Hall bar whose integer plateau is used as an **inhibit**: rotate *B* in-plane and the *R<sub>H</sub>* = *R<sub>K</sub>/ν* lock is a non-occurrence. The used device is the resistance quantum. This file is the opposite knob.
**QSA machines.** Draft `edge-channel` (core); `landauer-channel` as contrast (steps at *B* = 0); cyclotron resonance as the same *eB/m* combination with a different output.
**Status.** Working application of the leftover transport split, not a QHE resistance standard and not a QPC kit. **Not a cryostat SOP.**
**Envelope.** Cryogenic high-*B* lab. Higher-*T* graphene integer plateaus sit on the same gap-versus-*kT* clause; packaging that would make this home-scale does not exist yet.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** High field magnets and cryogens are institutional hazards. This file is a mapping, not a magnet procedure. Do not close *R<sub>K</sub>* or \(2e^2/h\) with a Chern / Landauer derivation story.

> **Checked 2026-11-11.** This file quotes no numbers beyond the defined constants *R<sub>K</sub>* = *h*/*e*² and 2*e*²/*h*. The library entries it rests on ([quantum-hall-effect](../library/quantum-hall-effect.md), [quantum-point-contact](../library/quantum-point-contact.md), [cyclotron-resonance](../library/cyclotron-resonance.md), [coulomb-blockade](../library/coulomb-blockade.md)) have not been converted to the sourcing standard, so every physical statement below is **unsourced** until they are. None of the cliffs removed elsewhere in this pass is used here. One wording change: the in-plane field is described as the end of a continuous tilt dependence. The standard expectation, not yet sourced here, is that the plateaus follow the perpendicular component of *B*, so the inhibit is graded in tilt angle and complete only when that component is too small to open a gap larger than *kT*.

> **Corrected 2026-11-11.** [quantum-hall-effect](../library/quantum-hall-effect.md) and [quantum-point-contact](../library/quantum-point-contact.md) are now sourced, so the statements below that rest on them are no longer unsourced. The tilt dependence is established physics, not an expectation: in silicon inversion layers tilted up to 90° the orbital quantization depends solely on the normal component *B* cos *θ*, and the parallel component has a negligible effect on it ([Fang and Stiles, *Phys. Rev.* 174, 823 (1968)](https://doi.org/10.1103/PhysRev.174.823), abstract). The inhibit is therefore a crossover in tilt angle. The parallel component still acts on the spin splitting, so a tilt at fixed normal field is not a null operation for spin-resolved plateaus. The constriction steps were measured with no magnetic field applied ([van Wees et al., *Phys. Rev. Lett.* 60, 848 (1988)](https://doi.org/10.1103/PhysRevLett.60.848), abstract) and are accurate to about 1 %, against parts in 10¹⁰ for the Hall plateau, so the contrast column is also a contrast in precision. Graphene plateaus at 300 K needed 29–45 T ([Novoselov et al., arXiv:cond-mat/0702408](https://arxiv.org/abs/cond-mat/0702408)). [cyclotron-resonance](../library/cyclotron-resonance.md) and [coulomb-blockade](../library/coulomb-blockade.md) were sourced separately; this note does not check them.

---

## 1. Claim

Integer QHE hardware is a 2DEG + perpendicular *B* that opens a bulk gap + an edge path. With *B* in the plane the perpendicular component is zero and the artifact does not occur. Between the two orientations the plateaus follow the normal component *B* cos *θ* (measured; see the 2026-11-11 note above). A ballistic 1D constriction at *B* = 0 shows \(2e^2/h\) steps and is a different machine (measured: `quantum-point-contact:consistency_gap:not-qhe`, `quantum-point-contact:emergent_output:two-e-squared-over-h`).

The cyclotron line on the same wafer shares *ω<sub>c</sub>* = *eB/m* and is not the plateau (`predicted:cyclotron-resonance:same-omega-c-not-a-plateau`). *R<sub>Q</sub>* as a tunnel floor is not *R<sub>K</sub>* (`predicted:coulomb-blockade:rq-is-not-rk`).

| Configuration | Output | Machine |
|---|---|---|
| 2DEG, *B* ⊥, *ν* in a gap | *R<sub>H</sub>* = *R<sub>K</sub>/ν*, *R<sub>xx</sub>* → 0 | `edge-channel` |
| Same bar, *B* tilted by *θ* | Plateaus at the field where *B* cos *θ* matches (measured) | `edge-channel`, shifted |
| Same bar, *B* in-plane | Plateau gone | Inhibit (this file) |
| Split-gate QPC, *B* = 0 | \(n\times 2e^2/h\) steps | `landauer-channel` |
| Microwave on, *ω* = *ω<sub>c</sub>* | *m\** absorption line | Cyclotron; not the plateau |

*R<sub>K</sub>* stays taken (`underived-hall-quantum`). This file does not use the plateau as an ohm.

---

## 2. Theory of operation

**On.** Perpendicular *B* opens the Landau / mobility gap. Current lives on the edge. *kT* and Hall field stay below the gap.

**Inhibit.** Rotate *B* in-plane (the plateaus follow *B* cos *θ* on the way, so the inhibit is the end of a continuous shift, not a switch), or walk *ν* off a plateau, or overrun the gap with *T* or current, or destroy the 2DEG. The lock disappears.

**Do not convert.** Pinching the same 2DEG into a short constriction without *B* is not “the plateau at zero field.” It is `landauer-channel`. Gating an island until *E<sub>c</sub>* > *kT* is `energy-gate` (charging), not *R<sub>K</sub>*.

---

## 3. Knobs

| Parameter | Toward a clean inhibit | Category error |
|---|---|---|
| *B* orientation | Perpendicular (on) to in-plane (off); in between, plateaus track *B* cos *θ* | Demanding *B* to open QPC steps |
| Filling *ν* | Sit in a gap, then walk off | Calling off-plateau “the ohm drifted” |
| *T*, current | Stay below the Landau/mobility gap | Graphene high-*T* plateaus as a second family |
| Constriction gate | Contrast column at *B* = 0 | Filing those steps as *R<sub>K</sub>/ν* |
| Microwave *ω* | Optional CR column | Walking off *ω<sub>c</sub>* and expecting *R<sub>H</sub>* to move |

---

## 4. Isolation sequence

0. 2DEG density / mobility check — buffer present.  
1. *B* ⊥, integer *ν* — plateau + *R<sub>xx</sub>* → 0.  
2. Rotate toward in-plane *B* at similar |*B*|, recording several tilt angles — plateaus move with the perpendicular component and are gone in-plane.  
3. Same chip, QPC at *B* = 0 — \(2e^2/h\) steps or pinch-off; no Hall plateau.  
4. Optional: CR line at *ω<sub>c</sub>*; walk *ω* off resonance — line dies, *R<sub>H</sub>* unmoved.  
5. Optional: Coulomb island — diamonds period *e*, *R<sub>Q</sub>* floor, not *R<sub>K</sub>*.

---

## 5. Falsifiers

- Steps that *require* a Landau ladder.  
- A Hall plateau at *B* = 0.  
- Identifying \(2e^2/h\) with *R<sub>K</sub>*, or *R<sub>Q</sub>* with *R<sub>K</sub>*.  
- Off-resonance cyclotron absorption moving *R<sub>H</sub>* off *R<sub>K</sub>/ν*.  
- Closing *R<sub>K</sub>* with a Chern-number story in this file.

---

## 6. What this file is not

- Not the SI ohm.  
- Not a QPC product or a SET electrometer.  
- Not `gapped-condensate` (Landau gap ≠ 2Δ; no Meissner).  
- Not a reason to file QSHE/QAHE here; those remain the unfiled cousin (`predicted:edge-channel:qshe-cousin-if-filed`).

## 7. Links

- [quantum-hall-effect](../library/quantum-hall-effect.md) — library source  
- [quantum-point-contact](../library/quantum-point-contact.md) — contrast machine  
- [cyclotron-resonance](../library/cyclotron-resonance.md) — same clock, different output  
