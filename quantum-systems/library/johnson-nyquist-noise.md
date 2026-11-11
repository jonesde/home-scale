---
id: johnson-nyquist-noise
title: Johnson–Nyquist Noise (Thermal Voltage Average)
status: formal
family: ensemble-averages
constraints:
  - thermal
  - clock-latency
confidence_data: high
confidence_mapping: medium
review_depth: light
related:
  - thermal-equilibrium-temperature
  - brownian-motion
  - electron-heat-capacity
  - superconductivity
  - skin-effect
updated: 2026-11-11
---

# Johnson–Nyquist Noise (Thermal Voltage Average)

### 4.1 Effect Name

Johnson–Nyquist noise (thermal voltage average)

### 4.2 Macroscopic Observation

An unbiased resistor in equilibrium with a heat bath shows a fluctuating open-circuit voltage. Its mean is zero; its mean square grows with temperature, with resistance and with the bandwidth through which it is observed. A short is quiet in voltage, a measurement in a vanishing bandwidth is quiet, and cooling reduces the noise.

### 4.3 Established Quantitative Boundaries

- **Measured.** Statistical fluctuation of charge exists in all conductors and produces a voltage across them; the value of Boltzmann's constant obtained from the measurements lies near the accepted value [S1].
- **Model (thermodynamics and statistical mechanics).** The electromotive force is calculated from first principles and agrees with those measurements [S2]. One-sided spectral density \(4kTR\), so \(\langle V^{2}\rangle = 4kTR\,\Delta f\); the two-sided form is \(2kTR\) [S3].
- **Convention.** \(k = 1.380649\times 10^{-23}\,\mathrm{J\,K^{-1}}\) and \(h = 6.62607015\times10^{-34}\,\mathrm{J\,s}\), exact [S5].
- **Computed here.** At 300 K, \(\sqrt{4kTR}\) is \(4.07\,\mathrm{nV\,Hz^{-1/2}}\) for 1 kΩ and \(0.91\,\mathrm{nV\,Hz^{-1/2}}\) for 50 Ω.
- **Model (one-dimensional black-body radiation on a matched line).** One-sided density \(4R\,hf/(e^{hf/kT}-1)\), which recovers \(4kTR\) for \(hf\ll kT\) and decays exponentially above a cutoff of order \(kT/h\) [S3].
- **Computed here.** \(kT/h\) is 6.25 THz at 300 K, 83 GHz at 4 K and 21 GHz at 1 K.
- **Measured.** Zero-point term. The voltage noise of current-biased resistively shunted Josephson junctions agrees with a prediction that includes zero-point fluctuations generated in the shunt resistor at the Josephson frequency and mixed down to the measurement frequency [S4].
- **Measured.** Shot noise is a separate output: it follows from the quantization of charge and appears when a current flows [S6][S3].

**Data confidence:** High for the \(4kTR\Delta f\) floor. The high-frequency form is a model read in lecture notes; the zero-point observation rests on one abstract. No measurement on nanometre-scale resistors was opened, so the first version's statement that such resistors still show the Nyquist floor is unsourced and is kept only as mapping language.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Classical Nyquist law \(S_V = 4kTR\) (one-sided). It is the electrical counterpart of \(D=kT/\gamma\) in [Brownian motion](brownian-motion.md): the same Langevin equation with \(C\) for \(m\) and \(1/R\) for \(\gamma\) [S3].
- Current form for a resistor held at zero voltage: \(\langle I^{2}\rangle = 4kT\Delta f/R\) [S3].
- High-frequency form [S3]:

  \[
  S_V(f) = 4R\,\frac{hf}{e^{hf/kT}-1}
  \]

  A zero-point contribution beyond this form has been observed [S4]; its expression was not read at source and is not written here.
- \(R\) is the real part of the impedance presented in the band, including [skin effect](skin-effect.md).

These relations describe the averaged electrical output of a thermal dissipative element. They fix no resistor volume.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A dissipative element with a stable resistance, coupled to a population with a stable [temperature](thermal-equilibrium-temperature.md). The scale is statistical: enough carriers, averaged over \(\Delta f\), that the mean-square voltage is the Nyquist value. No node count or volume is attached.

- **Clock rate / latency.** Two clocks: the observation bandwidth \(\Delta f\), and \(kT/h\) (6.25 THz at 300 K, 83 GHz at 4 K). Audio and radio-frequency work at room temperature sits far below \(kT/h\); cryogenic microwave work does not.

- **Energy barriers or thresholds.** None. A superconductor below its transition removes the voltage noise by removing \(R\) ([superconductivity](superconductivity.md)).

- **Dominant failure modes.**
  - **Crossover** — thermal: \(\langle V^2\rangle\propto T\) falls continuously with \(T\) in the classical form; the zero-point term remains at high frequency.
  - **Crossover** — bandwidth: integrated variance \(\propto\Delta f\).
  - **Crossover** — resistance: voltage noise \(\propto R\), current noise \(\propto1/R\). A superconducting transition makes this a **threshold** in temperature for that material.
  - **Crossover** — high frequency: the classical value is multiplied by \(x/(e^x-1)\), \(x=hf/kT\); scale \(kT/h\).
  - **Crossover** — undefined \(T\) or \(R\): inherited from the temperature entry.

- **Emergent constant or stable output.** A white voltage floor \(4kTR\) and a definite variance once \(\Delta f\) is stated.

### 4.6 Internal Consistency Notes

The failures are the statistical-family ones: shrink the thermal resource, or lengthen the average. They match [thermal equilibrium temperature](thermal-equilibrium-temperature.md) and [Brownian motion](brownian-motion.md).

Sourcing changed one statement. The first version said the zero-point term was unsettled and left it out. It has been measured in shunted Josephson junctions, so the file now records it as an observed high-frequency contribution; what a given amplifier can extract from it remains outside this entry. The numbers are unchanged.

The mapping supplies no resistor-volume threshold. Shot noise and other excess noise are different outputs on top of the Nyquist floor: shot noise needs a current and comes from charge quantization, thermal noise needs neither.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(4kTR\Delta f\) and its dependence on \(T\), \(\Delta f\), \(R\) and \(hf/kT\) translate into an averaging-window statement with no resistor volume.

## Related entries

- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the bath average this voltage reports
- [Brownian motion](brownian-motion.md) — mechanical counterpart (\(D=kT/\gamma\))
- [Electron heat capacity](electron-heat-capacity.md) — another electronic thermal average
- [Superconductivity](superconductivity.md) — \(R\to0\) removes the voltage noise
- [Skin effect](skin-effect.md) — frequency-dependent \(R\) used by the same formula

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Johnson, "Thermal agitation of electricity in conductors", *Phys. Rev.* 32, 97 (1928)](https://doi.org/10.1103/PhysRev.32.97) | abstract | Thermal charge fluctuation in all conductors; Boltzmann's constant from the measurements near the accepted value. |
| S2 | [Nyquist, "Thermal agitation of electric charge in conductors", *Phys. Rev.* 32, 110 (1928)](https://doi.org/10.1103/PhysRev.32.110) | abstract | Thermodynamic calculation of the electromotive force, in agreement with experiment. |
| S3 | [Merhav, "Statistical Physics: a Short Course for Electrical Engineering Students", arXiv:1307.5137, §8.2 and §8.5](https://arxiv.org/abs/1307.5137) | full-text | Spectral densities 2kTR (two-sided) and 2kT/R; RC-circuit Langevin analogue; cutoff of order kT/ħ; quantum form 4R ħω/(exp(ħω/kT) − 1); shot noise from discrete charge. Lecture notes, secondary. |
| S4 | [Koch, Van Harlingen and Clarke, *Phys. Rev. Lett.* 47, 1216 (1981)](https://doi.org/10.1103/PhysRevLett.47.1216) | abstract | Voltage noise of shunted Josephson junctions in agreement with a prediction including zero-point fluctuations of the shunt resistor. |
| S5 | [NIST, CODATA 2022 recommended values: Boltzmann constant (and Planck constant, Value?h)](https://physics.nist.gov/cgi-bin/cuu/Value?k) | full-text | k and h, exact. |
| S6 | [Blanter and Büttiker, "Shot noise in mesoscopic conductors", *Phys. Rep.* 336, 1 (2000), arXiv:cond-mat/9910158](https://arxiv.org/abs/cond-mat/9910158) | abstract | Shot noise as a consequence of charge quantization. |
