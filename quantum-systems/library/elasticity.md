---
id: elasticity
title: Elasticity (Small-Strain Restoring Output)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
review_depth: deep
related:
  - speed-of-sound
  - phonon-dispersion
  - melting
  - piezoelectricity
  - magnetostriction
  - thermal-expansion
  - ferromagnetic-hysteresis
  - ferroelectric-domains
updated: 2026-11-11
---

# Elasticity (Small-Strain Restoring Output)

### 4.1 Effect Name

Elasticity (small-strain restoring output)

### 4.2 Macroscopic Observation

A solid loaded below its yield stress changes length or angle in proportion to the load and returns to its original shape when the load is removed. The constants of proportionality are the Young's, shear and bulk moduli. Above the yield stress a metal flows plastically and does not recover; the yield stress depends on grain size, on prior working and on how fast the load is applied. A liquid has a bulk modulus and no static shear modulus. Metal particles thrown at a metal surface rebound at low speed and bond to it above a critical speed, which is the basis of cold spray.

### 4.3 Established Quantitative Boundaries

Moduli and yield:

- **Measured.** Elastic constants at 20 °C, with the room-temperature yield constant \(A\) of the Johnson–Cook fit (the flow stress at zero plastic strain and a strain rate of 1 s⁻¹) [S1][S2]:

  | Metal | \(E\) (GPa) | \(G\) (GPa) | \(K\) (GPa) | \(A\) (MPa), material tested |
  |---|---|---|---|---|
  | Copper | 129.8 | 48.3 | 137.8 | 90, OFHC copper |
  | Aluminium | 70.3 | 26.1 | 75.5 | 265, 2024-T351 alloy; 337, 7039 alloy |
  | Nickel | 199.5 soft, 219.2 hard | 76.0, 83.9 | 177.3, 187.6 | 163, Nickel 200 |
  | Iron | 211.4 soft | 81.6 | 169.8 | 175, Armco iron |
  | Steel | 211.9 mild | 82.2 | 169.2 | 350, 1006 steel; 792, 4340 steel |
  | Titanium | 115.7 | 43.8 | 107.7 | not found |

  The bulk modulus of diamond is 542 GPa [S1].
- **Measured.** Tensile strengths: rolled aluminium 90–150 MPa; rolled copper 200–400 MPa; mild steel (0.2 % C) 430–490 MPa; annealed copper wire 280–310 MPa; nickel wire 500–900 MPa [S1]. Strength depends on the rate of loading and the temperature [S1].
- **Computed here.** Elastic strain at yield, \(A/E\): copper \(6.9 \times 10^{-4}\), Nickel 200 \(8.2 \times 10^{-4}\), Armco iron \(8.3 \times 10^{-4}\), 1006 steel \(1.65 \times 10^{-3}\), 4340 steel \(3.7 \times 10^{-3}\), 2024 aluminium \(3.8 \times 10^{-3}\). The linear window of these metals ends between 0.07 % and 0.4 % strain.
- **Model (Hall–Petch).** Refining the grain size raises the strength of a metal, and the increment follows \(\sigma_y = \sigma_0 + k\,d^{-1/2}\) with \(d\) the grain size; six decades of studies on pure metals support it [S3]. The coefficients \(k\) were not read: only the abstract of the survey could be opened.
- **Model (Johnson–Cook).** \(\sigma = [A + B\varepsilon^n][1 + C\ln\dot\varepsilon^*][1 - T^{*m}]\), with \(\dot\varepsilon^*\) the strain rate in units of 1 s⁻¹ and \(T^*\) the homologous temperature. Fitted rate constants \(C\): OFHC copper 0.025, Nickel 200 0.006, Armco iron 0.060, 1006 steel 0.022, 2024-T351 aluminium 0.015, 4340 steel 0.014 [S2]. Nickel 200 is "not very sensitive to strain rate" [S2].
- **Computed here.** Rate factor \(1 + C\ln\dot\varepsilon^*\) at \(10^{6}\) s⁻¹ and at \(10^{9}\) s⁻¹: copper 1.35 and 1.52; nickel 1.08 and 1.12; Armco iron 1.83 and 2.24; 1006 steel 1.30 and 1.46; 2024 aluminium 1.21 and 1.31; 4340 steel 1.19 and 1.29. This extrapolates a fit made up to about \(10^{3}\) s⁻¹; strain rates in cold spray are \(10^{6}\)–\(10^{9}\) s⁻¹ [S5][S6].
- **Model (density-functional calculation).** Ideal shear strength, the minimum stress that plastically deforms an infinite dislocation-free crystal: 1.85 GPa for aluminium and 2.65 GPa for copper on \(\{111\}\) planes, given as 8–9 % of the shear modulus used there [S4].
- **Computed here.** Against the polycrystal \(G\) of the table those strengths are 7.1 % (Al) and 5.5 % (Cu). The shear yield of OFHC copper is 45–52 MPa (half, or \(1/\sqrt3\), of 90 MPa), so the ideal strength is 51–59 times larger. For 2024 aluminium alloy the factor is 12–14.
- **Measured.** The crystal still has a finite average shear modulus at its melting point [S13]; the liquid has none at acoustic frequencies. An excerpt of a nine-metal study states that the shear modulus vanishes in the melt and not in the solid [S16]. The loss of \(G\) at \(T_m\) is a jump.

Impact bonding (cold spray):

- **Measured.** Particles of 10–40 µm are accelerated to 300–1200 m s⁻¹ and bond on impact while solid [S5]. Below a critical velocity they rebound or abrade the surface; above an erosion velocity deposition stops again; deposition occurs in the window between [S5][S6]. The critical velocity falls as the particle temperature rises and rises as the particle gets smaller [S6].
- **Convention.** For a powder, the critical velocity is the velocity at 50 % deposition efficiency [S5].
- **Measured.** Single particles show a discontinuity: the coefficient of restitution falls with speed and reaches zero at the critical velocity, where material is ejected from the rim [S7].
- **Measured and model.** Reported critical velocities:

  | Metal | Value (m s⁻¹) | Conditions | Source |
  |---|---|---|---|
  | Copper | 570 | gas-atomized powder, 5–22 µm, experiment | [S5] |
  | Copper | 500 | simulation: shear instability in a 15 µm particle, none in a 5 µm particle | [S6] |
  | Copper | 300 to 610 | powder oxygen 0.02 to 0.38 wt % | [S5] |
  | Copper | 460–500 | 20 µm, tabulated; not reopened | [S11] |
  | Aluminium | 825 and 775 | single particles of 14 µm and 30 µm on aluminium | [S7] |
  | Aluminium | 742 to 867 | powder oxygen 0.001 to 0.045 wt % | [S5] |
  | Aluminium | 620–660 | 20 µm, tabulated; not reopened | [S11] |
  | Titanium | 750 | calculated, 25 µm | [S5] |
  | Titanium | 690; 505–610 | angular powder from deposition efficiency; 29 µm spherical, measured | [S5] |
  | Titanium | 700–890 | 20 µm, tabulated; not reopened | [S11] |
  | Steel 316L | 700–750 | 20 µm, tabulated; not reopened | [S11] |
  | Nickel | not found | measured in [S7] but given only in a figure; aluminium needs a higher speed than nickel | [S7] |

- **Model (empirical fits).** Assadi et al. 2003: \(v_{cr} = 667 - 14\rho + 0.08\,T_m + 0.1\,\sigma_u - 0.4\,T_i\) (g cm⁻³, °C, MPa) [S12]. Schmidt et al. 2006: \(v_{cr} = \sqrt{F_1\,4\sigma_u\bigl(1 - \tfrac{T_i - T_R}{T_m - T_R}\bigr)/\rho + F_2\,c_p(T_m - T_i)}\) with \(F_1 = 1.2\), \(F_2 = 0.3\) and \(T_R = 293\) K; the erosion velocity uses \(F_1 = 4.8\), \(F_2 = 1.2\) [S10]. Both are quoted from a review [S5]. A later form uses constants 4 and 0.25 for typical powder size distributions [S6].
- **Computed here.** The erosion constants are four times the bonding constants, so the erosion velocity is 2.0 times the critical velocity in that model. With room-temperature particles and the tensile strengths above, the Schmidt formula gives 479–580 m s⁻¹ for copper (erosion from 958 m s⁻¹) and 573–659 m s⁻¹ for aluminium, using \(c_p\) and \(T_m\) from [S2] and [S15].
- **Model (adiabatic shear instability).** Finite-element simulations show a sudden rise of strain and temperature at the particle rim once thermal softening outruns strain and strain-rate hardening, and the onset speed matches measured critical velocities; bonding is attributed to this instability [S12][S6][S5]. Below a critical particle diameter heat conduction prevents it [S5][S6]. A review notes that how the instability produces bonding "is not clear" [S5].
- **Measured and model (the critics).** Single-particle experiments with simulation conclude that the interfacial strain needed for bonding does not require adiabatic shear instability, that jetting comes from the pressure wave released at the particle edge, and that the critical velocity is proportional to the bulk speed of sound: \(v_{cr} \approx 0.15\sqrt{K/\rho}\) for particles near 10 µm (0.14 in simulation), with negligible dependence on strength [S7][S8]. The original authors replied that the first claim is inaccurate, the second correct but not new, and the third incorrect [S9].
- **Computed here.** \(\sqrt{K/\rho}\) is 3920, 5290 and 4460 m s⁻¹ for copper, aluminium and nickel, so the 0.15 rule gives 588, 793 and 669 m s⁻¹ [S1][S14]. The aluminium figure agrees with the single-particle 775–825 m s⁻¹; the copper figure is close to the 570 m s⁻¹ powder value. The two accounts differ most on what should change the number: strength and temperature in one, sound speed in the other.

**Data confidence:** High for the moduli (one handbook, cross-checked against sound speeds in [speed-of-sound](speed-of-sound.md)). Medium for yield: the values are fit constants for particular lots. The cold-spray entries from Schmidt et al. 2006 and 2009 and Assadi et al. 2003 rest on a review and on the hardware project's reference list; none of the three primaries was opened. No nickel critical velocity and no titanium yield stress were found.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Hooke's law, \(\sigma_{ij} = C_{ijkl}\varepsilon_{kl}\). For an isotropic solid \(G = E/2(1+\nu)\) and \(K = E/3(1-2\nu)\) [S1].
- Wave speeds from the same constants: \(v_L = \sqrt{(K + 4G/3)/\rho}\), \(v_T = \sqrt{G/\rho}\).
- Yield: Hall–Petch for grain size and Johnson–Cook for rate and temperature, both empirical.
- Stored energy per volume \(\tfrac12C\varepsilon^2\), returned on unloading.

Nothing here computes a yield stress from the unit cell.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A mechanically coupled lattice for \(E\) and \(G\); a fluid suffices for \(K\). The linear moduli are bulk averages of the same springs that set the sound speed. The yield stress is set by a mesoscale population of dislocations and grain boundaries and scales as \(d^{-1/2}\) with grain size.

- **Clock rate / latency.** Elastic response follows the acoustic clock of [speed-of-sound](speed-of-sound.md). Plastic flow has its own rate dependence, logarithmic in strain rate over the fitted range.

- **Energy barriers or thresholds.** Small-strain elasticity is a restoring well and stores no state. Yield bounds the well at 0.07–0.4 % strain in the metals tabulated. The barrier crossed at yield belongs to dislocation motion and is measured as a stress.

- **Dominant failure modes.**
  - **Crossover** — stress: plastic flow sets in over a range of stress and the yield stress is a convention on a continuous curve. Scales: \(\sigma_0 + k\,d^{-1/2}\) with grain size; \(1 + C\ln\dot\varepsilon^*\) with rate, 1.1 to 1.8 at \(10^{6}\) s⁻¹.
  - **Threshold** — melting: the static shear modulus is finite in the crystal at \(T_m\) and zero in the liquid ([melting](melting.md)).
  - **Crossover** — amplitude: beyond the linear window the response is nonlinear and still reversible until yield.
  - **Crossover** — impact bonding of a powder: deposition efficiency rises through the critical velocity, defined at 50 %, and falls again at about twice that speed. For one particle of one size the rebound-to-adhesion change is a threshold.
  - **Threshold** — medium: a fluid has no static shear modulus.

- **Emergent constant or stable output.** Handbook moduli as the small-amplitude restoring output of the lattice, with a yield envelope that depends on material, history, grain size and rate.

### 4.6 Internal Consistency Notes

Reading the moduli and the sound speeds as two views of one set of springs is tight: the speeds computed from \(K\), \(G\) and density agree with the measured ones to better than 1 % for copper, aluminium and nickel.

Sourcing changed four things. The ideal strength is a computed number, 5–9 % of the shear modulus, in place of the unsourced \(E/10\); the gap to real yield is a factor of 12 to 59 for the two cases worked. The loss of shear stiffness at melting is a jump and the first version's "\(G \to 0\)" read as a continuous softening. The linear window is 0.07–0.4 % strain. Diamond's Young's modulus could not be sourced and its bulk modulus is given instead.

The impact-bonding material is new. It belongs here because the competing accounts differ on which elastic or plastic property sets the critical velocity. The mapping does not choose between them. Each makes a separate, checkable statement: one predicts that a stronger or colder particle needs more speed; the other predicts that only \(\sqrt{K/\rho}\) matters at fixed size. The measured rise of the critical velocity with powder oxide content sits outside both.

The mapping is incomplete at yield. The mesoscale step from lattice springs to dislocation motion is not reduced to a buffer or barrier number; it is the mechanical counterpart of the gap between coercivity and anisotropy field on [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md). Elastomers share the word and not this machine.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the moduli and their identity with the sound speeds map cleanly onto the lattice, but yield and impact bonding are set by mesoscale and dynamic processes whose governing quantity is still disputed in the literature.

## Related entries

- [speed-of-sound](speed-of-sound.md) — the same constants read as a long-wave slope
- [phonon-dispersion](phonon-dispersion.md) — finite-\(q\) extension of the same springs
- [melting](melting.md) — the jump of \(G\) to zero; enthalpy to melt
- [piezoelectricity](piezoelectricity.md) — strain coupled to polarization
- [ferroelectric-domains](ferroelectric-domains.md) — 90° walls switch this strain
- [magnetostriction](magnetostriction.md) — strain coupled to ordered moment; uses the nickel modulus and yield from this file
- [thermal-expansion](thermal-expansion.md) — anharmonic correction to these wells
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — analogue of the mesoscale threshold

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Kaye and Laby, *Tables of Physical and Chemical Constants*, §2.2.2 Elasticities and strengths (NPL, archived)](https://web.archive.org/web/2018/http://www.kayelaby.npl.co.uk/general_physics/2_2/2_2_2.html) | full-text | E, G, K and Poisson ratio of Cu, Al, Ni, Fe, steels, Ti; bulk modulus of diamond; tensile strengths; isotropic relations. |
| S2 | [Johnson and Cook, *Proc. 7th Int. Symp. on Ballistics*, The Hague (1983)](https://archive.org/details/AConstitutiveModelAndDataForMetals) | full-text | Constitutive form and Table 1: A, C, density, specific heat and melting temperature for OFHC copper, Nickel 200, Armco iron, 1006 and 4340 steel, 2024-T351 and 7039 aluminium. Table read from the page image. |
| S3 | [Cordero, Knight and Schuh, *Int. Mater. Rev.* 61, 495 (2016)](https://dspace.mit.edu/handle/1721.1/112642) | abstract | Hall–Petch scaling and its support in pure metals. Coefficients not read. |
| S4 | [Roundy, Krenn, Cohen and Morris, *Phys. Rev. Lett.* 82, 2713 (1999)](https://doi.org/10.1103/PhysRevLett.82.2713) | abstract | Ideal shear strengths of Al and Cu, 1.85 and 2.65 GPa, 8–9 % of the shear modulus. |
| S5 | [Hussain, *Key Eng. Mater.* 533, 53 (2013)](https://www.nottingham.ac.uk/research/groups/cse/documents/peer-reviewed-journal-papers-2016/8-cold-spraying-of-titanium-a-review-of-bonding-mechanisms-microstructure-and-properties.pdf) | full-text | Review: process window, definition at 50 % deposition efficiency, the Assadi 2003 and Schmidt 2006 formulas and erosion constants (secondary), copper 570 m/s, titanium values, oxide effect, strain rates, unclear link from instability to bonding. |
| S6 | [Assadi, Kreye, Gärtner and Klassen, "Cold spraying – a materials perspective", *Acta Mater.* (2016)](https://bura.brunel.ac.uk/bitstream/2438/13101/1/FullText.pdf) | full-text | Shear instability in simulations, size and temperature dependence, window of deposition, fit constants 4 and 0.25, strain rates to 10⁹ per second. |
| S7 | [Hassani-Gangaraj, Veysset, Nelson and Schuh, "Supersonic impact of metallic micro-particles", arXiv:1612.08081](https://arxiv.org/abs/1612.08081) | full-text | Single-particle critical velocities for Al; restitution discontinuity; the 0.15 (0.14) rule against bulk sound speed; strength independence. |
| S8 | [Hassani-Gangaraj, Veysset, Champagne, Nelson and Schuh, *Acta Mater.* 158, 430 (2018)](https://doi.org/10.1016/j.actamat.2018.07.065) | abstract | Claim that adiabatic shear instability is not necessary for adhesion. |
| S9 | [Assadi, Gärtner, Klassen and Kreye, *Scripta Mater.* 162, 512 (2019)](https://doi.org/10.1016/j.scriptamat.2018.10.036) | abstract | Reply disputing S8. |
| S10 | Schmidt, Gärtner, Assadi and Kreye, *Acta Mater.* 54, 729 (2006) | cited-only | Critical and erosion velocity formula; read through S5. |
| S11 | [Schmidt et al., *J. Therm. Spray Technol.* 18, 794 (2009)](https://doi.org/10.1007/s11666-009-9357-7) | cited-only | Tabulated critical velocities for 20 µm particles, as recorded in the hardware project's reference list (em-csam/References.md §5). Publisher page refused access. |
| S12 | Assadi, Gärtner, Stoltenhoff and Kreye, *Acta Mater.* 51, 4379 (2003) | cited-only | Original shear-instability account and linear formula; read through S5 and S6. |
| S13 | [Buchenau and Zorn, "A new view of the Lindemann criterion", arXiv:1311.4739](https://arxiv.org/abs/1311.4739) | full-text | Finite average shear modulus of the crystal at its melting point. |
| S14 | [NIST, X-Ray Mass Attenuation Coefficients, Table 1 (element densities)](https://physics.nist.gov/PhysRefData/XrayMassCoef/tab1.html) | full-text | Densities of Cu, Al and Ni used for the bulk sound speeds. |
| S15 | [NIST-JANAF Thermochemical Tables, 4th ed., copper and aluminium reference states](https://janaf.nist.gov/tables/Cu-001.html) | full-text | Melting temperatures used in the Schmidt-formula arithmetic. |
| S16 | [Tallon, "The volume dependence of elastic moduli and the Born–Durand melting hypothesis" (1979)](https://scilit.com/publications/c7d8fe8bb71564cf1ea31b7b7c993670) | snippet | Shear modulus vanishing in the melt and not in the solid, for nine metals. |
