# Application: EM-LENR — Configuration Hypothesis for Hydrogen in a Pulsed Metal Powder

**Source problem:** configuration dependence of reported LENR / gas-loaded-metal anomalies.
**QSA role:** an application of the effect library to an unisolated problem, graded against sourced hydrogen and magnet facts.
**Status:** Working application. A hypothesis and a test plan. No nuclear process is asserted. **Not a tested protocol.**
**Updated:** 2026-11-11

> **Hazards (read [SAFETY.md](../SAFETY.md)).** H₂/D₂, fine metal powder, and pressure in one vessel are a fire, leak, and dust-explosion stack. A wet bed adds steam and a flammable headspace. kA-class pulses injure at arm's length even at tens of volts. BeCu is named only for shops that already control beryllium; otherwise stay on copper. This file is a mapping, not a procedure. Do not scale inventory, pressure, pulse energy, or liquid volume in search of a nuclear signature. Do not skip to a neutron search.

**Credit.** The physical problem, the configuration hypothesis, and the experimental direction are Steven E. Jones's. The notes this file analyzes were developed in collaboration with the author of this repository ([`../../em-csam/EM-CSAM-LENR.md`](../../em-csam/EM-CSAM-LENR.md), kept as the historical record). The EM-CSAM micro-railgun entered only as a related thought experiment. This document is QSA analysis of that work, not a claim of authorship of it.

**Sources.** Hydrogen facts are cited to [hydrogen-in-metals](../library/hydrogen-in-metals.md) (below **HM**) by section; strain and field facts to [magnetostriction](../library/magnetostriction.md) (**MS**); blocking to [superparamagnetism](../library/superparamagnetism.md). Their Sources tables hold the references. Arithmetic introduced here is guarded in [`analysis/checks/b2_hydrogen.py`](../analysis/checks/b2_hydrogen.py).

> **What changed on 2026-11-11, and why.** The earlier version was written before any hydrogen fact in the library was sourced. Checking it against sources changed six things.
> 1. The "blocking" analogy (a trapped hydrogen cluster held by a barrier that grows with its volume, as \(KV\) does in a magnetic grain) is withdrawn. Trapped hydrogen is bound per atom. The volume-proportional barrier that the sources do support belongs to the coherent hydride transition, which the earlier version set aside as "capacity".
> 2. Nickel was ranked first and described as loading hydrogen. Under 20–300 bar near room temperature it holds \(10^{-4}\) hydrogen atoms per metal atom and forms no hydride. The host table is corrected and palladium is the first host.
> 3. Magnetostriction was named as the scribe. It is the smallest strain in the cell. The write channel is now given as computed strains.
> 4. The success criterion had no dependent variable. Readouts are now defined: thermal desorption, the pressure–composition isotherm, lattice parameter, resistance.
> 5. Cells that cannot exist (a preloaded nickel hydride at ambient pressure) are removed, and several "predictions" are reclassified as established or contradicted (§8).
> 6. The 2019 multi-laboratory null result is cited (§9).

---

## 1. Scope and hypothesis

**The configuration hypothesis (Jones).** Reported anomalies in Pd–D, Ni–H and related systems depend on a specific arrangement of hydrogen in the metal that has not been isolated, and average loading alone does not predict them.

This file takes the hypothesis as a materials question and asks what it could be about, given what is measured. It asserts no nuclear process. It is useful if it names a state that can be written, detected after the drive is off, and erased, with instruments that already exist. If the tests in §6 fail, the mapping is wrong. Record that; do not patch it with a new nuclear story.

The discipline of the earlier version is kept: baselines before physics, a materials state before any nuclear search, falsifiers written in advance.

The project vocabulary is used as a speculative mapping: **capacity** (equilibrium occupancy set by pressure and temperature), **write** (a process that changes where hydrogen sits), **hold** (the state remains with the drive off), **erase** (heating removes it).

---

## 2. Two sourced objects the hypothesis could be about

The sources support two different objects. They are kept separate here.

| | (a) Trapped hydrogen | (b) Coherent hydride transition |
|---|---|---|
| What it is | Hydrogen at vacancies, dislocations, grain boundaries, voids | First-order α→β transition of a hydride former |
| Barrier | Binding energy per atom. Pd: 0.31, 0.23, 0.15 eV for vacancy clusters, single vacancies, and vacancies at high occupancy. bcc iron defects: 9–78 kJ mol⁻¹ | Coherency strain energy, proportional to the transforming volume |
| Dependence on amount held | Binding falls as a site fills; a vacancy holds up to six atoms | Barrier grows with particle volume |
| Hold | Remains after the gas is removed; occupancy follows the lattice concentration | Either phase persists between the desorption and absorption pressures |
| Erase | Arrhenius release, \(e^{-E_a/RT}\) per atom; no critical temperature | Cross the other branch of the loop, or exceed the critical temperature (566 K in bulk Pd) |
| Size dependence | None sourced as a threshold. Smaller specimens retain less hydrogen | Pd: absorption branch size-dependent below 30 nm; sloped transitions below 15 nm; coherent below about 50 nm; \(T_c(L) = 566 - 2381/L\) K |
| Measured by | Thermal desorption: peak temperature, area, shift with heating rate | Pressure–composition isotherm: plateau pressures and hysteresis width |
| Where it exists | Any metal with defects | Pd at about 2 kPa; Ni only above 6 kbar |

All entries are from HM §4.3 ("Trapping", "Palladium–hydrogen", "Size effects in palladium") and HM §4.6.

Reading of the hypothesis against these:

- The earlier version's latch, "cell volume × barrier ≳ *kT* ln(*τ*/τ₀)", described object (b) and assigned it to object (a). Object (b) is the hydride transition itself, which that version dismissed as "bulk β-phase fraction" and "capacity".
- If the hypothesis is about (a), the state is an ordinary trapped population whose amount and binding energies depend on defect history. Standard metallurgy already describes it. The open question is only whether a pulse changes it in a way that soaking, cold work and heating do not.
- If the hypothesis is about (b), the host must be a hydride former at the working pressure. That is palladium. The size dependence the earlier version looked for is measured there, without any pulse, in single nanocrystals.
- A third sourced object, vacancies bound to hydrogen at up to 30 at. % (superabundant vacancies), forms under hydrogen fugacity at the GPa level (HM §4.3). It is outside this apparatus.

No opened source gives a trapped population a barrier that scales with its volume (HM §4.6). The \(KV\) form stays where it is sourced: the magnetic moment of a grain ([superparamagnetism](../library/superparamagnetism.md) §4.3) and the coherent hydride transition.

---

## 3. Hosts

Values at 298 K. Solubilities for Ni, Fe and Cu are computed in HM §4.3 from fits measured above 500 K, so they are extrapolations.

| Host | State under H₂ | H/M | Hydride | Magnetic | What a column can test | What it cannot |
|---|---|---|---|---|---|---|
| **Pd** | Hydride former | 0.68 at 1 atm | Plateau 2.0 kPa (H₂), 9.8 kPa (D₂); misfit 3.5–3.7 % linear | Not ferromagnetic (not sourced in the library) | Objects (a) and (b). Whether a pulse shifts the plateau, the hysteresis width, or the desorption spectrum | Any magnetostrictive channel |
| **Ni** | Dilute solid solution | \(1.8\times10^{-5}\) at 1 bar; \(8.0\times10^{-5}\) at 20 bar; \(1.3\times10^{-4}\) at 50 bar; \(3.1\times10^{-4}\) at 300 bar | Forms above 6 kbar, decomposes near 3.4 kbar | Ferromagnet; Curie point 631 K | Object (a) only, in a magnetic host: whether a pulse changes the trapped population | Object (b); size-dependent hysteresis; any test that needs high occupancy |
| **Fe** | Dilute solid solution | \(5.7\times10^{-8}\) at 1 bar | Not addressed in the library | Ferromagnet | A magnetic host with 310 times less lattice hydrogen than Ni and much faster transport | Object (b) |
| **Cu** | Dilute solid solution | \(2.3\times10^{-9}\) at 1 bar | — | No | Plain-conductor baseline for eddy and Joule heating | Anything about hydrogen |

Consequences for nickel (HM §4.3, "Dilute solubility" and "Nickel–hydrogen"):

- Raising the pressure from 20 to 300 bar raises H/Ni by \(\sqrt{15} = 3.9\). There is no threshold in that range. The hydride needs 20 times the pressure of a 300 bar vessel.
- Nickel cannot be "loaded" or "preloaded" as a hydride in this apparatus. A nickel hydride made at kilobar pressure decomposes below about 3.4 kbar, so a preloaded nickel hydride under an inert headspace at ambient pressure does not exist as a stable inventory.
- Uptake cannot be verified by mass or pressure drop. One gram of nickel at 300 bar holds 5.3 µg of hydrogen (2.6 µmol H₂); in a 1 cm³ gas space that is 0.065 bar out of 300, a relative change of \(2.2\times10^{-4}\). Gas adsorbed on the powder surface is not quantified in the library and would add to any measured uptake.
- What a nickel column can show is a difference in the thermal desorption spectrum between pulsed and unpulsed powder. It can show nothing about a hydride.

Ranking for this apparatus: **Pd first**, because both objects exist there at pressures below one atmosphere and published values give a reference. **Ni second**, for object (a) in a magnetic host. **Cu** as the conductor baseline. **Fe** optional.

A palladium column needs no high pressure. The 2.0 kPa plateau is \(10^{-3}\) of the 20 bar prototype ceiling in the earlier version. The high-pressure cells of that version buy a factor of 3.9 in nickel occupancy and are dropped from the plan.

---

## 4. The write channel

### 4.1 Strains a pulse delivers

| Source of strain | Magnitude | Inputs and reference |
|---|---|---|
| Saturation magnetostriction of Ni | \(3.5\)–\(4.0\times10^{-5}\) | Measured polycrystalline values −35 and −40 ppm (MS §4.3) |
| Thermal expansion of Ni | \(1.34\times10^{-5}\) per kelvin | Expansivity \(13.4\times10^{-6}\) K⁻¹ (MS §4.3). One kelvin is 0.38 of the 35 ppm magnetostriction; 2.6–3.0 K equals all of it |
| Elastic strain of Nickel 200 at yield | \(8.2\times10^{-4}\) | 163 MPa over 199.5 GPa; 23 times the magnetostriction (MS §4.3) |
| Hydride misfit, Pd | \(3.5\times10^{-2}\) | Lattice parameter 3.889 Å to 4.025 Å (HM §4.3); 870–1000 times the nickel magnetostriction |
| Hydride misfit, Ni | \(5.9\times10^{-2}\) | 3.5238 Å to 3.731 Å, above 6 kbar only (HM §4.3); 1500–1700 times |

Stress is a separate question from strain. A free body magnetostricts without stress; stress appears only where the strain is constrained, and its ceiling is \(E\lambda_s\), 7.0–8.8 MPa in nickel, which is 4.3–5.4 % of the 163 MPa yield constant (MS §4.3 and §4.5, "clamping"). A loose powder particle is close to the free case. By the same reasoning, uniform heating of a free particle is stress-free and thermal stress needs a gradient or a constraint (inference made here from the elasticity definitions; no source was opened for it).

The field needed is also sourced: an isolated nickel sphere needs about 0.23 T applied to saturate (MS §4.3).

**Conclusion.** Magnetostriction is the smallest strain in the cell. A pulse that heats a nickel particle by 3 K strains it as much as full magnetic saturation does, and the stress available from a fully clamped grain is about a twentieth of yield. It cannot be assumed to create defects or to be the scribe. Lorentz and eddy-current body forces are not computed here; no sourced number for them is in the library.

### 4.2 What the host comparison can still separate

Ni against Pd against Cu remains a useful control design for three properties: a magnetic host, a hydride former, a plain conductor. It can show whether an effect needs a ferromagnet, needs a hydride phase, or appears in any conductor heated the same way.

It cannot attribute a nickel-only effect to magnetostriction. Nickel differs from palladium in hydrogen content by a factor of \(3.8\times10^{4}\), in hydrogen diffusivity by a factor of 1500, and, by inference made here with no sourced number, in magnetic hysteresis heating and in how its permeability changes the eddy-current coupling. Controls that address magnetostriction directly are sourced in MS §4.3: nickel above its Curie point (631 K), where the strain is zero; a peak field below and above the 0.23 T saturation field of a sphere; and Ni with 7 at. % Ga, whose magnetostriction is −10 ppm against −35.

### 4.3 Clocks

| Clock | Value at 298 K | Consequence |
|---|---|---|
| Coil pulse | 10–100 µs (carried from the source notes) | The write envelope |
| Hydrogen diffusion in Ni | \(D = 5.1\times10^{-14}\) m² s⁻¹; 0.71 nm in 10 µs, 2.3 nm in 100 µs; 1 µm in 20 s; 100 µm in 55 h | Lattice hydrogen in nickel does not move during a pulse. Soak times are seconds for micrometre grains and days for 100 µm grains |
| Hydrogen diffusion in Pd | \(D = 7.7\times10^{-11}\) m² s⁻¹; 28 nm in 10 µs, 88 nm in 100 µs; 1 µm in 13 ms | Hydrogen can cross a nanoparticle during a pulse and a micrometre grain between pulses |
| Hydrogen diffusion in Fe | 850 nm in 100 µs | Fast transport, almost no content |
| Detrapping | \(e^{-E_a/RT}\) per atom; a 50 kJ mol⁻¹ trap releases 1750 times faster at 473 K than at 298 K | The hold and erase clock. Traps deeper than 50 kJ mol⁻¹ are called irreversible at room temperature by convention |
| Magnetic blocking of a Ni grain | Tabulated blocking diameter 34 nm for \(KV = 25\,kT\) | A statement about the moment of the grain on a 100 s window, and a crossover. It is not a hydrogen clock |
| Thermometer or calorimeter | Seconds | Reads the average temperature only |

Diffusion values are from HM §4.3 ("Diffusion"); blocking from [superparamagnetism](../library/superparamagnetism.md) §4.3.

The earlier version required the pulse to be "long enough for gas to enter an opened volume". In nickel that cannot happen on the pulse clock: hydrogen moves 2.3 nm in 100 µs. Any hydrogen a pulse rearranges in nickel is hydrogen that was already within nanometres of the site.

---

## 5. Parameters and observables

### 5.1 Readouts (the dependent variables)

| Readout | Quantity recorded | Object | Reference value or caveat |
|---|---|---|---|
| Thermal desorption spectrum | Peak temperatures, peak areas, shift of each peak with heating rate (gives \(E_a\)) | (a) | Method and limits in HM §4.3: peak assignment can be speculative; small specimens lose hydrogen quickly, faster in vacuum than in argon. Nickel holds ppm-level hydrogen, so the blank matters |
| Pressure–composition isotherm (Pd) | Absorption and desorption plateau pressures at fixed temperature; hysteresis width \(\ln(p_\mathrm{abs}/p_\mathrm{des})\); H/Pd at 1 atm | (b) | 2.0 kPa (H₂) and 9.8 kPa (D₂) at 298 K; 0.68 at 1 atm. No bulk hysteresis ratio was found as a number in an opened source |
| Lattice parameter by diffraction | \(a\) before and after; phase fractions | (b) | Pd 3.889 Å; β phase \(a = 3.9321 + 0.1719\,x\) Å. Nickel should stay at 3.5238 Å; 3.731 Å would mean hydride |
| Resistance | Change on loading and after pulsing | Both | Secondary readout. No calibration is sourced in the library |
| Coil *I*(t), *V*(t); cell *T*(t) | Pulse energy and temperature rise | Control | Needed to build the heat-matched control of §5.2 |
| Grain-size distribution, microscopy | Size and defect state | Both | Measured, not taken from a vendor label |
| Neutron channel, calorimetry | — | Search | Phase 5 only |

### 5.2 Controls every pulsed cell needs

- **Heat-matched, no field.** Because 2.6–3.0 K of heating equals the full magnetostrictive strain, each pulsed cell is paired with a cell given the same temperature history without the field.
- **Soak only.** Same gas, pressure, temperature and time, no pulse.
- **Inert gas.** Same pulse train in helium or argon, then the same desorption run.
- **Cold work without a coil** (milled or pressed powder of the same lot). This tells whether a pulse does anything that ordinary deformation does not.

### 5.3 Knobs

| Parameter | Setting | Reason |
|---|---|---|
| Host | Pd, then Ni, with Cu baseline | §3 |
| Gas | H₂ first; D₂ as a paired column; inert control | In Pd, D₂ needs about 5 times the plateau pressure |
| Pressure | Pd: sweep through the plateau, below 1 atm. Ni: one fixed modest pressure | No threshold exists for Ni; pressure is a \(\sqrt{p}\) crossover |
| Temperature | Near ambient; a scan only as an Arrhenius measurement | Release is continuous in temperature |
| Powder size | Pd: a series from about 10 nm to above 100 nm | The published size dependence of the hydride transition lies at 15–50 nm and is the baseline |
| Defect state | Annealed and cold-worked lots of one chemistry | Trap population depends on defect history |
| Peak field | Below and above 0.23 T on Ni | Turns the magnetostrictive strain on and off |
| Pulse width, repetition, train length | 10–100 µs; 1, 10, 10², 10³ shots as separate cells | A dependence on shot count is a dependence on accumulated deformation or heat; the controls separate them |
| Plasma, current through the bed | Off | A confound for every readout; Phase 4 |

Not to optimize: neutron yield, excess heat, pulse energy, pressure, or fineness of powder.

---

## 6. Experimental matrix

Run down the list. A warm cell is not a reason to skip ahead.

**Phase 0 — Instrument.** Empty cell and Cu powder in inert gas with the full pulse train: *I*(t), *T*(t), pickup on every channel. Desorption blanks of each as-received powder. If the blanks are not reproducible, stop.

**Phase 1 — Reference state, no pulse.**

| Cell | Host | Gas | Measurement | Question |
|---|---|---|---|---|
| 1 | Pd, coarse | H₂ | Isotherm, lattice parameter | Does this lot reproduce 2.0 kPa and 0.68? |
| 2 | Pd, size series | H₂ | Isotherm | Does the lot reproduce the published narrowing of hysteresis with size? |
| 3 | Ni, annealed and cold-worked | H₂ soak | Desorption spectrum | What is the unpulsed trapped population of each lot? |
| 4 | Ni | Inert | Desorption spectrum | Blank |

**Phase 2 — Pulse as a factor.** Each row is run with the four controls of §5.2.

| Cell | Host | Gas | Pulse | Dependent variable |
|---|---|---|---|---|
| 5 | Pd | H₂, held inside the hysteresis loop | Train | Plateau pressures, hysteresis width and lattice parameter, before and after |
| 6 | Pd | H₂ | Train | Desorption peaks and areas against cell 1 |
| 7 | Ni | H₂ | Train, field above 0.23 T | Desorption peaks and areas against cell 3 |
| 8 | Ni | H₂ | Train, field below saturation | Same; separates field from magnetostrictive strain |
| 9 | Cu | H₂ | Train | Same; conductor baseline |

A positive result is a new or shifted desorption peak, or a shifted plateau or hysteresis width, that exceeds the scatter of repeats and is absent in the heat-matched and cold-work controls.

**Phase 3 — Hold and erase.** On any cell with a positive Phase 2 result: stop the coil, then repeat the readout after hours and after days. The hold test is whether the desorption peak or the hysteresis shift is still there with the coil dark. The erase test is whether an anneal removes it and a new pulse train restores it. Measure \(E_a\) of the new peak from the heating-rate shift and compare it with the trap energies of §2.

**Phase 4 — Other occupancy routes, as separate factors.** Current through the bed or a discharge; electrochemical loading. Electrochemical insertion is sourced for palladium (H/Pd 0.96 in a thin film against 0.68 from gas, HM §4.3). The wet cells of the earlier version are reduced to one question: does the Phase 2 result survive when hydrogen is supplied electrochemically. The preloaded nickel hydride cell is removed (§3). A preloaded palladium hydride is possible only in a hydrogen atmosphere above its desorption pressure.

**Phase 5 — Search.** Only after a state has been written, held and erased on command: a quiet neutron channel and the best calorimetry the cell allows, with columns H₂, D₂, inert; pulsed and unpulsed. A null here closes the nuclear question for this hardware. It does not undo a materials result from Phases 1–3.

---

## 7. Falsifiers

Written against the readouts of §5.1.

1. **Ni.** The desorption spectrum of pulsed nickel matches the heat-matched control and the cold-worked control in peak temperatures and areas, within the scatter of repeats. Then the pulse writes no trapped state that ordinary processing does not.
2. **Pd.** Plateau pressures, hysteresis width and lattice parameter after pulsing equal the unpulsed values of the same lot. Then the pulse does not act on the hydride transition.
3. **Hold.** Every difference is gone by the first readout after the coil is dark, or decays as the cell cools.
4. **Erase.** A difference exists but has the activation energy and annealing behaviour of the trapped populations of §2, and cold work reproduces it. Then it is ordinary trapping, and the hypothesis adds nothing to known metallurgy.
5. **Host pattern.** The same difference appears in Cu, or in nickel below the saturation field and above the Curie point alike. Then neither a hydride nor the magnetic state is involved.
6. **Size.** The size dependence found in pulsed palladium is the published unpulsed one.

Dropped from the earlier list, because standard physics already answers them: "annealed coarse Ni and nano Ni behave the same at the same H/M" (lattice H/M at fixed pressure and temperature is set by Sieverts' law, and fine powder differs from coarse in retention without any pulse); "Ni not special, Pd identical" (the hosts differ by four orders of magnitude in hydrogen content before any pulse).

A nuclear null after a positive materials result is not a falsifier of the materials result.

---

## 8. Status of the earlier version's predictions

| Earlier statement | Status | Basis |
|---|---|---|
| A grain below a blocking line cannot hold a pinned interstitial configuration | Contradicted as stated | Trap binding is per atom; no volume barrier is sourced (HM §4.6) |
| Hysteresis of the hydride transition narrows in small particles | Established, for Pd | HM §4.3; a crossover, measured without a pulse |
| Fine powder holds less | Established, for a different reason | Smaller specimens retain less hydrogen because the path to the surface is short (HM §4.3) |
| A peak field below the alignment field hides the magnetostriction | Established | The strain follows the magnetization and saturates (MS §4.5). Not a prediction |
| Nickel loads H and D; verify uptake by mass or pressure drop | Contradicted | §3 |
| A preloaded dry nickel hydride reproduces the gas-phase result | Contradicted | The hydride decomposes below about 3.4 kbar |
| Higher pressure opens the effect | Established as a crossover only | \(\sqrt{p}\); a factor of 3.9 from 20 to 300 bar |
| High temperature erases; cryogenic temperature freezes hops | Established | Arrhenius release and Arrhenius diffusion; no critical temperature |
| Gas enters an opened volume during the pulse | Contradicted for Ni | 2.3 nm in 100 µs |
| Magnetostrictive strain writes defects | Unsupported | Smallest strain in the cell; 4–5 % of yield when fully clamped |
| Pd is a weaker writer than Ni | Not testable as posed | The hosts differ in too many other ways (§4.2) |
| A signature that needs the coil on is heat | Kept as a criterion | §7, item 3 |
| Low pressure leaves opened volumes empty; annealed hosts are null; the anomaly lingers after the drive | Hypothesis | No source in the library |

---

## 9. The record

Berlinguette et al., *Nature* 570, 45 (2019), report a multi-institution programme to re-evaluate cold fusion (HM §4.3, "Anomalous-heat claims").

From the abstract ([PubMed record](https://pubmed.ncbi.nlm.nih.gov/31133686/)): the efforts "have yet to yield any evidence of such an effect". The same abstract says the work gave "new insights into highly hydrided metals and low-energy nuclear reactions" and that "there remains much interesting science to be done in this underexplored parameter space".

From a news account of the paper (secondary): three set-ups were tested. Palladium was loaded toward H/Pd 0.875, a level exceeded twice in several dozen tests. 420 samples of nickel powder heated in hydrogen showed no excess heat. Pulsed-plasma loading of palladium showed no enhanced tritium. The full paper was not opened.

The nickel-powder test is the closest published relative of the nickel column here, and it was null. This file therefore treats the anomaly claims as unconfirmed, and treats the configuration hypothesis as a materials question that can be answered without them.

---

## 10. Relation to the source notes, and status

| Source element | Fate here |
|---|---|
| Configuration dependence of reported anomalies | Kept as the hypothesis; given two candidate objects |
| Average loading necessary but insufficient | Kept for Pd as a statement to test; not applicable to Ni, which does not load |
| Defects, interfaces, cycling | Kept as the trap population, object (a) |
| Contained powder with an external pulsed coil | Kept as the instrument |
| Modular ¼″ Cu cell and ⅜″ coil form | Kept for shakedown. Schrader and HVAC fittings are not hydrogen service. Palladium work is done below one atmosphere |
| Ni first | Reversed: Pd first |
| Magnetostriction as the write | Withdrawn as an assumption; tested by the field and Curie controls |
| High-pressure cells (60–300 bar) | Dropped; no threshold exists for them to reach |
| Plasma, wet cells, electrolysis | Kept as Phase 4 factors |
| Neutrons and calorimetry | Kept as Phase 5 |
| Ordinary compression is insufficient for fusion | Kept; no nuclear process is asserted |

The other gate applications remain separate: this cell has no muon source ([muon-hydrogen-gate](muon-hydrogen-gate.md)) and no pyroelectric accelerator ([polar-beam-gate](polar-beam-gate.md)). The handbook relatives of this file are [hydrogen-embrittlement](hydrogen-embrittlement.md) and [hydride-storage](hydride-storage.md).

Next work, if any: Phase 0 on the existing hardware, then Phase 1 on one palladium lot and one nickel lot. Phase 1 uses no pulse and tests whether the instruments reproduce published values. Nothing later is interpretable without it.
