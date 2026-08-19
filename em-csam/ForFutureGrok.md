# Instructions for Future Grok – EM-CSAM Driver Board Project

## Project Goal
Open-source, home-buildable driver for a micro-railgun material deposition head (EM-CSAM). The **current baseline is the Unified Resonant Bridge**, not the older low-side dump. One half-bridge does preconditioning (~10–50 kHz, moderate current) and a short ≥200 kHz resonant launch burst. Energy is stored on a 48–60 V bus (battery pack is valid). The board sits on a ~1–2″ square × 4″ tall barrel: power/logic in from one end, rails out the other.

## Current Design Baseline (Unified Resonant, first revision)

Read these before editing anything:

- [`UnifiedResonantDriver.md`](UnifiedResonantDriver.md) — architecture
- [`UnifiedResonantSchematic.md`](UnifiedResonantSchematic.md) — blocks, bring-up, **§9 breadboard placement**
- [`UnifiedResonantShoppingList.md`](UnifiedResonantShoppingList.md) — parts actually being ordered

The v0.1 files (`DriverBoardDesign.md`, `DriverBoardSchematic.md`, `DriverShoppingList.md`) are the **previous** low-side-dump + separate H-bridge concept. Do not treat them as the live BOM or topology.

**What this variation is**
- Half-bridge first (not full-bridge). 4–8 TO-247s **per leg**; first build is 4+4 plus spares (`IRFP4568PBFXKMA1`).
- Two-tier capacitors: 100 V electrolytics as the **DC energy store**; 10–22 µF pulse film at the legs. A bank of 4700 µF **cannot** resonate at 200 kHz — do not size `L_series` as if it were the tank C.
- External swappable air-core `L_series` + bypass (relay or copper shorting bar) for preconditioning.
- Isolated dual gate driver: **`UCC21551ADWR` only (A suffix, 6.7 V VDD min)** on a wide SOIC-16 → DIP adapter ([PA0006](https://www.digikey.com/en/products/detail/chip-quik-inc/PA0006/5014721)). Do not buy `UCC21551C*` (13.5 V UVLO will sit dead on 12 V modules). Two isolated 12 V 2 W SIPs (`R12P212S`).
- Reverse polarity (rev 1): series Schottky `MBR20100CT-E3/4W` on the **charge** path, not an ideal-diode IC.
- Sense: ACS772 200 A (current tabs on the return bar; signal pins on logic), 220 kΩ/10 kΩ dividers + BAT85 clamps, TMP36.
- TVS: `5KP58A` axial (58 V standoff — fine for a 13s / “48 V” pack; 16s LFP wants `5KP64A`).
- HF decouple: radial C0G `C350C104F1G5TA` (0.1 µF 100 V). Not a substitute for the film cans.

**Two circuit parts (do not collapse this)**
- Logic / gate / sense: breadboard or later simple PCB.
- Pulse current: external copper bars (or a flat go/return pair). Never solderless-breadboard springs.
- They meet only at FET gates (`Rg`/`Rgs` at the FETs), isolated-supply returns, sense taps, and the bypass-coil drive.
- §9 of the schematic is a **bring-up placement sketch**. The eventual PCB will look different; do not copy those row numbers into KiCad.

## Preferred Tools & Formats
- Primary EDA: KiCad (latest stable)
- Project files must be valid, openable KiCad text files (`.kicad_pro`, `.kicad_sch`, `.kicad_pcb`)
- Documentation in Markdown
- All work should stay git-friendly

## Working Method with Local Agent
1. First check what files already exist. Prefer the Unified Resonant trio above.
2. Prefer generating or editing real KiCad S-expression files over pure description **once schematic capture starts**.
3. Hierarchical sheets: Power Stage (bank, half-bridge, `L_series`/bypass, rails) + Control/Drive (UCC21551, isolated 12 V, sense, MCU).
4. Scaling: design for 12 cap positions and 8 FETs **per half-bridge leg**; first populate is smaller. Electrolytic positions are the DC bus, not a 200 kHz MMC.
5. External bus bars handle bulk current; PCB (or proto) focuses on control, gate drive, sensing, and landing pads.
6. Ask for clarification only when a requirement-level decision is truly missing.
7. When generating files, make them as complete and loadable as possible, then note what still needs manual work in KiCad.
8. Through-hole first. Do not sneak SMD onto the bring-up path except the UCC21551 (on PA0006) and the ACS772 CB package.

## Key Open Items / Next Priorities
- KiCad project skeleton (this is the next real design step)
- Hierarchical schematic from `UnifiedResonantSchematic.md` §§2–3
- Net names and power domains (logic GND vs power return; two isolated 12 V secondaries)
- Later: PCB outline and placement (power in one end, rails the other) — **not** a copy of the breadboard sketch
- Bus-bar landing patterns, 2-bolt rail clamps, `L_series` pad pair
- Measure / estimate `L_rails`, then wind the air-core `L_series` kit (50 nH–2 µH)
- First electrical bring-up: dummy gates, pack **disconnected**, then §8 order

## Design Constraints to Respect
- Home-makable path (CNC isolation milling + external bus bars is acceptable)
- Low inductance on the pulse path is critical
- Mechanical robustness for bolted connections
- Clear separation of high-current and logic domains
- Open-source friendly (common parts, well-documented, forkable)
- 48 V battery as the charge reservoir is intended; the pack does not supply the launch pulse through long leads

## Tone & Style
Be practical, concise, and engineering-focused. Produce copy-pasteable files whenever possible. Prefer working code/files over long explanations unless the user asks for reasoning.

---
End of instructions. Continue from the Unified Resonant baseline above.
