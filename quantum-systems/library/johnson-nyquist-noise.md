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
related:
  - thermal-equilibrium-temperature
  - brownian-motion
  - electron-heat-capacity
  - superconductivity
  - skin-effect
updated: 2026-08-17
---

# Johnson–Nyquist Noise (Thermal Voltage Average)

### 4.1 Effect Name

Johnson–Nyquist noise (thermal voltage average)

### 4.2 Macroscopic Observation

An unbiased resistor in equilibrium with a heat bath produces a fluctuating open-circuit voltage. The mean voltage is zero; the mean-square voltage grows with the thermometer reading, with the resistance, and with the bandwidth of the filter through which the resistor is observed. A short (\(R\to 0\)) is quiet in voltage. A measurement taken in a vanishing bandwidth is quiet. Cooling the resistor toward \(T=0\) kills the classical noise. The same resistor still has a definite \(R\) and, in a metal, a Fermi surface; the noise is not the [electron heat capacity](electron-heat-capacity.md) and is not a transport threshold. It is the electrical reading of a thermal average.

### 4.3 Established Quantitative Boundaries

- Classical Nyquist envelope (Johnson 1928; Nyquist 1928), one-sided voltage spectral density:

  \[
  \langle V^{2}\rangle = 4kTR\,\Delta f
  \]

  with \(k = 1.380649\times 10^{-23}\,\mathrm{J\,K^{-1}}\) (defined). At \(300\,\mathrm{K}\), a \(1\,\mathrm{k}\Omega\) resistor delivers \(\approx 4.07\,\mathrm{nV\,Hz^{-1/2}}\); a \(50\,\Omega\) resistor delivers \(\approx 0.91\,\mathrm{nV\,Hz^{-1/2}}\). These are the everyday floor of a quiet voltage measurement.
- Equivalent current form for a resistor held at zero voltage: \(\langle I^{2}\rangle = 4kT\Delta f/R\).
- The classical envelope fails when the observation frequency is no longer small compared with \(kT/h\) (\(\approx 6.25\,\mathrm{THz}\) at \(300\,\mathrm{K}\); tens of gigahertz at a few kelvin). A quantum / high-frequency form exists and is recorded in §4.4 as an envelope, not as an interpretive claim.
- Collapse of the classical reading:
  - \(T\to 0\) → \(\langle V^{2}\rangle\to 0\) in the Nyquist formula.
  - \(\Delta f\to 0\) → integrated variance → \(0\).
  - \(R\to 0\) → voltage noise → \(0\) (a short). A superconductor below \(T_c\) is the clean material realization of that last limit.
- There is no universal resistor volume at which the formula “starts working.” A lithographed nanometre-scale resistor still presents \(4kTR\Delta f\) once it has a well-defined \(R\) and a bath \(T\); what changes in small devices is the appearance of extra, non-Nyquist noise (shot, telegraph, two-level systems), not a missing thermal floor.

**Data confidence:** High — the \(4kTR\Delta f\) floor is a metrological standard, reproduced from audio through microwave. The high-frequency / low-\(T\) crossover is high as a measured roll-off; the bookkeeping of any zero-point term in a given amplifier chain is medium and is not used here.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Classical Nyquist law as above. It is the fluctuation–dissipation companion of a linear resistance, the electrical analogue of \(D=kT/\gamma\) in [Brownian motion](brownian-motion.md).
- High-frequency envelope (Callen–Welton / Planck form), recorded without a zero-point interpretation:

  \[
  S_V(f) = 4R\,\frac{hf}{e^{hf/kT}-1}
  \]

  which recovers \(4kTR\) for \(hf\ll kT\) and falls exponentially for \(hf\gg kT\). Symmetric-correlator bookkeeping adds a term proportional to \(hf/2\); whether that term is an available voltage on a given bench is not settled by this entry and is not required by the collapse statement. It is a high-frequency envelope.
- \(R=R(f)\) once skin effect, leads, or dielectric loss enter. The formula uses the real part of the impedance actually presented in \(\Delta f\).

These relations describe the averaged electrical output of a thermal dissipative element. They do not derive \(k\), and they do not fix a resistor volume.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A dissipative element with a stable resistance, coupled to a thermal population that itself has a stable [temperature](thermal-equilibrium-temperature.md). The hardware scale is statistical: enough independent electronic (or other) contributors, averaged over the chosen \(\Delta f\), that the mean-square voltage is the Nyquist number rather than a single switching event. There is no universal node-count or volume cliff. Nanoscale resistors remain Nyquist until some other noise mechanism overtakes them, or until \(R\) or \(T\) ceases to be well defined.

- **Clock rate / latency.** Two clocks.
  1. The observation bandwidth \(\Delta f\). Narrowing it is a longer average and kills the integrated variance.
  2. The thermal electromagnetic / electronic clock \(kT/h\). Drive or observation above that clock leaves the classical envelope and follows the high-frequency form above.

  Ordinary audio and RF metrology sit far below \(kT/h\) at \(300\,\mathrm{K}\). Cryogenic microwave work does not.

- **Energy barriers or thresholds.** None holding a latched state. Sending the resistor into the superconducting state (\(R\to 0\)) removes the voltage noise by removing \(R\), a resource failure owned jointly with [superconductivity](superconductivity.md).

- **Dominant failure modes.**
  - Thermal: \(T\to 0\) → classical \(\langle V^{2}\rangle\to 0\).
  - Bandwidth: \(\Delta f\to 0\) → integrated variance → \(0\). The spectral density may still be \(4kTR\); the reading of a zero-width filter is not a noise power.
  - Resistance: \(R\to 0\) (short, superconductor) → voltage noise collapses; \(R\to\infty\) (open) → current noise collapses.
  - High frequency: \(hf\gtrsim kT\) → classical formula fails; the quantum envelope applies. Recorded as a clock failure of the classical output, not as a separate effect.
  - Undefined \(T\) or \(R\): the same population / exchange-window collapse as the temperature entry.

- **Emergent constant or stable output.** A white voltage floor \(4kTR\) (classical) as the electrical average of the thermal population, and a definite integrated variance once \(\Delta f\) is stated.

### 4.6 Internal Consistency Notes

The collapse — \(T\to 0\) or bandwidth \(\to 0\) — is the statistical-family failure: shrink the thermal resource, or lengthen the average until the variance is gone. That closes cleanly with [thermal equilibrium temperature](thermal-equilibrium-temperature.md) and with [Brownian motion](brownian-motion.md).

The mapping does not supply a resistor-volume cliff, and the data do not demand one. Inventing a minimum \(N\) of carriers would be a conjecture. Extra noise in small films (1/f, two-level systems) is real and is a *different* output sitting on top of the Nyquist floor; it is not the collapse of this effect.

The high-frequency form is kept as an envelope on purpose. Zero-point arguments about what a voltmeter can extract at \(T=0\) are not required by the measured roll-off and are omitted. That is a recorded gap in interpretation, not a gap in the collapse class.

[Skin effect](skin-effect.md) changes the effective \(R(f)\) of a bulk conductor and therefore the noise presented in a given band. It does not replace Nyquist; it retunes the \(R\) that Nyquist uses.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(4kTR\Delta f\), the \(T\to 0\) and \(\Delta f\to 0\) collapses, and the \(hf\sim kT\) roll-off are metrological; the QSA translation is a clean averaging-window statement and correctly refuses a universal resistor volume.

## Related entries

- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the bath average this voltage reports
- [Brownian motion](brownian-motion.md) — fluctuation–dissipation twin (\(D=kT/\gamma\))
- [Electron heat capacity](electron-heat-capacity.md) — another electronic thermal average; different buffer (Fermi-surface slice)
- [Superconductivity](superconductivity.md) — \(R\to 0\) removes the voltage noise
- [Skin effect](skin-effect.md) — frequency-dependent \(R\) that the same formula consumes
