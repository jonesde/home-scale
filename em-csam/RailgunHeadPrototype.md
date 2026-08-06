# EM-CSAM Railgun Print Head – Design Concept & Build Guide v0.1

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
- Primary recommendation: Tellurium copper (C145) or hard / half-hard C110.
- Experimental thicknesses: 0.5 mm, 1.0 mm, and 1.5 mm.
- Target bore height experiments: ~0.5 mm to 1.5 mm (0.5×0.5 mm and 0.5×1 mm are of particular interest for lower drive current).

### Body Materials
| Priority | Material     | Notes                                      |
|----------|--------------|--------------------------------------------|
| Primary  | PEI (Ultem)  | Best balance of machinability, insulation, cost, and temperature |
| Alternative | PEEK      | Higher continuous temperature capability   |
| Early testing | UHMW / HDPE | Acceptable only for very early mechanical trials |

### Key Design Features
- Flat mating surfaces on both halves for sealing and alignment
- Sufficient wall thickness around the barrel for firing rigidity
- Mounting holes placed so they do not interfere with the bore or clamping zone
- Optional metal exo-skeleton for increased stiffness
- Electrical connection at the top of the rails to the driver board (bolted interface)
- Designed so the internal geometry can later be adapted to printed or hybrid construction

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
*Document version 0.1 – initial consolidated design concept and build guide for the removable railgun print head.*
