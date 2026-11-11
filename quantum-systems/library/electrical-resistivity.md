---
id: electrical-resistivity
title: Electrical Resistivity and Joule Heating
status: formal
family: ensemble-averages
constraints:
  - thermal
  - spatial-buffer
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
review_depth: deep
related:
  - skin-effect
  - electrical-contacts
  - melting
  - electron-heat-capacity
  - thermal-conductivity-phonon
  - superconductivity
updated: 2026-11-12
---

# Electrical Resistivity and Joule Heating

### 4.1 Effect Name

Electrical resistivity and Joule heating

### 4.2 Macroscopic Observation

A steady current through a metal bar produces a voltage drop proportional to the current. Scaled by the bar's length and cross-section, the ratio is the same for every bar of that metal at that temperature: the resistivity. It rises as the metal is heated, steps up when the metal melts, and in some metals falls below measurement at a low transition temperature. The current heats the conductor. A pressed metal powder can have a resistivity many orders of magnitude above the solid metal and can lose most of the excess when it is heated in a reducing gas.

### 4.3 Established Quantitative Boundaries

Bulk solid metals:

- **Measured.** Critically evaluated resistivity of annealed, high-purity metals, in 10⁻⁸ Ω·m (copper 99.999 %, aluminium and tungsten 99.99 % or purer; iron about ±2 %):

  | Metal | 273 K | 293 K | 300 K | Key |
  |---|---|---|---|---|
  | Ag | 1.467 | 1.587 | 1.629 | [S1] |
  | Cu | 1.543 | 1.678 | 1.725 | [S1] |
  | Al | 2.417 | 2.650 | 2.733 | [S3] |
  | W | 4.82 | 5.28 | 5.44 | [S5] |
  | Ni | 6.16 | 6.93 | 7.20 | [S4] |
  | Fe | 8.57 | 9.61 | 9.98 | [S4] |

  The first column is 273.15 K for silver and copper.
- **Computed here.** Temperature coefficient at 293 K, taken as the slope between the 273 K and 300 K rows divided by the 293 K value: Ag 0.0038, Cu 0.0040, W 0.0043, Al 0.0044, Fe 0.0054, Ni 0.0056 K⁻¹.
- **Convention.** Standard annealed copper (IACS) is defined as 58 m Ω⁻¹ mm⁻² at 20 °C, or 1.7241 µΩ·cm, with a temperature coefficient of 0.00393 per °C at 20 °C [S2]. Conductor-grade aluminium is listed at 2.86 µΩ·cm and 0.00403 per °C [S6].
- **Computed here.** Pure copper at 293 K has a conductivity of \(5.96\times10^{7}\) S m⁻¹, 2.7 % above the IACS value.
- **Convention.** Low-carbon steel in a design standard: steel 1020 at 15.90 µΩ·cm and 20 °C, 10.8 % IACS, fusing temperature 1510 °C, coefficient 0.00160 per °C [S6]. A vendor sheet gives 14.3 µΩ·cm for cold-drawn AISI 1010 (tertiary) [S7]. The standard's coefficient is far below that of pure iron above and is a constant of the standard's fusing formula. No measured coefficient for a low-carbon steel was found in a primary source.
- **Computed here.** 14.3–15.9 µΩ·cm is 8.3–9.2 times IACS copper.
- **Model (Bloch–Grüneisen).** The phonon part of the resistivity is \(\rho_i(T) = (C/M\Theta)(T/\Theta)^5J_5(\Theta/T)\): proportional to \(T\) well above the Debye temperature \(\Theta\) and to \(T^5\) well below it. The formula is derived for a monovalent metal with a spherical Fermi surface and a Debye spectrum, and real metals deviate from it [S1][S8].
- **Model (Matthiessen's rule).** \(\rho(c,T) = \rho_0(c) + \rho_i(T)\): a temperature-independent residual term from impurities and defects plus the intrinsic term. Deviations from the rule are measured [S1].
- **Convention.** The residual resistivity ratio is \(\rho(300\,\mathrm{K})/\rho(4.2\,\mathrm{K})\) [S8]; other authors put 273 K or 293 K in the numerator [S1].
- **Measured.** Residual resistivity ratios: oxygen-free copper about 100 [S8] to 400 [S9]; single data sets for copper up to 4710 [S1]; aluminium with \(\rho_0\) of order 10⁻¹² Ω·m approaches 27000 [S3].
- **Measured.** In iron and nickel the resistivity rises steeply to the Curie temperature and its slope changes there: iron reaches \(101.1\times10^{-8}\) Ω·m at 1043 K and nickel \(28.7\times10^{-8}\) Ω·m at 630 K [S4].

Melting and the liquid:

- **Measured.** Resistivity at the melting point, in 10⁻⁸ Ω·m, from the evaluated tables [S1][S3][S4][S5], beside solid and liquid values from exploding 0.1 mm wires in µΩ·cm [S13]:

  | Metal | \(T_m\) (K) | Solid | Liquid | Ratio | Exploding wire | Ratio |
  |---|---|---|---|---|---|---|
  | Cu | 1357.6 | 10.171 | 21.01 | 2.07 | 9.9 → 18.9 | 1.91 |
  | Ag | 1235.08 | 8.415 | 17.30 | 2.06 | 8.6 → 15.9 | 1.85 |
  | Al | 933.52 | 10.565 | 24.77 | 2.34 | 11.2 → 23.1 | 2.06 |
  | Ni | 1728 | 60.2 | 82.2 | 1.37 | 59.2 → 79.6 | 1.34 |
  | Fe | 1811 | 128.2 | 135.2 | 1.055 | 119.2 → 123.6 | 1.04 |
  | W | 3660 | 120.8 | 131 | 1.08 | 90.3 → 116.1 | 1.29 |

  The copper and silver ratios are tabulated in [S1]. The liquid values for copper and nickel are provisional (5–6 % and ±10 %). The aluminium solid value is corrected for thermal expansion; uncorrected it is 10.74. The two sources disagree for tungsten.
- **Computed here.** The other ratios in the table, and 2.31 for aluminium on the uncorrected solid value.
- **Measured.** Liquid copper follows \(\rho = 21.01 + 0.009929\,(T - 1357.6)\) in 10⁻⁸ Ω·m [S1]. Liquid aluminium reaches 39.34 and liquid iron 138.2 at 2000 K [S3][S4].
- **Model (Mott).** \(\rho_L/\rho_S = \exp(80L_F/T_m)\), with \(L_F\) in kJ mol⁻¹: 2.16 for copper and 2.08 for silver against the measured 2.07 and 2.06, and within about 15 % for Cu, Au, Pd and Ag. The source calls the theory crude; Mott's paper was not opened [S1].

Heat and charge together:

- **Model (Sommerfeld free-electron gas).** Wiedemann–Franz law: \(\kappa/\sigma = LT\) with \(L_0 = 2.443\times10^{-8}\) V² K⁻² [S10]; quoted as 2.44 [S11] and 2.45 [S8].
- **Measured.** The Lorenz ratio is 2.2–3.0 × 10⁻⁸ V² K⁻² for many pure metals at room temperature, near the Sommerfeld value at liquid-helium temperature, and furthest below it for the purest metals at 15–40 K [S10]. At 273 K it runs from 2.12 (Na) to 2.90 (Nb) [S11]. A tertiary table that does not state the temperature gives Cu 2.23, Ag 2.31, Au 2.35 [S12]. No per-metal value for iron or tungsten was found in an opened primary.
- **Computed here.** Those extremes are 13 % below and 19 % above \(L_0\); the tertiary copper value is 9 % below.

Joule heating:

- **Convention.** The specific action is \(g = (1/A^2)\int I^2\,dt = \int J^2\,dt\). The energy density deposited is the integral of resistivity over specific action, so the resistivity and phase of a uniformly heated wire are approximately functions of \(g\) alone [S13].
- **Measured.** Specific action of 0.1 mm wires in the slow exploding-wire regime, in 10¹⁶ A² s m⁻⁴ [S13]:

  | Metal | Melting begins | Melting complete | Burst |
  |---|---|---|---|
  | Cu | 8.05 | 9.42 | 17.3 |
  | Ag | 6.17 | 7.18 | 11.2 |
  | Al | 2.52 | 3.20 | 6.58 |
  | W | 2.43 | 2.78 | 7.51 |
  | Ni | 1.72 | 2.12 | 5.60 |
  | Fe | 1.28 | 1.47 | 3.61 |

  Burst is the point of peak resistance. It is not a material constant: at very high current density the action at burst increases [S13]. A 2013 exploding-wire study reports disagreement with these copper and aluminium values; it was seen only as a search excerpt [S14].
- **Computed here.** The table is converted from the source's A² s mm⁻⁴ (copper 80492, 94228 and 173000). Copper takes 6.3 times the action of iron to reach melting. Burst is 2.1 times the melt-onset action in copper, 2.6 in aluminium and 2.8 in iron.
- **Computed here.** At a constant current density of 10¹⁰ A m⁻² (10 kA mm⁻²), melting begins after \(g/J^2\) = 0.81 ms in copper, 0.25 ms in aluminium and 0.13 ms in iron. To begin melting within 0.2–0.7 ms takes 20–11 kA mm⁻² in copper and 8.0–4.3 kA mm⁻² in iron.
- **Model (adiabatic fusing, as used in IEEE Std 80).** With constant volumetric heat capacity, resistivity linear in temperature, uniform current density and no heat loss [S15], \(\int J^2\,dt = (\mathrm{TCAP}/\alpha_r\rho_r)\ln[(K_0 + T_m)/(K_0 + T_a)]\). The closed form is derived here from those assumptions; the standard's own equation was not opened.
- **Computed here.** With the standard's constants for steel 1020 (TCAP 3.28 J cm⁻³ °C⁻¹, \(\alpha_r\) 0.00160, \(\rho_r\) 15.90 µΩ·cm, \(K_0\) 605, 20 °C to 1510 °C) [S6] the model gives \(1.57\times10^{16}\) A² s m⁻⁴, 23 % above the measured value for pure iron wire. It uses the coefficient flagged above. The source check obtained \(8.33\times10^{16}\) for copper and \(2.83\times10^{16}\) for conductor-grade aluminium from the same table, 3 % and 12 % above the wire values; those constants are not reproduced here. No measured specific action to melt was found for any steel; pure iron wire is the nearest measured value.
- **Model (author's statement; basis not given in the text opened).** Copper rails reach the melting temperature at 44 kA per millimetre of rail height and tungsten rails at 56 kA mm⁻¹ [S16].

Size, grains and powders:

- **Model (free-electron estimate from measured conductivity).** Mean free path in copper at room temperature: 39 nm with a scattering time of \(2.46\times10^{-14}\) s [S9]; about 40 nm [S8][S17]; \(\rho_0\Lambda_0 = 6.6\times10^{-16}\) Ω·m² [S17].
- **Model (Fuchs–Sondheimer; Mayadas–Shatzkes).** A film of thickness \(d\) has \(\rho = \rho_0[1 + (3/8)(\Lambda_0/d)(1 - p)]\) in the thick-film form, with \(p\) the fraction of specular surface reflections. Grain boundaries add a term governed by \(\alpha = (\Lambda/d_\mathrm{grain})\,R/(1 - R)\). Measured copper films rise faster than the surface term with \(p = 0\) predicts [S17].
- **Computed here.** At \(d = \Lambda_0\) and \(p = 0\) the surface term adds 37.5 %, at the edge of the thick-film form's validity.
- **Model (Montes et al.).** A powder compact of porosity \(\Theta\) has \(\rho_E = \rho_\mathrm{res}(1 - \Theta/\Theta_M)^{-n}\), which diverges at the tap porosity \(\Theta_M\). Without oxide \(n = 3/2\), the percolation exponent, with the tap density as the percolation bound; oxide films raise the fitted \(n\) to between 1.5 and 3.6 [S18].
- **Measured.** As-received powders extrapolated to zero porosity keep a residual resistivity of \(1.6\times10^{-5}\) Ω·m (Al), \(2.3\times10^{-6}\) (Fe), \(1.0\times10^{-6}\) (Ni) and \(1.88\times10^{-7}\) (bronze). Against the dense values in the same paper these are about 550, 19, 12 and 1.01 times [S18].
- **Computed here.** Against the pure-metal values in the first table the same residuals are 600, 24 and 14 times for Al, Fe and Ni.
- **Measured.** Copper. Pressed compacts of −149 µm powder at 76–80 % density start near 10⁴–10⁵ Ω·m at room temperature and fall to 10⁻⁵–10⁻⁶ Ω·m, the floor of the plot, once the oxide is reduced. The fall is sharp at about 190–210 °C in forming gas. Both figures were read from the paper's graph [S19]. The oxide film on the particles is 850–1050 nm at the start, and the indicative film thickness falls from 1 µm or more to below 1 nm during heating [S21]. Copper powder under uniaxial pressure up to 30 N mm⁻² has a resistance controlled by the oxide layer on the grains and following a power law in pressure [S20]. No measured resistivity was found for loose, unpressed copper powder, for copper powder in oil or paste, or for a conditioned slug.
- **Computed here.** The unreduced compact is \(6\times10^{11}\) to \(6\times10^{12}\) times bulk copper. The reduced compact, at the floor of the plot, is at most 60–600 times bulk.

The sharp collapse:

- **Measured.** Mercury, 1911: the transition is at 4.20 K. Just above 4.2 K the resistance was 10⁻⁵ of its value at 0 °C, and it rose by a factor of almost 400 within the next 0.1 K. The original reports were not opened [S22].

**Data confidence:** High for the bulk solid and liquid resistivities, which come from critically evaluated tables read in full. Medium for the action values: one 1975 data set on 0.1 mm wires, with a later disagreement seen only as a snippet [S14]. Medium for powders: the copper-compact figures were read from a graph and span an order of magnitude. Low-carbon steel rests on a design standard and a vendor sheet. The copper and silver Lorenz ratios are tertiary. Not found: action to melt for steel, and any resistivity for loose or oil-borne copper powder.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Matthiessen's rule and the Bloch–Grüneisen intrinsic term [S1]:

  \[
  \rho(c,T) = \rho_0(c) + \rho_i(T),\qquad \rho_i(T) = \frac{C}{M\Theta}\left(\frac{T}{\Theta}\right)^{5}J_5\!\left(\frac{\Theta}{T}\right)
  \]

- Wiedemann–Franz law: \(\kappa/\sigma = LT\), \(L_0 = 2.443\times10^{-8}\) V² K⁻² [S10].
- Joule heating in terms of specific action [S13]:

  \[
  g = \int J^2\,dt,\qquad e = \int \rho\,dg
  \]

- Mott's melting ratio: \(\rho_L/\rho_S = \exp(80L_F/T_m)\) [S1].
- Thin-film surface term: \(\rho = \rho_0[1 + (3/8)(\Lambda_0/d)(1 - p)]\) [S17].
- Powder compact: \(\rho_E = \rho_\mathrm{res}(1 - \Theta/\Theta_M)^{-n}\) [S18].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Statistical. Resistivity is an average over many scattering events of many carriers, and the bulk value holds when every dimension of the conductor and of its grains is large against the mean free path: 39–40 nm in copper at room temperature. Below that the value rises continuously. A granular body has a second requirement, a connected path through the particle contacts, which exists only on the dense side of the tap porosity and only where the surface films conduct.

- **Clock rate / latency.** Two clocks. The scattering time, \(2.46\times10^{-14}\) s in copper at 293 K, is the averaging window of the carriers. The heating clock is the action integral: at a fixed current density the time to the start of melting is \(g/J^2\), 0.81 ms for copper at 10 kA mm⁻².

- **Energy barriers or thresholds.** None in the bulk metal. Conduction is a driven dissipative average and holds no state. Three gates that belong to other entries appear here as steps in the resistivity: the latent heat at [melting](melting.md), the oxide film at a powder contact ([electrical-contacts](electrical-contacts.md)), and the gap of a [superconductor](superconductivity.md).

- **Dominant failure modes.** Failure here means the point where the bulk room-temperature constant stops describing the conductor.
  - **Crossover** — temperature: \(\rho = \rho_0 + \rho_i(T)\), with \(\rho_i \propto T\) above the Debye temperature and \(T^5\) well below it. Near 293 K the rise is 0.4 % per kelvin in Ag, Cu, Al and W and 0.54–0.56 % in Fe and Ni. Iron and nickel have a change of slope at the Curie temperature with no step.
  - **Threshold** — melting: at \(T_m\) the resistivity steps up by 2.07 in copper, 2.06 in silver, 2.34 in aluminium, 1.37 in nickel and 1.055 in iron. A first-order transition.
  - **Threshold** — Joule heating to melt: the action integral rises continuously and the conductor begins to melt when it reaches \(8.05\times10^{16}\) A² s m⁻⁴ in copper or \(1.28\times10^{16}\) in iron. One data set.
  - **Threshold** — burst: 2.1–2.8 times the melt-onset action in the wire data, and dependent on the rate of heating, so the number is not a material constant.
  - **Crossover** — size: \(\rho/\rho_0 = 1 + (3/8)(\Lambda_0/d)(1 - p)\), with scale \(\Lambda_0 = 40\) nm in copper. Grain boundaries add to it.
  - **Threshold** — percolation in a powder body: \(\rho_E \propto (1 - \Theta/\Theta_M)^{-n}\) diverges at the tap porosity. On the dense side of that bound the dependence on porosity is a continuous power law with \(n\) between 1.5 and 3.6.
  - **Threshold** — oxide state of a powder body: a pressed copper compact goes from 10⁴–10⁵ Ω·m to 10⁻⁵–10⁻⁶ Ω·m or less at about 190–210 °C in forming gas. Under pressure alone the change is a power law, a crossover.
  - **Threshold** — superconducting transition: in mercury the resistance collapses within about 0.1 K at 4.2 K. This is the one sharp collapse of resistivity to zero, and it is owned by [superconductivity](superconductivity.md).

- **Emergent constant or stable output.** An intensive constant \(\rho(T)\) that does not depend on the shape of the sample above the mean-free-path scale; a heating rate \(\rho J^2\) per unit volume; and a ratio to the thermal conductivity that stays within about −13 % to +19 % of \(L_0T\) at 273 K for the metals tabulated.

### 4.6 Internal Consistency Notes

For a bulk metal the mapping closes as an ensemble average: the statistical buffer is the mean free path, the clock is the scattering time, and there is no barrier. The family's collapse, too few independent contributors, appears as the size effect, and it is a crossover.

Most of the thresholds listed in §4.5 belong to other entries. This entry records what the resistivity does at the melting point, at the superconducting transition and at an oxide film; it does not own those gates, and their numbers must not be equated with one another. [Skin effect](skin-effect.md) consumes this entry's constant through the magnetic diffusivity \(\rho/\mu\).

Four gaps remain.

1. The Bloch–Grüneisen form is derived for a special model and Matthiessen's rule has measured deviations, so \(\rho_0 + \rho_i(T)\) is a description of the data and not a node rule.
2. The Lorenz ratio deviates from the Sommerfeld value by up to about 20 % at ordinary temperatures, and falls furthest below it at 15–40 K in the purest metals. Charge transport and heat transport are two averages over the same carriers, and this entry does not reduce the difference to a buffer or clock. The carriers' heat capacity is in [electron-heat-capacity](electron-heat-capacity.md); the lattice's share of the heat current is in [thermal-conductivity-phonon](thermal-conductivity-phonon.md).
3. The resistivity of a powder body is set by its contacts and their films, which this entry treats only through a fitted residual resistivity and exponent. No value was found for loose or oil-borne copper powder. The measured copper compacts lie either about twelve orders of magnitude above bulk or, once reduced, at an upper bound of 60–600 times bulk.
4. The action integral is local. Under a pulse the current occupies a layer near the surface, and the current density that enters \(g\) is that of the layer, not the total current over the full cross-section. The adiabatic fusing model assumes uniform current density.

This entry was written to the sourcing standard; there is no unsourced first version to correct.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the bulk constant maps cleanly onto a statistical buffer and an averaging clock, but the thresholds are borrowed from other entries, the powder case is not reduced to a contact specification, and the Lorenz deviations are recorded without being accounted for.

## Related entries

- [Skin effect](skin-effect.md) — uses \(\rho\) through the magnetic diffusivity; sets the layer in which a pulse current heats
- [electrical-contacts](electrical-contacts.md) — the films and constrictions that set the resistance of a powder body
- [Melting](melting.md) — owns the transition at which the resistivity steps
- [electron-heat-capacity](electron-heat-capacity.md) — the same carriers as a heat reservoir
- [thermal-conductivity-phonon](thermal-conductivity-phonon.md) — the lattice channel of heat flow; the electronic channel follows this entry through the Lorenz ratio
- [Superconductivity](superconductivity.md) — the threshold at which resistivity collapses

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Matula, *J. Phys. Chem. Ref. Data* 8, 1147 (1979)](https://srd.nist.gov/jpcrdreprint/1.555614.pdf) | full-text | Copper and silver resistivity, solid and liquid; melting ratios; Bloch–Grüneisen and Matthiessen forms; residual ratios; Mott's formula (Mott's paper and the review by Bass were not opened). |
| S2 | [*Copper Wire Tables*, National Bureau of Standards Handbook 100 (1966)](https://nvlpubs.nist.gov/nistpubs/Legacy/hb/nbshandbook100.pdf) | full-text | IACS definition and the 0.00393 per °C coefficient. |
| S3 | [Desai, James and Ho, *J. Phys. Chem. Ref. Data* 13, 1131 (1984)](https://srd.nist.gov/jpcrdreprint/1.555725.pdf) | full-text | Aluminium resistivity, solid and liquid; residual ratio approaching 27000. |
| S4 | [Ho et al., "Electrical Resistivity of Ten Selected Binary Alloy Systems", *J. Phys. Chem. Ref. Data* 12, 183 (1983)](https://srd.nist.gov/jpcrdreprint/1.555684.pdf) | full-text | Pure iron and pure nickel columns of Table 9: room temperature, Curie point, melting and liquid values. Read from the page image. |
| S5 | [Desai, Chu, James and Ho, "Electrical Resistivity of Selected Elements", *J. Phys. Chem. Ref. Data* 13, 1069 (1984)](https://srd.nist.gov/jpcrdreprint/1.555723.pdf) | full-text | Tungsten resistivity, solid and at melting. |
| S6 | [IEEE Std 80-2000, *Guide for Safety in AC Substation Grounding*, Table 1 (single-page copy)](https://satcon.in/public/tech_info/1583400418.pdf) | full-text | Steel 1020 and conductor-grade aluminium constants. Secondary copy of a design standard. |
| S7 | [Elgin Fasteners, "Carbon Steel Grade 1010 Data Sheet"](https://www.mwcomponents.com/uploads/Resource-Center/Elgin-Material-Sheets/Carbon-Steel-Grade-1010-Data-Sheet_Elgin-Fasteners.pdf) | full-text | Tertiary vendor value: AISI 1010 at 14.3 µΩ·cm. |
| S8 | [Calatroni, "Materials & Properties: Thermal & Electrical Characteristics", CERN Accelerator School 2017, arXiv:2006.02842](https://arxiv.org/abs/2006.02842) | full-text | Temperature limits of the phonon resistivity; definition of the residual resistivity ratio; mean free path about 40 nm; Lorenz number quoted as 2.45. |
| S9 | [Ratzinger and Wang, "The anomalous skin effect and copper cavity operation at cryogenic conditions", arXiv:2211.00135](https://arxiv.org/abs/2211.00135) | full-text | Mean free path 39 nm and scattering time in copper at 293 K; residual ratio of 400 for oxygen-free copper. |
| S10 | [Hust and Lankford, "Thermal Conductivity of Aluminum, Copper, Iron, and Tungsten for Temperatures from 1 K to the Melting Point", NBSIR 84-3007 (1984)](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir84-3007.pdf) | full-text | Sommerfeld Lorenz number 2.443e-8; measured range 2.2–3.0e-8 at room temperature; behaviour at low temperature. |
| S11 | [Pizzochero, "Two Wrongs Make One Right", arXiv:2510.04962](https://arxiv.org/abs/2510.04962) | full-text | Lorenz number 2.44e-8; values at 273 K from 2.12 (Na) to 2.90 (Nb). Secondary; values from Ashcroft and Mermin. |
| S12 | [HyperPhysics, "Thermal Conductivity" table](http://hyperphysics.phy-astr.gsu.edu/hbase/Tables/thrcn.html) | full-text | Tertiary: Lorenz ratios of Cu, Ag and Au; temperature not stated. |
| S13 | [Tucker and Toth, "EBW1: A Computer Code for the Prediction of the Behavior of Electrical Circuits Containing Exploding Wire Elements", Sandia SAND-75-0041 (1975)](https://www.osti.gov/servlets/purl/4229184) | full-text | Definition of specific action; action at melting and burst and wire resistivities for Cu, Ag, Al, W, Ni, Fe. Table read from the page image. |
| S14 | [Vanderburg et al., *IEEE Trans. Plasma Sci.* 41, 2427 (2013)](https://doi.org/10.1109/TPS.2013.2266900) | snippet | Reports disagreement with the 1975 copper and aluminium action values. |
| S15 | [IEEE PCIC 2022 conference paper 0514](https://ieeepcic.com/2022conference/wp-content/uploads/sites/7/2022/09/2022-PCIC-0514.pdf) | full-text | Assumptions behind the adiabatic fusing equation of IEEE Std 80. Secondary. |
| S16 | [McNab, *IEEE Trans. Magn.* 39, 295 (2003), hosted copy](https://research.lifeboat.com/ieee.em.pdf) | full-text | Rail melting at 44 kA/mm for copper and 56 kA/mm for tungsten. |
| S17 | [Shen et al., "Studies of two-dimensional MoS2 on enhancing the electrical performance of ultrathin copper films", arXiv:1810.06772](https://arxiv.org/abs/1810.06772) | full-text | Thin-film surface and grain-boundary forms; 40 nm mean free path; measured films above the surface-scattering prediction. Secondary for Fuchs (1938), Sondheimer (1952) and Mayadas and Shatzkes (1970), which were not opened. |
| S18 | [Montes et al., "Electrical Resistivity of Powdered Porous Compacts", IntechOpen (2018)](https://www.intechopen.com/chapters/61188) | full-text | Compact resistivity law, percolation exponent, residual resistivities of Al, Fe, Ni and bronze powders. |
| S19 | [Mahmoud, Link, Jelonnek and Thumm, *EPJ Web of Conferences* 149, 02007 (2017)](https://publikationen.bibliothek.kit.edu/1000073655/4324720) | full-text | Pressed copper compacts before and after oxide reduction; drop at 190–210 °C in forming gas. Values read from Fig. 1. |
| S20 | [Creyssels, Falcon and Castaing, *AIP Conf. Proc.* 1145 (Powders and Grains 2009)](https://labo.msc.u-paris.fr/~falcon/AIP09.pdf) | full-text | Copper powder under uniaxial pressure: resistance controlled by the oxide layer, power law in pressure. |
| S21 | [Rybakov, Mahmoud and Link, "Analysis of microwave heating of copper powder compacts", KIT repository copy](https://publikationen.bibliothek.kit.edu/1000171474/153493249) | full-text | Oxide film thickness on copper powder and its fall during heating; percolation behaviour as the oxide decomposes. |
| S22 | [van Delft and Kes, "The discovery of superconductivity", *Physics Today* 63(9), 38 (2010)](https://aip.brightspotcdn.com/PTO.v63.i9.38_1.online.pdf) | full-text | Mercury transition at 4.20 K and the size of the resistance change. Secondary; Kamerlingh Onnes's 1911 reports were not opened. |
