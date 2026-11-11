---
id: magnetostriction
title: Magnetostriction (Moment–Strain Coupling)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: medium
review_depth: deep
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - elasticity
  - piezoelectricity
  - thermal-expansion
  - melting
  - magnetic-domains
updated: 2026-11-13
---

# Magnetostriction (Moment–Strain Coupling)

### 4.1 Effect Name

Magnetostriction (moment–strain coupling)

### 4.2 Macroscopic Observation

A ferromagnetic rod changes length when it is magnetized. Nickel shortens by a few tens of parts per million; Terfenol-D lengthens by about a thousand parts per million. The strain grows with the magnetization and stops growing at magnetic saturation. It falls to zero at the Curie point. A transverse change of the opposite sign accompanies the length change, so the volume stays nearly constant. The reverse coupling also exists: stress applied to the rod changes its magnetization (the Villari effect).

### 4.3 Established Quantitative Boundaries

Sizes:

- **Measured.** Nominal maximum field-induced strain at room temperature: iron −9, nickel −40, Terfenol-D 1400, Galfenol 400 (parts per million) [S1]. Nickel and the other early transducer materials stay below 100 ppm; the Tb–Dy–Fe alloys exceed 1000 ppm [S1]. Across all magnetically ordered materials the strain runs from \(10^{-8}\) to \(10^{-3}\) [S2].
- **Measured.** Single-crystal constants at room temperature, in ppm: Fe \(\lambda_{100} = 20\), \(\lambda_{111} = -21\); Ni \(\lambda_{100} = -46\), \(\lambda_{111} = -24\); Terfenol-D \(\lambda_{100} = 90\), \(\lambda_{111} = 1640\) [S2]. A second source gives Fe 20.5 and −21.5 and Ni \(\lambda_{100} = -46\) [S13]. An older survey puts nickel between 20 and 50 ppm in magnitude depending on direction [S4].
- **Measured.** Nickel near absolute zero: \(\lambda_{100} = -60\), \(\lambda_{111} = -35\) ppm [S3]; a separate extrapolation to 0 K gives −57 and −28 ppm [S5]. Iron at 4.2 K: 26 and −30 ppm [S3]. Hexagonal cobalt has four constants, \(-66\), \(-123\), \(126\) and \(-128\) ppm in Mason's notation near 0 K [S3]; a tertiary source gives 60 ppm for polycrystalline cobalt at room temperature without a sign [S12].
- **Measured.** Polycrystalline nickel, as cast, at room temperature: −35 ppm. Two atomic per cent gallium changes it to −39 ppm and seven per cent to −10 ppm [S2].
- **Model (random polycrystal).** \(\lambda_s = (2\lambda_{100} + 3\lambda_{111})/5\) [S2]. For nickel the formula is only approximate (seen as a search excerpt of a 1966 study; not opened).
- **Computed here.** That average gives −33 ppm for nickel at room temperature from [S2], −45 or −40 ppm near 0 K from [S3] or [S5], −4.6 ppm for iron and 1020 ppm for Terfenol-D. The measured room-temperature values for polycrystalline nickel, −35 and −40 ppm [S2][S1], sit beside the computed −33.
- **Measured.** Terfenol-D, \(\mathrm{(Tb_{0.3}Dy_{0.7})Fe_{1.92}}\): about 1000 ppm of linear strain in industrial material at 5 kOe [S2]; \(\mathrm{TbFe_2}\) reaches nearly 2000 ppm at 800 kA m⁻¹ [S2]; a tertiary source quotes 2000 ppm at 160 kA m⁻¹ [S12]. The figure depends on field, prestress and grain alignment [S2].
- **Measured.** Galfenol, \(\mathrm{Fe_{1-x}Ga_x}\) with \(0.13 \le x \le 0.24\): about 400 ppm [S1]; \(\tfrac32\lambda_{100}\) up to 450 ppm with the peak near 19 at.% Ga [S2]; \(3.95 \times 10^{-4}\) for quench-cooled bulk crystals [S14]; \(\lambda_{100} = 153\) and \(\lambda_{111} = -16\) ppm at 13 % Ga [S2]. Tensile strength 500 MPa and Curie temperature 700 °C [S1]. Terfenol-D is brittle [S1][S2].

Field and temperature:

- **Measured.** Field to saturate nickel. The \([100]\) direction of a nickel crystal does not saturate until the effective (internal) field reaches 300 Oe. An ellipsoid of axial ratio 5 has a demagnetizing field of about 350 Oe, so the applied field had to be 650 Oe, and a 1000 Oe solenoid saturated the crystal "under all conditions" [S4].
- **Measured.** Saturation polarization of nickel 0.60 T at 298 K; iron 2.15 T; cobalt 1.76 T [S6].
- **Computed here.** 300 Oe is \(\mu_0H = 0.030\) T and 650 Oe is 0.065 T. An isolated nickel sphere has a demagnetizing field of \(J_s/3 = 0.20\) T, so it needs about 0.23 T applied to reach the same internal field. A powder particle is close to this case; a long rod along the field is close to the 0.03 T case.
- **Measured.** Curie points: nickel 631 K in the critically evaluated tables [S7], 358 °C [S6] and about 360 °C [S4]; iron 1042 K [S7] or 770 °C [S6]; cobalt 1131 °C [S6].
- **Measured.** Temperature dependence in nickel. The constants were measured from 20 K to 630 K [S5]. The saturation strain falls to zero at the Curie point [S4]. In polycrystalline nickel the range over which the strain tracks the square of the magnetization covers only about a quarter of its fall; the remaining three quarters occur close to the Curie temperature [S4]. The magnitude at 0 K is 1.2 to 1.5 times the room-temperature value (−57 to −60 against −46; −28 to −35 against −24) [S2][S3][S5].
- **Measured.** In iron the sign of the strain changes from positive to negative as the field rises (the Villari reversal) [S1], near 40 kA m⁻¹ according to a tertiary source [S12].

Inverse effect and clamping:

- **Measured.** Applying stress changes the magnetization. This is the Villari effect and is the basis of magnetostrictive force and torque sensors [S1].
- **Convention.** Joule magnetostriction is the length change along the field with a transverse change of opposite sign and zero net volume change [S1]. Volume magnetostriction is a separate, smaller effect; in gadolinium it is proportional to the square of the magnetization [S5].
- **Model (linear magnetoelasticity).** A body free to deform takes up the magnetostrictive strain with no stress. When the deformation is hindered, as in a film held by its substrate, a stress \(\sigma^\lambda = \lambda_s E/(1+\nu)\) appears instead [S11]. Saturating along two perpendicular directions in turn gives a strain difference of \(\tfrac32\lambda_s\) [S11].
- **Measured.** Inputs for nickel: Young's modulus 199.5 GPa (soft) to 219.2 GPa (hard), Poisson ratio 0.312 [S8]; yield constant of Nickel 200 at room temperature and a strain rate of 1 s⁻¹, 163 MPa; density 8900 kg m⁻³; specific heat 446 J kg⁻¹ K⁻¹ [S10]; linear expansivity \(13.4 \times 10^{-6}\) K⁻¹ at 293 K [S9].
- **Computed here.** Stress if a nickel grain were fully clamped along the strain: \(E\lambda_s = 7.0\) MPa for soft nickel at 35 ppm and 8.8 MPa for hard nickel at 40 ppm; the film form of [S11] gives 5.3 MPa. These are 4.3 % to 5.4 % of the 163 MPa yield constant. The elastic strain at yield, \(163\ \mathrm{MPa}/199.5\ \mathrm{GPa} = 8.2 \times 10^{-4}\), is 23 times the magnetostrictive strain.
- **Computed here.** Thermal strain of nickel for a 10 K rise: \(1.34 \times 10^{-4}\), which is 3.8 times a 35 ppm magnetostriction and 3.4 times a 40 ppm one. The whole saturation strain of nickel equals the thermal expansion from a rise of 2.6 to 3.0 K.
- **Computed here.** Elastic energy stored by clamping a 35 ppm strain: \(\tfrac12E\lambda_s^2 = 122\) J m⁻³. The heat capacity of nickel is \(3.97 \times 10^{6}\) J m⁻³ K⁻¹, so that energy equals a temperature rise of \(3.1 \times 10^{-5}\) K.
- **Convention.** Holding the saturated strain costs no power beyond what holds the magnetization.

**Data confidence:** High for nickel, iron, Terfenol-D and Galfenol, each read in two full-text sources that agree within the stated spread. The polycrystalline cobalt value and the Villari-reversal field rest on a tertiary source. The nickel temperature curve comes from two theses, one read as a scan and one as an abstract. The Curie temperature of Terfenol-D was not found.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Saturated strain at angle \(\theta\) to the magnetization, isotropic form:

  \[
  \frac{\Delta L}{L} = \frac32\lambda_s\Bigl(\cos^2\theta - \frac13\Bigr)
  \]

  The strain depends on \(\cos^2\theta\). Reversing the magnetization leaves it unchanged. The difference between parallel and perpendicular saturation is \(\tfrac32\lambda_s\) [S11].
- Polycrystal average: \(\lambda_s = (2\lambda_{100} + 3\lambda_{111})/5\) [S2].
- Clamped stress: between \(\lambda_sE/(1+\nu)\) for a film on a substrate [S11] and \(E\lambda_s\) for a bar held at both ends.
- Inverse effect: stress adds a uniaxial term of order \(\tfrac32\lambda_s\sigma\) to the anisotropy energy and shifts \(M(H)\) [S11].

These relations describe the measured strain. They do not compute why Terfenol-D reaches \(10^{-3}\) and nickel \(4 \times 10^{-5}\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** An ordered magnetic population in a deformable lattice. The strain is a property of the domain; a macroscopic length change needs the domain population redistributed or rotated by a field. A paramagnet has the lattice and no ordered moment.

- **Clock rate / latency.** Magnetic side: the domain-wall and rotation clocks of the magnet entries. Mechanical side: the acoustic transit of [elasticity](elasticity.md). No clock of its own.

- **Energy barriers or thresholds.** No separate magnetostrictive latch. The thresholds are the host magnet's: the Curie point and the field needed to align the moment. The magnetoelastic energy is small: 122 J m⁻³ in clamped nickel.

- **Dominant failure modes.**
  - **Threshold** — thermal: above the Curie point (631 K in nickel) the strain is zero. Below it the strain falls continuously with the magnetization, most steeply close to the transition.
  - **Crossover** — field: the strain follows \(M(H)\) and saturates. In nickel the internal field needed is about 300 Oe; the applied field depends on shape through the demagnetizing factor, about 0.23 T for a sphere.
  - **Crossover** — clamping: a constrained body shows stress in place of strain, linearly, up to \(E\lambda_s\) (7 to 9 MPa in nickel). A free body shows strain and no stress.
  - **Crossover** — composition: the coupling is a material number that passes through zero in some alloys; 7 at.% Ga takes nickel from −35 to −10 ppm.
  - **Threshold** — lattice: melting removes the solid (owned by [melting](melting.md)).

- **Emergent constant or stable output.** A saturation strain fixed by the material and the direction of the moment (−33 to −40 ppm in nickel at room temperature), even in the moment's direction, together with the inverse stress-to-magnetization channel.

### 4.6 Internal Consistency Notes

Filing under lattice-modes with `mechanical-lattice` and `thermal` tags fits: the output is a strain, and it ends at the Curie point or at melting. The latch entry owns remanence and coercivity.

Sourcing changed the mapping in three places. First, the magnitude. In nickel the full saturation strain is 35 to 40 ppm. Clamped completely, it produces 5 to 9 MPa, about a twentieth of the yield stress of annealed nickel, and it equals the thermal expansion from a 3 K rise. A pulse that heats a particle by 10 K strains it almost four times as much as full magnetic saturation does. The first version called severe shock through this coupling a route to scrambling a magnet and treated magnetostriction as a way to work the lattice; no opened source supports either, and the arithmetic is against the second. Second, a free particle. A single particle that is free to change shape takes the strain without stress, so loose powder is the least favourable case for producing magnetostrictive stress; stress needs a constraint, such as a neighbouring grain of different orientation or a rigid matrix, and is then bounded by the figures above. Third, the symmetry. The strain is even in the magnetization, so a moment that reverses carries the same strain. A statement that the strain averages to zero whenever the moment does is not correct for reversal along one axis; it holds only when the direction is sampled isotropically.

The mapping remains open on the size of the coupling. Why \(\lambda_s\) is \(4 \times 10^{-5}\) in nickel and \(10^{-3}\) in Terfenol-D is taken as data, as \(d_{33}\) is on [piezoelectricity](piezoelectricity.md). No source was opened on cyclic magnetostrictive loading, so nothing here speaks to fatigue under many pulses.

Invar's low expansion is attributed to a magnetic volume effect; [thermal-expansion](thermal-expansion.md) owns that statement.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the Curie threshold, the saturation with field and the lock of strain to the moment's axis are measured and consistent with the magnet entries, but \(\lambda_s\) is a handbook coupling and is not derived.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — the directional latch; this file is the length change tied to that moment
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — \(M(H)\) that the strain follows
- [elasticity](elasticity.md) — moduli and yield stress used for the clamped-stress comparison
- [piezoelectricity](piezoelectricity.md) — the charge analogue
- [thermal-expansion](thermal-expansion.md) — the thermal strain used for scale; Invar
- [melting](melting.md) — loss of the solid
- [magnetic-domains](magnetic-domains.md) — the population that a field redistributes

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Deng and Dapino, "Magnetostrictive Devices", *Wiley Encyclopedia of Electrical and Electronics Engineering* (2016)](https://u.osu.edu/smsl/files/2021/06/7-DENG_dapino_magnetostrictive_devices.pdf) | full-text | Table of nominal strains (Fe −9, Ni −40, Terfenol-D 1400, Galfenol 400 ppm); Joule and Villari effects; zero volume change; Villari reversal in iron; Galfenol strength and Curie temperature. |
| S2 | [Grössinger, Sato Turtelli and Mehmood, *IOP Conf. Ser.: Mater. Sci. Eng.* 60, 012002 (2014)](https://doi.org/10.1088/1757-899X/60/1/012002) | full-text | Single-crystal constants of Fe, Ni and Terfenol-D; polycrystal formula; polycrystalline Ni −35 ppm and Ni–Ga; Terfenol-D and TbFe2 strain against field; Fe–Ga values; range of the effect. |
| S3 | [Nieves et al., "MAELAS", *Comput. Phys. Commun.* (2021), arXiv:2009.01638](https://arxiv.org/abs/2009.01638) | full-text | Experimental low-temperature constants of Ni, Fe and hcp Co quoted beside the calculations (secondary for those measurements). |
| S4 | [Hunt, "The temperature dependence of magnetostriction in a nickel crystal", PhD thesis, Durham (1954)](https://etheses.durham.ac.uk/id/eprint/9310/) | full-text | Field to saturate nickel along [100]; demagnetizing field of the specimen; Curie point near 360 °C; strain falling to zero there; 20–50 ppm by direction. Read as a scanned copy. |
| S5 | [Hutchinson, "The magnetostriction of nickel and gadolinium", PhD thesis, Durham (1958)](https://etheses.durham.ac.uk/id/eprint/9170/) | abstract | Nickel measured from 20 K to 630 K; 0 K values −57 and −28 ppm; volume magnetostriction of gadolinium. |
| S6 | [University of Birmingham, "Magnetic Materials: Properties" (teaching note)](https://www.birmingham.ac.uk/Documents/college-eps/metallurgy/research/Magnetic-Materials-Background/Magnetic-Materials-Background-5-Properties.pdf) | full-text | Saturation polarization and Curie temperature of Fe, Co and Ni (secondary). |
| S7 | [NIST-JANAF Thermochemical Tables, 4th ed., nickel and iron reference states](https://janaf.nist.gov/tables/Ni-001.html) | full-text | Magnetic transition of nickel at 631 K and of iron at 1042 K. |
| S8 | [Kaye and Laby, *Tables of Physical and Chemical Constants*, §2.2.2 Elasticities and strengths (NPL, archived)](https://web.archive.org/web/2018/http://www.kayelaby.npl.co.uk/general_physics/2_2/2_2_2.html) | full-text | Young's modulus and Poisson ratio of soft and hard nickel. |
| S9 | [Kaye and Laby, §2.3.5 Thermal expansion (NPL, archived)](https://web.archive.org/web/2019/http://www.kayelaby.npl.co.uk/general_physics/2_3/2_3_5.html) | full-text | Linear expansivity of nickel at 293 K. |
| S10 | [Johnson and Cook, *Proc. 7th Int. Symp. on Ballistics*, The Hague (1983)](https://archive.org/details/AConstitutiveModelAndDataForMetals) | full-text | Nickel 200: yield constant 163 MPa, density and specific heat. Table read from the page image. |
| S11 | [Jay, Le Berre, Pogossian and Indenbom, "Direct and inverse measurement of thin films magnetostriction", arXiv:0911.1914](https://arxiv.org/abs/0911.1914) | full-text | Magnetostrictive stress when deformation is hindered; the 3/2 λs difference; stress-induced anisotropy. |
| S12 | [Wikipedia, "Magnetostriction"](https://en.wikipedia.org/wiki/Magnetostriction) | full-text | Tertiary: cobalt 60 ppm; Terfenol-D 2000 ppm at 160 kA/m; Villari reversal near 40 kA/m. |
| S13 | [MIT OpenCourseWare 3.45 Magnetic Materials, chapter 7 problems (2004)](https://ocw.mit.edu/courses/3-45-magnetic-materials-spring-2004/1f1fd3b19bca0b3fb41ef16ba2fb7862_probs_7.pdf) | full-text | Secondary: Fe 20.5 and −21.5 ppm; Ni λ100 −46 ppm. |
| S14 | [Parkes et al., "Magnetostrictive thin films for microwave spintronics", arXiv:1302.5097](https://arxiv.org/abs/1302.5097) | full-text | Bulk quench-cooled Fe–Ga value of 3/2 λ100 quoted for comparison (secondary). |
