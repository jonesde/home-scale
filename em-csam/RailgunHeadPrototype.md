# EM-CSAM Railgun Print Head – Design Concept & Build Guide v0.2

**What changed in 0.2.** The clamshell is unchanged. Added after the November 2026 review: copper rails 3–4 mm wide, a bore liner, thin covers with magnet pockets, a magnet-free conditioning zone, optional augmenting turns, muzzle voltage taps, velocity ports and a breech plunger. These are collected in §1A. Reasons and sources: [`DesignReview-2026-11.md`](DesignReview-2026-11.md) (B1, B5–B7, B9, B10, C3, C7) and [`References.md`](References.md). None of the additions has been built.

## 1. Design Concept

### Goals
- Home-buildable on a good desktop CNC router (Genmitsu 3020-PRO Ultra class or better)
- Precise, repeatable rail geometry for early splat testing
- Easy rail replacement / servicing
- Good electrical isolation + reasonable thermal performance
- Rectangular exterior for simple mounting
- Architecture that can later evolve toward higher printable content

### Overall Architecture – Clamshell
The head uses a two-part clamshell design:

- **Bottom half**: Contains the precision channels that hold the rails. The rails are placed and then finish-machined in position.
- **Top half**: Completely flat mating surface. This provides a clean, continuous sealing and clamping face.
- The two halves meet on large, flat, machined surfaces so that clamping force produces good alignment and sealing.
- Outer form is left rectangular for easy fixturing, mounting, and optional addition of a metal exo-skeleton.

This arrangement gives several advantages:
- Rails can be installed and inspected easily
- Critical rail faces can be finish-machined *after* the bars are fixed in place (the most reliable way to get parallelism on a desktop CNC)
- The flat top half is simple to machine and can be replaced independently
- A metal exo-skeleton (aluminum plates or frame) can later be added around a thinner plastic core for higher rigidity without changing the internal geometry

### Rail Geometry & Materials
- Move away from 2×2 mm square wire.
- Use rectangular copper bar stock for better straightness and easier finishing.
- Primary recommendation: Tellurium copper (C145). Avoid C110 with oil carriers: it is open to hydrogen embrittlement. See [`RailMaterial.md`](RailMaterial.md).
- Rail width 3–4 mm. Wider rails lower the inductance gradient. They do still carry some pulse current (the 0.2–0.7 ms pulse reaches 3–6 mm into copper and falls off smoothly; [skin-effect](../quantum-systems/library/skin-effect.md)), so the case for narrow rails rests on L′, not on a skin-depth cut-off. Behind the slug the current sits in a sub-millimetre layer at any rail width (velocity skin effect).
- Experimental thicknesses: 0.5 mm, 1.0 mm, and 1.5 mm.
- Target bore height experiments: ~0.5 mm to 1.5 mm (0.5×0.5 mm and 0.5×1 mm are of particular interest for lower drive current).

### Body Materials
| Priority | Material     | Notes                                      |
|----------|--------------|--------------------------------------------|
| Primary  | PEI (Ultem)  | Best balance of machinability, insulation, cost, and temperature **for the structural shell**. Not for the surface facing the bore; see the liner in §1A. |
| Alternative | PEEK      | Higher continuous temperature capability. Same caveat. |
| Early testing | UHMW / HDPE | Acceptable only for very early mechanical trials |

### Key Design Features
- Flat mating surfaces on both halves for sealing and alignment
- Sufficient wall thickness around the barrel for firing rigidity
- Mounting holes placed so they do not interfere with the bore or clamping zone
- Optional metal exo-skeleton for increased stiffness
- Electrical connection at the top of the rails to the driver board (bolted interface)
- Designed so the internal geometry can later be adapted to printed or hybrid construction

## 1A. Additions from the November 2026 Review

### Bore liner

PEI and PEEK track easily under arcing: both have a comparative tracking index of only 100–174 V, against 600 V or more for PTFE and polyethylene, and PEEK's arc resistance is about 40 s against 200–220 s for acetal ([MT-CTI](https://www.cmc.de/en/cti-kriechstromfestigkeit), [MT-ARC](https://www.specialchem.com/plastics/guide/arc-resistance)). Keep PEI as the shell and face the bore with something else.

| Liner | Good for | Notes |
|---|---|---|
| Mica sheet (0.2–0.5 mm) | First choice for the flat top cover and channel floor | Cheap, arc-tolerant, already in the barrel-manufacture notes. |
| Fired pyrophyllite ("lava") | Machined inserts | Machines soft, then fires at 1010–1095 °C to a hard ceramic ([MT-LAVA](https://professionalplastics.com/LAVA?XLT_TO=en)). |
| Macor or boron nitride | Machined inserts where budget allows | Macor to 800 °C; boron nitride has the better thermal shock ([MT-MACOR](https://accuratus.com/macormats.html)). |
| Acetal (POM) or PTFE | Deliberately ablative liners for the carrier-flash regime | They erode cleanly and release gas, as in arc chutes ([MT-ABLATE](https://link.springer.com/article/10.1007/s11090-024-10451-1)). PTFE releases fluorine compounds; ventilate. |

The bore will also be metallised by its own vapour. Measure rail-to-rail resistance with no slug before each series, and clean when it falls.

### Thin covers and magnet pockets

A field through the bore, perpendicular to the rail plane, adds a force of B × current × gap. At 0.8 T and a 0.5 mm gap that is 0.4 mN per amp, which is comparable to the rails' own force at this scale ([`EM-CSAM-ConceptTechnical.md`](EM-CSAM-ConceptTechnical.md) §3.6).

- **Covers over the bore:** 1–1.5 mm thick (liner plus a thin web), so the gap between magnet faces is 3–4 mm.
- **Magnets:** NdFeB bars about 10 mm wide and 5 mm thick, magnetised through the thickness, in pockets above and below the bore with opposite poles facing each other. SH grade (150 °C); standard grades weaken above 80 °C.
- **Yoke:** a mild-steel strip joining the backs of the upper and lower magnets around one side raises the field. Expect 0.6–0.9 T; measure it with a gaussmeter.
- **Polarity:** the magnet force must point at the muzzle. Check with a few amps through a loose wire laid across the rails, and flip the magnets if it moves toward the breech.
- **Magnet-free conditioning zone:** leave the first ~20 mm at the breech without magnets. Conditioning current in the field would eject the slug: 5 A is 2 mN, about 200 g on a 1 mg slug.

### Augmenting turns (second step)

Flat copper turns carrying the launch current, laid directly over and under the rails, add force per amp and cut the current the driver has to supply.

- 2–4 turns above and the same below, of strip about 4 × 0.5 mm, insulated with polyimide tape.
- Each turn's long sides lie over rail A and rail B, with current in the same direction as the rail beneath. The crossover at the muzzle end passes over the cover, not across the bore exit.
- Wired in series between the driver's inductor pads and rail A. Eight turns are about 2.6 µH and 6 mΩ, and count as part of `L_series`.
- **Coupling falls quickly with distance:** about 0.10 µH/m per turn-pair at 0.5 mm from the bore plane and 0.05 at 1.5 mm. Put the turns closest to the bore and the magnets outside them. The magnet gap then grows and the field drops, so the two compete for the same space.
- Clamp them. A turn is pulled toward the rail beneath it with tens of newtons during the pulse.
- They lengthen the current tail. Check the exit current with the model before building.

### Muzzle voltage taps

Solder or clamp a thin lead to the **muzzle** end of each rail and bring the two back as a twisted pair, routed away from the rails. This pair reads the slug voltage alone, with no rail drop and no inductive term, during conditioning and in flight. A few volts means solid contact; tens of volts means an arc. It is the most useful single diagnostic on the head.

### Velocity ports

Two cross-holes or a short slotted extension beyond the muzzle for a pair of photogates 10–20 mm apart. At 300 m/s a 15 mm spacing is 50 µs.

### Breech plunger

Copper powder conducts far better under pressure: resistance falls as pressure to the power −1.8 ([PC-CREYSSELS09](https://labo.msc.u-paris.fr/~falcon/AIP09.pdf)). A plunger entering along the bore from the breech can meter the charge, compact it and close the breech.

- It must be an **insulator** (a ceramic or glass rod, or a sleeved pin). A metal plunger between the rails would be a second armature.
- 30 MPa on this bore is about 7 N.
- Compaction needs something to press against. Wall friction over a few slug lengths may be enough; a retractable stop pin is the alternative. Open design question.
- A closed breech is also what the carrier-flash regime needs.

### Shorter barrel option

Barrel length does not change how much a slug is heated for a given velocity, but a longer barrel means more wall drag, more fouling and more rail resistance. A 30–50 mm barrel needs more current for less time. Make the rail channels so a short barrel can be tried in the same clamshell. With magnets, extra length does help.

## 2. Shopping / Parts List (Head Only)

| Item | Qty / Notes | Recommended | Alternatives | Approx. Cost | Sources |
|------|-------------|-------------|--------------|--------------|---------|
| Body material | 1–2 blocks | PEI (Ultem) sheet or plate, 10–20 mm thick | PEEK | $40–120 | Professional plastics suppliers, McMaster, online specialty |
| Rail stock | Several lengths | Tellurium copper (C145) rectangular bar 0.5 / 1.0 / 1.5 mm thick | Hard or half-hard C110 copper | $15–40 | Online metals, electrical suppliers |
| Fasteners | Assorted | M3–M5 stainless socket head or shoulder screws | — | $10–20 | McMaster, local hardware |
| Insulating washers / sleeves | As needed | PEEK, nylon, or ceramic | — | $5–15 | McMaster, Digi-Key |
| Adhesive (temporary + permanent) | Small | Non-drying gummy adhesive for initial placement + high-temp epoxy or structural adhesive | — | $10–25 | — |
| Optional exo-skeleton | 1 set | Aluminum plate or bar stock | — | $15–40 | Metals suppliers |
| Sealing (optional early) | — | Thin gasket material or high-temp O-ring cord | — | $5–15 | — |
| Bore liner | A few sheets | Mica sheet 0.2–0.5 mm | Pyrophyllite, Macor, boron nitride; acetal or PTFE for ablative trials | $10–60 | Electrical insulation suppliers, McMaster |
| Magnets | 4–8 | NdFeB bars ~40 × 10 × 5 mm, SH grade, magnetised through 5 mm | SmCo for hot barrels | $15–30 | Magnet suppliers |
| Yoke | 2 | Mild steel strip 3–5 mm | — | $5 | Hardware store |
| Augmenting-turn strip | 1 lot | Copper strip ~4 × 0.5 mm + polyimide tape | — | $10 | Metals suppliers |
| Muzzle tap leads | 1 | Thin high-temperature twisted pair | — | $5 | — |
| Plunger | Several | 0.5 mm ceramic or glass rod | Sleeved pin | $5–20 | Lab suppliers |
| Photogates | 2 | Slotted optical switches | IR LED + phototransistor | $5 | Digi-Key |

**Note:** Start with modest quantities. Rails and body material are the main recurring costs during iteration.

## 3. Build Process (CNC Router)

### 3.1 Preparation
- True and tram the CNC carefully.
- Prepare PEI (or PEEK) stock so both faces are reasonably flat.
- Cut rectangular copper bar to rough length (a bit longer than final barrel).

### 3.2 Machine the Bottom Half
1. Machine the overall rectangular outline and any mounting features.
2. Cut the rail channels (wide, shallow, precise depth).
3. Leave a small amount of material for final clean-up if desired.
4. Drill clamping and mounting holes.

### 3.3 Install the Rails
1. Clean the channels thoroughly.
2. Place the copper bars using a non-drying gummy adhesive or light mechanical hold-down so they sit flat and parallel.
3. Gently clamp or weight them so they cannot move during the next operation.

### 3.4 Finish-Machine the Rail Faces (Critical Step)
1. With the rails secured in the bottom half, run a finishing pass that cleans the inner faces of both rails in the same setup.
2. This step establishes the final gap and parallelism.
3. Use light cuts, sharp tooling, and conservative feeds — copper (especially pure copper) can be gummy.

### 3.5 Top Half
- Machine a completely flat mating surface.
- Add matching clamping holes and any alignment features (pins or shoulders).
- Keep the outer form rectangular.

### 3.6 Assembly
1. Clean both halves.
2. Optionally add a thin gasket or sealing compound.
3. Clamp the two halves together with insulating fasteners.
4. Verify rail gap and continuity.
5. Make the electrical connections at the top of the rails to the driver board interface.

### 3.7 Optional Metal Exo-Skeleton
- Add aluminum side plates or a simple frame around the plastic clamshell for extra rigidity once the basic design is proven.

## 4. Caveats & Practical Advice

- **Alignment is everything.** The in-place finish-machining of the rail faces is the single most important technique for getting usable geometry on a desktop CNC.
- Copper is harder to machine cleanly than aluminum. Tellurium copper is noticeably more pleasant. Use sharp tools and light passes.
- PEI is more forgiving to machine than PEEK on a small router. Start there.
- Soft copper will erode. Treat early barrels as consumable test articles.
- Viscous carrier fluid will try to leak. Plan for sealing even if you ignore it on the first one or two heads.
- Thermal limits of PEI/PEEK will eventually appear. Watch for softening or dimensional change after repeated high-energy shots.
- PEI and PEEK also track under arcing. Do not let them face the bore unlined, and check rail-to-rail resistance before each series.
- Aluminum rails are no longer recommended with copper, tin or zinc powders; see [`RailMaterial.md`](RailMaterial.md).
- Do not rely on firing forces to “seat” or align the rails. Geometry must be correct before the first shot.
- Keep the first barrels relatively short (60–100 mm) to stay well within the comfortable accuracy range of the machine.

## 5. Future Evolution Notes
This clamshell architecture with a flat mating face and rectangular exterior is intentionally simple so that:
- It can be reproduced on common CNC routers
- It can later accept printed or hybrid inserts
- A metal exo-skeleton can be added without redesigning the core
- The same overall form factor can be used while the internal construction moves toward higher printable content

The present focus remains performance and repeatability for splat testing. Printability is a later optimization.

---
*Document version 0.2 – clamshell design of 0.1 with the additions in §1A from the November 2026 review. Nothing in §1A has been built or tested.*
