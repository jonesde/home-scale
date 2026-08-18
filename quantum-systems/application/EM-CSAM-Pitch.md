---
origin: application
device: EM-CSAM opportunity brief (non-nuclear functional print)
updated: 2026-08-18
envelope: concept brief; shop first; nano/fab is fantasy
scope: non-nuclear
---

# EM-CSAM pitch — structure plus function, no furnace

**What this file is.** A hook and a reading of the safer application stack. Concept / opportunity brief. **Not a tested process, not a protocol, not a product datasheet.** Numbers are **classes** from the analysis and the hardware notes, not set points.
**What this file is not.** [EM-LENR](EM-LENR.md), [polar-beam-gate](polar-beam-gate.md), [muon-hydrogen-gate](muon-hydrogen-gate.md), and [coherence-window-recoil](coherence-window-recoil.md) are out of scope. No neutron search. Do not scale pulse energy, inventory, or Δ*T* in search of a nuclear signature.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** Capacitor discharge, flying metal, fine powder, and organic carriers can maim with no “interesting physics.” A hydrogen-rich carrier on high-strength steel or titanium is a [hydrogen-embrittlement](hydrogen-embrittlement.md) **write** — a process defect, not a feature. BeCu only in a shop that already controls beryllium; otherwise stay on copper. This file does not replace a safety review.

Hardware home: [`../../em-csam/`](../../em-csam/README.md). Isolation notes this brief leans on: [EM-CSAM](EM-CSAM.md), [thin-film-optics](thin-film-optics.md), [bonded-magnets](bonded-magnets.md).

**How to send it.** Contacts can stop after §1–3. People who might run a coupon series should read §4 and §6. §5 is a labeled fantasy for a well-funded reader who wants the ceiling, not the first splat.

---

## 1. The offer

A short-barrel electromagnetic deposition head can write **more than one state of ordinary metal** into a part — cold-bonded structure, a conducting and reflecting patch, or a magnetic patch that does **not** have to conduct — without a furnace and without cooking the substrate.

The interesting product is not “another 3D printer.” It is **structure plus function in one scan family**, at a feature scale set by a ~0.5 mm-class bore.

Cold-spray repair already exists industrially. The differentiator here is a small, cheap, replaceable barrel, rails that can be an alloying source on purpose, and using the same pulse as a **magnetic write**, not a claim that Lorentz force was just invented.

Three pictures to hold. They are **design targets**, not demonstrated assemblies.

1. **An insulating magnet next to a copper bus in the same plate.** Electrical percolation and magnetic blocking are different cliffs. A patch can hold remanence at zero continuous watts and still not be a current path. That is already how bonded magnets and ferrites earn their keep (eddy currents). The stretch is printing both patches on purpose, on the same part, with the same head family.
2. **Linear drive tracks printed into a frame, rail, or platen.** Conservative path: print the magnets and the soft-magnetic flux guides; leave the windings as a bought coil or a PCB. Linear first, because the “rotor” can be a long printed track and the forcer can move. Rotary is not forbidden; printed windings are the hard part.
3. **Cold repair, hard-face, and multi-material coat** for a shop, an airframe, or a later depot. Optional second act: a hydride film whose occupancy turns the same screening buffer on and off — metal or window, no hold voltage ([switchable-hydride-mirror](switchable-hydride-mirror.md)).

**Why a contact might care now.** Robots and printer-class machines are drowning in part count, harness, and bought actuators. Aerospace already pays for coatings that do not heat-treat the substrate. A humanoid joint, a gantry rail, or a hatch that is also a magnetic dock and a wear face is a different bill of materials than “print the plastic and bolt on the motor.”

**What we are not selling.** A finished motor. A chip fab. A nano-railgun. A nuclear story.

---

## 2. Handbook cliff vs next-step exploit

The sell dies if it pretends the motor is already in the barrel. The left column is filed. The right column is a design target.

| Already a filed cliff | Next-step exploit (not demonstrated) |
|---|---|
| Connected metal mirrors and conducts; islands do not ([thin-film-optics](thin-film-optics.md)) | Pattern that cliff across a plate as traces and windows |
| NdFeB-class grains block or they do not ([bonded-magnets](bonded-magnets.md)) | Print blocked tracks into a frame; leave other regions unblocked or non-magnetic |
| Bonded magnets and ferrites can be electrically poor; SMCs exist to cut eddy currents | Print *both* an insulating magnet and a percolated Cu path in one process family |
| Cold spray bonds by yield, not melt ([EM-CSAM](EM-CSAM.md)) | Shop-scale repair, hard-face, rail-alloyed coat |
| Occupancy can flip metal ↔ window ([switchable-hydride-mirror](switchable-hydride-mirror.md)) | Smart thermal / optical skin after a sealed low-inventory package exists |
| Pin *T<sub>B</sub>* ≠ parent *T<sub>C</sub>* ([exchange-pin-thermal-history](exchange-pin-thermal-history.md)) | One-shot “did this coupon overheat” bit |
| Polar *P<sub>r</sub>* dies thinner than the depolarization envelope ([depolarization-fuse](depolarization-fuse.md)) | Thinness witness / one-way fuse, no deuterium |
| In-plane *B* kills an integer Hall plateau ([edge-orientation-inhibit](edge-orientation-inhibit.md)) | Lab-only inhibit. Not a manufacturing product |

---

## 3. The state palette

What the head (and the later occupancy or field-cool steps) can leave on a surface. Machine names in parentheses are the QSA filing, not extra physics.

| State you can aim at | What the patch does afterward | Filed home |
|---|---|---|
| **Percolated metal** | Current path. Specular *R*. RF skin. SPR if you add a coupler. Conducting-plate attraction if the gap is in window. | `collective-screening` — [thin-film-optics](thin-film-optics.md), [percolation-dual-switch](percolation-dual-switch.md) |
| **Islanded / starved / plasma-transparent** | Open optically. Electrically discontinuous. Force contrast should die with *R*. | Same starve, four artifacts |
| **Cold-bonded splat** | Dense coat, low substrate heat. Bonding is yield plus oxide rupture, below *T<sub>m</sub>*. | `oscillator-grid` — [EM-CSAM](EM-CSAM.md) |
| **Mushy / splash / vapor** | HAZ, crown, recondensed junk. A different write. Plasma armature is a process lever and a confound. | Same, plus `dielectric-breakdown` |
| **Blocked magnetic grains** | Remanence at 0 W. A magnet, a brake, a dock. | `anisotropy-latch` — [bonded-magnets](bonded-magnets.md) |
| **Unblocked / too-small grains** | Ferrofluid-like. Langevin *M*(*H*), no archive remanence. | Superparamagnetism as the spec, not a failure |
| **Soft-magnetic, electrically poor** | Flux guide with cut eddy paths (SMC class). | Same two cliffs: magnetic order vs electrical percolation |
| **Reversible lattice H** | Capacity. Plateau. Optical shutter that still swings. | `ensemble-average` — [hydride-storage](hydride-storage.md), [switchable-hydride-mirror](switchable-hydride-mirror.md) |
| **Pinned H** | Residual that will not follow the design swing. Fade, stuck shutter, or delayed crack. | Latch / pin. On a load-bearing steel part this is a **defect**. |
| **AFM/FM pin written** | Loop shift *H<sub>ex</sub>* at 0 W. Trip through *T<sub>B</sub>* erases the shift and can leave *M<sub>r</sub>*. | Draft `exchange-pin` |
| **Thick-enough polar volume** | Remanent *P* at *E* = 0, 0 W. | `polar-latch` — [depolarization-fuse](depolarization-fuse.md) is the failure side |
| **Rail metal in the deposit** | Alloy or contamination. Choose the rail. | Process, not a new machine |

**Optionally magnetic and not conducting** is not a new phase. Magnetic particles can sit above the blocking line and still below *electrical* percolation. Ferrites and polymer-bonded NdFeB already live there. The printed claim is spatial: that patch *here*, a percolated Cu patch *there*, cold-bonded structure under both.

### 3.1 How far this scales (floor and ceiling)

This is the reality check. Interesting effects do **not** scale down to a single atom, and “more” is often just more mass. People have already parked single atoms with scanning probes and written with ion beams. That is the expensive nod: if a landing *state* is worth leaving, someone will pay to aim it. It is **not** the goal of this head, and it is not where the filed effects live. A single atom is not a mirror, not a magnet, and not a motor track.

| Effect | Floor (smaller is not more function) | Ceiling / upper bound (more is not more function) |
|---|---|---|
| **Mirror / sheet conductor / SPR** | Starve below ~5–10 nm *continuous* Ag/Al, or island at any nominal thickness. Visible mirror wants ~10–20 nm connected class. A lone atom has no connected screening buffer. | Once the film is percolated and optically thick at that *λ*, extra metal is mass (or a new layer). RF skin *inflates* as *f* → 0 — a foil that mirrors can still be electrically thin at DC. Do not quote optical 10–20 nm as RF skin. |
| **Hard magnet** | NdFeB-class blocking is a tens-of-nm contour at room temperature / lab time; magnetite smaller. Below that: no remanence on the service clock. | *T* → *T<sub>C</sub>* of **that** host (not BaTiO₃, not a hydride line). Huge grains go multi-domain; you still have a magnet until thermal erase or shock. Service life sets the *kT* multiplier (seconds vs years). |
| **Insulating magnet / SMC** | Same magnetic floor, plus stay *below* electrical percolation. | If the splat field percolates electrically, you printed a conducting magnet and bought eddy currents. That can be what you wanted. It is a different part. |
| **Polar remanence** | Dead-layer / depolarization envelope. No portable ferroelectric *KV* number. Thinner is not a smaller bit; it is an empty well. | *T* → *T<sub>C</sub>* of **that** ceramic (BaTiO₃ ≈ 393 K class). Do not import 30 nm NdFeB. |
| **Exchange-pin history bit** | Superparamagnetic FM grain cannot hold *H<sub>ex</sub>*. | Trip band is *T<sub>B</sub>* < *T* < *T<sub>C</sub>*(FM). *T<sub>B</sub>* is the pin’s number. A bake through FM *T<sub>C</sub>* erases both layers and is a worse crayon. |
| **Hydride shutter** | Metal phase still needs the percolation cliff. Island hydride is a starved buffer, not a shutter. | Cycle life and the pin (stuck open or shut). Overshoot toward host *T<sub>m</sub>* is `coupled-grid-loss`, not a cleverer switch. Packaging of the H inventory is the product ceiling. |
| **Casimir / conducting-plate force** | Starve the faces and the conducting-plate class should die with *R*. | Gap *d* is capacity of the force (0.1–1 μm class). Opening the gap into the noise is not percolation. Patch charge is the practical ceiling. |
| **CSAM write pixel (this head)** | Particles must pass the bore. Nano-only feedstock is skin + melt + H pickup. | ~0.5 mm-class bore is the present pixel. Larger bore buys rate and loses the map. Velocity class 200–800 m/s; Cu can stay solid farther than steel (steel liquifies on the way to 500 m/s class because resistivity dumps heat into a small *C*). |
| **Pulse as a materials knob** | Too short: gas/carrier never does what you wanted; current in a tens-of-μm Cu skin (~1 μs class). | Too long: a bake. ~100 μs class wets ~0.2–0.3 mm of Cu. More ∫*I*²*dt* is not a finer state. |
| **Printed logic / photonics (fantasy, §5)** | Tunnel islands and dopants are a different machine (`energy-gate` / Coulomb), not a tinier mirror. Latch bits cannot be smaller than *KV* / depolarization. | Complementary to a CMOS front-end, not a replacement. The paid ceiling today is backend, interposer, and electrical–optical packaging. |

**Process upper bounds of the pitch itself.** Joule-class shots, not a foundry. Bonded-magnet energy product below sintered. mm-class pixels, not lithography. Printed windings are not a sheet. Occupancy shutter waits on a sealed package. None of that kills the shop-scale offer in §1.

---

## 4. Speculative exploits (shop to lab)

Each box is a design target. **Stands on** is filed. **Stretch** is the part that is not demonstrated. **First trial** is a coupon, not a product. **Dies if** is how the exploit fails without rewriting the library.

### Manufacturing and aerospace

#### A. Cold structural coat and hard-face

**Function.** Repair or wear layer on a part that must not take a heat-treat cycle. Rails can be the same metal (clean) or a chosen alloy source (hard-face).

- **Stands on.** Yield-bond window vs melt ([EM-CSAM](EM-CSAM.md) §2). Rail erosion as a second feedstock.
- **Stretch.** “Exotic alloys on the fly” as *chemistry control* (powder + consumed rail + carrier atmosphere). Not a new phase of matter.
- **First trial.** Cu/oil → metal: velocity / *I* series. Then a dissimilar-rail shot and ask what landed, not whether it looks pretty.
- **Dies if.** The only dense coats are splash-melt, or rail metal is an uncontrolled contaminant you cannot turn off.

#### B. Depot and later in-space repair

**Function.** Same coat, farther from a furnace. Low substrate HAZ is the point of CSAM.

- **Stands on.** A.
- **Stretch.** Vacuum, feedstock handling, and a vehicle or depot envelope. Industrial-until-mitigated. Not ISRU folklore.
- **First trial.** Do A in a shop until the bond window is boring. Packaging is a later file.
- **Dies if.** The process only works with a wet slurry atmosphere you cannot take off the ground.

#### C. Multi-material pixel

**Function.** Cu bus, steel wear face, Al–Si, optional graphene–Cu *if* the flake survives the flash, on one toolhead.

- **Stands on.** Metered shots, rail choice, carrier chemistry ([PowderCarrierRailMaterial](../../em-csam/PowderCarrierRailMaterial.md)).
- **Stretch.** Registration between shots. Cross-contamination. Graphene survival.
- **First trial.** Two-chemistry coupon with a visible seam. Measure continuity on the Cu side and hardness on the steel side.
- **Dies if.** Every shot is the same grey alloy no matter what you loaded.

### Robotics and motion

#### D. Insulating magnet track in a plate

**Function.** A printed strip that holds remanence at 0 W and does **not** percolate electrically. Eddy-poor on purpose.

- **Stands on.** [bonded-magnets](bonded-magnets.md) *KV* cliff; electrical percolation as a *separate* starve ([thin-film-optics](thin-film-optics.md)).
- **Stretch.** Impact does not smash the grains through the blocking line or sinter them into a conducting network.
- **First trial.** Ferrite or bonded-NdFeB-class powder, sparse splat or insulating residue, *B* on during flight or on the substrate. Read remanence (VSM / powder pattern) **and** sheet resistance. You want *M<sub>r</sub>* without a Cu-like sheet.
- **Dies if.** Every magnetic deposit is either non-magnetic or a conducting sheet.

#### E. Conservative linear drive (the honest “print the motor into the frame”)

**Function.** Magnet track and/or soft-magnetic back-iron printed into a rail, platen, or robot link. **Coils stay conventional or PCB.** The frame *is* the reaction part.

- **Stands on.** D plus SMC-class flux guides (G). Linear geometry does not need end-turns on the printed side.
- **Stretch.** Alignment, pitch, and force density good enough to replace a bought linear motor on a printer-class axis — not on a servo catalog yet.
- **First trial.** A straight printed magnet track, a moving voice-coil or PCB forcer you already own, a force-vs-gap curve. Compare to the same forcer over a glued commercial magnet strip.
- **Dies if.** Printed remanence does not survive the splat, or the track shorts the forcer’s field into a conducting slab (then you needed D and failed it).

Linear is the lead because the long direction is a scan. A gantry already knows how to walk a head down a rail.

#### F. Stretch: printed windings and rotary

**Function.** Isolated conductor loops (linear or rotary) and/or a printed Halbach / sector-aligned rotor ring.

- **Stands on.** Percolated Cu as a sheet conductor. Alignment *B* in flight for sector magnets.
- **Stretch. Hard.** Splat wants a connected sheet, not a long insulated wire with end-turns and layer isolation. Rotary needs a return path the head does not own yet.
- **First trial.** Do not start here. After E exists: one printed hairpin or a sector magnet ring with *B* flipped between passes; windings still bought.
- **Dies if.** “Printed coil” is always a shorted pancake. That is a percolation success and a winding failure.

#### G. Soft-magnetic composite flux guides

**Function.** Iron-class powder below electrical percolation as printed teeth or back-iron. Twin of D, low *K*, high μ.

- **Stands on.** Same two-cliff split as D.
- **Stretch.** μ useful after impact, without sintering into a conducting block.
- **First trial.** Permeability of a printed yoke vs the same powder in a known SMC process. Sheet *R* high.
- **Dies if.** The yoke is either dead (no flux) or a solid eddy plate.

#### H. Zero-watt dock, gripper, or brake

**Function.** Write remanence, hold a tool or an axis with no current; erase with reverse *H*, heat through that host’s *T<sub>C</sub>*, or shock.

- **Stands on.** Latch hold-power = 0 W ([bonded-magnets](bonded-magnets.md)).
- **Stretch.** Cycle life on a robot (shock erase is also the mechanical failure path).
- **First trial.** A printed pad that picks up a keeper coupon after the write field is off, and drops it after a reverse-field or a controlled bake.
- **Dies if.** Hold requires the write coil to stay on. That is an electromagnet, and you did not need this process.

Humanoid-adjacent reading of D–H, still speculative: linear joints whose stator is the link; tool changers that hold at 0 W; wear faces hard-faced in the same campaign (A); harness replaced by a printed bus (C + percolated Cu). Printers and CNCs are the nearer robot.

### Functional surfaces

#### I. Printed metal / window map

**Function.** Shot count through percolation as an optical or EMI pattern. Some patches mirror and conduct; some transmit.

- **Stands on.** Thickness series cliff ([thin-film-optics](thin-film-optics.md)).
- **Stretch.** A *map*, not a coupon. Feature scale is the bore, not a litho grid.
- **First trial.** Glass slide, stepped shot count, *R*(λ) / *T*(λ). Cliff, not a linear fade. Then two regions on one slide.
- **Dies if.** *R* grows linearly through the 5–20 nm class with no percolation cliff.

#### J. Occupancy shutter skin

**Function.** A hydride film that is metal or dielectric with a *P*–*T* or electrochemical H swing. Optical / IR / thermal-control reading. Hold-power of the optical state is 0 extra W once occupancy is set.

- **Stands on.** [switchable-hydride-mirror](switchable-hydride-mirror.md). Metal-phase percolation still applies.
- **Stretch.** Sealed low-inventory package. Cycle life (the pin sticks the shutter — same two H populations as [hydride-storage](hydride-storage.md)).
- **First trial.** Not on the railgun. A purchased or evaporated Y/Mg-class film, one swing, *R*/*T* flip with no hold voltage. CSAM enters only as a way to *make* a metal-phase film; percolation is still the cliff.
- **Dies if.** The “shutter” needs a bias to stay reflective (electrochromic, different machine), or residual after the design swing never bakes out.

#### K. Dual-starve clutch

**Function.** One starve kills specular *R* and conducting-plate attraction together ([percolation-dual-switch](percolation-dual-switch.md)). Later: a packaged MEMS clutch.

- **Stands on.** `coupled-screening-failure`.
- **Stretch.** Gap control, patch charge, and calling the force Casimir when electrostatics dominate.
- **First trial.** Optics series first (I). Same thickness series as a plate at fixed *d*. Force class should vanish with *R*.
- **Dies if.** An island film still shows the conducting-plate 1/*d*⁴ class at the same *d*.

### Witnesses (QA, not the lead sell)

#### L. Thermal-history coupon

**Function.** AFM/FM stack. After *T<sub>B</sub>* < *T* < *T<sub>C</sub>*(FM), *H<sub>ex</sub>* is gone and FM remanence can remain. “Did this lot, this flight, this motor winding exceed the pin?”

- **Stands on.** [exchange-pin-thermal-history](exchange-pin-thermal-history.md).
- **Stretch.** A sealed coupon a shop will actually read. Not a Curie crayon.
- **First trial.** Thin-film lab: field-cool, trip, unshifted control. CSAM is optional and probably the wrong writer for the AFM.
- **Dies if.** *H<sub>ex</sub>* dies at FM *T<sub>C</sub>* rather than at a lower *T<sub>B</sub>*.

#### M. Depolarization fuse

**Function.** Ferroelectric film whose usable *P<sub>r</sub>* dies when thinner than the depolarization envelope, still below *T<sub>C</sub>*. Electrical twin of *KV* collapse. **No deuterium.**

- **Stands on.** [depolarization-fuse](depolarization-fuse.md).
- **Stretch.** Using thinness as a one-way process witness, not as FeRAM.
- **First trial.** Ceramics / thin-film shop. Thickness series at fixed *T* < *T<sub>C</sub>*.
- **Dies if.** Neutrons appear (wrong file) or a 30 nm NdFeB number is imported as the polar floor.

#### N. Orientation inhibit

**Function.** Rotate *B* in-plane on a 2DEG Hall bar; the integer plateau is a non-occurrence.

- **Stands on.** [edge-orientation-inhibit](edge-orientation-inhibit.md).
- **Stretch.** None for manufacturing. Lab only. Higher-*T* graphene packaging does not exist here.
- **First trial.** Only if the fridge and the magnet already exist.
- **Dies if.** This paragraph is used to sell a product.

---

## 5. If the write pixel goes to nano (fantasy, not a roadmap)

Skip this section if you came for hard-facing.

The ~0.5 mm barrel is a **metering and launch** story. If the valuable object is the **state palette** in §3, then shrinking the pixel is an industry problem, not a new machine. People already move atoms with FIB, MBE, ALD, STM lithography, ion implant, and e-beam. The expensive nod — “single atom out of a barrel” — is hyperbole for that fact: if the landing state is worth the cost, an industry appears. It is **not** Lorentz slurry at 1 Å, and it is **not** the goal.

What you would buy, if money were free, is a **directed writer that can choose which state to leave**, aimed first at µm, then nm, then a true atom/ion optic. The floors in §3.1 still apply. Printing smaller than a latch’s volume envelope does not give a smaller bit. A single atom is not a connected screening buffer: mirrors, SPR, and sheet current still need a percolated patch. Atom-scale writing gets you dopants, islands, and tunnel gaps — a different machine (`energy-gate` / Coulomb), not a tinier Ag mirror.

EUV and a CMOS front-end are not the competitor. The live need is **backend, interposer, photonics packaging, and mixed electrical–optical I/O**. That is where an additive, multi-state writer would get paid.

### O. Pixel-size ladder as a program

mm splat → µm jet or FIB-cousin → nm directed beam → atom/ion optic. Same palette, finer aim.

- **Stands on.** §3.1. Existing directed-write tools already exist; they do not speak this palette as one head.
- **Stretch.** One tool family that can pick metal / window / blocked / unblocked / occupancy / pin / polar well.
- **If money were free.** Three writers, one metrology stack (*R*/*T*, VSM, TDS, *P<sub>r</sub>*), same coupons stepped down in pitch.
- **Dies if.** Finer pixels only reproduce lithography’s existing materials, with no state choice beyond “metal is here.”

### P. Additive backend / interposer

Percolated Cu as interconnect. Starved patches as high-*R* or windows. Insulating-magnet islands as inductor cores next to RF traces.

- **Stands on.** I, D, G. Optical 10–20 nm is not the RF skin — use the skin clock.
- **Stretch.** Registration, via-like continuity in *z*, contamination from the writer.
- **If money were free.** An interposer coupon: a transmission line, a starved gap, a printed core, S-parameters vs a lithographed twin.
- **Dies if.** The only continuous Cu is a shorted plane, or the “core” percolates and kills Q.

### Q. Mixed electrical and optical fabric (the ceiling hook)

A percolated metal line is an electrical path **and** a light-handling strip (mirror, plasmon / SPR if coupled). A dielectric, islanded, or occupancy-starved neighbor is a window or a modulator. Hydride occupancy is a 0 W optical switch on a written pixel.

This is the large present need: getting on and off a chip optically without a second factory language.

- **Stands on.** [thin-film-optics](thin-film-optics.md), [switchable-hydride-mirror](switchable-hydride-mirror.md), I, J.
- **Stretch.** Mode matching, loss, and a pixel small enough that “next to” means a coupler, not a billboard. mm-class splat cannot do this. A nm writer might still fail on roughness and islanding.
- **If money were free.** Crude first, even at a generous pitch: one substrate, one metal line that carries current **and** supports a measurable optical mode or SPR dip, next to a window that transmits in the same band. Then an occupancy swing on one pixel only.
- **Dies if.** Electrical continuity and the optical mode never coexist on the same written metal, or the “optical path” is just a hole in a foil with no controllable interface.

### R. Crude printed logic (not a CPU)

Majority / relay class, labeled **crude**.

1. Percolation as a one-way “this wire exists” fuse.
2. Magnetic bits, domain-wall segments, or exchange-pin cells as 0 W state — no smaller than *KV*.
3. Polar *P<sub>r</sub>* bits — no smaller than the depolarization envelope.
4. Occupancy as a chemical / optical bit.
5. A metallic island with tunnel gaps as a SET-class `energy-gate`, **if** the writer can leave a gap on purpose.

- **Stands on.** The floors in §3.1. Contrast: [depolarization-fuse](depolarization-fuse.md), [exchange-pin-thermal-history](exchange-pin-thermal-history.md). Coulomb / SET is not *R<sub>K</sub>* and not a mirror.
- **Stretch.** Isolation and registration. Not “atoms think.”
- **If money were free.** A three-bit magnetic or polar coupon that holds overnight at 0 W, plus one percolation fuse you can blow. SET only after a gap is a controlled knob.
- **Dies if.** The only “logic” is a shorted sheet, or bits vanish on lab time because they were written below the latch floor.

### S. Mechatronic pixel

Motor track + interconnect + optical line + thermal-history coupon on one piece. Structure, drive, sense, and I/O from one writer family.

- **Stands on.** E, C, Q, L.
- **Stretch.** All of those stretches at once. This is the robotics ceiling: a humanoid link or a printer axis that is also the bus.
- **If money were free.** After E and a crude Q exist, put them on one coupon. Do not start here.
- **Dies if.** Each function only works on its own dedicated substrate.

### T. On-wafer nanopositioner (dogfood)

Printed magnet tracks plus conventional (then printed) coils as the stage that aims the next finer pixel. Linear still easier than rotary.

- **Stands on.** E, F, O.
- **Stretch.** Encoder-class pitch and a writer mounted on its own output.
- **If money were free.** A mm-scale printed track that moves an optics stage before anyone talks about wafers.
- **Dies if.** E never beats a glued magnet strip.

### U. Directed-atom chemistry

The hardware note’s rail-as-alloy, taken to the absurd: the “rail” or ion source is a dopant valve. Place a species, not a slurry. Name the landing state (metal, oxide, vacancy, occupancy) or you only made a mess.

- **Stands on.** Intentional rail consumption. Existing implant / MBE practice.
- **Stretch.** Calling that the same head. It is the same *palette*, not the same barrel.
- **If money were free.** Buy time on a directed-write tool and try to leave two states from §3 on one coupon. Do not build a nano-railgun to learn this.
- **Dies if.** The landing species cannot be read as one of the filed states.

---

## 6. Technical annex (first series, not a factory)

Full isolation sequences live in the application files. This brief does not duplicate them. Do not skip to a nuclear search. There is no Phase H here.

### 6.1 Cliff classes (do not equate)

| Cliff | Class | Do not quote as |
|---|---|---|
| Ag/Al visible connected buffer | ~10–20 nm continuous; starve ≲ 5–10 nm continuous or islands | RF skin, London *λ* |
| NdFeB blocking, RT / lab time | tens of nm (~30 nm class) | Ferroelectric thickness, hydride *T* |
| Magnetite blocking | smaller than NdFeB | “all magnets, 30 nm” |
| BaTiO₃ *T<sub>C</sub>* | ≈ 393 K class | NdFeB Curie, *T<sub>B</sub>* |
| Ni *T<sub>C</sub>* | 627 °C class | A hydride phase line |
| Cu skin | ~tens of μm at ~1 μs; ~0.2–0.3 mm at ~100 μs | Optical 10–20 nm |
| Bonding velocity | 200–800 m/s class, material-specific | A fusion knob |
| Casimir gap window | 0.1–1 μm class | The optical percolation thickness |
| Steel bake-out (erase of charged H) | 150–200 °C class — check the spec | A nuclear clock |

*T<sub>C</sub>*, *T<sub>B</sub>*, *T<sub>λ</sub>*, melt, and a blocking line are the same **kind** of thermal story only in the sloppiest reading. See [requirement-audit](../library/derived/requirement-audit.md).

### 6.2 First series a shop can run

Reuse [EM-CSAM](EM-CSAM.md) campaigns A–G. No D₂, no neutron channel, no BeCu unless that shop already exists.

| Order | Coupon | Question |
|---|---|---|
| 0 | Driver into shorted rails | Skin / EMI / heat baseline |
| 1 | Cu / oil → glass, shot-count series | Percolation cliff in *R*/*T* (I) |
| 2 | Cu / oil → metal, *I* / velocity series | Yield-bond vs melt (A) |
| 3 | Ni or ferrite, coil or in-flight *B*, inert | Remanence vs heat (D, start) |
| 4 | Magnetic powder, sparse / insulating residue | *M<sub>r</sub>* **and** high sheet *R* (D proper) |
| 5 | Printed track + bought forcer | Force vs a glued magnet strip (E) |
| 6 | Steel + dry vs H-rich carrier, bake column | Embrittlement as a **warning**, not a product |
| 7 | Optional: two-chemistry seam | Multi-material pixel (C) |

Hydride shutter (J), dual-starve force (K), exchange-pin (L), and polar fuse (M) are **other benches**. Do not bolt them onto the first barrel.

### 6.3 Falsifiers of this pitch

These are not library falsifiers. They are how the *sell* dies.

- Cu-on-glass *R* grows linearly through the 5–20 nm class with no percolation cliff.
- Ni / ferrite remanence is indistinguishable from heating; Pd and Ni look the same on remanence in the same coil.
- Every magnetic splat either has no *M<sub>r</sub>* or conducts like a metal sheet — the two cliffs cannot be separated.
- Printed tracks never hold *KV* after impact (shock-erase is the only outcome).
- “Cold” and “plasma” shots are calorimetrically identical after *I*²*R* (then plasma is not optional).
- A hydride “shutter” that needs hold voltage, or that never leaves the isotherm.

If (1) fails, do not take the later optical or motor-bus stories seriously. If the *KV* series in [bonded-magnets](bonded-magnets.md) fails, stop using the latch language on powder.

---

## 7. What this is asking

**A manufacturing or aerospace contact.** A conversation, a coupon, or a day on a spray / magnet / optics bench. Not a factory commitment. The nearest paid shapes are A (coat / repair / hard-face), D–E (insulating magnet and a linear track in a plate), and C (two metals, one head).

**A maker or lab.** One row of §6.2, results read against the cliffs, not against a hoped-for gadget.

**A well-funded workshop that likes the ceiling.** §5 after §6.2 is boring. Start with Q’s crude coupon (current and an optical mode on the same written metal) and E’s track-vs-glued-strip. Do not start by building a nano-railgun.

**Not asking.** Nuclear search. Scaling the bank. Casual BeCu. H₂ plus powder as a demo. Adding a pyroelectric crystal or a muon “to help.”

---

## Links

| File | Role in this brief |
|---|---|
| [EM-CSAM](EM-CSAM.md) | Head as writer; campaigns |
| [thin-film-optics](thin-film-optics.md) | Percolation / mirror / SPR calibration |
| [bonded-magnets](bonded-magnets.md) | *KV* calibration |
| [hydrogen-embrittlement](hydrogen-embrittlement.md) | Process warning |
| [hydride-storage](hydride-storage.md) | Two H populations |
| [switchable-hydride-mirror](switchable-hydride-mirror.md) | Occupancy shutter |
| [percolation-dual-switch](percolation-dual-switch.md) | Force channel of the same starve |
| [exchange-pin-thermal-history](exchange-pin-thermal-history.md) | *T<sub>B</sub>* witness |
| [depolarization-fuse](depolarization-fuse.md) | Polar floor, no D |
| [edge-orientation-inhibit](edge-orientation-inhibit.md) | Lab inhibit only |
| [`../../em-csam/`](../../em-csam/README.md) | Hardware notes |

Out of scope on purpose: [EM-LENR](EM-LENR.md), [polar-beam-gate](polar-beam-gate.md), [muon-hydrogen-gate](muon-hydrogen-gate.md), [coherence-window-recoil](coherence-window-recoil.md).
