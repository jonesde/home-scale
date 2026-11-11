---
origin: application
device: EM-CSAM opportunity brief (non-nuclear functional print)
updated: 2026-11-11
envelope: concept brief; shop first; nano/fab is fantasy
scope: non-nuclear
---

# EM-CSAM pitch — structure plus function, no furnace

**What this file is.** A hook and a reading of the safer application stack. Concept / opportunity brief. **Not a tested process, not a protocol, not a product datasheet.** Nothing in it has been built or measured on this head.
**What this file is not.** [EM-LENR](EM-LENR.md), [polar-beam-gate](polar-beam-gate.md), [muon-hydrogen-gate](muon-hydrogen-gate.md), and [coherence-window-recoil](coherence-window-recoil.md) are out of scope. No neutron search. Do not scale pulse energy, inventory, or Δ*T* in search of a nuclear signature.

> **Hazards (read [SAFETY.md](../SAFETY.md)).** Capacitor discharge, flying metal, fine powder, and organic carriers can maim with no “interesting physics.” A hydrogen-rich carrier on high-strength steel or titanium is a [hydrogen-embrittlement](hydrogen-embrittlement.md) **write**, a process defect. BeCu only in a shop that already controls beryllium; otherwise stay on copper. This file does not replace a safety review.

> **Revised 2026-11-11.** The first version sold several ideas on cliffs that the sourced library now records as smooth dependences or as wrong numbers. This revision keeps every idea and restates what each stands on. What changed: (1) reflectance has no thickness cliff and no “connected buffer”; the sharp change in a deposited film is dc percolation ([reflection](../library/reflection.md)). (2) Reflectance, the surface-plasmon dip and the Casimir force do not collapse together; thin or transparent faces reduce the force by up to about half, and a switchable mirror showed no change ([casimir-force](../library/casimir-force.md)). (3) The thermal-stability size of Nd₂Fe₁₄B is about 3.5 nm, a retention-time convention, and it is not what limits a magnet; coercivity and shock are ([superparamagnetism](../library/superparamagnetism.md), [permanent-magnet-latch](../library/permanent-magnet-latch.md)). (4) Ferroelectrics have no “superparaelectric volume”; thin films lose net remanence through poor screening while the polar phase survives to 1.2 nm ([ferroelectric-remanence](../library/ferroelectric-remanence.md)). (5) A blocking temperature is a rate-dependent crossover ([exchange-bias](../library/exchange-bias.md)). (6) The skin layer has no edge ([skin-effect](../library/skin-effect.md)). Ideas I, K, L and M changed basis; D, G, H and R changed wording; J is now stated as an existing published device, and L and M as uses of measured effects. Numbers are of three kinds: **library** (sourced, linked), **hardware note** (planning values and model results from [`../../em-csam/`](../../em-csam/README.md) and its `tools/shot_model.py`), and **unsourced**, which is said where it occurs.

Hardware home: [`../../em-csam/`](../../em-csam/README.md). Isolation notes this brief leans on: [EM-CSAM](EM-CSAM.md), [thin-film-optics](thin-film-optics.md), [bonded-magnets](bonded-magnets.md).

**How to send it.** Contacts can stop after §1–3. People who might run a coupon series should read §4 and §6. §5 is a labeled fantasy for a well-funded reader who wants the ceiling.

---

## 1. The offer

A short-barrel electromagnetic deposition head could write **more than one state of ordinary metal** into a part (cold-bonded structure, a conducting patch, a magnetic patch that does not have to conduct) without a furnace and without cooking the substrate.

The product is **structure plus function in one scan family**, at a feature scale set by a ~0.5 mm-class bore.

Cold-spray repair already exists industrially. The differences here are a small, cheap, replaceable barrel, rails that can be an alloying source on purpose, and a magnetic field present during the shot.

Three pictures to hold. They are **design targets**, none demonstrated.

1. **An insulating magnet next to a copper bus in the same plate.** Whether a deposit conducts and whether it holds remanence are independent properties. A patch can be a magnet at zero continuous watts and still not be a current path. Bonded magnets and ferrites already work that way. The stretch is printing both patches on purpose, on the same part, with the same head family.
2. **Linear drive tracks printed into a frame, rail, or platen.** Conservative path: print the magnets and the soft-magnetic flux guides; leave the windings as a bought coil or a PCB. Linear first, because the track is a scan and the forcer can move.
3. **Cold repair, hard-face, and multi-material coat** for a shop, an airframe, or a later depot. Optional second act: a hydride film that is a mirror or a window depending on its hydrogen content ([switchable-hydride-mirror](switchable-hydride-mirror.md), an existing laboratory device).

**Why a contact might care now.** Robots and printer-class machines carry a large part count, harness, and bought actuators. Aerospace already pays for coatings that do not heat-treat the substrate. A gantry rail or a hatch that is also a magnetic dock and a wear face is a different bill of materials from “print the plastic and bolt on the motor.”

**What we are not selling.** A finished motor. A chip fab. A nano-railgun. A nuclear story.

---

## 2. What is sourced, and the next-step exploit

The left column is in the library. The right column is a design target.

| Sourced | Next-step exploit (not demonstrated) |
|---|---|
| A deposited film conducts dc only above its percolation thickness; its reflectance rises smoothly with thickness ([thin-film-optics](thin-film-optics.md)) | Pattern conducting and non-conducting patches across a plate; optical density as a graded second channel |
| A hard magnet holds remanence at 0 W; what limits it is coercivity, temperature and shock ([bonded-magnets](bonded-magnets.md)) | Print tracks that keep their coercivity after impact |
| Solid particles bond above a critical velocity, 570 m/s measured for one copper powder ([EM-CSAM](EM-CSAM.md) §2.3) | Shop-scale repair, hard-face, rail-alloyed coat |
| Hydride films switch between mirror and window (published 1996, [switchable-hydride-mirror](switchable-hydride-mirror.md)) | Smart thermal / optical skin after a sealed low-inventory package exists |
| An exchange-bias loop shift vanishes near a blocking temperature below the ferromagnet's Curie point, and sets again on cooling ([exchange-pin-thermal-history](exchange-pin-thermal-history.md)) | Approximate “was this coupon overheated” bit, if the re-set shift can be told from the written one |
| A thin ferroelectric film loses its net polarization when its surface charge is poorly screened ([depolarization-fuse](depolarization-fuse.md)) | Electrode-quality witness, no deuterium |
| In-plane *B* removes an integer Hall plateau ([edge-orientation-inhibit](edge-orientation-inhibit.md); that library entry is not yet sourced) | Lab-only inhibit. Not a manufacturing product |

Not in the library, and used below as general industry knowledge: bonded magnets and ferrites are poor electrical conductors, and soft-magnetic composites exist to cut eddy currents.

---

## 3. The state palette

What the head (and the later occupancy or field-cool steps) could leave on a surface.

| State you can aim at | What the patch does afterward | Filed home |
|---|---|---|
| **Percolated metal** | dc current path. RF shield once thick against the skin depth. Reflectance set by thickness (90 % of bulk by about 30 nm of Ag, 15 nm of Al). Surface-plasmon dip with a coupler and a film in a window about 10 nm wide near 45–55 nm. | [thin-film-optics](thin-film-optics.md), [percolation-dual-switch](percolation-dual-switch.md) |
| **Islanded metal** | No dc path. Optically it still responds: an island-plasmon band, and reflectance that changes smoothly as islands join. No surface-plasmon dip below a metal fill of about 0.4. | Same files |
| **Cold-bonded splat** | Dense coat, low substrate heat. Bonding is plastic flow above a critical velocity with the bulk below *T<sub>m</sub>*. | [EM-CSAM](EM-CSAM.md) §2.3 |
| **Mushy / splash / vapor** | HAZ, crown, recondensed metal. A different write. Plasma armature is a process lever and a confound. | [EM-CSAM](EM-CSAM.md) §2.4 |
| **Hard-magnet grains with coercivity** | Remanence at 0 W. A magnet, a brake, a dock. | [bonded-magnets](bonded-magnets.md) |
| **Grains below the thermal-stability size** | Ferrofluid-like: reversible *M*(*H*), no remanence. Needs a few nm for Nd₂Fe₁₄B, 20–50 nm for magnetite, so it is a feedstock choice and no impact reaches it. | [superparamagnetism](../library/superparamagnetism.md) |
| **Soft-magnetic, electrically poor** | Flux guide with cut eddy paths (soft-magnetic composite class). | Unsourced in the library |
| **Reversible lattice H** | Capacity. Plateau. Optical state that follows the hydrogen atmosphere. | [hydride-storage](hydride-storage.md), [switchable-hydride-mirror](switchable-hydride-mirror.md) |
| **Trapped H** | Residual that does not follow the design swing. Fade, stuck shutter, or delayed crack. | On a load-bearing steel part this is a **defect** ([hydrogen-in-metals](../library/hydrogen-in-metals.md)) |
| **AFM/FM pin written** | Loop shift *H<sub>ex</sub>* at 0 W. Above the blocking temperature the shift is gone and *M<sub>r</sub>* can remain; on cooling, the pin sets again along that remanence. | [exchange-bias](../library/exchange-bias.md) |
| **Screened polar film** | Remanent *P* at *E* = 0, 0 W. | [ferroelectric-remanence](../library/ferroelectric-remanence.md); [depolarization-fuse](depolarization-fuse.md) is the failure side |
| **Rail metal in the deposit** | Alloy or contamination. Choose the rail. | Process |

**Magnetic and not conducting** is not a new phase. Ferrites and polymer-bonded NdFeB are already that. The printed claim is spatial: that patch *here*, a percolated Cu patch *there*, cold-bonded structure under both.

### 3.1 How far this scales (floor and ceiling)

This is the reality check. Most of these effects weaken gradually as the patch shrinks; a few have a real floor. People have already parked single atoms with scanning probes and written with ion beams. That is not the goal of this head.

| Effect | Small end | Large end |
|---|---|---|
| **Mirror** | No floor in thickness. Reflectance falls smoothly: Ag reflects 39 % at 10 nm and 14 % at 5 nm (computed from bulk constants; a 5.66 nm Au film matches the calculation), and a collective optical response is measured at one atomic layer ([reflection](../library/reflection.md)). | Beyond about 30 nm of Ag or 15 nm of Al, extra metal is mass. |
| **Sheet conductor** | A real floor: percolation, 6–12 nm for unseeded Ag, 6–7 nm for unseeded Au, 1–3 nm on a copper seed. It belongs to the deposition process; none is sourced for an impact deposit. | RF: a foil that mirrors can still be thin against the skin depth (2 mm in Cu at 1 kHz, 66 µm at 1 MHz). Do not quote the optical decay length as RF skin. |
| **Hard magnet** | Thermal stability is a contour that depends on the waiting time: 3.4–3.6 nm for Nd₂Fe₁₄B at room temperature and 100 s, 20–50 nm for magnetite ([superparamagnetism](../library/superparamagnetism.md)). No powder is near it. The working limit is coercivity, which in real magnets is under a fifth of the anisotropy field. | *T* → *T<sub>C</sub>* of that host (585 K for Nd₂Fe₁₄B). Above the single-domain size (0.2–0.4 µm in Nd₂Fe₁₄B) grains hold walls and are still a magnet. Shock demagnetizes (measured at 6–7 GPa). |
| **Insulating magnet / SMC** | Same magnetic limits, plus stay below electrical percolation. | If the splat field percolates electrically, the part is a conducting magnet with eddy currents. That can be what was wanted. It is a different part. |
| **Polar remanence** | No thermal-volume criterion was found. The limit is electrostatic and depends on the electrodes: polarization is reduced but present in 2.4 nm PbTiO₃ films, the polar phase is stable at 1.2 nm, and crystals of about 5 nm still switch. What goes first is net remanence, which relaxes in 10–500 µs in 5–30 nm BaTiO₃ capacitors ([ferroelectric-remanence](../library/ferroelectric-remanence.md)). | *T* → *T<sub>C</sub>* of that ceramic (393 K for BaTiO₃). |
| **Exchange-pin history bit** | The pin: no shift below a critical antiferromagnet thickness of a few nm. A small ferromagnetic grain is no obstacle; a CoO pin keeps 4 nm Co grains blocked to 220–290 K. | The trip band lies between the blocking temperature and *T<sub>C</sub>* of the ferromagnet. The blocking temperature is a distribution and moves with sweep rate. |
| **Hydride shutter** | Film thick enough to reflect, on the smooth curve above. | Cycle life and trapped hydrogen. Packaging of the H inventory is the product ceiling. |
| **Casimir force** | Thin or transparent faces reduce the force; no measured face removes it. A 9 nm Pd film gives less than a thick one, indium tin oxide 40–50 % less than Au. Islanded films are unmeasured. | Gaps of 0.1–1 µm in practice; thick real metals give 0.48–0.55 of the ideal force at 0.1 µm; above about 3 µm the thermal term dominates. Patch charge is a practical limit (unsourced here). |
| **CSAM write pixel (this head)** | Particles must pass the bore. | ~0.5 mm-class bore is the present pixel. Velocity class 200–800 m/s (hardware target). A 1 mm solid slug reaches melt-onset action at about 1800 m/s in Cu and 325 m/s in Fe on plain rails ([EM-CSAM](EM-CSAM.md) §2.2), which is why steel arrives molten. |
| **Pulse as a materials knob** | A ~1 μs pulse would reach about 0.13–0.23 mm into Cu, depending on the cut used. | A ~100 μs pulse reaches 1.3–2.3 mm of Cu. For plain rails the slug's action is fixed by its velocity, so a longer pulse is no gentler on the slug. |
| **This driver’s pulse (hardware note)** | The launch pulse is 0.2–0.7 ms at a natural frequency of 0.7–4 kHz. A ~1 μs write is outside it. | The field reaches 3–6 mm into Cu at that pulse and falls off smoothly; the slug has no skin effect. Conditioning is a separate, current-limited step. |
| **Printed logic / photonics (fantasy, §5)** | Tunnel islands and dopants are a different machine (Coulomb blockade). A magnetic bit needs *KV* of about 60 *kT* for ten-year storage in recording practice, 4.6–4.8 nm for Nd₂Fe₁₄B. A polar bit needs screening. | Complementary to a CMOS front-end. The paid ceiling today is backend, interposer, and electrical–optical packaging (unsourced). |

**Process upper bounds of the pitch itself.** Tens of joules per shot (hardware note), not a foundry. Bonded-magnet energy product below sintered (unsourced). mm-class pixels. Printed windings are not a sheet. The occupancy shutter waits on a sealed package. None of that kills the shop-scale offer in §1.

---

## 4. Speculative exploits (shop to lab)

Each box is a design target. **Stands on** is sourced or marked. **Stretch** is the part that is not demonstrated. **First trial** is a coupon. **Dies if** is how the exploit fails.

### Manufacturing and aerospace

#### A. Cold structural coat and hard-face

**Function.** Repair or wear layer on a part that must not take a heat-treat cycle. Rails can be the same metal (clean) or a chosen alloy source (hard-face).

- **Stands on.** Cold spray as an industrial process; sourced critical velocities for Cu, Al, Ti and 316L; a computed action margin of about 3 for a solid copper slug ([EM-CSAM](EM-CSAM.md) §2.2–2.3). Rail erosion as a second feedstock.
- **Stretch.** A slug of powder in a carrier is not a stream of separate particles; no source covers it. Zinc, tin and iron have no sourced bonding velocity. “Exotic alloys on the fly” means chemistry control (powder + consumed rail + carrier atmosphere).
- **First trial.** Cu/oil → metal: velocity / *I* series with slug resistance logged. Then a dissimilar-rail shot, and analyse what landed.
- **Dies if.** The only dense coats are splash-melt, the conditioned slug does not stay conducting once it moves, or rail metal is a contaminant that cannot be turned off.

#### B. Depot and later in-space repair

**Function.** Same coat, farther from a furnace.

- **Stands on.** A.
- **Stretch.** Vacuum, feedstock handling, and a vehicle or depot envelope. Unsourced.
- **First trial.** Do A in a shop until the bond window is routine. Packaging is a later file.
- **Dies if.** The process only works with a wet slurry atmosphere that cannot leave the ground.

#### C. Multi-material pixel

**Function.** Cu bus, steel wear face, Al–Si, optional graphene–Cu, on one toolhead.

- **Stands on.** Metered shots, rail choice, carrier chemistry ([PowderCarrierRailMaterial](../../em-csam/PowderCarrierRailMaterial.md)). Steel arrives molten on plain rails (iron reaches melt-onset action at 325 m/s per mm of slug), so the steel face is a hot deposit.
- **Stretch.** Registration between shots. Cross-contamination. Graphene survival (unsourced).
- **First trial.** Two-chemistry coupon with a visible seam. Measure continuity on the Cu side and hardness on the steel side.
- **Dies if.** Every shot is the same grey alloy whatever was loaded.

### Robotics and motion

#### D. Insulating magnet track in a plate

**Function.** A printed strip that holds remanence at 0 W and does not conduct. Eddy-poor on purpose.

- **Stands on.** Hard-magnet remanence and coercivity ([bonded-magnets](bonded-magnets.md)); dc percolation as a separate threshold ([thin-film-optics](thin-film-optics.md)). The first version stood this on a “*KV* cliff” near 30 nm. That size is 3.5 nm and is not the limit; the idea never needed it.
- **Stretch.** Hard-magnet grains are brittle and cold-spray bonding is plastic flow, so they need a binder that deforms. Impact must not demagnetize the grains: shock does so at 6–7 GPa in sintered Nd-Fe-B, and no impact pressure is sourced for this head. The binder must not form a conducting network.
- **First trial.** Ferrite or bonded-NdFeB-class powder, sparse splat or insulating residue, *B* on during flight or on the substrate. Read remanence and coercivity (VSM) **and** sheet resistance against impact velocity.
- **Prior art.** Cold-sprayed NdFeB exists, with an aluminum binder that deforms around the hard grains (Lamarre & Bernier, [J. Therm. Spray Technol. 28:1709, 2019](https://link.springer.com/doi/10.1007/s11666-019-00917-6); cited directly, not in the library). That deposit **conducts**. The insulating variant needs ferrite, coated grains, or a non-metallic binder.
- **Dies if.** Every magnetic deposit is either demagnetized or a conducting sheet.

#### E. Conservative linear drive

**Function.** Magnet track and/or soft-magnetic back-iron printed into a rail, platen, or robot link. **Coils stay conventional or PCB.**

- **Stands on.** D plus flux guides (G).
- **Stretch.** Alignment, pitch, and force density good enough to replace a bought linear motor on a printer-class axis.
- **First trial.** A straight printed magnet track, a voice-coil or PCB forcer already owned, a force-against-gap curve. Compare with the same forcer over a glued commercial magnet strip.
- **Dies if.** Printed remanence does not survive the splat, or the track is a conducting slab under the forcer.

#### F. Stretch: printed windings and rotary

**Function.** Isolated conductor loops and/or a printed Halbach or sector-aligned rotor ring.

- **Stands on.** Percolated Cu as a sheet conductor. Alignment *B* in flight for sector magnets.
- **Stretch. Hard.** A splat field makes a connected sheet; a winding is a long insulated wire with end-turns and layer isolation.
- **First trial.** Do not start here. After E exists: one printed hairpin, or a sector magnet ring with *B* flipped between passes.
- **Dies if.** “Printed coil” is always a shorted pancake.

#### G. Soft-magnetic composite flux guides

**Function.** Iron-class powder below electrical percolation as printed teeth or back-iron.

- **Stands on.** Soft-magnetic composites as an existing product class (unsourced in the library); dc percolation as a threshold. In an open body a soft material keeps little remanence, which is what a flux guide wants ([ferromagnetic-hysteresis](../library/ferromagnetic-hysteresis.md)).
- **Stretch.** Useful permeability after impact, without sintering into a conducting block. Iron melts at low velocity on plain rails, which works against keeping particles separate.
- **First trial.** Permeability of a printed yoke against the same powder in a known SMC process. Sheet resistance high.
- **Dies if.** The yoke carries no useful flux, or it is a solid eddy plate.

#### H. Zero-watt dock, gripper, or brake

**Function.** Write remanence, hold a tool or an axis with no current; release with a reverse field.

- **Stands on.** A magnet at rest dissipates nothing ([permanent-magnet-latch](../library/permanent-magnet-latch.md)). Switchable permanent-magnet holders are an existing product class (unsourced in the library); the new part would be printing the magnet.
- **Stretch.** Cycle life on a robot. Shock is a demagnetization route.
- **First trial.** A printed pad that picks up a keeper coupon after the write field is off, and drops it after a reverse-field pulse.
- **Dies if.** Hold requires the write coil to stay on.

Humanoid-adjacent reading of D–H, still speculative: linear joints whose stator is the link; tool changers that hold at 0 W; wear faces hard-faced in the same campaign (A); harness replaced by a printed bus (C + percolated Cu). Printers and CNCs are the nearer robot.

### Functional surfaces

#### I. Printed conducting / non-conducting map

**Function.** Patches that conduct dc and patches that do not, with optical density as a graded second channel.

- **Stood on.** A reflectance cliff at 5–20 nm. Measurements show none: reflectance rises smoothly with thickness and passes through percolation without a step.
- **Stands on now.** dc percolation, which is a threshold ([thin-film-optics](thin-film-optics.md)). The optical channel is analog: transmission falls as e^(−*d*/δ) with δ of 12–15 nm in Ag.
- **Stretch.** Thickness control at the 10 nm scale, which a splat does not have; that film comes only from the exploding or vapor regime. A metal-or-bare-glass map is ordinary patterning and needs no threshold at all.
- **First trial.** Glass slide, stepped deposit, sheet resistance and *R*(λ) / *T*(λ). Expect a dc step and a smooth optical curve. Then two regions on one slide.
- **Dies if.** No dc step at any thickness, or thickness cannot be held within the range where the patch is meant to sit.

#### J. Occupancy shutter skin

**Function.** A hydride film that is a mirror or a window with a hydrogen swing.

- **Stands on.** An existing published device: Y and La hydride films (1996) and Mg–Ni films (2001), cited in [switchable-hydride-mirror](switchable-hydride-mirror.md).
- **Stretch.** Sealed low-inventory package. Cycle life against trapped hydrogen.
- **First trial.** Not on the railgun. A purchased or evaporated film, one swing, *R*/*T* change. CSAM enters only as a possible way to lay down the metal film.
- **Dies if.** Residual after the design swing never bakes out, or the package cannot hold its inventory.

#### K. Force trim on a switched face (was “dual-starve clutch”)

**Function.** Change the conducting-plate attraction across a sub-micrometre gap by changing the film on one face.

- **Stood on.** `coupled-screening-failure`: one starve kills reflectance and the force together.
- **What the measurements show.** They do not go together. A hydride mirror switched from reflecting to transparent gave no significant change in force at 70–400 nm. Indium tin oxide gives 40–50 % less force than Au. A 9 nm Pd film gives less than a thick one. The force depends on the response of the faces over a wide band around *c*/2*d*, which is 0.1–1 eV for gaps of 1–0.1 µm, so a window in the visible removes little ([casimir-force](../library/casimir-force.md), [percolation-dual-switch](percolation-dual-switch.md)).
- **What it can be.** A trim of up to about a factor of two between a good metal and a poor conductor. A clutch would need a face whose infrared conduction can be switched off; no such measurement exists. Force on an islanded film is unmeasured and is the one open experiment.
- **First trial.** Optics and sheet-resistance series first (I). Then the same series as one plate at fixed *d*.
- **Dies if.** The islanded film gives the same reduced force as a thin continuous one (then nothing switches).

### Witnesses (QA, not the lead sell)

#### L. Thermal-history coupon

**Function.** AFM/FM stack whose loop shift records a trip past the blocking temperature.

- **Stands on.** Exchange bias, a measured effect used in spin valves ([exchange-bias](../library/exchange-bias.md), [exchange-pin-thermal-history](exchange-pin-thermal-history.md)). The split itself is established, so it is no longer a test of anything.
- **Stretch.** The shift is gone only while the stack is hot. On cooling, a magnetized ferromagnet sets the pin again, so a trip is readable only if the coupon was stored with its ferromagnet in a different remanent direction from the set one; then the shift comes back with a new sign. That state is an inference from the measured setting rule, not a demonstrated coupon. The blocking temperature is also a distribution that moves with sweep rate, so the coupon reads “above roughly *T<sub>B</sub>* for long enough,” and the shift falls with repeated reading (training).
- **First trial.** Thin-film lab: field-cool, reverse the ferromagnet, trip, cool, read the sign of the shift. CSAM is probably the wrong writer for the antiferromagnet.
- **Dies if.** The reversed state cannot be held, so every trip restores the original shift; or the distribution of blocking temperatures in a practical film is too wide to give a usable trip band.

#### M. Screening witness (was “depolarization fuse”)

**Function.** A thin ferroelectric capacitor whose net polarization does not hold when its electrodes screen poorly.

- **Stood on.** A thickness envelope below which the polar well is empty, as the electrical twin of a magnetic volume limit.
- **What the measurements show.** No such volume limit. The polar phase is stable at 1.2 nm. What is lost is net remanence: in 5–30 nm BaTiO₃ capacitors it relaxes within 10–500 µs when the residual depolarizing field reaches the coercive field, and that field is set by the electrode's screening length ([ferroelectric-remanence](../library/ferroelectric-remanence.md)).
- **What it can be.** A witness of electrode and interface quality at fixed thickness, read as retention. This is a known reliability effect in thin ferroelectric capacitors; the idea is a use, not a discovery.
- **First trial.** Thin-film shop. Same film, two electrode materials; retention against time.
- **Dies if.** Retention does not depend on the electrode.

#### N. Orientation inhibit

**Function.** Rotate *B* in-plane on a 2DEG Hall bar; the integer plateau is absent.

- **Stands on.** [edge-orientation-inhibit](edge-orientation-inhibit.md). The quantum Hall library entry is not yet sourced.
- **Stretch.** None for manufacturing. Lab only.
- **First trial.** Only if the fridge and the magnet already exist.
- **Dies if.** This paragraph is used to sell a product.

---

## 5. If the write pixel goes to nano (fantasy, not a roadmap)

Skip this section if you came for hard-facing. Everything in it is unsourced unless a library link says otherwise.

The ~0.5 mm barrel is a **metering and launch** story. If the valuable object is the **state palette** in §3, then shrinking the pixel is an industry problem. People already move atoms with FIB, MBE, ALD, STM lithography, ion implant, and e-beam. A “single atom out of a barrel” is not Lorentz slurry at 1 Å, and it is not the goal.

What a free budget would buy is a **directed writer that can choose which state to leave**, aimed first at µm, then nm. §3.1 still applies, with its corrections: a thinner metal film reflects less by degrees and stops conducting dc at percolation; a magnetic bit needs retention; a polar bit needs screening. Atom-scale writing gets dopants, islands, and tunnel gaps, which is a different machine.

EUV and a CMOS front-end are not the competitor. The live need is **backend, interposer, photonics packaging, and mixed electrical–optical I/O**.

### O. Pixel-size ladder as a program

mm splat → µm jet or FIB-cousin → nm directed beam → atom/ion optic. Same palette, finer aim.

- **Stands on.** §3.1. Directed-write tools exist; they do not offer this palette as one head.
- **Stretch.** One tool family that can pick conducting / non-conducting / hard-magnetic / soft / occupancy / pin / polar.
- **If money were free.** Three writers, one metrology stack (*R*/*T*, sheet resistance, VSM, TDS, *P<sub>r</sub>*), same coupons stepped down in pitch.
- **Dies if.** Finer pixels only reproduce lithography’s existing materials, with no state choice beyond “metal is here.”

### P. Additive backend / interposer

Percolated Cu as interconnect. Gaps as high-resistance regions. Insulating-magnet islands as inductor cores next to RF traces.

- **Stands on.** I, D, G. The optical decay length (Ag 12–15 nm, Al 6.6–8.3 nm) is not the RF skin depth.
- **Stretch.** Registration, via-like continuity in *z*, contamination from the writer.
- **If money were free.** An interposer coupon: a transmission line, a gap, a printed core, S-parameters against a lithographed twin.
- **Dies if.** The only continuous Cu is a shorted plane, or the “core” percolates and kills Q.

### Q. Mixed electrical and optical fabric (the ceiling hook)

A metal line is an electrical path and can also carry a surface plasmon. A dielectric or hydride neighbour is a window or a modulator.

- **Stands on.** [surface-plasmon-resonance](../library/surface-plasmon-resonance.md): the mode needs a coupler and a film in a thickness window about 10 nm wide (near 45–55 nm at 633 nm), and by the single-interface model it runs 65–73 µm on Ag and 10–15 µm on Au at 633 nm. [switchable-hydride-mirror](switchable-hydride-mirror.md), I, J.
- **Stretch.** Thickness held to a few nm, roughness, and a pixel no larger than the mode's run length. A mm-class splat cannot do this.
- **If money were free.** One substrate, one metal line that carries current and shows a measurable surface-plasmon dip, next to a window that transmits in the same band. Then a hydrogen swing on one pixel only.
- **Dies if.** Electrical continuity and the optical mode never coexist on the same written metal.

### R. Crude printed logic (not a CPU)

Majority / relay class, labeled **crude**.

1. Percolation as a one-way “this wire exists” fuse.
2. Magnetic bits or exchange-pin cells as 0 W state, sized for retention (about 60 *kT* for ten years in recording practice).
3. Polar bits, limited by screening and thin-film relaxation.
4. Occupancy as a chemical / optical bit.
5. A metallic island with tunnel gaps as a single-electron gate, **if** the writer can leave a gap on purpose.

- **Stands on.** §3.1. All five are existing device classes elsewhere (magnetic recording, FeRAM, single-electron transistors); the claim is one writer, not new bits.
- **Stretch.** Isolation and registration.
- **If money were free.** A three-bit magnetic or polar coupon that holds overnight at 0 W, plus one percolation fuse that can be blown.
- **Dies if.** The only “logic” is a shorted sheet, or bits relax on lab time.

### S. Mechatronic pixel

Motor track + interconnect + optical line + thermal-history coupon on one piece.

- **Stands on.** E, C, Q, L.
- **Stretch.** All of those stretches at once.
- **If money were free.** After E and a crude Q exist, put them on one coupon. Do not start here.
- **Dies if.** Each function only works on its own dedicated substrate.

### T. On-wafer nanopositioner (dogfood)

Printed magnet tracks plus conventional coils as the stage that aims the next finer pixel.

- **Stands on.** E, F, O.
- **Stretch.** Encoder-class pitch and a writer mounted on its own output.
- **If money were free.** A mm-scale printed track that moves an optics stage.
- **Dies if.** E never beats a glued magnet strip.

### U. Directed-atom chemistry

The hardware note’s rail-as-alloy, taken to the limit: the “rail” or ion source is a dopant valve. Place a species and name the landing state (metal, oxide, vacancy, occupancy).

- **Stands on.** Intentional rail consumption. Existing implant / MBE practice.
- **Stretch.** Calling that the same head. It is the same palette with a different writer.
- **If money were free.** Buy time on a directed-write tool and try to leave two states from §3 on one coupon. Do not build a nano-railgun to learn this.
- **Dies if.** The landing species cannot be read as one of the filed states.

---

## 6. Technical annex (first series, not a factory)

Full isolation sequences live in the application files. Do not skip to a nuclear search.

### 6.1 Number classes (do not equate)

Each row links its source. **Kind** says whether the number marks a threshold or a point on a smooth curve.

| Quantity | Value | Kind | Source |
|---|---|---|---|
| Ag/Al optical decay length (intensity, 450–650 nm) | Ag 12–15 nm, Al 6.6–8.3 nm | Crossover: an e-folding length, no minimum thickness | [reflection](../library/reflection.md) |
| Reflectance at half and at 90 % of bulk, 550 nm | Ag 12–14 nm and 31–33 nm; Al 4.5–6 nm and 14–17 nm | Crossover | [reflection](../library/reflection.md) |
| dc percolation thickness | Unseeded Ag 6–12 nm, unseeded Au 6–7 nm, 1–3 nm on a Cu seed; none sourced for Cu or for impact deposits | Threshold, process-dependent | [reflection](../library/reflection.md) |
| Nd₂Fe₁₄B thermal-stability diameter, 300 K, 100 s (25 *kT*) | 3.4–3.6 nm sphere; 4.6–4.8 nm at 60 *kT* | Crossover: a retention-time convention; not the limit of a real magnet | [superparamagnetism](../library/superparamagnetism.md) |
| Magnetite, same convention | 20–50 nm | Crossover | [superparamagnetism](../library/superparamagnetism.md) |
| Hard ferrite, same convention | 8.2–8.5 nm (computed here from *K*<sub>1</sub> = 0.32–0.36 MJ/m³) | Crossover | [shape-anisotropy](../library/shape-anisotropy.md) for *K*<sub>1</sub> |
| Nd₂Fe₁₄B *T<sub>C</sub>* | 585–588 K | Threshold | [permanent-magnet-latch](../library/permanent-magnet-latch.md) |
| Ni *T<sub>C</sub>* | 628–631 K (about 355 °C) | Threshold | [permanent-magnet-latch](../library/permanent-magnet-latch.md) |
| BaTiO₃ *T<sub>C</sub>* | 393 K (120 °C; 120–130 °C by crystal) | Threshold | [ferroelectric-remanence](../library/ferroelectric-remanence.md) |
| Exchange-bias blocking temperature | System-specific, at or below the Néel temperature of the layer | Crossover: distribution, rate-dependent | [exchange-bias](../library/exchange-bias.md) |
| Cu pulse depth, 2√(*Dt*) (other cuts are 0.4–0.65 of it) | 0.23 mm at 1 μs; 2.3 mm at 100 μs; 3.3–6.2 mm at 0.2–0.7 ms. Steady 1 MHz skin depth is 66 μm, a different rule | Crossover: no edge | [skin-effect](../library/skin-effect.md) |
| Action at melt onset | Cu 8.05, Al 2.52, Ni 1.72, Fe 1.28 × 10¹⁶ A² s m⁻⁴ (one data set) | Threshold | [electrical-resistivity](../library/electrical-resistivity.md) |
| Heat from 300 K to melt onset / fully liquid | Cu 466 / 673 kJ/kg | Threshold (latent heat) | [melting](../library/melting.md) |
| Critical bonding velocity | Cu 570 m/s measured (300–610 with powder oxygen); Al 775–825; Ti 505–610; none sourced for Zn, Sn, Ni, Fe | Threshold for one particle; crossover in deposition efficiency for a powder | [elasticity](../library/elasticity.md) |
| Head velocity | 200–800 m/s class | Hardware target, unmeasured | [EM-CSAM](EM-CSAM.md) §2.1 |
| Paschen floor | Air 327–352 V; H₂ 230–273 V | Threshold | [dielectric-breakdown](../library/dielectric-breakdown.md) |
| Contact melting voltage | Cu 0.43 V | Threshold | [electrical-contacts](../library/electrical-contacts.md) |
| Casimir force on a thin or transparent face | Reduced by up to about half; not removed | Crossover | [casimir-force](../library/casimir-force.md) |
| Steel bake-out of production hydrogen | 200 °C for 10 min sufficed for one hot-stamped martensitic steel; check the spec for the alloy | Crossover (Arrhenius detrapping) | [hydrogen-in-metals](../library/hydrogen-in-metals.md) |

Curie points, blocking temperatures and melting points are different numbers of different kinds. See [requirement-audit](../library/derived/requirement-audit.md), where `coupled-screening-failure`, `connected-spatial-buffer` and `latch-cell-is-the-cliff` are now recorded as in tension with the sourced library.

### 6.2 First series a shop can run

Reuse the [EM-CSAM](EM-CSAM.md) §4 campaigns. No D₂, no neutron channel, no BeCu unless that shop already exists.

| Order | Coupon | Question |
|---|---|---|
| 0 | Driver into shorted rails | *L*′, loop resistance, EMI and heat baseline |
| 1 | Slug conditioning, then motion | Does the slug stay conducting (the launch window in [EM-CSAM](EM-CSAM.md) §2.2)? |
| 2 | Cu / oil → metal, *I* / velocity series | Bond against melt (A) |
| 3 | Exploding foil or wire → glass, thickness series | dc percolation step, smooth *R*/*T* (I) |
| 4 | Ni, then ferrite or bonded-NdFeB-class powder, in-flight *B* | Remanence and coercivity kept against velocity (D, start) |
| 5 | Magnetic powder, sparse / insulating residue | *M<sub>r</sub>* **and** high sheet resistance (D proper) |
| 6 | Printed track + bought forcer | Force against a glued magnet strip (E) |
| 7 | Steel + dry vs H-rich carrier, bake column | Embrittlement as a **warning** |
| 8 | Optional: two-chemistry seam | Multi-material pixel (C) |

Hydride shutter (J), force trim (K), exchange-pin (L), and screening witness (M) are **other benches**.

### 6.3 Falsifiers of this pitch

These are how the *sell* dies.

- A conditioned slug does not stay conducting once it moves, so every shot is an exploding slug.
- No dense deposit without splash-melt at any velocity the head reaches.
- Cu-on-glass sheet resistance shows no step at any deposited thickness.
- Every magnetic splat is either demagnetized or conducts like a metal sheet.
- Printed tracks keep no useful coercivity after impact at any bonding velocity.
- Shots with and without a muzzle-voltage jump are calorimetrically identical after *R*∫*I*²*dt* (then plasma is not a separable state).

Removed in this revision because the outcome is already known: “*R* grows linearly with no percolation cliff” (reflectance is smooth; the step is in dc conductance), “Ni and Pd look the same on remanence” (Pd is not ferromagnetic), and “a hydride shutter that needs hold voltage” (the published devices follow the hydrogen atmosphere).

If the slug-resistance series fails, the rest of the barrel work waits. If the coercivity series in [bonded-magnets](bonded-magnets.md) fails, drop D–H.

---

## 7. What this is asking

**A manufacturing or aerospace contact.** A conversation, a coupon, or a day on a spray / magnet / optics bench. The nearest paid shapes are A (coat / repair / hard-face), D–E (insulating magnet and a linear track in a plate), and C (two metals, one head).

**A maker or lab.** One row of §6.2, with results read against the sourced numbers in §6.1.

**A well-funded workshop that likes the ceiling.** §5 after §6.2 is routine. Start with Q’s crude coupon (current and a surface-plasmon dip on the same written metal) and E’s track against a glued strip. Do not start by building a nano-railgun.

**Not asking.** Nuclear search. Scaling the bank. Casual BeCu. H₂ plus powder as a demo. Adding a pyroelectric crystal or a muon “to help.”

---

## Links

| File | Role in this brief |
|---|---|
| [EM-CSAM](EM-CSAM.md) | Head as writer; heat and bonding budget; campaigns |
| [thin-film-optics](thin-film-optics.md) | Reflectance, percolation, SPR |
| [bonded-magnets](bonded-magnets.md) | Hard-magnet limits |
| [hydrogen-embrittlement](hydrogen-embrittlement.md) | Process warning |
| [hydride-storage](hydride-storage.md) | Two H populations |
| [switchable-hydride-mirror](switchable-hydride-mirror.md) | Occupancy shutter (existing device) |
| [percolation-dual-switch](percolation-dual-switch.md) | Three readouts of one film; force channel |
| [exchange-pin-thermal-history](exchange-pin-thermal-history.md) | Blocking-temperature witness |
| [depolarization-fuse](depolarization-fuse.md) | Screening witness, no D |
| [edge-orientation-inhibit](edge-orientation-inhibit.md) | Lab inhibit only |
| [`../../em-csam/`](../../em-csam/README.md) | Hardware notes |

Out of scope on purpose: [EM-LENR](EM-LENR.md), [polar-beam-gate](polar-beam-gate.md), [muon-hydrogen-gate](muon-hydrogen-gate.md), [coherence-window-recoil](coherence-window-recoil.md).
