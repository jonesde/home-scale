---
id: debye-cutoff
title: Debye Cutoff (Finite-Mode Clock Ceiling)
status: formal
family: lattice-modes
constraints:
  - clock-latency
  - mechanical-lattice
confidence_data: high
confidence_mapping: high
review_depth: light
related:
  - phonon-dispersion
  - speed-of-sound
  - thermal-conductivity-phonon
  - melting
  - electron-heat-capacity
  - thermal-equilibrium-temperature
updated: 2026-11-11
---

# Debye Cutoff (Finite-Mode Clock Ceiling)

### 4.1 Effect Name

Debye cutoff (finite-mode clock ceiling)

### 4.2 Macroscopic Observation

A crystal of \(N\) atoms has a finite number of lattice vibrations. The heat capacity of an insulator rises as \(T^3\) at low temperature and levels off near \(3k\) per atom once \(T\) is well above a material-typical Debye temperature \(\Theta_D\). Lead is on that plateau at room temperature; diamond is far below it. Once every mode is thermally occupied, further heating adds no lattice-mode heat capacity.

### 4.3 Established Quantitative Boundaries

- **Model (harmonic lattice).** \(N\) atoms give exactly \(3N\) normal modes. The count is finite, unlike the modes of the electromagnetic field in a cavity [S1].
- **Measured.** At room temperature the heat capacity of most solids is about \(3k\) per atom (Dulong–Petit); at low temperature it falls as \(C_V=\alpha T^3+\gamma T\), with \(\gamma=0\) for insulators such as potassium chloride and the linear term in metals coming from the conduction electrons [S1].
- **Convention.** Debye's cutoff \(\omega_D\) is defined by requiring a continuous density of states to hold \(3N\) modes; \(\Theta_D=\hbar\omega_D/k\) [S1].
- **Model (Debye fit).** Lead: \(\Theta_D=105\) K in the low-temperature limit and 87 K at 298 K [S2]. Silicon 640 K [S3]. Diamond 1860 K [S4]. The value depends on the temperature and method of the fit.
- **Computed here.** Debye frequency \(k\Theta_D/h\): lead 2.2 THz (105 K), silicon 13.3 THz, diamond 38.8 THz.
- **Measured.** Heat capacity near room temperature: lead \(26.84\,\mathrm{J\,mol^{-1}K^{-1}}\) at 298.15 K [S2]; diamond \(0.52\,\mathrm{J\,g^{-1}K^{-1}}\) [S4]; silicon \(0.7\,\mathrm{J\,g^{-1}K^{-1}}\) [S3].
- **Computed here.** As a fraction of the Dulong–Petit value (\(3R=24.94\,\mathrm{J\,mol^{-1}K^{-1}}\), or \(3k\) per atom): lead 1.08, silicon 0.79, diamond 0.25. Silicon and diamond use the density and atom density on the same pages (\(2.329\,\mathrm{g\,cm^{-3}}\), \(5\times10^{22}\,\mathrm{cm^{-3}}\); \(3.515\,\mathrm{g\,cm^{-3}}\), \(1.764\times10^{23}\,\mathrm{cm^{-3}}\)) [S3][S4]. The lead figure is measured at constant pressure; the Dulong–Petit value is at constant volume.
- **Measured.** The Debye frequency is not the top of the real spectrum. The measured zone-centre optical modes of silicon (15.5 THz) and diamond (39.9 THz) lie above their Debye frequencies [S3][S4].
- **Measured.** Lead melts at 600.612 K [S2].
- **Computed here.** That is 5.7 times its low-temperature Debye temperature.

**Data confidence:** High for the \(3N\) count and the two heat-capacity limits. Medium for any single \(\Theta_D\): the lead figures come from a tertiary compilation and differ by 17 % between the 0 K and 298 K fits; the diamond value is the one opened here (other compilations quote higher values, not opened).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Debye wavevector for an isotropic, linear spectrum holding \(3N\) states:

  \[
  q_D = \bigl(6\pi^2 n\bigr)^{1/3}, \qquad \omega_D = v_s q_D, \qquad \Theta_D = \frac{\hbar\omega_D}{k}
  \]

  with \(n=N/V\) and \(v_s\) an average long-wave speed ([speed-of-sound](speed-of-sound.md)).
- Debye heat capacity [S1]:

  \[
  C_V = 9Nk\left(\frac{T}{\Theta_D}\right)^3\int_0^{\Theta_D/T}\frac{x^4 e^x}{(e^x-1)^2}\,dx
  \]

  Low \(T\): \(C_V = \frac{12\pi^4}{5} Nk (T/\Theta_D)^3\). High \(T\): \(C_V \to 3Nk\).

The formula does not generate the real \(\omega(\mathbf{q})\); the measured spectrum is in [phonon-dispersion](phonon-dispersion.md).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The ceiling exists because the node count is finite. A macroscopic crystal still has a highest mechanical frequency; a molecule or cluster has a discrete vibrational set. The Debye interpolation needs a 3-D lattice large enough that mode counting can be replaced by an integral.

- **Clock rate / latency.** \(\omega_D\) is the fitted clock ceiling of the ion grid: 2.2 THz for lead, 38.8 THz for diamond. Thermal occupation of the last modes needs \(kT\sim k\Theta_D\). Below that only a \(T^3\)-growing share of the \(3N\) modes is in play; above it the spectrum is fully occupied.

- **Energy barriers or thresholds.** No latched barrier. \(\hbar\omega_D\) is a spectral edge, not an activation energy that protects a state.

- **Dominant failure modes.**
  - **Threshold** — mode count: beyond the \(3N\)-th mode there is no lattice mode to occupy. The edge in frequency is the measured top branch; \(\omega_D\) approximates it and lies below it in silicon and diamond.
  - **Crossover** — thermal occupation: the heat capacity approaches \(3Nk\) continuously along the Debye function, with scale \(\Theta_D\). No temperature marks a switch.
  - **Threshold** — hardware: melting ends the crystalline modes ([melting](melting.md)); it is unrelated to \(\Theta_D\) (lead melts at \(5.7\,\Theta_D\)).
  - **Crossover** — counting: as \(N\) falls the density of states breaks into discrete lines; no scale filed here.
  - **Crossover** — approximation: with optical branches or anisotropy a single \(\omega_D\) is a fit parameter that moves with temperature (lead: 105 K to 87 K).

- **Emergent constant or stable output.** A material-typical \(\Theta_D\) and the two heat-capacity limits it organizes: \(T^3\) at low \(T\), \(3Nk\) at high \(T\).

### 4.6 Internal Consistency Notes

Finite \(N\) gives finite modes, so a highest lattice clock is unavoidable. Placing that ceiling at one spherical \(\omega_D\) is an interpolation; the measured ceiling is the top branch in [phonon-dispersion](phonon-dispersion.md). QSA takes \(\Theta_D\) as fitted and does not derive it from a node rule.

Sourcing changed the diamond figure from "about 2000 K" to the 1860 K that was opened, added the temperature dependence of the lead value, and added the comparison showing measured modes above the Debye frequency. The statement "no oscillator above \(\omega_D\)" is therefore true of the Debye model and false of the real crystals checked; the \(3N\) count is the part that holds.

\(\Theta_D\) is not a melting temperature. Lead is on the classical plateau at 300 K and stays solid to 600.6 K.

The insulator \(T^3\) law and a metal's extra \(\gamma T\) term are consistent once electrons and lattice are counted as separate populations ([electron-heat-capacity](electron-heat-capacity.md)).

### 4.7 Overall Confidence in the QSA Mapping

**High** — the \(3N\) count and the measured \(T^3\) and Dulong–Petit limits translate directly into a finite-mode clock specification. The gap is the Debye sphere against the real spectrum, not the existence of a ceiling.

## Related entries

- [phonon-dispersion](phonon-dispersion.md) — measured \(\omega(\mathbf{q})\) and the real top of the spectrum
- [speed-of-sound](speed-of-sound.md) — the long-wave slope Debye extends to \(q_D\)
- [thermal-conductivity-phonon](thermal-conductivity-phonon.md) — uses the same heat capacity and speed
- [melting](melting.md) — destruction of the crystal; a different threshold
- [electron-heat-capacity](electron-heat-capacity.md) — the electronic \(\gamma T\) term
- [thermal-equilibrium-temperature](thermal-equilibrium-temperature.md) — the \(T\) that occupies these modes

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Merhav, "Statistical Physics: a Short Course for Electrical Engineering Students", arXiv:1307.5137, ch. 7](https://arxiv.org/abs/1307.5137) | full-text | Exactly 3N modes; Dulong–Petit and the low-temperature T³ plus γT law; Debye's cutoff, Debye temperature and heat-capacity function. Lecture notes, secondary. |
| S2 | [KnowledgeDoor, Elements Handbook, lead](https://knowledgedoor.com/2/elements_handbook/lead.html) | full-text | Tertiary compilation: lead Debye temperature 105 K (0 K limit) and 87 K (298 K), molar heat capacity 26.84 J/(mol K), melting point 600.612 K. |
| S3 | [Ioffe Institute, NSM Archive, Silicon: basic parameters (with the thermal and mechanical pages)](http://www.ioffe.ru/SVA/NSM/Semicond/Si/basic.html) | full-text | Si Debye temperature 640 K, specific heat 0.7 J/g/K, zone-centre optical frequency 15.5 THz. Secondary. |
| S4 | [Ioffe Institute, NSM Archive, Diamond: basic parameters (with the thermal and mechanical pages)](http://www.ioffe.ru/SVA/NSM/Semicond/Diamond/basic.html) | full-text | Diamond Debye temperature 1860 K, specific heat 0.52 J/g/K, zone-centre optical frequency 39.9 THz. Secondary. |
