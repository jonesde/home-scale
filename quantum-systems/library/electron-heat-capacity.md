---
id: electron-heat-capacity
title: Electron Heat Capacity (Fermi-Surface Average)
status: formal
family: ensemble-averages
constraints:
  - thermal
confidence_data: high
confidence_mapping: medium
review_depth: standard
related:
  - thermal-equilibrium-temperature
  - superconductivity
  - debye-cutoff
  - semiconductor-gap-absorption
  - johnson-nyquist-noise
updated: 2026-11-13
---

# Electron Heat Capacity (Fermi-Surface Average)

### 4.1 Effect Name

Electron heat capacity (Fermi-surface average)

### 4.2 Macroscopic Observation

The heat capacity of a normal metal at low temperature has a term linear in \(T\): after the lattice \(T^{3}\) term is subtracted, \(\gamma T\) remains. The coefficient \(\gamma\) is a material constant, about 1 mJ mol⁻¹ K⁻² in simple metals and several times larger in transition metals. At room temperature the electronic term is about 1 % of the heat capacity of copper or aluminium. It is the leading term only below a few kelvin. In a superconductor the linear term is replaced below \(T_c\) by one that falls roughly exponentially.

### 4.3 Established Quantitative Boundaries

- **Measured.** Form. Below a few kelvin the normal-state heat capacity is \(C = \gamma T + \beta T^{3}\) within experimental error, shown for aluminium between 0.11 and 4.0 K [S2]. The cubic term is the lattice contribution bounded by the [Debye cutoff](debye-cutoff.md).
- **Measured.** \(\gamma\) in mJ mol⁻¹ K⁻²:

  | Metal | \(\gamma\) measured | \(\gamma\) free-electron | Source |
  |---|---|---|---|
  | Cu | 0.690–0.696 (0.695 tabulated) | 0.505 | [S1][S3] |
  | Ag | 0.645–0.652 (0.646 tabulated) | 0.645 | [S1][S3] |
  | Al | 1.35 | 0.912 | [S2][S3] |
  | Fe | 4.89–4.90 | — | [S4][S5] |
  | Ni | 7.04 | — | [S5] |
  | Pd | 9.42–9.45 | — | [S6][S5] |

- **Model (free-electron gas at the metal's conduction-electron density).** The free-electron column above [S3], and the Fermi temperatures: Cu \(8.16\times10^{4}\) K, Ag \(6.38\times10^{4}\) K, Al \(13.6\times10^{4}\) K, with Fermi energies of 7.00, 5.49 and 11.7 eV [S7]. These are model outputs, not measurements.
- **Computed here.** The free-electron formula \(\gamma = \pi^{2}zR/2T_F\) with those Fermi temperatures gives 0.503 (Cu), 0.643 (Ag) and 0.905 (Al, \(z = 3\)) mJ mol⁻¹ K⁻², matching the tabulated column. Measured over free-electron: 1.38 (Cu), 1.00 (Ag), 1.48 (Al). \(\gamma\) of Pd is 13.6 times that of Cu.
- **Measured.** Of the 9.42 mJ mol⁻¹ K⁻² in Pd, a band calculation accounts for 5.6; the rest is attributed to electron–phonon coupling (28–41 %) and to spin fluctuations (30–40 %) [S6].
- **Measured.** Heavy-fermion end: \(\mathrm{CeAl_3}\) below 0.2 K has \(\gamma = 1620\) mJ mol⁻¹ K⁻² [S9].
- **Computed here.** That is 2300 times the value for copper. The form \(C = \gamma T\) is unchanged.
- **Measured.** Debye temperatures used below: Cu 344 K [S1]; Al 427.7 K [S2].
- **Computed here.** The lattice coefficient \(A = 12\pi^{4}R/5\Theta_D^{3}\) is 0.0478 mJ mol⁻¹ K⁻⁴ for Cu and 0.0248 for Al. The electronic and lattice terms are equal at \(T = \sqrt{\gamma/A}\): 3.8 K in Cu and 7.4 K in Al. Below that temperature the electrons carry most of the heat capacity.
- **Measured.** Total heat capacity at 25 °C: Cu 24.440 J mol⁻¹ K⁻¹ (0.385 J g⁻¹ K⁻¹); Al 24.200 (0.897); Fe 25.10 (0.449); Ni 26.07 (0.444) [S8][S5].
- **Computed here.** Electronic share at 300 K, taking \(\gamma T\) with the low-temperature \(\gamma\):

  | Metal | \(\gamma T\) at 300 K (J mol⁻¹ K⁻¹) | Share of the total |
  |---|---|---|
  | Cu | 0.21 | 0.85 % |
  | Al | 0.41 | 1.7 % |
  | Fe | 1.47 | 5.9 % |
  | Ni | 2.11 | 8.1 % |

  For Cu and Al the extrapolation is safe, since \(T/T_F\) is 0.37 % for Cu at 300 K. For Fe and Ni it is an estimate: \(\gamma\) was measured in the ferromagnetic state near 1 K, and no opened source confirms that it is constant up to 300 K. The Dulong–Petit value \(3R\) is 24.9 J mol⁻¹ K⁻¹; the room-temperature totals above are within 5 % of it.
- **Measured.** Electron–lattice equilibration. In thin copper films heated by 150–300 fs pulses the electrons and lattice are out of equilibrium, and energy transfer to the lattice takes 1–4 ps, increasing with fluence [S10].
- **Measured.** Superconducting state. In aluminium (\(T_c = 1.163\) K) the electronic heat capacity for \(0.25 < T/T_c < 0.5\) follows \(C_{es}/\gamma T_c = 7.1\exp(-1.34\,T_c/T)\). Below \(T/T_c \approx 0.25\) it lies above that exponential, by a factor of 4 at the lowest temperature measured [S2]. The heat capacity jumps at \(T_c\) [S3].
- **Computed here.** The fitted exponential gives \(C_{es}/\gamma T_c = 0.49\) at \(T_c/2\), close to the normal-state 0.5, and 0.033 at \(T_c/4\), which is 13 % of the normal-state value.

**Data confidence:** High for Cu, Ag and Al, read in a NIST critical review and a primary abstract. Medium for Fe and Pd (one primary each plus a compiled handbook page) and for Ni, which rests on the compiled page alone. Room-temperature heat capacities are CRC values taken from a tertiary page. The 300 K electronic share for Fe and Ni is an extrapolation.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Sommerfeld form for a Fermi gas [S3]:

  \[
  C_e = \gamma T,\qquad \gamma = \frac{\pi^{2}}{3}D(E_F)\,k^{2}
  \]

  with \(D(E_F)\) the density of states at the Fermi energy. For free electrons, per mole of atoms with \(z\) electrons each, \(\gamma = \pi^{2}zR/2T_F\).
- Lattice companion at low \(T\): \(C_{\mathrm{ph}} = AT^{3}\), \(A = 12\pi^{4}R/5\Theta_D^{3}\). The two terms are separated by plotting \(C/T\) against \(T^{2}\) [S4].
- Superconducting state: an exponential fall below \(T_c\) and a jump at \(T_c\), as in the aluminium fit above. This entry does not own the gap.

\(\gamma\) is taken from measurement. \(T_F\) is a free-electron model parameter.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The electrons within about \(kT\) of the Fermi energy. That is a temperature-dependent statistical buffer, of order \((T/T_F)N\): 0.37 % of the conduction electrons in copper at 300 K. There is no node count at which the electronic heat capacity begins. A material with a gap at the Fermi energy has no such population.

- **Clock rate / latency.** The electron–lattice equilibration time, 1–4 ps in copper. Heat deposited in the electrons faster than that is held first by a subsystem with about 1 % of the total heat capacity; after a few picoseconds the lattice heat capacity governs. Calorimetry and ohmic heating on microsecond scales are far slower.

- **Energy barriers or thresholds.** The operating condition is the absence of a gap at the Fermi energy. A superconducting gap or a band gap removes the contributing slice; those gaps are owned by [superconductivity](superconductivity.md) and [semiconductor gap absorption](semiconductor-gap-absorption.md).

- **Dominant failure modes.**
  - **Crossover** — low temperature: \(\gamma T\) falls linearly to zero. No critical value; a fixed instrument floor is eventually crossed.
  - **Threshold** — superconducting transition: at \(T_c\) (1.163 K in Al) the heat capacity jumps and the linear term is replaced by a roughly exponential one, 13 % of the normal value at \(T_c/4\). A phase transition.
  - **Threshold** — no Fermi surface: an insulator or undoped semiconductor has no metallic \(\gamma T\). A property of the material class; no number filed.
  - **Crossover** — lattice dominance: the lattice term grows as \(T^{3}\) and equals the electronic term at 3.8 K (Cu) or 7.4 K (Al). At 300 K the electronic share is 0.85 % (Cu) to about 8 % (Ni, extrapolated). The average persists; it is a small part of the reading.

- **Emergent constant or stable output.** A heat capacity linear in \(T\) with a material coefficient \(\gamma\), from 0.65 (Ag) to 9.4 (Pd) mJ mol⁻¹ K⁻² in the metals tabulated.

### 4.6 Internal Consistency Notes

The participating-fraction picture fits the family: the output is an average over a thermal window, and shrinking the window shrinks the output. The superconducting and insulating cases replace the contributing population, the same class of failure as on the [temperature](thermal-equilibrium-temperature.md) entry.

Sourcing changed four things. Fermi temperatures were listed as measured material parameters; they are free-electron model values, and Cu is \(8.16\times10^{4}\) K. The free-electron model reproduces \(\gamma\) of silver, falls short by a factor of 1.4–1.5 for copper and aluminium, and has no tabulated entry for the transition metals, where \(\gamma\) is 7 to 14 times that of copper. The superconducting fall was given as a pure exponential; in aluminium the measured heat capacity departs from the exponential below a quarter of \(T_c\). And the file now states how small the electronic term is at room temperature, with the caveat on Fe and Ni.

For heating estimates elsewhere in the project: use the total specific heat (Cu 0.385, Al 0.897, Fe 0.449, Ni 0.444 J g⁻¹ K⁻¹ at 25 °C). The electronic term changes those by about 1 % in Cu and Al and matters separately only for deposition faster than a few picoseconds.

The mapping does not compute \(\gamma\). It takes the measured value, and the Pd and \(\mathrm{CeAl_3}\) cases show that interactions can raise it by a factor of 1.7 to 2300 over a band or free-electron estimate without changing the linear form.

[Johnson–Nyquist noise](johnson-nyquist-noise.md) is another readout of a thermal electron population in a metal. The two entries share a bath and not a buffer number.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(\gamma T\) and its replacement below \(T_c\) are measured and translate into a temperature-dependent Fermi-surface buffer; \(\gamma\) is taken, and no single node count is claimed.

## Related entries

- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the bath average of which this is one electronic readout
- [Superconductivity](superconductivity.md) — the gap that replaces the linear term
- [Debye cutoff](debye-cutoff.md) — the lattice \(T^{3}\) companion
- [Semiconductor gap absorption](semiconductor-gap-absorption.md) — no Fermi surface, no metallic \(\gamma T\)
- [Johnson–Nyquist noise](johnson-nyquist-noise.md) — electrical fluctuation readout of a thermal electron population

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Furukawa, Saba and Reilly, NSRDS-NBS 18 (1968)](https://nvlpubs.nist.gov/nistpubs/Legacy/NSRDS/nbsnsrds18.pdf) | full-text | Critical review: reported γ of Cu (0.690–0.696) and Ag (0.645–0.652); Debye temperature of Cu 344 K. |
| S2 | [Phillips, *Phys. Rev.* 114, 676 (1959)](https://doi.org/10.1103/PhysRev.114.676) | abstract | Aluminium 0.11–4.0 K: γ = 1.35 mJ/mol K², Debye temperature 427.7 K, Tc = 1.163 K, exponential fit of the superconducting heat capacity and its failure at low temperature. |
| S3 | [Wikipedia, "Electronic specific heat"](https://en.wikipedia.org/wiki/Electronic_specific_heat) | full-text | Tertiary (table from Kittel): measured and free-electron γ for Cu, Ag, Al; Sommerfeld formula; jump at Tc. |
| S4 | [Hill, McQueeney, Wu et al., arXiv:0708.1432 (2007)](https://arxiv.org/abs/0708.1432) | full-text | Pure α-Fe: γ = 4.89(1) mJ/mol K² from a plot of C/T against T². |
| S5 | [KnowledgeDoor, Elements Handbook (nickel page; iron, palladium and copper pages alongside)](https://knowledgedoor.com/2/elements_handbook/nickel.html) | full-text | Tertiary compilation: γ of Ni 7.04, Fe 4.90, Pd 9.45; specific heats at 298.15 K. |
| S6 | [Doubble et al., *Phys. Rev. Lett.* 105, 027207 (2010), arXiv:1005.4402](https://arxiv.org/abs/1005.4402) | full-text | Pd: experimental γ 9.42 mJ/mol K² against 5.6 from the band density of states; electron–phonon and spin-fluctuation enhancements. |
| S7 | [HyperPhysics, "Fermi energies, temperatures and velocities" (data from Ashcroft and Mermin)](http://hyperphysics.phy-astr.gsu.edu/hbase/Tables/fermi.html) | full-text | Tertiary: free-electron Fermi energies and temperatures of Cu, Ag, Al. |
| S8 | [Wikipedia, "Heat capacities of the elements (data page)"](https://en.wikipedia.org/wiki/Heat_capacities_of_the_elements_(data_page)) | full-text | Tertiary (CRC values): molar and specific heat capacities of Cu, Al, Fe, Ni at 25 °C. |
| S9 | [Andres, Graebner and Ott, *Phys. Rev. Lett.* 35, 1779 (1975)](https://doi.org/10.1103/PhysRevLett.35.1779) | abstract | CeAl3 below 0.2 K: γ = 1620 mJ/mol K². |
| S10 | [Elsayed-Ali, Norris, Pessot and Mourou, *Phys. Rev. Lett.* 58, 1212 (1987)](https://doi.org/10.1103/PhysRevLett.58.1212) | abstract | Electron–phonon energy transfer in copper films: 1–4 ps, increasing with fluence. |
