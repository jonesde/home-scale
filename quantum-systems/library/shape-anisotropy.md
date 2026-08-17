---
id: shape-anisotropy
title: Shape Anisotropy (Geometry Barrier)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - spatial-buffer
  - field-threshold
  - thermal
confidence_data: high
confidence_mapping: high
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - magnetic-domains
  - superparamagnetism
  - magnetostriction
updated: 2026-08-17
---

# Shape Anisotropy (Geometry Barrier)

### 4.1 Effect Name

Shape anisotropy (geometry barrier)

### 4.2 Macroscopic Observation

A strongly elongated particle or needle of a high-magnetization ferromagnet remains magnetized along its long axis after the applied field is removed, even when the crystal anisotropy \(K_1\) is small. A sphere of the same material does not supply that directional memory from geometry: all axes are equivalent and the shape barrier is gone. Thin films of soft magnets lie in-plane unless a perpendicular crystal anisotropy exceeds the film demag term. Alnico-class magnets hold remanence primarily by elongated Fe–Co precipitates in a matrix, not by a rare-earth-scale \(K_1\).

### 4.3 Established Quantitative Boundaries

- Demagnetizing factors of a uniformly magnetized ellipsoid (SI): \(N_x + N_y + N_z = 1\). Sphere: \(N = 1/3\) on every axis, so \(N_s - N_l = 0\). Infinite needle (prolate limit): \(N_l \to 0\), \(N_t \to 1/2\), so \(N_t - N_l \to 1/2\). Thin film: \(N_\perp \to 1\), \(N_\parallel \to 0\).
- Collapse of the geometry barrier: aspect ratio \(\to 1\) (sphere / cube class) \(\Rightarrow \Delta N \to 0\). Needles and thin plates are the opposite limit.
- Magnetostatic energy-density scale \((\mu_0/2)M_s^2\) is of order \(1\)–\(2\,\mathrm{MJ\,m^{-3}}\) in Fe (\(\mu_0 M_s \approx 2.15\,\mathrm{T}\)). That is the same order as a hard-magnet \(K_1\), which is why shape alone can latch a high-\(M_s\) needle. In Ni the same scale is several times smaller (\(\mu_0 M_s \approx 0.6\,\mathrm{T}\)).
- Soft iron itself has \(K_1\) of only \(\sim 10^4\,\mathrm{J\,m^{-3}}\) class and \(H_c < 10^2\)–\(10^3\,\mathrm{A\,m^{-1}}\) in bulk. The same iron, drawn into a high-aspect particle, shows a uniaxial barrier set by \(\Delta N\), not by that small \(K_1\).
- Thermal volume clause is unchanged in form: \(K_\mathrm{shape}V \gtrsim 25\,kT\) on laboratory time, with \(K_\mathrm{shape}\) now from \(\Delta N\) rather than from \(K_1\). Filed with the grain-volume collapse as [superparamagnetism](superparamagnetism.md).

**Data confidence:** High — ellipsoid demag factors, the sphere vs needle limits, and Fe’s \(M_s\) (hence the MJ m\(^{-3}\) magnetostatic scale) are standard. A given particle’s \(\Delta N\) is as accurate as its shape; real precipitates are not perfect ellipsoids.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Uniform-ellipsoid demagnetizing field: \(\mathbf{H}_d = -\mathsf{N}\cdot\mathbf{M}\), with \(\mathrm{tr}\,\mathsf{N} = 1\).
- Magnetostatic energy density:

  \[
  u_d = \frac{\mu_0}{2}\,\mathbf{M}\cdot\mathsf{N}\cdot\mathbf{M}
  \]

- Uniaxial shape-anisotropy density along the long axis of a prolate body:

  \[
  K_\mathrm{shape} = \frac{\mu_0}{2}M_s^2\,(N_t - N_l)
  \]

  \(N_t - N_l \to 0\) as the aspect ratio \(\to 1\); \(N_t - N_l \to 1/2\) for an infinite needle. Prefactor conventions differ by whether the energy is written \(\mu_0 M_s^2 \Delta N / 2\) or an equivalent; the measured fact is the \(\Delta N\) collapse, not the typesetting of the \(1/2\).

- Thin-film limit: an out-of-plane magnetization pays \(\approx (\mu_0/2)M_s^2\). In-plane magnetization does not. Perpendicular remanence appears only when a crystal or interface \(K\) exceeds that film term.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A ferromagnetic body whose *shape* is not isotropic — a nonzero \(\Delta N\) — and whose volume still satisfies \(K_\mathrm{shape}V \gtrsim 25\,kT\). A sphere has no geometry barrier at any size. A needle still fails if it is too small for the remaining \(K_\mathrm{shape}V\) to beat \(kT\). The latch cell is the particle (or precipitate), not the unit cell.

- **Clock rate / latency.** Same magnetic clocks as the parent latch: precession at \(\approx 28\,\mathrm{GHz\,T^{-1}}\); write latency set by the field sweep and by reversal mode (coherent rotation vs curling / buckling in real needles). Geometry changes the barrier; it does not invent a new carrier frequency.

- **Energy barriers or thresholds.** The barrier is magnetostatic and geometric: \(\Delta N\,(\mu_0/2)M_s^2 V\). No large \(K_1\) is required. Holding the long-axis remanent state costs zero continuous power. Energy is spent to rotate \(M\) off the long axis (the hard-axis or switching field of order \(H_K \sim M_s\Delta N\)).

- **Dominant failure modes.**
  - Geometry: aspect ratio \(\to 1\) \(\to \Delta N \to 0\) \(\to\) no shape latch. This is the defining collapse.
  - Thermal / volume: \(K_\mathrm{shape}V\) below the stability line \(\to\) superparamagnetic erasure.
  - Material: \(M_s \to 0\) (\(T > T_C\), or a weak moment) \(\to\) magnetostatic scale collapses even for a needle.
  - Field: a reverse field of order the shape-anisotropy field writes the opposite long-axis state.
  - Domain breakup: a particle large enough to support walls may no longer reverse as a single latch cell ([magnetic-domains](magnetic-domains.md)).

- **Emergent constant or stable output.** A uniaxial remanent direction locked to the long axis (or to the film plane), at zero continuous power, without a large magnetocrystalline \(K_1\).

### 4.6 Internal Consistency Notes

The mapping is the cleanest geometry clause in the latched-order family: the barrier is \(\Delta N\), and \(\Delta N = 0\) is a sharp, checkable collapse. It explains how a soft, low-\(K_1\) metal can still hold remanence once the body is a needle, and why the parent NdFeB latch does *not* need shape — its \(K_1\) already exceeds the magnetostatic scale. Alnico-class magnets sit on this file; sintered NdFeB sits on [permanent-magnet-latch](permanent-magnet-latch.md).

Uniform-ellipsoid \(\mathsf{N}\) is an idealization. Real precipitates, lithographed bits, and films have nonuniform magnetization and stray-field concentrations at corners. Those corrections change the numerical switching field (they are part of the same mesoscale \(H_c\) gap as on the hysteresis file). They do not remove the aspect-ratio \(\to 1\) collapse. Shape and crystal anisotropy simply add when both are present; this entry owns the \(\Delta N\) term only.

### 4.7 Overall Confidence in the QSA Mapping

**High** — demag factors, the sphere / needle / film limits, and the \(M_s^2\) energy scale are solid and translate directly into a geometry barrier and a unique aspect-ratio collapse.

## Related entries

- [permanent-magnet-latch](permanent-magnet-latch.md) — crystal-\(K_1\) latch; this file is the geometry alternative
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — the write / erase cycle whose barrier may be this \(\Delta N\)
- [magnetic-domains](magnetic-domains.md) — magnetostatic energy that, in a large body, is spent on walls rather than on a single-domain shape latch
- [superparamagnetism](superparamagnetism.md) — \(KV\) collapse with \(K\) now equal to \(K_\mathrm{shape}\)
- [magnetostriction](magnetostriction.md) — strain that can change effective shape and add a magnetoelastic term
