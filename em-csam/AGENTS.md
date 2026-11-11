# Handoff Notes – EM-CSAM Driver and Head

For any person or AI agent continuing this work. Formerly `ForFutureGrok.md`; rewritten after the November 2026 design review so it does not assume a particular assistant.

## Project Goal

Open-source, home-buildable hardware for a micro-railgun material deposition head (EM-CSAM): a pulse driver, a replaceable barrel, and the process knowledge to throw milligram slugs of metal at a substrate and have them stick.

## Read These First

| File | What it is |
|---|---|
| [`DesignReview-2026-11.md`](DesignReview-2026-11.md) | What the review found and why. Start here. |
| [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) | Driver architecture, modes and limits (v0.2) |
| [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md) | Nets, values, grounding, bring-up (v0.2) |
| [`UnifiedResonantShoppingList.md`](UnifiedResonantShoppingList.md) | Parts, with verified datasheet values (v0.2) |
| [`EM-CSAM-ConceptTechnical.md`](EM-CSAM-ConceptTechnical.md) | Physics: shot budget, slug resistance, augmentation (v0.3) |
| [`TestPlan.md`](TestPlan.md) | The experiments, in order |
| [`References.md`](References.md) | Sources with links and summaries |
| [`tools/shot_model.py`](tools/shot_model.py) | The model behind every number |

The v0.1 files (`DriverBoardDesign.md`, `DriverBoardSchematic.md`, `DriverShoppingList.md`) and most of `ControllerArchitecture.md` describe the earlier low-side-dump driver. They are kept for history and marked superseded.

## Current Baseline

- **One half-bridge of paralleled TO-247 MOSFETs** (`IRFP4568PBFXKMA1`), 4+4 first, on external copper bars.
- **Launch is one unipolar pulse** of 0.2–0.7 ms, shaped by the electrolytic bank and an air-core `L_series` of 0.5–3 µH. Natural frequency 0.7–4 kHz.
- **First light:** two cans, 2 µH, low-side gates tied to sources (the low side acts as diodes), bench supply at 5 V rising to 30 V, into a copper strap.
- **Conditioning** is ballast-limited current from a low bus through a relay and a power resistor, with slug resistance (from a muzzle voltage tap) as the endpoint.
- **Gate drive:** `UCC21551ADWR` on a SOIC-16 adapter, two isolated `R12P212S` gate rails, 10 µF + 0.1 µF at each rail on the adapter, 51 kΩ on the DT pin, a ≥10 V supervisor on both rails gating EN.
- **Sequencer:** an RP2040-class board on the power-return ground. The printer controller only sends FIRE, across an isolated link.
- **Sensing:** Rogowski loop on the return bar for launch current; ACS772 for conditioning current only; differential muzzle taps for slug voltage; dividers for bus and switch node.
- **Head:** C145 copper rails 3–4 mm wide in a lined clamshell, permanent magnets over the downstream 80 mm, a magnet-free conditioning zone at the breech.

## Rules That Must Not Be Undone

1. **Do not reintroduce a ≥200 kHz launch.** The circuit has no such resonance, the slug has no skin effect at that frequency, and the rails heat several times more. High frequency exists only as the low-current series-capacitor experiment in `UnifiedResonantDriver.md` §4.4.
2. **`L_series` is in series with the rails.** Earlier drawings showed it in parallel.
3. **No bypass relay across `L_series`.**
4. **Design to 450 A per FET for 0.5 ms**, not to IDM. 4+4 is about 1.4 kA.
5. **Obey the bus-voltage ceiling** for the populated bank and FET count (`UnifiedResonantDriver.md` §5.2). Six cans at 30 V exceed four FETs per leg.
6. **`UCC21551A` is the 5 V-UVLO part.** It is the right part and it needs the external supervisor.
7. **Logic ground is the power return**, bonded at one star point at the low-side sources. The galvanic boundary is between the sequencer and the outside world. Every PC link goes through a USB isolator.
8. **The ACS772 is not a launch sensor.** It clamps at ±200 A.
9. **Current must end before the slug exits.** Check exit current with the model.
10. **Copper rails with copper, tin and zinc powders.** Not aluminum.
11. **Two circuit parts:** logic, gate drive and sense on a board; pulse current on bars. Never through breadboard springs.
12. **Every number in these documents is a model result or a datasheet value until measured.** Say so when adding more, and regenerate tables with the script rather than by hand.

## The Builder's Kit (November 2026)

- On hand: the first-build kit from the shopping list (12 FETs, driver and spare, two isolated DC-DCs, ACS772, one T9AS relay, four 10 µF film cans, TVS, diodes, resistors, copper), **six or more** 4700 µF cans, and a few small pulse film capacitors (0.22–2.2 µF).
- Bench supply: a simple 0–30 V, 10 A unit. No higher-voltage supply yet.
- Not yet started: the board, the bar strip, any assembly.
- Still to buy: the "Additions for 0.2" in the shopping list.

Model expectation for this kit (idealised): a 1 mg slug reaches about 105–140 m/s plain or with magnets, about 320 m/s with augmenting turns and magnets; a 0.5 mg slug reaches about 340–530 m/s. Reaching the copper bonding window with 1 mg needs more FETs and voltage.

## Preferred Tools and Formats

- EDA: KiCad (latest stable). Project files must be valid, openable KiCad text files.
- Documentation in Markdown, git-friendly.
- Calculations in `tools/shot_model.py` (standard library only). Run `python3 em-csam/tools/shot_model.py selftest` after changing it, and `tables` to regenerate the numbers quoted in the documents.
- Sources go in `References.md` with a link and a short summary, and are cited inline by ID where a claim is made. Mark anything read only as an abstract or a secondary copy, and list what was not found.

## Working Method

1. Check what exists before writing. Prefer editing the live documents over adding new ones.
2. Once schematic capture starts, prefer real KiCad files over more description. Hierarchical sheets: Power Stage (bank, half-bridge, `L_series`, rails, ballast path) and Control (driver, gate rails, sequencer, protection logic, sensing).
3. Design for 12 capacitor positions and 8 FETs per leg; populate fewer.
4. External bars carry the pulse. The board carries control, gate drive, sensing and landing pads.
5. Through-hole first. Surface-mount exceptions: the UCC21551 on its adapter and the ACS772.
6. The breadboard placement in `UnifiedResonantSchematic.md` §9 is a bring-up sketch, not a layout.
7. Ask only when a requirement-level decision is missing.
8. When a measurement comes in, update the assumption table in `DesignReview-2026-11.md` §9 and the script defaults, then regenerate the tables.

## Open Items, In Order

1. Buy the additions. Build the paste-resistance fixture (TestPlan T0); it needs no driver.
2. Measure ESR and capacitance of every can.
3. Build the logic board on a breadboard and prove the enable default, on-time limit and supervisor (T1).
4. Build the bar strip; fire into a strap from 5 V upward; calibrate the Rogowski channel (T2).
5. KiCad project skeleton and hierarchical schematic from `UnifiedResonantSchematic.md` §2–3.
6. Head with liner, magnets and muzzle taps; solid-armature velocity tests (T3).
7. Conditioning curves on real paste (T4), then regime shots (T5) and deposits (T6).
8. Later: PCB outline and placement; second leg; 48–56 V operation with a DC-rated charge switch.

## Design Constraints to Respect

- Home-makable path (CNC isolation milling plus external bars is acceptable).
- Low inductance in the commutation loop and between the bank and the film cans.
- Mechanical robustness for bolted connections.
- Open-source friendly: common parts, well documented, forkable.
- A 48 V battery as the eventual charge reservoir; the pack never supplies the launch pulse directly.
- Safety equipment is part of the design: enclosure, backstop, eye protection, E-stop, fume extraction.

## Tone and Style

Practical, concise, engineering-focused. Produce files that can be used directly. State what is assumed and what is measured.
