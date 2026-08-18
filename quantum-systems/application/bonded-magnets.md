---
origin: application
device: bonded NdFeB part, magnetic recording medium, ferrofluid
updated: 2026-08-17
---

# Application: Bonded magnets, tape, and ferrofluid

**Device.** A polymer-bonded NdFeB magnet, a particulate recording layer, or a ferrofluid.
**QSA machines.** `anisotropy-latch` (core); `superparamagnetism` (volume cliff); `shape-anisotropy`; `exchange-pin` (some stacked media); `ensemble-average` (the unlocked fluid).
**Status.** Working application. **Calibration.** The cliff is in the handbook. **Not a tested process spec.**

If this file’s isolation sequence does not recover “NdFeB blocks near ~30 nm at room temperature / lab time; magnetite smaller; a ferrofluid has *no* remanence on purpose,” stop using the latch mapping on EM-LENR powder.

---

## 1. Claim

The device is a population of latch cells. The part’s *envelope* is capacity (how much moment you can pack). The **cliff** is grain / particle volume versus *kT* ln(*τ*/τ₀).

| Device | Which side of the line you want |
|---|---|
| Bonded / sintered magnet | **Blocked.** *KV* ≳ 25–60 *kT* on the service life. |
| Recording bit | **Blocked** on the archive time; writable on the head’s field and time. |
| Ferrofluid | **Unblocked.** Zero remanence, Langevin *M*(*H*). Superparamagnetism is the spec, not a failure. |

25 *kT* is a **timescale contour**, not a universal energy. Tape vs geological magnetite vs a 1-second ferrofluid measurement are different contours of the same machine.

---

## 2. Theory of operation

Write: applied *H* above the mesoscale *H*<sub>c</sub> (not *H*<sub>a</sub>).  
Hold: 0 W.  
Erase: reverse *H*, *T* > *T*<sub>C</sub>, shock, or shrink *V* until the blocking line is crossed.

Shape-anisotropy needles can latch without large *K₁*. Spheres of the same *K₁* may not.

---

## 3. Knobs

| Parameter | Toward a hard magnet | Toward a ferrofluid | Collapse of a hard magnet |
|---|---|---|---|
| Particle size | **Up** through ~30 nm (NdFeB) / keep well above the contour | **Down** through the contour | Fines in a “hard” mix |
| *K* | High-*K* phase (Nd₂Fe₁₄B), aligned | Low *K* or small *V* | Soft ferrite fill |
| *T* | Stay well below *T*<sub>C</sub> and below *T*<sub>B</sub>(*V*) | Ambient is fine if *V* is small | Bake toward *T*<sub>C</sub> |
| Aspect ratio | Needles / flakes if *K₁* is modest | Spheres | Spheroidize a shape-anisotropy grade |
| Time | Spec life (years) sets the *kT* multiplier | Measurement window ~seconds | Expect remanence on a VSM and none in a motor a year later if you sat on the contour |

---

## 4. Isolation / calibration sequence

1. Size series of the same chemistry: remanence and *H*<sub>c</sub> vs *d*. Recover a drop at the predicted class (NdFeB tens of nm; Fe₃O₄ smaller).  
2. Same size, two wait times (1 s vs 10³ s): the contour should move.  
3. Sphere vs needle at fixed volume.  
4. Ferrofluid: *M*(*H*) reversible, *H*<sub>c</sub> ≈ 0. That is success of the *other* side.  
5. Stacked AFM/FM (if present): *T<sub>B</sub>* < *T* < *T<sub>C</sub>*(FM) ⇒ *H*<sub>ex</sub> gone, *M<sub>r</sub>* can remain (`predicted:exchange-bias:hex-gone-above-tb-while-fm-latched`). No AFM ⇒ unshifted loop. A superparamagnetic FM grain cannot hold the shift. The history-bit reading of that split is [exchange-pin-thermal-history](exchange-pin-thermal-history.md).

If (1) is a smooth “smaller is weaker” with no class cliff, the *KV* mapping is not doing work.

---

## 5. Falsifiers

- Room-temperature, hour-scale remanence in well-dispersed 8 nm magnetite.  
- No remanence in aligned 100 nm Nd₂Fe₁₄B at room temperature (unless chemically decomposed).  
- *H*<sub>c</sub> = *H*<sub>a</sub> on a real sintered part (the mesoscale gap would have closed in a way the library does not claim).

---

## 6. Link to EM-CSAM

You can spray magnetic powder. Whether the deposit is a **magnet** or a **ferrofluid-like sludge** is this application: grain size after impact, alignment in the pulse *B*, and whether the splat still has *KV*. A coil around the barrel is a write-field during flight. See [EM-CSAM](EM-CSAM.md).
