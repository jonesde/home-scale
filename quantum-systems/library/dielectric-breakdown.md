---
id: dielectric-breakdown
title: Dielectric Breakdown (Field-Opened Insulator Conversion)
status: formal
family: threshold-conversion
constraints:
  - field-threshold
  - energy-barrier
  - spatial-buffer
  - thermal
  - mechanical-lattice
confidence_data: medium
confidence_mapping: medium
review_depth: deep
related:
  - refraction-dielectric
  - ionization-threshold
  - semiconductor-gap-absorption
  - photoconductivity
  - piezoelectricity
  - ferroelectric-remanence
  - plasma-frequency-cutoff
updated: 2026-11-12
---

# Dielectric Breakdown (Field-Opened Insulator Conversion)

### 4.1 Effect Name

Dielectric breakdown (field-opened insulator conversion)

### 4.2 Macroscopic Observation

An insulator — dry air, an oil, a polymer film, an oxide layer, a vacuum gap — supports an electric field and passes only a small leakage current up to a voltage that depends on the material, the geometry and the duration of the stress. Beyond it a conducting path forms suddenly: a spark in a gas, a puncture or carbon track in a solid, an arc between vacuum electrodes. A gas recovers when the discharge goes out. A solid is permanently changed, and a second discharge follows the damaged path.

### 4.3 Established Quantitative Boundaries

- **Measured.** Air at 1 atm and 20 °C in a uniform field breaks down at 31.6 kV across a 1.0 cm gap [S1]. The field at which ionization balances attachment in air at standard conditions is about 3 MV m⁻¹ [S2].
- **Computed here.** 31.6 kV across 1.0 cm is 3.16 MV m⁻¹. The usual "3 MV/m" is the value for a gap of about a centimetre.
- **Measured.** The breakdown field of air falls steadily with gap length at constant pressure. Tabulated uniform-field voltages divided by the gap give 46 kV cm⁻¹ at 1 mm, 34.2 at 5 mm, 31.6 at 1 cm, 29.2 at 2.5 cm, 26.5 at 10 cm and 25.5 at 20 cm [S1].
- **Model (Schumann fit to the air data).** \(V_b = 6.72\sqrt{pd} + 24.36\,pd\) kV, with \(pd\) in bar cm [S1].
- **Computed here.** At 1 bar the fit gives 45.6, 31.1 and 26.5 kV cm⁻¹ at gaps of 0.1, 1 and 10 cm.
- **Measured.** Humidity raises the breakdown voltage of air; for sphere gaps the effect does not exceed 2–3 % over ordinary laboratory humidity [S1].
- **Measured.** Paschen's law: the breakdown voltage of a uniform-field gap is a function of the product \(pd\) alone for a given gas and electrode material, up to about 1000–2000 torr cm [S1]. The curve has a minimum, and below the minimum voltage no breakdown by electron multiplication occurs at any \(pd\) [S1]:

  | Gas | Minimum voltage (V) | \(pd\) at the minimum (torr cm) | Gap at 1 atm (µm) |
  |---|---|---|---|
  | Air | 352 [S1]; 327 [S3] | 0.55; 0.567 | 7.2–7.5 |
  | N₂ | 240 [S1]; 251 [S4] | 0.65; 0.67 | 8.6–8.8 |
  | H₂ | 230 [S1]; 273 [S3] | 1.05; 1.15 | 13.8–15.1 |
  | Ar | 137 [S4] | 0.9 | 11.8 |
  | He | 155 [S1]; 156 [S3] | 4.0 | 52.6 |

  The values keyed [S3] and [S4] are from Naidu and Kamaraju's table, read in copies; the book itself was not opened. The two tabulations differ by 25 V for air and by 43 V (19 %) for hydrogen. Argon rests on the tertiary copy alone.
- **Computed here.** The gap column is \(pd\) divided by 760 torr. At the air minimum the field is 44–49 MV m⁻¹ (327 V across 7.5 µm, 352 V across 7.2 µm). A 1 mm air gap reaches its minimum at 5.5–5.7 torr. The hydrogen minimum is 54–122 V below the air minimum, depending on which table supplies each value.
- **Measured.** The minimum depends on the cathode. It follows the work function of the cathode material, and 64 V has been observed in neon between caesium-coated electrodes at 26 torr [S1].
- **Model (Townsend).** Left of the minimum, electrons cross the gap making few collisions and the breakdown voltage rises as \(pd\) falls [S1]. This branch is reached by lowering the pressure.
- **Measured.** At atmospheric pressure, a gap narrowed below the minimum does not follow that rising branch. The breakdown voltage plateaus between about 5 and 10 µm and then falls nearly linearly with gap below about 5 µm, which is attributed to field emission from the cathode [S5]. Another group saw a continuous decrease below 25 µm [S6]. A third reports deviation from the Paschen curve below 4 µm and breakdown at a roughly constant 350 V µm⁻¹ below 1 µm [S7].
- **Convention.** The regime boundaries differ between authors and electrodes: Paschen behaviour above 10 µm, a plateau from 5 to 10 µm and a steep decline below 5 µm in one reading; ion-enhanced field emission from 1.5 to 5 µm and pure Fowler–Nordheim emission below 1.5 µm in another [S5].
- **Measured.** Field emission sets in at an applied field of about 100 V µm⁻¹ (10⁸ V m⁻¹), or about 10 V µm⁻¹ with geometric enhancement and a suitable material [S5].
- **Model (Fowler–Nordheim tunnelling).** Emission current density follows \(j = CE^2\exp(-D/E)\). Local surface fields of 10⁷–10⁸ V cm⁻¹ (1–10 GV m⁻¹) give microampere currents, and such fields arise at sharp points and sub-microscopic irregularities with only 2–5 kV applied [S1].
- **Measured.** Gases compared at equal density, as the limiting value of \(E/N\) relative to \(\mathrm{SF_6}\) = 1: H₂ 0.18, air about 0.30, N₂ 0.36, CO₂ 0.30, Ar 0.07, Ne 0.006, and up to about 2.4 for the strongest gas listed. The scale is 3.61 × 10⁻¹⁵ V cm² for \(\mathrm{SF_6}\) [S9].
- **Computed here.** At 1 atm and 20 °C (\(N = 2.50 \times 10^{19}\) cm⁻³) those ratios are 27 kV cm⁻¹ for air, 32.5 for N₂ and 16 for H₂. Hydrogen holds 0.6 of the field of air and 0.5 of that of nitrogen.
- **Measured.** For the normal alkanes from methane to hexane, electric strength at fixed gap and pressure rises with chain length [S10]. No opened source gives the strength of a hydrocarbon vapour relative to air or nitrogen.
- **Model (Townsend).** Ionization coefficient \(\alpha/p = A\exp(-Bp/E)\). Breakdown when \(\gamma(e^{\alpha d} - 1) = 1\), stated as \(\alpha d\) reaching 8–10. The closed form \(V_b = B\,pd/\ln[A\,pd/\ln(1 + 1/\gamma)]\) with \(A\) = 12, \(B\) = 365 and \(\gamma\) = 0.02 gives a minimum of 325 V for air [S1].
- **Model (Raether–Meek).** An avalanche becomes a streamer when its head holds about 10⁸ electrons, \(\alpha x_c \approx 18\)–20 [S1]; about 18 in ambient air [S2]. The streamer mechanism replaces the Townsend mechanism at \(pd\) of 1–2 bar cm and above, marked by a discontinuity in the formative time lag [S1].
- **Convention.** The delay to breakdown is the statistical time lag, the wait for a first electron, plus the formative time lag, the time for the discharge to develop [S1].
- **Measured.** Time lags of 10⁻⁸ s and shorter are recorded in highly overvolted gaps; the change in formative lag between mechanisms occurs near 10⁻⁷ s [S1]. The Townsend mechanism alone predicts lags of order 10⁻⁵ s [S3].
- **Measured.** A short pulse raises the breakdown field of a gas. In air at 1 atm the field is 2.3 times higher for a 10 ns pulse and a few per cent higher for a 1 µs pulse; the gain is smaller at high pressure [S8]. This is Martin's reading of Felsenthal and Proud's curves, which were not opened.
- **Measured.** Mineral oil in the standard power-frequency test, with spherical electrodes 2.5 mm apart [S12]: dry new and aged oils break down at 60–88 kV. The voltage is almost unchanged below 20 % relative water saturation and falls rapidly above it [S11].
- **Computed here.** 60–88 kV across 2.5 mm is 24–35 MV m⁻¹.
- **Measured.** Highly purified liquids in small gaps reach higher fields: hexane 1.1–1.3 MV cm⁻¹, benzene 1.1, "good oil" about 1.0–4.0, silicone 1.0–1.2 [S1].
- **Model (Martin's empirical fit).** Pulsed breakdown of liquids over large areas: \(F\,t^{1/3}A^{1/10} = k\), with \(F\) in MV cm⁻¹, \(t\) in µs and \(A\) in cm²; \(k\) = 0.5 for transformer oil, 0.3 for water with a positive electrode and 0.6 with a negative one. Several per cent of water or carbon in the oil changes the pulsed value by less than 20 % [S8].
- **Computed here.** For oil the fit gives 0.5 MV cm⁻¹ at 1 µs and 1 cm², 0.32 at 1 µs and 100 cm², and 0.11 at 100 µs and 1 cm². The last is an extrapolation of a formula its author calls not very accurate.
- **Measured.** Polymer films in the 60 Hz short-time test. Polyimide (Kapton HN): 303 kV mm⁻¹ at 25 µm, 240 at 50 µm, 205 at 75 µm, 154 at 125 µm [S13]. Polyester (Mylar): over 600 kV mm⁻¹ at 6 µm and about 80 kV mm⁻¹ at 350 µm [S14].
- **Computed here.** Films of 6–125 µm therefore sit at 1.5–6 × 10⁸ V m⁻¹. Fitting \(E_\mathrm{bd} \propto d^{-n}\) to the end points gives \(n\) = 0.42 for the polyimide and 0.50 for the polyester.
- **Measured.** Polyethylene in recessed specimens under direct voltage, the "intrinsic" strength: about 17 MV in⁻¹ at 25 °C and below, falling to about 2 MV in⁻¹ at the melting point near 115 °C [S15].
- **Computed here.** 17 MV in⁻¹ is 670 MV m⁻¹ and 2 MV in⁻¹ is 79 MV m⁻¹.
- **Model (Martin's empirical fit).** Pulsed breakdown of plastics scales with stressed volume: \(E\,(\mathrm{vol})^{1/10} = k\), with \(E\) in MV cm⁻¹ and volume in cm³; \(k\) = 2.5 for polythene, 2.9 for polypropylene, 3.3 for Perspex, 3.6 for thick Mylar. Thin sheets become almost independent of volume, at 5.5 MV cm⁻¹ for 6.4 µm, 4.0 for 51 µm and about 3.0 for 254 µm. Life in pulses goes as \((E_\mathrm{BD}/E_\mathrm{op})^8\) [S8].
- **Computed here.** The pulsed thin-sheet values give \(n\) = 0.16.
- **Measured.** Deposited silicon dioxide (PECVD TEOS, 0.6–15 µm) under a voltage ramp: avalanche breakdown begins at a nominal 9.4 MV cm⁻¹ in a 0.9 µm film and 9.0 MV cm⁻¹ in a 15 µm film. The same paper notes that in thin oxides the breakdown field typically increases with thickness, the opposite of the polymer trend [S16]. No full text for thermally grown oxide was opened.
- **Measured.** Alumina ceramics, vendor values under direct voltage at room temperature: 17 to 32.6 kV mm⁻¹ by grade. The vendor warns that the result is sensitive to specimen geometry and that data from different sources should be compared with caution [S17].
- **Measured.** The strength of a solid falls with the time of stressing, through a sequence of mechanisms: intrinsic at about 10⁻⁸ s, then avalanche and electromechanical, thermal, and erosion or electrochemical out to 10⁴ s [S1].
- **Model (thermal balance; Stark–Garton).** Thermal breakdown occurs when heating by conduction and dielectric loss exceeds cooling; it is lower for alternating voltage and falls with frequency. Electromechanical collapse: no stable thickness exists below \(d/d_0 = 0.6\), giving an apparent strength \(E_a = 0.6\,(Y/\varepsilon_0\varepsilon_r)^{1/2}\). No satisfactory model predicts the intrinsic strength [S1].
- **Convention.** Gases are classed as self-restoring: a discharge leaves no change and the same sample can be tested many times. Tracking leaves a permanent conducting path, usually carbon, on organic insulation [S1].
- **Measured.** Vacuum gap. Conditioned copper electrodes under direct voltage in ultrahigh vacuum break down at a mean macroscopic field of 159 MV m⁻¹ with a standard deviation of 32 % [S18]. Across metals the conditioned field runs from about 100 MV m⁻¹ for aluminium to 850 MV m⁻¹ for stainless steel, with copper near 170 [S19].
- **Model (Fowler–Nordheim fit to the pre-breakdown current).** In the same copper measurements the field enhancement factor has a mean of 77 (36 %) and the local field at breakdown a mean of 10.8 GV m⁻¹ (16 %), independent of the gap [S18].
- **Measured.** Glow and arc. The cathode sheath voltage is typically several hundred volts in a glow discharge and 10–20 V in an arc; arcs burn at under 20 V to about 100 V [S20]. Lecture-note values: a glow at 75–300 V over 1–100 mA; when the current is raised to about 1 A or more the voltage falls suddenly to 20–50 V, with cathode current densities of 10³–10⁷ A cm⁻² [S3].
- **Convention.** A working classification calls a discharge an arc if the current exceeds 1 A and the voltage is below 100 V, and a glow if the reverse [S20].

**Data confidence:** Medium. That breakdown occurs at a field which depends on gap, density, time and material is established, and the air values, the Paschen law and the Townsend and streamer criteria were read in a full-text textbook. Weaker points: the argon minimum and Naidu's nitrogen value rest on a tertiary web copy [S4]; the 350 V µm⁻¹ figure rests on an abstract seen only in paraphrase [S7]; the 10 ns factor is Martin's reading of curves that were not opened [S8]; the oil test gap comes from a trade article [S12]; the polyethylene value and the alkane trend rest on abstracts [S15][S10]. The thickness exponents are computed here from datasheet end points; no published exponent was found.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Paschen form for a uniform-field gas gap, with the Townsend closed form [S1]:

  \[
  V_b = f(pd),\qquad V_b = \frac{B\,pd}{\ln\!\left[\dfrac{A\,pd}{\ln(1 + 1/\gamma)}\right]}
  \]

- Townsend ionization coefficient and breakdown criterion [S1]:

  \[
  \frac{\alpha}{p} = A\exp\!\left(-\frac{Bp}{E}\right),\qquad \gamma\left(e^{\alpha d} - 1\right) = 1
  \]

- Streamer criterion: \(\alpha x_c \approx 18\)–20, an avalanche head of about 10⁸ electrons [S1][S2].
- Fit for air: \(V_b = 6.72\sqrt{pd} + 24.36\,pd\) kV, \(pd\) in bar cm [S1].
- Field emission: \(j = CE^2\exp(-D/E)\) [S1].
- Empirical pulse scaling: \(F\,t^{1/3}A^{1/10} = k\) for liquids, \(E\,(\mathrm{vol})^{1/10} = k\) for plastics [S8].
- Electromechanical collapse: \(E_a = 0.6\,(Y/\varepsilon_0\varepsilon_r)^{1/2}\) [S1].

No single equation locates the breakdown field of a technical solid. For the intrinsic strength no satisfactory model exists [S1].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A single ionization ([ionization-threshold](ionization-threshold.md)) is not breakdown. In a gas the conversion needs a path with enough collisions for multiplication to outrun loss: \(\alpha d\) of 8–10 with feedback from the cathode, or an avalanche of about 10⁸ electrons for a streamer. The Paschen minimum is the smallest such buffer, 0.55–0.57 torr cm in air, which is 7.2–7.5 µm at 1 atm. When the gas buffer is under-provisioned the outcome depends on what else is present. At low pressure the voltage needed rises. At atmospheric pressure in a gap of a few micrometres, and in vacuum, the cathode surface supplies the electrons by field emission and the gap fails at a lower voltage than the gas mechanism requires. In a solid or a liquid the buffer is statistical: the weakest site in the stressed volume or area.

- **Clock rate / latency.** Two lags in a gas: the wait for a first electron and the formative time, 10⁻⁸ to 10⁻⁵ s by mechanism and overvoltage. The breakdown field rises only for pulses shorter than the formative time: 2.3 times at 10 ns, a few per cent at 1 µs. Liquids follow \(t^{-1/3}\) over the microsecond range. Solids weaken over 10⁻⁸ to 10⁴ s as slower mechanisms come into play.

- **Energy barriers or thresholds.** The operating gate is a field for a given gap, time and material. Two fixed numbers stand behind it. One is a voltage floor for the gas mechanism, the Paschen minimum (327–352 V in air). The other is a local field at the cathode surface for electron emission, 1–10 GV m⁻¹, reached through field enhancement at asperities; for conditioned copper in vacuum it is 10.8 GV m⁻¹. Holding the field below the gate costs only the leakage.

- **Dominant failure modes.**
  - **Threshold** — Paschen floor: below the minimum voltage (air 327–352 V, H₂ 230–273 V, for a given cathode) no multiplication breakdown occurs at any \(pd\).
  - **Crossover** — gap and density in a uniform gas gap: \(V_b = 6.72\sqrt{pd} + 24.36\,pd\) kV in air, so the field falls from 46 kV cm⁻¹ at 1 mm to 25.5 kV cm⁻¹ at 20 cm. "3 MV/m" is the convention for about 1 cm at 1 atm.
  - **Crossover** — low pressure, \(pd\) below the minimum: the voltage rises as \(pd\) falls, on the Townsend form. This is the case in which the spark is refused.
  - **Crossover** — microgap at atmospheric pressure: below 5–10 µm the voltage plateaus and then falls about linearly with gap, at 100–350 V µm⁻¹, as field emission takes over; the emission current follows \(j = CE^2\exp(-D/E)\).
  - **Threshold** — vacuum gap: a local cathode field near 10.8 GV m⁻¹ for copper (16 % scatter). The macroscopic field, 159 MV m⁻¹ with 32 % scatter, is statistical through the enhancement factor.
  - **Crossover** — stress time: a factor 2.3 in gas at 10 ns and a few per cent at 1 µs; \(F \propto t^{-1/3}A^{-1/10}\) in oil; life \(\propto (E_\mathrm{BD}/E_\mathrm{op})^8\) pulses in plastics.
  - **Crossover** — thickness and volume in solids: \(E_\mathrm{bd} \propto d^{-n}\) with \(n\) of 0.4–0.5 for polymer films at 60 Hz; \(E \propto (\mathrm{vol})^{-1/10}\) under pulses. The trend reverses in thin oxide.
  - **Crossover** — thermal: heating by leakage and loss against cooling; lower for alternating voltage and longer stress. No single scale filed.
  - **Threshold** — electromechanical collapse of a soft film at \(d/d_0 = 0.6\) (Stark–Garton model).
  - **Threshold** — damage: a solid that has punctured or tracked carries a permanent conducting path, and the original strength is no longer a property of that path. A gas restores itself.
  - **Crossover** — glow to arc: the cathode fall drops from several hundred volts to 10–20 V in an abrupt change of emission mode, but no fixed current marks it. The 1 A and 100 V line is a convention.

- **Emergent constant or stable output.** Below the gate: a stable insulating state, the useful output of the dielectric. Above it: a conducting channel, self-restoring in a gas and permanent in a solid. There is no material-universal breakdown field; gases alone span a factor of about 400 at equal density, and solids run from 17 kV mm⁻¹ for an alumina to over 600 kV mm⁻¹ for a 6 µm polyester film.

### 4.6 Internal Consistency Notes

Filed in threshold-conversion because below the gate the conversion does not occur. The assignment is incomplete. Unlike pair production or a work function, the breakdown field is not a single-node energy. It is an avalanche or emission condition that depends on path, time, defects, heat and the electrode surface. The class is clear; a closed buffer and barrier specification that predicts a polymer's strength from node rules is not in hand.

Sourcing changed the entry in six places. The first version said that very short gaps raise the voltage needed and that a microgap or a vacuum gap fails to spark because multiplication is under-provisioned. That holds at low pressure only. At atmospheric pressure the voltage plateaus and then falls below 5–10 µm, and a vacuum gap fails by field emission at about 160 MV m⁻¹ macroscopic field for copper. The first version put polymer films at 10⁷–10⁸ V m⁻¹; films measure 1.5–6 × 10⁸ V m⁻¹, and the lower range fits millimetre sheet and ceramics. It gave the air Paschen minimum as "near 300 V"; the tables give 327 and 352 V. It called the oxide value "thermal"; the opened measurement is for deposited oxide. It said thin films are stronger than bulk; that is measured for polymers and reverses in thin oxide. It treated different results for direct and pulsed stress as general; in a gas the pulse effect is a factor 2.3 at 10 ns and only a few per cent at 1 µs.

The correction matters for the mapping. A gas gap has two independent ways to fail, multiplication in the gas and emission from the cathode, and each has its own buffer. The first version carried only the first, so it read every under-provisioned gap as safe.

Contrast with [refraction-dielectric](refraction-dielectric.md): that entry is the reversible, below-threshold polarization of the same insulating population. Contrast with [ionization-threshold](ionization-threshold.md): that entry is the microscopic unbinding step the avalanche uses. Contrast with [photoconductivity](photoconductivity.md): light can raise the carrier density without destroying the lattice; breakdown of a solid usually does destroy it.

A remaining gap: after the first discharge in a solid the system is a different object, a carbon track or melted channel. QSA must not treat conduction along it as the original insulator with a new number.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — a field gate is present and non-conversion below it is well observed, but the gate moves with geometry, time, damage and electrode surface, two failure routes coexist in a gas gap, and the state after a discharge in a solid is no longer the original machine.

## Related entries

- [refraction-dielectric](refraction-dielectric.md) — reversible polarization of the same insulator below the gate
- [ionization-threshold](ionization-threshold.md) — the single-particle step the avalanche consumes
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — an energy gate in a gapped solid, opened by a photon in place of a field
- [photoconductivity](photoconductivity.md) — carriers generated without (necessarily) destroying the lattice
- [piezoelectricity](piezoelectricity.md) — strain–polarization coupling in an intact dielectric; a different failure envelope
- [ferroelectric-remanence](ferroelectric-remanence.md) — a latched polarization written by a field well below destructive breakdown
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — collective response of the charges after a conducting path exists

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Kuffel, Zaengl and Kuffel, *High Voltage Engineering: Fundamentals*, 2nd ed. (Newnes, 2000)](https://www.mv.helsinki.fi/home/tpaulin/Text/hveng.pdf) | full-text | Air breakdown voltages by gap and the Schumann fit; humidity; Paschen's law, minima for air, N2, H2, He and the cathode dependence; Townsend and streamer criteria; time lags; field emission; purified liquids; time dependence, thermal and electromechanical breakdown of solids; self-restoring classification. |
| S2 | [Nijdam, Teunissen and Ebert, "The physics of streamer discharge phenomena", *Plasma Sources Sci. Technol.* 29, 103001 (2020), arXiv:2005.14588](https://arxiv.org/abs/2005.14588) | full-text | Classical breakdown field of air about 3 MV/m; Meek number about 18 in ambient air. |
| S3 | [VSSUT lecture notes, "High Voltage Engineering", module I](https://vssut.ac.in/lecture_notes/lecture1423723357.pdf) | full-text | Secondary: Naidu and Kamaraju's Paschen minima for air, H2 and He (the book itself not opened); Townsend time lag of order 1e-5 s; glow and arc voltage and current ranges. |
| S4 | [Lux, "Paschen's Law", web note (1997/2001)](https://pe2bz.philpem.me.uk/Power/-%20HV/Site-101-Information-HV/paschen.htm) | full-text | Tertiary copy of Naidu and Kamaraju's table: the only opened source for the argon minimum and for their nitrogen value. |
| S5 | [Go and Pohlman, "A mathematical model of the modified Paschen's curve for breakdown in microscale gaps", *J. Appl. Phys.* 107, 103303 (2010)](https://people.eecs.berkeley.edu/~pister/147fa16/Resources/Go2010PaschenBreakdown.pdf) | full-text | Plateau at 5–10 µm and near-linear fall below 5 µm; regime boundaries from earlier work; field emission at about 100 V/µm, 10 V/µm with enhancement. |
| S6 | [Massarczyk, Chu, Elliott and Rielage, "Paschen's law studies in cold gases", arXiv:1612.07170 (2016)](https://arxiv.org/abs/1612.07170) | full-text | Continuous decrease of breakdown voltage below 25 µm. |
| S7 | [Peschot et al., "Deviations from the Paschen's law at short gap distances from 100 nm to 10 μm in air and nitrogen", *Appl. Phys. Lett.* 105, 123109 (2014)](https://doi.org/10.1063/1.4895630) | abstract | Deviation below 4 µm; roughly constant 350 V/µm below 1 µm. Abstract seen in paraphrase only. |
| S8 | [Martin, "Nanosecond Pulse Techniques", AWRE note SSWA/JCM/704/49 (1970); Circuit and Electromagnetic System Design Note 4](https://ece-research.unm.edu/summa/notes/CESDN/CESDN4.pdf) | full-text | Pulse-length dependence of gas breakdown (2.3 times at 10 ns, a few per cent at 1 µs); time and area scaling for oil and water; volume scaling, thin-sheet values and pulse life for plastics. Scanned typescript. |
| S9 | [Christophorou, Olthoff and Green, "Gases for Electrical Insulation and Arc Interruption", NIST Technical Note 1425 (1997), Table 1](https://nvlpubs.nist.gov/nistpubs/Legacy/TN/nbstechnicalnote1425.pdf) | full-text | Relative dielectric strengths of H2, air, N2, CO2, Ar, Ne and the strongest listed gas; the absolute scale for SF6. |
| S10 | [Devins and Crowe, "Electric Strength of Saturated Hydrocarbon Gases", *J. Chem. Phys.* 25, 1053 (1956)](https://doi.org/10.1063/1.1743096) | abstract | Electric strength of the normal alkanes rises with chain length. |
| S11 | [Vaisala, "The Effect of Moisture on the Breakdown Voltage of Transformer Oil", white paper B211282EN-A](https://fluid.yodify.com/Documentation/Document/KzlDo/CEN-TIA-power-whitepaper-Moisture-and-Breakdown-Voltage-B211282EN-A-LOW.pdf) | full-text | Vendor paper: oil test voltages of 60–88 kV; flat below 20 % relative saturation and falling above. |
| S12 | [Shkolnik, Dennison and Tate, "6 Things Every Transformer Owner Should Know About Dielectric Breakdown Voltage", *Transformer Technology* (Dec. 2022)](https://transformer-technology.com/article-hub/6-things-every-transformer-owner-should-know-about-dielectric-breakdown-voltage/) | full-text | Tertiary, trade article: 2.5 mm spacing of the spherical test electrodes. The IEC standards were not opened. |
| S13 | [DuPont, "Kapton HN polyimide film" technical data sheet, Table 3](https://www.epectec.com/downloads/DuPont-Kapton-HN-Polyimide-Film.pdf) | full-text | Vendor datasheet: dielectric strength of polyimide film at 25, 50, 75 and 125 µm. |
| S14 | [DuPont Teijin Films, "Mylar – Electrical Properties" product information](https://converting-tasm.pl/wp-content/uploads/2024/01/info-mylar-a-electrical-properties_ekotech_2023.pdf) | full-text | Vendor datasheet: polyester film over 600 kV/mm at 6 µm and about 80 kV/mm at 350 µm. |
| S15 | [Oakes, "The intrinsic electric strength of polythene and its variation with temperature", *J. IEE Part I* 95, 36 (1948)](https://manuscript.isc.ac/Inventory/49/1513259.htm) | abstract | Polyethylene about 17 MV/in at 25 °C and below, about 2 MV/in at the melting point. |
| S16 | [Giuliano et al., "Thickness-dependent dielectric breakdown in thick amorphous SiO2 capacitors", *Solid-State Electronics* 194, 108363 (2022)](https://hdl.handle.net/11585/895709) | full-text | Deposited oxide: avalanche onset at 9.4 and 9.0 MV/cm for 0.9 and 15 µm; breakdown field rising with thickness in thin oxides. Accepted manuscript. |
| S17 | [Morgan Advanced Materials, "Dielectric strength" (Ceramics 101 web page)](https://www.morgantechnicalceramics.com/ceramics-101/electrical-properties-of-ceramics/dielectric-strength) | full-text | Tertiary, vendor page: alumina grades 17 to 32.6 kV/mm; sensitivity to specimen geometry; caution on comparing sources. |
| S18 | [Descoeudres et al., "Investigation of the dc vacuum breakdown mechanism", *Phys. Rev. ST Accel. Beams* 12, 092001 (2009)](https://journals.aps.org/prab/pdf/10.1103/PhysRevSTAB.12.092001) | full-text | Copper in vacuum: breakdown field 159 MV/m, enhancement factor 77, local field 10.8 GV/m, with their scatter. |
| S19 | [Descoeudres et al., "dc breakdown conditioning and breakdown rate of metals and metallic alloys under ultrahigh vacuum", *Phys. Rev. ST Accel. Beams* 12, 032001 (2009)](https://journals.aps.org/prab/pdf/10.1103/PhysRevSTAB.12.032001) | full-text | Conditioned breakdown fields across metals, 100 MV/m for aluminium to 850 MV/m for stainless steel; copper about 170 MV/m. |
| S20 | [Anders, "Glows, arcs, ohmic discharges: An electrode-centered review on discharge modes and the transitions between them", *Appl. Phys. Rev.* 11, 031310 (2024)](https://doi.org/10.1063/5.0205274) | full-text | Cathode sheath voltages of glow and arc discharges; arc burning voltages; the 1 A and 100 V classification. First 100 000 characters read. |
