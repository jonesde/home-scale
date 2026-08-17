---
id: ferromagnetic-hysteresis
title: Ferromagnetic Hysteresis (Write–Erase Cycle)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - field-threshold
  - thermal
  - spatial-buffer
  - mechanical-lattice
confidence_data: high
confidence_mapping: high
related:
  - permanent-magnet-latch
  - superparamagnetism
  - magnetic-domains
  - shape-anisotropy
  - exchange-bias
  - magnetostriction
  - curie-paramagnetism
updated: 2026-08-17
---

# Ferromagnetic Hysteresis (Write–Erase Cycle)

### 4.1 Effect Name

Ferromagnetic hysteresis (write–erase cycle)

### 4.2 Macroscopic Observation

A ferromagnet driven around a closed cycle of applied field \(H\) returns a multi-valued magnetization (or induction) loop. After a large field is removed, a remanent magnetization remains. A reverse field of magnitude equal to the coercivity is required to bring that remanence back through zero. Soft iron and electrical steels show a narrow loop and lose useful remanence against their own demagnetizing field. Hard magnets show a wide loop and keep a useful remanent moment. A sample sitting at rest on a remanent branch produces no continuous hysteresis heat. Driving the loop repeatedly dissipates heat.

### 4.3 Established Quantitative Boundaries

- Soft iron and silicon steel: coercivity typically \(< 10^2\)–\(10^3\,\mathrm{A\,m^{-1}}\) (often much lower in annealed stock). The loop area is small. Remanence exists but is not stable against ordinary self-demagnetizing fields.
- Sintered NdFeB: coercivity is microstructure-dependent and typically of tesla class (often \(\sim 1\,\mathrm{T}\) in \(\mu_0 H_c\)), much less than the anisotropy field \(\mu_0 H_a \approx 7\)–\(8\,\mathrm{T}\) set by \(K_1 \approx 4.5\,\mathrm{MJ\,m^{-3}}\). The loop is wide enough that remanence survives the sample’s own demagnetizing field.
- Iron Curie point \(T_C \approx 1043\,\mathrm{K}\) (\(770^\circ\mathrm{C}\)); \(\mathrm{Nd_2Fe_{14}B}\) \(T_C \approx 585\,\mathrm{K}\). Above \(T_C\) the ordered moment is gone and the loop disappears.
- Energy per unit volume per cycle equals the loop area \(\oint\mathbf{H}\cdot d\mathbf{B}\). That energy is the write / erase cost. Holding a static remanent point costs zero continuous power.
- Larmor / FMR scale: \(\gamma/2\pi \approx 28.025\,\mathrm{GHz\,T^{-1}}\). Practical loop traversal is set by the field sweep and by domain-wall motion (and, in metals, eddy currents), not by that carrier.
- Grain-volume thermal collapse of the same barrier is the Néel–Arrhenius line \(KV \gtrsim 25\,kT\), filed as [superparamagnetism](superparamagnetism.md). On laboratory timescales a grain below that line does not hold a remanent branch.

**Data confidence:** High — soft / hard coercivity classes, Curie points, loop-area energy, and the \(H_a \gg H_c\) gap in NdFeB are standard measured facts. A specific commercial grade’s \(H_c\) is medium (process-dependent); the class distinction is not.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Induction and magnetization: \(\mathbf{B} = \mu_0(\mathbf{H} + \mathbf{M})\).
- Remanence \(M_r\) or \(B_r\): the intercept at \(H = 0\) after saturation. Coercivity \(H_c\): the intercept at \(M = 0\) (intrinsic) or \(B = 0\) (induction coercivity). The two intercepts differ when remanence is large.
- Dissipated energy density per cycle:

  \[
  w = \oint \mathbf{H}\cdot d\mathbf{B}
  \]

- Uniaxial anisotropy field (the scale \(H_a\), not the measured \(H_c\)):

  \[
  \mu_0 H_a = \frac{2K_1}{M_s}
  \]

  Stoner–Wohlfarth coherent rotation of an aligned uniaxial particle predicts a switching field of order \(H_a\). Measured loops in polycrystals and sintered magnets lie far below that prediction.

- Thermal escape of a grain moment: \(\tau = \tau_0\exp(KV/kT)\), as on the parent latch.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A ferromagnetic ordered volume large enough to support a remanent branch: at minimum a grain with \(KV\) above the thermal line, embedded in a lattice that supplies \(K\) (magnetocrystalline and/or shape). A single spin has no useful remanence against \(kT\). The *loop* as a macroscopic object further requires a population whose net moment is readable — a grain ensemble, a domain pattern, or a bulk body. Soft matrices supply order (high \(T_C\)) without a usable write barrier.

- **Clock rate / latency.** Single-moment precession at \(\approx 28\,\mathrm{GHz\,T^{-1}}\). Write / erase latency of a real loop is the time to nucleate reverse regions and move walls across the sample under the applied sweep; that is a much slower, microstructure-limited clock. Eddy currents add a conductive-metal delay.

- **Energy barriers or thresholds.** The barrier that protects remanence is the same anisotropy barrier as the [permanent-magnet latch](permanent-magnet-latch.md) (\(K_1 V\), plus shape terms). The field that writes the opposite state is the coercivity, a threshold much smaller than \(H_a\) in almost all bulk magnets. Holding remanence costs zero continuous power. The loop area is the energy spent to write and erase.

- **Dominant failure modes.**
  - Soft limit: barrier / pinning too small \(\to H_c \to 0\), loop area \(\to 0\) \(\to\) remanence does not survive removal of \(H\) (volatile alignment). The metal may still be ferromagnetic.
  - Thermal, order: \(T > T_C\) \(\to\) no ordered moment \(\to\) no loop.
  - Thermal, volume: \(KV \lesssim 25\,kT\) \(\to\) remanent branch erased on the laboratory clock.
  - Field: reverse \(H\) of order \(H_c\) writes the opposite remanent state. That is the cycle itself, not destruction of the hardware.
  - Mechanical: lattice / grain-boundary destruction changes \(H_c\) and can close a useful loop without reaching \(T_C\).

- **Emergent constant or stable output.** A stable remanent magnetization at \(H = 0\), and a reproducible dissipative cost \(\oint\mathbf{H}\cdot d\mathbf{B}\) each time the state is cycled, at zero continuous power on either remanent branch.

### 4.6 Internal Consistency Notes

The mapping closes on the distinction the parent latch already needed: ferromagnetism (an ordered collective state below \(T_C\)) is not the same effect as a useful directional latch (a barrier that survives \(H = 0\)). Hysteresis is the write / erase cycle of that latch. Zero hold power plus finite loop-area write cost is exactly the latch accounting.

The same mesoscale gap as on the parent file remains load-bearing here. Measured \(H_c\) is not \(H_a\). Grain boundaries, reverse-domain nucleation, dipolar coupling, and wall pinning set the write threshold. §4.4 records the Stoner–Wohlfarth formula as the coherent-rotation ceiling, not as the operating point. QSA does not yet have a buffer / barrier specification that produces \(H_c\) from those mesoscale ingredients. The soft-limit collapse, the \(T_C\) collapse, and the zero-hold-power clause do not depend on closing that gap.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the soft / hard split, the loop-area energy, \(T_C\), and zero hold power translate directly into barrier, field-threshold, and failure-envelope specifications; the open item is the mesoscale origin of \(H_c\), not the identification of the loop as the latch cycle.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — the held directional state whose write / erase cycle this loop is
- [superparamagnetism](superparamagnetism.md) — thermal collapse of the remanent branch when the grain volume is under-provisioned
- [magnetic-domains](magnetic-domains.md) — walls whose motion traces most of a bulk loop
- [shape-anisotropy](shape-anisotropy.md) — geometry contribution to the barrier that the loop is written over
- [exchange-bias](exchange-bias.md) — a second latch that shifts this loop along \(H\)
- [magnetostriction](magnetostriction.md) — lattice–moment coupling on the same ordered body
- [curie-paramagnetism](curie-paramagnetism.md) — unlocked ensemble above \(T_C\); contrast case
