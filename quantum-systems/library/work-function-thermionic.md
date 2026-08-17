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
related:
  - photoelectric-threshold
  - ionization-threshold
  - semiconductor-gap-absorption
  - photoconductivity
  - reflection
  - blackbody-spectrum
  - stefan-boltzmann
  - thermal-equilibrium-temperature
updated: 2026-08-17
---

# Work Function / Thermionic Emission (Heat-Opened Surface Gate)

### 4.1 Effect Name

Work function / thermionic emission (heat-opened surface gate)

### 4.2 Macroscopic Observation

A hot metal surface in vacuum emits a continuous electron current once it is hot enough. A tungsten filament at room temperature emits nothing measurable; the same filament, white-hot, supplies the cathode current of a vacuum tube or electron gun. No optical illumination is required. Cooling the surface extinguishes the current. A lower-work-function coating (thoriated tungsten, cesium, oxide layers) produces a usable current at a lower temperature than clean tungsten.

### 4.3 Established Quantitative Boundaries

- The conversion is gated by the surface work function \(\varphi\). Handbook polycrystalline values: W \(\varphi \approx 4.5\,\mathrm{eV}\) (often quoted \(4.54\,\mathrm{eV}\)); elemental Cs \(\varphi \sim 2\,\mathrm{eV}\) (face-dependent, \(\sim 1.8\)–\(2.1\,\mathrm{eV}\)); thoriated tungsten \(\varphi \approx 2.6\,\mathrm{eV}\). Crystal faces of a single metal differ by several tenths of an eV; polycrystalline surfaces therefore present a narrow patch of gates, not one infinitely sharp number.
- Thermal energy scale: \(kT \approx 26\,\mathrm{meV}\) at \(300\,\mathrm{K}\); \(kT \approx 0.22\,\mathrm{eV}\) at \(2500\,\mathrm{K}\) (a typical hot-W operating neighbourhood). For clean W, \(\varphi / kT \sim 170\) at room temperature and \(\sim 20\) at \(2500\,\mathrm{K}\). Emission is unmeasurable when \(kT \ll \varphi\) and becomes a laboratory current only when the Boltzmann factor \(\mathrm{e}^{-\varphi/kT}\) is no longer astronomically small.
- Theoretical Richardson constant \(A_0 = 4\pi e m k^2 / h^3 \approx 1.20 \times 10^6\,\mathrm{A\,m^{-2}\,K^{-2}}\). Measured apparent \(A\) for real metals is of the same order and is material- and surface-dependent (often tens of \(\mathrm{A\,cm^{-2}\,K^{-2}}\)).
- An applied surface field lowers the gate (Schottky effect). That is a field *modifier* of the same barrier, not a second conversion. Space charge in the vacuum gap can limit the collected current even when the surface gate is open (Child–Langmuir regime).
- Surface contamination, adsorption, and crystal-face mix shift \(\varphi\) by tenths of an eV and therefore move the temperature at which a given current appears. The existence of the gate is not in question; the last digit of \(\varphi\) is surface-specific.

**Data confidence:** High — work functions, the Richardson form, and the collapse of emission when \(kT \ll \varphi\) are multiply reproduced handbook facts. Apparent \(A\) and the exact \(\varphi\) of a given technical surface are medium.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Richardson–Dushman current density:

  \[
  J = A T^2 \exp\!\left(-\frac{\varphi}{kT}\right)
  \]

- Schottky lowering of the barrier in a surface field \(E\):

  \[
  \Delta\varphi = \sqrt{\frac{eE}{4\pi\varepsilon_0}},\qquad
  J = A T^2 \exp\!\left(-\frac{\varphi - \Delta\varphi}{kT}\right)
  \]

- Child–Langmuir space-charge limit between parallel plates (gap \(d\), voltage \(V\)), recorded as the collected-current ceiling, not as the surface gate:

  \[
  J_{\mathrm{CL}} = \frac{4\varepsilon_0}{9}\sqrt{\frac{2e}{m}}\,\frac{V^{3/2}}{d^2}
  \]

- Work function as the surface barrier measured from the Fermi level: \(\varphi = E_{\mathrm{vac}} - E_F\). The same \(\varphi\) is the photoelectric threshold of the same surface.

The exponential in \(J(T)\) is the entire macroscopic signature of a closed thermal gate. There is no additional mechanism required to explain why a cold cathode is dark.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The conversion event is single-electron: one occupied state at the surface, one barrier \(\varphi\), one escape. A measurable cathode current is the summed output of a large emitting area. There is no collective coherence volume analogous to the 10–20 nm mirror buffer; starving the *area* reduces current in proportion, it does not close the gate. The gate itself lives in a surface atomic layer.

- **Clock rate / latency.** Thermal attempt rates sit in the prefactor \(A T^2\) (electron thermal velocities and the surface attempt frequency). Once over the barrier, vacuum transit is set by the anode voltage and the gap; that latency belongs to collection, not to opening the gate. Relative to any mechanical clock the emission, when it occurs, is already complete.

- **Energy barriers or thresholds.** The operating gate is \(\varphi\). Heat opens it from below by populating the Boltzmann tail; a photon of energy \(h\nu > \varphi\) opens the same gate from above ([photoelectric-threshold](photoelectric-threshold.md)). An applied field lowers \(\varphi\) (Schottky) but does not replace it.

- **Dominant failure modes.**
  - Thermal / under-threshold: \(kT \ll \varphi\) → the conversion does not occur. That *is* the collapse of thermionic emission. A tungsten part at room temperature is not a cathode.
  - Surface: contamination or a different crystal face shifts \(\varphi\) and moves the temperature cliff. The gate remains a gate.
  - Field / collection: space charge or a missing anode field can starve the *collected* current while emission into the barrier region still occurs. That is a readout ceiling, not closure of \(\varphi\).
  - Thermal destruction: the lattice evaporates or melts if \(T\) is pushed far above the useful emission window. That destroys the hardware rather than closing the gate.

- **Emergent constant or stable output.** A stable current density \(J(T,\varphi)\) from a hot surface, with no optical drive, for as long as the surface, the temperature, and the collection field remain inside the envelope above.

### 4.6 Internal Consistency Notes

The mapping closes on the same surface barrier as photoelectric emission. One gate, two opening resources (heat vs. \(h\nu\)). Reflection from the same cold metal is the complementary below-threshold behaviour of the electron population: the cloud responds collectively and no electron leaves ([reflection](reflection.md)). Nothing in the thermionic numbers conflicts with that split.

The Richardson tail is not a second mechanism and is not evidence that the gate is soft in the sense of a new channel. It is the thermal occupation of states above a hard barrier. Patchy work functions and Schottky lowering smear the observed cliff; they do not replace it.

A remaining gap: QSA takes \(\varphi\) as a measured surface specification. It does not here derive the 4.5 eV of tungsten from a more primitive node rule. The collapse condition \(kT \ll \varphi\) does not depend on closing that derivation. Apparent \(A < A_0\) is likewise taken as a surface datum (reflection, transmission, density-of-states corrections in the standard description).

### 4.7 Overall Confidence in the QSA Mapping

**High** — the work function is a sharp, multiply measured energy gate, the collapse when \(kT \ll \varphi\) is unambiguous, and the mapping is the same photoelectric-class gate opened by heat rather than by a photon.

## Related entries

- [photoelectric-threshold](photoelectric-threshold.md) — the same \(\varphi\) gate, opened by \(h\nu\) instead of by the thermal tail
- [ionization-threshold](ionization-threshold.md) — leaving a bound atomic state rather than a solid surface; a single-particle gate at a different energy
- [semiconductor-gap-absorption](semiconductor-gap-absorption.md) — a bulk gap instead of a surface barrier; same conversion family
- [photoconductivity](photoconductivity.md) — carriers freed inside a solid and read as current, not ejected into vacuum
- [reflection](reflection.md) — below-threshold collective response of the same metal electron population
- [blackbody-spectrum](blackbody-spectrum.md) — the same hot surface as a thermal radiator
- [stefan-boltzmann](stefan-boltzmann.md) — integrated thermal emission from the hot body
- [thermal-equilibrium-temperature](thermal-equilibrium-temperature.md) — \(T\) as the ensemble coordinate that opens or closes this gate
