# EM-CSAM Test Plan

The experiments that turn the model numbers in these notes into measurements, in the order that risks least and teaches most. Written for the kit on hand in November 2026: the first-build driver parts, six or more cans, and a 0–30 V / 10 A bench supply. Nothing here needs the battery pack.

Background: [`DesignReview-2026-11.md`](DesignReview-2026-11.md). Driver wiring and values: [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md). Sources by ID: [`References.md`](References.md).

**Each stage has an exit test. Do not move on until it is met**, and write the result into the assumption table in the review (§9) and into the script defaults.

| Stage | What | Needs the driver? |
|---|---|---|
| T0 | Bench measurements: cans, coils, rails, paste resistance | No |
| T1 | Logic board alone | Logic only |
| T2 | Power into a copper strap | Yes |
| T3 | Solid armatures: is the launcher physics right? | Yes |
| T4 | Conditioning: can a paste slug be made to conduct? | Ballast path |
| T5 | Regime shots: what actually comes out? | Yes |
| T6 | Deposits and how to judge them | Yes |
| T7 | Optional: high-frequency comparison | Yes |

T0 and T1 can run in parallel. T4 can start as soon as T0 has a paste worth trying.

---

## Safety

Read before every session.

- **Current, not voltage, is the hazard at ≤30 V.** A dropped tool across the bars carries kiloamps and throws molten copper. No rings, watches or loose metal. Insulate the bars wherever a tool could bridge them.
- **The bank stays charged.** The bleeder takes 76–102 s to bring it below 5 V. Use the dump resistor, then check with a meter, then touch.
- **Projectiles.** A 1 mg slug at 300 m/s will penetrate an eye. Fire only inside the enclosure, into a backstop, wearing safety glasses.
- **Fume and fire.** Every shot makes an arc, an oil mist and metal fume in the same place. Run extraction. Keep solvents, rags and the powder stock away. Have a dry-powder or CO₂ extinguisher at hand; never water on burning metal powder.
- **Powder.** Keep the open inventory to grams. Fine aluminum and titanium are not for this bench ([SF-DUST](https://www.icheme.org/media/25710/hazards-30-paper-47-gakhar.pdf)). Zinc and copper fume cause metal fume fever ([SF-FUME](https://www.ncbi.nlm.nih.gov/books/NBK583199/)).
- **Earth.** The rig floats. The scope ground goes on the return bar and nowhere else. Any PC connection goes through a USB isolator.
- **Magnets.** NdFeB bars of this size snap together hard enough to break skin and shatter.
- **One change at a time**, and start each new configuration at the lowest voltage.

---

## What to Record for Every Shot

Date and shot number · bank (cans, voltage before and after) · `L_series` fitted · FETs per leg · armature or paste (material, mass, how prepared) · conditioning (ballast, voltage, time, final slug resistance) · magnets and augmenting turns fitted · current trace · muzzle-voltage trace · photogate times · witness plate photo · rail-to-rail resistance before and after · anything odd.

Derived: peak current, ∫I dt, ∫I² dt, velocity, momentum, exit current.

---

## T0 – Bench Measurements (no driver)

### T0.1 Capacitor ESR and capacitance

**Why.** ESR is about half the loop resistance and the largest unknown in the model. Nichicon publishes no kilohertz value ([DS-LGU](https://www.nichicon.co.jp/english/series_items/catalog_pdf/e-lgu.pdf)).

**How.**
1. Charge one can to 10 V through a resistor.
2. Discharge it into a known 0.22–1 Ω power resistor. Switch with a spare FET, its gate driven from a 9 V battery through a push switch; a mechanical switch bounces.
3. Scope the voltage at the can terminals. The step at switch-on is I × ESR. The decay time constant gives capacitance.

**Exit.** ESR and capacitance for every can, written on the can. Script default updated. If ESR is above about 50 mΩ, expect roughly 25 % less velocity than the tables.

### T0.2 Series inductors

Measure each wound coil with an LCR meter, or ring it against one of the 10 µF film cans and read the frequency: L = 1/((2πf)²C). Measure its DC resistance with a four-wire method at a few amps.

**Exit.** Inductance and resistance for each coil, labelled.

### T0.3 Rail inductance gradient

**Why.** The planning value is 0.4 µH/m with a range of 0.3–0.5 ([`EM-CSAM-ConceptTechnical.md`](EM-CSAM-ConceptTechnical.md) §3.2).

**How.** With the rails in the clamshell, put a shorting piece across them at 20, 40, 60 and 80 mm from the breech and measure inductance at each position. The steps are only 6–10 nH, which most handheld LCR meters cannot resolve. Use the ring method with a film capacitor at the breech, or accept that T3 gives the working value.

**Exit.** A low-current L′, or a note that it was below resolution.

### T0.4 Paste-resistance fixture

**Why.** This is the most important experiment in the plan and needs no driver. A slug must reach a few tenths of a milliohm to launch as a solid ([`PowderCarrierRailMaterial.md`](PowderCarrierRailMaterial.md) §0).

**Fixture.** Two C145 bars on an insulating base with a 0.5 mm shimmed gap. An insulating plunger (ceramic or glass rod) with a known force on it. The bench supply through a ballast resistor into the bars. Scope on the gap voltage and on the ballast (for current).

**How.**
1. Fill 1–2 mm of the gap with paste.
2. With 100 Ω ballast, raise the supply slowly from zero. Record the voltage at which current starts (breakdown).
3. Hold a current (0.1 A, then 1 A, then 5 A with a smaller ballast) and log resistance against time.
4. Repeat at plunger pressures of roughly 0, 1, 5, 10 and 30 MPa. On this gap 30 MPa is about 7 N per 0.25 mm² of plunger face.
5. Repeat for each candidate: solder paste; copper powder in oil at two loadings; copper with a flux or self-reducing carrier; copper–tin.

**Look for.** Which of two published behaviours the paste shows. Bead chains hold a plateau of 0.2–0.4 V per contact depending on the metal, 2–8 V across the gap ([PC-FALCON05](https://ar5iv.labs.arxiv.org/html/cond-mat/0407773)). A bed of oxidised copper powder showed no plateau: the voltage rose to a peak (33 V across 0.50 mm for a thick oxide, less under compaction) and then collapsed by five orders of magnitude ([PC-ALIOUAT22](https://doi.org/10.3390/ma15124096)). Record the peak voltage, whether there is a plateau, when it collapses to milliohms, and whether a tap or vibration undoes it (the welded bridges are reported to be weak). Resistance falling as pressure to about the power −1.8 ([PC-CREYSSELS09](https://labo.msc.u-paris.fr/~falcon/AIP09.pdf)).

**Exit.** At least one paste, loading and pressure that reaches 1 mΩ or less per millimetre of slug, repeatably, with the time and energy it took. If nothing does, the solid-slug regime needs a different feedstock (pressed pellets, wire) before any more driver work.

**Hazards.** Small sparks and hot oil vapour. Ventilate; glasses.

---

## T1 – Logic Board Alone

Nothing on the bars. A spare FET's gate is the driver's load.

| Check | Pass |
|---|---|
| Floating 12 V, 5 V, 3.3 V rails | In tolerance under load |
| Both isolated gate rails | 12–13 V; ripple under 0.3 V |
| EN with the sequencer unpowered or reset | Low; both outputs low |
| Supply-good chain | Pulling either gate rail below about 10 V drops EN |
| Dead time (both channels driven) | About 450 ns with 51 kΩ |
| Both inputs high | Both outputs low (interlock working) |
| On-time limit | A 10 ms command is cut at about 2 ms |
| Fault latch | Forcing the comparator input latches the output off until cleared |
| Gate rail droop during a 1 ms pulse into the spare FET | Under 0.5 V |
| Rise and fall at the gate | Clean; no ringing above the gate rail |
| Isolated link | FIRE in and FAULT out work with the far side on a separate supply |

**Exit.** Every row passes, three times in a row, including after a cold start.

---

## T2 – Power into a Copper Strap

A short, thick copper strap bolted across the rail pads in place of the barrel. Low-side gates tied to sources.

### T2.1 First pulses and current calibration

1. Two cans, 2 µH. Supply at 3 V, current limit 1 A.
2. Fire a 1 ms pulse. Expect about 105–125 A. Both the ACS772 and the Rogowski channel should see it.
3. Repeat at 4 V and 4.5 V (up to about 190 A, just inside the ACS772's ±200 A range).
4. Fit the Rogowski channel's scale factor to the ACS772 over these shots.

**Exit.** Rogowski calibration within 5 % across the three voltages.

### T2.2 Stepping up

1. Step through 10, 15, 20, 25 and 30 V. Expect about 35–42 A per volt, so 1.1–1.2 kA at 30 V.
2. At each step record current, switch-node voltage and bus voltage, and compare peak current with `python3 em-csam/tools/shot_model.py shot --cans 2 --volts V --l0 2e-6 --mass 1` (a 1 kg "slug" is a strap).
3. After five shots at each step, check each FET's case temperature.
4. Watch the bank go slightly negative at the end of the pulse and recover.

**Exit.** Clean pulses to 30 V. Model within 20 % after updating ESR. No FET more than 10 K hotter than its neighbours.

### T2.3 Hard turn-off at low current

1. Set the high-side on-time so it opens at about 100 A, then 200 A, then 400 A.
2. Measure the drain overshoot and the ring frequency at the switch node.
3. From the ring frequency and the output capacitance, estimate the commutation-loop inductance. From the bus step, estimate the bank-to-film inductance.
4. Extrapolate overshoot to 1.4 kA.

**Exit.** Extrapolated peak under 120 V at the intended bus voltage, or truncated mode stays off until the layout is tightened.

### T2.4 Six cans

Fit six cans. Obey the ceiling: about 19–21 V with 2 µH, 16–18 V with 1 µH ([`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) §5.2). Repeat T2.2 up to the ceiling.

**Optional.** Weld a nickel strip to a scrap cell tab. It is a good check that energy is really delivered, and useful in its own right ([PP-KWELD](https://www.keenlab.de/index.php/portfolio-item/kweld/)).

---

## T3 – Solid Armatures

**Question.** Is the launcher physics right, with the slug's chemistry taken out of it?

**Armatures.**
- A 0.5–2 mm length of bare 0.5 mm copper wire lying along the bore (about 0.9 mg per half millimetre).
- A folded strip of copper or aluminum foil that fills the gap.
- As a high-resistance control, a short length of 0.5 mm pencil lead.

Weigh each one.

**Setup.** Barrel in place of the strap, no magnets. Photogates 10–20 mm apart beyond the muzzle. Backstop. Muzzle taps connected.

### T3.1 Plain launcher

1. Two cans, 2 µH, 10 V. Fire. Step up to 30 V.
2. For each shot compute momentum (mass × velocity) and ∫I²dt.
3. Plot momentum against ∫I²dt. The slope is ½L′. The intercept is friction and start-up loss.

**Exit.** L′ to within 20 %. A friction estimate. Compare with the 0.3–0.5 µH/m range.

### T3.2 Muzzle voltage signatures

On the same shots, read the muzzle trace.

| Trace | Meaning |
|---|---|
| Under a volt or two, tracking the current | Solid contact |
| Jumps to tens of volts | Arcing at a contact |
| Large spike as the slug exits | Current was still flowing; ½LI² went into an arc |

**Exit.** A reference set of traces for solid contact, arc, and exit with and without residual current.

### T3.3 Magnets

Fit the magnets over the downstream 80 mm. Measure the field with a gaussmeter. Repeat T3.1.

The extra momentum should be B × gap × ∫I dt.

**Exit.** Measured velocity gain against the model's prediction (about 1.3× for 1 mg and 1.6× for 0.5 mg at 18 V on six cans).

### T3.4 Augmenting turns

Fit 4, then 8 turns. Remeasure `L_series` with them in circuit. Repeat T3.1 without magnets, then with.

**Exit.** Coupling per turn-pair, against the estimate of 0.05–0.10 µH/m. Exit current and muzzle spike for each configuration.

### T3.5 Barrel length

If the clamshell allows, repeat a few shots with a 30–50 mm barrel.

**Exit.** Whether the shorter barrel costs or gains velocity at the same bank voltage.

**Hazards.** These are real projectiles. Enclosure closed, backstop in place, glasses on.

---

## T4 – Conditioning

**Question.** Can a paste slug be brought to launch resistance in the barrel, without being ejected or exploded?

**Setup.** Head with the paste slug in the magnet-free breech zone, compacted if a plunger is fitted. Ballast path (relay and power resistor). Bridge off. Log the muzzle-tap voltage and the current.

### T4.1 Ballast conditioning

1. Start at 10 V bus and 10 Ω ballast (1 A maximum, 2.5 W maximum into the slug).
2. Close the relay for 50 ms. Log slug resistance against time.
3. Raise the voltage toward 28 V, then lower the ballast, one step at a time.
4. After each run check whether the slug has moved.

**Why a ballast.** With a resistor much larger than the slug, power into the slug falls as it sinters. A stiff source runs away ([PC-ALLEN08](https://cris.vtt.fi/en/publications/electrical-sintering-of-nanoparticle-structures/), [PC-HUMMELGARD11](https://pmc.ncbi.nlm.nih.gov/articles/PMC3044741)). The most power the slug can ever take is V²/(4 × ballast).

### T4.2 Energy-capped conditioning (alternative)

Charge two cans to a few volts and fire the high side into the slug. The slug cannot receive more than ½CV², which is 0.12 J at 5 V. This is voltage drive, so it will run away, but only as far as the stored energy allows.

### T4.3 Retention

Find the conditioning current at which the slug starts to creep. Expect it near 20 A without magnets (80 µN on 1 mg).

**Exit.** A recipe (ballast, voltage, time, pressure) that brings a slug to the target resistance from T0.4 nine times out of ten, with the slug still in place. Record the energy it took.

---

## T5 – Regime Shots

**Question.** What actually leaves the muzzle?

Fire onto witness plates 5–20 mm from the muzzle. Change one thing per series.

| Series | Slug | Breech | Expectation |
|---|---|---|---|
| A | Conditioned to target resistance | Open | Solid slug |
| B | Conditioned, but stopped early (a few milliohms) | Open | Molten or boiling slug |
| C | Unconditioned paste | Closed (plunger in) | Carrier flash: a spray |
| D | Unconditioned paste | Open | Mostly blow-back; little reaches the plate |
| E | Thin foil or fine wire | Open | Exploding armature: a vapor film |

**How to tell them apart.**

| Sign | Solid slug | Carrier flash | Exploding |
|---|---|---|---|
| Muzzle voltage | Low, follows current | Jumps when the carrier flashes | High throughout |
| Photogates | One sharp event | A smear | A fast, faint front |
| Witness plate | One splat or crater | A speckled cone | A thin, even film |
| Sound | Click | Crack | Loud crack |
| Rails afterwards | Light marking | Sooty | Pitted |

**Exit.** Each regime reproduced on purpose at least three times, with the settings that select it. This is the regime map the concept document describes ([`EM-CSAM-ConceptTechnical.md`](EM-CSAM-ConceptTechnical.md) §2.4), drawn from data.

---

## T6 – Deposits

Only after T5 shows which regime gives something worth keeping.

**Substrates.** Copper, aluminum, mild steel, glass. Degrease; for metal, abrade or grit-blast just before the shot.

**Variables.** Stand-off 5–20 mm. Substrate cold or warmed. Shots per spot (1, 5, 20).

**Judging a deposit with home equipment.**

| Property | Method |
|---|---|
| Adhesion | Tape pull; scratch with a scribe; bend the coupon |
| Density | Section it: set in epoxy, sand to 2000 grit, polish, look under a microscope for pores and unbonded particle boundaries. Ferric chloride etch for copper. |
| Conductivity | Four-point resistance along a line of overlapping splats, converted to % IACS from the section area. A quick proxy for oxide and porosity. |
| Hardness | File or scribe comparison; microhardness if available |
| Rail metal in the deposit | Colour; spot chemistry; elemental analysis if there is access to it |
| Carbon and oxide | Colour of the section; dark boundaries between particles |

**Exit.** A copper (or zinc, or tin) deposit that survives the tape and bend tests and shows metal-to-metal boundaries in section, with the settings that made it.

---

## T7 – Optional: High-Frequency Comparison

Tests the original idea at a safe scale ([`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) §4.4).

1. Fit a 1 µF pulse capacitor in series at the `L_series` pads, two FETs per leg, both driver channels active with dead time. Bus at 5 V, rising to no more than 15 V.
2. Find the resonance by sweeping frequency at low voltage; then run above it.
3. Into a strap first. Insulate the capacitor–inductor node: it reaches hundreds of volts.
4. Then condition identical paste slugs with the same RMS current at DC (ballast path) and at high frequency, for the same time.

**Compare.** Final slug resistance. Rail-edge temperature or discoloration. Whether the slug moved.

**Exit.** A yes or no on whether high-frequency current conditions a slug differently from DC at the same RMS current.

---

## Decision Points

| If | Then |
|---|---|
| T0.4 finds no paste that reaches about 1 mΩ per millimetre | Switch the feedstock to pressed pellets or wire for the solid regime, or commit to the carrier-flash regime. |
| T0.1 finds ESR above 50 mΩ per can | Add cans in parallel before anything else. |
| T2.3 extrapolates above 120 V | Tighten the bar layout; add film capacitance; keep to dump mode. |
| T3.1 gives L′ below 0.3 µH/m | Narrow the rails; rely more on augmentation. |
| T3.3 shows little gain from magnets | Check polarity and field; thin the covers. |
| T5 shows only the carrier-flash regime works | Redesign around a closed breech and treat the barrel as a nozzle. The prior art for that route is in [`References.md`](References.md) §3. |
| T6 gives bonded copper at this scale | Populate six to eight FETs per leg, move to 48 V, and start on the feed mechanism. |
