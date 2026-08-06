
# EM-CSAM Controller Architecture - Design and Build Notes

---

**For a 0.5 mm bore the practical hardware path is a capacitor-discharge pulse system controlled by the existing BigTreeTech + Pi 4 stack.** This is the cheapest and most hack-friendly route that still reaches the required peak currents (roughly 500–2000 A depending on pellet mass and target velocity) while keeping energy per shot low (tens to a few hundred millijoules kinetic + ohmic losses).

## Core Architecture (Single-Head First)

**Energy storage + switch (the pulse stage)** Use a local capacitor bank that is charged between shots and then dumped through low-inductance solid-state switches into the rails. Batteries or an AC-derived supply only recharge the bank; they do not supply the launch pulse directly. This keeps inductance low and peak current high.

- **Recommended starting bank**: 50–150 V, a few thousand µF of low-ESR film or electrolytic capacitors (or a modest bank of pulse-rated electrolytics). Total stored energy of 5–50 J is more than enough; you will only use a fraction of it per shot.
    - Cheap sources: surplus film capacitors, low-ESR electrolytic banks from old power supplies, or parallel strings of 63–100 V electrolytics from the usual Chinese vendors.
    - Layout: keep the high-current loop as short and wide as possible (laminated bus bars or thick copper sheet, minimal loop area). Mount the switches and caps as close to the toolhead as thermal and mass constraints allow.
- **Switch options ranked by cost/hackability for this current range**:
    1. **Paralleled discrete power MOSFETs or SiC MOSFETs** (best control and cheapest entry). Several TO-247 or similar devices in parallel can handle the pulse. SiC parts tolerate higher temperature and switch faster, which helps with the short pulse widths. Gate drivers can be simple TC442x-style or cheap isolated drivers triggered by an optocoupler.
    2. **IGBT modules / bricks** salvaged from welding inverters, induction cookers, or EV chargers. Higher current capability with fewer devices; gate drive is a bit more involved but well-documented in the hobby coilgun/railgun community.
    3. **SCRs / thyristors** for the simplest “dump everything” mode. Extremely robust and cheap, but you lose the ability to turn the current off early or shape the waveform. Good for first tests.

Modern SiC MOSFETs have become inexpensive enough that a paralleled discrete approach is now very accessible and gives the best flexibility for the multi-tier drive you want (pre-condition + shaped launch pulse).

**Charging the bank**

- Single-head: simplest is a small offline or boost converter from wall AC (or from the printer’s existing 24 V rail stepped up). A current-limited charge circuit + bleeder resistors is mandatory.
- Multi-head / rapid succession: a shared DC bus (battery pack or large PSU) that tops up local capacitor banks on each head between shots. Batteries shine here as bulk energy reservoirs; they do not have to deliver the microsecond–millisecond pulse themselves.

### Control from the BTT Board + Pi 4

The BTT MCU already has plenty of free GPIO, PWM, and communication pins. Klipper (or Marlin) can drive the system with almost no custom firmware:

- Use an [output_pin] or a short G-code macro to assert a logic-level trigger.
- Isolate it with an optocoupler (or a cheap digital isolator) that drives the gate-driver enable or SCR trigger.
- For waveform shaping or multi-pulse sequences, either (a) generate the timing on the Pi and send a digital pulse train, or (b) add a tiny secondary microcontroller (Arduino Nano, RP2040, or even a spare BTT auxiliary MCU) that receives a “fire” command and executes a pre-loaded current profile.
- Pre-conditioning (5–50 kHz, low amperage) can be handled by a spare stepper-driver channel, a small H-bridge, or a cheap Class-D / audio amplifier module driven by PWM from the board. This keeps the high-current path completely separate.

Current and voltage feedback (Hall-effect sensor or shunt + amplifier, plus a simple voltage divider on the bank) can be read by the Pi or an ADC on the secondary MCU for closed-loop charge control and safety cut-offs.

### Cost-Conscious Build Path

1. Start with a low-voltage (24–60 V) bank of paralleled low-ESR electrolytics + 4–8 paralleled MOSFETs. This is the safest and cheapest way to get to a few hundred amps for first tests.
2. Add a basic opto-isolated trigger from a free BTT pin.
3. Once the mechanical head and slurry feed are working, move to higher voltage / higher capacitance or SiC devices for the full current range.
4. Salvage IGBT modules or large film capacitors when you need more energy or multi-head capability.
5. Keep the high-current path physically separate from the BTT board; only logic-level or isolated signals cross the boundary.

### Battery Array vs AC + Capacitors

- **Single-head / early development**: AC-wall → rectifier/boost → capacitor bank is simpler, cheaper, and has no battery management overhead.
- **Multiple heads firing in rapid succession**: local capacitor banks on each toolhead, recharged from a common high-current DC bus. A battery pack (or large server PSU) is excellent for that bus because it can deliver continuous recharge current while the pulse energy itself still comes from the low-inductance capacitors. Pure battery-direct discharge into the rails is possible but fights inductance and internal resistance; the hybrid (battery charges caps, caps fire) is almost always better.

### Practical Notes for a Hack-Friendly System

- Energy per shot is small, so average power is modest if you limit pulse rate by thermal constraints on the rails and switches.
- Low inductance remains the dominant layout constraint—treat the switch–capacitor–rail loop like a high-current RF circuit.
- Safety essentials: bleeder resistors on every capacitor bank, mechanical or electronic interlocks, clear visual charge indicators, and never work on a charged system.
- The hobby coilgun / small railgun / electromagnetic-forming community has already solved most of the packaging, gate-drive, and protection problems; many of their open designs scale down cleanly to the energies you need.

This approach stays fully compatible with a stock BTT + Pi 4 control system, keeps the bill of materials in the “maker” price range, and gives you the current headroom and waveform control needed for both barrel-preserving and intentional-consumable modes at 0.5 mm. Once the single-head version is firing reliably you can replicate the pulse stage on additional heads and share the recharge bus.


---

## **Candidate single-head circuit (AC wall → BTT-controlled → rails)**

Here is a practical, inexpensive, hack-friendly topology that stays compatible with a stock BigTreeTech board + Pi 4, uses ordinary AC wall power, and keeps the high-current path simple and low-inductance. It is sized for the 0.5 mm bore targets we discussed (hundreds to low thousands of amps, 0.1–1 ms pulses).

### High-level block diagram

text

```
AC Mains
   │
   ├─ Fuse + EMI filter + isolation transformer (or isolated PSU)
   │
   ▼
Charging supply (current-limited, 50–150 V)
   │
   ▼
Pulse capacitor bank  ──┬── High-current switch (SiC MOSFETs / IGBT)
                        │         │
                        │         ▼
                        │    Rail A  ──► slurry / pellet ──► Rail B
                        │         │
                        └─────────┘  (return path, keep loop area tiny)

BTT GPIO / PWM  ──► opto-isolator ──► gate driver ──► switch gate(s)

Separate low-power path:
BTT PWM ──► small H-bridge / Class-D ──► (optional transformer) ──► rails
(for 5–50 kHz preconditioning, few–20 A)
```

### 1. Charging side (AC wall → capacitor bank)

- Start simple: a commercial isolated 48 V or 60–100 V power supply (server PSU, LED driver, or mean-well style) rated for a few amps continuous.
- Add a current-limiting resistor or a small active constant-current stage so the bank charges in 0.5–2 s without stressing the supply.
- Voltage sense (resistive divider + opto or isolated ADC) lets the Pi or BTT know when the bank is ready.
- Mandatory: bleeder resistors across the bank that discharge it safely in a few seconds when power is removed or an interlock opens.

This is far cheaper and safer than building a high-voltage offline converter from scratch for the first version.

### 2. Pulse capacitor bank

- 50–150 V, a few thousand µF of low-ESR film or good electrolytic capacitors.
- Total energy 5–30 J is plenty; you will only extract a fraction per shot.
- Physically mount the bank as close as practical to the switch and rails. Use wide copper sheet or laminated bus bars for the high-current connections.
- Parallel multiple capacitors to keep ESR and ESL low.

### 3. High-current switch (the critical part)

Two good starting options:

**A. Paralleled discrete SiC or silicon MOSFETs (most flexible & hack-friendly)**

- 4–8 TO-247 devices in parallel (or a couple of SiC half-bridge modules).
- Gate drivers: cheap isolated or bootstrap drivers (e.g. Si823x, or simple TC4420 + opto).
- Triggered by a single logic-level signal from the BTT via an optocoupler.
- Advantage: you can turn the current off early or shape the pulse with PWM/multiple edges.

**B. Single IGBT module or SCR (simpler, more robust)**

- Salvaged welding-inverter or induction-cooker IGBT brick, or a stud-mount SCR.
- Gate/trigger driven the same way through isolation.
- Advantage: fewer parts, higher surge rating. Disadvantage: harder to interrupt the current mid-pulse (SCRs especially).

Add a snubber (RC or RCD) across the switch and a freewheeling diode path so residual inductive energy has somewhere to go after the pellet leaves the rails.

### 4. Connection to the rails

- One side of the bank → switch → Rail A.
- Rail B → direct low-inductance return to the other side of the bank.
- Keep the entire high-current loop area as small as possible (ideally a few cm²). This is more important than almost any other layout detail.
- Use thick copper, multiple paralleled wires, or flexible laminated bus if the head moves.

Because the head is vertical and the pellet is viscous, gravity helps keep the material seated against the breech while the preconditioning stage runs; the launch pulse then accelerates it downward (or whatever print direction you choose).

### 5. Preconditioning path (separate, low power)

- A small H-bridge, Class-D audio amplifier module, or even a spare stepper-driver channel driven by a BTT PWM pin.
- Output coupled to the same rails (through a current-limiting resistor or small series inductor if needed).
- Frequency 5–50 kHz, current 1–20 A.
- This path can run for tens to hundreds of milliseconds while the capacitor bank is already charged, then the high-current switch fires.

### 6. BTT / Pi control interface

- One free GPIO or [output_pin] for the main “FIRE” trigger (opto-isolated).
- One or two PWM pins for preconditioning frequency/amplitude.
- Optional: another pin or ADC channel for bank-voltage feedback and a current-sense signal (Hall sensor or shunt).
- All high-voltage / high-current circuitry stays galvanically isolated from the BTT logic. Only the opto-isolated trigger and sense signals cross the boundary.

Klipper macros can sequence: precondition on → wait → fire → precondition off → recharge check.

### Safety & practical notes

- Enclose the capacitor bank and switch; high-energy capacitors can be dangerous.
- Bleeder resistors + visible charge indicator + interlock on the enclosure.
- Start with the lower-voltage (48–60 V) version and modest paralleled MOSFETs. You can raise voltage or add devices later.
- Measure actual loop inductance and current waveform early; that will tell you how aggressive you can be with di/dt.

This circuit stays entirely within reach of normal maker parts, uses the BTT board only for low-level control signals, and gives clean separation between the low-power preconditioning stage and the high-current launch stage. It is also easy to replicate later for multi-head setups (each head gets its own bank + switch, all charged from a shared DC bus).

---

## Parts list for initial 48-60V, AC Wall-driven Design

**48–60 V Single-Head Prototype Parts List**

This is a practical, inexpensive starting bill of materials focused on lower-power testing and early experiments (target capability roughly 300–800 A peak pulses at 48–60 V). Everything is chosen for availability from normal maker sources (AliExpress, Mouser, Digi-Key, Amazon, surplus) and easy paralleling later.

### 1. Capacitor Bank (Energy Storage)

|Qty|Part|Notes|Approx. cost|
|---|---|---|---|
|6–10|4700 µF 63 V low-ESR electrolytic (22×40 mm or snap-in)|Parallel for ~28–47 mF total. Low ESR important.|$1.5–4 each|
|2–4|100 nF–1 µF film capacitors (63–100 V)|Local decoupling right at the switch|$0.50 each|

**Stored energy** at 55 V with 40 mF ≈ 60 J (you will only use a small fraction per shot). Mount on a copper sheet or thick PCB with very short connections.

### 2. High-Current Switch

|Qty|Part|Notes|Approx. cost|
|---|---|---|---|
|4–6|IPT015N10N5 (or equivalent 100 V, ~1.5 mΩ, high-pulse current MOSFET) in TO-Leadless / HSOF or TO-247|Excellent low Rds(on). Parallel them.|$3–6 each|
|Alternative|IRFP4468, IRFP4568, or similar 100 V TO-247 high-current FETs|Easier to find / heatsink. Slightly higher Rds(on).|$2–5 each|
|1|Small heatsink or copper bar for the paralleled FETs|Pulse is short, but still helps|$5–10|

4–6 devices in parallel easily handle several hundred amps for sub-millisecond pulses when layout inductance is kept low.

### 3. Gate Drive & Isolation (from BTT)

|Qty|Part|Notes|Approx. cost|
|---|---|---|---|
|1|Optocoupler (HCPL-3120, FOD3182, TLP250, or similar gate-drive opto)|Isolates BTT GPIO from power side|$1–3|
|1|Gate driver IC (TC4420/TC4429, UCC275xx, or discrete totem-pole)|Provides strong gate current|$1–2|
|1|Isolated 12–15 V supply for gate drive (small DC-DC module or bootstrap)|Can be a cheap isolated 1 W module|$3–8|
|—|Gate resistors 2–10 Ω (one per MOSFET)|Damping|$0.10|

Trigger directly from a BTT [output_pin] or GPIO through the opto.

### 4. Current & Voltage Sensing

|Qty|Part|Notes|Approx. cost|
|---|---|---|---|
|1|Allegro ACS772 / ACS780 / ACS37200 or similar 100–200 A Hall sensor|Easy isolated current measurement for early tests|$5–12|
|Alternative|Low-inductance shunt (e.g. 0.5–1 mΩ) + differential amp|Cheaper, very accurate for pulses|$3–8|
|1|Resistive divider + opto or isolated amp for bank voltage|So the Pi knows when the bank is charged|$2|

### 5. Charging Supply (AC Wall)

|Qty|Part|Notes|Approx. cost|
|---|---|---|---|
|1|48 V or 60 V isolated power supply, 3–10 A (Mean Well, server PSU, LED driver, etc.)|Main energy source|$25–60|
|1|Power resistor or active current limiter (5–20 Ω, 20–50 W)|Soft-charges the bank|$3–8|
|1|Bridge rectifier + bulk capacitor if you start from raw AC (optional)|Only if not using a finished PSU|$5|

### 6. Protection & Snubbers

|Qty|Part|Notes|
|---|---|---|
|2–4|10–47 Ω + 0.1–1 µF snubber across the switch|RC or RCD|
|2|High-power bleeder resistors (e.g. 1–2 kΩ, 5–10 W) across the bank|Safety – discharges the bank|
|1|Freewheeling diode or TVS across the rails/switch|Catches inductive kick|
|1|Fuse or circuit breaker on the AC input||

### 7. Preconditioning Path (Low Power)

|Qty|Part|Notes|Approx. cost|
|---|---|---|---|
|1|Cheap H-bridge module or discrete MOSFETs + driver (e.g. BTS7960 style or IR2104 + FETs)|5–50 kHz, 5–20 A|$5–15|
|Optional|Small toroid or series inductor|If you want better current limiting|$2|

Driven directly from a BTT PWM pin.

### 8. Mechanical / Interconnect

- Thick copper sheet or bus bar for the high-current loop (bank → FETs → Rail A / return).
- Heavy-gauge wire or multiple paralleled wires only for the final short run to the toolhead.
- Screw terminals or Anderson-style connectors rated for high pulse current.
- Enclosure with interlock switch that dumps the bank when opened.

### Rough Total for a First Functional Prototype

**$80–160** depending on how much you already have and whether you buy name-brand or AliExpress parts. The biggest variables are the power supply and the number/quality of the MOSFETs.

### Suggested First Build Order

1. Capacitor bank + bleeder + charging supply (test charging and safe discharge first).
2. Gate drive + single MOSFET (verify clean switching into a dummy load).
3. Parallel the remaining MOSFETs and add current sensing.
4. Connect to a dummy resistive/inductive load that approximates the rail + slurry impedance.
5. Only then move to the actual rails and slurry.

This 48–60 V version gives you a large safety and debugging margin while still reaching useful pulse currents for 0.5 mm testing. You can later raise voltage, add more capacitance, or swap in higher-performance SiC devices without redesigning the control interface from the BTT board.

---

## Lead Flat Cable Design

```
Outer protective cloth tape
301/302 spring steel (tension side)
Kapton
Copper layer(s) + Kapton between them
Kapton
(optional second protective layer)
```

P**ut the spring steel on the outside of the bend (the tension side).** This puts the copper layers closer to the neutral axis or on the compression side, so the copper sees less stretching. The steel takes the tensile load and helps the whole stack return smoothly.

If you orient the finished cable so that the steel is always on the outside of the curve in normal machine motion, copper fatigue life improves significantly.

Look for **301 (or 302) stainless spring-temper strip** in 0.10–0.25 mm thickness and the same 1.5" width (or a bit narrower). 0.15–0.20 mm is a sweet spot for most people — stiff enough to smooth the flex without making the cable too springy or hard to route.

You can find it on Amazon, AliExpress, McMaster-Carr, or industrial suppliers as “301 spring temper stainless strip” or “301 full hard stainless steel strip.”

Because the connection is always bolted, you can treat the termination as a simple bolted sandwich:

- Fold or stack the end of the 0.3 mm foil a few times to build local thickness.
- Place a 1–2 mm copper plate (same width or slightly wider) on each side of the folded foil — these act as load-spreading “washers.”
- Put normal steel washers on the outsides and torque the bolt.
- The thick copper pieces distribute the clamping force, give a solid low-resistance face, and protect the thin foil.
- For maintenance you just peel the outer tape back and cut/expose more foil if the end ever needs re-terminating.

This is easy to make, fully inspectable, and avoids the risks of cold-crimping delicate foil.

**Short summary:**

Flexible high-current leads are made from multi-layer 0.32 mm (28 ga) copper strip, 1.5" wide, with Kapton insulation on each copper layer. A 301/302 spring-temper stainless strip is placed on the outside of the primary bend direction to take tensile stress and smooth flexing; the copper layers sit closer to the neutral or compression side. Outer cloth tape provides abrasion protection. At each end the copper foil is folded a few times for thickness, then sandwiched between two 1–2 mm copper plates that act as load-spreading washers. The stack is bolted with ordinary steel washers, giving a simple, low-resistance, fully serviceable termination that can be re-made by exposing more foil if needed.

```
Outer protective cloth tape
301/302 spring steel (tension side)
Kapton
Copper layer(s) + Kapton between them
Kapton
(optional second protective layer)
```

P**ut the spring steel on the outside of the bend (the tension side).** This puts the copper layers closer to the neutral axis or on the compression side, so the copper sees less stretching. The steel takes the tensile load and helps the whole stack return smoothly.

If you orient the finished cable so that the steel is always on the outside of the curve in normal machine motion, copper fatigue life improves significantly.

Look for **301 (or 302) stainless spring-temper strip** in 0.10–0.25 mm thickness and the same 1.5" width (or a bit narrower). 0.15–0.20 mm is a sweet spot for most people — stiff enough to smooth the flex without making the cable too springy or hard to route.

You can find it on Amazon, AliExpress, McMaster-Carr, or industrial suppliers as “301 spring temper stainless strip” or “301 full hard stainless steel strip.”

Because the connection is always bolted, you can treat the termination as a simple bolted sandwich:

- Fold or stack the end of the 0.3 mm foil a few times to build local thickness.
- Place a 1–2 mm copper plate (same width or slightly wider) on each side of the folded foil — these act as load-spreading “washers.”
- Put normal steel washers on the outsides and torque the bolt.
- The thick copper pieces distribute the clamping force, give a solid low-resistance face, and protect the thin foil.
- For maintenance you just peel the outer tape back and cut/expose more foil if the end ever needs re-terminating.

This is easy to make, fully inspectable, and avoids the risks of cold-crimping delicate foil.

**Short summary:**

Flexible high-current leads are made from multi-layer 0.32 mm (28 ga) copper strip, 1.5" wide, with Kapton insulation on each copper layer. A 301/302 spring-temper stainless strip is placed on the outside of the primary bend direction to take tensile stress and smooth flexing; the copper layers sit closer to the neutral or compression side. Outer cloth tape provides abrasion protection. At each end the copper foil is folded a few times for thickness, then sandwiched between two 1–2 mm copper plates that act as load-spreading washers. The stack is bolted with ordinary steel washers, giving a simple, low-resistance, fully serviceable termination that can be re-made by exposing more foil if needed.


---

## Oscilliscope Notes


**You’ll want a scope, but it doesn’t have to be extreme.** The frequencies and pulse widths involved are very manageable for a solid mid-range instrument, especially while you stay in lower-power test states.

### What you actually need to see

|Signal|Time scale|Key things to capture|Difficulty|
|---|---|---|---|
|Preconditioning (5–50 kHz)|ms–tens of ms|Waveform quality, amplitude, any distortion|Easy|
|Launch pulse current|50 µs – 1 ms total width|Peak value, rise time, flatness, ringing, tail|Medium|
|Switch voltage / rail voltage|same|Spikes, residual voltage, arcing, turn-off behavior|Medium–Hard|
|Gate-drive signal|10–200 ns edges|Clean turn-on/off, Miller plateau, ringing|Medium|
|Timing vs BTT trigger|overall sequence|Delay, jitter, prep-to-fire hand-off|Easy|

The launch pulse is the demanding one: short overall duration but potentially fast edges (especially with SiC) and high di/dt that produces inductive spikes and ringing.

### Recommended minimum specs (lower-power testing)

- **Bandwidth**: **100 MHz** (50 MHz can work for early low-di/dt tests; 100 MHz gives comfortable margin for edges and ringing).
- **Sample rate**: **≥ 500 MS/s**, preferably 1 GS/s.
- **Channels**: **4** is strongly preferred (voltage, current, gate, trigger/reference). 2-channel is usable but awkward.
- **Memory depth**: **≥ 1 Mpts** (more is better). You want to capture a full 1 ms pulse at high sample rate and still zoom into the leading edge.
- **Vertical range**: Able to handle ~1 mV/div up to at least 50–100 V/div with probes.
- **Triggering**: Edge + pulse-width; delayed or sequence trigger is a big quality-of-life improvement.

### Probes & current measurement (more important than the scope itself)

- Standard 10× passive probes for gate drive and low-voltage signals.
- **High-voltage differential probe** (very useful) for looking across the switch or between rails without creating ground loops.
- Current sensing options ranked by practicality for early tests:
    1. Low-inductance coaxial shunt or current-viewing resistor + voltage probe (cheap and accurate at these pulse widths).
    2. Hall-effect current probe rated for at least 100–300 A peak (plenty for lower-power work).
    3. Later: Rogowski coil or Pearson-style monitor when you go to higher currents.

### Practical “maker” recommendations

- Rigol DS1054Z / DS1104Z (or current 1000-series equivalents) — the classic affordable 4-channel 50/100 MHz workhorse.
- Siglent SDS1104X-E or SDS1202X-E — similar class, often better UI and memory.
- A clean used Tektronix or Keysight 100–200 MHz 4-channel from the secondary market is also excellent value.

You do **not** need 500 MHz+ or multi-GS/s deep-memory scopes for this project at the power levels you’ll start with. Those become useful only if you start chasing sub-20 ns edges or very high-frequency ringing in a fully optimized low-inductance layout.

### Probing advice that will save you pain

- Keep ground leads extremely short (or use spring-ground tips) when looking at fast edges.
- Prefer differential measurements on the high-current side.
- Start every new test at reduced bank voltage / smaller capacitance so a probing mistake doesn’t destroy the scope or the switch.
- Use the BTT trigger signal as the scope trigger source so everything is time-aligned.

With a 100 MHz 4-channel scope, a differential probe, and a decent way to measure current, you will be able to see every critical part of both the preconditioning stage and the launch pulse in lower-power test states. That is more than enough to iterate the circuit safely before you scale energy up.
