# Instructions for Future Grok – EM-CSAM Driver Board Project

## Project Goal
Design an open-source, home-buildable 48–60 V capacitor-discharge driver board for a micro-railgun material deposition head (EM-CSAM). The board sits on top of a ~1–2″ square × 4″ tall barrel, power/logic enters from the top, rails exit at the bottom.

## Current Design Baseline (v0.1)
- 12 parallel capacitor positions (4700 µF 63 V class)
- 8 paralleled TO-247 MOSFETs (IRFP4568 / IRFP4668 / IPT015N10N5 family or equivalents)
- Individual gate resistor per MOSFET
- External thick copper bus bars for the high-current pulse path
- Opto-isolated gate drive (HCPL-3120 class)
- Separate preconditioning path (5–50 kHz)
- Current sense + bank voltage sense
- Full safety set (bleeders, charge indicator, interlock, snubber)
- Bolted rail connections using 2-bolt clamps + 1–2 mm copper spreader washers
- Long-thin board form factor
- Prefer commonly available / drop-in compatible parts
- Scaling by population count (users populate only what they need)

## Preferred Tools & Formats
- Primary EDA: KiCad (latest stable)
- Project files must be valid, openable KiCad text files (.kicad_pro, .kicad_sch, .kicad_pcb)
- Documentation in Markdown
- All work should stay git-friendly

## Working Method with Local Agent
When continuing this project via API / local harness:
1. First check what files already exist in the working directory.
2. Prefer generating or editing real KiCad S-expression files over pure description.
3. Keep the design modular (hierarchical sheets recommended: Power Stage + Control/Drive).
4. Maintain the scaling approach (12 cap footprints, 8 MOSFET footprints with individual gate resistors).
5. External bus bars handle bulk current; PCB focuses on control, gate drive, sensing, and landing pads.
6. Ask for clarification only when a requirement-level decision is truly missing.
7. When generating files, make them as complete and loadable as possible, then note what still needs manual work in KiCad.

## Key Open Items / Next Priorities
- Create a real KiCad project skeleton
- Hierarchical schematic sheets (especially the repetitive Power Stage: capacitors + MOSFET array)
- Define exact net names and power domains
- PCB outline and major placement (top: inputs, middle: caps + FETs, bottom: rail pads)
- Bus-bar landing patterns and 2-bolt rail clamp footprints

## Design Constraints to Respect
- Home-makable path (CNC isolation milling + external bus bars is acceptable)
- Low inductance on the pulse path is critical
- Mechanical robustness for bolted connections
- Clear separation of high-current and logic domains
- Open-source friendly (common parts, well-documented, forkable)

## Tone & Style
Be practical, concise, and engineering-focused. Produce copy-pasteable files whenever possible. Prefer working code/files over long explanations unless the user asks for reasoning.

---
End of instructions. Continue from the current design baseline above.
