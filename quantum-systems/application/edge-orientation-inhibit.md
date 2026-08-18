---
origin: application
device: gapped 2DEG used as a B-orientation inhibit, not as the SI ohm
updated: 2026-08-17
envelope: cryogenic high-B lab until higher-T graphene packaging exists
---

# Application: Orientation-inhibited edge path

**Device.** A 2DEG Hall bar whose integer plateau is used as an **inhibit**: rotate *B* in-plane and the *R<sub>H</sub>* = *R<sub>K</sub>/ν* lock is a non-occurrence. The used device is the resistance quantum. This file is the opposite knob.
**QSA machines.** Draft `edge-channel` (core); `landauer-channel` as contrast (steps at *B* = 0); cyclotron resonance as the same *eB/m* combination with a different output.
**Status.** Working application of the leftover transport split, not a QHE resistance standard and not a QPC kit. **Not a cryostat SOP.**
**Envelope.** Cryogenic high-*B* lab. Higher-*T* graphene integer plateaus sit on the same gap-versus-*kT* clause; packaging that would make this home-scale does not exist yet.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** High field magnets and cryogens are institutional hazards. This file is a mapping, not a magnet procedure. Do not close *R<sub>K</sub>* or \(2e^2/h\) with a Chern / Landauer derivation story.

---

## 1. Claim

Integer QHE hardware is a 2DEG + perpendicular *B* that opens a bulk gap + an edge path. In-plane *B* is a **non-occurrence** of that artifact, not a small correction. A ballistic 1D constriction at *B* = 0 shows \(2e^2/h\) steps and is a different machine (`predicted:edge-channel:qpc-is-not-this-edge`, `predicted:quantum-point-contact:steps-survive-at-zero-b`).

The cyclotron line on the same wafer shares *ω<sub>c</sub>* = *eB/m* and is not the plateau (`predicted:cyclotron-resonance:same-omega-c-not-a-plateau`). *R<sub>Q</sub>* as a tunnel floor is not *R<sub>K</sub>* (`predicted:coulomb-blockade:rq-is-not-rk`).

| Configuration | Output | Machine |
|---|---|---|
| 2DEG, *B* ⊥, *ν* in a gap | *R<sub>H</sub>* = *R<sub>K</sub>/ν*, *R<sub>xx</sub>* → 0 | `edge-channel` |
| Same bar, *B* in-plane | Plateau gone | Inhibit (this file) |
| Split-gate QPC, *B* = 0 | \(n\times 2e^2/h\) steps | `landauer-channel` |
| Microwave on, *ω* = *ω<sub>c</sub>* | *m\** absorption line | Cyclotron; not the plateau |

*R<sub>K</sub>* stays taken (`underived-hall-quantum`). This file does not use the plateau as an ohm.

---

## 2. Theory of operation

**On.** Perpendicular *B* opens the Landau / mobility gap. Current lives on the edge. *kT* and Hall field stay below the gap.

**Inhibit.** Rotate *B* in-plane, or walk *ν* off a plateau, or overrun the gap with *T* or current, or destroy the 2DEG. The lock disappears.

**Do not convert.** Pinching the same 2DEG into a short constriction without *B* is not “the plateau at zero field.” It is `landauer-channel`. Gating an island until *E<sub>c</sub>* > *kT* is `energy-gate` (charging), not *R<sub>K</sub>*.

---

## 3. Knobs

| Parameter | Toward a clean inhibit | Category error |
|---|---|---|
| *B* orientation | Perpendicular (on) vs in-plane (off) | Demanding *B* to open QPC steps |
| Filling *ν* | Sit in a gap, then walk off | Calling off-plateau “the ohm drifted” |
| *T*, current | Stay below the Landau/mobility gap | Graphene high-*T* plateaus as a second family |
| Constriction gate | Contrast column at *B* = 0 | Filing those steps as *R<sub>K</sub>/ν* |
| Microwave *ω* | Optional CR column | Walking off *ω<sub>c</sub>* and expecting *R<sub>H</sub>* to move |

---

## 4. Isolation sequence

0. 2DEG density / mobility check — buffer present.  
1. *B* ⊥, integer *ν* — plateau + *R<sub>xx</sub>* → 0.  
2. Rotate to in-plane *B* at similar |*B*| — plateau gone.  
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
