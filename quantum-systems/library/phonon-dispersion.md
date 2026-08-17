---
id: phonon-dispersion
title: Phonon Dispersion (Lattice Allowed-Clock Map)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - clock-latency
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
related:
  - speed-of-sound
  - debye-cutoff
  - melting
  - thermal-conductivity-phonon
  - elasticity
  - thermal-expansion
  - piezoelectricity
updated: 2026-08-17
---

# Phonon Dispersion (Lattice Allowed-Clock Map)

### 4.1 Effect Name

Phonon dispersion (lattice allowed-clock map)

### 4.2 Macroscopic Observation

A crystal does not support mechanical oscillations at arbitrary frequency and wavelength. Inelastic neutron and X-ray scattering return discrete energy-loss peaks at \(\omega(\mathbf{q})\) along each branch; Raman and infrared spectroscopy read the long-wavelength optical frequencies; a struck solid rings at sound speeds set by the acoustic slope. Driving above the highest lattice frequency produces no additional phonon mode. Softening of a branch to \(\omega \to 0\) accompanies a structural transition; loss of Bragg order ends the map.

### 4.3 Established Quantitative Boundaries

- Acoustic branches: \(\omega(\mathbf{q})\to 0\) as \(\mathbf{q}\to 0\), with slope equal to a measured sound speed. Handbook long-wavelength speeds: Al longitudinal \(\approx 6.4\,\mathrm{km\,s^{-1}}\); Si \([100]\) longitudinal \(\approx 8.4\,\mathrm{km\,s^{-1}}\). Transverse speeds are lower. There is no acoustic shear wave in a liquid; that collapse is owned with [speed-of-sound](speed-of-sound.md).
- Optical branches (crystals with more than one atom per primitive cell): finite \(\omega\) at the zone centre. Zone-centre optical frequencies: Si \(15.5\,\mathrm{THz}\) (\(520\,\mathrm{cm^{-1}}\), the room-temperature Raman line); diamond \(40\,\mathrm{THz}\) (\(1332\,\mathrm{cm^{-1}}\)). Polar crystals split TO and LO at \(\mathbf{q}\approx 0\) and reflect in the reststrahlen band between them.
- Zone-boundary cutoff: \(\mathbf{q}\) stops at the Brillouin-zone edge (\(\sim \pi/a\), of order \(10^{10}\,\mathrm{m^{-1}}\)). Lattice constants: Si \(5.43\,\mathrm{\AA}\); Al \(4.05\,\mathrm{\AA}\); diamond \(3.57\,\mathrm{\AA}\). Maximum phonon frequencies sit in the few-to-tens-of-THz class (Al’s spectrum ends near \(10\,\mathrm{THz}\); diamond’s near \(40\,\mathrm{THz}\)). A drive above that ceiling is not a lattice mode.
- Mode count is finite: three acoustic branches plus \(3N-3\) optical branches for \(N\) atoms in the primitive cell. The Debye frequency \(\omega_D = k\Theta_D/\hbar\) is a continuum stand-in for that ceiling (Al \(\Theta_D \approx 428\,\mathrm{K}\); Si \(\approx 645\,\mathrm{K}\); Pb \(\approx 105\,\mathrm{K}\); diamond \(\approx 2200\,\mathrm{K}\)) and is filed properly as [debye-cutoff](debye-cutoff.md).
- Soft modes: a restoring branch can fall toward \(\omega = 0\) as a structural transition is approached (classic displacive ferroelectrics). An imaginary harmonic \(\omega\) is the statement that the current lattice is mechanically unstable. [Melting](melting.md) is the point at which Bragg order — the grid that carries the map — is lost.

**Data confidence:** High — \(\omega(\mathbf{q})\) from inelastic neutron and X-ray scattering, zone-centre Raman/IR frequencies, and ultrasonic sound speeds are multiply reproduced. Soft-mode trajectories are high as a class and medium for any one crystal’s exact \(T\)-axis.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Harmonic lattice: \(\omega_s(\mathbf{q})\) is the measured eigenfrequency of branch \(s\) at wavevector \(\mathbf{q}\) in the first Brillouin zone. Outside the zone the same frequencies repeat (reduced-zone scheme); they are not new clocks.

- Acoustic long-wavelength limit:

  \[
  \omega_{\mathrm{ac}}(\mathbf{q}) \approx v_s(\hat{\mathbf{q}})\,|\mathbf{q}|, \qquad |\mathbf{q}|\to 0
  \]

  with \(v_s = \sqrt{C/\rho}\) matching the continuum elastic speeds ([elasticity](elasticity.md), [speed-of-sound](speed-of-sound.md)).

- Optical zone-centre example (Si Raman):

  \[
  \nu_{\Gamma}(\mathrm{Si}) \approx 15.5\,\mathrm{THz}
  \]

- Group velocity \(\mathbf{v}_g = \nabla_{\mathbf{q}}\omega\) is the measured transport speed of a packet; it vanishes at many zone-boundary extrema. Mean-free-path collapse under Umklapp and defect scattering is owned by [thermal-conductivity-phonon](thermal-conductivity-phonon.md).

Anharmonic shifts and lifetimes appear as small \(T\)-dependent moves of the same peaks, not as a second map.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The crystalline lattice. One primitive cell is the repeating mechanical unit (and is already enough to define an optical zone-centre clock). A well-defined \(\mathbf{q}\) is a phase relation across many cells; the map as a *spectrum* is an extended-crystal object. There is no single nanometre cliff analogous to the 10–20 nm mirror. Amorphous solids retain a vibrational density of states but lose sharp \(\omega(\mathbf{q})\) branches; that is loss of the map, not a measured buffer thickness.

- **Clock rate / latency.** \(\omega_s(\mathbf{q})\) *is* the allowed-clock table. Acoustic clocks run from zero up to the zone-boundary frequency of that branch; optical clocks sit at THz. Nothing in the lattice oscillates as a phonon faster than the highest measured branch. Sound arrival times on laboratory samples are just the long-wave edge of the same table.

- **Energy barriers or thresholds.** Not a latch. The harmonic restoring energy of a mode is \(\tfrac{1}{2}\hbar\omega(2n+1)\) (or \(\tfrac{1}{2}ku^2\) classically); that is an oscillator budget, not an activation barrier that holds a directional state. Softening to \(\omega\to 0\) is loss of that restoring constraint along one coordinate.

- **Dominant failure modes.**
  - Clock ceiling: drive frequency above the highest branch → no additional lattice mode (reststrahlen / neutron cutoff).
  - Zone edge: \(\mathbf{q}\) outside the first zone is an alias, not a new clock.
  - Soft mode: \(\omega\to 0\) → that restoring channel closes; a structural transition follows.
  - Grid loss: melting or amorphization → Bragg order gone → the discrete \(\omega(\mathbf{q})\) map ends.
  - Scattering: finite lifetime / mean free path blurs a peak but does not erase the branch until the lattice itself fails.

- **Emergent constant or stable output.** The measured surface \(\omega_s(\mathbf{q})\), its long-wave speeds \(v_s\), and its zone-centre optical frequencies, for as long as the crystal remains ordered.

### 4.6 Internal Consistency Notes

Treating \(\omega(\mathbf{q})\) as the lattice’s allowed-clock map is internally consistent and almost definitional: the experiment *is* the table of clocks the grid will run. Acoustic slope matching macroscopic sound speed, optical Raman lines matching the \(\mathbf{q}=0\) intercept, and the absence of modes past the zone-boundary maximum all sit where that reading says they should.

The mapping is incomplete as a QSA *collapse* specification. Phonon dispersion is a spectrum, not a binary macro with one hardware number. The sharp on/off envelopes live in related entries: [speed-of-sound](speed-of-sound.md) (long-wave slope; shear dies in a liquid), [debye-cutoff](debye-cutoff.md) (finite node count ⇒ finite mode count), [melting](melting.md) (the grid stops being a grid), [thermal-conductivity-phonon](thermal-conductivity-phonon.md) (mean free path). This file is the shared clock table those entries read. That division is recorded rather than papered over by inventing a single dispersion cliff.

A further gap: QSA takes the measured \(\omega(\mathbf{q})\) as data. It does not derive branch frequencies from a more primitive set of node spring constants, and it does not predict *which* crystal will soften. Force-constant models that fit the curves are not promoted to node rules.

[Thermal expansion](thermal-expansion.md) (anharmonicity) and [piezoelectricity](piezoelectricity.md) (strain–polarization only in a lattice that lacks inversion) are couplings *on* this map, not additional clocks.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the measured \(\omega(\mathbf{q})\) is a solid clock table and the zone-boundary / melting failures are real, but the hardware scale is not a single number and the binary macros belong to the related lattice entries rather than to dispersion itself.

## Related entries

- [Speed of sound](speed-of-sound.md) — long-wavelength slope of the acoustic branches
- [Debye cutoff](debye-cutoff.md) — continuum ceiling for the finite mode count
- [Melting](melting.md) — loss of Bragg order; the grid that carries the map fails
- [Phonon thermal conductivity](thermal-conductivity-phonon.md) — heat current as a phonon-population transport spec
- [Elasticity](elasticity.md) — small-amplitude restoring output; yield is the failure envelope
- [Thermal expansion](thermal-expansion.md) — anharmonic correction; vanishes in the purely harmonic limit
- [Piezoelectricity](piezoelectricity.md) — strain ↔ polarization only in a lattice that lacks inversion
