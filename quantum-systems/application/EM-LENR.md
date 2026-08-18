# Application: EM-LENR — Defect-Pinned Interstitial Latch

**Source problem:** configuration dependence of reported LENR / gas-loaded-metal anomalies.
**QSA role:** first end-to-end use of the effect library and the `effect → implication → design → requirement` analysis layer.
**Status:** Working application. Utility and internal-consistency test only. No nuclear process is asserted. **Not a tested protocol.**
**Updated:** 2026-08-17

> **Hazards (read [SAFETY.md](../SAFETY.md)).** H₂/D₂, fine metal powder, and pressure in one vessel are a fire, leak, and dust-explosion stack. kA-class pulses injure at arm’s length even at tens of volts. BeCu is named only for shops that already control beryllium; otherwise stay on copper. This file is a mapping, not a procedure. Do not scale inventory, pressure, or pulse energy in search of a nuclear signature. Do not skip to a neutron search.

**Credit.** The physical problem, the configuration hypothesis, and the experimental direction are Steven E. Jones’s. The notes that this file analyzes were developed in collaboration with the author of this repository. Electromagnetic cold-spray additive manufacturing (EM-CSAM) entered only as a related thought experiment — a railgun barrel as an incidental high-*dB/dt*, high-strain environment — not as the subject of this application. This document is QSA analysis of that work, not a claim of authorship of it.

This file is the live theory-of-operation and parameter document. The prior notes remain the historical record ([`../../em-csam/EM-CSAM-LENR.md`](../../em-csam/EM-CSAM-LENR.md)).

---

## 1. Scope and claim

Reported anomalous heat or nuclear signatures in Pd–D, Ni–H/D, and related systems are treated as **possibly real and not yet isolated**. The experimental record is consistent with a missing hardware variable, not with a well-defined energy-gate that sometimes opens at random.

**Claim of this application.** The unisolated object is a **defect-pinned latched order of the interstitial hydrogen / deuterium population** — the same machine class as [`anisotropy-latch`](../analysis/README.md) and [`exchange-pin`](../analysis/README.md), applied to occupancy and strain rather than to spin. Bulk loading ratio (H/M, D/M) is capacity, not the latch. A nuclear conversion, if it ever occurs, is a separate `energy-gate` that can open only inside a provisioned cell.

That claim is a mapping, not a demonstration. It is useful if it produces:

- a short list of knobs with a predicted direction of tune,
- a host split (Ni vs Pd vs non-absorbing ferromagnet) that the source notes did not have,
- collapse tests that look like blocking, not like bulk β-phase fraction,
- a clean hold-power test after the coil is dark.

If those tests fail, the mapping is wrong. Record that; do not patch it with a new nuclear story.

Language stays inside the library rules: constraints, resources, synchronization, failure thresholds, emergent output. No agency.

---

## 2. Why the LENR record sits on a latch, not on an average or a gate

Jones’s configuration hypothesis is kept. QSA names the machine.

| Persistent feature of the record | QSA reading | Library home |
|---|---|---|
| High H/M is required but not sufficient | Sample envelope is **capacity**. The cliff is a **cell volume**. | `ensemble-average` vs `anisotropy-latch` |
| Defects, interfaces, multilayers, cold work | Barrier matrix / pin, not uniform interstitial sites | `exchange-pin`, `magnetic-domains` (as partition analog) |
| Dynamic trajectories, cycling, moving fronts | Write / erase cycle | `ferromagnetic-hysteresis` |
| Clean, annealed, equilibrium hosts are usually null | Soft limit: barrier → 0 | hysteresis soft-limit |
| Extreme intermittency, even in one lab | Volume-and-time collapse: too-small a cell thermally erases on the observation window | `superparamagnetism` |
| Anomaly can linger after the drive | Zero continuous hold-power | latch / pin outputs |
| Bulk *T* and phase diagrams do not predict it | Pin collapse is a **blocking** temperature, not the host Curie or hydride phase line | `exchange-pin` (*T*<sub>B</sub> ≠ *T*<sub>C</sub>) |

Machines that do **not** own the missing variable:

- **`ensemble-average`.** H/M, resistance ratio, and lattice expansion are the averages already measured. They have no universal *N*-cliff. The anomaly, if real, is what happens when a latch or gap *replaces* that average.
- **`energy-gate` alone.** Isolated D–D / p–p conversion is a discrete gate. Ordinary lattice compression does not open it. An under-threshold gate cannot explain metallurgical history or intermittency.
- **`energy-gate` as [muon-catalyzed fusion](../library/muon-catalyzed-fusion.md).** The handbook hydrogen-isotope nuclear gate. It requires a muon. Collapse is missing muon / decay / sticking, not blocking of a defect cell. This apparatus has no muon source. Cosmic-ray flux does not track bake-out or cold work. Do not file that cycle as this cell (`predicted:muon-catalyzed-fusion:muon-free-cell-is-null`). Device reading: [muon-hydrogen-gate](muon-hydrogen-gate.md).
- **`energy-gate` as [pyroelectric fusion](../library/pyroelectric-fusion.md).** Ordinary beam-target D–D opened by a pyroelectric high-voltage engine. This apparatus has no pyroelectric accelerator. Do not file a pulsed-coil hydride as that crystal. Pyroelectric neutrons, when they exist, track a thermal ramp, not *τ<sub>μ</sub>* (`predicted:pyroelectric-fusion:muon-free-still-not-mucf`). Device reading: [polar-beam-gate](polar-beam-gate.md).
- **`energy-gate` as [deuteron photodisintegration](../library/deuteron-photodisintegration.md).** A 2.224 MeV *γ* unbinds *d* → *p*+*n*. That photon is not a muon catalyst (`predicted:deuteron-photodisintegration:photon-is-not-a-muon`). Do not irradiate this cell, and do not read a 2.45 MeV D–D line as photodisintegration.
- **Bulk `collective-screening` of the Pd electron gas.** Connected buffer and plasma clock of a uniform metal. Too spatially uniform to carry the defect / recipe dependence.
- **`gapped-condensate`.** No measured pairing gap, London *λ*, or Meissner of the hydride at these temperatures. Same category error as folding a dilute BEC into the charged condensate.

A collective mode of **clustered interstitials inside a defect cavity** is not in the library. It is a predicted sibling of `collective-screening`, not a substitute for isolating the latch. Isolate the latch first.

---

## 3. Theory of operation

### 3.1 The machine

Three nested hardware layers:

1. **Oscillator-grid (scribe).** The host ion lattice. Pulses, shocks, and magnetostrictive strain write defects, open transient volume, and then collapse or pin it. Owned by [`oscillator-grid`](../library/phonon-dispersion.md) / [`magnetostriction`](../library/magnetostriction.md) / [`elasticity`](../library/elasticity.md).
2. **Interstitial latch (the missing object).** A high-occupancy, defect- or interface-associated arrangement of H or D, held by a strain / surface / vacancy barrier at **zero continuous power**. Cell volume must sit above a blocking line (KV analog). Too small → thermal erasure on laboratory time. Too soft a matrix → no remanence (soft-limit analog).
3. **Pin (optional, sharpens the collapse).** A second structure — grain boundary, misfit interface, multilayer, vacancy cluster — whose collapse temperature is **not** the bulk hydride phase line. This is why `exchange-pin` was split from `anisotropy-latch`: *T*<sub>B</sub> of the pin is not *T*<sub>C</sub> of the parent.

A nuclear energy-gate, if present, is a **fourth** layer that only sees the interior of a provisioned cell. This application does not tune for that gate until the latch can be written and erased on command.

### 3.2 Write cycle

A useful pulse does four things in order. None of them is “compress the lattice until nuclei fuse.”

| Step | What happens | QSA clause |
|---|---|---|
| 1. Align / stress | In Ni: *B* aligns *M*; magnetostriction strains the grid. In any conductor: eddy currents and Lorentz body forces add a second, less specific stress. | `magnetostriction` requires ordered *M* **and** a deformable lattice. Pd has the lattice and not the ordered moment. |
| 2. Open | Local volumes, vacancies, and interfaces open or move. Gas chemical potential (pressure, *T*) drives H/D into those volumes. | Capacity: high average occupancy is the reservoir. |
| 3. Collapse / pin | The grid snaps back or the interface reconstructs. A high-occupancy cluster is left in a well. | Latch write. Energy is the loop area, not a hold-power. |
| 4. Hold or erase | If cell volume × barrier ≳ *kT* ln(*τ*/τ₀), the configuration persists after the coil is dark. If not, it is gone on the observation window. | Superparamagnetic analog. Hold-power test. |

Plasma (arc, glow, surface discharge) is a **parallel write channel**: ion injection and surface reconstruction. It is not required by the latch mapping. It is a confound for calorimetry. Early runs keep it off; later runs turn it on as its own factor.

### 3.3 Host split (load-bearing)

The source notes ranked Pd–D first on historical association. For **this** write channel the ranking inverts.

| Host | Magnetic latch | Magnetostrictive scribe | Interstitial capacity | Role in this apparatus |
|---|---|---|---|---|
| **Ni** | Yes (ferromagnet) | Yes (*λ*<sub>s</sub> ~ 10⁻⁵ class) | H and D both load | **Primary.** Pulse writes strain through a filed machine. |
| **Pd** | No (Pauli paramagnet) | No *M*-locked *λ* of this kind | Excellent D/H host | **Control for “is *B*→*λ* load-bearing?”** Historical Pd–D writes were electrochemical / gas-trajectory, not coil writes. |
| **Fe / low-alloy steel** | Yes | Yes | Poor H host at these *T*, *P* relative to Pd/Ni; embrittlement | **Strain without interstitial capacity** (near-null for the latch, not for heating). |
| **Cu** | No | No | Negligible | **Eddy / Joule baseline.** Cell wall is already Cu in the prototype. |

If Ni + H/D + pulse shows a configuration signature and Pd in the same coil does not, the magnetostrictive write is load-bearing. If both do, Lorentz / eddy / pressure cycling is doing the writing and the Ni advantage collapses. If a ferromagnetic non-absorber shows the same “anomaly,” the signal is mechanical or magnetic heating.

Fine powder is not automatically better. A grain below the blocking line cannot hold the latch (`predicted:exchange-bias:no-hex-below-kv`, `predicted:magnetostriction:no-static-lambda-when-unblocked`). There is a **window**: small enough for high interfacial area and for the pulse to work the whole grain; large enough that *KV* (or the interstitial analog) stays above the thermal-escape line on the measurement window.

### 3.4 Clocks

| Clock | Scale | Role |
|---|---|---|
| Coil pulse | µs–ms | Write envelope. Must be long enough for wall / dislocation motion and for gas to enter an opened volume; short enough that the event is a pulse, not a bake. |
| Acoustic transit of a grain | ns–µs for µm–mm particles | Grid response. |
| H/D hop / diffusion into a fresh defect | highly *T*- and path-dependent; can be the slow step | If hops are slower than the open interval, step 2 fails. Raise *T* or lengthen the pulse, or raise *P* (chemical potential). |
| Thermal escape of an under-volume cell | τ₀ exp(*KV*/*kT*), τ₀ ~ 10⁻¹¹ s class | Hold / erase. This is the intermittency clock. |
| Calorimeter / thermometer | seconds | Must not be mistaken for the write clock. Observation slower than equilibration reads *T*; that is the ensemble-average machine, not the latch. |

### 3.5 Failure envelope (predicted)

The latch mapping dies in ways that are **not** “the nuclear gate stayed closed”:

- *T* above a blocking / unpinning line → configuration gone, bulk hydride may remain.
- Grain / island / film below a volume cliff → no remanence of the configuration on lab time.
- Soft, well-annealed host → nothing to pin; pulse only heats.
- *B* below the write field on Ni → *M* not aligned → *λ* hidden (`magnetostriction` unaligned-*M* failure).
- *P* / chemical potential too low → opened volumes refill with vacancy, not with H/D.
- Pulse so slow or so hot that the host sinters or melts → grid destroyed; latch matrix gone. That is `coupled-grid-loss` (shear, crystal *κ*, and Mössbauer *f* fail together at *T*<sub>m</sub>), not a Curie / *T*<sub>λ</sub> / nuclear cliff.
- Pulse so fast and so small-opening that gas never enters → write of empty defects.

A nuclear-null in all of those collapse cells, **plus** a nuclear-null in the provisioned cell, is a failed application of the energy-gate layer, not a failed isolation of the latch. Keep those verdicts separate.

---

## 4. Apparatus (carried forward, inverted)

The EM-CSAM micro-railgun was the thought-experiment that suggested incidental high *dB/dt* and high strain rate. It is the wrong primary instrument for this problem: one write, powder leaves, calorimetry is hostile.

**Primary instrument:** contained powder, external pulsed coil, no net ejection. Cell and coil geometry follow the modular sketches in the source notes.

| Element | First article | Upgrade |
|---|---|---|
| Cell | ¼″ Cu HVAC tube, Schrader fill, flare or compression closure | Rated high-pressure copper-alloy cell only under a real vessel review. **BeCu only in a beryllium-controlled shop;** otherwise stay on Cu and prototype pressure. |
| Coil | ⅜″ OD form sliding over the cell, 12 AWG high-temp magnet wire, 30–80 turns, long solenoid first | Swappable forms; short concentrated coils later; never a closed eddy loop in the fixture |
| Drive | kA-class short-to-moderate pulses, current in the **coil only** | Reproducible pulse trains; single-shot and low-duty modes for diagnostics |
| Inventory | Grams or less of powder | Same. Small volume is a control advantage, not a compromise. |
| Gas | H₂ / D₂ / inert; prototype 20–50 bar | 60–80 bar on ½″ ACR Cu if that cell is used; 150–300 bar on the machined cell |

Plasma is minimized on the first matrix (external coil, no intentional current through the powder). A later matrix routes current through the bed on purpose.

Hydrogen + fine metal powder + pulsed current + pressure is an ordinary industrial hazard set. Small inventory reduces inventory at risk; it does not make the stack hobby-safe. Schrader / HVAC fittings are not hydrogen service. This file does not replace a safety review and is not a procedure.

---

## 5. Parameters: which way to turn them

Direction is relative to **isolating the latch**, not to maximizing a hoped-for nuclear yield. “Up” means increase that quantity.

### 5.1 Materials

| Parameter | First setting | Tune toward isolation | Tune away (usually a confound) |
|---|---|---|---|
| Host | **Ni** powder | Then Pd (magnetic-write control), then Fe/steel (strain, poor H capacity), then Cu powder if needed (eddy baseline) | Starting on Pd because the literature did |
| Gas | H₂ on Ni first (handling); D₂ as a paired column, not the first gas | Inert (He/Ar) on the same Ni as the empty-reservoir control | Mixing gases in one cell |
| Powder size | A **bimodal or stepped series**, not “as fine as possible.” Include a cut above ~50–100 nm and a cut that crosses into the 10–30 nm class | Walk size across a suspected blocking line at fixed *T*, *P*, pulse | Only nano, or only coarse filings |
| Defect budget | Cold-worked / high-surface Ni, not vacuum-annealed large crystals | One annealed control lot of the same chemistry | Unknown metallurgical history |
| Loading | Verify *some* uptake (mass, *P* drop, resistivity if practical) before calling a cell “loaded” | Cross a high-occupancy threshold, then **stop using H/M as the knob** | Chasing a magic H/M as the primary variable |

### 5.2 Thermodynamic state

| Parameter | First setting | Tune toward isolation | Collapse / null if the mapping is right |
|---|---|---|---|
| Pressure | Prototype ceiling (20–50 bar) for mechanical shakedown | **Up** into 60–80 then 150–300 bar to raise chemical potential for step 2 | Very low *P*: opened volumes stay empty |
| Temperature | Near ambient for first pulse maps | A **coarse *T* scan** looking for a blocking-like drop of any configuration signature, *not* for a fusion Q(T) | High *T*: thermal erase and sintering. Cryogenic: hops freeze, step 2 fails |
| Soak before pulsing | Long enough that bulk loading is not still ramping | Then compare “soak + pulse” vs “pulse from a freshly filled cell” | Treating soak time as equivalent to write cycles |

### 5.3 Pulse (the write waveform)

| Parameter | First setting | Tune toward isolation | Collapse / null if the mapping is right |
|---|---|---|---|
| Peak *B* / current | Tesla-class at the powder if the coil and driver can do it; otherwise the highest reproducible *B* that does not melt the cell | **Up** through Ni’s technical write / alignment field so *λ* is not hidden | Below alignment: magnetostrictive channel off |
| Pulse width | Start ~10–100 µs class (between acoustic transit and thermal soak) | Walk **both ways**. Too short: gas never enters. Too long: bake / sinter | DC or 50/60 Hz soak: not a write pulse |
| *dB/dt* | High enough for a real pulse, low enough to avoid intentional breakdown | A two-point split: “mechanical / magnetostrictive” vs “discharge-rich” | Uncontrolled arcing as the default |
| Repetition rate | Low duty first (thermal baseline visible between pulses) | Then trains. Look for **cycle-count** dependence (hysteresis), not just RMS power | High duty that only raises average *T* |
| Train length | 1, 10, 10², 10³ shots as separate cells or well-separated blocks | If the signature needs many cycles, that is a write-loop, not a one-shot gate | One heroic pulse as the only condition |
| After-period | Record for several thermal time constants after the coil is dark | **Hold-power test.** A latched configuration can persist; Joule heat decays | Cutting the record when the current stops |

### 5.4 Geometry and electrical path

| Parameter | First setting | Tune toward isolation | Tune away |
|---|---|---|---|
| Current path | **Coil only** | Later: intentional current-through-powder as the plasma-present matrix | Current through Schrader / end-cap by accident |
| Cell ID / fill | Shallow bed, not a rammed slug | Leave headspace so particles can move a little; a welded brick only heats | Tight packing that turns the bed into a single eddy slug |
| Coil length | Long solenoid (more uniform *B*) | Short coil later if a field gradient is wanted | Fixture that is a shorted turn |
| Plasma | Off (external coil, no glow) | On, as its own factor, after a low-plasma baseline exists | Plasma as the unnamed default |

### 5.5 What *not* to optimize first

- Neutron yield or “excess watts.” Those are search channels on an unisolated machine. Do not scale inventory, pressure, or pulse energy to chase them.
- Maximum pulse energy. Reproducible *B*(t) beats a bigger bang.
- Finest powder. That walks straight into the volume-collapse side of the latch.
- Highest pressure before the latch protocol exists. Pressure is a chemical-potential assist, not the effect.

---

## 6. Experimental matrix (isolation sequence)

Run **down** this list. Do not skip to nuclear search because a cell got warm.

### Phase 0 — Instrument, not physics

Empty cell and Cu-powder cell, inert gas, same pulse train. Map *I*(t), *T*(t), and any pickup on the neutron channel. This is the eddy / Joule / EMI baseline. If this already looks “anomalous,” stop.

### Phase 1 — Write channel exists

| Cell | Host | Gas | Pulse | Question |
|---|---|---|---|---|
| 1 | Ni | inert | coil, low plasma | Strain / heating only |
| 2 | Ni | H₂ | same | Interstitial reservoir added |
| 3 | Pd | H₂ or D₂ | same | Magnetic-write channel removed |
| 4 | Fe / steel | H₂ | same | Strain, poor H capacity |
| 5 | Ni | H₂ | **no pulse**, same *T*, *P*, time | Trajectory vs soak |

A configuration-level success is **not** heat. It is a difference that tracks host magnetism × gas uptake × pulse, and that is absent in 1, 3, 4, and 5 in the pattern the mapping requires (see §3.3). Mass, *P* drop, post-run diffraction / resistivity, and *T*(t) shape (including the after-period) are the first readouts.

### Phase 2 — Blocking and write-field cliffs

On Ni + H₂ (or D₂), hold pulse shape fixed and walk:

1. Powder size across a decade that includes tens of nm and hundreds of nm.
2. *T* from well below room temperature (if available) through a range that approaches sintering, looking for a **drop** of the Phase-1 signature, not a fusion-like rise.
3. Peak *B* from below Ni alignment to well above it.

A latch mapping wants a **cliff** in size and/or *T*, and a **threshold** in *B*. A smooth “more energy in, more heat out” curve is the ensemble-average / Joule machine.

### Phase 3 — Hold-power

On a cell that showed a Phase-2 cliff: run the write train, then **stop the coil** and keep recording. Compare to a Joule-matched inert cell.

- Signature dies with *I*²*R* → heating transient.
- Signature persists or relaxes on a longer, *T*-dependent clock → consistent with a written state.

### Phase 4 — Plasma as a factor

Repeat the winning Ni + gas + pulse cell with intentional current through the bed or a discharge-prone gap. If the Phase-2 cliffs vanish and only a hot plasma remains, the latch was never isolated; the discharge wrote a different (or no) configuration and destroyed calorimetry.

### Phase 5 — Search, not isolation

Only after a write/erase protocol exists: add a quiet neutron channel and the best calorimetry the small cell allows. Columns: H₂ vs D₂ vs inert, loaded vs unloaded, Ni vs Pd, pulse vs no-pulse, on-train vs after-period.

A nuclear-null here, with the latch isolated, is a result: the energy-gate did not open in this cell. It does not erase Phases 1–3.

A high-strain-rate impact, if used at all, is a **Phase-2 supplement** (single shock write), not Phase 0. It is not an EM-CSAM process step.

---

## 7. Diagnostics (what each one is for)

| Diagnostic | Machine it reads | Notes |
|---|---|---|
| Coil *I*(t), *V*(t) | Write waveform | Needed to know whether *B* crossed the alignment / write field |
| Cell *T*(t), after-period | Ensemble average + hold-power | Decay after *I* = 0 is the first latch-vs-Joule split |
| Gas *P*, mass, (if possible) resistance | Capacity / loading | Threshold condition, not the primary knob |
| Post-run XRD / PDF / microscopy | Grid and defect budget | Before/after, not only “did we get heat” |
| Grain-size distribution | Volume cliff | Must be known, not assumed from the vendor label |
| Neutron channel | Energy-gate search | Low background; EMI from the pulse is a first-class background |
| Calorimetry | Last, not first | Ordinary pulse energy will dominate any historical-rate nuclear term |

Local-structure probes *during* a claimed episode remain the right long-term measurement. They are not required to start Phase 1.

---

## 8. Predicted implications (conjecture, marked)

These are design-down claims. Several already sit on `design_implication` as `origin = predicted`. They are not extracted library facts.

- A Ni grain below the blocking line does not hold a static magnetostrictive strain or a pinned interstitial configuration on laboratory time.
- Peak *B* below Ni’s alignment / write field hides *λ* and should starve the magnetostrictive write even at high *P*.
- Pd in the same coil should be a weaker writer of this latch than Ni if *B*→*λ* is load-bearing.
- A configuration signature that needs the coil to stay on is heat, not a latch.
- A plasma-present cell can load surfaces and destroy the thermal baseline without ever provisioning the latch.
- If a nuclear gate opens at all, it tracks the **presence of the written cell**, not RMS pulse power. That is a Phase-5 claim only.
- A muon-free hydride is not the μCF cycle; pyroelectric 2.45 MeV neutrons (if anyone runs that crystal) do not die with *τ<sub>μ</sub>*; a 2.224 MeV *γ* is not a muon. None of those gates is this cell. Do not add a muon source, a pyroelectric crystal, or a *γ* beam to “open” it.

---

## 9. Falsifiers

The mapping is in trouble if, after Phases 0–3 are actually run:

1. No host × gas × pulse pattern appears that matches §3.3 (Ni not special, Pd identical, non-absorber identical).
2. The only “cliffs” are thermal: more pulse energy, more *T*, no size or *B*-threshold structure.
3. The after-period is always a pure cooling curve, and no *T*-dependent persistence shows up on any size cut.
4. Annealed coarse Ni and nano Ni behave the same at the same H/M and the same *B*(t).

Item 4 alone, done carefully, is a strong kill of the volume-threshold clause.

A nuclear-null after a successful isolation is **not** a falsifier of the latch. It is a closed energy-gate in this hardware.

---

## 10. Relation to the source notes

| Source element | Fate here |
|---|---|
| Configuration dependence of reported LENR | Kept; named as a latch / pin |
| Average loading as necessary but insufficient | Kept; filed as capacity |
| Dynamic trajectories, defects, interfaces | Kept; filed as write cycle and barrier matrix |
| EM-CSAM railgun as a related thought experiment | Acknowledged; not the subject. Optional shock writer only |
| Inverted contained powder + pulsed field | Promoted to primary |
| Modular ¼″ cell / ⅜″ coil / HVAC path | Kept; BeCu only if the shop already controls beryllium |
| Pd–D as first host | Inverted for this write channel; Ni first |
| Plasma optional | Kept; sequenced after a low-plasma baseline |
| Neutrons as first-line nuclear signature | Kept as Phase-5 search, not as isolation |
| Ordinary compression insufficient for fusion | Kept; restated as energy-gate not opening from grid strain alone |

---

## 11. Status

This is the first application of the QSA library to a live, unisolated problem. It does not add a nuclear effect to [`library/`](../library/INDEX.md). If Phases 1–3 produce a blocking-like cliff, that cliff is a candidate for a new library entry (interstitial-cluster latch / defect-cavity occupancy), not a reason to edit `energy-gate`.

Next work on this application, if any: run Phase 0 on the hardware that already exists, then a three-host, two-gas, pulse/no-pulse matrix small enough to finish.
