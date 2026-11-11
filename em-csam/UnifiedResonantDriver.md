# Unified Resonant Bridge – Driver Architecture
EM-CSAM Micro-Railgun · Version 0.2

One half-bridge, one capacitor bank and one series inductor that condition a slug and then launch it with a single shaped pulse.

**What changed in 0.2.** The launch is now one unipolar pulse at the circuit's real resonance (about 1–4 kHz), not a ≥200 kHz burst. The same parts are used; their jobs changed. Section 3 gives the reasons, and [`DesignReview-2026-11.md`](DesignReview-2026-11.md) gives the full analysis. Source IDs resolve in [`References.md`](References.md). Numbers come from [`tools/shot_model.py`](tools/shot_model.py) and are **not measured**. The original concept is kept, briefly, in §12.

Companions: [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md) (nets, values, bring-up) and [`UnifiedResonantShoppingList.md`](UnifiedResonantShoppingList.md) (parts).

## 1. Purpose and Design Goals

- Deliver about 1 C and tens of joules to the rails in 0.2–0.7 ms at 1–4 kA, from a 48–60 V class bus (≤30 V for first light).
- Condition the slug first, with a current-limited source, until its resistance is low enough to launch ([`EM-CSAM-ConceptTechnical.md`](EM-CSAM-ConceptTechnical.md) §3.5).
- Meter each shot by bus voltage and pulse length, and record current and slug voltage for every shot.
- Stay home-buildable: through-hole parts, external copper bars, one small logic board.
- Keep the half-bridge so that later modes (chopped flat-top, series-resonant AC) need no new power stage.

## 2. Topology

`L_series` is **in series** with the rails. Earlier drawings showed it as a parallel branch; that was a drawing error.

```
            F1     D1      R1
SUPPLY+ ──[fuse]──▷|────[10 Ω]────┬───────────┬──────────┬─────────── BUS+
                                  │           │          │
                               C_bus       C_film     TVS, bleeder
                            (electrolytic) (4×10 µF)     │
                                  │           │          │
SUPPLY− ──────────────────────────┴─────┬─────┴──────────┴─────────── RETURN (one star point)
                                        │
BUS+ ── Q_HS (4–8 in parallel) ──●── L_series ── RAIL A ══ slug ══ RAIL B ── Rogowski ── ACS772 ── RETURN
                                 │ SW
RETURN ── Q_LS (4–8 in parallel) ┘

BUS+ ── K2 ── R_ballast ── RAIL A          (conditioning path, first build)
```

- **Bank (`C_bus`).** The electrolytics are the pulse-forming capacitor and the energy store.
- **Film (`C_film`).** Four 10 µF cans at the FET legs decouple the commutation loop. They hold 2.4 mC; they are not an energy store and not a tank.
- **`L_series`.** An air-core inductor of 0.5–3 µH that, with the bank, shapes the pulse and limits its rate of rise.
- **High side (`Q_HS`).** The launch switch.
- **Low side (`Q_LS`).** Carries the freewheel tail. For first light its gates are held off and it acts as a diode group.

## 3. Why launch is no longer "≥200 kHz resonant"

### 3.1 The circuit has no such resonance

All the capacitance is across the DC bus, and only `L_series` is in series with the load. That is a synchronous buck converter with no output capacitor. Its resonances are:

| Loop | Frequency | Meaning |
|---|---|---|
| Bank + `L_series` + rails | 0.67 kHz (six cans, 2 µH) to 4.2 kHz (two cans, 150 nH) | **The launch pulse.** Usually over-damped or near-critical. |
| Film cans + stray inductance to the bank | ~100 kHz | Parasitic bus ringing, to be damped. |
| Optional small series capacitor + `L_series` | 50–300 kHz | The high-frequency experiment (§4.4). |

For the bank itself to resonate at 200 kHz the loop inductance would have to be 22–67 pH.

### 3.2 What a 200 kHz burst would do

- It would be 100–200 hard-switched commutations per shot at 1–2 kA.
- Each turn-off disposes of ½·Lσ·I² from the commutation loop (about 35 mJ at 1.5 kA and 30 nH) and spikes the FETs by Lσ·di/dt.
- Switching loss adds roughly 140 K of junction rise over a 0.5 ms burst.
- Paralleled FETs do not share avalanche energy ([PP-PARALLEL](References.md#4-pulsed-power-practice)).

### 3.3 What it would buy

Nothing in this load.

| Hoped-for effect | What the numbers say |
|---|---|
| Skin effect in the slug | Skin depth at 200 kHz is 1.1 mm at 10⁻⁶ Ω·m and 3.6 mm at 10⁻⁵ Ω·m. The slug is 0.5–1 mm. |
| Skin effect in the rails | Copper skin depth falls from 2.1 mm at 1 kHz to 0.15 mm. Rail resistance rises several-fold, the rail edge heats, and L′ drops. |
| High current from low voltage | The reactive drop ωLI is 251 V at 2 kA into 100 nH. |
| Same thrust | Force goes as I², whose mean is half its peak, so AC gives half the impulse per peak amp. |

### 3.4 What the parts do naturally

The transit time for 100 mm at 300–500 m/s is 0.4–0.7 ms. A bank of 9–28 mF with 0.5–3 µH discharges in exactly that range. The pulse the kinematics need is the pulse the bought parts make.

## 4. Operating Modes

| Mode | What the bridge does | Status |
|---|---|---|
| Conditioning | Bridge idle. Ballast-limited current from a low bus through `K2` and `R_ballast` | First build |
| Launch, dump | High side on once; bank + `L_series` shape the pulse; low-side gates held off | First light |
| Launch, truncated | High side off under load at a programmed time | After overshoot is measured |
| Launch, chopped | Hysteretic 20–50 kHz for a flat top | Later revision |
| High-frequency experiment | Series capacitor fitted; true series-resonant inverter | Optional |

### 4.1 Conditioning

**Job.** Take the slug from megohms to a few tenths of a milliohm without exploding it, and hold it there until launch.

**Why current-limited.** Powder contacts sinter with positive feedback. Under a voltage source the power V²/R rises as the resistance falls, and the transition runs away in microseconds ([PC-ALLEN08](https://cris.vtt.fi/en/publications/electrical-sintering-of-nanoparticle-structures/)). With a series resistor much larger than the slug, power into the slug *falls* as it sinters ([PC-HUMMELGARD11](https://pmc.ncbi.nlm.nih.gov/articles/PMC3044741)).

**First build.** A power resistor of 1–10 Ω and a relay contact from the bus to rail A, with the bus at 5–28 V. Two thresholds apply and they are not the same thing. Puncturing the oxide films is a field effect; the contact spots then heat and micro-weld at a self-limiting 0.2–0.4 V per contact (bead chains: stainless 0.4, brass 0.3, bronze 0.2 V; copper not measured), 2–8 V across this gap ([PC-FALCON05](https://ar5iv.labs.arxiv.org/html/cond-mat/0407773)). A bed of heavily oxidised copper powder showed no plateau and needed 33 V across 0.50 mm before it collapsed, less under compaction ([PC-ALIOUAT22](https://doi.org/10.3390/ma15124096)). If the paste does not break down at 28 V, compact it or reduce the oxide before raising the bus.

- Slug voltage comes from the muzzle Kelvin tap; current from the ACS772. Their ratio is the slug resistance, which is the endpoint.
- Keep current at or below about 20 A without augmentation. 20 A already pushes a 1 mg slug with 80 µN (8 g) against a paste hold force of 0.2–2 mN.
- A bench supply is not a current source on this timescale: its output capacitor is a voltage source. It needs the ballast too.

**Why not PWM through `L_series`.** With 2 µH, a 30 V bus and a 2.5 µs current sensor, the current overshoots by V·t_d/L ≈ 50 A before any loop can react, and the duty cycle into a milliohm load is shorter than the dead time.

**Later.** A solid-state conditioning stage needs its own inductor of at least 50 µH with peak-current control, or a comparator loop faster than about 0.3 µs.

### 4.2 Launch, dump (first light)

- The bank is charged to a set voltage. That voltage is the energy knob.
- The high side turns on once, at zero current. `L_series` limits the rise.
- Current peaks as the bank empties, then freewheels through the low-side body diodes and decays with a time constant of about L/R.
- The high side turns off after the bank current has ended, so it switches almost nothing.
- **Low-side gates stay off** (driver input B strapped low). There is then no shoot-through path at all. Synchronous rectification would gain nothing here: at 350 A per FET the channel drop exceeds the diode drop.

**Bank reversal.** If the bank reaches zero while the high side is still on, the low-side diodes take over and hold the bank at about −1.3 to −1.8 V until it is recharged. Electrolytics tolerate that briefly. Keep the charger connected so the bank recovers.

### 4.3 Launch, truncated and chopped

- **Truncated:** the high side opens at a programmed time while current is still flowing. It gives finer impulse control and a shorter tail. It is a hard turn-off, so the voltage budget of §5.3 applies.
- **Chopped:** repeated truncation to hold a flat current. At 30 V only about 0.3 ms of headroom exists at 1.4 kA because 12 V is lost in loop resistance, so it belongs with a 48 V bus and a fast comparator.

### 4.4 High-frequency experiment

This keeps the original idea alive as something that can be tested safely.

- Fit a small pulse film capacitor (0.22–2.2 µF) in series at the `L_series` pads. The half-bridge then drives a true series-resonant circuit: 225 kHz for 1 µF with 0.5 µH, 107 kHz for 2.2 µF with 1 µH.
- Current is true AC, so it gives no net thrust from a magnet and half the self-field thrust of the same peak DC.
- Drive **above** resonance. Below it the body diodes recover hard.
- Limit current to 300 A by keeping the bus at or below 15 V and by counting cycles. The ACS772 reads low at these frequencies.
- Populate at most two FETs per leg. Gate power with four at 300 kHz exceeds the 2 W isolated supplies.
- The capacitor–inductor node reaches I·Z₀, which is 200–400 V at 300 A, on exposed copper. Insulate it.
- Check the capacitor's peak-current (dV/dt) rating before use.

**What it can answer:** whether a high-frequency current conditions a slug differently from the same RMS current at DC, and how much hotter the rail edges run.

## 5. Limits

### 5.1 Current per FET

| Pulse | Per IRFP4568 | 4+4 | 6+6 | 8+8 |
|---|---|---|---|---|
| 0.5 ms | 450 A | 1.4 kA | 2.1 kA | 2.8 kA |
| 1 ms | 350 A | 1.1 kA | 1.7 kA | 2.2 kA |

- Totals include a derate of about 20 % for unequal sharing.
- 450 A for 0.5 ms is about a 100 K junction rise (ZthJC ≈ 0.063 K/W at 500 µs, hot on-resistance ≈ 11 mΩ). IDM of 684 A is not a design current. Source: [DS-IRFP4568](https://www.infineon.com/dgdl/irfp4568pbf.pdf?fileId=5546d462533600a4015356310e811e5b); the thermal impedance is calculated and should be checked against the datasheet curve.
- Gate drive must be at least 10 V at these currents.

### 5.2 Bus-voltage ceiling

Peak current into a shorted barrel is proportional to bus voltage. The range below is for ESR of 25 → 15 mΩ per can.

| Bank and inductor | Amps per volt | Voltage for 1.4 kA | Current at 30 V |
|---|---|---|---|
| Six cans, 2 µH | 66–73 | 19–21 V | 2.0–2.2 kA |
| Six cans, 1 µH | 78–88 | 16–18 V | 2.3–2.6 kA |
| Two cans, 2 µH | 35–42 | 34–40 V | 1.1–1.2 kA |
| Two cans, 1 µH | 41–50 | 28–34 V | 1.2–1.5 kA |

**Rule:** never charge above the voltage at which a dead short stays inside the FET limit. Two cans with 2 µH is safe for 4+4 across the whole 0–30 V range and is the first-light configuration.

### 5.3 Hard turn-off voltage

Opening the high side under load raises the drain voltage by three terms:

\[
V_\text{DS,peak} \approx V_\text{bus} + I\sqrt{\frac{L_\text{bank}}{C_\text{film}}} + L_\sigma \frac{di}{dt}
\]

- **Bank-to-film pump.** Current in the stray inductance between the electrolytics and the film cans carries on into the film cans. With 60 nH and 40 µF that is 58 V at 1.5 kA.
- **Commutation spike.** The current fall is set mainly by source inductance inside the gate loop, not by the gate resistor. Estimated 50–180 V for four FETs across 25–45 nH.
- **Budget:** keep the sum under about 120 V on 150 V parts. Plausible at ≤30 V and 1.4 kA; unproven at 56 V.
- Keep the electrolytics close to the film cans, and measure both inductances from ringing before using truncated mode ([`TestPlan.md`](TestPlan.md), T2).

### 5.4 Exit current

If the slug leaves with current still flowing, ½·L·I² becomes a muzzle arc aimed at the deposit.

- Choose bank, inductance and voltage so the current has ended before exit. The script reports exit current and the energy behind it.
- The freewheel tail lasts about L/R. A large `L_series`, including augmenting turns, lengthens it.
- Model examples: 0.01 J at exit for six cans at 18 V with a 0.5 mg slug; 0.66 J with eight augmenting turns at 22 V; 4.4 J at 55 V.

### 5.5 Bus voltage

56 V maximum with the 5KP58A (58 V standoff, 64.4 V minimum breakdown).

## 6. Augmentation and the Driver

Augmentation is described in [`EM-CSAM-ConceptTechnical.md`](EM-CSAM-ConceptTechnical.md) §3.6 and built into the head ([`RailgunHeadPrototype.md`](RailgunHeadPrototype.md)). What it asks of the driver:

- **Permanent magnets** ask nothing electrically. They add about 0.4 mN per amp at 0.8 T. Conditioning must happen in the magnet-free zone at the breech, because any unipolar current in the field pushes the slug.
- **Series augmenting turns** are part of `L_series`: wind 4–8 flat turns over and under the rails and count their inductance (about 2.6 µH for eight) and resistance (about 6 mΩ) in the loop. They cut the current needed for a given force, which is what four FETs per leg are short of. They lengthen the freewheel tail (§5.4).

| Six cans, idealised | 1 mg | 0.5 mg | Peak |
|---|---|---|---|
| 18 V, 1 µH, plain | 106 m/s | 207 m/s | 1.38 kA |
| 18 V, 1 µH, 0.8 T magnet | 139 m/s | 336 m/s | 1.38 kA |
| 22 V, 8 turns + magnet | 320 m/s | 526 m/s | 1.00 kA |

The earlier bypass relay across `L_series` is gone. Its contact resistance (75 mΩ initial) cannot shunt a milliohm coil, and a closed or welded contact at launch would remove the inductance that limits the current.

## 7. Control and Sequencing

A small dedicated sequencer (RP2040 class) is required. Printer firmware cannot time 100–700 µs pulses with hardware limits and a fast abort. The printer controller sends "fire" and parameters across an isolated link.

Sequence for one shot:

1. **Pre-flight.** Gate supplies above 10 V. Bus voltage at or below the ceiling for the populated FET count. Rail-to-rail resistance open with no slug (the bore metallises with use).
2. **Feed and compact** the slug.
3. **Condition.** Close the ballast path; log slug voltage and current; stop on target resistance, energy limit or time limit.
4. **Charge** to the launch voltage.
5. **Launch.** One high-side pulse. Abort if no current appears within about 30 µs.
6. **Record.** Current from the Rogowski channel, muzzle voltage, bank voltage before and after, photogate times.
7. **Recover.** Re-zero the ACS772. Recharge.

Voltage, pulse length and the conditioning limits are parameters, so materials and barrels can be explored without hardware changes.

## 8. Protection and Measurability

- **Hardware maximum on-time** on the high-side command (about 2 ms), independent of firmware. It sits on the driver's input A, not on EN.
- **Fast over-current latch** fed from the Rogowski channel.
- **Gate-supply supervisor:** both isolated rails above 10 V, or EN stays low. The driver's own lockout is about 6 V and will not protect the FETs.
- **Dead-time interlock** set by a resistor on the driver's DT pin; never left open.
- **DC fuse** at the source, rated for the bus voltage. The charge resistor is never jumpered on a battery.
- **Bleeder** fitted permanently, plus a low-value dump resistor. The bleeder's time constant is 14–42 s.
- **Launch current is not visible to the ACS772** (±200 A). It measures conditioning current only.
- **Test points** for bus voltage, switch node, gate signals, muzzle voltage and the Rogowski signal.
- **People:** enclosure, backstop, eye protection, E-stop and fume extraction are part of the driver, not accessories. A 1 mg slug at 300 m/s will penetrate an eye, and the oil mist can ignite.

Values and wiring are in [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md).

## 9. Layout and Mechanical Constraints

- **Two circuits.** Logic, gate drive and sensing on a small board; pulse current on external copper bars. They meet only at the gates, the isolated-supply returns, the sense taps and the relay coil.
- **Commutation loop** (film cans → high side → low side → film cans) as small as it can be folded. This sets the turn-off spike.
- **Bank close to the film cans.** This sets the pump term of §5.3.
- **One star point** at the low-side sources and film negative. The low-side gate return is a Kelvin pair from the FET sources, with no second bond.
- **`L_series` on two-bolt pads**, or as the augmenting turns on the head.
- **Room for a second leg** in the rail B return, for a later full bridge.
- Board form factor still suits toolhead mounting: power in at one end, rails out at the other.

## 10. Scaling and Population

- **Capacitors:** two cans for first light, six for useful shots, twelve footprints for 48 V work.
- **FETs:** 4+4 to start (1.4 kA). 6+6 or 8+8 for the reference case in the concept document.
- **`L_series`:** swappable; 2 µH for first light, 1 µH or augmenting turns later.
- **Voltage:** ≤30 V on a bench supply first; 48–56 V with a pack and a DC-rated charge switch later.

**Two-switch asymmetric bridge.** Considered and not adopted. It has no shoot-through path and can terminate a pulse with −V, but it needs sixteen FETs for the same current, and running first light with the low-side gates held off gives the same shoot-through immunity with eight.

## 11. Development Sequence

1. Logic board alone: gate timing, dead time, supply droop, enable defaults, on-time limit.
2. Bars with two cans and 2 µH, bench supply at 5 V, into a copper strap. Calibrate the Rogowski channel against the ACS772.
3. Step the voltage up to the ceiling. Measure ring frequency and overshoot.
4. Solid armatures in a real barrel: velocity against ∫I²dt, with and without magnets.
5. Conditioning curves on real paste.
6. Full condition → launch sequence.
7. More cans, more FETs, more voltage, as the measurements allow.

The full procedure is [`TestPlan.md`](TestPlan.md).

## 12. Historical: the Original Resonant-Launch Concept

Version 0.1 of this document proposed delivering the launch energy as a high-frequency (≥200 kHz) resonant burst, by analogy with a solid-state Tesla coil turned to low impedance, with a tightly coupled transformer variant. The aims were strong skin effect in the rails and slug, and high current from a low-voltage bank.

What survives of it:

- **Resonance does shape the launch**, at the bank's own frequency rather than at 200 kHz.
- **A swappable series inductor** is still the main tuning part.
- **The half-bridge** is still the power stage for every mode.
- **High-frequency drive** is kept as the series-capacitor experiment of §4.4, where it can be studied at a few hundred amps.
- **The transformer-coupled variant** is not pursued. It needs AC through the rails, with the costs in §3.3.

## 13. Status

A conceptual architecture, re-baselined after review, with every number awaiting measurement. The power stage is unchanged from 0.1; the operating modes, limits, sensing and protection are new.
