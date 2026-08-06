# EM-CSAM Driver – Schematic Description v0.1
(Textual schematic / checklist for KiCad or equivalent)

## Sheet 1 – Power Stage

### Capacitor Bank
- 12 parallel positions (C1–C12) 4700 µF 63 V low-ESR electrolytic
- Parallel film decoupling capacitors (100 nF–1 µF) distributed across the bank
- Bleeder resistors across the whole bank
- Charge indicator LED + series resistor
- Soft-charge / current-limited input from 48–60 V supply

### Main Switch
- 8 × TO-247 N-channel MOSFETs (Q1–Q8) in parallel
  Recommended families: IRFP4568, IRFP4668, IPT015N10N5 or equivalents
- Individual gate resistor Rg for each MOSFET (2.2–10 Ω)
- Optional Rgs (10 kΩ) on each device
- Drain bus and Source/return bus implemented with wide pours + external bus-bar pads
- Snubber network (RC or RCD) across the switch
- Freewheeling diode or TVS from output to return

### Current Sense
- Hall sensor (ACS77x / ACS78x / ACS37200 class) or low-inductance shunt in the return path
- Sense output brought to logic-side connector (isolated or differential as needed)

### Rail Outputs
- Two large bare-copper contact pads at the bottom edge of the board
- Each pad designed for 2-bolt clamping of 2 mm × 2 mm (or wider) square rail stock
- 1–2 mm copper spreader washers used on both cable/rail and PCB sides

## Sheet 2 – Control & Drive

### Gate Drive
- Isolated DC-DC module providing 12–15 V for the driver
- HCPL-3120 / HCPL-J312 (or pin-compatible) gate-drive optocoupler
- Optional buffer (TC4420 / UCC27511 class) after the optocoupler
- Single drive signal fanned out through the individual gate resistors to Q1–Q8
- Input side of optocoupler driven from BTT/Pi FIRE signal (with series resistor)

### Preconditioning Path
- Independent H-bridge or discrete half-bridge driver
- Driven by PWM signal from BTT/Pi
- Output connected to the same rail terminals through a current-limiting resistor or small inductor
- Frequency range 5–50 kHz, current 5–20 A

### Logic Interface
- Opto-isolated or buffered inputs: FIRE, Precondition PWM, Enable / Interlock
- Outputs: Bank voltage sense, Current sense, optional status / fault
- 5 V or 12 V logic power input
- Clear separation from the high-current domain

### Protection
- Hardware path from over-current or interlock that can inhibit the gate drive or dump the bank
- Visible charge indicator
- Test points on gate drive, switch node, bank voltage, and current sense

## Implementation Notes for KiCad
- Use hierarchical sheets if desired (Power Stage + Control)
- Create a custom MOSFET symbol with gate-resistor already attached, then instantiate 8 times
- Capacitor bank can be a single hierarchical block with 12 parallel caps
- Place large copper pours / zones for the drain and source buses
- Add mounting holes and bus-bar alignment holes early
- Design rules: respect 60 V clearances; prioritise low inductance in the pulse loop

This textual schematic is intended as a direct working checklist while drawing the real schematic in KiCad (or another open-source EDA tool).
