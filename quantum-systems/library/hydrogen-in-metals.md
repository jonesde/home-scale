---
id: hydrogen-in-metals
title: Hydrogen in Metals (Solubility, Hydride Formation, Trapping)
status: formal
family: latched-order
constraints:
  - thermal
  - energy-barrier
  - mechanical-lattice
  - spatial-buffer
confidence_data: medium
confidence_mapping: medium
review_depth: deep
related:
  - elasticity
  - melting
  - magnetostriction
  - superparamagnetism
  - ferromagnetic-hysteresis
  - electrical-resistivity
updated: 2026-11-11
---

# Hydrogen in Metals (Solubility, Hydride Formation, Trapping)

### 4.1 Effect Name

Hydrogen in metals: interstitial solubility, hydride formation, and trapping at defects

### 4.2 Macroscopic Observation

A metal held in hydrogen gas takes hydrogen into its lattice as atoms, in an amount that rises with the square root of the gas pressure while the concentration is low. Some metals (palladium, titanium) take up a large fraction of a hydrogen atom per metal atom near room temperature and swell by several percent; others (nickel, iron, copper) take up parts per million. In palladium the uptake at fixed temperature jumps at a plateau pressure, and the pressure at which the hydrogen leaves is lower than the pressure at which it entered. After the gas is removed, part of the hydrogen stays in the metal and is released on heating, in peaks at characteristic temperatures. Hydrogen-charged high-strength metals can fracture at reduced stress.

### 4.3 Established Quantitative Boundaries

Dilute solubility:

- **Model (ideal dilute solution; Sieverts' law).** The lattice concentration is \(c = K_S(T)\sqrt{p}\), with \(K_S = S_0 e^{-E_S/RT}\). It holds at low concentration, and at high pressure the fugacity replaces \(p\) [S2]. It gives the lattice concentration only: at lower temperatures hydrogen segregates to defects, and the total is the sum of lattice and defect hydrogen [S2].
- **Measured.** Gas-phase permeation, 560–1000 K: nickel \(S = 2.2\times10^{-6}e^{-10.8\,\mathrm{kJ}/RT}\) and copper \(S = 1.4\times10^{-5}e^{-37.6\,\mathrm{kJ}/RT}\), in mol H₂ per mol metal per Pa^1/2 [S1]. Iron, 500–900 K: \(S = 180.1\,e^{-23.66\,\mathrm{kJ}/RT}\) mol H₂ m⁻³ MPa^-1/2 [S2]. In all three the heat of solution is positive and solubility rises with temperature; iron and nickel have low solubility at ambient temperature and pressure [S19].
- **Computed here.** H/M at 1 bar from those fits, ideal gas, with the iron molar volume 7.09 cm³ mol⁻¹ [S30]. The 298 K column lies below the measured temperature range of every fit and is an extrapolation.

  | Metal | H/M at 298 K | H/M at 573 K |
  |---|---|---|
  | Ni | \(1.8\times10^{-5}\) | \(1.4\times10^{-4}\) |
  | Fe | \(5.7\times10^{-8}\) | \(5.6\times10^{-6}\) |
  | Cu | \(2.3\times10^{-9}\) | \(3.3\times10^{-6}\) |

  Other values for 298 K: nickel 0.00005 wt %, which is H/Ni \(2.9\times10^{-5}\) (tertiary, pressure not stated) [S16]; iron about \(2\times10^{-8}\) at 0.1 MPa (search snippet only) [S33]. The primary solid solution of nickel is quoted as NiH\(_x\) with \(x \approx 0.01\) near ambient conditions, which is a phase limit and not the 1 bar equilibrium [S15].
- **Computed here.** Nickel at 298 K by the same fit: H/Ni is \(8.0\times10^{-5}\) at 20 bar, \(1.3\times10^{-4}\) at 50 bar and \(3.1\times10^{-4}\) at 300 bar. By mass these are 0.31 wt ppm at 1 bar and 5.3 wt ppm at 300 bar. One gram of nickel at 300 bar holds 2.6 µmol of H₂; in a 1 cm³ gas space holding 12.1 mmol that is a pressure drop of 0.065 bar. No fugacity correction was applied.
- **Measured.** Palladium equilibrated with 1 atm H₂ at room temperature holds H/Pd = 0.68 [S3]; a tertiary source gives about 0.7 [S4].
- **Computed here.** That is \(3.8\times10^{4}\) times the nickel value.
- **Measured.** Titanium absorbs up to 60 at. % hydrogen and forms TiH\(_{1.5\text{–}2.0}\) with a volume expansion of about 18 %; its solubility falls as temperature rises, the reverse of iron (secondary) [S31]. No Sieverts constant for titanium was opened.

Palladium–hydrogen:

- **Measured.** At room temperature the dilute α phase exists for \(x < 0.017\) and the β phase for \(x > 0.58\); between them the two coexist. The lattice parameter goes from 388.9 pm to 389.5 pm across α, and β appears at 402.5 pm (tertiary, citing [S5], not opened) [S4]. Pure Pd is 3.889 Å, and in β \(a = 3.9321 + 0.1719\,x\) Å [S3]. In bulk Pd \(\Delta a/a = 0.063\,x\) [S6]. Hydrides of this class expand 10–20 % in volume [S6][S8].
- **Computed here.** Linear strain of β at \(x = 0.58\) against pure Pd: 3.5 % from the tertiary constants, 3.7 % from each of the other two relations. Volume strain 10.9 %. A film taken from 3.892 Å to 4.063 Å expanded 4.4 % [S3].
- **Measured.** Plateau pressure follows \(\ln(p/1\,\mathrm{atm}) = A/RT + B/R\). Absorption on Pd powder: \(A = -36\pm1\) kJ mol⁻¹, \(B = 88\pm3\) J K⁻¹ for H₂; \(A = -32\pm2\), \(B = 88\pm9\) for D₂. Lässer's constants, tabulated in the same paper: \(-37.8\), 93.9 (H₂) and \(-33.7\), 93.7 (D₂). The plateau at about 25 °C is described as 1 to 10 kPa. The lighter isotope has the greater affinity for palladium [S7].
- **Computed here.** At 298 K the plateau is 2.0 kPa (H₂) and 9.8 kPa (D₂) from the first set, 1.9 and 9.8 kPa from the second. Deuterium needs about 5 times the pressure.
- **Measured.** The two-phase region closes at a critical temperature of 566 K [S8]. The critical composition and pressure were not found in an opened source.
- **Measured.** Above \(x = 0.7\) each further 0.1 in H/Pd needs about 1.5 orders of magnitude more H₂ pressure [S3]. Electrochemical insertion reached \(0.96\pm0.02\) in a thin film and \(0.83\pm0.02\) in a foil, limited by mechanical damage from the volume change [S3].
- **Computed here.** From 0.7 to 0.9 that is a factor of 1000 in pressure.
- **Model (Schwarz–Khachaturyan coherent open system).** When α and β stay lattice-coherent, the coherency strain is a macroscopic energy barrier between the phases. The phases cannot coexist at equilibrium, the phase rule does not apply to the plateau, and absorption and desorption occur at different pressures [S11]. The barrier is proportional to the sample volume and cannot be crossed by thermal fluctuation unless the particle is small enough [S8][S9]. The 2006 paper applying this to metal–hydrogen systems was not opened.
- **Model (incoherent transformation).** In bulk Pd, β nucleates incoherently, dislocations form to relieve the elastic stress, and absorption occurs near the equal-area (Maxwell) pressure [S8]; the hysteresis is then assigned to an interfacial energy barrier [S9]. A coherent hydride inclusion in bulk Pd is limited to about 4 nm [S9]. The standard reference on hydride hysteresis [S12] was not opened.

Nickel–hydrogen:

- **Measured.** Nickel hydride forms at 25 °C above 6 kbar of H₂ and is nearly stoichiometric; it decomposes near 3.4 kbar (secondary, after Baranowski; the primary [S14] was not opened) [S13][S16]. In a diamond-anvil cell, 1.6 µm nickel powder was still a solid solution at 0.6 GPa and converted above about 1 GPa; NiH has \(a = 3.731\) Å against 3.5238 Å for Ni [S15].
- **Computed here.** Formation needs 20 times the pressure of a 300 bar vessel and decomposition sets in at 11 times that pressure. Formation over decomposition is 1.8. Linear misfit 5.9 %, volume 18.7 %.

Size effects in palladium:

- **Measured.** Single nanocubes of 13–29 nm at 246 K: every particle above 15 nm switched abruptly between α and β, particles below 15 nm showed sloped transitions, all showed hysteresis, and the loading pressure fell with size and lay below the bulk value (98 Pa for a 23 nm cube) [S9].
- **Measured.** Single nanocrystals by plasmonic sensing: enthalpy and entropy of hydride formation nearly independent of size and shape; hysteresis wider than in bulk; the absorption branch depends on size below 30 nm and the desorption branch does not [S10].
- **Model (mean-field lattice gas with a surface shell, fitted to the collected data).** Desorption pressures of nanoparticles equal the bulk value. Absorption pressure rises with size above 8 nm. The critical temperature of a cube of edge \(L\) (nm) is \(T_c = 566 - 2381/L\) K. Shell and core volumes are equal at 9.7 nm. Desorption is fully coherent only below about 50 nm and near \(T_c\) [S8]. A sphere up to 30 nm is expected to keep a dislocation-free interface [S9].
- **Computed here.** \(T_c(L)\) is 487 K at 30 nm and reaches 300 K at 9.0 nm.
- **Measured.** Below 2.6 nm no hydride forms (tertiary) [S4].

Trapping:

- **Measured.** Deuterium implanted in Pd is bound at 0.31 eV (helium bubbles, vacancy clusters), 0.23 eV (single vacancies) and 0.15 eV (vacancies at high occupancy), relative to the solution site. A vacancy in an fcc metal holds up to six. Trap strength rises in the order dislocation, vacancy, void [S20].
- **Model (effective-medium theory, with the same experiments).** In Ni, Cu, Fe and Mo the first two atoms in a vacancy have nearly the same binding energy and each further atom is bound less [S20]. Both hydrogen-release stages seen in implanted nickel are accounted for by vacancy trapping with an occupancy-dependent binding enthalpy [S21]. A first-principles study gives −0.27 eV for a single nickel vacancy and −0.41 eV for a divacancy (search snippet only) [S32]. No measured value for nickel was read in an opened document.
- **Model (density-functional theory).** Nickel grain boundaries: the Σ3 boundary does not trap and has a 0.55 eV barrier to cross; the Σ5 boundary traps, with 0.06 eV to enter and 0.26 eV to leave (secondary) [S23]. Palladium dislocation cores: 0.164 eV at 5 % strain; hydrides a few nanometres across form at cores at 0 K and dissolve as temperature rises [S22].
- **Measured.** bcc iron and steels, by thermal desorption, permeation and diffusion analysis: dislocation strain field 12–27 kJ mol⁻¹, grain boundary 9–49, single vacancy 24–78 (partly first-principles), microvoid 40, incoherent TiC 60–129. Lattice migration is 4.5–5.5 kJ mol⁻¹ [S19].
- **Convention.** A trap deeper than 50 kJ mol⁻¹ is called irreversible at room temperature [S19].
- **Model (first-order release; Kissinger analysis).** The detrapping rate is \(dx/dt = A(1-x)e^{-E_a/RT}\) with \(E_a = E_b + E_s\), the binding energy plus the local migration energy. \(E_a\) is obtained from the shift of a desorption peak with heating rate. Peak assignment to a defect can be speculative, and one peak often has several overlapping contributions [S19].
- **Measured.** Trap occupancy follows the lattice concentration: at 0.01 wt ppm lattice hydrogen in iron, 50 kJ mol⁻¹ traps are over 90 % full and 10 kJ mol⁻¹ traps under 10 % full. Smaller specimens retain less hydrogen, and loss is faster in vacuum than in argon [S19].
- **Computed here.** 0.23 eV is 22 kJ mol⁻¹ and \(9.0\,kT\) at 298 K; 0.31 eV is 30 kJ mol⁻¹; 50 kJ mol⁻¹ is 0.52 eV and \(20\,kT\). The Boltzmann factor of a 50 kJ mol⁻¹ trap is \(1.7\times10^{-9}\) at 298 K and \(3.0\times10^{-6}\) at 473 K, a gain of 1750 in release rate.
- **Measured.** Under hydrogen fugacity at the GPa level, metal vacancies bound to hydrogen reach up to 30 at. % (superabundant vacancies; secondary) [S19]. Pd under 5 GPa of hydrogen at 800 °C contracts toward a vacancy-ordered structure M₃VacH₄ [S24]. The original report [S25] was not opened.

Diffusion:

- **Measured.** Nickel: \(D = 9.2\times10^{-7}e^{-41.4\,\mathrm{kJ}/RT}\) m² s⁻¹, 260–980 K [S1]. Palladium: \(D = 0.006\,e^{-0.23\,\mathrm{eV}/kT}\) cm² s⁻¹ [S17]; in β-PdH\(_x\) about \(10^{-11}\) m² s⁻¹ at room temperature [S3]. Annealed iron: \(D = 7.23\times10^{-8}e^{-5.69\,\mathrm{kJ}/RT}\) m² s⁻¹ up to 80 °C (secondary) [S18].
- **Computed here.** At 298 K, with crossing time \(x^2/D\) and depth \(\sqrt{Dt}\):

  | Metal | \(D\) (m² s⁻¹) | 1 µm | 100 µm | Depth in 100 µs |
  |---|---|---|---|---|
  | Ni | \(5.1\times10^{-14}\) | 20 s | 55 h | 2.3 nm |
  | Pd (α) | \(7.7\times10^{-11}\) | 13 ms | 130 s | 88 nm |
  | Fe | \(7.3\times10^{-9}\) | 0.14 ms | 1.4 s | 850 nm |

  In nickel the depth reached in 10 µs is 0.71 nm.

Embrittlement:

- **Measured.** Embrittlement requires a hydrogen content above a critical level together with a sufficient stress; 5 wt ppm lowers the tensile strength of a martensitic steel. Baking removes hydrogen taken up in production: 200 °C for 10 min sufficed for one hot-stamped martensitic steel [S19].
- **Model.** The named mechanisms are hydrogen-enhanced decohesion (HEDE), hydrogen-enhanced local plasticity (HELP) and adsorption-induced dislocation emission (AIDE) [S19].

Strain scale:

- **Measured.** Nickel: \(\lambda_{100} = -46\) ppm, \(\lambda_{111} = -24\) ppm; as-cast polycrystalline nickel \(-35\) ppm [S29]. Linear thermal expansion \(13.4\times10^{-6}\) K⁻¹ at 25 °C (tertiary) [S30].
- **Computed here.** \((2\lambda_{100} + 3\lambda_{111})/5 = -33\) ppm. Taking \(34\times10^{-6}\) as the magnitude, the hydride misfit is about 1000 times larger in Pd and 1700 times larger in Ni. A 10 K change strains nickel by \(1.3\times10^{-4}\), 3.9 times the magnetostriction; 2.5 K gives the same strain as magnetic saturation.

Anomalous-heat claims:

- **Measured.** A multi-institution programme re-evaluated cold fusion and reported that its efforts "have yet to yield any evidence of such an effect" [S27]. According to a news account of the paper, it tested three set-ups: palladium loaded toward H/Pd 0.875, a level exceeded twice in several dozen tests; 420 samples of nickel powder heated in hydrogen, none showing excess heat; and pulsed-plasma loading of palladium, with no enhanced tritium (secondary) [S28]. The authors state that much of the parameter space remains unexplored [S27].

**Data confidence:** Medium — the solubility, diffusion and plateau relations were read in full text and agree with second sources within a factor of two, but every room-temperature solubility for Ni, Fe and Cu is extrapolated from fits made above 500 K. The Pd phase limits and lattice constants rest on a tertiary page whose primary [S5] was not opened. The nickel-hydride pressures rest on a secondary; [S14] was not opened. Numbers from [S32] and [S33] are snippets. No measured trap energy for nickel was opened. The standard references on hysteresis [S12] and on microstructure and trapping [S26] were not read in full.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Sieverts' law [S2]: \(c = S_0\,e^{-E_S/RT}\sqrt{p}\).
- Plateau pressure (van 't Hoff) [S7]: \(\ln(p/p_\mathrm{ref}) = A/RT + B/R\).
- Lattice expansion of Pd [S6]: \(\Delta a/a = 0.063\,x\).
- Size dependence of the critical temperature of Pd nanocubes [S8]: \(T_c(L) = 566 - 2381/L\) (K, nm).
- Diffusion [S1]: \(D = D_0\,e^{-E_D/RT}\); crossing time \(x^2/D\).
- Detrapping [S19]: \(dx/dt = A(1-x)\,e^{-E_a/RT}\), \(E_a = E_b + E_s\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Dilute solubility has no minimum size; it is an occupancy fraction set by pressure and temperature. The hydride transition has two sourced length scales in palladium: about 10 nm, where the surface shell holds half the sites and \(T_c(L)\) falls to room temperature, and 30–50 nm, below which the transformation stays coherent. A trap is one defect site holding one to six atoms. No sourced fact gives a trapped population a minimum cluster volume.

- **Clock rate / latency.** The interstitial hop, read as \(D(T)\): at room temperature 1 µm is crossed in 20 s in nickel, 13 ms in palladium and 0.14 ms in iron. The release clock of a trap is \(\tau = A^{-1}e^{E_a/RT}\) per atom. The observer's clock is the heating rate of a desorption run or the time since charging.

- **Energy barriers or thresholds.** Three separate quantities. The heat of solution sets how much dissolves. The trap binding energy, 0.15–0.31 eV in Pd and 9–78 kJ mol⁻¹ for lattice defects in iron, is an energy per atom that falls as a site fills. The coherency barrier of the α–β transformation is proportional to the transforming volume; it is the one barrier in this entry with the form of \(KV\) in [superparamagnetism](superparamagnetism.md), and it belongs to the hydride transition at its plateau pressure.

- **Dominant failure modes.**
  - **Threshold** — hydride plateau: a first-order transition at \(p_\mathrm{plateau}(T)\), with hysteresis. Pd: 2.0 kPa (H₂) and 9.8 kPa (D₂) at 298 K. Ni: formation above 6 kbar, decomposition near 3.4 kbar.
  - **Threshold** — critical temperature: above 566 K in bulk Pd there is no two-phase region and no hysteresis. In nanocubes the line moves as \(566 - 2381/L\).
  - **Crossover** — pressure: \(c \propto \sqrt{p}\) in the dilute range, with no critical pressure. Nickel goes from \(1.8\times10^{-5}\) at 1 bar to \(3.1\times10^{-4}\) at 300 bar.
  - **Crossover** — temperature: \(c \propto e^{-E_S/RT}\). Solubility rises on heating in Ni, Fe and Cu and falls in Ti.
  - **Crossover** — detrapping: Arrhenius, \(e^{-E_a/RT}\) per atom. The 50 kJ mol⁻¹ line between reversible and irreversible traps is a convention for room temperature.
  - **Crossover** — size in Pd: the absorption plateau falls and the hysteresis narrows as \(L\) decreases below 30–50 nm; transitions are sloped below 15 nm. No hydride forms below 2.6 nm (tertiary).
  - **Crossover** — overloading: above H/Pd 0.7 the required pressure rises about 1.5 decades per 0.1.
  - **Crossover** — transport: a pulse shorter than \(x^2/D\) does not move hydrogen a distance \(x\). In nickel 100 µs corresponds to 2.3 nm.
  - **Threshold** — fracture: embrittlement needs both a critical hydrogen content and a sufficient stress; the values depend on the alloy.

- **Emergent constant or stable output.** An equilibrium occupancy H/M set by \(p\) and \(T\); in hydride formers a two-phase plateau with a lattice expansion of 3.5–5.9 % linear; and a trapped residue that remains after the gas is removed and leaves on heating.

### 4.6 Internal Consistency Notes

The entry holds three behaviours that the library's families separate. Dilute solubility is an ensemble average with no latch. The hydride transition is first-order and hysteretic, with both states available between the absorption and desorption pressures; this is the reason for filing under `latched-order`. Trapped hydrogen is retained with no power supplied, and its barrier is per atom.

The comparison with a magnetic grain follows from the sourced facts. In [superparamagnetism](superparamagnetism.md) the barrier \(KV\) grows with grain volume. For hydrogen, the sourced volume-proportional barrier is the coherency strain of the α–β transformation, and the size experiments on single Pd nanocrystals measure its consequence: hysteresis that narrows and closes as the particle shrinks. That object exists only at the plateau pressure of a hydride former. The opened sources give no barrier that scales with the volume of a trapped cluster: binding per atom is constant for the first two atoms in a vacancy and decreases after that, and retention is governed by \(E_a\), by the lattice concentration, and by the diffusion path to a free surface. Smaller specimens retain less hydrogen for the last reason.

Nickel under gas near room temperature stays in the dilute range. At 300 bar the computed lattice occupancy is \(3.1\times10^{-4}\), and the hydride needs 20 times that pressure. A size dependence of the kind measured in palladium has not been measured for nickel in any opened source.

Thermal desorption is an established hold-and-erase measurement: charge, wait, heat at a known rate, and read the release peaks. Peak assignment is often uncertain, and small specimens lose hydrogen quickly.

The hydride misfit is \(10^{3}\) times the saturation magnetostriction of nickel ([magnetostriction](magnetostriction.md)), and a 2.5 K temperature change strains nickel as much as magnetic saturation does.

Open items: no Sieverts constant for Pd above the critical temperature or for Ti was opened; no measured trap energy for nickel; the 300 bar figure assumes an ideal gas; surface adsorption on fine powder, which adds to any measured uptake, is not quantified here.

The record on anomalous heat is entered as a null measurement [S27]. This entry asserts no mechanism for such claims.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the plateau, the critical temperature and the Arrhenius release law map cleanly onto threshold, threshold and crossover, and the volume-proportional barrier is sourced for the hydride transition; the entry combines an ensemble average, a hysteretic transition and a per-atom trap under one family, and the trap data for nickel are thin.

## Related entries

- [elasticity](elasticity.md) — the coherency strain energy that sets the hydride hysteresis
- [melting](melting.md) — loss of the host lattice; a separate thermal threshold
- [magnetostriction](magnetostriction.md) — strain of order \(10^{-5}\) in nickel, against \(10^{-2}\) for hydride misfit
- [superparamagnetism](superparamagnetism.md) — the \(KV\) barrier that the coherent hydride transition resembles and trapping does not
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — hysteresis from a barrier between two states
- [electrical-resistivity](electrical-resistivity.md) — resistance as a loading readout

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Hagi, *Trans. Japan Inst. Metals* 27, 233 (1986)](https://www.jstage.jst.go.jp/article/matertrans1960/27/4/27_4_233/_article) | full-text | Solubility and diffusion coefficient of hydrogen in nickel and copper. |
| S2 | [San Marchi and Somerday, *Technical Reference for Hydrogen Compatibility of Materials*, Sandia report SAND2012-7321](https://www.osti.gov/servlets/purl/1055634) | full-text | Sieverts' law as used; solubility relation for iron (Table 2.1 of the carbon-steel chapter); lattice hydrogen against hydrogen at defects. |
| S3 | [Benck, Jackson, Young, Rettenwander and Chiang, *Chem. Mater.* 31, 4234 (2019), arXiv:1808.01555](https://arxiv.org/abs/1808.01555) | full-text | H/Pd 0.68 at 1 atm; lattice-parameter calibration; pressure per 0.1 H/Pd above 0.7; electrochemical loading to 0.96; diffusion in the β phase. |
| S4 | [Wikipedia, "Palladium hydride"](https://en.wikipedia.org/wiki/Palladium_hydride) | full-text | Tertiary: α and β composition limits and lattice constants (citing S5); about 0.7 at 1 atm; no hydride below 2.6 nm. |
| S5 | [Manchester, San-Martin and Pitre, *J. Phase Equilibria* 15, 62 (1994)](https://doi.org/10.1007/BF02667685) | cited-only | Standard assessment of the H–Pd phase diagram. |
| S6 | [Wagner and Pundt, *AIMS Materials Science* 7, 399 (2020)](https://publikationen.bibliothek.kit.edu/1000121373/134309554) | full-text | Expansion factor 0.063 per H/Pd; 10–20 % volume expansion; site-energy analysis of Pd films. |
| S7 | [Sharpe, Shmayda and Glance, *Fusion Sci. Technol.* (2020), accepted manuscript at OSTI](https://www.osti.gov/servlets/purl/1647469) | full-text | Van 't Hoff constants for Pd–H and Pd–D, with Lässer's and Gillespie's; plateau of 1 to 10 kPa near 25 °C; isotope affinity. |
| S8 | [Griessen, Strohfeldt and Giessen, *Nature Mater.* 15, 311 (2016), author-hosted copy](https://www.pi4.uni-stuttgart.de/publications/files/2016_naturematerials_griessen.pdf) | full-text | Critical temperature 566 K; volume-proportional coherency barrier; size dependence of absorption and desorption pressures; Tc(L); 9.7 nm and 50 nm scales. |
| S9 | [Baldi, Narayan, Koh and Dionne, *Nature Mater.* 13, 1143 (2014), institute-hosted copy](https://www.differ.nl/sites/default/files/attachments/biblio/2014_59958.pdf) | full-text | Single-nanocube isotherms at 246 K; sharp transitions above 15 nm; coherent-size limits of 4 nm, 22 nm and 30 nm. |
| S10 | [Syrenova et al., *Nature Mater.* 14, 1236 (2015), repository record](https://research.chalmers.se/en/publication/222889) | abstract | Size dependence of the absorption branch below 30 nm; size-independent desorption; wider hysteresis than bulk. |
| S11 | [Schwarz and Khachaturyan, *Phys. Rev. Lett.* 74, 2523 (1995), OSTI record](https://www.osti.gov/biblio/27865) | abstract | Coherency strain as a macroscopic barrier; inapplicable phase rule; hysteresis. |
| S12 | [Flanagan and Clewley, *J. Less-Common Met.* 83, 127 (1982)](https://doi.org/10.1016/0022-5088(82)90176-X) | cited-only | Plastic-deformation account of hydride hysteresis. |
| S13 | [Shan, *The Interaction of Water and Hydrogen with Nickel Surfaces*, thesis, Leiden University (2009), chapter 7](https://scholarlypublications.universiteitleiden.nl/handle/1887/14365) | full-text | Secondary: nickel hydride forms above 6 kbar at 25 °C and decomposes near 3.4 kbar. |
| S14 | [Baranowski and Filipek, *J. Alloys Compd.* 404–406, 2 (2005)](https://doi.org/10.1016/j.jallcom.2005.02.102) | cited-only | Review of nickel hydride by its discoverer. |
| S15 | [Ying et al., *Phys. Rev. B* 98, 140101 (2018), author-hosted copy](https://www2.ph.ed.ac.uk/~aherman2/wp-content/uploads/2021/04/PhysRevB_98_140101_2018.pdf) | full-text | Solid-solution limit of nickel; NiH above about 1 GPa in a diamond cell; lattice parameters of Ni and NiH. |
| S16 | [Wikipedia, "Nickel hydride"](https://en.wikipedia.org/wiki/Nickel_hydride) | full-text | Tertiary: 0.00005 wt % hydrogen in nickel at 25 °C; the 6 and 3.4 kbar pressures. |
| S17 | [Heuser et al., *Phys. Rev. Lett.* 113, issue 2 (2014), NIST publication record](https://www.nist.gov/node/566041) | abstract | Bulk and dislocation-pipe diffusion of hydrogen in Pd. |
| S18 | [Zafra, Harris, Sun and Martínez-Pañeda, arXiv:2112.00589](https://arxiv.org/abs/2112.00589) | full-text | Secondary for Kiuchi and McLellan (1983): diffusion of hydrogen in annealed iron. |
| S19 | [Chen et al., "Hydrogen trapping and embrittlement in metals – A review", *Int. J. Hydrogen Energy* 136, 789 (2025), arXiv:2404.07736](https://arxiv.org/abs/2404.07736) | full-text | Trap energies in bcc iron; 50 kJ/mol convention; detrapping law and thermal desorption method; occupancy; specimen-size loss; superabundant vacancies (secondary); embrittlement mechanisms; baking. |
| S20 | [Besenbacher, Bech Nielsen, Nørskov, Myers and Nordlander, Sandia report SAND-89-2232C (1989)](https://www.osti.gov/servlets/purl/5658854) | full-text | Binding enthalpies of deuterium at vacancies and bubbles in Pd; six atoms per vacancy; occupancy dependence. |
| S21 | [Myers et al., *Phys. Rev. B* 33 (2) (1986), OSTI record](https://www.osti.gov/biblio/6303761) | abstract | Two release stages in implanted nickel explained by occupancy-dependent vacancy trapping. |
| S22 | [Trinkle, Ju, Heuser and Udovic, *Phys. Rev. B* 83, 174116 (2011), arXiv:1104.3757](https://arxiv.org/abs/1104.3757) | full-text | Trapping at Pd dislocation cores; nanometre hydrides at 0 K. |
| S23 | [Jain, Olleak, He, Chaurasia and Di Stefano, arXiv:2601.05917](https://arxiv.org/abs/2601.05917) | full-text | Secondary for Di Stefano et al. (2015): barriers at Σ3 and Σ5 grain boundaries in nickel. |
| S24 | [Degtyareva, arXiv:1001.1525](https://arxiv.org/abs/1001.1525) | full-text | Vacancy-ordered Pd hydride at 5 GPa and 800 °C. Secondary for S25. |
| S25 | [Fukai and Ōkuma, *Phys. Rev. Lett.* 73, 1640 (1994)](https://doi.org/10.1103/PhysRevLett.73.1640) | cited-only | Original report of superabundant vacancies in Pd hydride. |
| S26 | [Pundt and Kirchheim, *Annu. Rev. Mater. Res.* 36, 555 (2006)](https://doi.org/10.1146/annurev.matsci.36.090804.094451) | abstract | Microstructure and size change solubility and phase boundaries. |
| S27 | [Berlinguette et al., *Nature* 570, 45 (2019), PubMed record](https://pubmed.ncbi.nlm.nih.gov/31133686/) | abstract | No evidence of the claimed effect; parameter space described as underexplored. |
| S28 | [Physics World news report on S27 (2019)](https://physicsworld.com/?p=80431) | full-text | Secondary: the three set-ups, the 0.875 loading level, 420 nickel powder samples, the tritium test. |
| S29 | [Grössinger, Sato Turtelli and Mahmood, *IOP Conf. Ser.: Mater. Sci. Eng.* 60, 012002 (2014)](https://doi.org/10.1088/1757-899X/60/1/012002) | full-text | Single-crystal magnetostriction constants of nickel; polycrystalline nickel at −35 ppm. |
| S30 | [KnowledgeDoor, *Elements Handbook*, nickel and iron pages](https://knowledgedoor.com/2/elements_handbook/nickel.html) | full-text | Tertiary: thermal expansion of nickel; molar masses and molar volumes. |
| S31 | [Bhadeshia, "Titanium and its alloys", University of Cambridge lecture notes](https://www.phase-trans.msm.cam.ac.uk/2000/C9/lecture3.pdf) | full-text | Secondary: hydrogen uptake, hydride and temperature trend in titanium. |
| S32 | [Tanguy, Wang and Connétable, "Stability of vacancy-hydrogen clusters in nickel from first-principles calculations", *Acta Mater.* (2014), repository record](https://hal.science/hal-01169788) | snippet | Computed segregation energies at nickel vacancies. |
| S33 | [Nagumo, *Fundamentals of Hydrogen Embrittlement* (Springer, 2016), chapter 1](https://link.springer.com/chapter/10.1007/978-981-10-0161-1_1) | snippet | Hydrogen concentration in α-iron at room temperature and 0.1 MPa. |
