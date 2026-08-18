---
origin: application
device: ferroelectric film used on the failure side — Pr dies thinner than the depolarization envelope
updated: 2026-08-17
envelope: ceramic / thin-film lab; no deuterium
---

# Application: Depolarization fuse

**Device.** A ferroelectric film or grain (BaTiO₃ / PZT class) read for the **loss** of usable remnant *P* when the film is thinner than its depolarization / dead-layer envelope, while *T* is still below *T<sub>C</sub>*. Not a memory product.
**QSA machines.** `polar-latch` on the failure side (`predicted:ferroelectric-remanence:depolarization-kills-thin-pr`). Contrast: [polar-beam-gate](polar-beam-gate.md) (same engine, nuclear gate stacked on); FeRAM as the used 0 W memory.
**Status.** Working application of the mesoscale polar gap as a one-way thinness witness. **Not a FeRAM spec.**
**Envelope.** Ceramic / thin-film lab. No D₂. Closer to later packaging than the accelerator files.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** High *E* on thin dielectrics; leaded PZT is a materials-handling problem in a shop that already controls lead. This file is a mapping, not a fuse datasheet. No deuterium and no neutron channel.

---

## 1. Claim

The polar latch needs a volume that can stand the depolarization field. Below that envelope the well is emptied even though the polar phase is still named and *T* < *T<sub>C</sub>*. That is the electrical twin of superparamagnetic *KV* collapse, **without** a portable ferroelectric *KV* number yet (`polar-depolarization-buffer` stays open).

| State | *T* | Thickness / volume | Usable *P<sub>r</sub>* |
|---|---|---|---|
| Written latch | < *T<sub>C</sub>* | Above the depolarization envelope | Yes, 0 W at *E* = 0 |
| This fuse (tripped) | < *T<sub>C</sub>* | Thinner than the envelope | No |
| Thermal erase | > *T<sub>C</sub>* | Any | No |
| Linear dielectric | n/a | Any | Never remanent |

Used FeRAM lives on the first row. This file lives on the second. Do not quote ~30 nm NdFeB as the ferroelectric number.

---

## 2. Theory of operation

**Write.** *E* > *E<sub>c</sub>* on a thick-enough polar volume. Hold at *E* = 0, 0 W.

**Trip by thinness.** Dead layer / depolarization field empties the well. *T* may still be below *T<sub>C</sub>*. *E<sub>c</sub>* itself stays mesoscale (`polar-depolarization-buffer`).

**Trip by heat.** *T* > *T<sub>C</sub>* (BaTiO₃ ≈ 393 K class; PZT composition-dependent). That is the ordinary polar thermal cliff, not this fuse. Piezoelectric coupling on the same crystal dies with the polar phase; quartz (no remanence) is a different machine.

**Not a nuclear gate.** No D. A pyroelectric Δ*T* on a *thick* crystal is the field engine of [polar-beam-gate](polar-beam-gate.md). This file does not open D–D.

---

## 3. Knobs

| Parameter | Toward isolating the fuse | Category error |
|---|---|---|
| Thickness | Walk a series through the dead-layer / depolarization class | Using 30 nm NdFeB as the number |
| *T* | Hold < *T<sub>C</sub>* while thinning | Only a *T<sub>C</sub>* bake (that is thermal erase of any thickness) |
| *E<sub>c</sub>* write | Enough to pole the thick controls | Treating *E<sub>c</sub>* as a derived node number |
| Electrodes / dead layer | Record as process; it *is* the mesoscale gap | “The polar phase is named, so *P<sub>r</sub>* must remain” |
| D inventory | **Off** | Stacking a beam-target gate on this coupon |

---

## 4. Isolation sequence

0. Thick ceramic / film, *T* < *T<sub>C</sub>* — remnant *P* at *E* = 0.  
1. Thickness series, same chemistry and *T* — *P<sub>r</sub>* dies while the polar phase is still named.  
2. Thick control through *T<sub>C</sub>* — thermal erase; *P<sub>r</sub>* gone at any thickness.  
3. Same thick crystal, piezo *d<sub>ij</sub>* vs *T<sub>C</sub>* — strain channel dies with the polar phase (library supporting).  
4. No D, no neutron channel. If a burst appears, the wrong file is in use.

---

## 5. Falsifiers

- Usable *P<sub>r</sub>* in a film thinner than its depolarization envelope at *T* < *T<sub>C</sub>*.  
- Pyroelectric voltage that survives *T* > *T<sub>C</sub>*.  
- A portable *KV* number imported from NdFeB.  
- Neutrons (that is [polar-beam-gate](polar-beam-gate.md), and it is out of this coupon).

---

## 6. What this file is not

- Not FeRAM.  
- Not a PIR sensor or pyroelectric X-ray tube (used products).  
- Not [polar-beam-gate](polar-beam-gate.md).  
- Not [bonded-magnets](bonded-magnets.md); kinship is the latch *kind*, not the number.

## 7. Links

- [ferroelectric-remanence](../library/ferroelectric-remanence.md) — library source  
- [polar-beam-gate](polar-beam-gate.md) — same engine, nuclear gate stacked on  
- [bonded-magnets](bonded-magnets.md) — magnetic twin (different number)  
