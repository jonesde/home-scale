---
id: coulomb-blockade
title: Coulomb Blockade (Single-Electron Charging Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - thermal
  - spatial-buffer
confidence_data: high
confidence_mapping: high
review_depth: light
related:
  - photoelectric-threshold
  - quantum-hall-effect
  - josephson-effect
updated: 2026-11-11
---

# Coulomb Blockade (Single-Electron Charging Gate)

### 4.1 Effect Name

Coulomb blockade (single-electron charging gate)

### 4.2 Macroscopic Observation

A small conducting island coupled to leads through tunnel barriers passes no current in a window of bias and gate voltage. Adding one electron costs a charging energy, and the conductance shows oscillations that are periodic in gate voltage. Raising the temperature, enlarging the island or opening the barriers reduces the effect continuously until a smooth conductance remains.

### 4.3 Established Quantitative Boundaries

- **Convention.** Charging energy. One source defines \(E_C = e^2/2C\) for an island of capacitance \(C\) [S2]; the standard review uses \(e^2/C\), the change in electrostatic energy for one added electron [S1]. This file uses \(e^2/2C\).
- **Computed here.** For \(C = 1\) fF, \(e^2/2C\) is 80 µeV, which is \(k_B \times 0.93\) K; \(e^2/C\) is twice that, 160 µeV or 1.86 K. For 1 aF, \(e^2/2C\) is 80 meV, \(k_B \times 930\) K [S4].
- **Measured.** First devices: tunnel junctions with capacitance of about 1 fF or less showed structure in the current–voltage curve that arises from the tunneling of individual electrons charging and discharging the capacitance, in agreement with a model of charging energies and voltages of \(e/C\) [S3]. A metal grain of about 10 nm can have a charging energy as large as 100 meV, so that single-electron effects occur up to room temperature [S1].
- **Computed here.** A charging energy \(e^2/C\) of 100 meV corresponds to 1.6 aF. The voltage \(e/C\) is 0.16 mV at 1 fF.
- **Model (uncertainty estimate, orthodox theory).** Two conditions for effects of discrete charge: \(e^2/C \gg k_BT\) and tunnel resistance \(R_t \gg h/e^2\). The second follows from requiring the energy uncertainty \(h/(R_tC)\) of the charging time \(R_tC\) to be small against \(e^2/C\) [S1]. \(h/e^2 = 25\,812.807\ \Omega\) [S4].
- **Computed here.** The charging time \(R_tC\) is 0.1 ns for 100 kΩ and 1 fF.
- **Measured.** Strong coupling. The blockade is destroyed when the conductance to the leads reaches about \(2e^2/h\) [S1]. With one tunable channel swept from a tunnel barrier to a ballistic contact, charge quantization falls as the square root of the residual reflection probability on approaching the ballistic point, and at raised temperature thermal fluctuations suppress it exponentially [S2].
- **Measured.** Period. Conductance oscillations are periodic in gate voltage with period \(e/C_g\), and current steps occur at bias intervals of about \(e/C\) [S1].

**Data confidence:** High — the charging scale, the two conditions and the periodicity were read in a full-text review [S1] and a full-text experiment [S2]. The first observation was read in its abstract [S3]. The capacitance of any one device is Medium.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Charging energy: \(E_C = e^2/2C\) (or \(e^2/C\); see §4.3).
- Conditions [S1]:

  \[
  R_t \gg \frac{h}{e^2}, \qquad \frac{e^2}{C} \gg k_BT
  \]

- Gate period: \(\Delta V_g = e/C_g\) [S1].
- Near the ballistic limit of one channel with reflection probability \(1-\tau\), the quantized part of the charge scales as \(\sqrt{1-\tau}\) [S2].

Orthodox theory compares the electrostatic energy of \(N\) and \(N+1\) electrons on the island with \(k_BT\) and \(eV\). It does not derive \(e\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One island whose capacitance makes the charging energy exceed \(k_BT\), and tunnel barriers of high resistance. The island is the buffer: a larger island has a larger \(C\) and a smaller gate. One conversion event is one electron.

- **Clock rate / latency.** The charging time \(R_tC\), 0.1 ns for 100 kΩ and 1 fF.

- **Energy barriers or thresholds.** The charging energy is the load-bearing gate: 80 µeV at 1 fF, 80 meV at 1 aF. It is electrostatic. It is not an anisotropy latch and not a work function.

- **Dominant failure modes.**
  - **Crossover** — thermal: thermal fluctuations suppress charge quantization exponentially as \(k_BT\) approaches the charging energy. The condition \(e^2/C \gg k_BT\) is a convention for "well inside".
  - **Crossover** — island size: the gate falls as \(1/C\).
  - **Crossover** — coupling: quantization falls as the square root of the residual reflection of a channel and reaches zero at a ballistic contact, about \(2e^2/h\). \(R_t \gg h/e^2\) is an order-of-magnitude condition, not a floor at 25.8 kΩ.
  - **Threshold** — bias: beyond the blockade voltage, of order \(e/C\) and periodic in gate voltage, current flows. The edge is rounded by temperature.

- **Emergent constant or stable output.** A window of bias and gate voltage with suppressed current, and oscillations with a gate period of one electron charge, \(e/C_g\).

### 4.6 Internal Consistency Notes

One electron is the event, as in the photoelectric gate, but the threshold is electrostatic and set by a capacitance. The charging energy is not a work function, and \(h/e^2\) enters here as the scale of tunnel resistance above which the island charge is well defined, not as a Hall plateau.

Sourcing changed no number: 80 µeV and 0.93 K at 1 fF and \(h/e^2\) are confirmed. It changed the form of three of the four failure modes. The first version called the temperature and tunnel-resistance collapses sharp. Both are measured crossovers with known forms: exponential in temperature, and a square-root law in the residual reflection that ends at a ballistic contact. The first version's clock, written as \((e^2R_TC)^{-1}\), was dimensionally wrong; the charging time is \(R_tC\). The two conventions for the charging energy differ by a factor of two and are now both stated.

Whether a blockaded island counts as a held integer charge or as a transport gate depends on the observation. The blockade of current is this file's effect.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the charging energy and the period of one electron translate directly into buffer, barrier and output specifications. The failure envelope is a set of crossovers in temperature, size and coupling, with one bias threshold.

## Related entries

- [photoelectric-threshold](photoelectric-threshold.md) — another \(N=1\) electron gate; \(\varphi\), not \(E_c\)
- [quantum-hall-effect](quantum-hall-effect.md) — \(h/e^2\) as a resistance *output*, not as this tunnel-resistance scale
- [josephson-effect](josephson-effect.md) — Cooper-pair charging (Cooper-pair box) is a harder related case and is not this normal-island file

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Kouwenhoven et al., "Electron transport in quantum dots", in *Mesoscopic Electron Transport* (Kluwer, 1997)](https://courses.physics.illinois.edu/phys598MN/sp2012/readings/Dots_Review.pdf) | full-text | Review: charging energy e²/C; the two conditions and the uncertainty argument; 10 nm grain with 100 meV; blockade destroyed near 2e²/h; gate period e/Cg and bias steps e/C. |
| S2 | [Jezouin et al., "Controlling charge quantization with quantum fluctuations", *Nature* 536, 58 (2016), arXiv:1609.08910](https://arxiv.org/pdf/1609.08910) | full-text | E_C = e²/2C; charge quantization against channel transmission from tunnel to ballistic: square-root law; exponential thermal suppression. |
| S3 | [Fulton and Dolan, "Observation of single-electron charging effects in small tunnel junctions", *Phys. Rev. Lett.* 59, 109 (1987)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.59.109) | abstract | Junctions of about 1 fF or less; structure from tunneling of individual electrons; voltage e/C. |
| S4 | [NIST, CODATA 2022 recommended values: von Klitzing constant (with the pages for e and k)](https://physics.nist.gov/cgi-bin/cuu/Value?rk) | full-text | h/e² = 25 812.807 Ω; constants for the charging energies. |
