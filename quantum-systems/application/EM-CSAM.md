---
origin: application
device: EM-CSAM micro-railgun deposition head, driver, and the same barrel/coil as a lab
updated: 2026-11-14
---

# Application: EM-CSAM head (manufacture + experiment)

**Device.** A short-barrel parallel-rail micro-accelerator that throws a metered metal-powder armature (usually in a carrier) at 200–800 m/s class onto a substrate, plus the capacitor-discharge driver that feeds it. Hardware home: [`../../em-csam/`](../../em-csam/README.md).
**QSA machines.** `oscillator-grid` (impact, yield, melt: [elasticity](../library/elasticity.md), [melting](../library/melting.md)); `collective-screening` ([skin-effect](../library/skin-effect.md) in rails and armature); `energy-gate` as [dielectric-breakdown](../library/dielectric-breakdown.md) (gas route to a plasma) and [electrical-contacts](../library/electrical-contacts.md) (the contact route); [electrical-resistivity](../library/electrical-resistivity.md) (Joule heating, action to melt); `anisotropy-latch` and [magnetostriction](../library/magnetostriction.md) when the powder is ferromagnetic; hydrogen only if H/D is in the system ([hydrogen-in-metals](../library/hydrogen-in-metals.md), [EM-LENR](EM-LENR.md), [hydrogen-embrittlement](hydrogen-embrittlement.md), [hydride-storage](hydride-storage.md)).
**Status.** Working application of *this* repository’s hardware. Manufacturing first. The same setup is a pulsed high-strain, high-*dB/dt* experiment. **Not a tested protocol.**
**Credit.** EM-CSAM is the author’s project. QSA here is analysis of that device, not a redesign of the barrel.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** Capacitor discharge, rail–armature current, flying metal, and carrier vapor can maim without any “interesting physics.” Hydrogen-rich carriers on steel or Ti can charge a part that cracks later. Machining BeCu is a beryllium-control problem; stay on copper if you do not already have that shop. These notes are not a build sequence or a pressure rating. Do not scale the barrel or bank in search of a nuclear signature.

Derived specs: [design-spec-sheets](../library/derived/design-spec-sheets.md), [requirement-audit](../library/derived/requirement-audit.md).

> **Revised 2026-11-14** (extends the corrections of 2026-11-12). Every number in this file is now one of three kinds, and says which. **Library**: stated in a sourced library file, linked where it is used. **Computed here**: arithmetic on library numbers with the inputs shown, guarded by [`analysis/checks/b3_applications.py`](../analysis/checks/b3_applications.py). **Hardware note**: a planning value or model result from [`../../em-csam/`](../../em-csam/README.md) and its `tools/shot_model.py`; none of these is a measurement. What changed: §2.2 gains Joule heating by action integral and by enthalpy; §2.3 states the bonding window from the sourced critical velocities and lists the metals that have none; §2.4 compares the bank voltage with the Paschen floor and the arc minimum; §3 restates each experiment against observables the library supports, and §5 drops the falsifiers that standard physics already answers (the skin split with pulse width, nickel against palladium remanence). The skin layer is treated throughout as a smooth profile with no edge.

---

## 1. What the device is, in QSA terms

A shot is a **write** on several machines at once:

| During the pulse | Machine | What is being written or erased |
|---|---|---|
| Current in rails and armature | `collective-screening` ([skin-effect](../library/skin-effect.md)) | Current density falls off smoothly into the rail; the depth depends on pulse length and, behind a moving slug, on speed. The layer has no edge. |
| The same current as heat | [electrical-resistivity](../library/electrical-resistivity.md) | Joule heating counted by the action integral; melting begins at a measured action. |
| Rail–armature interface and particle contacts | [electrical-contacts](../library/electrical-contacts.md) | Film puncture, then heating of the contact spots to softening and melting voltage. Solid versus arcing contact. |
| Gas gaps and slurry voids | [dielectric-breakdown](../library/dielectric-breakdown.md) | Paschen breakdown of the gas route. Process lever **and** confound. |
| Lorentz body force, impact, plastic strain | `oscillator-grid` ([elasticity](../library/elasticity.md), [melting](../library/melting.md)) | Yield, bond, melt or erode. A cold bond is made by plastic flow above a critical velocity, with the bulk of the particle below *T*<sub>m</sub>. |
| *B* in a Ni/Fe particle | [magnetostriction](../library/magnetostriction.md) + latch | Strain follows the alignment of *M* below *T*<sub>C</sub> (628–631 K for Ni). It is small: Ni saturates at −35 to −40 ppm, which fully clamped is 7–9 MPa, about 5 % of yield, and equals the thermal expansion of a 3 K rise. A free particle takes it with no stress. |
| H-rich carrier or residual moisture on steel/Ti | trapped hydrogen ([hydrogen-in-metals](../library/hydrogen-in-metals.md)) | Unwanted write of [embrittlement](hydrogen-embrittlement.md). |
| Impact of already-magnetized hard powder | `anisotropy-latch` ([permanent-magnet-latch](../library/permanent-magnet-latch.md)) | Shock demagnetizes: measured in sintered Nd-Fe-B at 6–7 GPa (by fracture between grains) and at 22 GPa. No threshold is established. |

The manufacturing goal (coherent deposit, low substrate heat) and the experimental goal (isolate one of those writes) use the **same knobs**, turned for different verdicts.

---

## 2. Manufacturing theory of operation

### 2.1 Acceleration

*F* = ½ *L*′ *I*². Momentum then fixes the action, whatever the pulse shape: ∫*I*²*dt* = 2*mv*/*L*′. These are the standard railgun relations. The values that go into them are planning figures from the hardware notes ([`EM-CSAM-ConceptTechnical.md`](../../em-csam/EM-CSAM-ConceptTechnical.md) §3, [`DesignReview-2026-11.md`](../../em-csam/DesignReview-2026-11.md)); none has been measured.

| Quantity | Value | Kind |
|---|---|---|
| Bore, barrel | 0.5 × 0.5 mm, 100 mm | Hardware note |
| *L*′ | 0.4 µH/m, range 0.3–0.5, for flat side-by-side rails (0.5–0.6 was for a square bore) | Hardware note: three estimates, to be measured |
| Reference slug | 0.5 × 0.5 × 1.0 mm: 2 mg solid, 0.8–1.5 mg as paste; 0.25–0.5 mg for the first driver | Hardware note |
| Constant current for a 2 mg slug, *L*′ = 0.4 | 2.1, 3.5 and 5.7 kA for 300, 500 and 800 m/s, over 0.67, 0.40 and 0.25 ms | Hardware note, recomputed here |
| Launch pulse | One unipolar pulse of 0.2–0.7 ms at 1–4 kA; natural frequency 0.7–4 kHz | Hardware note |
| Rails' own field | About 0.8 T across the gap at 2 kA | Hardware note (model) |
| Velocity | 200–800 m/s class as the target; 50–870 m/s across the shot-model cases | Hardware note and `shot_model.py` |

The barrel is short, so velocity is bought with current. The armature is a slurry slug whose mass, conductivity and fill fraction are process variables.

Two further knobs come from the hardware review: an external field from permanent magnets (a force term linear in *I*) and series augmenting turns (more force per *I*²). Because the rails' own field is under a tesla, a magnet competes with it. For plain rails the action at a given velocity is fixed by the relation above; the magnet term is what lets heat be traded against velocity.

### 2.2 Skin and heating

**Where the current is.** Three rules, one constant. Current enters a conductor by magnetic diffusion with *D* = ρ/μ (0.0137 m²/s in Cu). Steady sine: δ = √(2ρ/ωμ). Single pulse of length *t*: the railgun literature uses δ(*t*) = 2√(*Dt*), and other cuts on the same erfc profile run from 0.8 to 2 times √(*Dt*). Moving contact: 2√(*Da*/*V*), set by the transit time of a contact of length *a*. Each is a 1/e-type length on a smooth profile. Numbers and sources: [skin-effect](../library/skin-effect.md) §4.3.

| Pulse | Depth in Cu as a single pulse, 2√(*Dt*) (other cuts) | Steady δ if the pulse were one half-period | Manufacturing read |
|---|---|---|---|
| ~1 µs | 0.23 mm (0.13–0.15 mm) | 0.09 mm; the often-quoted 66 µm is a steady 1 MHz sine | Outside this driver |
| ~100 µs | 2.3 mm (1.3–1.5 mm) | 0.9 mm | Outside this driver |
| 0.2–0.7 ms (the launch pulse) | 3.3–6.2 mm (1.9–3.9 mm) | 1.3–2.5 mm | The field reaches through a 3–4 mm rail before the pulse ends |

No rail width is a cut-off. By the step-field (erfc) solution the field in Cu at the end of the 0.2–0.7 ms pulse is still 20–49 % of its surface value 3 mm in and 9–36 % at 4 mm. A wider rail carries progressively less extra pulse current, and that taper continues past 3–4 mm.

Behind the moving slug the velocity skin effect applies. The rail under a 1 mm slug sees current only for the transit time (10 µs at 100 m/s, 2 µs at 500 m/s), so the contact current sits in the first 0.73 mm of Cu at 100 m/s, 0.42 mm at 300 m/s, 0.33 mm at 500 m/s and 0.26 mm at 800 m/s, whatever the pulse length, and it concentrates at the rear of the slug. The railgun literature names this as a main cause of the transition from solid contact to arcing, in worked cases near 1 km/s. It rests on a diffusion model and on transition speeds; no direct measurement of the layer was found.

Anomalous skin (mean free path ≳ δ) does not occur here. The mean free path in room-temperature Cu is 39–40 nm against a δ of 1 mm or more at 0.7–4 kHz, a ratio of about 3–6 × 10⁴. The optical depths (about 13 nm in Ag and 7 nm in Al, as intensity depths) are a different length.

If the armature is a **powder compact**, the skin clock applies to the slug as a body. A 20 µm Cu particle is electrically thin at every pulse this driver makes: its 10 µm radius is 0.15 of the steady δ at 1 MHz and under 0.01 of it at the launch pulse. For the slug, δ grows as √ρ: at 200 kHz it is 0.15 mm in solid Cu, 0.47 mm at 10× bulk resistivity and 1.5 mm at 100×. At the launch pulse's own 0.7–4 kHz, δ is 1–2.5 mm even in solid Cu, which is larger than the 0.5 × 0.5 × 1.0 mm slug, so the pulse current fills a paste armature.

**Joule heating of the slug, by action.** The specific action *g* = ∫*J*²*dt* fixes the state of a uniformly heated conductor, and melting begins at a measured value of it ([electrical-resistivity](../library/electrical-resistivity.md) §4.3; one 1975 data set on 0.1 mm wires, disputed by one later paper). For a slug of length ℓ that fills a square bore, the current crosses a section ℓ × bore height, and the momentum relation gives *g* = 2ρ<sub>m</sub>*v*/(*L*′ℓ), with ρ<sub>m</sub> the density. The bore size drops out. Computed here for solid metal, ℓ = 1 mm, plain rails:

| Metal | Action at melt onset, 10¹⁶ A² s m⁻⁴ (library) | Density, kg/m³ (as used in [melting](../library/melting.md)) | Velocity at melt onset, *L*′ = 0.4 (0.3–0.5) µH/m |
|---|---|---|---|
| Cu | 8.05 | 8960 | 1800 m/s (1350–2250) |
| Al | 2.52 | 2699 | 1870 m/s (1400–2330) |
| Ni | 1.72 | 8902 | 390 m/s (290–480) |
| Fe | 1.28 | 7874 | 325 m/s (245–405) |

- Copper at 300, 500 and 800 m/s uses 17 %, 28 % and 45 % of its melt-onset action. The README's "copper to 1 km/s without melting" is 56 %.
- Iron at 500 m/s takes 1.5 times its melt-onset action, which is past complete melting (1.47 against 1.28) and 55 % of the burst value. That is the README's statement that steel liquefies on the way to 500 m/s. No action to melt was found for any steel; pure iron wire is the nearest measured value.
- The velocity scales with ℓ, so a 0.5 mm slug has half these figures. Augmentation raises them by (*L*′ + 2*M*′)/*L*′, and a magnet raises them further.
- The same check in current density: 1–4 kA through 1 mm × 0.5 mm is 2–8 kA/mm². The library gives melt onset within 0.2–0.7 ms at 20–11 kA/mm² in copper and at 8.0–4.3 kA/mm² in iron.
- Zinc and tin, the first two metals of the hardware ladder, have no action value in the library. The hardware notes take 1.1 and 0.17 × 10¹⁶ from the same 1975 report.
- The hardware notes print this table at *L*′ = 0.45 with the actions rounded (Cu about 2000 m/s, Fe about 370 m/s). The planning value of 0.4 gives the lower figures above.

Two limits. The formula assumes uniform current density, and the velocity skin effect concentrates the current at the rear of a solid slug, so the local action there is higher than the mean. And the wire data are for dense metal; a compact is covered by the enthalpy route below.

**By enthalpy.** For a slug of resistance *R* on plain rails the Joule heat per kilogram is *e* = *R*∫*I*²*dt*/*m* = 2*Rv*/*L*′ (hardware note §3.5); the mass drops out. Copper needs 466 kJ/kg from 300 K to reach the melting point and 673 kJ/kg to be fully liquid, of which 207 kJ/kg is fusion ([melting](../library/melting.md) §4.3). Computed here at *L*′ = 0.4 µH/m with *R* held constant:

| Velocity | *R* for melt onset (466 kJ/kg) | *R* for fully liquid (673 kJ/kg) |
|---|---|---|
| 300 m/s | 0.31 mΩ | 0.45 mΩ |
| 500 m/s | 0.19 mΩ | 0.27 mΩ |

A solid Cu slug of 0.5 × 0.5 × 1.0 mm, with the current crossing the 0.5 mm gap, is 0.017 mΩ at 293 K. Melt onset at 500–300 m/s therefore allows 11–19 times the cold solid resistance, which is the hardware note's "10–20× bulk". For solid copper the cold value undercounts, because resistivity rises on the way: the action figure corresponds to a mean resistivity of 5.2 × 10⁻⁸ Ω·m, 3.1 times the 293 K value.

The sourced powder data do not reach that window. A pressed, unreduced Cu compact measures 10⁴–10⁵ Ω·m, about 10¹² times bulk; once reduced it lies at the floor of the plot, which bounds it at 60–600 times bulk; no value was found for loose or oil-borne powder or for a conditioned slug ([electrical-resistivity](../library/electrical-resistivity.md)). The shot model's states (0.2 mΩ solid, 0.5 mΩ melting, 1 mΩ molten, for a 0.5 mg slug with a magnet at 336–313 m/s) are model results on the same heat budget with thresholds of 0.45 and 0.65 MJ/kg.

**Rails.** One published figure exists: copper rails reach melting at 44 kA per millimetre of rail height (an author's statement whose basis was not in the text opened). This head's 1–4 kA over a 0.5 mm rail height is 2–8 kA/mm, 5–18 % of it.

**Contacts.** What the particles have is contacts. An oxidised powder chain is high-resistance and force-dependent: 10⁴–10⁷ Ω for a 50-bead steel chain, about 10⁸ Ω for a 0.3 mm bed of oxidised Cu powder. Two gates then act, and they are different conditions. Film puncture is a field gate, 10⁷–10⁸ V/m across the oxide. The metal gate is thermal: a contact spot heats with the voltage across it and melts at a fixed voltage, 0.43 V for Cu. Current-driven bead chains hold 0.2–0.4 V per contact (steel 0.4, brass 0.3, bronze 0.2; copper was not measured), and that plateau is the micro-welding regime, the stage in which the necks grow. A 3D bed of oxidised Cu powder shows no plateau: its voltage climbs to 52–67 kV/m, about 5 V per particle layer, and then collapses by five orders. Numbers and sources: [electrical-contacts](../library/electrical-contacts.md) §4.3. That the contact state, more than skin, decides solid against boiling armature is a **conjecture** consistent with the budget above: no opened source covers a powder-slurry armature.

### 2.3 Bonding

Cold spray accelerates 10–40 µm particles to 300–1200 m/s and they bond while solid. Deposition occurs between a critical velocity (by convention the speed at 50 % deposition efficiency) and an erosion velocity, which is twice the critical velocity in the Schmidt model. For one particle of one size the change from rebound to adhesion is a threshold; for a powder it is a rise in deposition efficiency. The critical velocity falls as the particle gets hotter, rises as it gets smaller, and for copper moves from 300 to 610 m/s as the powder oxygen goes from 0.02 to 0.38 wt %. The mechanism is disputed between adiabatic shear instability and a pressure-wave account in which the critical velocity is 0.15 √(*K*/ρ). Numbers and sources: [elasticity](../library/elasticity.md) §4.3.

| Metal | Sourced critical velocity, m/s | Against 200–800 m/s |
|---|---|---|
| Cu | 570 (5–22 µm powder, experiment); 460–500 (20 µm, tabulated, not reopened); 588 by the sound-speed rule | Inside, upper half |
| Al | 775–825 (single 14–30 µm particles); 742–867 with powder oxygen; 620–660 (tabulated, not reopened) | At the top or above |
| Ti | 505–610 (29 µm spherical, measured); 690; 700–890 (tabulated, not reopened) | Upper half or above. Hydrogen hazard |
| Steel 316L | 700–750 (tabulated, not reopened) | At the top |
| Ni | Not found. 669 by the sound-speed rule only | — |
| Fe, carbon steel, Zn, Sn | No sourced value | — |

The hardware notes use 360–380 m/s for zinc and 160–180 m/s for tin, from a table they saw as a figure caption; the library has not opened it, and an attempt to open the paper for this pass met a paywall. Those two are the first rungs of the hardware ladder, so their bonding velocities are the least-supported numbers in the plan.

Putting §2.2 beside this table, for a 1 mm solid slug on plain rails at *L*′ = 0.4 µH/m (computed here):

| Metal | Melt-onset velocity by action | Critical velocity used | Ratio |
|---|---|---|---|
| Cu | 1800 m/s | 570 (460–500) | 3.2 (3.6–3.9) |
| Al | 1870 m/s | 775–825 (620–660) | 2.3–2.4 (2.8–3.0) |
| Fe | 325 m/s | 700–750, the 316L figure | 0.43–0.46 |
| Ni | 390 m/s | none | — |

Copper and aluminium have room as solid metal. Iron melts before it reaches the only steel figure available. A porous slug has less room, in proportion to its resistance.

The upper edge of the window has two parts. Erosion: 958 m/s for copper in the Schmidt model, above this head's class. Heat: the kinetic energy per kilogram is *v*²/2, which is 45, 125 and 320 kJ/kg at 300, 500 and 800 m/s, or 10 %, 27 % and 69 % of copper's 466 kJ/kg to melt onset. Kinetic energy alone equals the heat to melt onset at 965 m/s for Cu, 1150 m/s for Al (665 kJ/kg) and 1450 m/s for Fe (1050 kJ/kg). The slug also arrives carrying its Joule heat, so the budget for a cold bond is Joule heat plus *v*²/2 below the melt-onset enthalpy. At 570 m/s that leaves copper 304 kJ/kg, which is *R* ≤ 0.11 mΩ at *L*′ = 0.4 µH/m, 6.4 times the cold solid slug. This is a bulk average; heating at the particle rim is local and reaches melting earlier.

What the library cannot supply for this head:

1. Every critical velocity above is for separate particles of 5–40 µm. No source covers a 0.25 mm³ slug of powder in a carrier. The measured trends (lower for larger and for hotter particles) favour the slug; the hardware notes rely on that.
2. Critical velocities for zinc, tin, nickel, iron and carbon steel.
3. Whether a paste slug arrives as one body or as a spray of particles.

| Outcome | Condition | How it looks |
|---|---|---|
| Bounce / poor adhesion | Below the critical velocity, or oxide not broken | Dust, unsintered |
| Cold bond | Above it, bulk below *T*<sub>m</sub> | Dense, low HAZ |
| Mushy / splash | Joule heat plus impact reaches melt onset | Splash crown, substrate HAZ |
| Vapor / plasma spray | Slug resistance far above the window | A different process |

The speed of sound in the metal, √(*K*/ρ), is 3920 m/s in Cu, so 200–800 m/s is 5–20 % of it. The clock on impact is the acoustic transit: 5 ns across a 20 µm particle and 0.26 µs across a 1 mm slug, against a launch pulse of 0.2–0.7 ms. Strain rates in cold spray are 10⁶–10⁹ s⁻¹.

**Rail erosion** injects rail metal into the deposit. That is alloying if the rail was chosen for it and contamination otherwise.

### 2.4 Plasma as a process lever

Breakdown of the carrier vapor or the contact gap is geometry-dependent and messy after the first spark. The technical note wants a **solid or compact armature**. Numbers and sources for this section: [dielectric-breakdown](../library/dielectric-breakdown.md) §4.3 and [electrical-contacts](../library/electrical-contacts.md) §4.3.

Which rule applies depends on the gap.

| Gap | Rule | Number |
|---|---|---|
| mm–cm (barrel bore, stand-off) | Field, falling slowly with gap | Dry air ~3 MV/m at 1 cm, 4.6 MV/m at 1 mm |
| Any gap, voltage below the Paschen floor | No avalanche breakdown at all | 327–352 V in air, 230–273 V in H₂ |
| ~7–15 µm at 1 atm | The Paschen minimum itself | Air 7.2–7.5 µm (44–49 MV/m); H₂ 13.8–15.1 µm |
| Below ~5–10 µm at 1 atm (voids between particles, the rail face) | Field emission from the cathode; voltage falls with gap | 100–350 V/µm |

So ~3 MV/m is valid only for the first row. A void of 1–10 µm holds about a hundred to a few hundred volts, and below the Paschen minimum it fails through the electrode surface.

**What the bank can do.** The bank sits at 18–55 V in the shot-model cases (hardware note). Computed here: that is 6–20 times below the Paschen floor of air, so the bank voltage cannot start an avalanche in any gas gap at any pressure. At 100–350 V/µm it reaches field emission only across gaps under 0.05–0.55 µm. It is above the minimum arc voltage, 12–15 V at 0.4–1.1 A in a resistive circuit. And in an inductive circuit a molten bridge that is pinched off starts an arc at open-circuit voltages down to the melting voltage, about 0.4 V for Cu, on rough surfaces. In this head, then, a plasma starts at a contact that parts or starves while current flows, or from the voltage induced when the current is interrupted. The gas tables say what a spark does once such a voltage exists.

**How to see it.** The railgun literature reads the muzzle voltage: below 50 V is taken as sliding metal contact, and the change to plasma contact is a jump in it. Measured plasma armatures have electrode falls totalling 45 ± 3 V plus 141 V/cm of column, which for a 0.5 mm gap is about 52 V (computed here). Those measurements were at 6–28 kA/cm²; this head's 2–8 kA/mm² is 200–800 kA/cm², outside that range. Solid-armature transitions are reported near 1 km/s (1,030–1,575 m/s in one study), above this head's class, but no single transition criterion is published. A static rule of one gram-force per ampere of holding force would be 10–39 N at 1–4 kA; a paste slug has no such preload, and the hardware table's Lorentz force is 0.9–6.4 N. If that rule carries over, the contact is starved and the contact route is the expected one. The hardware's muzzle taps are the instrument for all of this.

The gas is **weaker in hydrogen**: H₂ holds about 0.6 of the field of air and 0.5 of N₂ at the same density, and its Paschen floor is 54–122 V lower, depending on the table used. That is sourced for hydrogen gas only. Hydrocarbon vapour from an oil carrier is not shown to be weaker than air: alkane strength rises with chain length, and no ratio to air was found. The same floor is why the [EM-LENR](EM-LENR.md) cell treats plasma as Phase 4.

Pulse length does not move the gas threshold here. The breakdown field of air is 2.3 times higher for a 10 ns pulse and a few per cent higher at 1 µs, so at 0.2–0.7 ms it is the static value.

| Plasma | Manufacture | Experiment |
|---|---|---|
| Off (good contact, wet slurry, contact kept under load while current flows) | Reproducible mass, less rail gouging | Isolate yield, heating and the H write |
| On (starved contact, dry powder, contact lost while current flows) | Oxide break, extra heat, rail loss, EMI | A **different write**. Do not compare to “cold” shots |

### 2.5 Manufacturing knobs (which way)

| Parameter | Toward a cold, coherent Cu deposit | Toward a controlled alloyed / hotter deposit | Loss of the process |
|---|---|---|---|
| *I* peak | **Up** until velocity is in the bond window | Higher still for more rail injection | Melt, then plasma armature |
| Slug resistance | **Down**, below the §2.2 window, by conditioning, compaction or reduction | Higher for a hot or molten deposit | Boiling or exploding slug |
| Slug length | Longer for more action margin (velocity at melt onset scales with ℓ) | Shorter | Mass the bank cannot launch |
| Pulse width | Does not change the slug's action at a given velocity on plain rails; sets peak current and how far the field diffuses into the rail | Longer ⇒ more of the rail heated | So long it is a bake |
| Magnet / augmenting turns | **On**: the same velocity for less action | — | — |
| Barrel length | Fixed ~100 mm | — | Wear along unused length |
| Powder / carrier conductivity | **Up** (Cu, light oil) | Lower-σ powder for heat (steel) | Poor contact ⇒ arcing at the contacts (§2.4) |
| Particle size | Large enough to survive flight; no particle here is electrically thick | Fines for surface area; they oxidize faster, and oxygen raises the critical velocity | Nano only: more oxide per unit of metal (not quantified in the library) |
| Carrier | Low residue, matched to metal (no H source on Ti) | Reducing carrier if oxides are the problem | H-rich carrier on high-strength steel / Ti → [embrittlement](hydrogen-embrittlement.md) |
| Rail metal | Same as powder (Cu/Cu) | Dissimilar on purpose (hard-facing) | Accidental Fe in a Cu film |
| Substrate *T* | Cold | Warm for extra diffusion | Substrate melt |
| Stand-off / angle | Normal incidence, short | — | Grazing bounce (no sourced angle data) |

Precondition is a **contact knob**: a current-limited sintering step whose endpoint is slug resistance (the hardware notes use a ballast-limited current). The direction is supported. A current step leaves welded bridges, and the resistance afterwards is set by the largest current applied. Under a voltage source the same step runs away (under 2 µs in silver nanoparticle structures); a series resistor limits that and does not remove it, and the first asperity to touch still sees nearly the whole source voltage.

The caveat is mechanical. The bridges are 10–15 µm and weak: in a static copper powder bed a shock restores the high-resistance state, and a coherer resets when tapped. A slurry that flows or accelerates after conditioning may reset the same way. Nothing has been tested on a moving slurry, so whether the step holds through the main pulse is open until the slug resistance is measured after motion. Sources: [electrical-contacts](../library/electrical-contacts.md) §4.3.

---

## 3. The same device as an experiment

A missed shot, an empty barrel, a coil around a ¼″ cell, or a glass slide as the substrate is an experiment on a filed machine. Each entry below states the question, what the library already settles, and the result that would contradict the plan. Where standard physics already gives the answer, the entry is a calibration and has no falsifier.

### 3.1 Shorted rails and Cu-powder baseline — skin and Joule (calibration)

**What.** Fire the driver into shorted rails, then throw Cu powder in oil with no ambition to build a part.

**Reads.** *I*(*t*), bus and muzzle voltage, rail temperature rise, EMI on nearby loops. This is EM-LENR Phase 0 and the calorimetry baseline.

**Question.** What are *L*′ and the loop resistance for this barrel at this pulse? The hardware range for *L*′ is 0.3–0.5 µH/m from three estimates, and every velocity and action figure in §2 scales with it.

**Settled already.** Magnetic diffusion into the rail is standard: the field is through a 3–4 mm rail by the end of a 0.2–0.7 ms pulse. The earlier test (“a shorter pulse heats a thinner skin”) is removed: within this driver's range the layer is comparable to the rail, and the outcome would test only the diffusion equation.

### 3.2 Glass-slide coatings — [thin-film-optics](thin-film-optics.md)

**What.** Deposit Cu or Al (or Ag) onto glass. Measure *R*(λ), *T*(λ) and sheet resistance.

**Question.** At what deposited thickness does the splat field percolate, seen as a step in dc sheet resistance? The library has percolation thicknesses for evaporated and sputtered Au and Ag (6–12 nm unseeded Ag); it has none for Cu, and none for a film made by impact.

**Settled already.** Reflectance rises smoothly with thickness and has no step: for Ag it is half the bulk value near 12–14 nm and 90 % near 31–33 nm ([reflection](../library/reflection.md)). A smooth rise in *R* is what ordinary thin-film optics predicts, so it tests nothing.

**Regime.** A solid-slug or splat shot lands µm-class metal, which is optically thick. A 5–20 nm film comes only from the exploding or vapor regime (thin foil or fine wire as the armature), a different write from cold bonding. Run the series there.

**Would contradict.** No step in sheet resistance at any thickness (the deposit never forms a connected film), or a step in *R* coincident with it in a film shown to be continuous.

A percolated Cu film that still transmits in the visible is thin compared with its optical decay length, or oxidized.

### 3.3 Ni powder in the pulse *B* — a soft-magnet control

**What.** Ni powder as armature, or as the inventory in the coil cell with no ejection.

**Settled already.** Three library facts answer the earlier question (“does *B* write strain or remanence, or only heat?”).

- The field is enough. A Ni sphere saturates at an applied field of about 0.23 T. By the hardware note's 0.8 T at 2 kA, the rails pass that near 0.6 kA.
- The strain is not retained and is small beside heating. Saturation strain is −35 to −40 ppm, the thermal expansion of a 3 K rise; a 10 K rise strains the particle almost four times as much ([magnetostriction](../library/magnetostriction.md)).
- Nickel is soft (*K*<sub>1</sub> = −5 kJ/m³), and an open body keeps remanence only if its coercivity exceeds its demagnetizing field ([ferromagnetic-hysteresis](../library/ferromagnetic-hysteresis.md)). Its tabulated blocking diameter (34 nm) is above its single-domain diameter (31 nm), so no sprayable Ni powder is a single stable latch cell ([superparamagnetism](../library/superparamagnetism.md), [magnetic-domains](../library/magnetic-domains.md)).

**What it can be.** The soft control for §3.6: the same shot and readout (VSM or powder pattern) on a powder expected to keep little remanence. The earlier Ni-against-Pd comparison is removed; Pd has no ferromagnetic order to compare.

**Tune.** Keep well below Ni *T*<sub>C</sub> (628–631 K, about 355 °C). Above it there is nothing to read.

### 3.4 Steel or Ti + H-rich carrier — [hydrogen-embrittlement](hydrogen-embrittlement.md)

**What.** High-strength steel or Ti with an oil or glycerol-type carrier against a dry one.

**Question.** Did the process leave hydrogen in the deposit above what a bake removes?

**Library.** Embrittlement needs a hydrogen content above a critical level together with sufficient stress; 5 wt ppm lowers the tensile strength of one martensitic steel, and 200 °C for 10 min removed production hydrogen from one hot-stamped steel ([hydrogen-in-metals](../library/hydrogen-in-metals.md)). The values depend on the alloy.

**Tune.** Carrier off hydrogen (isoparaffinic, dry gas) against on (glycerol, moisture). Post-spray bake as erase. Compare toughness and delayed cracking, and measure hydrogen content if possible.

**Would contradict the warning.** Deposits from dry and H-rich carriers equally tough, with no effect of a bake.

### 3.5 Hydride-forming powder — [hydride-storage](hydride-storage.md)

**What.** Pd or a storage alloy as feedstock, then a Sieverts or residual-H measurement. Nickel is not a hydride former at these pressures: its hydride forms above 6 kbar, and H/Ni is 1.8 × 10⁻⁵ at 1 bar and 298 K.

**Question.** Does impact leave trapped hydrogen that a designed *P*–*T* swing does not give back?

**Tune.** Shot count up; a bake column to erase.

### 3.6 Hard-magnet deposit — [bonded-magnets](bonded-magnets.md)

**What.** NdFeB or hard-ferrite powder, optionally with *B* on during flight or on the substrate.

**Question.** How much remanence and coercivity does the deposit keep, against impact velocity? The earlier question (“is *KV* still on the blocked side?”) does not apply: the thermal-stability size of Nd₂Fe₁₄B is about 3.5 nm, far below any powder grain, and what limits a real magnet is coercivity, a microstructure property ([permanent-magnet-latch](../library/permanent-magnet-latch.md)).

**Library.** Shock demagnetizes sintered Nd-Fe-B at 6–7 GPa by fracture between grains, with coercivity recoverable by annealing. No impact pressure is sourced for this head's velocities, so the velocity at which this sets in is open.

**Tune.** Impact velocity down until remanence survives; alignment field on for a magnet, off for a control; Ni (§3.3) as the soft control.

**Would contradict the plan.** No velocity at which the powder both bonds and keeps useful coercivity.

### 3.7 Contained coil cell (no rails) — [EM-LENR](EM-LENR.md) Phase 0–3

**What.** The ¼″ cell and ⅜″ coil already specified. Powder stays in. The same driver family used as a repetitive writer.

**Question.** Does pulsing change a measurable hydrogen state (a thermal desorption peak, or the Pd hydride hysteresis), with no nuclear search?

**Tune.** Follow [EM-LENR](EM-LENR.md) §§5–6. Pd first. Plasma off. Repeat the readout with the coil dark.

Steven owns whether that state is the LENR configuration. You own whether the coil writes something that bake-out can erase.

### 3.8 Breakdown map of the barrel gas — [dielectric-breakdown](../library/dielectric-breakdown.md)

**What.** Controlled fill (air, N₂, H₂, oil vapor) at known gap, pressure and voltage, no powder. Use the actual rail metal and finish: the Paschen minimum depends on the cathode. The launch bank cannot do this; it sits below the Paschen floor (§2.4). The map needs a separate source of several hundred volts.

**Question.** Where is the breakdown threshold for this geometry, and does any voltage in a real shot reach it? The second half is read on the muzzle and bus taps during powder shots.

**Tune.** Pressure both ways. At 1 atm every mm-scale barrel gap is far to the right of the minimum, which sits at 7–9 µm in air and N₂ and 14–15 µm in H₂; a 1 mm air gap reaches it near 5.5–5.7 torr. Expect H₂ to hold about 0.6 of the air field; oil vapor has no sourced ratio, so measure it. Pulse length is not a gas knob at these durations.

This map covers the gas route only. An arc started by a contact that parts under current is a contact event and needs powder shots to map.

**Would contradict §2.4.** A gas breakdown in the barrel with every recorded voltage below the measured floor.

---

## 4. Combined isolation sequence (device-first)

Run as **device campaigns**.

| Campaign | Shots | What it gives |
|---|---|---|
| A. Driver into shorted rails | no powder | *L*′, loop resistance, EMI and heat baseline |
| B. Slug resistance | conditioning, then motion | Whether a conditioned slug stays in the §2.2 window |
| C. Cu / oil → metal | velocity / *I* series, muzzle voltage logged | Bond window against melt; contact state |
| D. Exploding foil or wire → glass | thickness series | dc percolation step; smooth *R*/*T* |
| E. Ni, then hard-magnet powder | velocity, alignment field | Remanence and coercivity kept (Ni as soft control) |
| F. Steel + H-rich vs dry carrier → part | bake column | Embrittlement write/erase |
| G. Breakdown map, no powder, separate HV source | *P*, gap, gas | Gas route as a known factor |
| H. Coil cell, Pd, H₂ | per EM-LENR | Hydrogen state written or not |
| I. Only then: D₂, neutrons, calorimetry | EM-LENR Phase 5 | Search, not isolation |

A–C are manufacturing. D–H are experiments the same hardware can run. I waits on Steven for interpretation.

---

## 5. Falsifiers (device-level)

These are results that would contradict the plan in §2. Results that standard physics already fixes are not listed.

- A conditioned Cu slug whose resistance, measured after it has moved, is back in the megohm state (the conditioning step does not survive motion).
- A slug with measured resistance inside the §2.2 window that still arrives molten (the uniform-current heat budget fails, for instance through current crowding at the rear).
- A paste slug that does not bond at or above the sourced powder critical velocity for its metal (the assumption that a large, warm body bonds at a lower velocity than a 20 µm particle fails).
- Shots that stay below the 50 V muzzle convention and shots that jump above it are calorimetrically identical after *R*∫*I*²*dt* is subtracted (then “plasma off” is not a separable state here).
- Cu-on-glass sheet resistance shows no step at any deposited thickness.
- Steel deposits from dry and H-rich carriers are equally tough, and a bake does nothing.
- No impact velocity at which a hard-magnet powder both bonds and keeps useful coercivity.

Removed on 2026-11-14 because standard physics answers them: “pulse width does not change the rail-face against bulk heating split” (magnetic diffusion), and “Ni and Pd are indistinguishable on remanence” (Pd is not ferromagnetic). None of the list is a LENR falsifier.

---

## 6. What this file is not

- Not a KiCad driver design ([`AGENTS.md`](../../em-csam/AGENTS.md) still owns that).  
- Not a substitute for [EM-LENR](EM-LENR.md).  
- Not a claim that rail erosion, skin, or magnetostriction are new physics. They are the library applied to a head you are actually building.
