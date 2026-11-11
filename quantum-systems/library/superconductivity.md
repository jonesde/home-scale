---
id: superconductivity
title: Superconductivity (Zero-Resistance Transport)
status: formal
family: gapped-coherence
constraints:
  - thermal
  - field-threshold
  - energy-barrier
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - meissner
  - josephson-effect
  - flux-quantization
  - type-ii-critical-field
  - superfluid-helium-4
  - electron-heat-capacity
updated: 2026-11-11
---

# Superconductivity (Zero-Resistance Transport)

### 4.1 Effect Name

Superconductivity (zero-resistance transport)

### 4.2 Macroscopic Observation

Below a material-specific critical temperature the DC resistance of certain metals, alloys and compounds falls below the instrument floor, and a closed loop carries a current with no measurable decay and no continuous voltage. Warming through \(T_c\), applying a large enough magnetic field, or driving a large enough current restores ordinary resistance. Field expulsion is a related observation filed separately ([meissner](meissner.md)).

### 4.3 Established Quantitative Boundaries

- **Measured.** Critical temperatures at zero field: Al 1.19 K, Sn 3.73 K, Pb 7.2 K, Nb 9.25 K [S1]; Hg 4.15 K, NbTi 9.4 K, \(\mathrm{Nb_3Sn}\) 18 K [S2]. A second table gives Al 1.14 K and Nb 9.2 K [S2]. \(\mathrm{YBa_2Cu_3O_{7-\delta}}\) near optimal doping: 92–93.7 K [S4]. Copper, silver and gold do not superconduct at ambient pressure [S2].
- **Measured.** Critical fields at \(T \to 0\), type I: Al 10 mT, Sn 30.5 mT, Pb 80.3 mT [S1]. Niobium (type II), at 2 K: \(B_{c1} \approx 160\) mT, thermodynamic \(B_c \approx 190\) mT, \(B_{c2} \approx 300\) mT [S2]; the review table lists 206 mT for Nb [S1]. NbTi: \(B_{c2} = 14\) T [S2].
- **Model (Ginzburg–Landau and WHH extrapolation from resistive transitions).** YBCO films: \(\mu_0 H_{c2}(0) = 153\) T with the field along *c* and 638 T with the field in the *ab* plane [S3].
- **Measured.** Gap \(\Delta(0)\): Al 0.175 meV, Sn 0.557 meV, Pb 1.365 meV, Nb 1.52 meV [S1].
- **Computed here.** \(2\Delta(0)/k_BT_c\) from the two columns of [S1]: Al 3.41, Sn 3.47, Pb 4.40, Nb 3.81. The weak-coupling BCS value is 3.52 (\(\Delta(0) = 1.76\,k_BT_c\)) [S2]. Gap frequency \(2\Delta/h\): Al 85 GHz, Sn 269 GHz, Pb 660 GHz, Nb 735 GHz.
- **Model (BCS / Pippard; tabulated values).** Coherence length \(\xi_0\): Al 1.6 µm, Sn 0.23 µm, Pb 0.090 µm, Nb 0.030 µm [S1]. A second table gives Nb 39 nm and Pb 510 nm [S2]; the two tables differ by a factor of five for lead. YBCO: \(\xi_{ab}(0) = 1.18\) nm and \(\xi_c(0) = 0.30\) nm [S3], or \(\xi_{ab}(0) = 1.41\) nm [S4].
- **Measured.** Persistent current: the decay time of the current in a superconducting solenoid was bounded at more than 100,000 years [S5].
- **Measured.** Mixed state: a transport current through a type-II conductor in a field moves the flux tubes and produces a resistance unless they are held at pinning centres. Pinned NbTi carries 3700 A mm⁻² at 5 T and 4.2 K [S2].
- **Measured.** Small cross-sections. Aluminium wires thinned from about 100 nm to below 10 nm still superconduct, with a critical temperature that rises as the wire or film gets thinner; these are far below the 1.6 µm \(\xi_0\) of bulk aluminium. Wires below about 50 nm show quantum phase slips and a resistance that persists to low temperature; near 10 nm diameter the phase slips proliferate and the wire crosses over to normal behaviour even at \(T = 0\) [S1].
- **Convention.** Holding a persistent current costs zero continuous power: no voltage is present on the loop.

**Data confidence:** High for \(T_c\), type-I \(H_c\), the gap and the existence of \(H_{c1}/H_{c2}\). Tabulated \(\xi_0\) and \(\lambda\) differ between the two opened tables by up to a factor of five. The 100,000-year bound rests on a `snippet` of a secondary account; the 1963 letter itself was not opened. YBCO numbers are from one film study and one tertiary page.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Type-I field envelope (empirical): \(H_c(T) \approx H_c(0)\,[1-(T/T_c)^2]\).
- Upper critical field and coherence length [S2]:

  \[
  \mu_0 H_{c2} = \frac{\Phi_0}{2\pi\xi^2}, \qquad \Phi_0 = \frac{h}{2e} = 2.067\,833\,848\ldots\times 10^{-15}\,\mathrm{Wb}\ \text{[S6]}
  \]

  **Computed here:** 14 T gives \(\xi = 4.8\) nm (the source quotes 5 nm [S2]).
- Weak-coupling BCS relation \(\Delta(0) = 1.76\,k_BT_c\) [S2]. Measured ratios run from 3.41 to 4.40 in the four elements above.
- A wire of cross-section \(s\) acquires resistance through phase slips, each of which changes the phase difference by \(2\pi\) and produces a voltage pulse; the thermally activated rate depends on the condensation energy of a volume \(s\,\xi\) [S1].

Pairing mechanisms are not recorded as QSA content.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A connected superconducting path. The coherence length is a material property spanning 0.3 nm to 1.6 µm; it is not a minimum size, since aluminium wires two orders of magnitude thinner than \(\xi_0\) superconduct. The measured size limit is a cross-section of order 10 nm in the wires studied, reached through a rising phase-slip rate. A persistent current further needs a closed loop ([flux-quantization](flux-quantization.md)).

- **Clock rate / latency.** The gap sets a frequency \(2\Delta/h\): 85 GHz for Al, 660–735 GHz for Pb and Nb. DC zero resistance is the \(\omega \to 0\) output.

- **Energy barriers or thresholds.** The gap \(2\Delta\) suppresses quasiparticle transport. \(T_c\), \(H_c\) or \(H_{c2}\), and the specimen's critical current bound the state. Holding a persistent current costs no continuous voltage.

- **Dominant failure modes.**
  - **Threshold** — thermal: \(T > T_c\), a phase transition. In wires of cross-section below about 50 nm it broadens into a crossover through phase slips.
  - **Threshold** — field: \(H > H_c\) (type I) or \(H > H_{c2}\) (type II). Between \(H_{c1}\) and \(H_{c2}\) expulsion has failed and zero resistance holds only with pinned flux.
  - **Threshold** — current: above the specimen's critical current. Specimen-specific; no material constant is filed.
  - **Crossover** — flux motion in the mixed state: resistance appears when the flux tubes move, \(\mathbf{E} = \mathbf{B}\times\mathbf{v}\), and falls with pinning strength. No single scale.
  - **Crossover** — cross-section: phase-slip rate rises as the wire thins; normal behaviour at about 10 nm diameter in the wires reviewed.

- **Emergent constant or stable output.** DC resistance below the instrument floor and a persistent loop current at zero voltage, while \(T\), \(H\) and \(I\) stay inside the envelope.

### 4.6 Internal Consistency Notes

The three limits \(T_c\), \(H_c\) or \(H_{c2}\), and the critical current map onto thermal, field and current failures of a gapped state. The split from Meissner is required by the data: mixed-state wires carry lossless current while flux has entered.

Sourcing changed three things. The coherence length is not a minimum hardware size: superconductivity is measured in wires far thinner than \(\xi_0\), and the loss of zero resistance with size is a crossover through phase slips near 10 nm. The BCS ratio 3.52 is bracketed by measured ratios of 3.41 to 4.40. Entries with no opened source were dropped (\(\mathrm{MgB_2}\), Hg-1223, the \(\mathrm{Nb_3Sn}\) upper critical field); the Nb coherence length is 30–39 nm and the YBCO in-plane value 1.2–1.4 nm.

The mapping does not close on hardware identity. Pinning, which decides whether the mixed state is lossless, is set by microstructure and is not a buffer or barrier specification here.

This entry asserts no pairing mechanism. [Superfluid helium-4](superfluid-helium-4.md) is the chargeless analogue; [electron-heat-capacity](electron-heat-capacity.md) reads the same gap thermally.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(T_c\), the critical fields and \(2\Delta\) are measured envelopes that translate into thermal, field and gap failures; the minimum cross-section is a crossover known for a few materials, and the pinning step is unspecified.

## Related entries

- [Meissner effect](meissner.md) — field expulsion; different artifact, same condensate
- [Josephson effect](josephson-effect.md) — pair current through a weak link
- [Flux quantization](flux-quantization.md) — closed-loop fluxoid
- [Type-II critical field](type-ii-critical-field.md) — mixed state and vortex lattice
- [Superfluid helium-4](superfluid-helium-4.md) — chargeless analogue
- [Electron heat capacity](electron-heat-capacity.md) — the same gap read in the heat capacity

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Arutyunov, Golubev and Zaikin, "Superconductivity in one dimension", arXiv:0805.2118 (2008)](https://arxiv.org/abs/0805.2118) | full-text | Review. Table I: critical temperature, penetration depth, coherence length, critical field and gap of Al, Sn, Pb, Nb. Phase slips; Al wires down to below 10 nm; crossover to normal near 10 nm diameter. |
| S2 | [Schmüser, Proc. 11th Workshop on RF Superconductivity (2003), paper MOT01](https://jacow.org/SRF2003/papers/MOT01.pdf) | full-text | Secondary (lecture). Critical-temperature table; BCS ratio; Nb fields at 2 K; NbTi 14 T and 5 nm; second table of penetration depth and coherence length; flux-flow resistance, pinning, 3700 A/mm². |
| S3 | [Petrenko et al., *Low Temp. Phys.* 48, 856 (2022), arXiv:2209.14668](https://arxiv.org/abs/2209.14668) | full-text | YBCO films: extrapolated upper critical fields 153 T and 638 T; coherence lengths 11.8 Å and 3.0 Å. |
| S4 | [Hoffman Lab, Harvard, YBCO materials page](https://hoffman.physics.harvard.edu/materials/ybco/) | full-text | Tertiary. YBCO critical temperature 92–93.7 K near optimal doping; in-plane coherence length 1.41 nm (Gauzzi et al. 2000). |
| S5 | [File and Mills, *Phys. Rev. Lett.* 10, 93 (1963)](https://doi.org/10.1103/PhysRevLett.10.93) | snippet | Persistent-current decay time above 100,000 years. Paywalled; the figure was seen only in a search excerpt of a secondary account. |
| S6 | [CODATA 2022, magnetic flux quantum (NIST)](https://physics.nist.gov/cgi-bin/cuu/Value?flxquhs2e) | full-text | Flux quantum, exact since 2019. |
