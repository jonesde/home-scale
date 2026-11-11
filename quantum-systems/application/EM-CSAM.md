---
origin: application
device: EM-CSAM micro-railgun deposition head, driver, and the same barrel/coil as a lab
updated: 2026-11-12
---

# Application: EM-CSAM head (manufacture + experiment)

**Device.** A short-barrel parallel-rail micro-accelerator that throws a metered metal-powder armature (usually in a carrier) at 200–800 m/s class onto a substrate, plus the capacitor-discharge driver that feeds it. Hardware home: [`../../em-csam/`](../../em-csam/README.md).
**QSA machines.** `oscillator-grid` (impact, yield, melt); `collective-screening` (skin in rails and armature); `energy-gate` as `dielectric-breakdown` (gas route to a plasma) and [`electrical-contacts`](../library/electrical-contacts.md) (the contact route); [`electrical-resistivity`](../library/electrical-resistivity.md) (Joule heating, action to melt); `anisotropy-latch` + `magnetostriction` when the powder is ferromagnetic; interstitial latch only if H/D is in the system ([EM-LENR](EM-LENR.md), [hydrogen-embrittlement](hydrogen-embrittlement.md), [hydride-storage](hydride-storage.md)).
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
| Current in rails and armature | `collective-screening` (skin) | Current density falls off exponentially into the rail; the depth depends on pulse length and, behind a moving slug, on speed. There is no edge to the layer. |
| Rail–armature interface and particle contacts | `electrical-contacts` | Film puncture, then heating of the contact spots to softening and melting voltage. Solid versus arcing contact. |
| Gas gaps and slurry voids | `dielectric-breakdown` | Paschen breakdown of the gas route. Process lever **and** confound. |
| Lorentz body force, impact, plastic strain | `oscillator-grid` | Yield vs melt vs fracture. Bonding is a yield/oxide-rupture event, not a *T*<sub>m</sub> event if you stay “cold.” |
| *B* in a Ni/Fe particle | `magnetostriction` + latch | Strain locked to *M* if *B* exceeds alignment and *T* < *T*<sub>C</sub> and the grain is blocked. |
| H-rich carrier or residual moisture on steel/Ti | interstitial latch | Unwanted write of [embrittlement](hydrogen-embrittlement.md). |
| Impact of already-latched magnetic powder | `anisotropy-latch` | Shock can erase remanence (mechanical failure path). |

The manufacturing goal (coherent deposit, low substrate heat) and the experimental goal (isolate one of those writes) use the **same knobs**, turned for different verdicts.

---

## 2. Manufacturing theory of operation

### 2.1 Acceleration

*F* = ½ *L*′ *I*² with *L*′ ~ 0.3–0.5 µH/m class for this head’s flat side-by-side rails (the earlier 0.5–0.6 was for a square bore; the hardware review of 2026-11 revised it). Short barrel (~100 mm) ⇒ you buy velocity with *I*, not with length. The armature is a slurry slug whose mass, conductivity, and fill fraction are process variables, not nuisances.

Two knobs the hardware notes added after that review ([`DesignReview-2026-11.md`](../../em-csam/DesignReview-2026-11.md)): an external field (permanent magnets, a term linear in *I*) and series augmenting turns (more force per *I*²). At this scale the rails’ own field is only ~0.8 T class at 2 kA, so a magnet competes with it. The magnet term is what lets pulse shape trade heat against velocity.

### 2.2 Skin and heating (why pulse width is a materials knob)

Three rules, one constant. Current enters a conductor by magnetic diffusion with *D* = ρ/μ (0.0137 m²/s in Cu). Steady sine: δ = √(2ρ/ωμ). Single pulse of length *t*: the railgun literature uses δ(*t*) = 2√(*Dt*), and other cuts on the same erfc profile run from 0.8 to 2 times √(*Dt*). Moving contact: 2√(*Da*/*V*), set by the transit time of the slug. Each of these is a 1/e-type length on a smooth profile; none is the edge of a layer. Numbers and sources: [skin-effect](../library/skin-effect.md) §4.3. A short pulse keeps current near the rail face and the armature surface. That is good for launching a compact (current where the Lorentz force needs it) and bad for a thick Cu rail you thought was uniformly wet.

| Pulse | Depth in Cu as a single pulse, 2√(*Dt*) (other cuts) | Steady δ if the pulse were one half-period | Manufacturing read |
|---|---|---|---|
| ~1 µs | 0.23 mm (0.13–0.15 mm) | 0.09 mm; the often-quoted 66 µm is a steady 1 MHz sine | Current near the bore face; erosion localized; armature must conduct at its surface |
| ~100 µs | 2.3 mm (1.3–1.5 mm) | 0.9 mm | More of the rail participates; less peak face *T* for the same ∫*I*²*dt* |
| 0.2–0.7 ms launch pulse (the driver’s actual pulse) | 3.3–6.2 mm (1.9–3.9 mm) | 1.3–2.5 mm | The field reaches through a 3–4 mm rail before the pulse ends; the pulse is a bulk heater of the rail edge zone |

No rail width is a cut-off. By the step-field (erfc) solution the field in Cu at the end of the 0.2–0.7 ms pulse is still 20–49 % of its surface value 3 mm in and 9–36 % at 4 mm; under a steady sine it falls as e^(−*x*/δ). A wider rail carries progressively less extra pulse current, and that taper does not end at 3–4 mm.

Behind the moving slug a different clock applies, the velocity skin effect. The rail under a 1 mm slug sees current only for the transit time, so the contact current sits in the first 0.73 mm of Cu at 100 m/s and 0.33 mm at 500 m/s, whatever the pulse length, and it concentrates at the rear of the slug. The railgun literature names this as a main cause of the transition from solid contact to arcing. It rests on a diffusion model and on transition speeds; no direct measurement of the layer was found.

Anomalous skin (mean free path ≳ δ) is negligible here. The mean free path in room-temperature Cu is 39–40 nm against a δ of 1 mm or more at this driver’s 0.7–4 kHz, a ratio of about 3–6 × 10⁴; the two would meet only near 3 THz. Do not confuse the optical depth (about 13 nm in Ag and 7 nm in Al, as intensity depths) with any of these.

If the armature is a **powder compact**, the skin clock applies to the *slug*, not to each particle. A 20 µm Cu particle is electrically **thin** at every pulse this driver makes: its 10 µm radius is 0.15 of the steady δ even at 1 MHz (66 µm) and under 0.01 of it at the 0.2–0.7 ms launch pulse (an earlier version of this note had that backwards). For the slug, δ is set by its effective resistivity and grows as √ρ. At 200 kHz δ is 0.15 mm in solid Cu, 0.47 mm at 10× bulk resistivity and 1.5 mm at 100×. Against a 0.5 × 0.5 × 1.0 mm slug the 100× case exceeds every dimension, and the 10× case is marginal: about the bore width and half the slug length. At the launch pulse’s own 0.7–4 kHz, δ is 1–2.5 mm even in solid Cu, so there is no skin effect in a paste armature. The “10–100× bulk” figure is itself an assumption for a conditioned slug. A pressed, unreduced Cu compact measures 10⁴–10⁵ Ω·m, about 10¹² times bulk, and no value was found for loose or oil-borne powder ([electrical-resistivity](../library/electrical-resistivity.md)). A higher resistivity only makes δ larger. What the particles do have is **contacts**. An oxidised powder chain is high-resistance and force-dependent: 10⁴–10⁷ Ω for a 50-bead steel chain, about 10⁸ Ω for a 0.3 mm bed of oxidised Cu powder. “Insulator” overstates it. Two gates then act, and they are different conditions. Film puncture is a field gate, 10⁷–10⁸ V/m across the oxide. The metal gate is thermal: a contact spot heats with the voltage across it and melts at a fixed voltage, 0.43 V for Cu. Current-driven bead chains hold 0.2–0.4 V per contact (steel 0.4, brass 0.3, bronze 0.2; copper was not measured), and that plateau is the micro-welding regime itself, the stage in which the necks grow. A 3D bed of oxidised Cu powder shows no plateau: its voltage climbs to 52–67 kV/m, about 5 V per particle layer, and then collapses by five orders. Numbers and sources: [electrical-contacts](../library/electrical-contacts.md) §4.3. That this contact latch, and not skin, decides solid vs boiling armature is a **conjecture**: no opened source covers a powder-slurry armature. Steel liquifies on the way to 500 m/s in the project README because resistivity dumps *I*²*R* into a small *C* — that is this machine, not a mystery.

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

Breakdown of the carrier vapor or the contact gap is `dielectric-breakdown`: geometry-dependent and messy after the first spark. The technical note already wants a **solid or compact armature**, not a plasma armature. Numbers and sources for this section: [dielectric-breakdown](../library/dielectric-breakdown.md) §4.3 and [electrical-contacts](../library/electrical-contacts.md) §4.3.

Which rule applies depends on the gap.

| Gap | Rule | Number |
|---|---|---|
| mm–cm (barrel bore, stand-off) | Field, falling slowly with gap | Dry air ~3 MV/m at 1 cm, 4.6 MV/m at 1 mm |
| Any gap, voltage below the Paschen floor | No avalanche breakdown at all | 327–352 V in air, 230–273 V in H₂ |
| ~7–15 µm at 1 atm | The Paschen minimum itself | Air 7.2–7.5 µm (44–49 MV/m); H₂ 13.8–15.1 µm |
| Below ~5–10 µm at 1 atm (voids between particles, the rail face) | Field emission from the cathode; voltage falls with gap | 100–350 V/µm |

So ~3 MV/m is valid only for the first row. A void of 1–10 µm holds about a hundred to a few hundred volts, a field 15–100 times the dry-air figure, and below the Paschen minimum it fails through the electrode surface. Under a micrometre the voltage it holds falls in proportion to the gap. The earlier version applied 3 MV/m to the contact gap and the slurry voids.

The gas is **worse in hydrogen**: H₂ holds about 0.6 of the field of air and 0.5 of N₂ at the same density, and its Paschen floor is lower. That is sourced for hydrogen gas only. Hydrocarbon vapour from an oil carrier is not shown to be weaker than air: alkane strength rises with chain length, and no ratio to air was found.

Pulse length does not move the gas threshold here. The breakdown field of air is 2.3 times higher for a 10 ns pulse and a few per cent higher at 1 µs, so at this driver’s 0.2–0.7 ms it is the static value. Any *dV/dt* effect in the device comes from the circuit (induced voltage) or from the contact. The contact route is the one to watch: in an inductive circuit a molten bridge that is pinched off starts an arc at open-circuit voltages down to the melting voltage, about 0.4 V for Cu, on rough surfaces. An established arc then needs only 12–15 V and 0.4–1.1 A in a resistive circuit.

| Plasma | Manufacture | Experiment |
|---|---|---|
| Off (good contact, wet slurry, contact kept under load while current flows) | Reproducible mass, less rail gouging | Isolate yield / magnetostriction / H-latch |
| On (starved contact, dry powder, contact lost while current flows) | Oxide break, extra heat, rail loss, EMI | A **different write**. Do not compare to “cold” shots |

Paschen in a small H₂-contaminated gap is why the [EM-LENR](EM-LENR.md) cell treats plasma as Phase 4, not Phase 0: the H₂ floor is 54–122 V below the air floor, depending on the table used. The same rule applies on the barrel.

### 2.5 Manufacturing knobs (which way)

| Parameter | Toward a cold, coherent Cu deposit | Toward a controlled alloyed / hotter deposit | Collapse |
|---|---|---|---|
| *I* peak | **Up** until velocity is in the bond window | Higher still if you want more rail injection | Runaway melt / plasma armature |
| Pulse width | Short enough to limit ∫*I*²*dt* in the rails; the slug has no skin effect at this driver's pulses | Longer ⇒ more bulk heating | So long it is a bake |
| Barrel length | Fixed ~100 mm; do not chase velocity with length | — | Wear along extra unused length |
| Powder / carrier conductivity | **Up** (Cu, light oil) for solid armature | Lower-σ powder if you *want* heat (steel) | Poor contact ⇒ arcing at the contacts (see §2.4) |
| Particle size | Large enough to survive flight (no particle here is electrically thick: a 20 µm Cu particle is thin at every pulse) | Fines for surface area, knowing they heat and oxidize faster | Only nano: melt + oxide + H pickup |
| Carrier | Low residue, matched to metal (no H source on Ti) | Reducing carrier if oxides are the problem | H-rich carrier on high-strength steel / Ti → [embrittlement](hydrogen-embrittlement.md) |
| Rail metal | Same as powder (Cu/Cu) | Dissimilar on purpose (hard-facing) | Accidental Fe into a Cu mirror film |
| Substrate *T* | Cold (the point of CSAM) | Warm if you need extra diffusion | Substrate melt |
| Stand-off / angle | In the cold-spray window | Steeper for peening / more strain | Grazing bounce |

Precondition is a **contact knob**: a current-limited sintering step whose endpoint is slug resistance (the hardware notes now use a ballast-limited current, not a 5–50 kHz tone). The direction is supported. A current step leaves welded bridges, and the resistance afterwards is set by the largest current applied. Under a voltage source the same step runs away (under 2 µs in silver nanoparticle structures); a series resistor limits that and does not remove it, and the first asperity to touch still sees nearly the whole source voltage. Use the step as “plasma off,” not as extra energy.

The caveat is mechanical. The bridges are 10–15 µm and weak: in a static copper powder bed a shock restores the high-resistance state, and a coherer resets when tapped. A slurry that flows or accelerates after conditioning may reset the same way. Nothing has been tested on a moving slurry, so whether the step lowers breakdown chance in the main pulse is open until the slug resistance is measured after motion. Sources: [electrical-contacts](../library/electrical-contacts.md) §4.3.

---

## 3. The same device as an experiment

You do not need a second lab. A missed shot, an empty barrel, a coil around a ¼″ cell, or a glass slide as the substrate *is* a QSA experiment. Below, each is a real applied use of a filed machine.

### 3.1 Empty-barrel / Cu-powder baseline — `collective-screening` + Joule

**What.** Fire the driver into shorted rails, or throw Cu powder in inert/oil with no ambition to build a part.

**Reads.** *I*(t), rail-face heating, EMI on nearby loops. This is EM-LENR Phase 0 and the manufacturing calorimetry baseline.

**Tune.** Pulse width vs rail temperature: shorter pulse should heat a thinner skin (higher face *T*, less bulk *T*). If face and bulk *T* do not split with width, your *ω* is not where you think.

### 3.2 Glass-slide coatings — `collective-screening` / [thin-film-optics](thin-film-optics.md)

**What.** Deposit Cu or Al (or Ag if you ever load it) onto glass. Measure *R*(λ), *T*(λ), continuity.

**Question.** Did the splat field **percolate** (a step in sheet resistance), and how thick is the connected film? Reflectance rises smoothly with thickness and has no step: for Ag it is half the bulk value near 12–14 nm and 90 % near 31–33 nm ([reflection](../library/reflection.md)).

**Regime.** A solid-slug or splat shot lands µm-class metal, far above the thickness at which a film is optically thick. A 5–20 nm film only comes from the **exploding / vapor** regime (thin foil or fine wire as the armature), which is a different write from cold bonding. Run this series there, and do not read a splat coupon against the percolation threshold.

**Tune.** Shot count **up** to cross percolation: expect a step in dc sheet resistance (unseeded Ag percolates at 6–12 nm) and a smooth rise in *R*. Pulse energy **down** if you are melting instead of tiling. Rail metal will show up in the film — treat it as the film’s second layer.

A percolated Cu film that still transmits in the visible is thin compared with its optical decay length, or oxidized (carrier *n* killed). That is the plasma-edge / *n* knob, not “cold spray failed.”

### 3.3 Ni or Fe powder in the pulse *B* — `magnetostriction` + latch

**What.** Ni powder as armature or as the inventory in the sliding ⅜″ coil cell (no ejection).

**Question.** Does *B* write strain / remanence, or only heat?

**Tune.**

| Knob | Toward a magnetostrictive write | Null |
|---|---|---|
| Peak *B* | Through Ni alignment / technical write field | Below alignment: *λ* hidden |
| Particle size | Above the blocking class for Ni (about 34 nm at room temperature and 100 s; see [superparamagnetism](../library/superparamagnetism.md)) | Superparamagnetic: no static *λ*, no remanence |
| *T* | Well below Ni *T*<sub>C</sub> (628–631 K, about 355 °C; an earlier version of this note said 627 °C) | Approach *T*<sub>C</sub> or melt |
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

**What.** Controlled fill (air, N₂, H₂, oil vapor) at known gap, pressure and voltage, no powder. Use the actual rail metal and finish: the Paschen minimum depends on the cathode.

**Question.** Where is the Paschen / vapor-breakdown threshold for *this* geometry?

**Tune.** Pressure **both ways** (Paschen minimum). At 1 atm every mm-scale barrel gap is already far to the right of the minimum, which sits at 7–9 µm in air and N₂ and 14–15 µm in H₂; a 1 mm air gap reaches it near 5.5–5.7 torr. Gap **up** raises the voltage needed on that side. Fill: expect H₂ to hold about 0.6 of the air field; oil vapor has no sourced ratio, so measure it. *dV/dt* is not a gas knob at these pulse lengths, since the threshold moves only for pulses of a microsecond and shorter. Record voltage and contact state in its place. Numbers: [dielectric-breakdown](../library/dielectric-breakdown.md) §4.3.

This map covers the gas route only. An arc started by a contact that parts under current is a contact event ([electrical-contacts](../library/electrical-contacts.md)) and needs powder shots to map.

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
| G. Breakdown map, no powder | *P*, gap | Gas-route plasma as a known factor |
| H. Only then: D₂, neutrons, calorimetry | EM-LENR Phase 5 | Search, not isolation |

A–C are manufacturing. D–G are experiments the same hardware is good for. H waits on Steven for interpretation; the data are still yours to take cleanly.

---

## 5. Falsifiers (device-level)

- Pulse width does not change the rail-face vs bulk heating split (skin mapping unused).  
- Cu-on-glass sheet resistance shows no step as shot count crosses the percolation thickness. (The earlier version asked for a cliff in *R*; a smooth rise in *R* is what thin-film optics predicts, so it tests nothing.)  
- Ni and Pd in the same coil cell are indistinguishable on remanence and on any H-related residual.  
- Steel deposits from dry vs H-rich carriers are equally tough, and bake does nothing.  
- “Cold” and “plasma” shots are calorimetrically identical after you subtract *I*²*R* (then you cannot claim plasma is optional).

None of these is a LENR falsifier. They are falsifiers of using this barrel as a controlled writer of the machines you already filed.

---

## 6. What this file is not

- Not a KiCad driver design ([`AGENTS.md`](../../em-csam/AGENTS.md) still owns that).  
- Not a substitute for [EM-LENR](EM-LENR.md).  
- Not a claim that rail erosion, skin, or magnetostriction are new physics. They are the library applied to a head you are actually building.
