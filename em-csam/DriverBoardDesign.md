# EM-CSAM Micro-Railgun Driver Board – Candidate Design v0.1

Open-source baseline for a 48–60 V capacitor-discharge driver intended for a 0.5 mm-class micro-railgun deposition head.
Designed for home fabrication, common parts, scaling flexibility, and easy forking.

## Design Goals
- Long, relatively thin board that sits on top of a ~1–2″ square × 4″ tall barrel assembly
- Power / logic entry at the top, rail connections at the bottom
- 12 capacitor positions + 8 MOSFET positions for easy scaling
- External thick copper bus bars for the main high-current pulse path
- Full safety and measurability features
- Commonly available parts with drop-in alternatives
- Compatible with BigTreeTech + Raspberry Pi control

## Electrical Ratings (First Target)
- Bus voltage: 48–60 V (63 V capacitors)
- Peak pulse current: 600–1200 A (set by number of MOSFETs populated)
- Pulse width: 50 µs – 1.5 ms
- Preconditioning: 5–50 kHz, 5–20 A
- Logic interface: 3.3 V / 5 V compatible

## Topology Summary
Capacitor bank → paralleled MOSFETs (main switch) → rails
Separate low-power preconditioning path that can drive the same rails
Opto-isolated gate drive from BTT/Pi
Current sense in return path + bank voltage sense
Bleeder, charge indicator, interlock dump, snubber, and freewheel protection

## Mechanical
- Board thickness 2.0–2.4 mm preferred
- Copper weight 2 oz minimum, 3 oz preferred
- Large bare copper pads at bottom edge for rail connection
- Each rail uses a 2-bolt clamp system with 1–2 mm copper spreader washers
- Candidate rail conductors: 2 mm × 2 mm square (can be widened later)
- High-current pulse path uses external copper bus bars (thicker stock or layers of the custom flexible strip)

## Scaling Approach
- 12 identical capacitor footprints in parallel – populate any number
- 8 TO-247 MOSFET footprints with individual gate resistors – populate any number
- Gate drive sized for the full complement
- External bus bars scaled independently of the PCB

## Schematic Notes (for implementation)
- Capacitor bank is a simple parallel group with local film decoupling
- Each MOSFET has its own gate resistor (2.2–10 Ω); optional gate-source resistor
- Single isolated gate-drive optocoupler (HCPL-3120 class) + optional buffer, fanned out to all gate resistors
- Current sense placed in the low-side / return path
- Preconditioning driver is independent and can share the output terminals through a current-limiting element
- Bleeder resistors across the bank, sized to discharge safely in a few seconds
- Interlock input forces a dump or prevents charging when open
- All high-current joints intended for bolted copper-washer connections
- Keep the capacitor → MOSFET → output loop as tight as practical; use external bus bars to achieve this on a home-made board

## Construction Notes
- Target is single-sided or simple double-sided with external bus bars (CNC isolation-milling friendly)
- Through-hole preferred for power components
- Large copper pours under the MOSFET array and capacitor bank
- Test points for gate, switch node, current, and bank voltage

## Future-Proofing
- Extra footprints already provided for scaling
- Clear separation of power and control domains so the design can be forked for multi-head, higher energy, or different switch technologies
- Bus-bar landing patterns accept a range of copper thickness

This document is the master design description for v0.1.
Schematic details are expanded in the companion schematic file.
