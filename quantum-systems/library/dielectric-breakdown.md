---
id: dielectric-breakdown
title: Dielectric Breakdown (Field-Opened Insulator Conversion)
status: formal
family: threshold-conversion
constraints:
  - field-threshold
  - energy-barrier
  - spatial-buffer
  - thermal
  - mechanical-lattice
confidence_data: medium
confidence_mapping: medium
related:
  - refraction-dielectric
  - ionization-threshold
  - semiconductor-gap-absorption
  - photoconductivity
  - piezoelectricity
  - ferroelectric-remanence
  - plasma-frequency-cutoff
updated: 2026-08-17
---

# Dielectric Breakdown (Field-Opened Insulator Conversion)

### 4.1 Effect Name

Dielectric breakdown (field-opened insulator conversion)

### 4.2 Macroscopic Observation

An insulator — dry air, a polymer film, an oxide layer — supports an electric field and passes only a negligible leakage current up to a material- and geometry-dependent field. Crossing that field produces a sudden conducting path: a spark in air, a puncture or carbon track in a solid. Below the cliff the part is still an insulator and the conversion has not occurred. Above it the part is often permanently changed. A second spark then follows a damaged path, not the original material.

### 4.3 Established Quantitative Boundaries

- Dry air at STP, centimetre-scale roughly uniform gaps: breakdown field of order \(3\,\mathrm{MV\,m^{-1}}\) (\(30\,\mathrm{kV\,cm^{-1}}\)). This is an order-of-magnitude working number, not a universal constant. Electrode shape, humidity, pressure, gap, and pulse length all move it.
- Gases follow a Paschen relation: breakdown voltage is a function of the pressure–gap product \(pd\), with a minimum of a few hundred volts in air (commonly quoted near \(300\,\mathrm{V}\) at a small \(pd\)). Very short gaps and very low pressures both *raise* the voltage needed, because an avalanche cannot develop.
- Common polymer films sit in a broad \(10^7\)–\(10^8\,\mathrm{V\,m^{-1}}\) class. Thermal \(\mathrm{SiO_2}\) films sit higher, in a \(10^8\)–\(10^9\,\mathrm{V\,m^{-1}}\) (few-to-\(\sim 10\,\mathrm{MV\,cm^{-1}}\)) class. These are handbook *ranges*. Quoting a single polymer or oxide number to three figures is not supported.
- Time and area matter. Longer stress and larger electrodes lower the observed field (weak-spot statistics, time-dependent dielectric breakdown). Thin films can show higher apparent \(E_{\mathrm{bd}}\) than bulk of the same chemistry.
- Below \(E_{\mathrm{bd}}\) the response is reversible leakage and polarization: remove the field and the insulator is still an insulator. Above \(E_{\mathrm{bd}}\) the usual laboratory outcome in a solid is destructive (puncture, carbonization, melted channel). Gases can recover after the plasma extinguishes if the electrodes and chemistry allow.

**Data confidence:** Medium — the *existence* of a field cliff and the air \(\sim 3\,\mathrm{MV\,m^{-1}}\) class are high. Any one numerical \(E_{\mathrm{bd}}\) is medium or lower (geometry, time, defects, humidity).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Phenomenological gate:

  \[
  E < E_{\mathrm{bd}} \;\Rightarrow\; \text{no conversion (insulator remains an insulator)}
  \]

  \[
  E \ge E_{\mathrm{bd}} \;\Rightarrow\; \text{conducting path forms}
  \]

  \(E_{\mathrm{bd}}\) is a measured envelope, not a first-principles constant.

- Paschen form for a gas between electrodes (descriptive):

  \[
  V_{\mathrm{bd}} = f(pd)
  \]

  with a minimum at a gas-specific \(pd\). Equivalent statement: the avalanche needs a sufficient product of density and path length.

- Townsend multiplication (descriptive of the gas step): ionization along a path \(\propto \mathrm{e}^{\alpha d}\), with \(\alpha = \alpha(E/p)\). Runaway occurs when multiplication exceeds losses.
- Solids add defect-assisted injection, thermal runaway, and electromechanical stress. No single equation locates \(E_{\mathrm{bd}}\) for a technical polymer the way \(2m_e c^2\) locates pair production.

Below-threshold non-conversion *is* the collapse of this effect. Pre-breakdown leakage is not the spark.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A single ionization ([ionization-threshold](ionization-threshold.md)) is not breakdown. The conversion that is *this* effect is a many-node avalanche: a path long enough, and a medium dense enough, that multiplication outruns loss. Paschen’s minimum is that buffer condition made visible. A vacuum gap and a microgap fail to spark at the same voltage as a centimetre of air because the hardware for multiplication is under-provisioned, not because \(I\) of the molecule changed. In a solid the corresponding buffer is a defect-rich path across the film.

- **Clock rate / latency.** Avalanche growth, streamer crossing, and thermal runaway have nanosecond-to-microsecond (and longer, for thermal) clocks. DC, pulsed, and lightning-scale stresses therefore report different \(E_{\mathrm{bd}}\). That is a latency dependence of the same field gate, not a family change.

- **Energy barriers or thresholds.** The operating gate is a field, \(E_{\mathrm{bd}}\), not a single quantum \(h\nu\) or \(I\). Microscopically the avalanche still spends ionization energy \(I\) or a mobility gap; the *macroscopic* lock that failed is the applied field. Holding \(E < E_{\mathrm{bd}}\) costs only the leakage; crossing it writes a conducting path.

- **Dominant failure modes.**
  - Under-threshold: \(E < E_{\mathrm{bd}}\) → conversion does not occur. The dielectric continues to support the field. That is the collapse / non-occurrence of breakdown.
  - Over-threshold, solids: the insulator is destroyed along a track. The original \(E_{\mathrm{bd}}\) is no longer a property of that path.
  - Geometry / buffer: \(pd\) off the Paschen window, or a path too short for multiplication → the field gate moves or the spark refuses.
  - Thermal: Joule heating of leakage can run away and open a path at a field below the short-pulse \(E_{\mathrm{bd}}\).
  - Mechanical: puncture, cracking, or electromechanical collapse of a soft film is a lattice / matrix failure coincident with the electrical one.

- **Emergent constant or stable output.** Below threshold: a stable insulating state (the useful operating output of the dielectric). Above threshold: a conducting channel, often irreversible in solids. There is no single material-universal \(E_{\mathrm{bd}}\) analogous to \(2m_e c^2\).

### 4.6 Internal Consistency Notes

Filed in threshold-conversion because the dominant observed cliff is under-threshold field: below \(E_{\mathrm{bd}}\) the conversion does not occur. That assignment is honest and incomplete. Unlike pair production or a work function, \(E_{\mathrm{bd}}\) is not a single-node energy. It is an avalanche condition that depends on path, time, defects, and heat. The mapping is therefore medium: the *class* (a field-opened conversion of insulator to conductor) is clear; a closed buffer / barrier specification that predicts a polymer’s \(E_{\mathrm{bd}}\) from node rules is not in hand.

Contrast with [refraction-dielectric](refraction-dielectric.md): that entry is the reversible, below-threshold polarization of the same insulating population. Contrast with [ionization-threshold](ionization-threshold.md): that entry is the microscopic unbinding step the avalanche uses. Contrast with [photoconductivity](photoconductivity.md): light can raise the carrier density without destroying the lattice; breakdown usually does destroy it.

A remaining gap, stated as a gap: after the first spark the system is a different object (plasma column, carbon track). QSA must not treat post-breakdown conduction as the original insulator with a new number. The clean operating envelope is the reversible side of \(E_{\mathrm{bd}}\).

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — a field gate is clearly present and under-threshold non-conversion is well observed, but \(E_{\mathrm{bd}}\) is geometry-, time-, and damage-dependent, and the post-spark state is no longer the original machine.

## Related entries

- [refraction-dielectric](refraction-dielectric.md) — reversible polarization of the same insulator below \(E_{\mathrm{bd}}\)
- [ionization-threshold](ionization-threshold.md) — the single-particle step the avalanche consumes
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — an energy gate in a gapped solid, opened by a photon rather than by a field
- [photoconductivity](photoconductivity.md) — carriers generated without (necessarily) destroying the lattice
- [piezoelectricity](piezoelectricity.md) — strain–polarization coupling in an intact dielectric; a different failure envelope
- [ferroelectric-remanence](ferroelectric-remanence.md) — a latched polarization written by a field well below destructive breakdown
- [plasma-frequency-cutoff](plasma-frequency-cutoff.md) — collective response of the charges *after* a conducting path exists
