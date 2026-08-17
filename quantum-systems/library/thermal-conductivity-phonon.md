---
id: thermal-conductivity-phonon
title: Phonon Thermal Conductivity (Mean-Free-Path Transport)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - thermal
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
related:
  - phonon-dispersion
  - speed-of-sound
  - debye-cutoff
  - elasticity
  - melting
  - thermal-expansion
  - electron-heat-capacity
updated: 2026-08-17
---

# Phonon Thermal Conductivity (Mean-Free-Path Transport)

### 4.1 Effect Name

Phonon thermal conductivity (mean-free-path transport)

### 4.2 Macroscopic Observation

An electrical insulator carries a steady heat current under a temperature gradient. In a good crystal the thermal conductivity \(\kappa\) is small at the lowest temperatures, rises steeply, peaks at an intermediate temperature (often tens of kelvin), and then falls toward room temperature and above. An amorphous solid of similar composition conducts much less heat and lacks that crystal-style peak. Metals are excluded from this entry: their heat current is dominated by the electronic channel.

### 4.3 Established Quantitative Boundaries

- Descriptive kinetic structure, used as data: \(\kappa = \frac13 C\, v\, \ell\), with \(C\) the phonon heat capacity per volume, \(v\) a mean acoustic speed, and \(\ell\) the phonon mean free path.
- Low \(T\), clean crystal (Casimir / boundary-scattering limit): \(\ell\) saturates at the specimen size, \(C \propto T^3\) (`debye-cutoff`), so \(\kappa \propto T^3\). The buffer that limits transport is then the sample itself.
- Intermediate \(T\): \(\kappa\) peaks, then falls as phonon–phonon umklapp scattering shortens \(\ell\). At high \(T\), \(C\) has saturated and \(\ell\) continues to drop, so \(\kappa\) falls (often roughly as \(1/T\) in simple crystals).
- Crystal vs amorphous: the same chemical substance as a glass shows a much shorter \(\ell\) and no umklapp peak of the crystal kind. Room-temperature class: diamond \(\kappa \sim 10^3\,\mathrm{W\,m^{-1}\,K^{-1}}\); typical oxide glasses \(\kappa \sim 1\,\mathrm{W\,m^{-1}\,K^{-1}}\).
- Umklapp requires the reciprocal lattice of `phonon-dispersion`. Normal phonon–phonon processes do not by themselves degrade a heat current in the Peierls accounting; umklapp does.
- This channel collapses if the grid is destroyed (`melting`) or if \(T\to 0\) (\(C\to 0\)). It is not the electronic Wiedemann–Franz channel.

**Data confidence:** High — the \(\kappa(T)\) peak, the low-\(T\) size effect, the crystal / glass contrast, and the diamond-vs-glass class are multiply reproduced. Any one peak temperature or residual-resistivity-style \(\ell\) is sample-dependent (medium).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Kinetic formula:

  \[
  \kappa = \frac13 C\, v\, \ell
  \]

  Equivalent, in a single-mode relaxation picture, to an integral of \(C(\omega) v^2 \tau(\omega)\) over the phonon spectrum. The factor \(1/3\) is a kinetic average, not a derived node rule.

- Casimir limit (low \(T\), boundary-dominated \(\tau\)): \(\ell \sim L_{\mathrm{sample}}\) (up to a geometric factor of order one). Then \(\kappa \propto C(T) \propto T^3\) in an insulator.

- Umklapp: a three-phonon process that consumes a reciprocal-lattice vector and relaxes crystal momentum. The rate rises with the thermal population of the large-\(q\) modes; the conventional high-\(T\) statement is \(\ell \propto 1/T\).

- Fourier readout: \(\mathbf{j}_Q = -\kappa\nabla T\), valid when the gradient is gentle on the scale of \(\ell\). Ballistic flow across a device thinner than \(\ell\) is outside that continuum statement.

The formula organizes measured \(\kappa\). It does not predict the peak value of a given crystal from first node rules (isotope mix, anharmonicity, dislocation density).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A lattice that supports propagating acoustic modes, plus a mean free path. In the Casimir limit the spatial buffer *is* the specimen: shrinking \(L\) lowers \(\kappa\) at low \(T\). In a glass the effective \(\ell\) is already microscopic and the crystal-style peak never forms. A metal’s phonon channel is present but is not the macroscopic \(\kappa\) this entry maps.

- **Clock rate / latency.** Carrier speed \(v\) is the long-wave acoustic slope (`speed-of-sound`). The transport clock is the scattering time \(\tau = \ell/v\): boundary-limited and long at low \(T\), umklapp-limited and short at high \(T\). Zone-boundary / Debye periods remain the underlying oscillator clocks (`debye-cutoff`).

- **Energy barriers or thresholds.** No latched barrier. Umklapp is a kinematic threshold in the phonon population (enough large-\(q\) modes occupied) rather than an activation barrier that stores a state. \(T\to 0\) starves \(C\); \(T\to T_m\) removes the grid.

- **Dominant failure modes.**
  - Mean free path: umklapp, defects, isotopes, or amorphization → \(\ell\) collapses → \(\kappa\) falls. This is the load-bearing failure of the *transport* spec.
  - Spatial: specimen size below the intrinsic \(\ell\) (Casimir) → \(\kappa\) set by \(L\), not by bulk scattering.
  - Thermal, low: \(C\to 0\) as \(T\to 0\) → no heat capacity to carry.
  - Thermal / mechanical, high: melting → the crystalline phonon population is gone.
  - Channel confusion: measuring a metal and attributing \(\kappa\) to phonons → wrong machine.

- **Emergent constant or stable output.** A material- and size-dependent \(\kappa(T)\) with the crystal peak-and-fall shape, produced by a synchronized phonon population whose heat current is limited by \(\ell\).

### 4.6 Internal Consistency Notes

Factoring \(\kappa\) into \(C\), \(v\), and \(\ell\) is consistent with the other lattice-mode entries: `debye-cutoff` owns \(C(T)\), `speed-of-sound` owns \(v\), this file owns the scattering resource \(\ell\). Umklapp as the high-\(T\) killer is consistent with `phonon-dispersion` owning the zone (no reciprocal lattice, no umklapp).

The mapping takes the kinetic formula and the Peierls umklapp distinction as descriptive data. It does not yet extract a particular \(\ell(T)\) from node-level anharmonicity. That is the same anharmonicity `thermal-expansion` names without pinning to one hardware number. Mapping confidence is therefore medium: the failing resource (\(\ell\)) is correctly identified; its value is not derived.

Electronic thermal conductivity and the Wiedemann–Franz ratio belong with the electron population, not here.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the Casimir, umklapp, and crystal/glass collapses are well measured and identify \(\ell\) as the transport resource, but \(\kappa = \frac13 C v \ell\) and the umklapp rate are taken as descriptive rather than extracted from node rules.

## Related entries

- [phonon-dispersion](phonon-dispersion.md) — zone structure that makes umklapp possible
- [speed-of-sound](speed-of-sound.md) — carrier speed \(v\)
- [debye-cutoff](debye-cutoff.md) — \(C(T)\) and the mode ceiling
- [elasticity](elasticity.md) — the same moduli that set \(v\)
- [melting](melting.md) — destruction of the phonon-carrying grid
- [thermal-expansion](thermal-expansion.md) — anharmonicity, the same resource that feeds umklapp
- [electron-heat-capacity](electron-heat-capacity.md) — electronic channel, not this \(\kappa\)
