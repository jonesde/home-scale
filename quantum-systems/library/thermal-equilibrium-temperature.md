---
id: thermal-equilibrium-temperature
title: Thermal Equilibrium Temperature (Population Average)
status: formal
family: ensemble-averages
constraints:
  - thermal
  - clock-latency
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
related:
  - ideal-gas-pressure
  - blackbody-spectrum
  - johnson-nyquist-noise
  - brownian-motion
  - electron-heat-capacity
  - melting
  - debye-cutoff
updated: 2026-08-17
---

# Thermal Equilibrium Temperature (Population Average)

### 4.1 Effect Name

Thermal equilibrium temperature (population average)

### 4.2 Macroscopic Observation

A macroscopic body left in contact with a larger body, or isolated long enough after internal disturbances have died, presents a single, stable thermometer reading. Two bodies placed in thermal contact converge to the same reading. A third body that matches the first also matches the second — the operational content of the zeroth law. The reading does not depend on which contact thermometer is used once each instrument has itself equilibrated. A sample with only a handful of independent contributors, or a probe that records faster than the sample can exchange energy, does not present that stable reading: successive observations scatter.

### 4.3 Established Quantitative Boundaries

- Boltzmann constant (SI, defined): \(k = 1.380649\times 10^{-23}\,\mathrm{J\,K^{-1}}\). After the 2019 redefinition the kelvin is realized through this fixed \(k\).
- Thermal energy at \(300\,\mathrm{K}\): \(kT \approx 4.14\times 10^{-21}\,\mathrm{J} \approx 25.9\,\mathrm{meV}\).
- Relative size of energy (or inferred-\(T\)) fluctuations of a finite population scales as \(N^{-1/2}\) in the usual ensemble formulae. There is no single universal \(N\) at which a thermometer starts working. Laboratory gases, liquids, and solids sit at \(N\) so large that the scatter is lost in instrument noise; clusters, single-electron devices, and few-ion traps do not.
- Local equilibration clocks are medium-specific and are not a universal constant. In air at standard density the molecular mean free path is of order \(65\,\mathrm{nm}\) and the time between collisions is of order \(10^{-10}\,\mathrm{s}\). In ordinary crystals phonon–phonon and electron–phonon exchange run from picoseconds to nanoseconds. Radiative exchange between macroscopic surfaces is much slower (set by the [Stefan–Boltzmann](stefan-boltzmann.md) current and the heat capacity).
- A reading taken inside the exchange window, or on a subsystem that is not exchanging, is not the equilibrium \(T\).

**Data confidence:** High — \(k\) is defined; \(kT\) conversions are arithmetic; the \(N^{-1/2}\) scatter and the existence of a finite equilibration window are multiply reproduced. The numerical value of that window is medium for any one sample and geometry.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Equipartition for a quadratic term in the energy: mean energy \(\frac{1}{2}kT\) per such term. This is an envelope for the averaged output, not a statement about one node.
- Boltzmann factor for level occupation in a population at equilibrium:

  \[
  p_i \propto e^{-E_i/kT}
  \]

- Relative energy fluctuation of a finite population (canonical envelope):

  \[
  \frac{\sigma_E}{\langle E\rangle} \sim N^{-1/2}
  \]

- Zeroth-law operational statement: once A has stopped exchanging net energy with B, and B with C, a thermometer coupled to A and one coupled to C report the same \(T\).

These formulae describe the stable average. They do not identify a primitive node clock, and they do not fix a minimum \(N\). \(k\) is a defined conversion between energy and the kelvin; it is not a measured cliff.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A large population of independent contributors sharing energy-exchange channels. The hardware scale is statistical: the macro effect is a stable average, not a single-node property. There is no universal node-count cliff analogous to the 10–20 nm mirror stack or the \(KV\sim 25\,kT\) magnet grain. Collapse is gradual in \(1/\sqrt{N}\). What counts as enough \(N\) is set by the required stability of the reading against the instrument, not by a material constant.

- **Clock rate / latency.** The relevant clock is the equilibration window of the population under study — collision time, phonon/electron exchange time, or radiative time, depending on the medium and the coupling. Observation faster than that window returns a sequence of incomplete averages, not \(T\). Relative to any mechanical or human clock, ordinary condensed samples have already finished.

- **Energy barriers or thresholds.** No latch holds \(T\). The operating resource is exchange among contributors, not a barrier that protects a written state. Barriers elsewhere in the library (Curie point, superconducting gap, melting) destroy or replace this average; they are not the resource that produces \(T\).

- **Dominant failure modes.**
  - Population: too few independent contributors → scatter dominates the mean → no stable thermometer reading.
  - Temporal: observation or drive faster than the exchange window → the population has not finished averaging → the reading is not \(T\).
  - Isolation: no exchange channel (no collisions, no radiation, no contact) → two bodies do not converge.
  - Replacement of the ensemble: a gap or latch opens (superconducting gap, magnetic order, melting) and the original contributing population is no longer the one being averaged.

- **Emergent constant or stable output.** A single shared number \(T\), and with it the conversion \(kT\) between that number and an energy scale, as the averaged output of the population.

### 4.6 Internal Consistency Notes

The failure class is the family definition: too few contributors, or a clock faster than the averaging window. That matches the taxonomy and matches what a thermometer actually does.

The mapping does not close on a hardware number. QSA currently *takes* the observed \(N^{-1/2}\) scatter and the measured equilibration time as the buffer and clock specifications. It does not derive \(k\), or a minimum \(N\), from node rules. That is a gap, not a contradiction, and it is the same gap that will reappear on every other entry in this family.

\(k\) being defined in SI is a metrological fact, not a QSA result. Treating the defined \(k\) as if it were an extracted machine constant would over-claim.

Contrast cases sit in other families: [melting](melting.md) is a lattice-mode collapse at a thermal threshold; [superconductivity](superconductivity.md) and the [magnet latch](permanent-magnet-latch.md) replace the unlocked thermal average with a gapped or barrier-protected state. Those entries own the replacement; this one owns the average that they replace.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the collapse class (under-populated average, or observation inside the exchange window) is well established and fits the family; the mapping does not supply a single buffer size or a derived \(k\), and that limit is inherent to a statistical hardware scale.

## Related entries

- [Ideal-gas pressure](ideal-gas-pressure.md) — wall force as another averaged readout of the same thermal population
- [Blackbody spectrum](blackbody-spectrum.md) — spectral readout of \(T\)
- [Johnson–Nyquist noise](johnson-nyquist-noise.md) — electrical readout of the same average
- [Brownian motion](brownian-motion.md) — visible incomplete average of molecular impacts
- [Electron heat capacity](electron-heat-capacity.md) — Fermi-surface slice of a thermal electronic population
- [Melting](melting.md) — lattice-mode collapse at a thermal threshold; a different family
- [Debye cutoff](debye-cutoff.md) — finite mode count that shapes the phonon share of the heat capacity
