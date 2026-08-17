---
id: superconductivity
title: Superconductivity (Zero-Resistance Transport)
status: formal
family: gapped-coherence
constraints:
  - thermal
  - field-threshold
  - energy-barrier
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
related:
  - meissner
  - josephson-effect
  - flux-quantization
  - type-ii-critical-field
  - superfluid-helium-4
  - electron-heat-capacity
updated: 2026-08-17
---

# Superconductivity (Zero-Resistance Transport)

### 4.1 Effect Name

Superconductivity (zero-resistance transport)

### 4.2 Macroscopic Observation

Below a material-specific critical temperature, the DC electrical resistance of certain metals, alloys, and compounds falls below the instrument floor. A closed superconducting loop carries a persistent current for years with no measurable decay and no continuous voltage. Raising the temperature through \(T_c\), applying a large enough magnetic field, or driving a large enough current restores ordinary dissipative resistance. Field expulsion is a related but separately filed observation ([meissner](meissner.md)).

### 4.3 Established Quantitative Boundaries

- Critical temperatures (handbook, ambient pressure): Nb \(T_c = 9.25\,\mathrm{K}\); Pb \(7.2\,\mathrm{K}\); Sn \(3.72\,\mathrm{K}\); Hg \(4.15\,\mathrm{K}\); Al \(1.18\,\mathrm{K}\). \(\mathrm{MgB_2}\) \(39\,\mathrm{K}\). \(\mathrm{YBa_2Cu_3O_{7-\delta}}\) (YBCO) \(\approx 92\,\mathrm{K}\). Cuprates at ambient pressure extend to \(\sim 135\,\mathrm{K}\) (Hg-1223). These are material numbers, not a single universal \(T_c\).
- Type I thermodynamic critical fields at \(T\to 0\): Al \(\mu_0 H_c \approx 10.5\,\mathrm{mT}\); Pb \(\approx 80\,\mathrm{mT}\); Sn \(\approx 30\,\mathrm{mT}\). Above \(H_c\) the type-I metal is normal and \(R\) returns.
- Type II: zero resistance can survive in a mixed state between a lower field \(H_{c1}\) and an upper field \(H_{c2}\), *if vortices do not move*. Clean Nb is weakly type II, with \(\mu_0 H_{c2}(0)\) of a few tenths of a tesla; dirty Nb and alloys sit much higher. Technical numbers (order of magnitude, pinning- and orientation-dependent): NbTi \(\mu_0 H_{c2}(4.2\,\mathrm{K}) \approx 11\,\mathrm{T}\); \(\mathrm{Nb_3Sn}\) \(\mu_0 H_{c2}(0) \approx 25\)–\(30\,\mathrm{T}\); YBCO \(\mu_0 H_{c2,ab}(0)\) of order \(10^{2}\,\mathrm{T}\). Flux-flow when vortices move is a finite resistance *inside* \(H_{c2}\).
- Critical current \(I_c\) (or density \(J_c\)) is real and sharp on a given specimen, but it is not a material constant. It depends on cross-section, pinning landscape, field, and temperature. No single handbook \(I_c\) is quoted here.
- Spectroscopic gap: tunneling and infrared absorption show a threshold \(2\Delta(T)\) that closes as \(T\to T_c^-\). The weak-coupling BCS ratio \(2\Delta(0)/kT_c \approx 3.52\) is a fit to many conventional superconductors (Al sits close to it). It is not universal: Pb is \(\sim 4.3\). Cuprate gaps do not collapse onto that number.
- Coherence-length class (not one hardware number): Al \(\xi_0 \sim 1.6\,\mu\mathrm{m}\); Nb \(\xi_0 \sim 40\,\mathrm{nm}\); YBCO \(\xi_{ab} \sim 1.5\)–\(2\,\mathrm{nm}\). The related London depth \(\lambda\) is owned by [meissner](meissner.md).

**Data confidence:** High — \(T_c\), type-I \(H_c\), the existence of \(H_{c1}/H_{c2}\), persistent currents, and tunneling gaps are multiply reproduced. \(I_c\) and dirty-limit \(H_{c2}\) are high as a class and medium for any one wire.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Empirical two-fluid / GL-like field envelope (type I):

  \[
  H_c(T) \approx H_c(0)\left[1-\left(\frac{T}{T_c}\right)^2\right]
  \]

- Type II upper critical field in terms of the coherence length:

  \[
  \mu_0 H_{c2} = \frac{\Phi_0}{2\pi\xi^2}, \qquad \Phi_0 = \frac{h}{2e} \approx 2.07\times 10^{-15}\,\mathrm{Wb}
  \]

- Spectroscopic gap (BCS weak-coupling *fit*, not a universal law):

  \[
  \frac{2\Delta(0)}{kT_c} \approx 3.52
  \]

  \(\Delta(T)\to 0\) as \(T\to T_c^-\). Quasiparticle tunneling current is suppressed for \(|eV| < 2\Delta\).

- A transport current produces dissipation once it depins vortices (type II) or exceeds the pair-breaking / Silsbee budget (type I). The observed \(I_c\) is that threshold on the specimen, not a first-principles constant.

Pairing mechanisms are not recorded as QSA content. The isotope effect, phonon spectra, and cuprate phenomenology are experimental facts that belong to a mechanism discussion this entry does not enter.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A coherent superconducting volume at least of order the coherence length in each direction — micrometres in clean Al, nanometres in YBCO. That is a *class* of buffer, not a single measured cliff analogous to the 10–20 nm mirror. Granular films and nanowires lose zero resistance when the coherent cross-section is under-provisioned or when phase slips become frequent; those thresholds are sample-specific. The macroscopic persistent current further requires a closed loop large enough to hold a trapped fluxoid (see [flux-quantization](flux-quantization.md)).

- **Clock rate / latency.** The spectroscopic gap sets a frequency scale \(2\Delta/h\): of order \(10^{11}\,\mathrm{Hz}\) for conventional metals (\(\Delta\) in meV) and higher in cuprates. AC dissipation (Mattis–Bardeen / residual resistance) rises as the drive approaches that scale. DC zero resistance is the \(\omega\to 0\) output, not a statement that the condensate has no internal clock.

- **Energy barriers or thresholds.** The measured gap \(2\Delta\) is the energy threshold that suppresses ordinary quasiparticle transport. \(kT_c\), \(\mu_0 H_c\) (or \(H_{c2}\)), and the specimen \(I_c\) are the three macroscopic envelopes that close that gap or destroy the coherent current. Holding a persistent current in a closed loop costs no continuous voltage.

- **Dominant failure modes.**
  - Thermal: \(T > T_c\) → gap closes → finite \(R\).
  - Field: \(H > H_c\) (type I) or \(H > H_{c2}\) (type II) → condensate gone → finite \(R\). Between \(H_{c1}\) and \(H_{c2}\), *complete field expulsion* has already failed while \(R=0\) can still hold if vortices are pinned. That split is why [meissner](meissner.md) is a separate artifact.
  - Current: \(I > I_c\) → dissipation (pair-breaking, hot spots, or flux flow).
  - Pinning (type II only): mobile vortices → flux-flow resistance *inside* \(H_{c2}\). Pinning is a mesoscale step, not specified by \(T_c\) or \(\Delta\) alone.

- **Emergent constant or stable output.** DC resistance below the instrument floor, and a persistent loop current at zero continuous voltage, for as long as \(T\), \(H\), and \(I\) remain inside the envelope above.

### 4.6 Internal Consistency Notes

The triple collapse \(T_c / H_c(H_{c2}) / I_c\) maps cleanly onto thermal, field-threshold, and current-budget failures of a gapped coherent state. Zero continuous voltage is exactly what a dissipationless current is supposed to cost. The split from Meissner is required by the data: type-II mixed-state wires carry lossless current while flux has already entered.

The mapping does *not* close on hardware identity. The coherence length spans three orders of magnitude across materials; QSA does not have a single buffer number for “the condensate.” Vortex pinning — the mesoscale reason \(R=0\) can outlive complete expulsion — is not yet a buffer / barrier specification. Both gaps are recorded rather than filled.

This entry does not assert a pairing mechanism. \(2\Delta/kT_c \approx 3.52\) is filed as a fit to many conventional superconductors, not as a universal node rule. Cuprates, heavy-fermion systems, and other families that leave that ratio (or an s-wave gap) are not treated as contradictions of a law this file never claimed.

[Superfluid helium-4](superfluid-helium-4.md) is the chargeless analogue (zero viscosity below \(T_\lambda\)); [electron-heat-capacity](electron-heat-capacity.md) reads the same gap as an exponential freeze-out of electronic \(C\). Neither is required to close the transport mapping.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(T_c\), \(H_c/H_{c2}\), \(I_c\), and \(2\Delta\) are solid measured envelopes and translate into gap, field, and current failures, but the minimum coherent volume is not a single hardware number and the pinning step that protects \(R=0\) after Meissner has failed is still unspecified.

## Related entries

- [Meissner effect](meissner.md) — field expulsion; different artifact, same condensate
- [Josephson effect](josephson-effect.md) — pair current through a weak link; voltage–frequency lock
- [Flux quantization](flux-quantization.md) — closed-loop fluxoid \(\Phi_0 = h/2e\)
- [Type-II critical field](type-ii-critical-field.md) — mixed state, \(H_{c1}/H_{c2}\), vortex lattice
- [Superfluid helium-4](superfluid-helium-4.md) — chargeless gapped-coherence analogue
- [Electron heat capacity](electron-heat-capacity.md) — the same gap read in the electronic heat capacity
