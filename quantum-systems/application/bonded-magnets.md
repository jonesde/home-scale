---
origin: application
device: bonded NdFeB part, magnetic recording medium, ferrofluid
updated: 2026-11-11
---

# Application: Bonded magnets, tape, and ferrofluid

**Device.** A polymer-bonded NdFeB magnet, a particulate recording layer, or a ferrofluid.
**QSA machines.** `anisotropy-latch` (core); [superparamagnetism](../library/superparamagnetism.md) (the retention-time crossover); [shape-anisotropy](../library/shape-anisotropy.md); `exchange-pin` (some stacked media); `ensemble-average` (the unlocked fluid).
**Status.** Working application. **Calibration** against sourced sizes. **Not a tested process spec.**

If this file’s isolation sequence does not recover “magnetite blocks near 20–50 nm at room temperature on laboratory time; Nd₂Fe₁₄B far smaller, a few nanometres; a ferrofluid has *no* remanence on purpose,” stop using the latch mapping on EM-LENR powder.

The first version of this file had the calibration target wrong: it put NdFeB near ~30 nm and magnetite below it. The library's own volume (2.3×10⁻²⁶ m³) is a 3.5 nm sphere, and magnetite, with about 340 times less anisotropy, blocks at a larger size. Numbers and sources are in [superparamagnetism](../library/superparamagnetism.md). A correct experiment would have failed the old gate.

> **Re-checked 2026-11-11** against [superparamagnetism](../library/superparamagnetism.md), [permanent-magnet-latch](../library/permanent-magnet-latch.md), [magnetic-domains](../library/magnetic-domains.md), [ferromagnetic-hysteresis](../library/ferromagnetic-hysteresis.md) and [shape-anisotropy](../library/shape-anisotropy.md). The sizes stand. Changes: the volume limit is called a crossover throughout and is stated as not being what limits a bonded or sintered magnet (coercivity, temperature and shock are); the *kT* multipliers are given with their conventions; a hard-ferrite size is added; the ferrofluid row notes that a suspension also loses remanence by particle rotation; §6 asks about coercivity and shock after impact in place of *KV*.

---

## 1. Claim

The device is a population of latch cells. The part’s *envelope* is capacity (how much moment you can pack). Thermal stability of one grain is a **crossover**: the retention time is τ₀ exp(*KV*/*kT*), steep in size and with no critical value. It decides between a magnet and a ferrofluid only for grains of a few nanometres (Nd₂Fe₁₄B), 8 nm (hard ferrite) or 20–50 nm (magnetite). Bonded and sintered magnets use grains far above it. Their working limits are coercivity, which is a microstructure property and under a fifth of the anisotropy field in real Nd-Fe-B, the Curie point (585 K), and shock ([permanent-magnet-latch](../library/permanent-magnet-latch.md)).

| Device | Which side of the line you want |
|---|---|
| Bonded / sintered magnet | **Blocked**, by a wide margin: a 30 nm Nd₂Fe₁₄B cube has *KV* of about 29 000 *kT*. |
| Recording bit | **Blocked** on the archive time: decay sets in near 35 *kT* and about 60 *kT* is required for ten-year storage. Writable on the head’s field and time. |
| Ferrofluid | **Unblocked**, or free to rotate. Zero remanence, Langevin *M*(*H*). In a fluid the whole particle can also turn (Brownian relaxation), so a suspension loses remanence even when the grain itself is blocked. |

25 *kT* is the convention for a 100 s measurement with an attempt time of 10⁻⁹ s; ten years with the same attempt time is 40 *kT*, which needs only 17 % more diameter. Tape, geological magnetite and a 1-second ferrofluid measurement are different contours of the same relation. Hard ferrite at 25 *kT* and 300 K is an 8.2–8.5 nm sphere (computed here from *K*<sub>1</sub> = 0.32–0.36 MJ/m³ in [shape-anisotropy](../library/shape-anisotropy.md), with the formula of [superparamagnetism](../library/superparamagnetism.md) §4.3).

---

## 2. Theory of operation

Write: applied *H* above the mesoscale *H*<sub>c</sub> (not *H*<sub>a</sub>).  
Hold: 0 W.  
Erase: reverse *H*; *T* > *T*<sub>C</sub>; shock (sintered Nd-Fe-B is demagnetized at 6–7 GPa by fracture between grains, recoverable by annealing, and at 22 GPa); hydrogen decrepitation; or a grain so small that its retention time is shorter than the service time.

Shape-anisotropy needles can hold a direction without large *K₁*, but only as a semi-hard latch: an iron needle reaches at most 0.92 MJ/m³ and real elongated particles reverse at 15–19 % of the ideal field ([shape-anisotropy](../library/shape-anisotropy.md)). Spheres get nothing from shape, and half the needle limit is already reached at an aspect ratio near 2.

---

## 3. Knobs

| Parameter | Toward a hard magnet | Toward a ferrofluid | Collapse of a hard magnet |
|---|---|---|---|
| Particle size | Keep above the contour: a few nm for Nd₂Fe₁₄B, 20–50 nm for magnetite. Real NdFeB powders are far above it; their limit is coercivity, not *KV* | **Down** through the contour | Fines in a low-*K* mix |
| *K* | High-*K* phase (Nd₂Fe₁₄B), aligned | Low *K* or small *V* | Soft ferrite fill |
| *T* | Stay well below *T*<sub>C</sub> (coercivity falls continuously well before it) | Ambient is fine if *V* is small | Bake toward *T*<sub>C</sub> |
| Aspect ratio | Needles / flakes if *K₁* is modest | Spheres | Spheroidize a shape-anisotropy grade |
| Time | Spec life (years) sets the *kT* multiplier | Measurement window ~seconds | Expect remanence on a VSM and none in a motor a year later if you sat on the contour |

---

## 4. Isolation / calibration sequence

1. Size series of the same chemistry: remanence and *H*<sub>c</sub> vs *d*. Recover the fall-off at the predicted class (Fe₃O₄ 20–50 nm; Nd₂Fe₁₄B a few nm, which is hard to reach without destroying the phase). Expect a steep but continuous curve, not a step.  
2. Same size, two wait times (1 s vs 10³ s): the contour should move.  
3. Sphere vs needle at fixed volume.  
4. Ferrofluid: *M*(*H*) reversible, *H*<sub>c</sub> ≈ 0. That is success of the *other* side.  
5. Stacked AFM/FM (if present): *T<sub>B</sub>* < *T* < *T<sub>C</sub>*(FM) ⇒ *H*<sub>ex</sub> gone, *M<sub>r</sub>* can remain (`exchange-bias:failure_mode:blocking`). No AFM ⇒ unshifted loop. Both are established facts. The earlier third clause, that a superparamagnetic FM grain cannot hold the shift, is contradicted: a CoO pin keeps 4 nm Co grains blocked to 220–290 K ([exchange-bias](../library/exchange-bias.md)). The history-bit reading of that split is [exchange-pin-thermal-history](exchange-pin-thermal-history.md).

The Néel–Arrhenius form predicts a steep exponential in *d*³, not a step: about a factor of four thousand in retention time for 10 % in diameter. If (1) shows no such steepness and no shift with wait time in (2), the *KV* mapping is not doing work. The Néel–Brown form is itself measured on single particles, so this sequence recovers a known result; it calibrates a bench and does not test the mapping against standard magnetism.

---

## 5. Falsifiers

- Room-temperature, hour-scale remanence in well-dispersed, uncoupled 8 nm magnetite (measured 4–5 nm magnetite blocks near 45 K).  
- No remanence in aligned 100 nm Nd₂Fe₁₄B at room temperature (unless chemically decomposed).  
- *H*<sub>c</sub> = *H*<sub>a</sub> on a real sintered part (the mesoscale gap would have closed in a way the library does not claim).

---

## 6. Link to EM-CSAM

You can spray magnetic powder. Whether the deposit is a **magnet** is decided by what impact does to coercivity, and by alignment in the pulse *B*. The thermal-stability size plays no part: no impact makes 3.5 nm grains. The sourced risk is shock demagnetization (6–7 GPa in sintered Nd-Fe-B); the impact pressure at this head’s velocities is not sourced, so remanence and coercivity against impact velocity is the first measurement. Hard-magnet grains are brittle and need a binder that deforms; cold-sprayed NdFeB with an aluminum binder is published (reference in [EM-CSAM-Pitch](EM-CSAM-Pitch.md), idea D). A coil around the barrel is a write field during flight. See [EM-CSAM](EM-CSAM.md) §3.6.
