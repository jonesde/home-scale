# EM-CSAM Design Review – November 2026

A review of the whole `em-csam/` folder: the concept, the micro-railgun mechanics, the Unified Resonant driver, and the metallurgy and chemistry. It records what was found, the numbers behind each finding, and where each one was fixed in the other documents.

**Status of every number here.** Nothing in this review was measured. The findings rest on reading the documents, on manufacturer datasheets, on published literature, and on a first-order model ([`tools/shot_model.py`](tools/shot_model.py)). Sources are cited by ID as links; the IDs resolve in [`References.md`](References.md). Assumptions are listed in §9 with the measurement that would overturn each.

---

## 1. Summary

1. **The driver as documented does not resonate at 200 kHz.** It has a stiff DC bus and no series capacitor, so a "≥200 kHz launch burst" is a hundred or more hard-switched kiloamp commutations per shot. High frequency also gives no skin effect in a slurry slug and several times more heating in the rails.
2. **The same parts suit a different pulse.** The electrolytic bank and `L_series` form a damped discharge with a natural frequency of 0.7–4 kHz and a length of 0.2–0.7 ms, which is the transit time the kinematics need. The driver is re-baselined to one unipolar pulse per shot.
3. **Charge, capacitor ESR and FET heating set the limits.** A shot needs about 1 C whatever the velocity; two cans hold half of that. Four FETs per leg carry about 1.4 kA, not the 2.7 kA their pulse rating suggests.
4. **Energy per shot is tens of joules.** Efficiency is 0.1–0.5 %, because the motional impedance of a slow slug is a fraction of a milliohm and everything else in the loop is larger.
5. **Slug resistance decides everything.** Powder in oil is high-resistance (megohms) until the particle contacts break down. A slug has to be at or below a few tenths of a milliohm to launch as a solid; at a few milliohms it boils.
6. **Magnetic augmentation was missing.** At this scale a permanent magnet's field is comparable to the rails' own. Magnets, and a few series turns laid over the rails, are worth roughly 1.5–1.9× in velocity and matter most when FET current is the cap.
7. **Three different processes were described as one.** A solid slug thrown by Lorentz force, a spray driven by the flashing carrier, and an exploding slug are different regimes with different products.
8. **Materials.** Copper rails first, not aluminium. PEI and PEEK are poor arc-facing bore walls. Carrier choice should start from conductivity, and metallic or self-reducing carriers were not on the list.
9. **What the kit on hand should reach.** With six cans, four FETs per leg and a 0–30 V supply: the tin and zinc bonding windows with 1 mg slugs, and the copper window only with slugs of 0.5 mg or less, or with more FETs and voltage (§7).

---

## 2. Scope and method

**Read in full:** every Markdown file in `em-csam/`, plus `quantum-systems/application/EM-CSAM.md` and `EM-CSAM-Pitch.md`.

**Checked against sources:** all driver part numbers against manufacturer datasheets; the railgun physics, prior art, cold-spray windows, powder conduction, carrier chemistry and materials against published work.

**Modelled:** capacitor bank → switch → series inductor → rails → moving slug, with resistive losses, back-EMF, optional magnet field and augmenting turns, freewheel through the low-side diodes, and Joule heating of the slug. The model is idealised: a rigid slug of fixed resistance, no friction, no wall drag, no vapor pressure.

**Second opinion:** an independent reviewer re-derived the circuit behaviour from the documents and criticised a first draft of the recommendations. Several corrections below (A6, A7, A13, the on-time limiter, the first-light voltage ceiling) come from that pass.

---

## 3. Driver findings

### A1. There is no 200 kHz resonance in the circuit as drawn

- **Documents say:** "short ≥200 kHz resonant launch burst"; the electrolytics are "the DC energy store" and 10 µF film sits "at the legs".
- **Finding:** all capacitance is across the DC bus. The series path is bus+ → high-side FETs → switch node → `L_series` → rails and slug → current sensor → return. That is a synchronous buck converter with no output capacitor. Its only launch resonance is bank with `L_series`: 0.67 kHz for six cans and 2 µH, 4.2 kHz for two cans and 150 nH. For the bank to resonate at 200 kHz the loop inductance would have to be 22–67 pH.
- **Also:** the film cans form a parasitic bus resonance near 100 kHz with the stray inductance to the bank. That is ringing to be damped, not a tank.
- **Fixed in:** `UnifiedResonantDriver.md` §2–3, `UnifiedResonantSchematic.md` §2.

### A2. A 200 kHz burst at kiloamps is 100–200 hard commutations per shot

- **Finding:** each turn-off has to dispose of ½·Lσ·I² from the commutation loop (about 35 mJ at 1.5 kA and 30 nH) and spikes the FETs by Lσ·di/dt. Switching loss on top is of the order of 45 mJ per cycle. Over a 0.5 ms burst that is roughly a 140 K junction rise from switching alone.
- **Why it matters:** paralleled MOSFETs do not share avalanche energy; the device with the lowest breakdown voltage takes most of it ([PP-PARALLEL](References.md#4-pulsed-power-practice)). The current sensor on the BOM cannot see any of this (A10).
- **Fixed in:** `UnifiedResonantDriver.md` §3.

### A3. High frequency gives no physical benefit here

| Claim in the documents | What the numbers say |
|---|---|
| "Skin effect is strong in … the conductive slurry/armature" | Skin depth at 200 kHz is 1.1 mm for a slug at 10⁻⁶ Ω·m and 3.6 mm at 10⁻⁵ Ω·m. The slug is 0.5–1 mm. There is no skin effect in it. Individual 20 µm particles are far thinner than the 0.15 mm skin depth of solid copper. |
| Skin effect in the rails is a goal | Copper skin depth is 0.15 mm at 200 kHz against 2.1 mm at 1 kHz. Current is squeezed into the rail edge, which raises rail resistance several-fold, heats the edge, and lowers L′ toward its high-frequency minimum. |
| High peak current, low voltage | The reactive drop is ωLI. For 100 nH at 200 kHz that is 126 mΩ, or 251 V at 2 kA, from a 48–60 V bus. |
| AC still propels | It does, because force goes as I². But the mean of I² is half its peak, so AC gives half the impulse per peak amp. |

- **Fixed in:** `UnifiedResonantDriver.md` §3; table 6 of the script output.

### A4. Charge sets the bank size, and two cans are not enough

- **Finding:** for a constant-current shot the charge drawn is Q = I·t = 2·√(m·s/L′), independent of velocity. For 2 mg, 100 mm and 0.6 µH/m (the concept table) that is 1.15 C; for 1 mg at 0.4 µH/m, 1.0 C.

| Bank | Charge | Energy |
|---|---|---|
| 2 cans at 55 V | 0.52 C | 14.2 J |
| 6 cans at 30 V | 0.85 C | 12.7 J |
| 6 cans at 55 V | 1.55 C | 42.7 J |
| 12 cans at 55 V | 3.10 C | 85.3 J |

- **So:** "Two cans is enough for first shots" is wrong for anything but very light slugs. The older v0.1 list (6–12 cans) was better matched. The four film cans hold 2.4 mC and are decoupling only.
- **ESR dominates the loop.** Nichicon gives tan δ 0.20 at 120 Hz, which is ≤56 mΩ per can, and publishes nothing at kilohertz ([DS-LGU](https://www.nichicon.co.jp/english/series_items/catalog_pdf/e-lgu.pdf)). The model assumes 25 mΩ per can. At that value six cans contribute 4 mΩ, about half the loop. Nichicon's general guidance also advises against rapid, frequent charge/discharge of standard cans ([DS-LGU-GUIDE](https://www.mouser.lt/pdfDocs/nichicon-gxc-app-guidelines.pdf)), so shot rate should stay low and can temperature should be watched.
- **Fixed in:** `UnifiedResonantShoppingList.md` (budget table), `EM-CSAM-ConceptTechnical.md` §3.4.

### A5. Electrical energy per shot is tens of joules

- **Documents say:** "the kinetic energy remains well under 1 J. Capacitor banks of a few tens of joules are therefore ample".
- **Finding:** momentum fixes the action: ∫I²dt = 2mv/L′. Loss is R·∫I²dt. For 1 mg at 300 m/s that is 1500 A²s, so 15 J at 10 mΩ and 30 J at 20 mΩ, against 45 mJ of kinetic energy. Whole-shot efficiency is about L′v/(4R), which is 0.1–0.5 %. A bank of tens of joules is needed *per shot*, not as a comfortable reserve.
- **Levers:** lower slug mass, lower loop resistance, and more force per amp (augmentation, B5).
- **Fixed in:** `EM-CSAM-ConceptTechnical.md` §3.4.

### A6. Four FETs per leg carry about 1.4 kA

- **Finding:** IDM is 684 A, but it is bounded by junction temperature. With a transient thermal impedance of about 0.063 K/W at 500 µs and a hot on-resistance near 11 mΩ, 450 A for 0.5 ms is about a 100 K rise; 350 A is the figure for 1 ms ([DS-IRFP4568](https://www.infineon.com/dgdl/irfp4568pbf.pdf?fileId=5546d462533600a4015356310e811e5b); thermal impedance calculated, see References). Gate drive must be at least 10 V at that current. With a derate for unequal sharing, 4+4 is good for about 1.4 kA.
- **Consequence:** six cans at 30 V into a shorted barrel give 2.0–2.6 kA. The bus voltage has to be capped (see §6).
- **Fixed in:** `UnifiedResonantDriver.md` §5, `UnifiedResonantSchematic.md` §4.

### A7. The hard turn-off voltage budget was incomplete

Switching the high side off under load has three terms, not one:

1. the bus voltage;
2. the **bank-to-film pump**: current flowing in the stray inductance between the electrolytics and the film cans keeps going into the film cans, raising them by about I·√(L_bank/C_film). With 60 nH and 40 µF that is 58 V at 1.5 kA;
3. the **commutation spike** Lσ·di/dt. The current fall is set mostly by source inductance inside the gate loop, not by the gate resistor, until the resistor is very large. Estimated 50–180 V for four FETs across 25–45 nH.

- **Rule:** keep the sum under about 120 V on 150 V parts. Hard turn-off at 1.4 kA is plausible at ≤30 V and unproven at 56 V. The full-dump mode avoids the question because the switch opens near zero current.
- **Status:** estimate. Lσ and L_bank must be measured from ringing (TestPlan T2).
- **Fixed in:** `UnifiedResonantDriver.md` §5, `UnifiedResonantSchematic.md` §4.

### A8. The gate driver's undervoltage lockout will not protect the FETs

- **Documents say:** `UCC21551A`, "8 V UVLO / 6.7 V VDD min".
- **Finding:** the A suffix is the **5 V** UVLO option, with a typical turn-on of 6.0 V ([DS-UCC21551](https://www.ti.com/lit/ds/symlink/ucc21551.pdf)). It is still the right part for 12 V rails (the B and C are not sold in the SOIC-16 package), but it will keep switching with a sagging gate rail, below the 7–8 V a FET needs at 450 A.
- **And:** the BOM puts only 0.1 µF on each isolated rail. One edge of four gates moves 0.6 µC, which droops 0.1 µF by 6 V. TI asks for about 10 µF plus 100 nF.
- **Fix:** 10 µF + 0.1 µF soldered at the adapter on each rail, and a ≥10 V supervisor on both secondaries that gates EN.
- **Fixed in:** `UnifiedResonantSchematic.md` §3.4, `UnifiedResonantShoppingList.md`.

### A9. Dead time, enable and input filtering were never specified

- Dead time is tDT[ns] = 8.6·RDT[kΩ] + 13. With the DT pin open or tied to VCCI there is **no interlock** and both outputs can be high. A 51 kΩ resistor gives 452 ns.
- EN is active-high with an internal pull-down, so the safe default is free; it needs an explicit external pull-down and a filter.
- The inputs want a small RC at the adapter, because the bars radiate.
- **Fixed in:** `UnifiedResonantSchematic.md` §3.4.

### A10. Nothing measures or protects launch current

- The ACS772-200B is ±200 A and clamps beyond that ([DS-ACS772](https://www.allegromicro.com/-/media/files/datasheets/acs772-datasheet.pdf)). The shopping list calls it the launch "protection / peak" sensor. It is a conditioning-current sensor.
- Its overcurrent rating is 1200 A for one second. A sub-millisecond pulse of 1–2 kA is far below that in I²t, but the output carries up to 0.4 A of magnetic offset afterwards and must be re-zeroed.
- **Fix:** a Rogowski loop around the return bar, sampled and integrated numerically, calibrated against the ACS772 at 100–200 A. A sense winding on `L_series` is not a substitute: it reads flux, which depends on slug position.
- **Fixed in:** `UnifiedResonantSchematic.md` §3.7.

### A11. The dividers defeat the isolation, and there is no logic supply

- The design isolates the gate driver and both gate supplies, then hangs resistive dividers from the bus and the rails to the MCU's ADC. That ties MCU ground to the power return.
- No 12 V source for the driver's logic side and the DC-DC inputs is on the BOM. "5 V from the 12 V isolated rail" would hang the logic on a gate-drive secondary.
- **Decision recorded:** logic ground *is* the power return, bonded at one star point. The sequencer lives on that ground. The galvanic boundary moves to the link between the sequencer and the printer controller or PC. A third, floating 12 V supply feeds the logic.
- **Hazard that follows:** any earthed USB link grounds the return bar, after which an oscilloscope ground clip on the switch node shorts the bank through protective earth. Every PC link gets a USB isolator.
- **Fixed in:** `UnifiedResonantSchematic.md` §3.8–3.9.

### A12. Printer firmware cannot time the pulse

Klipper-class firmware schedules steps well but is not a tool for 100–700 µs pulses with hardware limits and a fast abort. A small dedicated sequencer (RP2040 class) is required. The printer sends "fire" and parameters.

- **Fixed in:** `UnifiedResonantSchematic.md` §3.8, `ControllerArchitecture.md` banner.

### A13. Constant-current conditioning cannot run through the launch inductor

- **First draft said:** regulate 5–20 A by PWM through `L_series`, sensing with the ACS772.
- **Finding:** with 2 µH, a 30 V bus and a 2.5 µs sensor, the current overshoots by V·t_d/L ≈ 50 A before the loop can react. The duty cycle into a milliohm load is under 1 %, shorter than the dead time.
- **Fix for the first build:** limit conditioning current with a ballast resistor from a low bus voltage. Power into the slug then *falls* as its resistance falls, which is the self-limiting behaviour wanted (C8). A solid-state stage needs a separate inductor of at least 50 µH, or a comparator loop faster than about 0.3 µs.
- **Fixed in:** `UnifiedResonantDriver.md` §4, `UnifiedResonantSchematic.md` §3.6.

### A14. Protection gaps

| Gap | Consequence | Fix |
|---|---|---|
| No source fuse | A shorted FET is a pack short | DC fuse rated ≥60 V (automotive blade fuses are 32 V) |
| "May be jumpered once the bank is up" | Removes the only current limit between pack and bridge | Never jumper the charge resistor on a battery |
| No hardware limit on on-time | A firmware hang holds the switch on; then 90 W (30 V) or 314 W (56 V) sits in the 25 W charge resistor | Per-pulse maximum on-time on the high-side command; bench current limit ≤1 A while charging |
| No over-current trip | See A10 | Fast latch from the Rogowski channel |
| Bleeder "few seconds" | 1.5 kΩ with 9.4–28 mF is a 14–42 s time constant; 76–102 s to fall below 5 V | State the real time; add a low-value dump resistor |
| Bank reversal | If the bank runs to zero with the switch still on, the low-side diodes clamp it at about −1.3 to −1.8 V | Tolerable briefly; keep the charger connected so it recovers |

- **Fixed in:** `UnifiedResonantSchematic.md` §5, `UnifiedResonantShoppingList.md`.

### A15. Parts with the wrong job

- **T9AS relay.** Rated 20 A at 28 VDC resistive, with 75 mΩ initial contact resistance and 15 ms operate time ([DS-T9A](https://tvsat.com.pl/PDF/1/1-1393210-3.pdf)). As a bypass across `L_series` it cannot shunt a milliohm coil, and a closed or welded contact at launch removes the inductance that limits current (3–6 kA). It is removed from that role and reused as charge-enable at ≤30 V.
- **MUR1560.** IFSM 150 A. It cannot carry a kiloamp freewheel tail; the FET body diodes (684 A pulse each) do.
- **Rail-pad TVS.** A 5KP58A clamps 54.5 A. It is not a muzzle-arc suppressor.
- **Fixed in:** `UnifiedResonantShoppingList.md` role table.

### A16. Diagram defects

- Both ASCII figures in `UnifiedResonantDriver.md` drew `L_series` as a branch in parallel with the rails. The text, correctly, has it in series.
- The §9.2 bar-strip sketch never showed the low-side sources reaching the return bar.
- **Fixed in:** both files; the schematic now carries one explicit net-level drawing.

---

## 4. Launcher physics and mechanics

### B1. L′ is 0.3–0.5 µH/m and has to be measured

- **Documents use:** 0.6 µH/m.
- **Finding:** the rails here are flat strips lying side by side with a 0.5 mm gap between their edges, which is not the square-bore geometry the usual figures come from.

| Estimate | L′, µH/m |
|---|---|
| Thin coplanar strips, 2 / 4 / 8 mm wide | 0.55 / 0.47 / 0.40 |
| Kerrisk high-frequency fit, 2 / 4 / 8 mm wide, 0.5 mm high ([RG-KERRISK82](https://www.osti.gov/servlets/purl/5222337)) | 0.37 / 0.33 / 0.28 |
| Flux that actually crosses the gap, current spread 0.5 / 1 / 2 mm into the rail | 0.55 / 0.38 / 0.25 |

- **Why the spread matters:** thin rails are transparent to flux, so only the flux crossing the gap pushes the slug; the rest pushes on rail metal. Right behind a moving slug the current has had only microseconds to spread, which favours the higher values.
- **Design consequence:** rails wider than about 3–4 mm lower L′. Narrower rails are worth trying for that reason.
- **Correction (2026-11-11):** this finding originally added that wider rails "carry no extra pulse current (the pulse only penetrates about 2 mm)". That used the steady 1 kHz skin depth for a single pulse. A single 0.5 ms pulse diffuses into copper with an error-function profile, not to an edge: the depth is 2.1 mm, 3.3 mm or 5.2 mm depending on the cut used (0.8, 1.27 or 2 times √(Dt); the 1/e point is 3.3 mm), and after 0.2–0.7 ms the field at 3 mm is still 20–49 % of its surface value ([EM-MORITZ11](https://arxiv.org/abs/1103.1800); [skin-effect](../quantum-systems/library/skin-effect.md)). The earlier "about 2 mm" was the steady 1 kHz skin depth, the smallest of these. The rail-resistance default in the model (34 mΩ/m, current in the outer 2 mm of 0.5 mm-thick rails) is therefore a conservative assumption, uncertain by about a factor of two until T2 measures it. It matters little: in the model's magnet case, 17 mΩ/m (the DC value of a 4 × 0.5 mm pair) gives 346 m/s and 68 mΩ/m gives 317 m/s, against 336 m/s at the default (`shot_model.py tables`, §12). Right behind the moving slug the current is confined much more tightly than that: the velocity skin depth 2√(D·a/V) for a 1 mm slug is about 0.73 mm at 100 m/s and 0.33 mm at 500 m/s in copper, whatever the pulse length (model formula, [RG-WOODS96](https://apps.dtic.mil/sti/tr/pdf/ADA320642.pdf); no direct measurement opened). That layer, not the pulse depth, sets rail-face heating at the contact.
- **Fixed in:** `EM-CSAM-ConceptTechnical.md` §3.2, `RailMaterial.md`, TestPlan T0 and T3.

### B2. Slug resistance is the gate

- **Documents say:** the slurry "must support clean current initiation and flow".
- **Finding:** an oxidised metal powder chain is high-resistance at low voltage (10⁴–10⁷ Ω), then breaks down to a few ohms and sits at about 0.4 V per contact while the contact spots reach about 1050 °C ([PC-FALCON05](https://ar5iv.labs.arxiv.org/html/cond-mat/0407773)). Across a 0.5 mm gap with 25–50 µm particles that is roughly 4–8 V at any current, until real necks grow. At a kiloamp, 4–8 V is 4–8 kW into a milligram.
- **Correction (2026-11-11):** 0.4 V is the stainless-steel value; the same paper gives 0.3 V for brass and 0.2 V for bronze, and copper was not measured, so the range is 2–8 V. The plateau is the micro-welding regime itself. A bed of heavily oxidised copper powder showed no plateau: 0.50 mm rose to 33 V and then collapsed by five orders of magnitude; compaction lowered the threshold and a shock undid the bridges ([PC-ALIOUAT22](https://doi.org/10.3390/ma15124096)). Film puncture (a field threshold) and the thermal plateau are separate steps. Sources and numbers: [electrical-contacts](../quantum-systems/library/electrical-contacts.md).
- **Window, from the model** (0.5 mg slug, six cans at 18 V, magnet):

| Slug resistance | Joule heat in the slug | State | Velocity |
|---|---|---|---|
| 0.2 mΩ | 0.21 MJ/kg | solid | 336 m/s |
| 0.5 mΩ | 0.50 MJ/kg | melting | 327 m/s |
| 1 mΩ | 0.94 MJ/kg | molten | 313 m/s |
| 2–5 mΩ | 1.7–3.3 MJ/kg | boiling | 290–244 m/s |
| ≥20 mΩ | >6 MJ/kg | vapor | <165 m/s |

- **For scale:** a solid copper slug of this size is about 0.02 mΩ. The launchable window is roughly 10–20× bulk resistivity, which is a sintered compact, or one pressed and then reduced, not a paste. (Corrected 2026-11-11: pressing alone is not enough; a pressed, unreduced copper compact measured 10⁴–10⁵ Ω·m. See [electrical-resistivity](../quantum-systems/library/electrical-resistivity.md).)
- **Fixed in:** `EM-CSAM-ConceptTechnical.md` §3.5, `PowderCarrierRailMaterial.md`, TestPlan T0 and T4.

### B3. Heating and velocity are locked together

Joule heat per kilogram of slug is 2·R_slug·v/(L′ + 2M′). It rises with velocity and with slug resistance, falls with force per amp, and does not depend on barrel length: a shorter barrel needs more current for less time and the same action. In a plain railgun the only ways to change the temperature a slug arrives at, for a given velocity, are its resistance and its length.

- **Fixed in:** `EM-CSAM-ConceptTechnical.md` §3.5.

### B4. Action margin by material

For a solid slug 1 mm long, the velocity at which Joule heating reaches melt onset, against the cold-spray critical velocity:

| Material | Melt onset, m/s per mm of slug | Critical velocity, m/s | Margin |
|---|---|---|---|
| Copper | ~1790 (1340–2230) | 460–500 | 3.7 (2.8–4.7) |
| Copper, measured powder | ~1790 (1340–2230) | 570 | 3.1 (2.4–3.9) |
| Aluminium | ~1850 (1390–2320) | 620–660 | 2.9 (2.2–3.6) |
| Zinc | ~310 (230–390) | 360–380 | 0.8 (0.6–1.0) |
| Iron | ~330 (250–410) | 700–750 (316L) | 0.5 (0.3–0.6) |
| Tin | ~47 (35–58) | 160–180 | 0.3 (0.2–0.3) |

Model result at the planning value L′ = 0.4 µH/m; the bracket is the range L′ = 0.3–0.5 (`shot_model.py tables`, §10).

Action values from [RG-TUCKER75](https://www.osti.gov/servlets/purl/4229184-1IbmTb/); windows from [CS-SCHMIDT09](https://www.researchgate.net/figure/alues-of-critical-velocity-for-bonding-assuming-a-particle-size-of-20-lm-Material-Melting_tbl1_225516724).

- **Reading:** copper and aluminium have room. Iron and tin melt before they reach a bonding velocity, which matches the old README note about steel. A porous slug divides the margin by its resistivity ratio; augmentation multiplies it by (L′ + 2M′)/L′.
- **Correction (2026-11-11):** read the table with these qualifiers (detail and arithmetic in [`quantum-systems/application/EM-CSAM.md`](../quantum-systems/application/EM-CSAM.md) §2.2–§2.4).
  - The table was first computed at L′ = 0.45 µH/m (copper ~2000 m/s, margin 4.2). It was regenerated on 2026-11-11 at the planning value of 0.4 with the 0.3–0.5 range shown.
  - The copper window of 460–500 m/s is a tabulated 20 µm value. The one measured critical velocity opened for copper powder is 570 m/s (5–22 µm powder); the second copper row uses it.
  - Iron is compared with the 316L window because no critical velocity for iron or carbon steel is sourced. Nickel has none either. The zinc and tin windows and action values come from one table and one report that could not be re-opened; they are the least-supported rows, and they are the first two rungs of the test ladder.
  - By enthalpy, copper tolerates a slug resistance of 0.19–0.31 mΩ at 500–300 m/s before melt onset, 11–19 times the 0.017 mΩ solid slug. No sourced copper compact reaches that window without sintering or reduction.
- **Fixed in:** `EM-CSAM-ConceptTechnical.md` §3.5.

### B5. Augmentation is the missed lever

- **Why it works at this scale:** the rails' own field at 2 kA is equivalent to about 0.8 T across the gap. Large railguns run at tens of tesla, where a permanent magnet is irrelevant. Here it is comparable. The literature says the same: augmentation helps "especially in low current railguns" ([RG-ASGARI19](https://www.aemjournal.org/index.php/AEM/article/download/961/443/4084)), and a low-voltage capacitor-fed gun went 85 % faster with a magnet field (RG-HARTKE97, summary only).
- **Two forms:**
  - *Permanent magnets* above and below the bore add B·I·gap, linear in current. 0.8 T across 0.5 mm is 0.4 mN per amp.
  - *Series turns* laid flat over and under the rails, carrying the launch current in the same sense as the rail beneath, add M′·I² ([RG-GALLANT02](https://researchportal.rma.ac.be/ws/portalfiles/portal/8004700/ParallelAugmentedRailguns.pdf)). Because the gap is narrow, each turn-pair couples only 0.05–0.10 µH/m at 0.5–1.5 mm from the bore plane. Eight turns give about 0.35 µH/m and about 2.6 µH.
- **From the model** (six cans, idealised):

| Configuration | 1 mg | 0.5 mg |
|---|---|---|
| 18 V, 1 µH, plain | 106 m/s | 207 m/s |
| 18 V, 1 µH, 0.8 T magnet | 139 m/s | 336 m/s |
| 22 V, 8 augmenting turns | 238 m/s at 1.0 kA | — |
| 22 V, 8 turns + magnet | 320 m/s at 1.0 kA | 526 m/s |

- **Expect roughly 1.5–1.9×**, more for light slugs. Augmenting turns also cut peak current, which is what four FETs per leg are short of.
- **Fixed in:** `EM-CSAM-ConceptTechnical.md` §3.6, `RailgunHeadPrototype.md`, `UnifiedResonantDriver.md` §6.

### B6. What a magnet changes

- Force from the magnet is linear in current while heating is quadratic. Pulse shape can therefore trade arrival temperature against velocity, which a plain railgun cannot do (B3).
- Any unipolar conditioning current inside the magnet zone pushes the slug: 5 A × 0.8 T × 0.5 mm is 2 mN, about 200 g on a 1 mg slug. A half-bridge cannot make zero-mean current without a series capacitor, and a series capacitor cannot pass the launch pulse.
- **Fix:** the first ~20 mm of barrel is a magnet-free conditioning zone.
- **Fixed in:** `RailgunHeadPrototype.md`.

### B7. Current must end before the slug leaves

- **Finding:** when the slug exits with current still flowing, ½·L·I² has nowhere to go but an arc at the muzzle, pointed at the deposit. In the model that is 0.15–0.7 J for the augmented cases (three to ten times the kinetic energy) and over 4 J for a 55 V shot.
- **Rule:** choose bank, inductance and voltage so the current has decayed before exit. The script prints the exit current and the energy behind it. A muzzle shunt is the established alternative ([RG-MUZZLE](References.md#2-railgun-physics-and-augmentation)).
- **Tension:** the freewheel tail lasts about L/R, so a large inductance (including augmenting turns) lengthens it.
- **Fixed in:** `UnifiedResonantDriver.md` §5, `EM-CSAM-ConceptTechnical.md` §3.7.

### B8. Three regimes were described as one process

| Regime | What moves the metal | What lands | Needs |
|---|---|---|---|
| **Solid slug** | Lorentz force on a conducting compact | One warm slug, 100–600 m/s | Slug ≲0.3 mΩ (B2); a slug that slides rather than smears (B9) |
| **Carrier flash** | Pressure of the vaporising carrier, with Lorentz force secondary | A spray of particles dragged by hot gas | Closed breech; vapor generated behind or within the charge |
| **Exploding slug** | The metal itself boils | Vapor and fine droplets; thin films and nanoparticles | Slug resistance in the milliohm-to-ohm range |

- **Scale of the carrier-flash force (estimate):** about 0.1 J vaporises the oil in a 0.25 mm³ slug. Its pressure gives 0.6–6 N on this bore, against 0.45–2.5 N of Lorentz force in the concept table. Whenever the carrier flashes, the device is at least partly an electrothermal gun.
- **Prior art sits in the last two regimes:** [PA-EPD](https://patents.google.com/patent/US6329025B1/en) drags powder with a gas column; [PA-ELTEPS](https://link.springer.com/article/10.1361/105996302770349032) explodes the powder.
- **Fixed in:** `EM-CSAM-ConceptTechnical.md` §2.4, TestPlan T5.

### B9. A liquid plug will not cross the barrel intact

- **Estimate:** wall shear on a plug moving at 300 m/s in a 0.5 mm bore gives 0.07 N of drag at 0.01 Pa·s, 0.7 N at 0.1 Pa·s and 7 N at 1 Pa·s, against a drive force of 0.45–2.5 N. A film only 2 µm thick over 100 mm of bore holds 0.4 mm³, more than the whole 0.25 mm³ slug.
- **Reading:** the slug has to behave as a solid by the time it moves, or the barrel has to be much shorter, or the charge has to travel as a spray (B8).
- **Fixed in:** `EM-CSAM-ConceptTechnical.md` §3.8, `RailgunHeadPrototype.md` (shorter-barrel option).

### B10. Conditioning details, and missing diagnostics

- Conditioning current pushes the slug even without a magnet: 20 A gives 80 µN, which is 8 g on 1 mg, against a paste hold force of roughly 0.2–2 mN. Stay at or below about 20 A unaugmented.
- A breech solenoid for induction heating at 10–50 kHz does nothing useful: the slug is far thinner than its skin depth.
- No document said how velocity, launch current or slug voltage would be measured. A differential voltage tap at the **muzzle** end of the rails reads the slug voltage alone, with no rail drop and no inductive term, during both conditioning and flight.
- **Fixed in:** TestPlan (diagnostics), `UnifiedResonantSchematic.md` §3.7, `RailgunHeadPrototype.md`.

### B11. Prior art

Summarised in §8.

---

## 5. Metallurgy and chemistry

### C1. Copper rails first, not aluminium

- **Conflict:** `RailMaterial.md` recommended aluminium for the first generation; `RailgunHeadPrototype.md` recommended tellurium copper; the README offered either with copper powder.
- **Finding:** copper and aluminium form a eutectic at 548 °C. Hot copper powder on an aluminium rail makes liquid at the contact well below either melting point. Aluminium's oxide also re-forms in milliseconds and needs breaking down on every shot.
- **Recommendation:** tellurium copper C145 for the first rails.
- **Fixed in:** `RailMaterial.md`, `README.md`.

### C2. Avoid C110 under a hydrogen-rich carrier vapour

Oxygen-bearing ETP copper is embrittled when hydrogen reaches its Cu₂O and forms steam, with the risk quoted above about 370 °C ([MT-CUH](https://www.mdpi.com/2075-4701/14/5/588)). A mineral-oil carrier decomposes to hydrogen and acetylene (C5). C145 is phosphorus-deoxidized and 93 % IACS ([MT-C145](https://www.concast.com/files/C14500.pdf)), which gives the machinability argument a metallurgical one beside it. Immunity of deoxidized grades was not directly confirmed in a source.

- **Fixed in:** `RailMaterial.md`.

### C3. PEI and PEEK are poor arc-facing walls

| Material | Comparative tracking index | Arc resistance (D495) |
|---|---|---|
| PEI (Ultem 1000) | 150 V (group IIIb) | 128 s |
| PEEK | 150 V (group IIIb) | 40 s |
| POM (acetal) | — | 200–220 s |
| PTFE, PE | ≥600 V (group I) | — |

Sources: [MT-CTI](https://www.cmc.de/en/cti-kriechstromfestigkeit), [MT-ARC](https://www.specialchem.com/plastics/guide/arc-resistance).

- **Reading:** PEI is a fine structural shell. The surface that faces the bore should be a liner: mica sheet, Macor, hexagonal boron nitride, fired pyrophyllite, or an ablative polymer (POM, PTFE) of the kind used in arc chutes ([MT-ABLATE](https://link.springer.com/article/10.1007/s11090-024-10451-1)). The bore will also be metallised by its own vapour, so a rail-to-rail resistance check before each series is worth building in.
- **Fixed in:** `RailgunHeadPrototype.md`, `BarrelHighVolMfg.md`.

### C4. Carrier choice should start from conductivity

The combination tables chose carriers for suspension and gas chemistry. Given B2, the first question is how the slug comes to conduct. Options that were missing:

- **Metallic carriers.** Gallium and Galinstan conduct at 2.9×10⁻⁷ Ω·m, about 17× copper, which is inside the launchable window from the first microsecond; with copper powder they harden to CuGa₂ over hours ([CH-GALLIUM](https://par.nsf.gov/servlets/purl/10188018)). Gallium destroys aluminium, so no aluminium rails, bodies or substrates. Low-melting tin alloys with copper powder form transient-liquid-phase pastes whose intermetallics melt far above the processing temperature (CH-TLPS; no primary source pinned).
- **Self-reducing carriers.** Copper formate decomposes at 200–220 °C to copper, CO₂ and hydrogen, leaving fresh metal at the particle necks ([CH-FORMATE](https://documentserver.uhasselt.be/bitstream/1942/27642/3/MarchalW_draft2018_1_IC.pdf)).
- **Fluxes.** Potassium fluoroaluminate for aluminium–silicon; self-fluxing NiCrBSi for hard-facing ([CH-AL](https://www.mdpi.com/2075-4701/10/3/368/htm), CH-NICRBSI).
- **Solder paste** as a ready-made tin system for feed and conduction experiments.
- **Fixed in:** `PowderCarrierRailMaterial.md`, `README.md`.

### C5. What an oil carrier becomes

Arcing in oil gives mainly hydrogen and acetylene, with soot ([CH-DGA](https://limswiki.org/index.php/Dissolved_gas_analysis)). Carbon is harmless in copper, carburises iron, and with aluminium forms Al₄C₃ above about 500 °C, which later hydrolyses in humid air ([CH-AL](https://en.wikipedia.org/wiki/Aluminium_carbide)). Hydrogen causes porosity in aluminium and embrittles titanium and high-strength steel. No measured composition for flash heating was found.

- **Fixed in:** `PowderCarrierRailMaterial.md`.

### C6. The starter ladder needs numbers, and zinc

Critical velocities at 20 µm: Sn 160–180, Zn 360–380, Cu 460–500, Al 620–660, 316L 700–750, Ti 700–890 m/s ([CS-SCHMIDT09](https://www.researchgate.net/figure/alues-of-critical-velocity-for-bonding-assuming-a-particle-size-of-20-lm-Material-Melting_tbl1_225516724)). Three modifiers matter here:

- **Oxygen.** Copper powder at 0.02 wt % oxygen bonds near 300 m/s; at 0.38 wt % it needs 610 m/s (CS-SCHMIDT06, via review). Powder storage is a process variable.
- **Size.** Larger particles bond slower ([CS-DOWDING20](https://www.osti.gov/servlets/purl/1658603)), which favours a slug-sized body.
- **Temperature.** Hot particles bond slower ([CS-MORIDI14](https://re.public.polimi.it/bitstream/11311/968457/4/Cold%20spray%20coating_11311-968457_Guagliano_1.pdf)). By the Schmidt formula copper drops from about 485 m/s cold to about 340 m/s at 550 °C (indicative).

Zinc belongs on the list: cheap, conductive, useful, and bonding at 360–380 m/s.

- **Fixed in:** `PowderCarrierRailMaterial.md`, `README.md`.

### C7. Compaction is a strong lever

Copper powder resistance falls as pressure to the power −1.8 ([PC-CREYSSELS09](https://labo.msc.u-paris.fr/~falcon/AIP09.pdf)). On this bore, 30 MPa is about 7 N. A breech plunger can meter the charge, compact it, and close the breech in one part.

- **Fixed in:** `RailgunHeadPrototype.md`, TestPlan T0.

### C8. Conditioning is electrical sintering

Printed metal inks sinter electrically in under 2 µs once started, "due to strong positive feedback induced by the voltage boundary condition" ([PC-ALLEN08](https://cris.vtt.fi/en/publications/electrical-sintering-of-nanoparticle-structures/)); a series resistor limits the runaway without removing it ([PC-HUMMELGARD11](https://pmc.ncbi.nlm.nih.gov/articles/PMC3044741)). Conditioning must be current-limited. A bench supply's output capacitor is a voltage source on this timescale, so it needs a ballast resistor too.

- **Fixed in:** `UnifiedResonantDriver.md` §4, TestPlan T4.

### C9. Adjacent uses of the same driver

- **Electrospark deposition:** capacitor sparks of 0.005–10 J through a consumable electrode ([AD-ESD](https://www.svc.org/clientuploads/directory/resource_library/02_087.pdf)). The driver's energy range overlaps.
- **Tab and spot welding:** the same current class as a kWeld ([PP-KWELD](https://www.keenlab.de/index.php/portfolio-item/kweld/)), and a good dummy load.
- **Nanopowder:** wire explosion in liquid ([PC-EEW](https://doi.org/10.1023/B:NANO.0000006069.45073.0b)).
- **Printed magnets:** cold-sprayed NdFeB exists, but with an aluminium binder, so it conducts ([AD-MAGNET](https://link.springer.com/doi/10.1007/s11666-019-00917-6)). The "insulating magnet" in the pitch needs ferrite or coated grains.
- **Fixed in:** `PowderCarrierRailMaterial.md`, `quantum-systems/application/EM-CSAM-Pitch.md`.

---

## 6. The re-baselined driver, in brief

Full detail is in [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) and [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md).

| Mode | What happens | When |
|---|---|---|
| Launch, dump | High side on once; bank and `L_series` shape the pulse; energy set by bus voltage; low-side gates held off so those FETs act only as freewheel diodes | First light |
| Launch, truncated | High side switched off under load at a set time | After overshoot is measured, ≤30 V first |
| Conditioning | Ballast-limited current from a low bus | First build |
| High-frequency experiment | A small pulse capacitor in series makes a true series-resonant inverter, ≤300 A | Optional |

**Voltage ceiling for 1.4 kA into a shorted barrel** (range is ESR 25 → 15 mΩ per can):

| Bank and inductor | Amps per volt | Ceiling |
|---|---|---|
| Six cans, 2 µH | 66–73 | 19–21 V |
| Six cans, 1 µH | 78–88 | 16–18 V |
| Two cans, 2 µH | 35–42 | safe to 30 V |
| Two cans, 1 µH | 41–50 | 28–34 V |

The two-switch asymmetric bridge was considered and not adopted: it needs sixteen FETs for the same current. The bar layout leaves room for a second leg.

---

## 7. What the kit on hand should reach

Kit: twelve FETs, six or more cans, four film cans, a 0–30 V / 10 A supply. Idealised solid slug of 0.2 mΩ; produced by `python3 em-csam/tools/shot_model.py tables`, table 8.

| Configuration | Slug | Velocity | Peak current | Exit current |
|---|---|---|---|---|
| Two cans, 30 V, 2 µH, plain | 0.25 mg | 203 m/s | 1.05 kA | ~0 |
| Six cans, 18 V, 1 µH, plain | 1 mg | 106 m/s | 1.38 kA | 0 |
| Same + 0.8 T magnet | 1 mg | 139 m/s | 1.38 kA | 0 |
| Same + 0.8 T magnet | 0.5 mg | 336 m/s | 1.37 kA | 0.16 kA |
| Same + 0.8 T magnet | 0.25 mg | 633 m/s | 1.37 kA | 0.60 kA |
| Six cans, 22 V, 8 augmenting turns + magnet | 1 mg | 320 m/s | 1.00 kA | 0.42 kA |
| Six cans, 22 V, 8 augmenting turns + magnet | 0.5 mg | 526 m/s | 1.00 kA | 0.70 kA |
| Six cans, 30 V, 1 µH, magnet, **6+6 FETs** | 1 mg | 398 m/s | 2.29 kA | 0.52 kA |

**Reading.** With four FETs per leg, a 1 mg slug reaches the tin window plain and the zinc window with augmentation. The copper window (460–500 m/s cold, lower when warm) needs slugs of 0.5 mg or less, or six to eight FETs per leg and more voltage. Sensitivity for the 0.5 mg magnet case: L′ of 0.3 or 0.5 µH/m moves 336 m/s to 266 or 391; ESR of 50 or 15 mΩ per can moves it to 252 or 396.

---

## 8. Prior art

The top-level README said no close cousin had been found. None is identical, but four are close enough to cite.

| Work | Mechanism | Scale | Relation to this project |
|---|---|---|---|
| **UT-CEM electromagnetic powder deposition** ([patent US 6,329,025](https://patents.google.com/patent/US6329025B1/en), expired; [fact sheet](https://p2infohouse.org/ref/11/10452.htm)) | Railgun plasma armature snowplows a gas column; side-fed powder is dragged to >2 km/s | 12.7 mm bore, ≥50 cm rails, ~150 kA, ~120 µs, 28 mF | A railgun for powder deposition, at 100× the current. Gas, not the slug, is the working body. Reported bond strength equal to base metal and <3 % porosity. |
| **EMAPS** ([Kitamura et al. 2003](https://link.springer.com/article/10.1361/105996303770348519)) | Coaxial pulsed plasma gun accelerates pre-injected powder | ~100 kA, ~300 µs, 1–3 km/s | Same idea as above with a different electrode geometry; ceramic coatings. |
| **ELTEPS** ([Tamura group](https://link.springer.com/article/10.1361/105996302770349032)) | A discharge through a powder column explodes it | 2–3× melt energy; 0.9–3 km/s | The exploding-slug regime, done deliberately for refractory coatings. |
| **Lorentz-force liquid-metal jetting** ([Vader/Xerox](https://briefs.techconnect.org/papers/advances-in-magnetohydrodynamic-molten-metal-jet-printing/); Océ US 9,593,403) | Pulsed coil, or current through the melt in a permanent-magnet field, ejects molten droplets | 250–1000 µm drops, several m/s, up to 1 kHz | The molten, low-velocity end. The Océ patent is the direct-current, magnet-augmented cousin of this head. |

What still looks unoccupied: a **solid or sintered** milligram armature, at **kiloamp** rather than 100 kA scale, from a **low-voltage** bank, in a **cheap replaceable** barrel. No patent search was done.

---

## 9. Assumptions, and what would overturn them

| Assumption | Used in | Overturned by |
|---|---|---|
| ESR 25 mΩ per can at 1–10 kHz | Peak current, velocity, voltage ceilings | Discharge each can into a known resistor (T0). Above 50 mΩ, expect about 25 % less velocity. |
| L′ = 0.4 µH/m | All velocities | LCR meter with a sliding short (T0); velocity fit against ∫I²dt (T3). |
| Rail resistance 34 mΩ/m for the pair | Velocity, weakly (+3 % at half, −6 % at double) | Four-wire resistance of the rail pair, and the current decay into a strap at two barrel positions (T2). |
| Commutation loop 20–45 nH; bank-to-film 60 nH; source inductance 8–13 nH | Turn-off budget (A7) | Ring frequency and overshoot at low current (T2). |
| ZthJC from an older Foster model | FET current limit (A6) | Fig. 13 of the current datasheet; case temperature after a shot. |
| ±20 % current sharing among paralleled FETs | 4+4 = 1.4 kA | Per-device drain-source voltage or temperature (T2). |
| Augmenting coupling 0.05–0.10 µH/m per turn-pair | B5 | Velocity with and without the turns (T3). Rails that exclude flux on the pulse timescale would raise it. |
| Magnet field 0.8 T in the bore | B5 | Gaussmeter in an assembled head. |
| Slug behaves as a rigid body of fixed resistance | All velocities | It will not. T3 uses solid armatures to test the launcher alone; T4–T5 test the slug. |
| Wall drag and vapor pressure neglected | All velocities | Estimates in B8 and B9 say both can exceed the Lorentz force. |
| Action-to-melt values | B4 | Disputed by one later paper; treat as ±tens of percent. |

---

## 10. Where each finding was fixed

| Finding | Document |
|---|---|
| A1–A3, A7, A13, B7 | [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) |
| A6–A11, A13–A16 | [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md) |
| A4, A8, A14, A15 | [`UnifiedResonantShoppingList.md`](UnifiedResonantShoppingList.md) |
| A4, A5, B1–B9 | [`EM-CSAM-ConceptTechnical.md`](EM-CSAM-ConceptTechnical.md) |
| B1, C1, C2 | [`RailMaterial.md`](RailMaterial.md) |
| B5, B6, B10, C3, C7 | [`RailgunHeadPrototype.md`](RailgunHeadPrototype.md) |
| B2, C4–C6, C9 | [`PowderCarrierRailMaterial.md`](PowderCarrierRailMaterial.md), [`README.md`](README.md) |
| C3 | [`BarrelHighVolMfg.md`](BarrelHighVolMfg.md) |
| A12 | [`ControllerArchitecture.md`](ControllerArchitecture.md) |
| All measurements | [`TestPlan.md`](TestPlan.md) |
| Handoff | [`AGENTS.md`](AGENTS.md) |
| Document defects | The files named in the list below |

**Document defects repaired:** `EM-CSAM-ConceptTechnical.md` held four interleaved copies of itself; `ControllerArchitecture.md` repeated its flat-cable section; `EM-CSAM-LENR.md` had one corrupted word; the three v0.1 driver files carried no "superseded" notice; `quantum-systems/application/EM-CSAM.md` called a 20 µm copper particle electrically thick at 1 µs, where the skin depth is about 66 µm.
