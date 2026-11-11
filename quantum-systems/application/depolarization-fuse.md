---
origin: application
device: thin ferroelectric capacitor read for loss of net polarization when its surface charge is poorly screened
updated: 2026-11-14
envelope: ceramic / thin-film lab; no deuterium
---

# Application: Depolarization fuse (screening witness)

**Device.** A thin ferroelectric film (BaTiO₃ / PbTiO₃ / PZT class) between electrodes, read for the **loss of net remanent polarization** while *T* is still below *T<sub>C</sub>*. Not a memory product.
**QSA machines.** `polar-latch` on the failure side. Contrast: [polar-beam-gate](polar-beam-gate.md) (same engine, nuclear gate stacked on); FeRAM as the used 0 W memory.
**Status.** A use of a measured thin-film effect. **Not a FeRAM spec.**
**Envelope.** Ceramic / thin-film lab. No D₂.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** High *E* on thin dielectrics; leaded PZT is a materials-handling problem in a shop that already controls lead. This file is a mapping, not a fuse datasheet. No deuterium and no neutron channel.

> **Corrected 2026-11-14**, after the sourcing of [ferroelectric-remanence](../library/ferroelectric-remanence.md) and [ferroelectric-domains](../library/ferroelectric-domains.md). The first version said the polar latch needs a volume that can stand the depolarization field, that below a thickness "envelope" the well is emptied, and that this is the electrical twin of superparamagnetic *KV* collapse. The sources give no such volume limit and no thermal-activation size criterion. The polar phase is stable in PbTiO₃ films of 3 unit cells (1.2 nm), polarization is reduced but present at 2.4 nm, and crystals of about 5 nm still switch. What a thin film loses is its **net** polarization, by two routes that depend on the boundary and not on the volume: with no free charge it forms stripe domains, and with imperfect electrodes it relaxes when the residual depolarizing field reaches the coercive field. The row `predicted:ferroelectric-remanence:depolarization-kills-thin-pr` is marked established, so it is a measured fact and no longer a prediction. The device is kept and restated as a witness of screening. The magnetic comparison is withdrawn on both sides: the magnetic limit is itself a retention-time crossover and is not what limits a real magnet.

---

## 1. Claim

A slab polarized along its normal carries bound surface charge, and unless that charge is compensated its own field opposes the polarization. For BaTiO₃ (*P* = 0.263 C/m²) the uncompensated field would be 3.0 × 10¹⁰ V/m; the thin-film coercive field is 3–4 × 10⁷ V/m, 0.10–0.13 % of it. Compensation therefore has to be complete to about one part in a thousand before the residual field is below the write field. Numbers and sources: [ferroelectric-remanence](../library/ferroelectric-remanence.md) §4.3.

| State | *T* | Boundary | Net *P<sub>r</sub>* |
|---|---|---|---|
| Written latch | < *T<sub>C</sub>* | Electrodes that screen well | Yes, 0 W at *E* = 0 |
| This device (tripped) | < *T<sub>C</sub>* | Residual depolarizing field at or above *E<sub>c</sub>* | Relaxes; measured over 10–500 µs in 5–30 nm BaTiO₃ capacitors |
| No free charge at all | < *T<sub>C</sub>* | Insulating substrate | Zero net: 180° stripe domains, measured in 1.2–42 nm PbTiO₃ films. The polar phase is present |
| Thermal erase | > *T<sub>C</sub>* | Any | No |
| Linear dielectric | n/a | Any | Never remanent |

Used FeRAM lives on the first row. This file lives on the second. Thickness enters through the electrode: the same imperfect screening leaves a larger residual field in a thinner film, so the loss is gradual in thickness (tetragonality falls below about 20 nm in PbTiO₃) and has no critical value in the measurements. A calculated critical thickness exists (about six unit cells, 2.4 nm, for BaTiO₃ between SrRuO₃ electrodes; 2–7 cells for PbTiO₃); it is a zero-temperature model result for one electrode.

---

## 2. Theory of operation

**Write.** *E* > *E<sub>c</sub>* on a film with screening electrodes. Hold at *E* = 0, 0 W. *E<sub>c</sub>* is taken from loops and rises as the film thins (*E<sub>c</sub>* ∝ *d*<sup>−2/3</sup> from 100 µm down to 200 nm).

**Trip by poor screening.** In SrRuO₃ / BaTiO₃ / SrRuO₃ capacitors of 5–30 nm the depolarizing field is comparable to or larger than the coercive field and agrees with an electrostatic calculation from the electrode's screening length (0.8 ± 0.1 Å). The net polarization then relaxes, with a large change between 10 and 500 µs. For a 15 nm film with noble-metal electrodes 500–900 kV/cm is expected. The authors conclude that this relaxation limits capacitor devices before any critical thickness does.

**Trip by heat.** *T* > *T<sub>C</sub>* (BaTiO₃ 393 K; PZT grades 468–638 K). That is the ordinary Curie threshold and is not this device. Piezoelectric coupling of a poled ceramic ends there too, and can be lost well below it by depoling ([piezoelectricity](../library/piezoelectricity.md)).

**Not a nuclear gate.** No D. A pyroelectric Δ*T* on a thick crystal is the field engine of [polar-beam-gate](polar-beam-gate.md).

---

## 3. Knobs

| Parameter | Toward isolating the effect | Category error |
|---|---|---|
| Electrode material | Compare a good screener with a poor one at fixed film thickness | Treating the loss as a property of the film volume |
| Thickness | A series at fixed electrode; expect a gradual change | Expecting a critical thickness, or importing a magnetic size |
| Time after poling | Read retention from microseconds upward | A single late reading |
| *T* | Hold < *T<sub>C</sub>* | Only a *T<sub>C</sub>* bake (thermal erase at any thickness) |
| Substrate | Conducting. On an insulating substrate the film forms stripes and never holds net *P* | Reading zero net *P* as loss of the polar phase |
| D inventory | **Off** | Stacking a beam-target gate on this coupon |

---

## 4. Isolation sequence

0. Thick ceramic or film, *T* < *T<sub>C</sub>*: remnant *P* at *E* = 0.  
1. Thin film, two electrode materials, same thickness and *T*: retention against time after poling. This is the device.  
2. Thickness series at fixed electrode: gradual loss of net *P*; check by diffraction that the polar phase is still present.  
3. Thick control through *T<sub>C</sub>*: thermal erase.  
4. No D, no neutron channel.

---

## 5. Falsifiers

Steps 1 and 2 repeat published measurements, so their expected outcomes do not test the mapping against standard ferroelectric physics. What would contradict the restated device:

- Retention that does not depend on the electrode at fixed thickness.  
- A film on an insulating substrate that holds net *P<sub>r</sub>* with no stripe domains.  
- A sharp critical thickness in net *P<sub>r</sub>* that does not move with the electrode (this would restore the first version's envelope).  

Removed: “pyroelectric voltage that survives *T* > *T<sub>C</sub>*” (the Curie threshold is established) and “a portable *KV* number imported from NdFeB” (a category rule, not a measurement).

---

## 6. What this file is not

- Not FeRAM.  
- Not a PIR sensor or pyroelectric X-ray tube (used products).  
- Not [polar-beam-gate](polar-beam-gate.md).  
- Not a twin of [bonded-magnets](bonded-magnets.md). The magnetic small-grain limit is thermal activation over *KV*; the polar thin-film limit is an uncompensated field. The mechanisms differ and neither is a sharp size.

## 7. Links

- [ferroelectric-remanence](../library/ferroelectric-remanence.md) — library source  
- [ferroelectric-domains](../library/ferroelectric-domains.md) — stripe domains, wall widths  
- [polar-beam-gate](polar-beam-gate.md) — same engine, nuclear gate stacked on  
- [bonded-magnets](bonded-magnets.md) — the magnetic latch, for contrast  
