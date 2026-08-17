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
related:
  - photoelectric-threshold
  - quantum-hall-effect
  - josephson-effect
updated: 2026-08-17
---

# Coulomb Blockade (Single-Electron Charging Gate)

### 4.1 Effect Name

Coulomb blockade (single-electron charging gate)

### 4.2 Macroscopic Observation

A small conducting island, tunnel-coupled to leads, passes no current in a window of bias and gate voltage around the charge-degeneracy points. Adding one electron costs a charging energy that is visible as a Coulomb diamond or a Coulomb staircase. Raising temperature, enlarging the island, or making the tunnel resistance too small washes the blockade out and restores a smooth conductance.

### 4.3 Established Quantitative Boundaries

- Charging energy of an island with capacitance \(C\):

  \[
  E_c = \frac{e^2}{2C}.
  \]

  For \(C = 1\,\mathrm{fF}\), \(E_c \approx 80\,\mu\mathrm{eV} \approx k\times 0.93\,\mathrm{K}\). Laboratory SET islands sit in the aF–fF class so that \(E_c\) is above the mixing-chamber \(kT\).

- Orthodox operating window (both required):

  \[
  kT \ll E_c, \qquad R_T \gg R_Q = \frac{h}{e^2} \approx 25813\,\Omega.
  \]

  If \(R_T\) is not large compared with \(R_Q\), charge on the island is not a well-defined integer and the blockade is smeared by quantum fluctuations.

- Bias / gate: current is blocked for \(|eV| \lesssim E_c\) except at charge-degeneracy (gate-tuned) points, where single-electron tunneling proceeds.

**Data confidence:** High — diamonds, the \(e^2/2C\) scale, and the \(T\) / \(R_T\) collapses are standard mesoscopic facts. Any one device’s \(C\) is medium (geometry).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms. Orthodox Coulomb-blockade theory compares the electrostatic energy of \(N\) versus \(N+1\) electrons on the island with \(kT\) and \(eV\). The Coulomb staircase is the \(I(V)\) of that comparison. These describe the observed blockade. They do not derive \(e\) from a node rule.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One island whose \(C\) makes \(E_c\) larger than \(kT\), plus two (or more) high-resistance tunnel barriers. The island is the buffer: too large \(\to\) \(E_c\) vanishes into \(kT\). One conversion event is one electron. Area of the leads is capacity.

- **Clock rate / latency.** Tunnel rate \(\sim (e^2 R_T C)^{-1}\) class, set by \(R_T\) and \(C\). Observation faster than charging is not a blockade reading.

- **Energy barriers or thresholds.** \(E_c\) is the load-bearing gate. It is a charging threshold, not an anisotropy latch and not a work function. The electron that tunnels *leaves* or *arrives*; the island’s \(N\) is the written integer only while \(R_T\) keeps it discrete.

- **Dominant failure modes.**
  - Thermal: \(kT \gtrsim E_c\) \(\to\) diamonds wash out.
  - Spatial: island too large (\(C\) up, \(E_c\) down) \(\to\) same washout.
  - Resistance: \(R_T \lesssim R_Q\) \(\to\) \(N\) not sharp \(\to\) no blockade.
  - Bias: \(|eV| \gg E_c\) \(\to\) the gate is overrun (current flows; that is operation outside the blockaded window).

- **Emergent constant or stable output.** A bias/gate window of vanishing current, and a staircase / diamond pattern with period \(e\) on the island, while \(T\), \(C\), and \(R_T\) remain inside the envelope.

### 4.6 Internal Consistency Notes

This is the charging twin of the photoelectric \(N=1\) gate: one electron is the event, but the threshold is electrostatic, not \(\varphi\). Do not identify \(E_c\) with a work function or with \(h/e^2\) Hall plateaus. \(R_Q = h/e^2\) here is a *resistance floor for charge quantization*, not a Hall output.

Whether a blockaded island is a latch (held \(N\) at 0 W) or a gate (transport event) depends on the observation. The *blockade of current* is this file’s effect; remnant charge on an isolated island is a cousin, not a second family.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(E_c\), the \(kT\) and \(R_T\) collapses, and the single-electron period are sharp and translate directly into buffer, barrier, and failure specifications.

## Related entries

- [photoelectric-threshold](photoelectric-threshold.md) — another \(N=1\) electron gate; \(\varphi\), not \(E_c\)
- [quantum-hall-effect](quantum-hall-effect.md) — \(h/e^2\) as a resistance *output*, not as this \(R_T\) floor
- [josephson-effect](josephson-effect.md) — Cooper-pair charging (Cooper-pair box) is a harder related case and is not this normal-island file
