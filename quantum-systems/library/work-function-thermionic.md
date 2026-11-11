---
id: work-function-thermionic
title: Work Function / Thermionic Emission (Heat-Opened Surface Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: high
review_depth: standard
related:
  - photoelectric-threshold
  - ionization-threshold
  - semiconductor-gap-absorption
  - photoconductivity
  - reflection
  - blackbody-spectrum
  - stefan-boltzmann
  - thermal-equilibrium-temperature
updated: 2026-11-11
---

# Work Function / Thermionic Emission (Heat-Opened Surface Gate)

### 4.1 Effect Name

Work function / thermionic emission (heat-opened surface gate)

### 4.2 Macroscopic Observation

A hot metal surface in vacuum emits a continuous electron current. A tungsten filament at room temperature emits nothing measurable; the same filament, white-hot, supplies the cathode current of a vacuum tube or electron gun. No illumination is required. Cooling the surface extinguishes the current. A low-work-function coating (thorium on tungsten, caesium, oxide layers) gives a usable current at a lower temperature than clean tungsten.

### 4.3 Established Quantitative Boundaries

- **Measured.** Polycrystalline tungsten: 4.55 eV in one compilation [S1] and 4.54 eV in another [S2].
- **Measured.** Caesium: 1.95 eV [S1], 1.81 eV from thermionic data [S2], and 2.14 eV in an older compilation whose value a later review calls doubted [S3]. The 1.8–2.1 eV range is a spread between compilations. No opened source gives measured values for separate caesium crystal faces.
- **Measured.** Tungsten carrying a full monolayer of thorium emits as \(I = 3\,T^2\exp(-30{,}500/T)\) A cm⁻² [S4], tabulated as 2.63 eV with \(A\) = 3.0 A cm⁻² K⁻² [S2].
- **Computed here.** 30,500 K is 2.63 eV. The thorium layer lowers tungsten's barrier by 1.92 eV.
- **Measured.** Crystal faces of tungsten: (110) 5.25 eV, (100) 4.65 eV, (111) 4.47 eV [S1]; a second set gives 5.05, 4.64 and 4.39 eV [S3].
- **Computed here.** The faces span 0.78 eV in the first set and 0.66 eV in the second. A polycrystalline surface is a set of patches with different gates.
- **Computed here.** \(kT\) is 25.85 meV at 300 K and 0.2154 eV at 2500 K [S12]. For tungsten at 4.55 eV, \(\varphi/kT\) is 176 and 21.1, the Boltzmann factor \(e^{-\varphi/kT}\) is 3.7 × 10⁻⁷⁷ and 6.7 × 10⁻¹⁰, and \(\varphi/k\) is 5.28 × 10⁴ K.
- **Model (Sommerfeld free-electron gas with spin).** The theoretical Richardson constant \(A_0 = 4\pi emk^2/h^3\) is 120 A cm⁻² K⁻², an upper limit for a clean metal [S5][S2].
- **Computed here.** With CODATA 2022 constants \(A_0 = 1.2017 \times 10^6\) A m⁻² K⁻² [S12].
- **Measured.** The apparent \(A\), the intercept of a Richardson line, is 60–100 A cm⁻² K⁻² for tungsten, 60 for tantalum and 55 for molybdenum [S5]; a table lists Ni 30, Pt 32, Re 100, Cs 160, Ir 170 [S2]. The same note cites a known effect that must make the apparent \(A\) smaller than the true one by a factor of at least 2 or 3 [S5]. Composite cathodes are far lower: thorium on tungsten 3.0, barium on tungsten 1.5, mixed barium–strontium oxide about 10⁻² [S2].
- **Computed here.** The thoriated value is 40 times below \(A_0\).
- **Model (image charge in a uniform applied field).** A surface field \(F\) lowers the barrier by \(e\sqrt{eF/4\pi\varepsilon_0}\), which is \(0.0379\sqrt{F/\mathrm{MV\,m^{-1}}}\) eV; 0.268 eV at 50 MV m⁻¹ [S6].
- **Computed here.** The same formula gives 0.038 eV at 1 MV m⁻¹, 0.12 eV at 10 MV m⁻¹, 0.38 eV at 100 MV m⁻¹ and 1.2 eV at 1 GV m⁻¹.
- **Model (planar diode, zero emission velocity).** Space charge limits the steady current density that can cross a gap \(d\) at voltage \(V\) to \(J_\mathrm{CL} = (4\sqrt{2}/9)\,\varepsilon_0\sqrt{e/m}\,V^{3/2}/d^2\) [S7].
- **Computed here.** The prefactor is \(2.334 \times 10^{-6}\) A V\(^{-3/2}\).
- **Measured.** On clean, outgassed metal the thermionic and photoelectric work functions agree. Tungsten: thermionic 4.71 V and a photoelectric threshold of 2575 Å, reported as identical within the experimental error [S8]. Molybdenum: photoelectric 4.15 ± 0.02 V, thermionic 4.15 V on the same specimen [S9]. Palladium: photoelectric 4.97 ± 0.01 V, thermionic 4.99 ± 0.04 V [S10].
- **Computed here.** 2575 Å is 4.81 eV; the printed figure is illegible in the scan. The three metals agree within 0.02–0.1 eV.
- **Measured.** On a composite surface the two differ. For thoriated tungsten the thermionic and photoelectric work functions are different at low temperature and approach each other at high temperature, as expected for a nonuniform surface [S11]. In photoemission the patch with the lower work function tends to eclipse the others [S1].

**Data confidence:** High — the work functions, the Richardson form and the agreement of thermionic and photoelectric values on clean metals are multiply reproduced. The primary compilations (Kawano, Michaelson, the CRC table) were not opened; their values were read in [S1] and in a tertiary table [S2]. The thoriated-tungsten fit and the apparent \(A\) values of [S5] rest on abstracts. The apparent \(A\) and exact \(\varphi\) of a given technical surface are medium.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Richardson–Dushman current density [S2][S4]:

  \[
  J = A T^2 \exp\!\left(-\frac{\varphi}{kT}\right)
  \]

- Schottky lowering of the barrier in a surface field \(F\) [S6]:

  \[
  \Delta\varphi = e\sqrt{\frac{eF}{4\pi\varepsilon_0}},\qquad
  J = A T^2 \exp\!\left(-\frac{\varphi - \Delta\varphi}{kT}\right)
  \]

- Child–Langmuir space-charge limit between parallel plates, the ceiling on the collected current [S7]:

  \[
  J_{\mathrm{CL}} = \frac{4\varepsilon_0}{9}\sqrt{\frac{2e}{m}}\,\frac{V^{3/2}}{d^2}
  \]

- The \(\varphi\) of a Richardson line is the photoelectric threshold of the same surface when that surface is clean and uniform [S8][S9][S10]. On a patchy surface the two readings weight the patches differently and differ at low temperature [S11].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The conversion event is single-electron: one occupied state at the surface, one barrier \(\varphi\), one escape. A measurable cathode current is the summed output of a large emitting area. There is no collective coherence volume analogous to the mirror buffer of [reflection](reflection.md); reducing the area reduces the current in proportion. On a polycrystalline or coated surface the hardware is a set of patches, each with its own gate.

- **Clock rate / latency.** Attempt rates sit in the prefactor \(AT^2\). Once over the barrier, vacuum transit is set by the anode voltage and the gap; that latency belongs to collection. No opening time is filed.

- **Energy barriers or thresholds.** The operating gate is \(\varphi\): 4.55 eV for polycrystalline tungsten, 2.63 eV with a thorium monolayer, about 2 eV for caesium. Heat opens it from below by populating the Boltzmann tail; a photon with \(h\nu > \varphi\) opens the same gate from above ([photoelectric-threshold](photoelectric-threshold.md)). An applied field lowers it by \(0.038\sqrt{F/\mathrm{MV\,m^{-1}}}\) eV.

- **Dominant failure modes.**
  - **Crossover** — thermal: \(J = AT^2\exp(-\varphi/kT)\), with scale \(\varphi/k = 5.28 \times 10^4\) K for tungsten. There is no critical temperature. The Boltzmann factor is 3.7 × 10⁻⁷⁷ at 300 K and 6.7 × 10⁻¹⁰ at 2500 K, and "no measurable emission" is a statement about the instrument's floor.
  - **Crossover** — surface state: a coating, a contaminant or a different mix of faces changes \(\varphi\), by 1.92 eV for a thorium monolayer on tungsten and by up to 0.78 eV between tungsten faces. No functional form filed.
  - **Crossover** — collection: space charge caps the collected current at \(J_\mathrm{CL} \propto V^{3/2}/d^2\) while the surface gate is open.
  - **Threshold** — destruction of the emitter: melting ends the surface ([melting](melting.md)). No number filed in this entry.

- **Emergent constant or stable output.** A stable current density \(J(T,\varphi)\) from a hot surface, with no optical drive, for as long as the surface, the temperature and the collection field stay inside the envelope above.

### 4.6 Internal Consistency Notes

The mapping closes on the same surface barrier as photoelectric emission: one gate, two opening resources. That is measured on clean tungsten, molybdenum and palladium. Reflection from the same cold metal is the complementary below-threshold behaviour of the electron population ([reflection](reflection.md)).

Sourcing changed five statements. The first version called the caesium range face-dependent; it is a spread between compilations, and no face-resolved measurement was found. It said the apparent \(A\) of real surfaces is of the same order as \(A_0\); that holds for clean metals and fails for the coated cathodes the same entry names, where thoriated tungsten is 40 times lower. It stated without qualification that the thermionic \(\varphi\) is the photoelectric threshold of the same surface; on a patchy or partly covered surface the two differ at low temperature. It gave the spread between crystal faces as several tenths of an eV; tungsten spans 0.78 eV. And it called \(kT \ll \varphi\) the collapse of the effect and a temperature cliff. The Richardson law is a continuous exponential with no critical temperature, so the thermal failure mode is a crossover. The gate \(\varphi\) is sharp; its thermal opening is gradual.

The Richardson tail is the thermal occupation of states above the barrier and needs no second mechanism. A patchy surface does change the reading: a Richardson fit returns one \(\varphi\) and one \(A\) for a surface that has several gates, which is one reason the apparent \(A\) departs from \(A_0\).

A remaining gap: QSA takes \(\varphi\) as a measured surface specification. It does not derive the 4.55 eV of tungsten from a more primitive node rule. Apparent \(A\) is likewise taken as a surface datum.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the work function is a multiply measured energy gate, thermionic and photoelectric values agree on clean metals, and the mapping is the same photoelectric-class gate opened by heat. The single-gate reading applies to a uniform surface; a patchy one is several gates read as one.

## Related entries

- [photoelectric-threshold](photoelectric-threshold.md) — the same \(\varphi\) gate, opened by \(h\nu\) instead of by the thermal tail
- [ionization-threshold](ionization-threshold.md) — leaving a bound atomic state in place of a solid surface; a single-particle gate at a different energy
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — a bulk gap instead of a surface barrier; same conversion family
- [photoconductivity](photoconductivity.md) — carriers freed inside a solid and read as current, not ejected into vacuum
- [reflection](reflection.md) — below-threshold collective response of the same metal electron population
- [blackbody-spectrum](blackbody-spectrum.md) — the same hot surface as a thermal radiator
- [stefan-boltzmann](stefan-boltzmann.md) — integrated thermal emission from the hot body
- [thermal-equilibrium-temperature](thermal-equilibrium-temperature.md) — \(T\) as the ensemble coordinate that opens or closes this gate

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Tran et al., "Anisotropic work function of elemental crystals", *Surf. Sci.* 687, 48 (2019), arXiv:1902.07811](https://arxiv.org/pdf/1902.07811) | full-text | Secondary for the compilations it tabulates: polycrystalline W 4.55 eV (Kawano 2008), Cs 1.95 eV (CRC Handbook), W faces 5.25, 4.65, 4.47 eV (Derry, Kern and Worth 2015); lower-work-function patches dominate photoemission. The compilations themselves were not opened. |
| S2 | [SIMION supplemental documentation, "Richardson-Dushman Equation", Table 1](https://simion.com/definition/richardson_dushman.html) | full-text | Tertiary table: W 4.54 eV, Cs 1.81 eV, thorium on tungsten 2.63 eV with A of 3.0; apparent A for clean metals and composite cathodes; the Richardson–Dushman form and constant. |
| S3 | [Olawole et al., *Heliyon* 8, e11030 (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9626890/) | full-text | Cs 2.14 eV described as doubted; second set of W face values (4.64, 5.05, 4.39 eV). Review. |
| S4 | [Dushman and Ewald, "Electron Emission from Thoriated Tungsten", *Phys. Rev.* 29, 857 (1927)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.29.857) | abstract | Emission law for a full thorium monolayer on tungsten: A of 3 and 30,500 K. |
| S5 | [Reimann, "The Apparent Thermionic Constant A of Clean Metals", *Nature* 133, 833 (1934)](https://www.nature.com/articles/133833a0) | abstract | Upper theoretical limit of 120 A cm⁻² K⁻²; apparent A of W, Ta and Mo; apparent A below the true value by a factor of at least 2 or 3. |
| S6 | [Dowell and Schmerge, "Quantum efficiency and thermal emittance of metal photocathodes", *Phys. Rev. ST Accel. Beams* 12, 074201 (2009)](https://journals.aps.org/prab/pdf/10.1103/PhysRevSTAB.12.074201) | full-text | Schottky lowering formula and coefficient; 0.268 eV at 50 MV/m. |
| S7 | [Lau, Li and Chernin, "On the Child–Langmuir law in one, two, and three dimensions", *Phys. Plasmas* 30, 093104 (2023), arXiv:2307.14552](https://arxiv.org/pdf/2307.14552) | full-text | Child–Langmuir law and its assumptions. |
| S8 | [Warner, *Proc. Natl. Acad. Sci.* 13, 56 (1927)](https://authors.library.caltech.edu/records/5fg27-76d86/files/PNAS-1927-Warner-56-60.pdf) | full-text | Clean tungsten: thermionic 4.71 V, photoelectric threshold 2575 Å, identical within experimental error. Scan with poor text layer. |
| S9 | [DuBridge and Roehr, *Phys. Rev.* 42, 52 (1932)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.42.52) | abstract | Outgassed molybdenum: photoelectric 4.15 ± 0.02 V and thermionic 4.15 V on the same specimen. |
| S10 | [DuBridge and Roehr, *Phys. Rev.* 39, 99 (1932)](https://authors.library.caltech.edu/records/e5878-gs665) | abstract | Palladium: photoelectric 4.97 ± 0.01 V, thermionic 4.99 ± 0.04 V. |
| S11 | [King, "Photoelectric and Thermionic Investigations of Thoriated Tungsten Surfaces", *Phys. Rev.* 53, 570 (1938)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.53.570) | abstract | Thermionic and photoelectric work functions of a composite surface differ at low temperature and converge at high temperature. |
| S12 | [NIST, CODATA 2022 recommended values: Boltzmann constant (with the pages for e, the electron mass and h)](https://physics.nist.gov/cgi-bin/cuu/Value?k) | full-text | Constants used for kT, the ratios to the work function, and the Richardson constant. |
