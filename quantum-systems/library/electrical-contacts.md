---
id: electrical-contacts
title: Electrical Contacts (Constriction, Softening and Melting Voltage)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - thermal
  - spatial-buffer
  - mechanical-lattice
  - field-threshold
confidence_data: medium
confidence_mapping: medium
review_depth: deep
related:
  - dielectric-breakdown
  - electrical-resistivity
  - melting
  - skin-effect
  - work-function-thermionic
updated: 2026-11-12
---

# Electrical Contacts (Constriction, Softening and Melting Voltage)

### 4.1 Effect Name

Electrical contacts (constriction, softening and melting voltage)

### 4.2 Macroscopic Observation

Two metal bodies pressed together conduct through a few small spots. The joint has more resistance than the same length of solid metal, and that resistance falls as the load rises. A surface film adds a further resistance that can be many orders larger. As the voltage across the joint is raised, the joint changes irreversibly at definite values: a film is punctured, the metal at the spot softens, and at a few tenths of a volt the spot melts, grows, and holds the voltage at that level. At about ten volts and about an ampere an arc can burn between the parted surfaces. A chain or bed of oxidised metal grains shows the same sequence in series: a high resistance that collapses by orders of magnitude once enough current is driven through it, and a low resistance that then persists until the grains are disturbed.

### 4.3 Established Quantitative Boundaries

- **Model (Holm–Maxwell spreading resistance).** A circular conducting spot (an a-spot) of radius \(a\) between like metals has constriction resistance \(R_c = \rho/2a\); between unlike metals it is \((\rho_1 + \rho_2)/4a\) [S6][S7]. The standard reference is [S8], which was not opened.
- **Computed here.** Copper, \(\rho = 1.65 \times 10^{-8}\) Ω m [S6]: 83 mΩ at \(a\) = 0.1 µm, 8.3 mΩ at 1 µm, 0.83 mΩ at 10 µm.
- **Model (plastic asperity contact).** Touching asperities deform plastically, so each carries a load equal to the hardness times its area, and the true contact area is a small fraction of the apparent area. For a clean contact with many spots, \(R_c = (\rho/2)(\pi H/F)^{1/2}\) [S6].
- **Computed here.** Copper with \(H\) = 120 kg mm⁻² and the same \(\rho\) [S6]: 5.0 mΩ at 0.01 N, 0.50 mΩ at 1 N, 0.050 mΩ at 100 N.
- **Model (film in series).** A film adds \(R_f = \rho_f d/A\). Tabulated example for a 10 µm spot with 2 nm of oxide: Cu–Cu 1.7 mΩ metal to metal against 0.18 Ω through \(\mathrm{Cu_2O}\); Al–Al 2.6 mΩ against 23.2 Ω through \(\mathrm{Al_2O_3}\) [S6].
- **Computed here.** \(\rho/a\) for that copper spot is 1.65 mΩ, so the tabulated 1.7 mΩ is twice \(\rho/2a\). The slide does not explain the factor.
- **Measured.** Load dependence with a film present. An oxidised stainless-steel bead chain at low current follows \(R_0 \propto F^{-3/2}\), against the \(F^{-1/3}\) of a clean elastic contact [S2]. Copper powder compressed up to 30 N mm⁻² follows \(R \propto P^{-1.8}\) [S5].
- **Model (Kohlrausch relation with the Wiedemann–Franz law).** The highest temperature in a constriction is set by the voltage across it: \(T_m^2 - T_0^2 = U^2/4L\), with \(L = \pi^2k^2/3e^2 = 2.45 \times 10^{-8}\) V² K⁻² [S1]; [S7] uses 2.4 × 10⁻⁸. Geometry, current and material do not enter, because the same electrons carry the heat and the charge [S1]. The Lorenz value does not apply to iron, nickel, platinum or tungsten [S7].
- **Computed here.** From \(T_0\) = 290 K with \(L = 2.45 \times 10^{-8}\) V² K⁻²: 0.2 V gives 702 K, 0.3 V gives 1001 K, 0.4 V gives 1310 K, 0.43 V gives 1404 K.
- **Model (heat diffusion).** A spot reaches its temperature in \(\tau = Ca^2/4\lambda\); for copper (\(C\) = 3.44 J cm⁻³ K⁻¹, \(\lambda\) = 4 W cm⁻¹ K⁻¹) and \(a\) = 10 µm this is 2.2 × 10⁻⁷ s [S6].
- **Computed here.** The same formula at \(a\) = 1 µm gives 2.2 × 10⁻⁹ s.
- **Measured.** Softening and melting voltages across a contact at room temperature. The values are Holm's [S8], read here in a report that reproduces his table [S9], in a tutorial [S6], in a vendor manual [S7] and in a vendor table [S11]:

  | Metal | Softening (V) | Melting (V) | Calculated melting (V) [S11] |
  |---|---|---|---|
  | Cu | 0.12 | 0.43 | 0.42 |
  | Ag | 0.09 | 0.37 | not listed |
  | Al | 0.1 | 0.3 | 0.29 |
  | Fe | 0.21 [S9]; 0.19 [S6][S11] | 0.6 [S11]; 0.19 [S6] | 0.54 |
  | Ni | 0.22 [S9]; 0.16 [S6][S11] | 0.65 [S9][S11]; 0.16 [S6] | 0.54 |
  | W | not established | 1.1 [S9] | 1.16 |

  Copper, silver and aluminium agree in every opened source. Boiling voltages in the same table are 0.8 V for copper, 0.75 V for silver and 2.1 V for tungsten [S9].
- **Measured.** Iron and nickel are disputed. Holm-derived tables give melting at 0.6 V (Fe) and 0.65 V (Ni) [S9][S11]. Timsit's table gives 0.19 V and 0.16 V for both softening and melting [S6], and his measurements found that Fe/Fe and Ni/Ni contacts melt at a lower potential drop than the voltage–temperature relation predicts, while W/W contacts did not melt at contact temperatures up to 890 °C [S10]. The iron melting digit in the scanned report [S9] is partly illegible. No opened source gives a legible softening voltage for tungsten.
- **Computed here.** The Kohlrausch relation from \(T_0\) = 293 K, with melting points of 1083 °C for copper and 660 °C for aluminium [S20], gives 0.41 V and 0.28 V. Reaching 1800 °C needs 0.64 V.
- **Convention.** Softening is read as the first drop in constriction resistance and is a narrow spread of voltages. At the melting voltage the spot collapses to a larger area and the voltage stops rising [S7]. Melting of a spot is determined by the voltage across it and not by the current [S6].
- **Measured.** Film puncture. When the field across an insulating film of about 100 Å or more reaches about 10⁵–10⁶ V cm⁻¹ (10⁷–10⁸ V m⁻¹), current starts in selected areas, heats the film and the metal under it, and punctures the film; a metallic bridge forms and the contact voltage falls suddenly [S7][S13]. Voltages below 30 mV do not permanently damage a film [S7].
- **Computed here.** At 10⁷–10⁸ V m⁻¹ a 2 nm film punctures at 0.02–0.2 V, a 10 nm film at 0.1–1 V, a 100 nm film at 1–10 V. For a film of a few nanometres the field gate and the thermal gates fall in the same range of voltage; they remain different conditions.
- **Convention.** A-fritting is the voltage-induced formation of the first conducting channel through a film. B-fritting is the current-induced widening of an existing channel [S12], terms from [S8].
- **Measured.** Probe needles on aluminium pads: A-fritting below 2.5 V with mechanical scrub, and breakdown of the film complete after about 150 µs [S12].
- **Measured.** Bead chain. Fifty oxidised stainless-steel beads of 8 mm have a resistance of 10⁴–10⁷ Ω at low current, depending on the applied force and on the film. Under rising current the voltage saturates. On reducing the current the resistance is 1–10 Ω and is set by the largest current that was applied; the change is irreversible [S1].
- **Measured.** The saturation voltage per contact, \(U_c = U_0/(N+1)\), is about 0.4 V for stainless steel, 0.2 V for bronze and 0.3 V for brass. It is constant for \(N\) from 1 to 41 beads and independent of the applied force [S1][S2]. Copper beads were not measured.
- **Computed here.** The source's example of 13 beads at \(U_0\) = 5.8 V is 0.41 V per contact.
- **Model (Kohlrausch relation applied to the measured plateau).** At 0.4 V the microcontacts reach about 1050 °C and weld ("microsoldering"); the contact radius grows from much less than 0.1 µm to about 10 µm [S1][S2]. After welding the bridge does not change for currents below the previous maximum, and each contact probably holds a single bridge [S1]. The plateau is therefore the regime in which the necks grow.
- **Measured.** Coherer. The resistance of loosely packed metal filings falls by several orders of magnitude when a spark is made nearby, and stays low until the tube is tapped. A direct-current version exists, with a transition when the source exceeds a threshold voltage [S1].
- **Measured.** Copper powder bed. Powder of median diameter 87.5 µm carrying 1200 nm of \(\mathrm{Cu_2O}\), as a 0.30 mm bed in a 10 mm die: about 10⁸ Ω up to 10 µA; the voltage climbs to 15.6 ± 2.3 V and then falls by five orders of magnitude at about 0.4 mA; afterwards the bed is ohmic at less than 1 Ω. The peak voltage is 15.6, 24.3 and 33.4 V for beds of 0.30, 0.40 and 0.50 mm [S3]. The bed shows a peak and a collapse where the bead chain shows a plateau.
- **Computed here.** Those peaks are fields of 52, 61 and 67 kV m⁻¹. Counting one median diameter per particle layer, that is 4.6–5.8 V per layer, more than ten times the bead-chain plateau.
- **Measured.** The breakdown field of that powder falls with compaction: 56.6 ± 4.5 kV m⁻¹ unloaded, 39.0 ± 5.2 at 1 MPa, 32.4 ± 5.1 at 10 MPa, 21.7 ± 4.0 at 40 MPa, 17.6 ± 3.5 at 300 MPa. Initial resistivity falls from 387 to 115 MΩ m between 0 and 40 MPa [S3].
- **Computed here.** On the same count the pressure series is 5.0 V per layer unloaded and 1.5 V per layer at 300 MPa.
- **Measured.** In another compressed copper powder (100 µm grains, about 1 MΩ) the transition to the conducting state occurs at the same dissipated Joule power whatever the applied stress [S4].
- **Measured.** Weld bridges and their weakness. Electron microscopy of the copper bed after the transition shows metal-to-metal bridges of about 10–15 µm where the oxide was removed; the authors take a local voltage above 0.6 V as enough to pass the sublimation point of \(\mathrm{Cu_2O}\), about 1800 °C. The bridges are small and the bed is weakly consolidated: a mechanical shock breaks them and returns the bed to its insulating state [S3].
- **Measured.** Drive matters. Under a voltage source, electrical sintering of silver nanoparticle structures has positive feedback: the main transition takes less than 2 µs and conductivity rises by more than five orders of magnitude, to 3.7 × 10⁷ S m⁻¹. A series resistor limits the feedback without removing it [S16][S17].
- **Model (finite element) with measurement.** Spark-plasma sintering of metal powders under pressure is the contrasting case: current density at the necks is about 5 × 10⁴ A cm⁻², the Joule overheating there is under 1 °C because heat diffuses away quickly, and densification proceeds by ordinary dislocation glide and climb with no measurable effect of the current [S18]. By the Kohlrausch relation the quantity that separates this case from the bead chain is the voltage across each contact.
- **Measured.** Contact welding on closure. When the melting voltage appears across an interface a liquid bridge forms. The first asperity to touch is so small that nearly the whole source voltage appears across it, so its temperature is set by the source voltage even when a resistor limits the current [S7].
- **Measured.** Minimum arc voltage and current in normal atmosphere, Holm's determinations with those of other observers, from a patent that reproduces his table [S14]:

  | Cathode metal | \(V_m\), Holm (V) | \(I_m\), Holm (A) | Other observers |
  |---|---|---|---|
  | Cu | 13 | 0.43 | 8.5–12.5 V; 1.15 A |
  | Ag | 12 | 0.4 | 8–12.3 V; 0.9 A |
  | W | 15 | 1.0–1.1 | 10–15.2 V; 1.27–1.75 A |
  | Al | 14 | not tabulated | 18.3 V |
  | Fe | 13–15 | 0.35–0.55 | 8.0 V; 0.73 A |
  | Ni | 14 | 0.5 | 8.0 V; 0.2 A |

  Vendor tables give 0.4–0.9 A and 11–12.5 V for silver [S7], and 12–13 V for copper, 0.8–1.2 A for tungsten, 11.2 V and 0.4 A for aluminium [S11]. The aluminium current rests on that vendor table alone.
- **Convention.** \(V_m\) and \(I_m\) are read where an established arc goes out in a purely resistive circuit. They belong to the cathode material and the atmosphere, and they are inter-related: the higher the source voltage, the lower the current at which an arc keeps burning [S7].
- **Measured.** Closure arcs in an inductive circuit start below \(V_m\). Arcs were initiated at open-circuit potentials down to the melting voltage of the electrode metal (about 0.4 V for copper, 1.1 V for tungsten) and not below it: a molten asperity bridge is pinched off and the circuit inductance supplies the voltage. No arcs formed on very smooth surfaces [S9].
- **Measured.** In hydrocarbon vapour, arcing leaves carbonaceous deposits that lower the field at which an arc starts and the minimum arc current. Platinum, palladium, gold, silver and copper are affected; tungsten, molybdenum, iron and nickel are not [S7].
- **Measured.** A burning metal-vapour arc with no magnetic field holds 15–29 V depending on the cathode material, and arc voltages stay below about 100 V when a magnetic field raises them [S15].
- **Convention.** Sliding contacts in a railgun. Armature transition is defined as the change from sliding metal-to-metal contact to plasma contact; it appears as a jump in muzzle voltage, often in two steps, one per rail [S19]. A muzzle voltage below 50 V is taken as good sliding contact and above it as loss of solid contact [S20].
- **Measured.** Solid-armature data show metal-to-metal contact failing near 1 km s⁻¹, with transition velocities of 1,030–1,575 m s⁻¹ in one study; aluminium armatures already run on a thin molten film above 700 m s⁻¹ [S19]. Average muzzle voltages of about 4 V and 12 V were measured for brush armatures at 0.81 and 0.97 MJ and about 10 V for a C-shaped armature [S20].
- **Measured.** After transition, the two electrode falls of a plasma armature total 45 ± 3 V, independent of surface state and of current density from 6 to 28 kA cm⁻², and the column adds 141 ± 4 V cm⁻¹ (about 90 V cm⁻¹ in copper vapour) [S21]. Hybrid armatures ran about 100 V below plasma armatures [S19].
- **Computed here.** A 1 cm column at 141 V cm⁻¹ plus the electrode falls is 186 V.
- **Measured.** No single transition criterion is published. A survey by six authors concludes that no one mechanism has emerged as the consensus cause; the candidates include melt waves from the velocity skin effect, wear, magnetic blow-off and falling current [S22].
- **Measured.** At zero speed, multipoint contacts did not transition when the holding force was about one gram-force per ampere through the whole pulse; transitions late in a pulse are attributed to loss of contact force as the current falls [S23].
- **Computed here.** One gram-force per ampere is 9.8 N per kiloampere.

**Data confidence:** Medium. The constriction formulas, the Kohlrausch relation, the copper, silver and aluminium voltages and the granular results were read in full text, the last in primary papers. Holm's book [S8] was not opened; every Holm value here comes from a reproduction. The iron and nickel melting voltages are disputed by a factor of three to four. The transition survey [S22], the force rule [S23], the iron and nickel melting result [S10], the neck-temperature model [S18] and part of the voltage-drive result [S17] rest on abstracts. The 30 mV level and the hydrocarbon effect each rest on one vendor manual [S7].

**Not known for a metal-powder slurry armature.** No opened source reports contact voltage, breakdown or transition data for a metal-powder paste or slurry carrying current. No saturation voltage per contact has been measured for copper beads or copper powder. No source tests whether bridges made by a conditioning current survive flow or acceleration of the powder; the static result is that a shock removes them. No source gives the current needed per unit bridge area to widen a bridge, or a film-puncture time shorter than the 150 µs above. No numeric criterion exists for the transition of a sliding contact in current per unit length, action or velocity.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Constriction and film resistance [S6][S7]:

  \[
  R_c = \frac{\rho}{2a},\qquad R_c \approx \frac{\rho}{2}\sqrt{\frac{\pi H}{F}}\ \text{(many spots, plastic)},\qquad R = R_c + \frac{\rho_f d}{A}
  \]

- Voltage–temperature relation of a spot [S1]:

  \[
  T_m^2 - T_0^2 = \frac{U^2}{4L},\qquad L = \frac{\pi^2 k^2}{3e^2}
  \]

- Thermal time of a spot, \(\tau = Ca^2/4\lambda\) [S6].
- Film puncture when \(U/d\) reaches the fritting field of the film, 10⁷–10⁸ V m⁻¹ [S7][S13].
- Chain of \(N\) beads at saturation, \(U_0 = (N+1)\,U_c\) [S1].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One a-spot. Its radius sets the resistance of the joint (0.83 mΩ at 10 µm and 83 mΩ at 0.1 µm in copper), and it is a property of load, hardness, film and current history. A welded bridge in the granular experiments is about 10–15 µm. A chain or bed is that buffer repeated: the voltage needed scales with the number of contacts in series.

- **Clock rate / latency.** The spot's thermal time, 2.2 × 10⁻⁷ s at 10 µm and 2.2 × 10⁻⁹ s at 1 µm in copper. On any pulse longer than a microsecond the spot temperature follows the instantaneous voltage. Film puncture took about 150 µs in the one timed measurement, and a voltage-driven sintering transition less than 2 µs.

- **Energy barriers or thresholds.** Three gates in series, in three different units.
  1. Film: a field of 10⁷–10⁸ V m⁻¹ across the film at its weakest point.
  2. Metal: the melting temperature of the spot, read as a voltage through the Kohlrausch relation (0.43 V for copper). The spot cannot hold more than this; it grows instead.
  3. Gap: the arc, at 12–15 V and 0.4–1.1 A in a resistive circuit, or from the melting voltage upward when an inductive circuit pinches off a molten bridge.

- **Dominant failure modes.**
  - **Threshold** — film not punctured: below the fritting field at the film's weakest point the contact stays in its high-resistance state. Which spot goes first and when is statistical.
  - **Threshold** — melting voltage: the spot voltage limits itself at the melting value (Cu 0.43 V, Ag 0.37 V, Al 0.3 V, W 1.1 V; Fe and Ni disputed between 0.16 and 0.65 V). Bead chains hold 0.2–0.4 V per contact by metal.
  - **Crossover** — softening: a narrow band of voltage, read as the first drop in resistance; 0.12 V for copper is a tabulated convention.
  - **Crossover** — load: \(R \propto F^{-1/2}\) for clean plastic contact, \(F^{-1/3}\) elastic, \(F^{-3/2}\) to \(P^{-1.8}\) with a film. No critical force.
  - **Threshold** — powder bed: an abrupt fall of five orders at a peak field that depends on the state of the bed, 57 kV m⁻¹ unloaded to 18 kV m⁻¹ at 300 MPa in one copper powder, and at a fixed dissipated power in another.
  - **Crossover** — mechanical reset: shock or tapping breaks the bridges and restores the high-resistance state. No measured scale filed.
  - **Crossover** — arc: \(V_m\) and \(I_m\) trade against each other and against the circuit; the tabulated pair is a convention for a resistive circuit. In an inductive circuit the floor for a closure arc is the melting voltage.
  - **Crossover** — sliding transition: the event is an abrupt jump in muzzle voltage, but no single variable locates it. Reported scales are about 1 km s⁻¹, about one gram-force per ampere, and the 50 V convention.

- **Emergent constant or stable output.** A metallic bridge whose resistance is set by the largest current it has carried, ohmic below that current, and retained at zero power until it is mechanically broken. While it is forming, a contact voltage clamped at the melting voltage of the metal.

### 4.6 Internal Consistency Notes

The entry sits in threshold-conversion because each step is a gate: below the film field, below the melting voltage, or below the arc minimum, the corresponding conversion does not occur. The fit is partial. The converted state persists with no power and is erased mechanically, which is the behaviour of a latch, and the entry could be argued into latched-order on that ground. It stays here because no barrier energy protecting the bridge has been measured; the only erase data are "a shock" and "tapping".

The melting-voltage gate is the cleanest part: one number per metal, independent of geometry and current, tied to the melting point by a relation with no free constant. It fails for iron and nickel, where the tabulated voltages disagree by a factor of three to four and the measured melting falls below the relation. The entry does not resolve that.

The bead chain and the powder bed do not give the same picture. The chain holds a plateau at the thermal gate. The copper bed shows a peak of several volts per particle layer and then a collapse, with a peak that falls under pressure and, in a second powder, tracks dissipated power. Whether the bed's peak is film puncture, heating, or rearrangement of the current path is not settled by the opened sources, and no buffer or barrier number is assigned to it here.

Spark-plasma sintering shows that current through a neck does not by itself heat it. The mapping therefore keys every thermal statement to the voltage per contact, which no source reports for a paste or slurry.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the three gates and the a-spot buffer are well specified for single contacts of copper, silver and aluminium, but the powder-bed transition, the erase barrier of a bridge, and the sliding transition have no closed specification, and nothing is measured for a slurry.

## Related entries

- [dielectric-breakdown](dielectric-breakdown.md) — the gas and film gates in their own right; the Paschen floor and the glow-to-arc change
- [electrical-resistivity](electrical-resistivity.md) — the bulk \(\rho\) and Lorenz number that the constriction and Kohlrausch relations use
- [melting](melting.md) — the temperature that the melting voltage stands for
- [skin-effect](skin-effect.md) — where the current flows on the way to the contact
- [work-function-thermionic](work-function-thermionic.md) — electron emission from the cathode, the supply for an arc

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Falcon and Castaing, "Electrical conductivity in granular media and Branly's coherer: A simple experiment", *Am. J. Phys.* 73, 302 (2005), arXiv:cond-mat/0407773](https://arxiv.org/abs/cond-mat/0407773) | full-text | Bead-chain resistances before and after; saturation voltage 0.4, 0.2, 0.3 V per contact by metal; the Kohlrausch relation and Lorenz value; welding at about 1050 °C; bridge frozen below the largest current; the coherer. |
| S2 | [Falcon, Castaing and Creyssels, "Nonlinear electrical conductivity in a 1D granular medium", *Eur. Phys. J. B* 38, 475 (2004), arXiv:cond-mat/0311453](https://arxiv.org/abs/cond-mat/0311453) | full-text | Saturation voltage independent of force and bead number; low-current resistance as the −3/2 power of force; microcontact temperature and growth. |
| S3 | [Aliouat et al., "Investigation of Electrical Transitions in the First Steps of Spark Plasma Sintering", *Materials* 15, 4096 (2022)](https://doi.org/10.3390/ma15124096) | full-text | Copper powder bed: resistance, peak voltage by bed thickness, collapse by five orders, breakdown field against pressure, 10–15 µm bridges, 0.6 V and the oxide sublimation point, bridges broken by shock. |
| S4 | [Falcon, Castaing and Laroche, "'Turbulent' electrical transport in copper powders", *Europhys. Lett.* 65, 186 (2004), arXiv:cond-mat/0306555](https://arxiv.org/abs/cond-mat/0306555) | full-text | Transition of compressed copper powder at a fixed dissipated power whatever the stress. |
| S5 | [Creyssels, Falcon and Castaing, "Experiment and Theory of the Electrical Conductivity of a Compressed Granular Metal", *AIP Conf. Proc.* 1145, 123 (2009)](https://labo.msc.u-paris.fr/~falcon/AIP09.pdf) | full-text | Copper powder resistance as the −1.8 power of pressure. |
| S6 | [Timsit, "Fundamental Properties of Electrical Contacts", BiTS Workshop tutorial (2006)](https://www.testconx.org/archive/archive2006/2006tutorial_timsit.pdf) | full-text | Constriction and multispot formulas, plastic asperities, film resistance example, thermal time of a spot, copper constants, table of softening and melting voltages including the low iron and nickel values. Tutorial slides. |
| S7 | [Deringer-Ney, *Ney Contact Manual*, revised 1st ed. (2022)](https://deringerney.com/wp-content/uploads/2022/04/Ney-Contact-Manual-Revised-1st-Edition.pdf) | full-text | Secondary, vendor manual: constriction formula, Lorenz value and its exceptions, softening as a spread, fritting field, 30 mV level, welding on closure, meaning of the minimum arc pair, silver values, hydrocarbon activation. |
| S8 | Holm, *Electric Contacts: Theory and Application*, 4th ed. (Springer, 1967) | cited-only | The standard reference and the origin of the softening, melting and minimum-arc tables and the fritting terms. Not opened; every value attributed to it was read in S6, S7, S9, S11, S12 or S14. |
| S9 | [Cuthrell, "Low Voltage Initiation of Damaging Arcs Between Electrical Contacts", Sandia SAND75-0103 (1975)](https://www.osti.gov/servlets/purl/4193307) | full-text | Reproduces Holm's softening, melting and boiling voltages (scan, some digits degraded); closure arcs down to the melting voltage in an inductive circuit and none on smooth surfaces. |
| S10 | [Timsit, "The 'melting' voltage in electrical contacts", *IEEE Trans. CHMT* 14, 285 (1991)](https://doi.org/10.1109/33.87306) | abstract | Fe/Fe and Ni/Ni contacts melt below the voltage the relation predicts; W/W contacts not melted at 890 °C. |
| S11 | [Doduco, Electrical Contacts Wiki, "Physical Properties of the Most Important Metals", Table 4](https://www.electrical-contacts-wiki.com/index.php/Physical_Properties_of_the_Most_Important_Metals) | full-text | Tertiary, vendor table: measured and calculated melting voltages, iron and nickel softening values, minimum arc values for copper, tungsten and aluminium. |
| S12 | [Degen, Nagler, Horn and Kaesen, "Parametric Study of Contact Fritting for Improved CRes Stability", Southwest Test Workshop (2006)](https://www.swtest.org/swtw_library/2006proc/PDF/S04_02_Degen.pdf) | full-text | Definitions of A-fritting and B-fritting (secondary to Holm); A-fritting below 2.5 V and film breakdown in about 150 µs on aluminium pads. Conference slides. |
| S13 | [US Patent 7,061,259 B2, "Inspection method and inspection apparatus" (2006)](https://patents.google.com/patent/US7061259B2/en) | full-text | Secondary: fritting field of 10⁵–10⁶ V/cm. |
| S14 | [US Patent 7,486,488 B2 (2009), Table 1](https://patents.google.com/patent/US7486488B2/en) | full-text | Secondary: reproduces Holm's table of minimum arc voltage and current with the values of other observers. |
| S15 | [Anders, "The evolution of ion charge states in cathodic vacuum arc plasmas: a review", *Plasma Sources Sci. Technol.* 21, 035014 (2012), LBNL preprint](https://www.osti.gov/servlets/purl/1055684) | full-text | Arc burning voltage 15–29 V by cathode material; below about 100 V with a magnetic field. |
| S16 | [Hummelgård, Zhang, Nilsson and Olin, "Electrical Sintering of Silver Nanoparticle Ink Studied by In-Situ TEM Probing", *PLoS ONE* 6, e17209 (2011)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3044741/) | full-text | Electrical sintering under voltage drive; a series resistor limits the feedback without removing it. |
| S17 | [Allen et al., "Electrical sintering of nanoparticle structures", *Nanotechnology* 19, 175201 (2008)](https://doi.org/10.1088/0957-4484/19/17/175201) | abstract | Positive feedback under a voltage boundary condition; main transition within 2 µs; conductivity up by more than five orders to 3.7e7 S/m. |
| S18 | [Trzaska et al., "Spark plasma sintering microscopic mechanisms of metallic systems: Experiments and simulations", *J. Am. Ceram. Soc.* 102, 654 (2019)](https://doi.org/10.1111/jace.15999) | abstract | Neck current density about 5e4 A/cm² with overheating under 1 °C; no measurable effect of current on densification. |
| S19 | [Keefer et al., "Railgun Plasma Armatures", Final Report, Univ. Tennessee Space Institute (1996), DTIC ADA311530](https://apps.dtic.mil/sti/tr/pdf/ADA311530.pdf) | full-text | Definition and voltage signature of armature transition; failure of solid contact near 1 km/s; transition velocities; hybrid armature voltage. Read in an archived copy. |
| S20 | [Wild et al., "A comparison of C-shaped and brush armature performance", *IEEE Trans. Plasma Sci.* 45, 1227 (2017), arXiv:1702.04153](https://arxiv.org/abs/1702.04153) | full-text | 50 V convention for good sliding contact; measured muzzle voltages; melting points of copper and aluminium used in the computed melting voltages. |
| S21 | [Parker, "An empirical model for plasma armature voltage", Los Alamos LA-UR-90-456 (1990)](https://www.osti.gov/servlets/purl/7247340) | full-text | Electrode drop 45 ± 3 V over 6–28 kA/cm²; column field 141 ± 4 V/cm. |
| S22 | [Barber et al., "A survey of armature transition mechanisms", *IEEE Trans. Magn.* 39, 47 (2003)](https://doi.org/10.1109/TMAG.2002.805913) | abstract | No single mechanism is the consensus cause of transition; the candidate list. |
| S23 | [Marshall, "Current carrying capacity of solid armatures for railguns at zero speed", *IEEE Trans. Magn.* 33, 125 (1997)](https://doi.org/10.1109/20.559916) | abstract | One gram-force per ampere held for the whole pulse prevents transition. |
