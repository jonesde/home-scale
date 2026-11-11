---
id: melting
title: Melting (Loss of Lattice Order)
status: formal
family: lattice-modes
constraints:
  - thermal
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
review_depth: deep
related:
  - phonon-dispersion
  - elasticity
  - speed-of-sound
  - debye-cutoff
  - thermal-expansion
  - permanent-magnet-latch
  - ferroelectric-remanence
updated: 2026-11-13
---

# Melting (Loss of Lattice Order)

### 4.1 Effect Name

Melting (loss of lattice order)

### 4.2 Macroscopic Observation

A crystalline solid held at its melting temperature coexists with a liquid of the same composition and, with further heat, becomes liquid throughout. While both phases are present the temperature stays fixed, which is why freezing metals serve as temperature standards. The heat absorbed at constant temperature is the enthalpy of fusion. The liquid does not support a static shear stress and carries one sound wave where the solid carried two. The equilibrium temperature moves slowly with pressure. Small particles melt lower than the bulk, and a crystal whose surface is prevented from melting can be held briefly above the equilibrium temperature.

### 4.3 Established Quantitative Boundaries

Temperatures and heats:

- **Measured.** Melting points at one standard atmosphere, from critically evaluated tables: zinc 692.73 K, aluminium 933.45 K, copper 1358 K, nickel 1728 K, iron 1809 K [S1]. Tin, zinc, aluminium and copper freezing points define the temperature scale at 505.078, 692.677, 933.473 and 1357.77 K [S2][S3], and the triple point of water at 273.16 K [S3]. Tungsten: 3660 K in a critically evaluated resistivity table [S12] and 3695 K in a tertiary listing seen as a search excerpt [S16].
- **Measured.** Iron passes through three solid-state transitions before it melts: the Curie point at 1042 K, bcc to fcc at 1184 K and fcc to bcc at 1665 K. Nickel has its Curie point at 631 K [S1].
- **Measured.** Enthalpy relative to 298.15 K of the crystal at \(T_m\) and of the liquid at \(T_m\), in kJ mol⁻¹: Cu 29.660 and 42.798; Al 17.982 and 28.693; Fe 58.645 and 72.452; Ni 47.361 and 64.516; Zn 10.825 and 18.147. At 300 K the same quantity is 0.045 to 0.048 [S1].
- **Computed here.** Enthalpy of fusion, and the enthalpy to take the metal from 300 K to fully liquid at \(T_m\), from those entries. Molar masses and room-temperature densities are from [S4]; the volumetric figure is per cubic metre of cold solid.

  | Metal | \(T_m\) (K) | Fusion (kJ mol⁻¹) | Fusion (kJ kg⁻¹) | 300 K to liquid (kJ mol⁻¹) | 300 K to liquid (kJ kg⁻¹) | 300 K to liquid (GJ m⁻³) | Share that is fusion |
  |---|---|---|---|---|---|---|---|
  | Copper | 1358 | 13.14 | 207 | 42.75 | 673 | 6.03 | 31 % |
  | Aluminium | 933.45 | 10.71 | 397 | 28.65 | 1062 | 2.87 | 37 % |
  | Iron | 1809 | 13.81 | 247 | 72.41 | 1297 | 10.21 | 19 % |
  | Nickel | 1728 | 17.16 | 292 | 64.47 | 1098 | 9.78 | 27 % |
  | Zinc | 692.73 | 7.32 | 112 | 18.10 | 277 | 1.97 | 40 % |

- **Computed here.** Tin is not in those tables. Two heat-capacity points, 0.221 J g⁻¹ K⁻¹ at 273 K and 0.240 at 373 K [S5], extrapolated linearly to 505 K give about 50 kJ kg⁻¹ from 300 K to the melting point. A tertiary value of 7.0 kJ mol⁻¹ for the enthalpy of fusion [S6] is 59 kJ kg⁻¹. Together: about 109 kJ kg⁻¹, or 0.80 GJ m⁻³. This is an estimate.
- **Measured.** First-order character: a latent heat at fixed temperature [S1] and a liquid–solid plateau stable enough to realize a fixed point within about 0.1 mK [S2].

Pressure, size and kinetics:

- **Measured.** Pressure raises these melting points: by 3.3 (tin), 4.3 (zinc) and 7.0 (aluminium) \(\times 10^{-8}\) K Pa⁻¹ near one atmosphere [S2].
- **Computed here.** That is 3.3, 4.3 and 7.0 K per kilobar, or 7.1 mK per atmosphere for aluminium.
- **Measured.** Small particles. Gold particles down to 20 Å in diameter melt at temperatures that fall with size [S10]. For 2.5 nm gold the published value is 47 °C (320 K) after a theory-based correction and about 400 °C (673 K) uncorrected, against 1064 °C (1337 K) for the bulk [S11]. A separate electrochemical study finds transitions at 509 °C (782 K) for 4.1 nm and 132 °C (405 K) for 1.6 nm gold, with the depression roughly proportional to the inverse diameter [S11]. The original analysis needed a liquid surface layer about 6 Å thick in one of its two models [S10].
- **Measured.** Superheating. Silver spheres of about 130 µm coated with a continuous gold layer stayed solid at least 7.5 K above the melting point of silver for about one minute; without such a coating superheating is "usually only a few degrees or less". The duration was set by interdiffusion of the coating [S9].
- **Measured.** The liquid. Liquid tin at 240 °C and liquid zinc at 450 °C carry longitudinal sound at 2471 and 2780 m s⁻¹ [S14]. Transverse excitations exist in liquid gallium only at wavevectors above 9 nm⁻¹, with a lifetime of 0.5 ps and a range of 0.4–0.5 nm [S13].
- **Measured.** The crystal at its melting point still has a finite average shear modulus [S7]; an excerpt of a nine-metal study states that the shear modulus vanishes in the melt and not in the solid [S15].

Lindemann criterion:

- **Convention.** The criterion states that melting occurs when the root-mean-square thermal displacement reaches a fixed fraction, about one tenth, of the interatomic distance; it "is not very accurately fulfilled" [S7].
- **Measured and model.** Reported values of the ratio at melting span 0.12 to 0.19: 0.15–0.16 for face-centred cubic and 0.18–0.19 for body-centred cubic solids. Simulations of soft repulsive particles give 0.15 and 0.18 for the two structures [S8]. The ratio is not universal [S8].

**Data confidence:** High for the melting points and enthalpies of copper, aluminium, iron, nickel and zinc, which come from one critically evaluated set and agree with the temperature-scale fixed points to 0.3 K. Medium for tin (two heat-capacity points and a tertiary enthalpy of fusion) and for tungsten (two values 35 K apart, one seen only as an excerpt). The gold-particle numbers were read in a later paper that reports them; only the abstract of the original was opened. The ice point at one atmosphere and the Debye temperatures quoted in the first version were not found in an opened source.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Coexistence (Clapeyron): \(dT_m/dP = \Delta V/\Delta S\). A positive slope, as measured for tin, zinc and aluminium, means the liquid is less dense.
- Heat to melt from temperature \(T_0\): \(\int_{T_0}^{T_m}c_p\,dT + \Delta H_\mathrm{fus}\), tabulated above for \(T_0 = 300\) K.
- Lindemann: \(\sqrt{\langle u^2\rangle}/a \approx 0.1\)–0.19 at \(T_m\) [S7][S8].
- Size dependence: \(T_m(d) \approx T_m(\infty)(1 - c/d)\) to first order in inverse diameter [S11].

No equation in this entry produces a melting temperature from node-level quantities.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A crystal large enough for the bulk value to hold. The measured size dependence gives the scale: a 2.5 nm gold particle melts at a quarter to a half of the bulk absolute temperature, and the depression falls off as the inverse diameter, so micrometre powder is bulk for this purpose.

- **Clock rate / latency.** Melting is limited by heat supply and by nucleation at a surface. With the surface blocked, a crystal survived 7.5 K above \(T_m\) for a minute. No material clock is filed.

- **Energy barriers or thresholds.** Two numbers per material: the temperature \(T_m\) and the enthalpy of fusion. Reaching \(T_m\) is not sufficient; fusion is 19 % to 40 % of the heat needed from room temperature in the five metals tabulated.

- **Dominant failure modes.**
  - **Threshold** — thermal: at \(T_m\) for the given pressure the solid converts to liquid with a latent heat. The temperature moves 3 to 7 K per kilobar in tin, zinc and aluminium.
  - **Crossover** — size: \(T_m\) falls roughly as \(1/d\). Gold shows a transition at 58 % of the bulk absolute temperature at 4.1 nm and at 30 % at 1.6 nm.
  - **Crossover** — kinetic: superheating and supercooling are nucleation-limited and depend on time and surface condition; 7.5 K for a minute with the surface coated, a few degrees otherwise.
  - **Crossover** — non-thermal loss of order (heavy plastic strain, irradiation, dissolution): no measured scale filed.

- **Emergent constant or stable output.** A material constant \(T_m(P)\) reproducible to a fraction of a millikelvin in pure metals, and a fixed enthalpy of fusion.

### 4.6 Internal Consistency Notes

Filing melting under lattice-modes is consistent with the taxonomy: the solid's shear stiffness and long-range order end here.

Sourcing changed the entry in four ways. It now carries the energy budget, which the first version omitted: melting copper from room temperature takes 673 kJ kg⁻¹ and aluminium 1062 kJ kg⁻¹, a third of it at constant temperature. The shear modulus does not soften to zero on the way to \(T_m\); the crystal is still stiff at the transition and the liquid is not, so there is no soft-mode precursor in the sources opened, and a surface-blocked crystal can be carried past \(T_m\) without a lattice instability. The Lindemann ratio is wider (0.12–0.19) and structure-dependent, which weakens it further as anything more than a rule of thumb. And the liquid is not strictly free of shear response: transverse excitations survive over about half a nanometre and half a picosecond.

The comparison with Debye temperatures in the first version (lead, diamond) was dropped because no source for those numbers was opened here.

The mapping does not close on why a metal melts at its particular temperature. The melting points and enthalpies are data. This is the same open item as before, now with one fewer candidate: a vanishing phonon branch or shear modulus is not what the measurements show.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(T_m\), the enthalpy of fusion and the loss of static shear are sharp measured boundaries, but \(T_m\) is taken as an empirical threshold and is not obtained from a node-level barrier.

## Related entries

- [phonon-dispersion](phonon-dispersion.md) — mode map of the solid; no soft-mode precursor of melting was found
- [elasticity](elasticity.md) — shear modulus of the solid; impact bonding below \(T_m\)
- [speed-of-sound](speed-of-sound.md) — two waves in the solid, one in the liquid
- [debye-cutoff](debye-cutoff.md) — clock ceiling of the solid
- [thermal-expansion](thermal-expansion.md) — anharmonicity of the same wells, short of melting
- [permanent-magnet-latch](permanent-magnet-latch.md) — the Curie point lies below \(T_m\) in iron and nickel
- [ferroelectric-remanence](ferroelectric-remanence.md) — lattice loss as a secondary failure of an electrical latch

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST-JANAF Thermochemical Tables, 4th ed. (Chase, 1998): reference states of Cu, Al, Fe, Ni, Zn](https://janaf.nist.gov/tables/Cu-001.html) | full-text | Melting points; enthalpy of crystal and liquid at the melting point; enthalpy at 300 K; solid-state transitions of iron and nickel. |
| S2 | [BIPM, *Guide to the Realization of the ITS-90*, §2.4 Metal fixed points (2018)](https://www.bipm.org/utils/common/pdf/ITS-90/Guide_ITS-90_2_4_MetalFixedPoints_2018.pdf) | full-text | Freezing points of tin, zinc and aluminium in °C; pressure coefficients; reproducibility of the plateau. |
| S3 | [its-90.com, "ITS-90 Fixed Points"](https://its-90.com/fixed-points) | full-text | Tertiary: the defining fixed points in kelvin, including copper and the triple point of water. |
| S4 | [NIST, X-Ray Mass Attenuation Coefficients, Table 1](https://physics.nist.gov/PhysRefData/XrayMassCoef/tab1.html) | full-text | Densities and Z/A (hence molar mass) of Cu, Al, Fe, Ni, Zn, Sn. |
| S5 | [Kaye and Laby, *Tables of Physical and Chemical Constants*, §2.3.6 Specific heat capacities (NPL, archived)](https://web.archive.org/web/2019/http://www.kayelaby.npl.co.uk/general_physics/2_3/2_3_6.html) | full-text | Specific heat of tin at 273 K and 373 K. |
| S6 | [WebElements, "Tin: thermochemistry and thermodynamics"](https://winter.group.shef.ac.uk/webelements/tin/thermochemistry.html) | full-text | Tertiary: enthalpy of fusion of tin, 7.0 kJ/mol. |
| S7 | [Buchenau and Zorn, "A new view of the Lindemann criterion", arXiv:1311.4739](https://arxiv.org/abs/1311.4739) | full-text | Statement of the criterion (about one tenth, not accurately fulfilled); finite shear modulus of the melting crystal. |
| S8 | [Saija, Prestipino and Giaquinta, *J. Chem. Phys.* 124, 244504 (2006), arXiv:cond-mat/0605492](https://arxiv.org/abs/cond-mat/0605492) | full-text | Lindemann ratio 0.12–0.19, by structure; simulated values; non-universality. |
| S9 | [Däges, Gleiter and Perepezko, *MRS Proc.* 57, 67 (1985)](https://www.cambridge.org/core/journals/mrs-online-proceedings-library-archive/article/superheating-of-metallic-crystals/24FD3F9DE338433CD25086E9F17C0D66) | abstract | Gold-coated silver spheres superheated at least 7.5 K for about a minute. |
| S10 | [Buffat and Borel, *Phys. Rev. A* 13, 2287 (1976)](https://doi.org/10.1103/PhysRevA.13.2287) | abstract | Size-dependent melting of gold particles down to 20 Å; liquid-layer model. |
| S11 | [Mainali, Pattadar, Sharma et al., "Electrochemical analysis of the thermal stability of 0.9–4.1 nm diameter gold nanoclusters" (accepted manuscript)](https://par.nsf.gov/servlets/purl/10477166) | full-text | Secondary for the Buffat and Borel value at 2.5 nm, corrected and uncorrected; own transition temperatures at 4.1 and 1.6 nm; inverse-diameter trend; bulk gold 1064 °C. |
| S12 | [Desai et al., *J. Phys. Chem. Ref. Data* 13, 1069 (1984)](https://srd.nist.gov/jpcrdreprint/1.555723.pdf) | full-text | Tungsten: solid and liquid resistivity tabulated at a melting point of 3660 K. |
| S13 | [Hosokawa et al., *Phys. Rev. Lett.* 102, 105502 (2009)](https://doi.org/10.1103/PhysRevLett.102.105502) | abstract | Transverse acoustic excitations in liquid gallium: wavevector range, lifetime and propagation length. |
| S14 | [Kaye and Laby, §2.4.1 The speed and attenuation of sound (NPL, archived)](https://web.archive.org/web/2018/http://www.kayelaby.npl.co.uk/general_physics/2_4/2_4_1.html) | full-text | Sound speeds in liquid tin and zinc. |
| S15 | [Tallon, "The volume dependence of elastic moduli and the Born–Durand melting hypothesis" (1979)](https://scilit.com/publications/c7d8fe8bb71564cf1ea31b7b7c993670) | snippet | Shear modulus vanishing in the melt and not in the solid. |
| S16 | [WebElements, "Tungsten: thermochemistry and thermodynamics"](https://winter.group.shef.ac.uk/webelements/tungsten/thermochemistry.html) | snippet | Tertiary: tungsten melting point 3695 K. |
