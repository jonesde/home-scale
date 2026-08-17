---
origin: application
device: EM-CSAM micro-railgun deposition head, driver, and the same barrel/coil as a lab
updated: 2026-08-17
---

# Application: EM-CSAM head (manufacture + experiment)

**Device.** A short-barrel parallel-rail micro-accelerator that throws a metered metal-powder armature (usually in a carrier) at 200–800 m/s class onto a substrate, plus the capacitor-discharge driver that feeds it. Hardware home: [`../../em-csam/`](../../em-csam/README.md).
**QSA machines.** `oscillator-grid` (impact, yield, melt); `collective-screening` (skin in rails and armature); `energy-gate` as `dielectric-breakdown` (plasma on/off); `anisotropy-latch` + `magnetostriction` when the powder is ferromagnetic; interstitial latch only if H/D is in the system ([EM-LENR](EM-LENR.md), [hydrogen-embrittlement](hydrogen-embrittlement.md), [hydride-storage](hydride-storage.md)).
**Status.** Working application of *this* repository’s hardware. Manufacturing first. The same setup is a pulsed high-strain, high-*dB/dt* experiment. **Not a tested protocol.**
**Credit.** EM-CSAM is the author’s project. QSA here is analysis of that device, not a redesign of the barrel.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** Capacitor discharge, rail–armature current, flying metal, and carrier vapor can maim without any “interesting physics.” Hydrogen-rich carriers on steel or Ti can charge a part that cracks later. Machining BeCu is a beryllium-control problem; stay on copper if you do not already have that shop. These notes are not a build sequence or a pressure rating. Do not scale the barrel or bank in search of a nuclear signature.

Derived specs: [design-spec-sheets](../library/derived/design-spec-sheets.md), [requirement-audit](../library/derived/requirement-audit.md). Concept numbers (*L*′, *F* = ½ *L*′ *I*², ~100 mm barrel) follow the technical note, not new measurements.

Concepts repeat on purpose. The library remains the singular source.

---

## 1. What the device is, in QSA terms

A shot is a **write** on several machines at once:

| During the pulse | Machine | What is being written or erased |
|---|---|---|
| Current in rails and armature | `collective-screening` (skin) | Current lives in a skin δ(*ω*). A “solid” rail is electrically thin or thick depending on pulse width. |
| Contact gap, slurry voids, rail–armature interface | `dielectric-breakdown` | Plasma armature vs solid/compact armature. Process lever **and** confound. |
| Lorentz body force, impact, plastic strain | `oscillator-grid` | Yield vs melt vs fracture. Bonding is a yield/oxide-rupture event, not a *T*<sub>m</sub> event if you stay “cold.” |
| *B* in a Ni/Fe particle | `magnetostriction` + latch | Strain locked to *M* if *B* exceeds alignment and *T* < *T*<sub>C</sub> and the grain is blocked. |
| H-rich carrier or residual moisture on steel/Ti | interstitial latch | Unwanted write of [embrittlement](hydrogen-embrittlement.md). |
| Impact of already-latched magnetic powder | `anisotropy-latch` | Shock can erase remanence (mechanical failure path). |

The manufacturing goal (coherent deposit, low substrate heat) and the experimental goal (isolate one of those writes) use the **same knobs**, turned for different verdicts.

---

## 2. Manufacturing theory of operation

### 2.1 Acceleration

*F* = ½ *L*′ *I*² with *L*′ ~ 0.5–0.6 µH/m for simple rails. Short barrel (~100 mm) ⇒ you buy velocity with *I*, not with length. The armature is a slurry slug whose mass, conductivity, and fill fraction are process variables, not nuisances.

### 2.2 Skin and heating (why pulse width is a materials knob)

Classical skin: δ = √(2/ωμσ). A short pulse (high *ω*) confines current to the rail face and the armature skin. That is good for launching a compact (current where the Lorentz force needs it) and bad for a thick Cu rail you thought was uniformly wet.

| Pulse | Skin in Cu (order) | Manufacturing read |
|---|---|---|
| ~1 µs | ~tens of µm | Current on the bore face; erosion localized; armature must conduct at its skin |
| ~100 µs | ~0.2–0.3 mm | More of the rail participates; less peak face *T* for the same ∫*I*²*dt* |
| ~ms / precondition 5–50 kHz | δ still sub-mm at 50 kHz | Precondition path in the driver is a **clock**, not just a “warm-up” |

Anomalous skin (mfp ≳ δ) is a High-mapping sibling; at room-temperature Cu and these pulses it is usually secondary. Do not confuse optical 10–20 nm with RF skin.

If the armature is a **powder compact**, each particle has its own δ. A 20 µm Cu particle is electrically thick at 1 µs; a 20 µm steel particle is closer to the line (lower σ). Steel liquifies on the way to 500 m/s in the project README because resistivity dumps *I*²*R* into a small *C* — that is this machine, not a mystery.

### 2.3 Bonding: yield, not melt (unless you choose melt)

Cold-spray success is `elasticity` past yield plus oxide rupture, at a particle velocity above a material-specific window, **below** the velocity that melts the particle in flight.

| Outcome | Grid clause | How it looks |
|---|---|---|
| Bounce / poor adhesion | Below yield / no oxide break | Dust, unsintered |
| Cold bond | Plasticity, *T* < *T*<sub>m</sub> | Dense, low HAZ |
| Mushy / splash | Local *T* → *T*<sub>m</sub> | Splash crown, substrate HAZ |
| Vapor / plasma spray | Grid gone, then recondense | Not this process goal |

First-sound / *v*<sub>s</sub> in the metal is km/s. Your 200–800 m/s is sub-sonic in the solid and still above many cold-spray windows. The clock that matters on impact is the acoustic transit of the particle (ns–µs), not the coil’s ms tail.

**Rail erosion** injects rail metal into the deposit. That is alloying if you chose the rail, contamination if you did not. QSA does not add a new machine; it is grid material from a second source.

### 2.4 Plasma as a process lever

Breakdown of the carrier vapor or the contact gap is `dielectric-breakdown`: geometry-dependent, messy after the first spark, dry-air class ~3 MV/m and **worse** in H-rich vapor. The technical note already wants a **solid or compact armature**, not a plasma armature.

| Plasma | Manufacture | Experiment |
|---|---|---|
| Off (good contact, wet slurry, moderate *dV/dt*) | Reproducible mass, less rail gouging | Isolate yield / magnetostriction / H-latch |
| On (starved contact, high *dV/dt*, dry powder) | Oxide break, extra heat, rail loss, EMI | A **different write**. Do not compare to “cold” shots |

Paschen in a small H₂-contaminated gap is why the [EM-LENR](EM-LENR.md) cell treats plasma as Phase 4, not Phase 0. The same rule applies on the barrel.

### 2.5 Manufacturing knobs (which way)

| Parameter | Toward a cold, coherent Cu deposit | Toward a controlled alloyed / hotter deposit | Collapse |
|---|---|---|---|
| *I* peak | **Up** until velocity is in the bond window | Higher still if you want more rail injection | Runaway melt / plasma armature |
| Pulse width | Match skin to armature size (Cu powder: shorter is OK) | Longer ⇒ more bulk heating | So long it is a bake |
| Barrel length | Fixed ~100 mm; do not chase velocity with length | — | Wear along extra unused length |
| Powder / carrier conductivity | **Up** (Cu, light oil) for solid armature | Lower-σ powder if you *want* heat (steel) | Too dry / insulating ⇒ gap breakdown |
| Particle size | Large enough to be electrically thick and to survive flight | Fines for surface area, knowing they heat and oxidize faster | Only nano: skin + melt + H pickup |
| Carrier | Low residue, matched to metal (no H source on Ti) | Reducing carrier if oxides are the problem | H-rich carrier on high-strength steel / Ti → [embrittlement](hydrogen-embrittlement.md) |
| Rail metal | Same as powder (Cu/Cu) | Dissimilar on purpose (hard-facing) | Accidental Fe into a Cu mirror film |
| Substrate *T* | Cold (the point of CSAM) | Warm if you need extra diffusion | Substrate melt |
| Stand-off / angle | In the cold-spray window | Steeper for peening / more strain | Grazing bounce |

Precondition (5–50 kHz on the existing driver) is a **clock knob**: it can wet contacts and lower breakdown chance before the main pulse. Use it as “plasma off,” not as extra energy.

---

## 3. The same device as an experiment

You do not need a second lab. A missed shot, an empty barrel, a coil around a ¼″ cell, or a glass slide as the substrate *is* a QSA experiment. Below, each is a real applied use of a filed machine.

### 3.1 Empty-barrel / Cu-powder baseline — `collective-screening` + Joule

**What.** Fire the driver into shorted rails, or throw Cu powder in inert/oil with no ambition to build a part.

**Reads.** *I*(t), rail-face heating, EMI on nearby loops. This is EM-LENR Phase 0 and the manufacturing calorimetry baseline.

**Tune.** Pulse width vs rail temperature: shorter pulse should heat a thinner skin (higher face *T*, less bulk *T*). If face and bulk *T* do not split with width, your *ω* is not where you think.

### 3.2 Glass-slide coatings — `collective-screening` / [thin-film-optics](thin-film-optics.md)

**What.** Deposit Cu or Al (or Ag if you ever load it) onto glass. Measure *R*(λ), *T*(λ), continuity.

**Question.** Did the splat field **percolate**, and is the connected thickness ≳ 10–20 nm class?

**Tune.** Shot count **up** to cross percolation (cliff in *R*, not linear). Pulse energy **down** if you are melting instead of tiling. Rail metal will show up in the film — treat it as the film’s second layer.

A percolated Cu film that still transmits in the visible is starved buffer or oxidized (carrier *n* killed). That is the plasma-edge / *n* knob, not “cold spray failed.”

### 3.3 Ni or Fe powder in the pulse *B* — `magnetostriction` + latch

**What.** Ni powder as armature or as the inventory in the sliding ⅜″ coil cell (no ejection).

**Question.** Does *B* write strain / remanence, or only heat?

**Tune.**

| Knob | Toward a magnetostrictive write | Null |
|---|---|---|
| Peak *B* | Through Ni alignment / technical write field | Below alignment: *λ* hidden |
| Particle size | Above the blocking class (not only 10 nm) | Superparamagnetic: no static *λ*, no remanence |
| *T* | Well below Ni *T*<sub>C</sub> (627 °C) | Approach *T*<sub>C</sub> or melt |
| Host | Ni vs Pd in the same coil | Pd should be the weak magnetic writer |

Post-shot VSM / powder-pattern remanence is the readout. A coil around the barrel during a Ni shot is a **write field in flight** for [bonded-magnets](bonded-magnets.md).

### 3.4 Steel or Ti + H-rich carrier — [hydrogen-embrittlement](hydrogen-embrittlement.md)

**What.** The README already warns hydrogen is harmful to titanium. High-strength steel with oil / glycerol-type carriers is the same write.

**Question.** Did the process charge and pin H?

**Tune.** Carrier **off** hydrogen (isoparaffinic, dry gas) vs **on** (glycerol, moisture). Post-spray bake as **erase**. Compare toughness / delayed crack, not just deposit density.

If bake restores toughness, you wrote the interstitial latch while making a part. That is a successful QSA observation and a manufacturing defect.

### 3.5 Hydride-forming powder — [hydride-storage](hydride-storage.md)

**What.** Pd, Ni, or a storage alloy as feedstock, then a Sieverts / residual-H measurement.

**Question.** Did impact **decrepitate** the grid and grow a pinned residual that a designed *P*–*T* swing will not give back?

**Tune.** Cycle count (shots) **up** to grow residual; a bake column to erase. Useful as a way to *make* traps on purpose.

### 3.6 Magnetic deposit — [bonded-magnets](bonded-magnets.md)

**What.** NdFeB or hard-ferrite powder, optionally with *B* on during flight or on the substrate.

**Question.** After splat, is *KV* still on the blocked side? Did impact shock-erase remanence (mechanical latch failure)?

**Tune.** Particle size **up**; impact velocity **down** until remanence survives; alignment field **on** if you want a magnet, **off** if you want a control.

### 3.7 Contained coil cell (no rails) — [EM-LENR](EM-LENR.md) Phase 0–3

**What.** The ¼″ cell + ⅜″ coil already specified. Powder stays in. This is not CSAM deposition; it is the same driver family used as a repetitive writer.

**Question.** Host × gas × pulse pattern of the interstitial latch, **without** opening the energy-gate.

**Tune.** Follow EM-LENR §§5–6. Ni first. Plasma off. Hold-power after *I* = 0.

Steven owns whether that latch is the LENR configuration. You own whether the coil writes *something* that bake-out / size / *B*-threshold can erase.

### 3.8 Breakdown map of the barrel gas — `dielectric-breakdown`

**What.** Controlled fill (air, N₂, H₂, oil vapor) at known gap and *dV/dt*, no powder.

**Question.** Where is the Paschen / vapor-breakdown cliff for *this* geometry?

**Tune.** Pressure **both ways** (Paschen minimum). Gap **up** to leave the minimum. *dV/dt* **down** to stay left of breakdown if you want a solid armature.

Until this map exists, “plasma optional” is a wish.

---

## 4. Combined isolation sequence (device-first)

Run as **device campaigns**, not as separate science projects.

| Campaign | Shots | Verdict you want |
|---|---|---|
| A. Driver into shorted rails | no powder | Skin / EMI / heat baseline |
| B. Cu / oil → glass | thickness series | Percolation + *R*/*T* (optics) |
| C. Cu / oil → metal | velocity / *I* series | Yield-bond window vs melt |
| D. Ni powder, coil cell, inert | *B*, size, *T* | Magnetostriction / remanence |
| E. Ni powder, coil cell, H₂ | vs D | Interstitial reservoir added |
| F. Steel + H-rich vs dry carrier → part | bake column | Embrittlement write/erase |
| G. Breakdown map, no powder | *P*, gap, *dV/dt* | Plasma as a known factor |
| H. Only then: D₂, neutrons, calorimetry | EM-LENR Phase 5 | Search, not isolation |

A–C are manufacturing. D–G are experiments the same hardware is good for. H waits on Steven for interpretation; the data are still yours to take cleanly.

---

## 5. Falsifiers (device-level)

- Pulse width does not change the rail-face vs bulk heating split (skin mapping unused).  
- Cu-on-glass *R* grows linearly with shot count through the 5–20 nm class with no percolation cliff.  
- Ni and Pd in the same coil cell are indistinguishable on remanence and on any H-related residual.  
- Steel deposits from dry vs H-rich carriers are equally tough, and bake does nothing.  
- “Cold” and “plasma” shots are calorimetrically identical after you subtract *I*²*R* (then you cannot claim plasma is optional).

None of these is a LENR falsifier. They are falsifiers of using this barrel as a controlled writer of the machines you already filed.

---

## 6. What this file is not

- Not a KiCad driver design ([`ForFutureGrok.md`](../../em-csam/ForFutureGrok.md) still owns that).  
- Not a substitute for [EM-LENR](EM-LENR.md).  
- Not a claim that rail erosion, skin, or magnetostriction are new physics. They are the library applied to a head you are actually building.
