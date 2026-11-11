---
origin: application
device: AFM/FM bilayer coupon whose loop shift records a trip through TB
updated: 2026-11-11
envelope: thin-film lab; conceivable later as a sealed coupon
---

# Application: Exchange-pin thermal-history bit

**Device.** An AFM/FM bilayer (or stack) field-cooled through the pin’s blocking temperature so that a loop shift *H*<sub>ex</sub> is written. The useful output is not a used spin-valve signal. It is the **split**: after a thermal trip *T<sub>B</sub>* < *T* < *T<sub>C</sub>*(FM), *H*<sub>ex</sub> is gone and ordinary FM remanence can remain.
**QSA machines.** Draft `exchange-pin` (core); `anisotropy-latch` (the FM cell the pin writes on).
**Status.** Working application of a one-shot temperature-history witness, not an HDD read head or MRAM bit. **Not a process spec.**
**Envelope.** Thin-film lab. A sealed coupon is closer to later home-scale packaging than the accelerator or reactor files.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** Thin-film deposition and field-cool magnets are ordinary lab hazards. This file is a mapping, not a thermal-fuse datasheet.

---

## 1. Claim

`exchange-pin` is a second latch. Collapse is *T<sub>B</sub>* of the AFM pin (*T<sub>B</sub>* ≤ *T<sub>N</sub>* of that layer), not the FM Curie point. Remove the AFM (or never deposit it) and the loop is unshifted. Both statements are measured facts, sourced in [exchange-bias](../library/exchange-bias.md); the two predicted rows that restated them are now marked established.

The third statement in the first version of this file was wrong. It said a superparamagnetic FM grain cannot hold a static *H*<sub>ex</sub> (`predicted:exchange-bias:no-hex-below-kv`). Measurements show the reverse dependence: a 4 nm Co grain that blocks near 6–10 K on its own anisotropy stays blocked to 220–290 K and carries a 367 mT shift once it is coupled to an effective CoO pin. The pin supplies the barrier. What kills the shift is a pin that is too thin (a 1.0 nm CoO shell gives none) or a temperature above the blocking temperature of the coupled grain.

*T<sub>B</sub>* is a crossover, not a sharp line: a real film has a distribution of blocking temperatures and *T<sub>B</sub>* rises with sweep rate. A history bit built on it reads "was above roughly *T<sub>B</sub>* for long enough," not "crossed exactly *T<sub>B</sub>*."

| After this history | *H*<sub>ex</sub> | FM *M<sub>r</sub>* |
|---|---|---|
| Field-cooled through *T<sub>B</sub>*, then *T* < *T<sub>B</sub>* | Held (0 W) | Held |
| Tripped through *T<sub>B</sub>*, still *T* < *T<sub>C</sub>*(FM) | Gone | Can remain |
| *T* > *T<sub>C</sub>*(FM) | Gone | Gone |
| No AFM layer | ≈ 0 | Ordinary FM latch |

That table is the device. A spin-valve / MRAM uses the same bilayer as a *used* product; this file does not.

---

## 2. Theory of operation

**Write.** Field-cool through *T<sub>B</sub>*. The pin sets a unidirectional barrier. Hold-power of the shift is 0 W.

**Read.** Loop shift vs a control coupon of the same FM without AFM (or with the pin destroyed).

**Trip.** A thermal excursion above *T<sub>B</sub>* erases the pin and leaves the parent latch. That is the history bit.

**Starve.** The pin, not the FM grain. Below a critical antiferromagnet thickness of a few nanometres (system-dependent; 6 nm in one IrMn study) the shift drops to zero. A small FM grain is not starved by its own *KV*: pinned, it is stabilized.

---

## 3. Knobs

| Parameter | Toward a readable history bit | Collapse |
|---|---|---|
| AFM grain / thickness | Sets *T<sub>B</sub>* class (*T<sub>B</sub>* ≤ *T<sub>N</sub>* of the layer) | Below a few nm: no pin, no shift |
| FM thickness | *H*<sub>ex</sub> ~ 1/*t*<sub>FM</sub>; thinner gives a larger shift | Too thick: shift diluted. Too thin to be continuous: the 1/*t* law fails |
| Spacer | None | The coupling decays exponentially through a metal spacer and is gone by about 50 Å |
| Field-cool | Through *T<sub>B</sub>* with a write field | Zero-field cool: weak or no shift |
| Trip *T* | A band *T<sub>B</sub>* < *T* < *T<sub>C</sub>*(FM) | Only a bake through FM *T<sub>C</sub>* (erases both layers) |
| Control coupon | Same FM, no AFM | No unshifted reference |

Do not quote NdFeB 585 K or BaTiO₃ 393 K as *T<sub>B</sub>*. The number is the pin’s, not a shared thermal-cliff figure.

---

## 4. Isolation sequence

0. FM-only coupon — centered loop.  
1. AFM/FM, field-cooled — *H*<sub>ex</sub> ≠ 0 at 0 W.  
2. Same stack, *T<sub>B</sub>* < *T* < *T<sub>C</sub>*(FM), cool back — *H*<sub>ex</sub> gone, *M<sub>r</sub>* can remain.  
3. AFM thickness series at fixed FM — shift drops to zero below a critical thickness of a few nm.  
4. Destroy or omit the AFM — unshifted loop.

---

## 5. Falsifiers

- *H*<sub>ex</sub> that dies at FM *T<sub>C</sub>* rather than at a lower *T<sub>B</sub>*.  
- Loop shift without an AFM pin.  
- A loop shift that survives above the blocking temperature of the coupled grain.  
- A shift with an antiferromagnet thinner than its critical thickness.  
- *H*<sub>ex</sub> that requires continuous current to hold (that is not this latch).

---

## 6. What this file is not

- Not an HDD read head or MRAM product.  
- Not [bonded-magnets](bonded-magnets.md) (parent latch calibration). This file owns the *split*.  
- Not a Curie-temperature crayon. *T<sub>B</sub>* ≠ *T<sub>C</sub>*.

## 7. Links

- [exchange-bias](../library/exchange-bias.md) — library source  
- [bonded-magnets](bonded-magnets.md) — FM *KV* calibration  
- [permanent-magnet-latch](../library/permanent-magnet-latch.md) — parent latch  
