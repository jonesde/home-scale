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
review_depth: light
related:
  - ideal-gas-pressure
  - blackbody-spectrum
  - johnson-nyquist-noise
  - brownian-motion
  - electron-heat-capacity
  - melting
  - debye-cutoff
updated: 2026-11-11
---

# Thermal Equilibrium Temperature (Population Average)

### 4.1 Effect Name

Thermal equilibrium temperature (population average)

### 4.2 Macroscopic Observation

A macroscopic body left in contact with a larger body, or isolated long enough after a disturbance, presents one stable thermometer reading. Two bodies in thermal contact converge to the same reading, and a third body that matches the first also matches the second (the zeroth law). A sample with few independent contributors, or a probe that records faster than the sample exchanges energy, does not present that stable reading: successive observations scatter.

### 4.3 Established Quantitative Boundaries

- **Convention.** Boltzmann constant \(k = 1.380649\times 10^{-23}\,\mathrm{J\,K^{-1}}\), exact; the kelvin is defined through it [S1].
- **Computed here.** At 300 K, \(kT = 4.142\times 10^{-21}\,\mathrm{J} = 25.85\,\mathrm{meV}\).
- **Model (canonical ensemble).** Energy variance \(\langle(\Delta U)^2\rangle = kT^2C_V\); the fractional fluctuation scales as \(N^{-1/2}\) [S2].
- **Computed here.** For a monatomic ideal gas (\(U=\tfrac32NkT\), \(C_V=\tfrac32Nk\)) the fractional fluctuation is \(\sqrt{2/3N}\): 8 % at \(N=100\), 0.08 % at \(N=10^{6}\).
- **Measured.** Spontaneous temperature fluctuations have been measured: paramagnetic-salt thermometers coupled to 2 K reservoirs, read with superconducting magnetometers, gave noise spectra in very good agreement with the fluctuation–dissipation theorem [S3].
- **Measured.** Isolation from a bath does not forbid thermal local readings: in an isolated quantum many-body system imaged site by site, local observables thermalize while the full state stays pure [S7].
- **Model (kinetic theory).** Mean free path of air molecules at ambient pressure: 64–68 nm [S4].
- **Computed here.** Collision time in air, \(\lambda/\bar v\) with \(\lambda = 66\,\mathrm{nm}\) and the mean speed of \(\mathrm{N_2}\) at 293.15 K, \(\bar v=\sqrt{8kT/\pi m}=471\,\mathrm{m\,s^{-1}}\) (atomic weight of nitrogen 14.007 [S5]): \(1.4\times10^{-10}\,\mathrm{s}\).
- **Measured.** Electron–lattice energy exchange in a copper film: 1–4 ps, increasing with laser fluence [S6]. Exchange times are specific to the medium; none is a universal constant.

**Data confidence:** High for \(k\), the \(kT\) conversions and the \(N^{-1/2}\) scaling. Medium for the exchange times: the air mean free path rests on a tertiary range and the crystal figure is one metal at one set of conditions. The first version's "picoseconds to nanoseconds" for crystals was not sourced beyond the copper value.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Equipartition: mean energy \(\tfrac12kT\) per quadratic term in the energy [S8].
- Boltzmann factor for level occupation at equilibrium: \(p_i \propto e^{-E_i/kT}\) [S8].
- Canonical energy fluctuation [S2]:

  \[
  \frac{\sqrt{\langle(\Delta U)^2\rangle}}{U} = \frac{\sqrt{kT^2C_V}}{U} \sim N^{-1/2}
  \]

- Zeroth law: once A has stopped exchanging net energy with B, and B with C, thermometers coupled to A and to C report the same \(T\).

These relations describe the stable average. They fix no minimum \(N\). \(k\) is a defined conversion between energy and the kelvin, not a measured threshold.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A large population of contributors sharing energy-exchange channels. The scale is statistical: the output is a stable average, and its scatter falls as \(1/\sqrt{N}\). No node count marks a switch. What counts as enough \(N\) is set by the stability required of the reading.

- **Clock rate / latency.** The equilibration window of the population: collision time in a gas (\(10^{-10}\,\mathrm{s}\) in air), electron–lattice exchange in a metal (picoseconds in copper), or radiative exchange ([stefan-boltzmann](stefan-boltzmann.md)). Observation faster than the window returns incomplete averages.

- **Energy barriers or thresholds.** No latch holds \(T\). The resource is exchange among contributors. Barriers elsewhere in the library (Curie point, superconducting gap, melting) replace the population being averaged; they do not produce \(T\).

- **Dominant failure modes.**
  - **Crossover** — population: fractional scatter \(\sim N^{-1/2}\) (\(\sqrt{2/3N}\) for a monatomic gas); the reading degrades continuously as \(N\) falls. The cut is whatever stability the instrument needs.
  - **Crossover** — temporal: a reading taken inside the exchange window approaches the equilibrium value on that time scale (\(10^{-10}\,\mathrm{s}\) in air; 1–4 ps electron–lattice in copper).
  - **Threshold** — isolation: with no exchange channel two bodies do not converge.
  - **Threshold** — replacement of the ensemble: a phase transition (superconducting gap, magnetic order, melting) changes which population is averaged.

- **Emergent constant or stable output.** One shared number \(T\), and the conversion \(kT\) between it and an energy.

### 4.6 Internal Consistency Notes

The failure class is the family definition: too few contributors, or a clock faster than the averaging window. Both are continuous.

Sourcing changed little in the numbers: \(kT\) is 25.85 meV (was 25.9), the collision time is now computed, and the crystal exchange range was narrowed to the one opened measurement. Two facts were added that bear on the mapping. Temperature fluctuations of the predicted size have been measured, so the \(N^{-1/2}\) scatter is an observed quantity. And an isolated quantum system has been seen to thermalize locally with no external bath, so a closed system is not by itself excluded from giving a thermal reading; the size of that system was not read here.

The mapping does not close on a hardware number. QSA takes the \(N^{-1/2}\) scatter and the measured exchange times as buffer and clock. It does not derive \(k\) or a minimum \(N\). The same gap recurs on every entry in this family.

\(k\) is defined in SI. Treating it as an extracted machine constant would over-claim.

Contrast cases: [melting](melting.md) is a lattice threshold; [superconductivity](superconductivity.md) and the [magnet latch](permanent-magnet-latch.md) replace the thermal average with a gapped or barrier-protected state.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the two crossovers (under-populated average, observation inside the exchange window) are established; the mapping supplies no single buffer size and no derived \(k\), which is inherent to a statistical hardware scale.

## Related entries

- [Ideal-gas pressure](ideal-gas-pressure.md) — wall force as another averaged readout
- [Blackbody spectrum](blackbody-spectrum.md) — spectral readout of \(T\)
- [Johnson–Nyquist noise](johnson-nyquist-noise.md) — electrical readout of the same average
- [Brownian motion](brownian-motion.md) — visible incomplete average of molecular impacts
- [Electron heat capacity](electron-heat-capacity.md) — the electronic thermal population
- [Melting](melting.md) — a lattice threshold; a different family
- [Debye cutoff](debye-cutoff.md) — finite mode count behind the lattice heat capacity

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST, CODATA 2022 recommended values: Boltzmann constant](https://physics.nist.gov/cgi-bin/cuu/Value?k) | full-text | k = 1.380649e-23 J/K, exact. |
| S2 | [Kaufman, statistical mechanics lecture notes, part 2, Cleveland State University](https://academic.csuohio.edu/kaufman-miron/wp-content/uploads/sites/60/2023/02/lecturenotes_part2.pdf) | full-text | Energy variance kT²C_V; fractional fluctuation scaling as N^(-1/2); ideal-gas inputs. Lecture notes, secondary. |
| S3 | [Chui, Swanson, Adriaans, Nissen and Lipa, *Phys. Rev. Lett.* 69, 3005 (1992)](https://doi.org/10.1103/PhysRevLett.69.3005) | abstract | First quantitative measurement of spontaneous temperature fluctuations; agreement with the fluctuation–dissipation theorem. |
| S4 | [Wikipedia, "Mean free path"](https://en.wikipedia.org/wiki/Mean_free_path) | full-text | Tertiary: 64–68 nm for air at ambient pressure, citing Jennings, *J. Aerosol Sci.* 19, 159 (1988), which was not opened. |
| S5 | [NIST, Atomic Weights and Isotopic Compositions: nitrogen](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=N) | full-text | Standard atomic weight of nitrogen, 14.00643–14.00728. |
| S6 | [Elsayed-Ali, Norris, Pessot and Mourou, *Phys. Rev. Lett.* 58, 1212 (1987)](https://doi.org/10.1103/PhysRevLett.58.1212) | abstract | Electron–phonon energy transfer in copper films, 1–4 ps. |
| S7 | [Kaufman et al., "Quantum thermalization through entanglement in an isolated many-body system", arXiv:1603.04409 (*Science* 353, 794)](https://arxiv.org/abs/1603.04409) | abstract | Local thermalization in a small isolated quantum system whose full state stays pure. |
| S8 | [Merhav, "Statistical Physics: a Short Course for Electrical Engineering Students", arXiv:1307.5137](https://arxiv.org/abs/1307.5137) | full-text | Equipartition theorem and Boltzmann distribution. Lecture notes, secondary. |
