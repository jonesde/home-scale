---
id: permanent-magnet-latch
title: Permanent Magnet (Directional Latch)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - thermal
  - mechanical-lattice
  - spatial-buffer
confidence_data: high
confidence_mapping: high
related:
  - superparamagnetism
  - ferromagnetic-hysteresis
  - magnetic-domains
  - shape-anisotropy
  - magnetostriction
updated: 2026-08-17
---

# Permanent Magnet (Directional Latch)

### 4.1 Effect Name

Permanent magnet (directional latch)

### 4.2 Macroscopic Observation

A hard permanent magnet (for example sintered NdFeB) exerts a continuous directional mechanical force on iron and on other magnets with no external power input and no continuous heat generation while the magnet sits at rest. Soft magnetic materials (annealed iron, many electrical steels) take a large magnetization in an applied field and lose almost all useful remanence when that field is removed. Heating a hard magnet through its Curie point, or severely deforming its lattice, destroys the net directional force.

### 4.3 Established Quantitative Boundaries

- Free-electron spin precession / magnetic-resonance frequency: \(\gamma/2\pi \approx 28.025\,\mathrm{GHz\,T^{-1}}\).
- \(\mathrm{Nd_2Fe_{14}B}\) Curie temperature: \(T_C \approx 585\,\mathrm{K}\) (\(312^\circ\mathrm{C}\)). Commercial NdFeB grades span roughly \(310\)–\(400^\circ\mathrm{C}\) depending on Co substitution. Above \(T_C\), net magnetization is gone.
- Room-temperature uniaxial anisotropy of \(\mathrm{Nd_2Fe_{14}B}\): \(K_1 \approx 4.5\,\mathrm{MJ\,m^{-3}}\); anisotropy field \(\mu_0 H_a \approx 7\)–\(8\,\mathrm{T}\). These are the numbers that distinguish a hard latch from a soft host.
- Soft iron and silicon steel: coercivity typically \(< 10^2\)–\(10^3\,\mathrm{A\,m^{-1}}\) (often much lower in annealed stock). Remanence exists but is small against self-demagnetizing fields, so the sample does not remain a useful permanent magnet once the applied field is removed. Iron’s own Curie point is \(\approx 1043\,\mathrm{K}\) (\(770^\circ\mathrm{C}\)) — the metal is still ferromagnetic, just not latched in a useful direction.
- Mechanical shock, plastic deformation, and decrepitation can destroy useful remanence without reaching \(T_C\) (lattice / grain-structure failure).
- A static magnet at rest produces no continuous \(I^2R\) or hysteresis heat. Energy is consumed to *change* the magnetization (the hysteresis loop), not to hold it.
- Volume stability (same barrier, now times grain volume): the conventional Néel–Arrhenius laboratory-stability criterion is \(KV \gtrsim 25\,kT\). With \(K_1 = 4.5\,\mathrm{MJ\,m^{-3}}\) at \(300\,\mathrm{K}\),

  \[
  V \gtrsim \frac{25\,kT}{K_1} \approx 2.3 \times 10^{-26}\,\mathrm{m^3}
  \]

  i.e. a characteristic linear size of order \(30\,\mathrm{nm}\) for a uniaxial NdFeB grain. Below that scale the latch is thermally written at random on laboratory timescales (superparamagnetism). The factor \(25\) is a *timescale convention*, not a single sharp experimental cliff; the volume collapse itself is well established.

**Data confidence:** High — resonance frequency, \(T_C\), \(K_1\), and the hard/soft distinction are standard measured parameters. Grain-size / blocking-temperature numbers are high as a class and medium for any one commercial powder.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Zeeman / Larmor frequency:

  \[
  f = \frac{g\mu_B B}{h} \approx 28.0\,\mathrm{GHz\,T^{-1}}\quad (g \approx 2)
  \]

- Uniaxial anisotropy energy density:

  \[
  E_A = K_1\sin^2\theta
  \]

  with a per-grain barrier \(\Delta E \approx K_1 V\) between the two easy directions.

- Néel–Arrhenius attempt time for thermal escape:

  \[
  \tau = \tau_0 \exp\!\left(\frac{K_1 V}{kT}\right)
  \]

  \(\tau_0\) is empirically \(10^{-10}\)–\(10^{-12}\,\mathrm{s}\). Laboratory stability (\(\tau\) of hours to years) is the origin of the \(\sim 25\,kT\) convention.

- Magnetization collapses at the Curie point: \(M(T)\to 0\) as \(T\to T_C^-\) (mean-field critical exponent is a fit to data, not used here as a mechanism claim).

- Macroscopic force in an external field gradient: \(\mathbf{F} = \nabla(\mathbf{m}\cdot\mathbf{B})\). Useful \(\mathbf{m}\) requires a large aligned population, not a single spin.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested buffers:
  1. **Latch cell.** A crystalline anisotropy environment around each spin (or strongly coupled spin cluster) large enough that \(K_1 V \gtrsim 25\,kT\). Soft matrices do not supply this barrier → volatile alignment. Hard matrices do → non-volatile latch. For NdFeB at room temperature that cell is tens of nanometres.
  2. **Macroscopic force.** A single latched grain’s moment is not a usable motor. The observed continuous force is the synchronized output of a large aligned population (domains / grains / bulk body). There is no single universal millimetre-scale cliff analogous to the 10–20 nm mirror threshold; the force simply scales with aligned moment. The *sharp* hardware cliff is the grain-scale latch, not the sample envelope.

- **Clock rate / latency.** Baseline single-spin precession at \(\approx 28\,\mathrm{GHz\,T^{-1}}\). Thermal escape attempts occur on the \(\tau_0\) scale (\(\sim 10^{-11}\,\mathrm{s}\)) and almost always bounce off the barrier in a stable grain. Write / erase of a hard magnet is set by the applied-field sweep and domain-wall motion, not by the 28 GHz carrier.

- **Energy barriers or thresholds.** Magnetocrystalline anisotropy energy \(K_1 V\) (and, in some geometries, shape-anisotropy energy) locks orientation. Holding the latched state costs zero continuous power. Energy is spent only on transitions (the area of the hysteresis loop).

- **Dominant failure modes.**
  - Thermal, barrier: \(kT\) exceeds the anisotropy barrier at the Curie point → loss of phase coherence across the array → net-zero magnetization.
  - Thermal, volume: \(KV \lesssim 25\,kT\) at operating temperature → superparamagnetic erasure on laboratory time. Same barrier, under-provisioned volume. Filed in more detail as queued `superparamagnetism`.
  - Mechanical: lattice displacement / grain fracture destroys the directional matrix → write error across the array, often without reaching \(T_C\).
  - Field: a reverse field of order the coercivity (microstructure-dependent, much less than \(H_a\)) writes the opposite state. That is a write operation, not a destruction of the latch hardware.

- **Emergent constant or stable output.** A stable directional moment and the associated static field / force, at zero continuous power cost, for as long as the barrier, the grain volume, and the lattice remain inside the envelope above.

### 4.6 Internal Consistency Notes

The volatile / non-volatile split maps directly onto presence or absence of a sufficient anisotropy barrier. Zero continuous power is exactly what a latched state is supposed to cost. Thermal and mechanical collapses sit where the mapping says they should.

The preliminary handover listed “crystalline anisotropy environment” as the minimum hardware scale and did not separate grain volume from sample volume. Superparamagnetism is the missing spatial-buffer clause: it is to the magnet what the 5–10 nm film is to the mirror. Until `superparamagnetism` is written as its own entry, that clause lives here.

A remaining gap: coercivity of a real sintered magnet is not \(H_a\). It is set by grain-boundary structure, reverse-domain nucleation, and dipolar coupling — a mesoscale write threshold sitting between the unit-cell anisotropy and the bulk force. QSA does not yet have a clean buffer / barrier specification for that mesoscale step. The latch-vs-soft and \(T_C\) / \(KV\) collapses do not depend on closing it.

Soft iron’s high \(T_C\) plus low coercivity is internally consistent: the metal still has a ferromagnetic collective state, but the directional *memory* is missing. Ferromagnetism and the permanent-magnet latch are not the same effect. Related queued entries `ferromagnetic-hysteresis` and `magnetic-domains` own that distinction.

### 4.7 Overall Confidence in the QSA Mapping

**High** — frequencies, Curie points, anisotropy energies, and the hard/soft/volume distinctions are solid measured boundaries and translate directly into barrier, clock, buffer, and failure-envelope specifications; the open item is the mesoscale coercivity step, not the latch itself.

## Related entries

- `superparamagnetism` (queued) — volume collapse of this same latch
- `ferromagnetic-hysteresis` (queued) — the write / erase cycle; remanence and coercivity as operating points
- `magnetic-domains` (queued) — how a large body partitions the aligned population
- `shape-anisotropy` (queued) — a different barrier (sample geometry / demagnetizing field) that can latch without large \(K_1\)
- `magnetostriction` (queued) — lattice–moment coupling; mechanical failure path
