---
origin: application
device: metal-hydride storage bed / tank / compressor
updated: 2026-11-13
---

# Application: Metal-hydride storage

**Device.** A packed bed or tank of hydride-forming metal (LaNi₅-class, TiFe, Mg, Pd, Ti) that takes up and gives back hydrogen on a *P*–*T* swing.
**QSA machines.** `ensemble-average` (dilute lattice H); a hysteretic first-order transition (the hydride plateau); trapped H at defects; `oscillator-grid` (*T*<sub>m</sub>, decrepitation, thermal conductivity of the bed).
**Status.** Working application. No anomaly claim. **Not a tested protocol.** Hydrogen service and fine powder are industrial hazards ([SAFETY.md](../SAFETY.md)).

> **Changed 2026-11-13**, after [hydrogen-in-metals](../library/hydrogen-in-metals.md) (below **HM**) was sourced. Nickel is removed from the device list: it forms a hydride only above about 6 kbar. The plateau is now described as a hysteretic first-order transition; the earlier text called it "filling the reservoir" and "not a latch write". Release of trapped hydrogen is an Arrhenius crossover with no "blocking line". "Fines trap more per gram" is dropped: the sourced statement is that smaller specimens retain less. Falsifiers are restated as desorption and isotherm measurements.

---

## 1. Claim

Three hydrogen populations share the tank, and only the first is the product.

| Population | Sourced behaviour (HM §4.3) | What the designer wants |
|---|---|---|
| Hydride phase, across the plateau | First-order transition with hysteresis: absorption and desorption occur at different pressures. Pd: 2.0 kPa (H₂) at 298 K; two-phase region closes at 566 K; volume change 10.9 % | Reversible capacity. The swing must span both branches of the loop |
| Dilute lattice hydrogen | \(c \propto \sqrt{p}\,e^{-E_S/RT}\), no threshold | Small; follows the gas |
| Hydrogen at vacancies, dislocations, grain boundaries, surfaces | Bound per atom (0.15–0.31 eV in Pd), binding falling as a site fills; released by Arrhenius detrapping | A residue that does not come off on the design swing |

Bulk H/M is the sum. An isotherm reads the first two. Thermal desorption reads the third.

Palladium is the only host in the list whose numbers are sourced in the library. The LaNi₅, TiFe and Mg classes are named as device classes; their plateau data are not in the library.

---

## 2. Theory of operation

**Useful capacity.** Raise *P* or lower *T* through the absorption plateau; reverse through the desorption plateau. The pressure gap between the two is the hysteresis. Where the two phases stay lattice-coherent the barrier between them is strain energy proportional to the transforming volume (HM §4.3, Schwarz–Khachaturyan model); in bulk material the transformation is incoherent and makes dislocations. In the project's vocabulary the plateau is a write with a loop, and the loop area is work lost per cycle.

**Damage.** The volume change deforms the host: in bulk palladium the β phase nucleates incoherently and dislocations form to relieve the elastic stress (HM §4.3). New defects are new trap sites. That cycling increases the trapped residue in a given storage alloy is a hypothesis here; no cycling data are in the library.

**Release of trapped hydrogen.** Per atom, at a rate \(\propto e^{-E_a/RT}\). There is no critical temperature. A trap deeper than 50 kJ mol⁻¹ is called irreversible at room temperature by convention; a 50 kJ mol⁻¹ trap releases 1750 times faster at 473 K than at 298 K. A bake above the service temperature is therefore a faster release, and how complete it is depends on time and trap depth.

**Size.** In palladium the absorption plateau falls and the hysteresis narrows as particles shrink below 30–50 nm, and no hydride forms below 2.6 nm (HM §4.3). Smaller specimens also retain less hydrogen after the gas is removed, because the path to the surface is short.

**Grid.** Bed thermal conductivity is `thermal-conductivity-phonon` plus gas in the voids; a starved bed has a hot core and a cold skin. Overshoot to *T*<sub>m</sub> is `coupled-grid-loss`, a different failure from a plateau shift.

Capacity fade is not a nuclear effect. Residual hydrogen is not [muon-catalyzed fusion](../library/muon-catalyzed-fusion.md) and not a [polar-beam-gate](polar-beam-gate.md).

---

## 3. Knobs

| Parameter | Toward a reversible bed | Toward measuring the trapped residue |
|---|---|---|
| Cycle count | Minimize plastic damage | Walk cycles and record the desorption spectrum at each stage |
| Particle size | Heat and mass transfer against fire risk; below tens of nanometres the plateau itself changes | A size series, with the retention effect of short diffusion paths taken into account |
| Activation / bake | Only as needed to open the surface | A bake series at several temperatures and times (Arrhenius) |
| Alloy / coating | Plateau pressures of both branches inside the service band | A clean lot against a cold-worked lot at the same plateau capacity |
| *P*–*T* swing | Wide enough to cross both branches | Over-swing that decrepitates the bed |
| Residual after designed desorption | At the specified residual | A higher-temperature desorption peak and its activation energy |

---

## 4. Isolation sequence

0. First absorption and desorption isotherm on an activated, un-cycled lot: both plateau pressures, hysteresis width, residual.
1. *N* cycles on the same swing: plateau pressures and residual against *N*.
2. Thermal desorption after the designed desorption: peak temperatures, areas, and their shift with heating rate.
3. Bake series: residual against bake temperature and time.
4. Cold-worked against annealed powder of one chemistry, first cycle.
5. Size cuts at fixed *N*.

---

## 5. Falsifiers

- No desorption peak remains above the designed desorption temperature at any cycle count, and the residual is accounted for by the isotherm.
- Cold work changes neither the residual nor the desorption spectrum at fixed plateau capacity.
- The residual does not fall with bake temperature in the Arrhenius manner.

---

## 6. Link to EM-CSAM

A railgun or coil pulse on hydride powder is an extreme deformation step. Whether it adds trap sites beyond what milling adds is the question posed in [EM-LENR](EM-LENR.md) §6; it is also a warning if the feedstock is a storage alloy that was meant to stay reversible. See [EM-CSAM](EM-CSAM.md). The same hydride transition read as an optical switch is [switchable-hydride-mirror](switchable-hydride-mirror.md).
