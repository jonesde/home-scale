# EM-CSAM Micro-Railgun Deposition – Technical Concept Document
Version 0.3 – Engineering Overview

**What changed in 0.3.** The file had accidentally been saved with several copies of itself interleaved; those are removed. Section 3 is rebuilt around a shot budget (action, charge, energy), a realistic inductance gradient, the slug-resistance window, magnetic augmentation and the exit-current rule. Section 2 gains a regime map. The reasons and sources are in [`DesignReview-2026-11.md`](DesignReview-2026-11.md); source IDs resolve in [`References.md`](References.md). Numbers come from [`tools/shot_model.py`](tools/shot_model.py) (`python3 em-csam/tools/shot_model.py tables`) and are **not measured**.

## 1. Introduction and Intended Applications

Electromagnetic Cold Spray Additive Manufacturing (EM-CSAM) uses a miniature parallel-rail linear accelerator (micro-railgun) to accelerate metered volumes of metal powder suspended in a carrier fluid. The goal is controlled deposition of metal for additive manufacturing, repair, and specialized coating processes.

Unlike conventional large-scale railguns optimized for hypervelocity kinetic projectiles, the micro-scale version is designed for short barrels (≈100 mm or less), modest velocities (typically 200–800 m/s depending on material), and precise metering of feedstock. The same Lorentz-force acceleration mechanism is retained, but the operating regime, thermal management, and success criteria are inverted to serve manufacturing rather than weapon or launch applications.

### Primary Use Cases
- Local and hobby-scale metal additive manufacturing with equipment that can be built and maintained by serious makers and small shops.
- Industrial processes that benefit from metallurgy compatible with existing powder-metallurgy or thermal-spray practice, while accepting lower overall energy efficiency in exchange for geometric flexibility, multi-material capability, or reduced thermal distortion of the substrate.
- Research platform for studying high-current powder consolidation, carrier-mediated shielding, and rail–powder interactions.

### Example Material Systems
Early development prioritizes combinations that balance process robustness, safety, and useful metallurgy. The current list, with the reasons, is in [`PowderCarrierRailMaterial.md`](PowderCarrierRailMaterial.md). In short:

- **Tin or solder paste**, copper rails — lowest bonding velocity; proves feed, conduction and launch.
- **Zinc powder**, copper rails — bonds at 360–380 m/s; useful deposit.
- **Copper powder**, copper rails — the main target; needs the most velocity of the three.

More demanding targets (aluminium–silicon, iron, titanium, chromium-carbide hard-facing, copper–graphene) remain later steps.

## 2. Parallel-Rail Linear Accelerator Mechanics – Micro vs Macro

A parallel-rail accelerator consists of two conductive rails and a conductive armature (in this case a metered slug) that closes the circuit. Current flowing down one rail, through the armature, and back the other rail produces a magnetic field; the interaction of that field with the current in the armature generates a Lorentz force that accelerates the armature along the rails.

Key physical principles:
- Ampère’s law and the Biot–Savart relation for the magnetic field produced by the rail currents.
- The Lorentz force on a current-carrying conductor in a magnetic field.
- Conservation of energy and the conversion of stored electrical energy into kinetic energy plus losses (ohmic heating, contact resistance, friction, armature deformation).
- Inductance gradient of the rail pair, which determines force for a given current.

### 2.1 Critical Differences at Micro Scale
Large railguns are typically designed for multi-kilogram projectiles, multi-meter barrels, peak currents of hundreds of kiloamperes to megamperes, and velocities of 2 km/s or higher. They contend with extreme rail erosion, plasma armature management, enormous structural loads, and pulsed-power systems of corresponding scale.

At the 0.5 mm-class bore and ≈100 mm barrel lengths considered here the situation changes:

- **Current** scales down to roughly 1–4 kA. **Stored energy does not scale down as far**: tens of joules per shot are needed, because efficiency at these velocities is a fraction of a percent (§3.4).
- **Armature state** can remain solid, partially molten, or a dense powder compact rather than a fully developed plasma. Which one occurs is set by the slug's electrical resistance (§3.5), not by intent alone.
- **The rails' own magnetic field is weak.** At 2 kA it is equivalent to about 0.8 T across the gap. A permanent magnet can match it, which is not true at any larger scale (§3.6).
- **Thermal and erosion management** remain important but occur on a scale that can be addressed with replaceable rail inserts and moderate cooling.
- **Precision and metering** become first-order requirements. The “projectile” is a small, repeatable volume whose mass, conductivity, and rheology are process variables.

### 2.2 Turning Classical Weaknesses into Process Advantages
Several phenomena that are problems for kinetic-launch railguns become useful or at least manageable in a deposition context:

- **Rail erosion** injects rail material into the deposit. This can be treated as contamination or as a deliberate alloying/hard-facing mechanism.
- **Contact arcing and local melting** can assist oxide disruption and inter-particle bonding when properly controlled.
- **Short acceleration length** limits maximum velocity but also limits the time available for unwanted side reactions and keeps the mechanical package compact enough for a moving toolhead.
- **Sensitivity to armature conductivity and mass** becomes a process control lever: slurry formulation, preconditioning, and pulse shaping directly influence deposit quality.

### 2.3 What the device is

The micro-railgun is best understood as a high-current, short-pulse powder consolidation and acceleration device rather than a scaled-down ordnance launcher.

### 2.4 Three regimes, not one process

Earlier notes described "solid, partially molten, or a dense powder compact" as one continuum. They are three different processes with different products, and a given shot lands in one of them according to the slug's resistance and whether the carrier flashes.

| Regime | What moves the metal | What lands | Needs |
|---|---|---|---|
| **Solid slug** | Lorentz force on a conducting compact | One warm slug at 100–600 m/s | Slug at or below a few tenths of a milliohm (§3.5); a slug that slides rather than smears (§3.8) |
| **Carrier flash** | Pressure of the vaporising carrier; Lorentz force secondary | A spray of particles dragged by hot gas | A closed breech; vapor generated behind or within the charge |
| **Exploding slug** | The metal itself boils | Vapor and fine droplets; thin films, nanoparticles | Slug resistance in the milliohm-to-ohm range |

- **Carrier flash (estimate):** about 0.1 J vaporises the oil in a 0.25 mm³ slug. Its pressure gives 0.6–6 N on this bore, against 0.45–2.5 N of Lorentz force in §3.3. Whenever the carrier flashes, the device is at least partly an electrothermal gun.
- **Prior art lives in the last two regimes.** The UT-CEM process drags powder with a railgun-driven gas column ([PA-EPD](https://patents.google.com/patent/US6329025B1/en)); the Tamura group's process explodes a powder column on purpose ([PA-ELTEPS](https://link.springer.com/article/10.1361/105996302770349032)). The solid-slug regime at this scale is the part that looks new.
- The rest of this section's mathematics describes the **solid-slug** regime. The other two need their own experiments ([`TestPlan.md`](TestPlan.md), T5).

## 3. First-Order Performance Calculations (0.5 mm Class)

### 3.1 Governing Relations

The force on the armature is related to the current and the inductance gradient of the rail pair:

\[
F = \frac{1}{2} L' I^{2}
\]

where
- \(F\) is the accelerating force (N),
- \(L'\) is the inductance gradient (H/m),
- \(I\) is the current (A).

Under the constant-acceleration approximation for a barrel of length \(s\):

\[
a = \frac{v^{2}}{2s}, \quad F = m a, \quad t = \frac{2s}{v}, \quad I = \sqrt{\frac{2 m a}{L'}}, \quad KE = \frac{1}{2} m v^{2}
\]

where \(v\) is muzzle velocity, \(m\) is armature mass, and \(t\) is acceleration time.

### 3.2 The inductance gradient

Version 0.2 used \(L' = 0.6\,\mu\text{H/m}\). For this geometry that is optimistic. The rails are flat strips lying side by side with a 0.5 mm gap between their edges, not the square bore the usual figures describe.

| Estimate | L′, µH/m |
|---|---|
| Thin coplanar strips, 2 / 4 / 8 mm wide | 0.55 / 0.47 / 0.40 |
| Kerrisk high-frequency fit, 2 / 4 / 8 mm wide, 0.5 mm high ([RG-KERRISK82](https://www.osti.gov/servlets/purl/5222337)) | 0.37 / 0.33 / 0.28 |
| Flux that actually crosses the gap, current spread 0.5 / 1 / 2 mm into the rail | 0.55 / 0.38 / 0.25 |

- **Planning value: 0.4 µH/m, range 0.3–0.5.** Current scales as \(1/\sqrt{L'}\), so 0.4 instead of 0.6 means 22 % more current.
- **Why no formula settles it.** Thin rails are transparent to flux, so only the flux crossing the gap pushes the slug; the rest pushes on rail metal. How far the current has spread into the rail depends on pulse length and, behind a moving slug, on velocity.
- **Geometry lever.** A single 0.5 ms pulse diffuses into copper with an error-function profile, not to an edge: the depth is 2.1 mm, 3.3 mm or 5.2 mm depending on the cut used (0.8, 1.27 or 2 times √(Dt); the 1/e point is 3.3 mm), and after 0.2–0.7 ms the field at 3 mm is still 20–49 % of its surface value ([EM-MORITZ11](https://arxiv.org/abs/1103.1800); [skin-effect](../quantum-systems/library/skin-effect.md)). The earlier "about 2 mm" was the steady 1 kHz skin depth, the smallest of these. So rails wider than 3–4 mm lower L′ but are not idle: they still carry part of the pulse and run cooler. Right behind the moving slug the current is confined much more tightly than that: the velocity skin depth 2√(D·a/V) for a 1 mm slug is about 0.73 mm at 100 m/s and 0.33 mm at 500 m/s in copper, whatever the pulse length (model formula, [RG-WOODS96](https://apps.dtic.mil/sti/tr/pdf/ADA320642.pdf); no direct measurement opened). (Corrected 2026-11-12; this bullet used to say wider rails carry no more pulse current.)
- **Measure it.** An LCR meter with a sliding short gives the low-current value; a velocity fit against ∫I²dt gives the working one ([`TestPlan.md`](TestPlan.md), T0 and T3).

### 3.3 Reference Case – 0.5 mm × 0.5 mm Bore, 100 mm Barrel

**Geometry**
- Bore: 0.5 mm × 0.5 mm
- Barrel length \(s = 100\,\text{mm}\)
- Example metered volume: 0.5 mm × 0.5 mm × 1.0 mm = 0.25 mm³

**Mass estimates**
- Solid density ≈ 8000 kg/m³ → \(m \approx 2.0\,\text{mg}\)
- Practical slurry (40–60 % metal by volume) → 0.8–1.5 mg for the same volume
- Shorter slugs of 0.25–0.5 mg are the practical range for the first driver (§3.9)

**Constant-current results, 2 mg slug**

| Target velocity | Force | Current at L′ = 0.6 (v0.2) | Current at L′ = 0.4 | Time | Kinetic energy | Charge |
|---|---|---|---|---|---|---|
| 300 m/s | 0.90 N | 1.7 kA | 2.1 kA | 0.67 ms | 90 mJ | 1.15–1.41 C |
| 500 m/s | 2.5 N | 2.9 kA | 3.5 kA | 0.40 ms | 250 mJ | 1.15–1.41 C |
| 800 m/s | 6.4 N | 4.6 kA | 5.7 kA | 0.25 ms | 640 mJ | 1.15–1.41 C |

Current scales with \(\sqrt{m}\): a 1 mg slug needs 71 % of these figures and a 0.25 mg slug 35 %.

### 3.4 Shot budget: action, charge and energy

Three quantities follow from momentum and do not depend on how the pulse is shaped.

**Action.** Because force goes as I², the momentum fixes the time-integral of I²:

\[
\int I^{2}\,dt = \frac{2 m v}{L'}
\]

**Charge.** For a constant-current shot the charge drawn is independent of velocity:

\[
Q = I\,t = 2\sqrt{\frac{m\,s}{L'}}
\]

| Slug | L′ | Charge needed |
|---|---|---|
| 2 mg | 0.6 µH/m | 1.15 C |
| 1 mg | 0.4 µH/m | 1.00 C |
| 0.5 mg | 0.4 µH/m | 0.71 C |
| 0.25 mg | 0.4 µH/m | 0.50 C |

**Energy.** Every milliohm in the loop dissipates R·∫I²dt:

| Slug, velocity | Action | Loss at 10 mΩ | Loss at 20 mΩ | Kinetic energy | Efficiency |
|---|---|---|---|---|---|
| 1 mg, 300 m/s | 1500 A²s | 15 J | 30 J | 45 mJ | 0.15–0.30 % |
| 2 mg, 300 m/s | 3000 A²s | 30 J | 60 J | 90 mJ | 0.15–0.30 % |
| 2 mg, 500 m/s | 5000 A²s | 50 J | 100 J | 250 mJ | 0.25–0.50 % |
| 0.25 mg, 400 m/s | 500 A²s | 5 J | 10 J | 20 mJ | 0.20–0.40 % |

- **Whole-shot efficiency is about \(L'v/(4R)\).** The motional impedance \(\tfrac12 L'v\) is 0.06–0.2 mΩ at these velocities, and everything else in the loop is ten to a hundred times larger. Poor efficiency at low velocity is a general railgun result ([RG-MCNAB03](https://research.lifeboat.com/ieee.em.pdf)).
- **Correction to v0.2.** It said kinetic energy is "well under 1 J", so "banks of a few tens of joules are therefore ample". The kinetic energy is small; the electrical energy per shot is tens of joules, and the bank has to hold about a coulomb.
- **Levers:** a lighter slug, a lower loop resistance (more cans in parallel, more FETs, shorter rails), and more force per amp (§3.6).

### 3.5 Slug heating and the resistance window

The slug carries the full current. Its Joule heat per kilogram is

\[
e = \frac{R_\text{slug}}{m}\int I^{2}\,dt = \frac{2\,R_\text{slug}\,v}{L' + 2M'}
\]

where \(M'\) is any augmenting coupling (§3.6). Velocity and temperature are locked together, and barrel length does not appear: a shorter barrel needs more current for less time and the same action.

**What "conductive enough" means.** Model result for a 0.5 mg slug (six cans at 18 V, magnet):

| Slug resistance | Joule heat | State on arrival | Velocity |
|---|---|---|---|
| 0.2 mΩ | 0.21 MJ/kg | solid | 336 m/s |
| 0.5 mΩ | 0.50 MJ/kg | melting | 327 m/s |
| 1 mΩ | 0.94 MJ/kg | molten | 313 m/s |
| 2–5 mΩ | 1.7–3.3 MJ/kg | boiling | 290–244 m/s |
| ≥20 mΩ | >6 MJ/kg | vapor | <165 m/s |

- A solid copper slug of this size is about 0.02 mΩ. The launchable window is roughly 10–20× bulk resistivity: a sintered compact, or one pressed and then reduced, not a paste. Pressing alone does not get there: a pressed, unreduced copper compact measured 10⁴–10⁵ Ω·m, and reduction brought it to at most 60–600× bulk ([electrical-resistivity](../quantum-systems/library/electrical-resistivity.md)).
- **Powder in oil is high-resistance until its contacts break down** (corrected 2026-11-12). Two steps are involved and they are different physics ([electrical-contacts](../quantum-systems/library/electrical-contacts.md)). First the surface films puncture, a field effect of about 10⁷–10⁸ V/m in the film. Then the contact spots heat until they micro-weld, which limits the voltage across each contact.
  - *Bead chains.* A chain of oxidised metal beads measures 10⁴–10⁷ Ω at low current (force-dependent), then drops to a few ohms and holds a fixed voltage per contact while the spots reach about 1050 °C: 0.4 V for stainless steel, 0.3 V for brass, 0.2 V for bronze. Copper was not measured ([PC-FALCON05](https://ar5iv.labs.arxiv.org/html/cond-mat/0407773)). The plateau is the neck-growth regime itself, not a stage before it. With 10–20 contacts across 0.5 mm that is 2–8 V.
  - *A real copper powder bed* behaves differently. A 0.50 mm bed of 87.5 µm copper powder with a thick (1200 nm) oxide sat near 10⁸ Ω, climbed to 33 V with no plateau, then collapsed by five orders of magnitude at about 0.4 mA. The breakdown field fell with compaction, from 57 kV/m unloaded to 18 kV/m at 300 MPa (28 V down to 9 V across 0.5 mm). The welded bridges were 10–15 µm and weak: a mechanical shock returned the bed to high resistance ([PC-ALIOUAT22](https://doi.org/10.3390/ma15124096)).
  - No opened source covers powder in oil, a thin native oxide, or a moving slug. Treat 2–8 V as the bead-chain figure and expect the threshold for the actual paste to be set by its oxide and compaction; measure it on the T0 fixture.
- Preconditioning therefore has one job: take the slug from megohms to "a few tenths of a milliohm" without exploding it on the way, and keep it there until launch (the bridges are fragile). See [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) §4 and [`PowderCarrierRailMaterial.md`](PowderCarrierRailMaterial.md).

**Action margin by material.** For a solid slug 1 mm long, the velocity at which Joule heating reaches melt onset, against the cold-spray critical velocity:

| Material | Melt onset, m/s per mm of slug | Critical velocity, m/s | Margin |
|---|---|---|---|
| Copper | ~2000 | 460–500 | 4.2 |
| Aluminium | ~2080 | 620–660 | 3.3 |
| Zinc | ~350 | 360–380 | 0.9 |
| Iron | ~370 | 700–750 (316L) | 0.5 |
| Tin | ~50 | 160–180 | 0.3 |

Action values from [RG-TUCKER75](https://www.osti.gov/servlets/purl/4229184-1IbmTb/) (disputed by one later paper; treat as ±tens of percent). Windows from [CS-SCHMIDT09](https://www.researchgate.net/figure/alues-of-critical-velocity-for-bonding-assuming-a-particle-size-of-20-lm-Material-Melting_tbl1_225516724).

- Copper and aluminium have room. Iron and tin melt before they reach a bonding velocity, which is the old README's point about steel.

- **Read the table with these qualifiers (added 2026-11-14; detail and arithmetic in [`quantum-systems/application/EM-CSAM.md`](../quantum-systems/application/EM-CSAM.md) §2.2–§2.4).**
  - The table is computed at L′ = 0.45 µH/m. At the planning value of 0.4 used elsewhere in these notes, copper melt onset is about 1800 m/s per mm of slug (1350–2250 over L′ = 0.3–0.5) and aluminium about 1870.
  - The copper window of 460–500 m/s is a tabulated 20 µm value. The one measured critical velocity opened for copper powder is 570 m/s; against that the copper margin is about 3.1–3.2, not 4.2.
  - Iron is compared with the 316L window because no critical velocity for iron or carbon steel is sourced. Nickel has none either. The zinc and tin windows and action values come from one table and one report that could not be re-opened; they are the least-supported rows, and they are the first two rungs of the test ladder.
  - By enthalpy, copper tolerates a slug resistance of 0.19–0.31 mΩ at 500–300 m/s before melt onset, 11–19 times the 0.017 mΩ solid slug. No sourced copper compact reaches that window without sintering or reduction.
- A porous slug divides the margin by its resistivity ratio. Augmentation multiplies it by \((L'+2M')/L'\).
- A hot, large body bonds at a lower velocity than a cold 20 µm particle ([CS-MORIDI14](https://re.public.polimi.it/bitstream/11311/968457/4/Cold%20spray%20coating_11311-968457_Guagliano_1.pdf), [CS-DOWDING20](https://www.osti.gov/servlets/purl/1658603)), so some Joule heat is useful. By the Schmidt formula copper falls from about 485 m/s cold to about 340 m/s at 550 °C (indicative).

### 3.6 Magnetic augmentation

At this scale the rails' own field is weak enough that an external field competes with it. That is the largest single lever the earlier notes did not have.

**Permanent magnets** above and below the bore, magnetised through the rail plane:

\[
F = \tfrac12 L' I^{2} + B\,I\,g
\]

with \(g\) the gap. At 0.8 T and 0.5 mm that is 0.4 mN per amp. The literature notes that such augmentation helps "especially in low current railguns" ([RG-ASGARI19](https://www.aemjournal.org/index.php/AEM/article/download/961/443/4084)).

**Series augmenting turns** laid flat over and under the rails, carrying the launch current in the same sense as the rail beneath ([RG-GALLANT02](https://researchportal.rma.ac.be/ws/portalfiles/portal/8004700/ParallelAugmentedRailguns.pdf)):

\[
F = \left(\tfrac12 L' + M'\right) I^{2}
\]

Because the gap is narrow, each turn-pair couples only a little:

| Height of the turn above the bore plane | M′ per turn-pair |
|---|---|
| 0.5 mm | 0.10 µH/m |
| 1.0 mm | 0.07 µH/m |
| 1.5 mm | 0.05 µH/m |
| 3.0 mm | 0.03 µH/m |

Eight turns give about 0.35 µH/m and add about 2.6 µH and 6 mΩ. The estimate treats the rails as transparent to flux; rails that exclude it would do better.

**Model results** (six cans, four FETs per leg, idealised):

| Configuration | 1 mg | 0.5 mg |
|---|---|---|
| 18 V, 1 µH, plain | 106 m/s | 207 m/s |
| 18 V, 1 µH, 0.8 T magnet | 139 m/s | 336 m/s |
| 22 V, 8 augmenting turns | 238 m/s at 1.0 kA | — |
| 22 V, 8 turns + magnet | 320 m/s at 1.0 kA | 526 m/s |

**Consequences**
- Expect roughly 1.5–1.9× velocity, more for light slugs.
- Augmenting turns lower the current needed, which is what limits the first driver.
- The magnet force is linear in current while heating is quadratic, so pulse shape can trade arrival temperature against velocity. A plain railgun cannot (§3.5): on plain rails the slug's action at a given velocity is 2mv/L′ whatever the pulse width.
- **Where a plasma can start (added 2026-11-14).** The 18–55 V bank is 6–20 times below the Paschen minimum for air (327–352 V), so it cannot start a gas avalanche across the bore at any gap. It is above the 12–15 V minimum arc voltage of the common contact metals, so an arc starts at a parting or poor contact, or from the induced voltage when current is interrupted. A plasma armature across a 0.5 mm bore would need roughly 50 V by the measured electrode falls. Sources: [dielectric-breakdown](../quantum-systems/library/dielectric-breakdown.md), [electrical-contacts](../quantum-systems/library/electrical-contacts.md).
- A magnet also pushes on conditioning current: 5 A is 2 mN, about 200 g on a 1 mg slug. The first ~20 mm of barrel stays magnet-free ([`RailgunHeadPrototype.md`](RailgunHeadPrototype.md)).

### 3.7 The current must end before the slug leaves

If the slug exits with current still flowing, the stored energy \(\tfrac12 L I^{2}\) has nowhere to go but an arc at the muzzle, aimed at the deposit.

| Case (model) | Exit current | Energy behind it | Kinetic energy |
|---|---|---|---|
| 18 V, magnet, 0.5 mg | 0.16 kA | 0.01 J | 0.03 J |
| 18 V, magnet, 0.25 mg | 0.60 kA | 0.19 J | 0.05 J |
| 22 V, 8 turns + magnet, 0.5 mg | 0.70 kA | 0.66 J | 0.07 J |
| 55 V, magnet, 1 mg, 8+8 FETs | 2.9 kA | 4.4 J | 0.38 J |

- **Rule:** choose bank, inductance and voltage so the current has decayed before exit. The script prints both columns.
- The freewheel tail lasts about L/R, so a large series inductance, including augmenting turns, lengthens it. That is the price of augmentation.
- A muzzle shunt is the established alternative ([RG-MUZZLE](References.md#2-railgun-physics-and-augmentation)).

### 3.8 Wall drag and barrel length

A liquid plug will not cross 100 mm of 0.5 mm bore intact (estimates):

| Paste viscosity at shear | Wall drag at 300 m/s | Compare |
|---|---|---|
| 0.01 Pa·s | 0.07 N | Drive force 0.45–2.5 N |
| 0.1 Pa·s | 0.7 N | |
| 1 Pa·s | 7 N | |

A film only 2 µm thick over the whole bore holds 0.4 mm³, more than the 0.25 mm³ slug.

- The slug has to behave as a solid by the time it moves, or travel as a spray (§2.4).
- **Barrel length is a free parameter for heating** (§3.5) but not for drag, fouling or rail resistance. A 30–50 mm barrel needs more current for less time and is worth testing. With a magnet, length helps: the magnet term's heating falls as \(1/\text{length}\).

### 3.9 Implications for Driver Design

- **Pulse:** one unipolar pulse of 0.2–0.7 ms. The bank and a series inductor of 0.5–3 µH form it naturally, at 0.7–4 kHz. A ≥200 kHz launch gives no skin effect in the slug and several times more heating in the rails ([`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) §3).
- **Current:** 1–4 kA for the reference case. Four TO-247 FETs per leg carry about 1.4 kA, so the first driver works with slugs of 0.25–0.5 mg, or with augmentation.
- **Charge and energy:** about 1 C and tens of joules per shot. Capacitor ESR is half the loop.
- **Low parasitic inductance** in the capacitor–switch loop still matters, for the turn-off voltage rather than for rise time.
- **Preconditioning** is a current-limited sintering step with slug resistance as its measured endpoint (§3.5).

### 3.10 Diagnostics

None of the above can be trusted without measurement. The minimum set:

- **Launch current** from a Rogowski loop on the return bar.
- **Slug voltage** from a differential tap at the *muzzle* end of the rails. It reads the slug alone: no rail drop and no inductive term, during conditioning and in flight. A few volts means solid contact; tens of volts means an arc.
- **Velocity** from two photogates or break-wires a known distance apart, cross-checked by a small ballistic pendulum.
- **Bank voltage** before and after, for charge.

Details and procedures are in [`TestPlan.md`](TestPlan.md).

## 4. Scaling Considerations

### 4.1 Larger Bore Size
Increasing bore cross-section raises the metered mass roughly with area (or volume if pellet length is also scaled). Because \(I \propto \sqrt{m}\), current rises with the square root of mass. A 1 mm × 1 mm bore with proportionally larger metered volume can require multi-kiloampere to tens-of-kiloampere pulses.

Consequences:
- Higher peak current and greater rail heating/erosion.
- Larger mechanical loads on the barrel structure.
- Reduced spatial resolution of the deposited feature.
- More demanding pulsed-power and cooling design.
- Permanent-magnet augmentation loses value as the rails' own field grows with current.

Larger bores trade precision and toolhead compactness for deposition rate. They remain useful for bulk fill or lower-resolution work but move the technology away from the fine-feature regime that motivates the 0.5 mm class.

### 4.2 Multiple Railgun Heads (Arrays)
An array of micro-railgun heads on a shared or modular toolplate enables:
- Higher area coverage rate.
- Multi-material deposition (different powder/carrier/rail combinations per head).
- Redundancy and selective firing.

System-level topology questions include:
- Independent capacitor banks and switches per head versus shared DC bus with local energy storage.
- Coordination of firing sequences to manage peak power demand and mechanical reaction forces.
- Powder feed architecture (individual metering versus shared distribution with valving).
- Thermal and electrical isolation between adjacent heads.
- Control integration with the motion platform (timing relative to toolpath, interleaving of preconditioning and launch pulses).

A practical near-term architecture keeps a local low-inductance capacitor + switch module with each head, charged from a common DC bus, while the motion controller sequences fire commands. This preserves pulse fidelity while allowing scalable power distribution.

### 4.3 Material Feeding and Firing Rate (Single Barrel)
Deposition rate for a single barrel is the product of:
- Metered mass (or volume) per shot,
- Firing frequency,
- Duty cycle limited by rail heating, capacitor recharge, and slurry feed rate.

Limits arise from:
- Thermal recovery of the rails and barrel structure.
- Time required to meter and precondition the next slug.
- Capacitor recharge, capacitor heating, and switch cooling.
- Mechanical stability of the toolhead under repeated reaction forces.

Early systems will operate at low duty cycle (a few shots per second or less) while process stability is established. At tens of joules per shot, ten shots a second is a few hundred watts, most of it dissipated in the capacitors and rails. Standard aluminium electrolytics are not rated for rapid, frequent discharge ([DS-LGU-GUIDE](https://www.mouser.lt/pdfDocs/nichicon-gxc-app-guidelines.pdf)), so sustained rates need pulse-rated capacitors as well as cooling and a faster feed.

---

**Document status**
Version 0.3 replaces the calculations of 0.2 for engineering purposes. It uses a realistic inductance gradient, adds the action, charge and energy budget, states the slug-resistance window that separates launching from exploding, and adds magnetic augmentation and the exit-current rule. Everything quantitative here is a first-order model awaiting the measurements in [`TestPlan.md`](TestPlan.md).
