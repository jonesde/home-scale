---
id: melting
title: Melting (Loss of Lattice Order)
status: formal
family: lattice-modes
constraints:
  - thermal
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
related:
  - phonon-dispersion
  - elasticity
  - speed-of-sound
  - debye-cutoff
  - thermal-expansion
  - permanent-magnet-latch
  - ferroelectric-remanence
updated: 2026-08-17
---

# Melting (Loss of Lattice Order)

### 4.1 Effect Name

Melting (loss of lattice order)

### 4.2 Macroscopic Observation

A crystalline solid held at its melting temperature coexists with a liquid of the same composition and then, with further heat, becomes liquid throughout. Bragg spots disappear and are replaced by the broad rings of a liquid structure factor. The solid’s shear restoring force is gone: the melt does not propagate a shear sound wave and does not support a static shear stress. Melting of ice, aluminum, and tungsten is reversible at the same temperature on the cooling branch once nucleation occurs (supercooling is common; the equilibrium \(T_m\) is the coexistence point).

### 4.3 Established Quantitative Boundaries

- Measured 1 atm melting points (ITS / handbook): ice \(T_m = 273.15\,\mathrm{K}\); aluminum \(T_m = 933\,\mathrm{K}\); tungsten \(T_m = 3695\,\mathrm{K}\). These are empirical failure temperatures of the respective grids, not computed outputs of a single universal formula.
- First-order character for these three: a latent heat at \(T_m\), a volume jump, and a two-phase plateau under heat input at fixed pressure.
- Lindemann criterion (conventional, not a derivation): the crystal is near melting when the fractional rms thermal displacement reaches \(\sqrt{\langle u^2\rangle}/a \sim 0.1\)–\(0.15\). The number correlates with \(T_m\) across many solids; it does not predict \(T_m\) from node rules, and the prefactor is structure-dependent.
- Structural readout: loss of crystalline Bragg order. Elastic readout: collapse of the shear modulus that `elasticity` and `speed-of-sound` assign to the solid.
- \(T_m\) is not \(\Theta_D\). Lead is already in the classical heat-capacity regime at room temperature (\(\Theta_D \sim 100\,\mathrm{K}\); `debye-cutoff`) and remains solid until \(T_m \approx 600\,\mathrm{K}\). Diamond’s \(\Theta_D\) class is \(\sim 2000\,\mathrm{K}\) and the 1 atm solid sublimes rather than showing a tungsten-style melt.
- Glasses and amorphous solids have no Bragg grid to lose; their softening is a viscosity / timescale crossover and is not this \(T_m\) cliff.

**Data confidence:** High — \(T_m\) for ice, Al, and W, the latent-heat signature, and the loss of Bragg peaks are metrology-grade. The Lindemann window is medium as a number and high as a qualitative correlation.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Equilibrium coexistence (Clapeyron), descriptive of how \(T_m\) moves with pressure:

  \[
  \frac{dT_m}{dP} = \frac{\Delta V}{\Delta S}
  \]

  Ice is the familiar anomaly (\(\Delta V < 0\) ⇒ \(T_m\) falls with \(P\)). This relation organizes measured slopes; it does not give \(T_m(P=0)\).

- Lindemann diagnostic:

  \[
  \frac{\sqrt{\langle u^2\rangle}}{a} \simeq 0.1\text{–}0.15 \quad\text{near } T_m
  \]

  \(\langle u^2\rangle\) can be taken from a Debye or phonon sum; that is a consistency check on the displacement, not a first-principles \(T_m\).

- Order-parameter readout: crystalline Bragg intensity \(\to 0\); liquid \(S(q)\) peaks remain. Soft-mode language on `phonon-dispersion` describes some instabilities; ordinary 3-D melting of ice / Al / W is not the vanishing of a single \(\omega(q)\) branch.

No closed continuum equation in this entry outputs \(273.15\,\mathrm{K}\), \(933\,\mathrm{K}\), or \(3695\,\mathrm{K}\). Those are data.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A crystalline grid large enough to produce Bragg peaks and a macroscopic shear modulus. A few-atom cluster has no bulk \(T_m\); a glass has no Bragg grid. The sharp hardware is the ordered lattice itself, not a universal millimetre envelope.

- **Clock rate / latency.** Thermal vibration of the ions, with a spectral ceiling at the Debye / zone-boundary clock (`debye-cutoff`, `phonon-dispersion`). Melting is not that clock being exceeded; it is the grid losing the restoring couplings that defined the clock. Nucleation and front propagation set the laboratory time to complete the conversion and are not a single material pin.

- **Energy barriers or thresholds.** The load-bearing threshold is the measured \(T_m\): \(kT\) in the presence of the crystal’s cohesion is then sufficient to unbind the ordered grid. The latent heat is the energy that must be supplied at coexistence. There is no simple anisotropy-style barrier \(KV\) from which \(T_m\) is computed in this mapping.

- **Dominant failure modes.**
  - Thermal: \(T \to T_m\) at the ambient pressure → loss of Bragg order, loss of static shear, conversion to a fluid that carries only compressional sound.
  - Mechanical / chemical: the grid can also be destroyed below \(T_m\) by large plastic strain, radiation amorphization, or dissolution. Those are lattice-destruction routes, not the thermal coexistence cliff.
  - Superheating: a defect-poor crystal can temporarily overshoot \(T_m\); the equilibrium collapse point remains the measured coexistence temperature.

- **Emergent constant or stable output.** Below \(T_m\), a solid with Bragg order and a shear modulus. At \(T_m\), a first-order conversion whose temperature is a material constant at given pressure. Above \(T_m\), a fluid without that grid.

### 4.6 Internal Consistency Notes

Filing melting under lattice-modes is consistent with the taxonomy: the dominant collapse is loss of crystalline order and of the shear-carrying grid, not a latched moment or a plasma clock. Latch entries (`permanent-magnet-latch`, `ferroelectric-remanence`) may list lattice destruction as a secondary failure; they own the latch, this file owns the grid.

The mapping does not close on *why* ice, Al, and W fail at those particular temperatures. Lindemann is a displacement criterion, not a derived barrier. Cohesive well depth, coordination, and anharmonicity (`thermal-expansion`) all enter, and QSA does not yet have them as primitive node specifications. That is why the mapping confidence is medium while the \(T_m\) data are high.

Soft-mode melting of a particular lattice instability, if measured, belongs with `phonon-dispersion`. It should not be silently identified with the first-order melting of Al or W.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(T_m\) and the loss of Bragg / shear order are sharp measured boundaries and correctly identify the grid as the failing hardware, but the mapping takes \(T_m\) as an empirical threshold rather than extracting it from a stated node-level barrier.

## Related entries

- [phonon-dispersion](phonon-dispersion.md) — mode map of the living grid; softening is a related but not identical collapse
- [elasticity](elasticity.md) — shear modulus of the solid; yield is a different failure envelope
- [speed-of-sound](speed-of-sound.md) — shear branch present only while the grid holds
- [debye-cutoff](debye-cutoff.md) — clock ceiling of the solid; not \(T_m\)
- [thermal-expansion](thermal-expansion.md) — anharmonicity of the same wells, short of unbinding
- [permanent-magnet-latch](permanent-magnet-latch.md) — lattice destruction erases the latch; the latch entry owns that path
- [ferroelectric-remanence](ferroelectric-remanence.md) — same grid-loss secondary failure on an electrical latch
