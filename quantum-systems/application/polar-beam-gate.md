---
origin: application
device: pyroelectric polar crystal as a transient HV engine opening beam-target D–D
updated: 2026-08-17
envelope: institutional until a packaged, interlocked, low-inventory unit exists
---

# Application: Polar-field beam-target burst

**Device.** A pyroelectric crystal (LiTaO₃ class) that, on a thermal ramp in deuterium, writes a transient tens-of-kV face and opens ordinary beam-target D–D. Witness is a 2.45 MeV neutron burst per ramp.
**QSA machines.** `polar-latch` (field engine); `energy-gate` (beam-target D–D). Contrast: `muon-catalyzed-fusion`; the coil hydride in [EM-LENR](EM-LENR.md).
**Status.** Working application of a *stacked-gate* isolation, not a used DT tube or ²⁵²Cf source. **Not a generator protocol.**
**Envelope.** Institutional / industrial until interlocked low-inventory packaging exists. Home-scale waits on that mitigation.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** High voltage on an isolated face, D₂, and a neutron channel in one cell. Dielectric breakdown and leakage are ordinary industrial hazards. This file is a mapping, not a procedure. Do not scale crystal size, Δ*T*, or D inventory in search of a nuclear signature. Do not skip isolation to “see neutrons.”

---

## 1. Claim

Two gates in series, two machines:

| Layer | Machine | What it is |
|---|---|---|
| Field engine | `polar-latch` | Pyroelectric Δ*P* on an isolated face writes a potential. Dies at host *T*<sub>C</sub> (`predicted:pyroelectric-fusion:dies-above-host-tc`). Remanent *P* at *E* = 0 is the supporting resource, not the nuclear output. |
| Nuclear conversion | `energy-gate` | Ordinary beam-target D–D once ions sit in the tens-of-keV window. No muon. *N* small. Product leaves. |

This is **not** [muon-catalyzed fusion](../library/muon-catalyzed-fusion.md). Pyroelectric neutrons, when they exist, track a thermal ramp, not *τ<sub>μ</sub>* (`predicted:pyroelectric-fusion:muon-free-still-not-mucf`). A muon-free hydride coil is **neither** machine.

Used neutron sources (sealed DT tubes, ²⁵²Cf) are out of scope. The QSA object is the stacked-gate split.

---

## 2. Theory of operation

**Write of the field.** Ramp *T* (seconds-class). Bound charge Δ*P* = *γ<sub>p</sub>* Δ*T* builds *V* until ionization, leakage, or breakdown limits it.

**Open the nuclear gate.** D ions in the tens-of-keV window see the ordinary D–D Coulomb barrier. Below that potential the cross section collapses. No D ⇒ no D–D neutrons.

**Erase of the engine.** *T* → *T*<sub>C</sub> of the host (LiTaO₃ ~890 K class; ordinary ramps stay far below). Leakage or breakdown dumps the face. Removing D closes the nuclear gate without touching the polar latch.

**Hold.** There is no 0 W remnant fusion cycle. After the ramp the burst is over. That is the opposite of a latched interstitial cell.

---

## 3. Knobs

| Parameter | Toward isolating the stack | Collapse / confound |
|---|---|---|
| Δ*T* | Tens of K on a mm-class crystal, enough for the ~100 kV *class* | Tiny ramp; or a ramp that only leaks |
| D inventory | Present as gas and/or deuterated target | No D: field engine may still write *V*, nuclear gate stays shut |
| Host *T* vs *T*<sub>C</sub> | Stay well below *T*<sub>C</sub> | Through *T*<sub>C</sub>: engine gone even with D |
| Leakage / breakdown | Dry, isolated face | `dielectric-breakdown` eats the potential (different gate: it *destroys* the insulator) |
| Clock | Seconds ramp, then prompt fusion | Looking for a *τ<sub>μ</sub>* = 2.197 μs die-off is the wrong machine |
| Muon source | **Off.** None | Adding muons files a different gate ([muon-hydrogen-gate](muon-hydrogen-gate.md)) |

Yield per cycle is a wide class (~10³–10⁵ in the handbook demo). Treat it as a class, not a constant. Do not tune for it.

---

## 4. Isolation sequence

0. Crystal, no D, ramp — measure face potential / ionization. Field engine only.  
1. Same ramp + D — 2.45 MeV line vs no-D.  
2. Same crystal + D, hold *T* static (no Δ*T*) — should be null.  
3. Host through *T*<sub>C</sub> (or a lower-*T<sub>C</sub>* polar substitute) + D — burst should die (`predicted:pyroelectric-fusion:dies-above-host-tc`).  
4. Time structure: burst on the ramp, not on a 2.2 μs muon clock.  
5. Contrast cell: muon-free Pd–D / Ni–H coil with **no** polar crystal ([EM-LENR](EM-LENR.md)) must not reproduce this cycle.

---

## 5. Falsifiers

- Burst after *T* > host *T*<sub>C</sub> with D still present.  
- Burst that tracks *τ<sub>μ</sub>* or α-sticking.  
- Yield from a pulsed-coil hydride with no polar crystal.  
- A remnant neutron rate at 0 W after the ramp is dark (that would be a latch, not this gate).

A nuclear-null on a well-isolated engine (potential present, D present, *T* < *T*<sub>C</sub>) is a closed beam-target gate in this geometry, not a failed polar latch.

---

## 6. What this file is not

- Not a DT tube or radioisotope source.  
- Not [muon-hydrogen-gate](muon-hydrogen-gate.md).  
- Not [EM-LENR](EM-LENR.md). Do not add this crystal to the coil cell to “open” it.  
- Not FeRAM or a PIR sensor ([depolarization-fuse](depolarization-fuse.md) owns the polar *failure* side with no D).  
- Not a net-energy claim.

## 7. Links

- [pyroelectric-fusion](../library/pyroelectric-fusion.md) — library source  
- [ferroelectric-remanence](../library/ferroelectric-remanence.md) — polar engine  
- [muon-hydrogen-gate](muon-hydrogen-gate.md) — the other uncommon H-isotope gate  
- [EM-LENR](EM-LENR.md) — muon-free, pyro-free coil cell  
