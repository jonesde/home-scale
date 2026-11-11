---
id: curie-paramagnetism
title: Curie Paramagnetism (Unlocked-Spin Ensemble)
status: formal
family: ensemble-averages
constraints:
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: medium
review_depth: standard
related:
  - permanent-magnet-latch
  - superparamagnetism
  - ferromagnetic-hysteresis
  - antiferromagnetic-order
  - thermal-equilibrium-temperature
  - faraday-rotation
updated: 2026-11-13
---

# Curie Paramagnetism (Unlocked-Spin Ensemble)

### 4.1 Effect Name

Curie paramagnetism (unlocked-spin ensemble)

### 4.2 Macroscopic Observation

A paramagnetic salt or a dilute magnetic ion in a host acquires a magnetization along an applied field and loses it when the field is removed. The susceptibility falls as the temperature rises. There is no remanent moment and no hysteresis loop. Cooling toward an ordering temperature replaces this reversible \(1/T\) response with a ferromagnetic, ferrimagnetic or antiferromagnetic state. Ordinary laboratory fields at room temperature stay in the linear range; at about a kelvin, a few tesla saturate the moment.

### 4.3 Established Quantitative Boundaries

- **Measured.** Curie's law, \(\chi = C/T\), was found by fitting experimental data. It holds at high temperature and weak field; at low temperature and strong field the magnetization saturates [S3].
- **Model (non-interacting moments).** The Curie constant is \(C = \mu_0 n g^{2}\mu_B^{2}J(J+1)/3k\) for number density \(n\) and angular momentum \(J\) [S3]; \(J = S\) when the orbital moment is quenched, as measured for \(\mathrm{Cr^{3+}}\) [S2].
- **Measured.** Constants (CODATA 2022): \(\mu_B = 9.2740100657\times10^{-24}\) J T⁻¹ [S1]; the electron precession scale is 28 024.951 MHz T⁻¹ [S5].
- **Computed here.** \(\mu_B/k = 0.6717\) K T⁻¹ with the exact \(k\). The field at which \(\mu_B B = kT\) is 447 T at 300 K and 1.49 T at 1 K. At 1 T and 300 K, \(\mu_B B/kT = 2.2\times10^{-3}\), and the fractional departure of a spin-½ moment from linearity, \(x^{2}/3\), is \(1.7\times10^{-6}\). The precession scale is 28.02 GHz T⁻¹.
- **Computed here.** Size of \(C\). For one mole of \(S = \tfrac12\), \(g = 2\) moments the molar Curie constant is \(4.71\times10^{-6}\) m³ K mol⁻¹, or 0.375 cm³ K mol⁻¹ in cgs units. For \(S = \tfrac72\) (\(\mathrm{Gd^{3+}}\)) the factor \(g^{2}S(S+1)\) is 21 times larger.
- **Measured.** Saturation. \(\mathrm{Cr^{3+}}\) in potassium chromium alum reaches 99.5 % of saturation at 1.29 K in 50 000 G. The curve agrees with the Brillouin function for \(g = 2\) (orbital moment quenched) and is markedly incompatible with the classical Langevin function. Iron ammonium alum and gadolinium sulfate octahydrate were also taken to saturation [S2].
- **Computed here.** 50 000 G is 5 T. For \(S = \tfrac32\), \(g = 2\) at 5 T and 1.29 K the Brillouin argument \(g\mu_BSB/kT\) is 7.8 and \(B_{3/2} = 99.6\) %, against the measured 99.5 %. The same ion at 1 T and 300 K is at 0.37 % of saturation.
- **Model (mean field).** With interactions, \(\chi = C/(T - \theta)\) above the ordering temperature (Curie–Weiss). The law fails close to the Curie point, where the susceptibility follows a critical power law, and holds well above it with \(\theta\) somewhat different from the ordering temperature [S4]. Below the ordering temperature the ferromagnet has a spontaneous magnetization [S4].
- **Measured.** Ordering temperatures are material-specific; values are in the ordered-state entries ([permanent-magnet latch](permanent-magnet-latch.md), [antiferromagnetic order](antiferromagnetic-order.md)).
- **Model (Fermi–Dirac statistics).** Conduction electrons in a metal give a susceptibility that goes to a constant at low temperature instead of \(1/T\) (Pauli paramagnetism) [S3]. It is not Curie paramagnetism.

**Data confidence:** High — the constants are CODATA values, the saturation curve is a primary measurement read in its abstract, and the recomputed Brillouin value agrees with it to 0.1 %. The formula for \(C\), the Curie–Weiss limits and the Pauli statement rest on tertiary pages; they are textbook results. \(C\) and \(\theta\) of a given compound are not filed.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Curie law and constant:

  \[
  \chi = \frac{C}{T},\qquad C = \frac{\mu_0 n\,g^{2}\mu_B^{2}J(J+1)}{3k}
  \]

- Magnetization of non-interacting moments: \(M = n g\mu_B J\,B_J(x)\) with \(x = g\mu_B J B/kT\) and

  \[
  B_J(x) = \frac{2J+1}{2J}\coth\!\Big(\frac{2J+1}{2J}x\Big) - \frac{1}{2J}\coth\!\Big(\frac{x}{2J}\Big)
  \]

  Small \(x\) gives \(\chi = C/T\); large \(x\) saturates. For \(J = \tfrac12\) this is \(\tanh x\) [S3].
- Curie–Weiss: \(\chi = C/(T - \theta)\), a mean-field form with \(\theta\) a fitted intercept [S4].

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A population of moments that are free to follow the field and share a bath temperature. The scale is statistical: \(\chi\) is the averaged response, and no minimum count is defined. Volume enters as a count. The thermal reversal of a single-domain grain with an anisotropy barrier is [superparamagnetism](superparamagnetism.md), a different family.

- **Clock rate / latency.** Single moments precess at 28.02 GHz T⁻¹. The Curie reading is a time average of the projection along the field, valid for observation slower than the moments' relaxation to the bath. No relaxation time is filed.

- **Energy barriers or thresholds.**
  - Operating condition: no barrier holds the moments. The response is reversible.
  - Scale for leaving the linear range: \(\mu_B B \sim kT\), which is 447 T at 300 K and 1.49 T at 1 K.
  - Ordering temperature: below it the population is ordered and this entry no longer applies.

- **Dominant failure modes.**
  - **Threshold** — ordering: at \(T_C\) or \(T_N\) the free population is replaced by an ordered state with a spontaneous or staggered magnetization. A phase transition. The Curie–Weiss form already fails in the critical region just above it.
  - **Crossover** — field saturation: \(M/M_\mathrm{sat} = B_J(g\mu_BJB/kT)\), a function of \(B/T\) only. 0.37 % at 1 T and 300 K; 99.5 % measured at 5 T and 1.29 K. No critical field.
  - **Crossover** — high temperature: \(\chi \propto 1/T\) falls without limit; the moment produced by a given field eventually drops below any instrument floor.
  - **Crossover** — small population: the relative fluctuation of the summed moment grows as \(1/\sqrt{N}\); no measured scale is filed.

- **Emergent constant or stable output.** A reversible susceptibility \(\chi = C/T\), or \(C/(T - \theta)\), linear in field at small \(B/T\), with zero remanence at zero field.

### 4.6 Internal Consistency Notes

The contrast with the [permanent-magnet latch](permanent-magnet-latch.md) is the consistency test for this entry. A latched grain holds a moment at zero field and zero power. A Curie population holds nothing at zero field. A soft ferromagnet below its Curie point is still an ordered collective, however low its coercivity; [ferromagnetic hysteresis](ferromagnetic-hysteresis.md) owns that case. Treating a hard magnet's remanence as a Curie response is a filing error, not a failure mode of this effect.

[Superparamagnetism](superparamagnetism.md) is the other contrast. A small ferromagnetic grain above its blocking temperature responds as one large free moment, with a magnetization curve that scales with \(H/T\) like the Brillouin curve here. The difference is the barrier: the grain has an anisotropy energy \(KV\) and a relaxation time \(\tau_0\exp(KV/kT)\), so whether it appears free depends on the measurement time. That entry is a crossover in time. A Curie ion has no such barrier in this description.

Sourcing changed little in substance. The constants were right. The saturation statement now rests on a measured point, 99.5 % at 1.29 K and 5 T, which the Brillouin function reproduces and the classical Langevin function does not; the first version named the two functions as alternatives. The failure-mode list was relabelled: ordering is the one threshold, and saturation, the high-temperature fall and the small-population limit are crossovers. "Mis-filing" was removed from the failure modes and kept as the note above. An oxygen-bearing gas was named as an example in the first version; no source for it was opened and it was dropped.

The mapping does not compute \(C\) or \(\theta\) and names no minimum spin count. Pauli paramagnetism shares the statistical character of this family and is closer to the [electron heat capacity](electron-heat-capacity.md) entry; it is not given a home here.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the \(C/T\) form, Brillouin saturation and the replacement by order at \(T_C\) or \(T_N\) are sourced, and the free-against-latched contrast holds against the magnet entries; the hardware scale is statistical, with no minimum count.

## Related entries

- [Permanent magnet (directional latch)](permanent-magnet-latch.md) — the latched contrast: remanent moment at zero field
- [Superparamagnetism](superparamagnetism.md) — a grain with a barrier that responds as a free moment only on long enough time scales
- [Ferromagnetic hysteresis](ferromagnetic-hysteresis.md) — the loop of the ordered state
- [Antiferromagnetic order](antiferromagnetic-order.md) — staggered order below \(T_N\)
- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the bath that sets the \(1/T\) scale
- [Faraday rotation](faraday-rotation.md) — optical readout of a moment population, free or latched

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [NIST, CODATA 2022 value of the Bohr magneton](https://physics.nist.gov/cgi-bin/cuu/Value?mub) | full-text | Bohr magneton 9.2740100657 × 10⁻²⁴ J/T. |
| S2 | [Henry, *Phys. Rev.* 88, 559 (1952)](https://doi.org/10.1103/PhysRev.88.559) | abstract | Cr³⁺ alum at 99.5 % saturation at 1.29 K and 50 000 G; agreement with the Brillouin function for g = 2 and disagreement with the Langevin function; Fe³⁺ and Gd³⁺ salts saturated. |
| S3 | [Wikipedia, "Curie's law"](https://en.wikipedia.org/wiki/Curie%27s_law) | full-text | Tertiary: the law as an experimental fit valid at high temperature and weak field; Curie constant formula; tanh form for two-level moments; constant susceptibility of a Fermi gas. |
| S4 | [Wikipedia, "Curie–Weiss law"](https://en.wikipedia.org/wiki/Curie%E2%80%93Weiss_law) | full-text | Tertiary: Curie–Weiss form above the Curie temperature, its mean-field origin and failure near the Curie point. |
| S5 | [NIST, CODATA 2022 electron gyromagnetic ratio in MHz/T](https://physics.nist.gov/cgi-bin/cuu/Value?gammaebar) | full-text | 28 024.951 3861 MHz/T. |
