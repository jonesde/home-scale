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
review_depth: light
related:
  - speed-of-sound
  - debye-cutoff
  - melting
  - thermal-conductivity-phonon
  - elasticity
  - thermal-expansion
  - piezoelectricity
updated: 2026-11-11
---

# Phonon Dispersion (Lattice Allowed-Clock Map)

### 4.1 Effect Name

Phonon dispersion (lattice allowed-clock map)

### 4.2 Macroscopic Observation

A crystal supports mechanical oscillations only at the frequencies \(\omega(\mathbf{q})\) of its branches. Inelastic neutron and X-ray scattering return energy-loss peaks along each branch; Raman and infrared spectroscopy read the long-wavelength optical frequencies; a struck solid rings at sound speeds set by the acoustic slope. Above the highest branch there is no lattice mode. At a displacive structural transition one branch softens toward zero frequency. Loss of crystalline order ends the map of sharp branches.

### 4.3 Established Quantitative Boundaries

- **Measured.** Acoustic slope. Longitudinal sound speed of polycrystalline aluminium \(6374\,\mathrm{m\,s^{-1}}\), shear \(3111\,\mathrm{m\,s^{-1}}\) [S3].
- **Model (continuum elasticity, \(v=\sqrt{C/\rho}\) from measured elastic constants).** Silicon along \([100]\): longitudinal \(8.43\,\mathrm{km\,s^{-1}}\), transverse \(5.84\,\mathrm{km\,s^{-1}}\). Diamond along \([100]\): \(17.52\) and \(12.82\,\mathrm{km\,s^{-1}}\) [S1][S2].
- **Measured.** Zone-centre optical frequency: silicon \(15.5\,\mathrm{THz}\) at 300 K; diamond \(39.9\,\mathrm{THz}\) [S1][S2]. These are the highest frequencies listed for either crystal; the listed zone-boundary modes lie between 3.45 and 14.7 THz in silicon and between 16.9 and 37.6 THz in diamond [S1][S2].
- **Computed here.** In wavenumbers, \(15.5\,\mathrm{THz} = 517\,\mathrm{cm^{-1}}\) and \(39.9\,\mathrm{THz} = 1331\,\mathrm{cm^{-1}}\).
- **Measured.** Lattice constants: silicon \(5.431\,\mathrm{\AA}\); diamond \(3.567\,\mathrm{\AA}\) [S1][S2].
- **Computed here.** Zone-boundary scale \(2\pi/a\): \(1.16\times10^{10}\,\mathrm{m^{-1}}\) for silicon, \(1.76\times10^{10}\,\mathrm{m^{-1}}\) for diamond.
- **Model (harmonic lattice).** A crystal of \(N\) atoms has exactly \(3N\) normal modes [S6]. With \(p\) atoms in the primitive cell these form 3 acoustic and \(3p-3\) optical branches.
- **Model (Debye fit to heat capacity).** Debye temperatures: aluminium 427.7 K [S4]; silicon 640 K [S1]; diamond 1860 K [S2].
- **Computed here.** Debye frequencies \(k\Theta_D/h\): aluminium 8.9 THz, silicon 13.3 THz, diamond 38.8 THz. For silicon and diamond the measured top of the spectrum (15.5 and 39.9 THz) lies above the Debye frequency. The Debye value is a fitted stand-in, filed as [debye-cutoff](debye-cutoff.md).
- **Measured.** Soft modes. In displacive transitions (ferroelectric perovskites such as \(\mathrm{PbTiO_3}\) and \(\mathrm{BaTiO_3}\), cell-doubling perovskites such as \(\mathrm{SrTiO_3}\), quartz) a branch frequency falls toward zero as the transition is approached. Order–disorder systems such as \(\mathrm{NaNO_2}\) show no soft mode above \(10^{11}\,\mathrm{Hz}\) [S5].
- **Measured.** Melting is not preceded by a soft mode: the crystal keeps a finite shear modulus up to its melting point [S7]. See [melting](melting.md).

**Data confidence:** High for the silicon and diamond frequencies, speeds and lattice constants (one evaluated semiconductor data archive) and for the aluminium sound speed. Debye temperatures are fitted numbers and move with the method. No maximum phonon frequency for aluminium and no aluminium lattice constant was opened; both were dropped. [S7] was read in the review of the melting entry and not re-opened here.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Harmonic lattice: \(\omega_s(\mathbf{q})\) is the measured frequency of branch \(s\) at wavevector \(\mathbf{q}\) in the first Brillouin zone. Outside the zone the same frequencies repeat.
- Acoustic long-wavelength limit:

  \[
  \omega_{\mathrm{ac}}(\mathbf{q}) \approx v_s(\hat{\mathbf{q}})\,|\mathbf{q}|, \qquad v_s=\sqrt{C/\rho}
  \]

  with \(C\) the relevant elastic constant ([elasticity](elasticity.md), [speed-of-sound](speed-of-sound.md)) [S1].
- Group velocity \(\mathbf{v}_g = \nabla_{\mathbf{q}}\omega\) is the transport speed of a packet. Mean-free-path limits are owned by [thermal-conductivity-phonon](thermal-conductivity-phonon.md).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The crystalline lattice. One primitive cell is the repeating unit; a well-defined \(\mathbf{q}\) is a phase relation across many cells, so the spectrum is an extended-crystal object. No single length is attached to it. An amorphous solid keeps a vibrational density of states and loses sharp branches.

- **Clock rate / latency.** \(\omega_s(\mathbf{q})\) is the allowed-clock table. Acoustic clocks run from zero to the zone-boundary frequency of the branch; optical clocks sit at terahertz (15.5 THz in silicon, 39.9 THz in diamond). Nothing in the lattice oscillates as a phonon above the highest measured branch.

- **Energy barriers or thresholds.** Not a latch. The mode energy \(\hbar\omega(n+\tfrac12)\) is an oscillator budget, not a barrier that holds a state. Softening to \(\omega\to0\) is loss of the restoring constraint along one coordinate.

- **Dominant failure modes.**
  - **Threshold** — clock ceiling: above the highest branch there is no lattice mode. The edge is the measured maximum of \(\omega_s(\mathbf{q})\), not the Debye frequency.
  - **Threshold** — zone edge: \(\mathbf{q}\) outside the first zone is an alias of a mode inside it.
  - **Crossover** — soft mode: at a displacive transition one branch frequency falls continuously toward zero as the transition temperature is approached; the structural change follows. Absent in order–disorder transitions and absent before melting.
  - **Threshold** — grid loss: melting is first-order. The branches end with the crystal, with no softening first.
  - **Crossover** — scattering: finite lifetime broadens a peak in proportion to the scattering rate; no scale filed here.

- **Emergent constant or stable output.** The measured surface \(\omega_s(\mathbf{q})\), its long-wave speeds and its zone-centre optical frequencies, for as long as the crystal stays ordered.

### 4.6 Internal Consistency Notes

Reading \(\omega(\mathbf{q})\) as the lattice's clock table is close to definitional: the acoustic slope matches the sound speed, the Raman line matches the zone-centre intercept, and no mode appears above the top branch.

Sourcing changed three things. The soft-mode failure is now limited to displacive structural transitions; the earlier text placed melting next to it, and the measured crystal keeps a finite shear modulus up to the melting point, so the predicted row `soft-mode-before-tm` is contradicted for ordinary melting. The Debye frequency is shown to fall below the measured top of the spectrum in silicon and diamond, so it is not the ceiling. Debye temperatures were corrected (silicon 640 K, diamond 1860 K) and the lead value moved to [debye-cutoff](debye-cutoff.md); the aluminium ceiling "near 10 THz" was dropped for lack of an opened source.

The mapping is incomplete as a collapse specification. Dispersion is a spectrum, not a binary output with one hardware number. The on/off envelopes sit in related entries: [speed-of-sound](speed-of-sound.md), [debye-cutoff](debye-cutoff.md), [melting](melting.md), [thermal-conductivity-phonon](thermal-conductivity-phonon.md). QSA takes the measured \(\omega(\mathbf{q})\) as data; it does not derive branch frequencies from node spring constants and does not predict which crystal will soften.

[Thermal expansion](thermal-expansion.md) and [piezoelectricity](piezoelectricity.md) are couplings on this map, not further clocks.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the measured \(\omega(\mathbf{q})\) is a solid clock table and the ceiling and grid-loss failures are real, but the hardware scale is not a single number and the binary outputs belong to the related lattice entries.

## Related entries

- [Speed of sound](speed-of-sound.md) — long-wavelength slope of the acoustic branches
- [Debye cutoff](debye-cutoff.md) — fitted stand-in for the finite mode count
- [Melting](melting.md) — first-order loss of the crystal that carries the map
- [Phonon thermal conductivity](thermal-conductivity-phonon.md) — heat current carried by these modes
- [Elasticity](elasticity.md) — the elastic constants behind the acoustic slope
- [Thermal expansion](thermal-expansion.md) — anharmonic correction
- [Piezoelectricity](piezoelectricity.md) — strain–polarization coupling in a lattice that lacks inversion

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Ioffe Institute, NSM Archive, Silicon: mechanical properties, elastic constants, lattice vibrations (and the Basic Parameters page)](http://www.ioffe.ru/SVA/NSM/Semicond/Si/mechanic.html) | full-text | Si wave speeds from elastic constants, phonon frequencies at the zone centre and boundary, lattice constant 5.431 Å, Debye temperature 640 K. Evaluated data archive, secondary. |
| S2 | [Ioffe Institute, NSM Archive, Diamond: mechanical properties, elastic constants, lattice vibrations (and the Basic Parameters page)](http://www.ioffe.ru/SVA/NSM/Semicond/Diamond/mechanic.html) | full-text | Diamond wave speeds, phonon frequencies (from Solin and Ramdas 1970), lattice constant 3.567 Å, Debye temperature 1860 K. Secondary. |
| S3 | [Kaye and Laby, *Tables of Physical and Chemical Constants*, §2.4.1 The speed and attenuation of sound (NPL, archived)](https://web.archive.org/web/2018/http://www.kayelaby.npl.co.uk/general_physics/2_4/2_4_1.html) | full-text | Longitudinal and shear sound speeds of aluminium. |
| S4 | [Phillips, *Phys. Rev.* 114, 676 (1959)](https://doi.org/10.1103/PhysRev.114.676) | abstract | Aluminium Debye temperature 427.7 K from low-temperature heat capacity. |
| S5 | [Scott, "Soft-mode spectroscopy: experimental studies of structural phase transitions", *Rev. Mod. Phys.* 46, 83 (1974)](https://doi.org/10.1103/RevModPhys.46.83) | abstract | Classes of displacive transition with a soft mode; order–disorder systems with none above 10¹¹ Hz. |
| S6 | [Merhav, "Statistical Physics: a Short Course for Electrical Engineering Students", arXiv:1307.5137, ch. 7](https://arxiv.org/abs/1307.5137) | full-text | Exactly 3N normal modes in a crystal of N atoms. Lecture notes, secondary. |
| S7 | [Buchenau and Zorn, "A new view of the Lindemann criterion", arXiv:1311.4739](https://arxiv.org/abs/1311.4739) | cited-only | Finite shear modulus of the crystal at its melting point. Read in full for the melting entry; not re-opened in this pass. |
