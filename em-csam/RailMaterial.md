# Rail Material – Trade-offs & Best Practices
EM-CSAM Micro-Railgun Print Head

**Revised November 2026.** The earlier version of this note recommended aluminum for the first barrels. That recommendation is withdrawn: **start with tellurium copper (C145)**. The reasons are in §2. Background and sources: [`DesignReview-2026-11.md`](DesignReview-2026-11.md) (C1, C2, B1) and [`References.md`](References.md) §8.

## 1. Summary Comparison

| Factor | Aluminum | Copper (C145) | Better for early prototypes |
|---|---|---|---|
| Electrical conductivity | ~61 % of copper | 93 % IACS | Copper |
| Rail heating | Higher | Lower | Copper |
| Machinability (desktop CNC) | Easy | Good for C145 (pure copper is gummy) | Even |
| Cost & availability | Lower | Higher | Aluminum |
| Oxide / contact | Insulating oxide re-forms in milliseconds | Much better | Copper |
| **Reaction with copper powder** | **Forms liquid at 548 °C (Cu–Al eutectic)** | None; same metal | Copper |
| Melting point | 660 °C | 1085 °C | Copper |
| Shot-to-shot consistency | More variable | Better | Copper |
| Hydrogen from the carrier | Porosity if it melts | C145 and oxygen-free grades tolerate it; C110 does not | Copper (right grade) |

**Overall recommendation**
Use **C145 tellurium copper** from the first barrel. Use aluminum rails only when the powder is aluminum-based.

## 2. Why Not Aluminum First

The earlier case for aluminum was machinability, cost, and the idea that extra rail heating would make thermal effects easier to study. Three things outweigh it.

- **Copper powder on aluminum rails makes liquid metal at 548 °C.** Copper and aluminum form a eutectic far below either melting point. A hot copper slug in contact with an aluminum rail dissolves the rail surface on every shot and leaves brittle copper–aluminum intermetallics in the deposit and on the rail. The starter powders are tin, zinc and copper; none of them wants aluminum rails.
- **The oxide.** Aluminum's oxide is an insulator and re-forms within milliseconds of cleaning. The slug already has a conduction problem ([`EM-CSAM-ConceptTechnical.md`](EM-CSAM-ConceptTechnical.md) §3.5); the rails should not add one.
- **Machinability is not a real difference** once the copper is C145. It machines well on a small router.

## 3. Copper Rails

### Which copper

| Grade | Conductivity | Use it? | Why |
|---|---|---|---|
| **C145 (tellurium copper)** | 93 % IACS | **Yes, first choice** | Machines cleanly. Phosphorus-deoxidized ([MT-C145](https://www.concast.com/files/C14500.pdf)). |
| C101 / C102 (oxygen-free) | 101 % IACS | Yes | No oxide to react with hydrogen. Gummy to machine. |
| **C110 (ETP)** | 100 % IACS | **Avoid with oil carriers** | Contains 0.02–0.04 % oxygen as Cu₂O. Hydrogen diffuses in, forms steam at the oxide and opens grain-boundary voids, with the risk quoted above about 370 °C ([MT-CUH](https://www.mdpi.com/2075-4701/14/5/588)). An oil carrier decomposes to hydrogen and acetylene. |

That deoxidized grades are immune was not confirmed directly in a source; the mechanism needs the oxide, which they lack.

### Best practices
- Rectangular bar, finish-machined in place (see §6).
- Clean the working faces before a test series.
- Treat rails as consumables and log shots per rail.

## 4. Harder-Wearing Options

For when copper rails erode too fast. Conductivity and softening figures are from supplier data; no head-to-head erosion data for this use was found.

| Material | Conductivity | What it offers | Catch |
|---|---|---|---|
| CuCrZr (C18150) | 75–85 % IACS | Standard resistance-welding electrode alloy. Holds hardness to about 500 °C, where pure copper softens near 200 °C ([MT-C18150](https://alcavil.pages.dev/en/materials/class-2-c18150)). | Less pleasant to machine than C145. |
| GlidCop AL-15 / AL-25 | 92 / 87 % IACS | Dispersion-strengthened copper; little softening after high heat ([MT-GLIDCOP](https://en.wikipedia.org/wiki/Glidcop)). | Cost, availability in small bar. |
| Copper–tungsten (75W–25Cu) | 40–46 % IACS | EDM and welding electrode stock; resists arc erosion ([MT-WCU](https://eposintering.com/wp-content/uploads/2014/09/Material-Datasheet-W-Cu-20250312.pdf)). Sold as small ground bars. | Hard to machine; grind instead. More rail resistance. |
| Tungsten (TIG electrode rod) | ~31 % IACS | Cheap, straight, precise ground rod in 1.6 and 2.4 mm. Does not alloy with copper. | Round, so the bore shape changes. **Use lanthanated or ceriated rod, not thoriated**, which is radioactive when ground. Untested idea. |
| Graphite (EDM grade) | ~0.15 % IACS | Does not melt; machines easily. | High resistance, so use only as a thin face insert. Adds carbon to the deposit. |

A cold-sprayed CuCrZr–W coating on railgun rails has been reported to erode less than dispersion-strengthened copper ([MT-RAILCOAT](https://doaj.org/article/7666ef35a8fe4eefba41fe0c597a9b15)). That suggests faced rails as a later step.

## 5. Aluminum Rails – When They Fit

Aluminum rails are the same-metal choice for aluminum and aluminum–silicon powders.

- **Alloy:** 6101 (bus-bar grade, 52–59 % IACS). 1100 or 1350 for maximum conductivity. Not 6061-T6.
- **Oxide:** abrade and solvent-clean before a series; expect to need an oxide-clearing step in preconditioning.
- **Never with copper powder, copper rails opposite, or any gallium-bearing carrier.** Gallium penetrates aluminum grain boundaries quickly, even with no applied stress ([CH-GALLIUM](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11901249/)).
- Expect more debris and more frequent cleaning than copper.

## 6. Geometry and Shared Practice

- **Rail width: 3–4 mm.** A 0.5 ms pulse penetrates about 2 mm of copper. Width beyond 3–4 mm carries no extra pulse current and lowers the inductance gradient ([`EM-CSAM-ConceptTechnical.md`](EM-CSAM-ConceptTechnical.md) §3.2). The 8–12 mm widths in earlier notes are worth keeping only where needed for clamping or cooling.
- **Rail thickness:** 0.5–1.5 mm, which is the bore height.
- **Installation:** place the bars in the machined channel, secure them, then finish-machine the two inner faces in one setup.
- **Clamshell:** one half carries the channels; the other is a flat mating face. Open it to clean.
- **Electrical interface:** bolted at the breech. A twisted pair from the muzzle ends brings back the slug voltage ([`RailgunHeadPrototype.md`](RailgunHeadPrototype.md)).
- **Consumable mindset:** early barrels are test pieces.

## 7. Development Sequence

1. **Phase 1:** C145 rails, 3–4 mm wide, in a lined clamshell. Tin or solder paste, then zinc, then copper.
2. **Phase 2:** once deposits are coherent, compare rail widths and measure erosion per shot.
3. **Phase 3:** if erosion limits barrel life, try CuCrZr, then copper–tungsten or faced rails.
4. **Aluminum rails** only when the work moves to aluminum powders.
