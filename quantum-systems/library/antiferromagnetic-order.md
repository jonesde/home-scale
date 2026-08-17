---
id: antiferromagnetic-order
title: Antiferromagnetic Order (Cancelled Latch)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - thermal
  - mechanical-lattice
  - field-threshold
  - spatial-buffer
confidence_data: high
confidence_mapping: high
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - exchange-bias
  - curie-paramagnetism
  - superparamagnetism
updated: 2026-08-17
---

# Antiferromagnetic Order (Cancelled Latch)

### 4.1 Effect Name

Antiferromagnetic order (cancelled latch)

### 4.2 Macroscopic Observation

Below a material-specific Néel temperature an antiferromagnet orders, but the sample exerts no useful permanent-magnet force and shows no large remanent dipole. Neutron diffraction and related probes nevertheless find a static magnetic superlattice: opposing sublattices are each magnetized and locked antiparallel. Above \(T_N\) the superlattice intensity is gone and the material is an ordinary paramagnet. Ordinary laboratory fields do not turn the ordered body into a permanent magnet.

### 4.3 Established Quantitative Boundaries

- Handbook Néel points of the rock-salt monoxide class: \(\mathrm{MnO}\) \(T_N \approx 118\,\mathrm{K}\); \(\mathrm{FeO}\) \(T_N \approx 198\,\mathrm{K}\) (stoichiometry-sensitive); \(\mathrm{NiO}\) \(T_N \approx 523\,\mathrm{K}\). These are measured collapse temperatures of the magnetic Bragg intensity and of the susceptibility cusp, not fitted parameters of a model.
- Macroscopic moment: \(M_\mathrm{net} \approx 0\) on the scale of a ferromagnet of the same sublattice magnetization. Weak canting in some compounds produces a small parasitic moment; that is a perturbation, not a permanent-magnet latch.
- Susceptibility: a cusp or kink at \(T_N\), not the ferromagnetic divergence. Above \(T_N\), Curie–Weiss \(\chi \approx C/(T+\theta)\) with \(\theta\) of the same order as \(T_N\) and opposite in sign to the ferromagnetic case. Below \(T_N\), the parallel susceptibility of a uniaxial crystal falls toward zero as \(T\to 0\); the perpendicular susceptibility stays finite.
- Ordinary applied fields (well below a spin-flop / spin-flip field) do not rewrite the AFM order into a net ferromagnet. Spin-flop fields, where they are measured, are tesla-class or larger in the monoxides and sit far above the coercivity of a soft ferromagnet.
- Holding the ordered (cancelled) state costs zero continuous power. There is no hysteresis-heat bill at rest.

**Data confidence:** High — \(T_N\) of \(\mathrm{MnO}\), \(\mathrm{NiO}\), and \(\mathrm{FeO}\), the vanishing net moment, the susceptibility cusp, and magnetic Bragg collapse are multiply reproduced handbook facts. A given crystal’s spin-flop field is medium (anisotropy- and sample-dependent).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Two-sublattice accounting: \(\mathbf{M}_A \approx -\mathbf{M}_B\), so \(\mathbf{M}_\mathrm{net} = \mathbf{M}_A + \mathbf{M}_B \approx 0\). Each sublattice magnetization is of ordinary atomic-moment size.
- Curie–Weiss form above \(T_N\):

  \[
  \chi = \frac{C}{T + \theta},\qquad \theta > 0
  \]

  with \(\theta\) comparable to \(T_N\). This is the measured unlocked-ensemble envelope, filed in contrast as [curie-paramagnetism](curie-paramagnetism.md).
- Magnetic Bragg intensity \(\to 0\) as \(T\to T_N^-\). Mean-field \(T_N \sim J\) identifies the exchange energy with the thermal cliff; the identification is a fit to that cliff, not a derivation of \(J\) from a node rule.
- Spin-flop: at a threshold field the sublattices rotate to a configuration with a small net moment along \(\mathbf{H}\). That threshold is a field write of the AFM configuration, not the everyday coercivity of a ferromagnet.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two (or more) interpenetrating sublattices, each a directional latch, correlated over a volume large enough that exchange can hold the antiparallel relation against \(kT\). A single spin is not an antiferromagnet. The *macroscopic* signature is the cancelled total, so the readable hardware is the superlattice (neutron / resonant x-ray / AFM-resonance), not a dipole field.

- **Clock rate / latency.** The protecting energy is exchange, set by \(kT_N\). The corresponding rate is far above ordinary ferromagnetic FMR. Macroscopic readout of the cancelled moment has no slow write unless a spin-flop field or an exchange-bias field-cool is imposed.

- **Energy barriers or thresholds.** Exchange locks each sublattice against the other. The barrier holds at zero continuous power. The emergent dipole is \(\sim 0\) *because* the two latches are opposed; the cancelled force is the output, not a failure of the latch.

- **Dominant failure modes.**
  - Thermal: \(T > T_N\) \(\to\) sublattice order gone \(\to\) magnetic Bragg intensity gone, Curie–Weiss paramagnet.
  - Mechanical: destruction of the lattice that defines the two sublattices erases the AFM matrix without a well-defined \(T_N\).
  - Field: a spin-flop / spin-flip field rewrites the relative orientation. Ordinary laboratory \(H\) is usually under that threshold.
  - Spatial: a particle so small that the AFM correlation cannot hold (blocking / finite-size reduction of \(T_N\)) — the volume analog of [superparamagnetism](superparamagnetism.md), without a single portable \(KV\) number claimed here.

- **Emergent constant or stable output.** A static antiparallel superlattice with \(M_\mathrm{net}\approx 0\), held at zero continuous power below \(T_N\). The coupling of that cancelled latch into a ferromagnet is filed as [exchange-bias](exchange-bias.md).

### 4.6 Internal Consistency Notes

A latch is defined by a barrier that holds a configuration at zero continuous power, not by a nonzero dipole. AFM order meets that definition: two remanent sublattices, a sharp thermal cliff, no hold-power bill. Treating “no force on iron” as evidence that nothing is latched would contradict the neutron superlattice and the \(T_N\) collapse. The cancelled output is internally consistent.

The mapping takes the sign of the inter-sublattice coupling as data (the lattice and electronic structure that make \(J\) antiferromagnetic). QSA does not here derive why \(\mathrm{MnO}\) is AFM and Fe is FM. That is a gap in the node rules, not a gap in the latch accounting. Weak ferromagnetism / canting in some compounds is a small uncancelled remainder; it does not convert the family into the permanent-magnet latch.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(T_N\), vanishing net moment, magnetic Bragg collapse, and zero hold power specify a cancelled latch cleanly; the open item is the microscopic origin of the AFM sign of \(J\), not the identification of the ordered state.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — the uncancelled cousin: same class of barrier, nonzero macro moment
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — write / erase cycle of uncancelled order; contrast case
- [exchange-bias](exchange-bias.md) — this cancelled latch as the pin on a ferromagnet
- [curie-paramagnetism](curie-paramagnetism.md) — unlocked ensemble above \(T_N\)
- [superparamagnetism](superparamagnetism.md) — volume collapse of a magnetic latch; finite-size AFM is the analog
