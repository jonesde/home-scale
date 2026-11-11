---
id: thermal-conductivity-phonon
title: Phonon Thermal Conductivity (Mean-Free-Path Transport)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - thermal
  - spatial-buffer
confidence_data: medium
confidence_mapping: medium
review_depth: standard
related:
  - phonon-dispersion
  - speed-of-sound
  - debye-cutoff
  - elasticity
  - melting
  - thermal-expansion
  - electron-heat-capacity
updated: 2026-11-11
---

# Phonon Thermal Conductivity (Mean-Free-Path Transport)

### 4.1 Effect Name

Phonon thermal conductivity (mean-free-path transport)

### 4.2 Macroscopic Observation

An electrical insulator carries a steady heat current under a temperature gradient. In a good crystal the thermal conductivity \(\kappa\) is small at the lowest temperatures, rises steeply, peaks, and falls toward room temperature and above. Diamond is the extreme case. Removing the minority isotope raises its conductivity further. A glass conducts far less, and different glasses behave alike. In a metal most of the heat is carried by electrons; the lattice carries a minor share, which is the part this entry maps.

### 4.3 Established Quantitative Boundaries

- **Measured.** Natural diamond at room temperature: about 2200 W m⁻¹ K⁻¹. It contains about 1.07 % ¹³C. A crystal purified to about 0.00024 % ¹³C measures about 3100 W m⁻¹ K⁻¹ at room temperature, comparable to the best values for less pure crystals, which suggests a further scattering mechanism such as vacancies [S1].
- **Measured.** A 99.9 % ¹²C diamond at 104 K: 410 W cm⁻¹ K⁻¹, the highest thermal conductivity measured for a solid above liquid-nitrogen temperature at the time [S2].
- **Computed here.** 410 W cm⁻¹ K⁻¹ is 41 000 W m⁻¹ K⁻¹, 19 times the room-temperature value of natural diamond. The isotopically pure crystal conducts 1.4 times as well as natural diamond at room temperature.
- **Model (Callaway).** The same analysis predicts more than 2000 W cm⁻¹ K⁻¹ near 80 K for a 99.999 % ¹²C crystal [S2]. This is a prediction and was not measured there.
- **Measured.** Glasses. The thermal conductivity of several non-crystalline solids, measured from 0.05 K to 100 K, agrees within a factor of 5 over the whole range and varies as \(T^{1.8}\) below 1 K. The phonon mean free path derived from it is about \(10^{-4}\) cm at 2 K and falls as \(T^{-4}\) at higher temperature [S3].
- **Model (first-principles transport).** In vitreous silica above the low-temperature plateau, anharmonicity has a negligible effect on heat transport [S6].
- **Model (first-principles Boltzmann transport).** In 18 metals at room temperature the phonon contribution is 2–18 W m⁻¹ K⁻¹, between 1 % and 40 % of the total. Copper: 17.6 of 378.5 (measured total 402). Aluminium: 8.1 of 233.9 (237). Nickel: 14.5 of 115.6 (93). Phonon mean free paths in these metals are within 10 nm; electron mean free paths are 5–25 nm. The Sommerfeld value of the Lorenz number is \(2.44 \times 10^{-8}\) W Ω K⁻² [S4].
- **Computed here.** Phonon share of the calculated total: copper 4.7 %, aluminium 3.5 %, nickel 12.5 %.
- **Measured.** On melting, the conductivity of a metal drops sharply as the crystalline order disappears, and in liquid metals the lattice contribution is about two orders of magnitude below the electronic one (tertiary) [S5]. The metal remains a good conductor of heat in the liquid.
- **Model (kinetic theory).** \(\kappa = \tfrac13Cv\ell\), with \(C\) the phonon heat capacity per volume, \(v\) a mean sound speed and \(\ell\) the mean free path. This is the relation used to extract the mean free paths in [S3]. At low temperature in a clean crystal \(\ell\) is limited by the specimen surface and \(\kappa\) follows \(C \propto T^3\); at high temperature phonon–phonon umklapp scattering shortens \(\ell\) roughly as \(1/T\). No source was opened for these two limits; they are textbook statements.

**Data confidence:** Medium, lowered from High. The diamond and glass measurements and the metal calculations were read in sources, two of them as abstracts. The boundary-scattering limit, the \(1/T\) law, a general peak temperature and a room-temperature value for an oxide glass were not found in an opened source, and the melting statement rests on a tertiary column.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Kinetic formula: \(\kappa = \tfrac13Cv\ell\); equivalently an integral of \(C(\omega)v^2\tau(\omega)\) over the spectrum.
- Boundary limit: \(\ell\) of the order of the specimen size, so \(\kappa \propto T^3\) in an insulator at low temperature.
- Umklapp: a three-phonon process that changes the total crystal momentum by a reciprocal-lattice vector; normal processes conserve it.
- Electronic channel in a metal (Wiedemann–Franz): \(\kappa_e = L_0\sigma T\) with \(L_0 = 2.44 \times 10^{-8}\) W Ω K⁻² [S4].
- Fourier's law, \(\mathbf j_Q = -\kappa\nabla T\), holds when the gradient is gentle on the scale of \(\ell\).

The formula organizes measured \(\kappa\). It does not predict a crystal's peak value from node-level quantities.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A lattice that carries propagating acoustic modes, and a mean free path. The spatial buffer is \(\ell\): about a micrometre in a glass at 2 K, under 10 nm for phonons in a metal at room temperature. When \(\ell\) reaches the specimen size, the specimen is the buffer.

- **Clock rate / latency.** The carrier speed is the sound speed of [speed-of-sound](speed-of-sound.md). The transport clock is the scattering time \(\ell/v\).

- **Energy barriers or thresholds.** None stored.

- **Dominant failure modes.**
  - **Crossover** — isotopes and defects: \(\kappa\) scales with \(\ell\). 1.07 % of a second isotope lowers diamond from about 3100 to about 2200 W m⁻¹ K⁻¹.
  - **Crossover** — disorder: in a glass \(\ell\) falls as \(T^{-4}\) above a few kelvin and no crystal-like peak forms.
  - **Crossover** — temperature: on either side of the peak, as \(C\) vanishes at low temperature and as phonon–phonon scattering grows at high temperature (form \(T^3\) and roughly \(1/T\); not sourced here).
  - **Crossover** — specimen size at low temperature: \(\kappa\) follows the smallest dimension once it is shorter than the bulk \(\ell\) (no measured scale opened).
  - **Crossover** — channel: in a metal the lattice carries 1–40 % of the heat, so the measured \(\kappa\) is mostly not this entry's output.
  - **Threshold** — melting: the crystal's phonon population ends at \(T_m\). In a metal the total conductivity drops and stays large, because the electronic channel continues.

- **Emergent constant or stable output.** A \(\kappa(T)\) set by heat capacity, sound speed and mean free path: about 2200 W m⁻¹ K⁻¹ in natural diamond at room temperature and 2–18 W m⁻¹ K⁻¹ for the lattice part in metals.

### 4.6 Internal Consistency Notes

Factoring \(\kappa\) into \(C\), \(v\) and \(\ell\) is consistent with the other lattice entries: [debye-cutoff](debye-cutoff.md) owns \(C(T)\), [speed-of-sound](speed-of-sound.md) owns \(v\), and this file owns \(\ell\).

Sourcing changed the entry in three ways. Diamond is 2200 to 3100 W m⁻¹ K⁻¹ at room temperature; the first version gave the order of magnitude only, and its figure of about 1 W m⁻¹ K⁻¹ for oxide glasses could not be sourced and was removed. Metals were excluded outright in the first version; they are now included with the lattice share stated, because every metal has this channel and it is 12 % of the total in nickel. And the statement that the channel "collapses" at melting needed care: the phonon population of the crystal does end, but in a metal the conductivity that is measured falls and does not vanish, since electrons carry it on both sides.

The glass result in [S6] is a caution for the mapping: in a strongly disordered solid, heat transport is not limited by anharmonic scattering, so the umklapp account applies to crystals only.

The mapping takes the kinetic formula as descriptive. It does not obtain \(\ell(T)\) from node-level anharmonicity, which [thermal-expansion](thermal-expansion.md) also leaves unquantified.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the isotope, disorder and channel-share results identify the mean free path as the transport resource, but the temperature and size limits are unsourced here and \(\ell\) is not derived.

## Related entries

- [phonon-dispersion](phonon-dispersion.md) — zone structure that makes umklapp possible
- [speed-of-sound](speed-of-sound.md) — carrier speed
- [debye-cutoff](debye-cutoff.md) — heat capacity and the mode ceiling
- [elasticity](elasticity.md) — the moduli that set the speed
- [melting](melting.md) — end of the crystal's phonon population
- [thermal-expansion](thermal-expansion.md) — the same anharmonicity
- [electron-heat-capacity](electron-heat-capacity.md) — the electronic channel that dominates in metals

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Cheng et al., "Ultrahigh thermal conductivity in isotopically ultrapure single-crystal diamond", arXiv:2609.24191](https://arxiv.org/abs/2609.24191) | full-text | Natural diamond about 2200 W/m/K; 1.07 % carbon-13; purified crystal about 3100 W/m/K at room temperature. Preprint. |
| S2 | [Wei, Kuo, Thomas, Anthony and Banholzer, *Phys. Rev. Lett.* 70, 3764 (1993)](https://doi.org/10.1103/PhysRevLett.70.3764) | abstract | 410 W/cm/K at 104 K in 99.9 % carbon-12 diamond; Callaway-model prediction near 80 K. |
| S3 | [Zeller and Pohl, *Phys. Rev. B* 4, 2029 (1971)](https://doi.org/10.1103/PhysRevB.4.2029) | abstract | Glasses from 0.05 K to 100 K: agreement within a factor of 5, exponent 1.8 below 1 K, mean free path at 2 K and its temperature dependence. |
| S4 | [Tong, Li, Ruan and Bao, "A comprehensive first-principles analysis of phonon thermal conductivity and electron-phonon coupling in different metals", arXiv:1907.01364](https://arxiv.org/abs/1907.01364) | full-text | Phonon and electron conductivities of 18 metals with measured totals; mean free paths; Lorenz number. |
| S5 | [Lasance, "Thermal conductivity of liquid metals", *Electronics Cooling* (May 2008)](https://www.electronics-cooling.com/2008/05/thermal-conductivity-of-liquid-metals/) | full-text | Tertiary: sharp drop of conductivity on melting; lattice contribution two orders below the electronic one in liquid metals. |
| S6 | [Simoncelli, Mauri et al., "Thermal conductivity of glasses above the plateau: first-principles theory and applications", arXiv:2209.11201](https://arxiv.org/abs/2209.11201) | full-text | Anharmonicity negligibly affects heat transport in vitreous silica. |
