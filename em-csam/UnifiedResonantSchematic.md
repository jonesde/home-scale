# Schematic Description – Unified Resonant Bridge Driver Board
EM-CSAM Micro-Railgun
Alternate driver: single half-/full-bridge for preconditioning + ≥200 kHz resonant launch

## 1. Purpose of this Document

Provide a clear, hierarchical schematic description and best-guess component guidance sufficient to begin schematic capture and PCB layout. The design implements one low-inductance power stage that operates in two modes:

- Preconditioning: lower frequency (~10–50 kHz), moderate current, L_series bypassed.
- Launch: short high-current resonant burst ≥200 kHz with external swappable L_series in circuit.

Target bus voltage class remains 48–60 V for early work (adjustable later). Peak launch current capability should be scalable into the high hundreds of amps by population of parallel devices. Layout must prioritize minimal high-current loop area.

## 2. Top-Level Blocks

1. DC input & charging / bus management
2. Pulse capacitor bank (C_tank)
3. Half- or full-bridge power stage (paralleled MOSFETs)
4. Gate drive & local protection
5. L_series interface + bypass path
6. Rail output interface
7. Current / voltage / temperature sensing
8. Control logic & MCU interface (BTT or equivalent)
9. Auxiliary power & housekeeping

Optional: separate low-power ignition/high-voltage tick generator (not required for first revision).

## 3. Block Descriptions and Candidate Parts

### 3.1 DC Input & Charging

- Input: 48–60 V nominal DC (wall supply with bulk capacitance or battery array).
- Reverse-polarity protection (series MOSFET or ideal-diode controller).
- Soft-start / inrush limiting.
- Charging path to the pulse capacitor bank: current-limited resistor, active current source, or simple buck pre-regulator.
- Bus voltage sense for MCU.

**Candidate direction**
- Input TVS and bulk electrolytic/film for supply decoupling.
- Ideal-diode controller or discrete P-channel/N-channel reverse protection.
- Charge current limit sized so the bank reaches target voltage in an acceptable time without excessive supply stress.

### 3.2 Pulse Capacitor Bank (C_tank)

- Modular parallel positions (design for up to 12 footprints).
- Pulse-rated film capacitors preferred for low ESR/ESL and high surge current; low-ESR electrolytics or hybrids acceptable for early prototypes if ripple and life are accepted.
- Local decoupling directly at the bridge with high-quality film or ceramic.

**Candidate direction**
- Film pulse capacitors in the low-to-mid µF range per can, voltage rating ≥100 V (comfortable margin above 60 V bus and resonant rise).
- Populate number of cans to achieve the desired joule budget (\(\frac12CV^2\)).
- Footprints allow mixing values or leaving positions empty for scaling.

### 3.3 Power Bridge

**Topology recommendation for first revision: half-bridge**
(Full-bridge can be a later option if bipolar drive or higher effective voltage is needed.)

- High-side and low-side switch positions, each designed for multiple paralleled MOSFETs (target 4–8 devices per position).
- Kelvin source connections where possible for clean gate drive.
- Snubbers or RC clamps across each half-bridge leg.
- Bootstrap or isolated supply for high-side gate drive.

**Candidate MOSFET families (48–60 V bus, high pulse current)**
- 100 V or 120–150 V N-channel power MOSFETs with very low R<sub>DS(on)</sub> and robust pulse current ratings.
- Examples of commonly available directions: Infineon OptiMOS / StrongIRFET, Onsemi, Vishay, or equivalent low-R<sub>DS(on)</sub> 100 V class devices in TO-220, TO-247, or power-surface-mount packages that can be paralleled and heatsunk.
- Final choice by pulse-current rating, R<sub>DS(on)</sub>, package thermal performance, and availability.

Populate fewer devices for early low-current testing; scale up for full launch current.

### 3.4 Gate Drive

- Dedicated gate-driver ICs capable of strong peak source/sink current (several amps) for fast switching of paralleled MOSFETs.
- Half-bridge driver with integrated bootstrap or fully isolated drivers.
- Local gate resistors (per device or per group) for damping and current sharing.
- Desaturation or V<sub>DS</sub> sensing for over-current protection, feeding a fast fault latch that inhibits the drivers.

**Candidate direction**
- Industry-standard half-bridge drivers (IR21xxx family style, Infineon, TI, Analog Devices, etc.) sized for the chosen MOSFET gate charge and desired rise/fall times.
- Isolated supply or bootstrap dimensioned for the maximum duty and frequency of preconditioning mode.

### 3.5 L_series Interface & Bypass

- Two heavy, low-inductance terminals or bus-bar pads for the external series inductor.
- Bypass path that reliably shorts those terminals during preconditioning.

**Bypass options**
- Early prototypes: robust relay or manual shorting bar.
- Later: paralleled MOSFETs or a solid-state crowbar-style switch rated for the preconditioning current and the voltage present when open.

Bypass control is a digital output from the MCU (with appropriate level shifting and drive).

### 3.6 Rail Output Interface

- Heavy copper or external bus-bar connection points sized for the peak launch current.
- Mechanical interface consistent with the existing toolhead / breech rail connection (bolted pads, copper washers, etc.).
- Optional current-sense shunt or Hall / CT sensor in the return or high-side path.
- TVS or clamp devices at the output for inductive kick and resonant overshoot protection.

### 3.7 Sensing

- Bus voltage divider (scaled to MCU ADC range).
- Bridge / rail current sense (shunt + amplifier or current transformer / Hall sensor).
- Temperature sensors on the MOSFET heatsink or board copper near the bridge.
- Optional rail-voltage sense for diagnostics.

All sense signals filtered and protected before reaching the MCU.

### 3.8 Control & MCU Interface

- Logic-level inputs from the main controller (BTT or equivalent):
  – PWM / gate-drive command
  – Mode select or separate precondition vs launch enables
  – Bypass control
  – Fault reset
- Fast fault output back to MCU (active on desaturation, over-current, over-temperature, etc.).
- Optical isolation or careful level translation if the MCU ground and power ground are separated.

Firmware responsibilities (not schematic, but required for function): frequency selection, duty/burst length, current-limit thresholds per mode, sequencing (precondition → bypass open → launch burst), and fault handling.

### 3.9 Auxiliary Power

- Local regulators for gate-drive supply, sense amplifiers, and logic (e.g., 12 V / 5 V / 3.3 V as required).
- Derived from the main DC bus or a small auxiliary input.
- Adequate decoupling and sequencing so gate drive is stable before the power stage is enabled.

## 4. Mode Configuration (Schematic-Level)

**Preconditioning**
- Bypass closed.
- L_series shorted out of the power path.
- Bridge driven at moderate current, lower frequency (10–50 kHz class).
- Current limit set to the moderate range.

**Launch**
- Bypass open.
- L_series in circuit.
- Bridge driven with a short, high-current resonant burst at the frequency set by C_tank and L_total.
- Current limit / desaturation thresholds raised to the launch value.
- Burst length (number of half-cycles) controlled by the MCU.

## 5. Protection Summary

- Reverse-polarity input protection.
- Bus over- and under-voltage detection.
- Fast desaturation / over-current on the bridge.
- Gate-drive under-voltage lockout.
- Snubbers / clamps for resonant overshoot and inductive spikes.
- Thermal monitoring.
- Hard inhibit of gate drive on any critical fault until MCU reset.

## 6. Layout Directives (for schematic → PCB)

- Treat the loop C_tank → bridge → L_series/bypass → rails as a single high-current, low-inductance path; place components to minimize enclosed area.
- Kelvin connections for gate drive and current sense where practical.
- Separate power and signal returns with controlled joining strategy.
- Provide clear, labeled test points for bus voltage, bridge current, gate signals, and rail output.
- Mechanical mounting and rail-terminal placement consistent with toolhead constraints (power entry preferred from one end, rail connections from the other).
- Single-sided PCB with external bus bars remains acceptable for home fabrication; multi-layer is fine if available.

## 7. Scaling Notes

- Capacitor bank: populate 1–12 positions according to joule requirement.
- MOSFET parallel count: start low for bring-up; increase until launch current and thermal margins are met.
- L_series: external and swappable — primary means of frequency tuning.
- Bypass: simple for first articles; solid-state later if high repetition rate is required.
- Voltage class: 48–60 V baseline; component footprints should allow later migration to higher bus voltage if experiments demand it (with appropriate part substitution).

## 8. Suggested Bring-Up Order

1. Auxiliary supplies and MCU interface (no high power).
2. Gate-drive timing and dead-time verification into dummy loads.
3. Low-voltage, low-current bridge test with bypass closed (preconditioning path).
4. Capacitor bank charging and bus monitoring.
5. Controlled moderate-current preconditioning into a resistive or dummy rail load.
6. Install L_series, open bypass, verify resonant frequency and short low-energy bursts.
7. Increase energy and current stepwise while monitoring device temperatures, voltage overshoot, and waveform quality.
8. Full sequencing with real barrel and slurry once electrical behavior is stable.

## 9. Breadboard Placement Sketch

Placement only — no jumper list. First-build populate (8 MOSFETs, not 16). Parts match [`UnifiedResonantShoppingList.md`](UnifiedResonantShoppingList.md).

**This is a bring-up jig, not the PCB.** An eventual board will look quite different: tighter gate loops, Kelvin sources, pours or bars under the FETs, and no solderless contacts. Do not copy these row numbers into KiCad.

Two physical pieces, same split as the shopping list:

1. **Logic breadboard** — 12 V / 5 V / 3.3 V, UCC21551 on a PA0006, MCU header, dividers, sense *signals*, relay *coil*.
2. **High-current bar strip** — pack, Schottky, bank, FETs, `L_series` / bypass, rails, ACS772 *current* path. Never through breadboard springs.

They meet only at a short gate-lead header, isolated-supply returns, sense taps, and the bypass-coil drive.

Convention: top of the breadboard drawing is the MCU / BTT end; bottom is the gate-header facing the FET bars. Empty rows omitted. DIP bodies span the gutter as multi-row blocks.

### 9.1 Logic breadboard

Standard 830-point view. Power rails along the long edges. Columns `a–e` and `f–j` are the two 5-hole strips.

> ```
>  +12 / +5   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
>  GND        ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
>                a b c d e   f g h i j
>
>  1–3        [ MCU / BTT header              ]  PWM, EN, bypass, fault, 3.3 V, GND
>
>  5–7        [ L7805 + 5 V decouple          ]  house 5 V for ACS772 / TMP36
>                                                (AMS1117-3.3 beside if needed)
>
>  9–16       [ UCC21551ADWR on PA0006        ]  isolated half-bridge driver
>              (16-pin DIP adapter, 300 mil)
>
> 18–21       [ R12P212S  #1  (low-side 12 V) ]  isolated SIP → driver VDDB
>
> 23–26       [ R12P212S  #2  (high-side 12 V)]  isolated SIP → driver VDDA
>
> 28–32       [ bus divider 220k / 10k        ]  BAT85 clamps on the tap
>              [ + charge LED                 ]
>
> 34–37       [ rail divider 220k / 10k       ]  BAT85 clamps on the tap
>
> 39–40       [ TMP36  (signal only)          ]  second sensor is on the FET bar
>
> 42–44       [ ACS772 signal pins only       ]  VCC, GND, VIOUT — not the current tabs
>
> 46–48       [ relay coil + NPN + flyback    ]  contacts live on the bar, not here
>
> 50–53       [ gate / isol-12 V header       ]  HO, LO, HS 12 V, LS 12 V, returns
>                                                short leads toward the FET gates
> ```

| Rows | Part | Notes |
|------|------|-------|
| 1–3 | MCU / BTT header | Logic only. No 48 V. |
| 5–7 | L7805 (+ optional 3.3 V LDO) | From isolated 12 V or a small aux. |
| 9–16 | UCC21551 + [PA0006](https://www.digikey.com/en/products/detail/chip-quik-inc/PA0006/5014721) | Wide SOIC-16 on 300 mil adapter. Dummy gate load (spare FET or ~10 nF) for first dead-time check — **no pack connected**. |
| 18–26 | Two R12P212S | One per driver secondary. Keep secondaries off the breadboard GND except at the intended returns. |
| 28–37 | Dividers + BAT85 + LED | 3.3 V ADC ratio. Clamps catch spikes only. |
| 39–44 | TMP36, ACS772 signals | Hall *body* is on the return bar. |
| 46–48 | T9AS coil drive | 12 V coil. Power contacts stay on the `L_series` pads. |
| 50–53 | Gate header | Shortest practical leads to the TO-247 gates. `Rg` / `Rgs` sit at the FETs, not here. |

### 9.2 High-current bar strip

Not a breadboard. Fold this loop as small as the parts allow. First build: 4 high-side + 4 low-side TO-247s.

> ```
>  PACK+ ── Schottky ── HS25 10 Ω ── C_bus (2× 100 V snap-in)
>                           │              + 4× 10 µF film at the legs
>                           │              + 5KP58A on the bus
>                           │
>                           ├── HS FETs (Q1–Q4) ─┬── L_series pads ── RAILS
>                           │                    │    ├ bypass relay contacts
>                           │                    │    └ or copper shorting bar
>                           └── LS FETs (Q5–Q8) ─┘
>
>  PACK− / return bar  ──────── ACS772 current tabs ─────────────┘
>       bleeder across the bank    5KP58A at the rail pads
>       MUR1560 clamps at the legs
> ```

| Position | Part | Notes |
|----------|------|-------|
| Pack + | MBR20100CT-E3/4W | Charge path only. Anode(s) to pack +, cathode to bus. |
| After Schottky | HS25 10 Ω | Soft-charge. May be jumpered once the bank is up. |
| Mid-bar | 2× 100 V electrolytics + 4× 10 µF film | Film right at the FET drains/sources. |
| Bridge | 4 HS + 4 LS IRFP4568, isolated tabs | `Rg` / `Rgs` / C0G at each gate. Heatsink bar, tabs **not** common. |
| After bridge | `L_series` 2-bolt pads | Relay or copper short across the pads for preconditioning. |
| Far end | Rail clamps (same as the print head) | Second 5KP58A here. |
| Return break | ACS772 current terminals | Signal pins fly to breadboard rows 42–44. |
| Across bank | Bleeder (hardwired) | Not a jumper that can fall out. |

### 9.3 First electrical bring-up on this placement

Follow §8, but with this split: steps 1–2 entirely on the breadboard (dummy gates). Do not energize the bar strip until dead time is verified. Then bring the pack up through the Schottky and charge resistor with the bleeder already fitted.

---

## 10. Status

This schematic description defines a unified resonant-bridge driver that collapses separate preconditioning and launch power stages into one flexible half- or full-bridge architecture. External L_series + bypass provides frequency agility and mode switching. Component directions favor commonly available, robust parts suitable for a 48–60 V high-current pulsed application and for iterative home or small-lab construction.

§9 is a **breadboard / bus-bar placement sketch** for first bring-up only. The eventual PCB (or milled board + bars) will not follow those row numbers.

Next concrete step: schematic capture following the block hierarchy above, followed by a low-inductance layout that respects the mechanical interface to the micro-railgun toolhead.
