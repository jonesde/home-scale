---
id: ferroelectric-remanence
title: Ferroelectric Remanence (Polar Latch)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - field-threshold
  - thermal
  - spatial-buffer
  - mechanical-lattice
confidence_data: high
confidence_mapping: medium
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - superparamagnetism
  - piezoelectricity
  - refraction-dielectric
  - dielectric-breakdown
updated: 2026-08-17
---

# Ferroelectric Remanence (Polar Latch)

### 4.1 Effect Name

Ferroelectric remanence (polar latch)

### 4.2 Macroscopic Observation

A ferroelectric crystal or ceramic, after a large electric field is applied and then removed, retains a remanent polarization \(P_r\). The sample remains electrically poled at zero continuous field and zero continuous power. A reverse field of magnitude equal to the coercive field \(E_c\) is required to switch that polarization through zero. Heating through the Curie point, or reducing the grain (or film) until the polar state is no longer stable, destroys useful remanence. Linear dielectrics polarize in an applied field and return to \(P = 0\) when the field is removed.

### 4.3 Established Quantitative Boundaries

- \(\mathrm{BaTiO_3}\) Curie point \(T_C \approx 120^\circ\mathrm{C}\) (\(393\,\mathrm{K}\)). Above \(T_C\) the room-temperature tetragonal polar phase is gone (cubic perovskite) and remanent \(P\) collapses. Further polar-phase changes in \(\mathrm{BaTiO_3}\) sit near \(5^\circ\mathrm{C}\) (tetragonal–orthorhombic) and \(-90^\circ\mathrm{C}\) (orthorhombic–rhombohedral); those are structure changes of an already-latched polar state, not the primary \(T_C\) cliff.
- End-member \(\mathrm{PbTiO_3}\): \(T_C \approx 490^\circ\mathrm{C}\). Commercial PZT (lead zirconate titanate) solid solutions sit below that end-member and are composition-dependent. The PZT family is the common ceramic latch; there is no single PZT \(T_C\).
- Coercive fields of bulk \(\mathrm{BaTiO_3}\) and PZT-family ceramics are of \(\mathrm{kV\,cm^{-1}}\) class (larger in many thin films). \(E_c\) is microstructure- and thickness-dependent; the class, not a grade-specific number, is the boundary used here.
- Room-temperature spontaneous polarization of single-crystal \(\mathrm{BaTiO_3}\) along \(c\) is \(P_s \approx 0.26\,\mathrm{C\,m^{-2}}\). Ceramic remanence is lower; PZT-family \(P_r\) remains in the \(10^{-1}\,\mathrm{C\,m^{-2}}\) (tens of \(\mu\mathrm{C\,cm^{-2}}\)) class.
- Energy per unit volume per cycle equals the loop area \(\oint\mathbf{E}\cdot d\mathbf{P}\). Holding remanent \(P\) at \(E = 0\) costs zero continuous power.
- Small grains and ultrathin films lose stable remanence (superparaelectric / depolarization collapse). The magnetic analog \(KV \gtrsim 25\,kT\) is not a standardized ferroelectric number; depolarization fields and electrodes enter, and a single laboratory-stability volume is not claimed here.

**Data confidence:** High — \(T_C\) of \(\mathrm{BaTiO_3}\) and \(\mathrm{PbTiO_3}\), the PZT family as a polar ceramic class, \(P_s\) of \(\mathrm{BaTiO_3}\), and \(\mathrm{kV\,cm^{-1}}\)-class \(E_c\) are handbook facts. A given ceramic’s \(E_c\) and the grain-size cliff are medium (process-dependent).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Dielectric displacement: \(\mathbf{D} = \varepsilon_0\mathbf{E} + \mathbf{P}\).
- Remanence \(P_r\): intercept at \(E = 0\) after saturation. Coercive field \(E_c\): intercept at \(P = 0\).
- Dissipated energy density per cycle:

  \[
  w = \oint \mathbf{E}\cdot d\mathbf{P}
  \]

- Landau–Devonshire expansion (a fit to the observed polar transition, not a node rule):

  \[
  F = \tfrac{1}{2}\alpha(T - T_C)P^2 + \tfrac{1}{4}\beta P^4 + \cdots - EP
  \]

  The double well below \(T_C\) is the standard description of two remanent polarities.

- Depolarization field of a uniformly polarized slab (electrostatics of the same \(P\)): \(E_d\) is of order \(P/\varepsilon\), reduced by electrodes and free charge. It is the electrical analog of a demagnetizing field and is the named reason thin or uncompensated samples lose remanence.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A polar lattice cell (perovskite \(\mathrm{ABO_3}\) in the oxides above) plus a correlated volume large enough that the polar well survives \(kT\) and the depolarization field. One unit-cell dipole is not a macroscopic remanent capacitor. Ceramic remanence is the synchronized output of a poled grain population. Below a process-dependent grain / thickness buffer the latch does not hold.

- **Clock rate / latency.** The polar displacement is ionic and sits on the lattice-mode clock (optical-phonon / THz class). Macroscopic switching of a ceramic or a multidomain crystal is slower and is set by nucleation and wall motion under the applied \(E\), not by the phonon period.

- **Energy barriers or thresholds.** A polar double well, locked to a non-centrosymmetric lattice, holds \(\pm P_r\) at \(E = 0\). Holding that state costs zero continuous power. Energy is spent only on transitions (the \(P\)–\(E\) loop area). The write threshold is \(E_c\), not the Landau barrier of a perfect crystal.

- **Dominant failure modes.**
  - Thermal: \(T > T_C\) \(\to\) polar well closes \(\to\) \(P_r \to 0\).
  - Field: reverse \(E\) of order \(E_c\) writes the opposite polarity (the cycle). Larger \(E\) can destroy the insulator ([dielectric-breakdown](dielectric-breakdown.md)); that is hardware failure, not a clean rewrite.
  - Spatial: grain or film too small, or depolarization uncompensated \(\to\) superparaelectric / volatile \(P\).
  - Mechanical: loss of the non-centrosymmetric lattice (cracking, phase conversion, electrode failure) erases the polar matrix.

- **Emergent constant or stable output.** A stable remanent polarization and the associated bound charge / field at zero continuous power, for as long as \(T\), grain volume, electrodes, and lattice stay inside the envelope above.

### 4.6 Internal Consistency Notes

The electrical twin of the magnet latch is tight on the accounting: remanent \(P\) at \(E = 0\), zero hold power, finite loop-area write cost, collapse at \(T_C\), and a soft / linear-dielectric limit when the polar well is missing. [Piezoelectricity](piezoelectricity.md) is the strain readout of the same polar lattice; [refraction-dielectric](refraction-dielectric.md) is the linear, unlatched polarization of a dielectric that does not keep \(P\) at \(E = 0\).

The mapping is not closed on the write threshold or the volume cliff. \(E_c\) of a ceramic is a mesoscale nucleation / grain-boundary number, analogous to magnetic \(H_c \ll H_a\), and is not derived here from the Landau well. The superparaelectric size line is real as a class and is *not* a portable \(KV/25kT\) constant: depolarization, screening, and electrodes are extra constraints that the magnetic grain problem does not carry in the same form. Those gaps are stated rather than filled.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(T_C\), remanence at \(E = 0\), and zero hold power map cleanly onto a polar latch, but \(E_c\) and the grain / depolarization buffer remain mesoscale data without a closed QSA specification.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — magnetic twin: remanent moment at zero continuous field
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — the same loop accounting, written in \(M(H)\) instead of \(P(E)\)
- [superparamagnetism](superparamagnetism.md) — volume collapse of a directional latch; electrical analog is the superparaelectric grain
- [piezoelectricity](piezoelectricity.md) — strain \(\leftrightarrow\) polarization on a lattice that lacks inversion
- [refraction-dielectric](refraction-dielectric.md) — linear bound-charge response without remanence
- [dielectric-breakdown](dielectric-breakdown.md) — field destruction of the insulator that hosts the polar latch
