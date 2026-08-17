---
id: superparamagnetism
title: Superparamagnetism (Volume Collapse of the Magnetic Latch)
status: formal
family: latched-order
constraints:
  - spatial-buffer
  - energy-barrier
  - thermal
  - mechanical-lattice
confidence_data: high
confidence_mapping: high
related:
  - permanent-magnet-latch
  - ferromagnetic-hysteresis
  - magnetic-domains
  - shape-anisotropy
  - curie-paramagnetism
updated: 2026-08-17
---

# Superparamagnetism (Volume Collapse of the Magnetic Latch)

### 4.1 Effect Name

Superparamagnetism (volume collapse of the magnetic latch)

### 4.2 Macroscopic Observation

A fine ferromagnetic or ferrimagnetic powder that would be a permanent magnet in bulk shows no usable remanence and no coercivity on laboratory timescales. Magnetization follows an applied field reversibly and saturates at large field; when the field is removed the net moment returns to zero. Cooling the same particles restores hysteresis below a blocking temperature. Holding the unblocked state costs no continuous power; the directional memory is simply gone.

### 4.3 Established Quantitative Boundaries

- Same latch hardware as [permanent-magnet-latch](permanent-magnet-latch.md). Room-temperature uniaxial anisotropy of \(\mathrm{Nd_2Fe_{14}B}\): \(K_1 \approx 4.5\,\mathrm{MJ\,m^{-3}}\). Magnetite \(\mathrm{Fe_3O_4}\) at \(300\,\mathrm{K}\): \(|K_1| \approx 1.35 \times 10^{4}\,\mathrm{J\,m^{-3}}\) (cubic; two orders of magnitude smaller). Shape anisotropy can exceed magnetocrystalline anisotropy in non-equant magnetite and must not be folded into a single \(K\).
- Néel–Arrhenius laboratory-stability criterion: \(KV \gtrsim 25\,kT\). With \(K_1 = 4.5\,\mathrm{MJ\,m^{-3}}\) at \(300\,\mathrm{K}\),

  \[
  V \gtrsim \frac{25\,kT}{K_1} \approx 2.3 \times 10^{-26}\,\mathrm{m^3}
  \]

  i.e. a characteristic linear size of order \(30\,\mathrm{nm}\) for a uniaxial NdFeB grain. Magnetite’s laboratory blocking size is smaller — typically in the \(10\)–\(30\,\mathrm{nm}\) class for near-equant grains — and moves with shape and with the observation window. There is no single magnetite cliff.
- The factor \(25\) is a *timescale convention*, not a sharp experimental cliff. It corresponds to \(\tau \sim 10^{1}\)–\(10^{2}\,\mathrm{s}\) for attempt times \(\tau_0 \sim 10^{-10}\)–\(10^{-12}\,\mathrm{s}\) (ordinary magnetometry). Magnetic recording uses a \(40\)–\(60\,kT\) convention for archival (year-scale) retention. Mössbauer spectroscopy windows sit near \(10^{-8}\,\mathrm{s}\), so the same grain can look blocked in one apparatus and unblocked in another.
- Macroscopic signatures on the unblocked side of the window: coercivity and remanence collapse to zero; \(M(H)\) is reversible and Langevin-like. Below a blocking temperature \(T_B\) the same particles recover a hysteresis loop.
- Two relaxation channels must be kept separate. **Néel** relaxation flips the moment inside a fixed lattice — this is the volume collapse of the latch. **Brownian** relaxation rotates the whole particle in a fluid (ferrofluids). Only the first is superparamagnetism of the crystalline latch.

**Data confidence:** High — \(K_1\), the Néel–Arrhenius form, and the disappearance of remanence below a volume / temperature / time surface are standard measured facts. Any one commercial powder’s blocking diameter is medium (size distribution, surface anisotropy, interactions).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Uniaxial barrier between easy directions:

  \[
  \Delta E \approx K_1 V
  \]

  Cubic magnetocrystalline anisotropy does not use this uniaxial form; the barrier is a fraction of \(|K_1|V\) and is not substituted here as if it were \(K_1 V\).

- Néel–Arrhenius escape time:

  \[
  \tau = \tau_0 \exp\!\left(\frac{KV}{kT}\right)
  \]

  \(\tau_0\) is empirically \(10^{-10}\)–\(10^{-12}\,\mathrm{s}\). Blocking on a measurement window \(\tau_m\) is the contour \(KV = kT\ln(\tau_m/\tau_0)\).

- Superparamagnetic \(M(H)\) of an isotropic ensemble of moments \(m = M_s V\):

  \[
  M = n m \left(\coth\xi - \frac{1}{\xi}\right), \qquad \xi = \frac{\mu_0 m H}{kT}
  \]

- Curie (or Néel) point of the parent order is a different thermal ceiling: \(M_s(T)\to 0\) as \(T\to T_C^-\). A grain can be superparamagnetic well below \(T_C\).

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The latch cell of the permanent magnet — a crystalline anisotropy environment with \(KV\) above the stability line of the observation window. For NdFeB at room temperature and laboratory time that cell is tens of nanometres. Below it the barrier is under-provisioned by *volume*, not by a missing anisotropy mechanism. This is to the magnet what the 5–10 nm film is to the mirror: the spatial-buffer clause of the same latch. A single unblocked grain’s fluctuating moment is not a usable motor; the observed Langevin curve is already an ensemble average.

- **Clock rate / latency.** Thermal escape attempts run on the \(\tau_0\) scale (\(\sim 10^{-11}\,\mathrm{s}\)). In a stable grain they bounce off the barrier. In an under-volume grain they succeed inside \(\tau_m\), and the directional state is rewritten at random. Single-spin precession remains \(\approx 28\,\mathrm{GHz\,T^{-1}}\); that carrier is not the failure clock.

- **Energy barriers or thresholds.** The same magnetocrystalline (or shape) barrier \(\Delta E \approx KV\) that holds a permanent magnet. Superparamagnetism is not a different barrier; it is that barrier times an insufficient \(V\), compared with \(kT\ln(\tau_m/\tau_0)\).

- **Dominant failure modes.**
  - Spatial / thermal: \(KV \lesssim kT\ln(\tau_m/\tau_0)\) → thermal erasure of the directional latch on the observation window → zero remanence, zero coercivity.
  - Thermal, parent order: \(T > T_C\) → \(M_s \to 0\). The ordered moment itself is gone; that is the Curie collapse of the parent entry, not this volume cliff.
  - Mechanical: lattice destruction removes the anisotropy matrix, as on the bulk magnet.
  - Field: a large \(H\) saturates the Langevin curve; that is a driven alignment of unlocked moments, not a write of a latch.

- **Emergent constant or stable output.** On the unblocked side: a reversible, zero-remanence magnetization curve and a blocking contour \(T_B(V,\tau_m)\). On the blocked side: the directional latch of the parent magnet. Zero continuous power in either case.

### 4.6 Internal Consistency Notes

The volatile / non-volatile split on the parent magnet entry already pointed at this clause. Mapping the same \(K_1 V\) barrier onto a volume cliff, at fixed material and temperature, is internally consistent: the latch hardware is unchanged; the buffer is the grain.

The \(25\,kT\) line must not be treated as a universal energy cliff. It is a contour of \(\tau_m\). A mapping that hid the timescale dependence would over-claim a single hardware number. Recording-media (\(40\)–\(60\,kT\)) and Mössbauer windows are the same contour read at different clocks, which is consistent rather than contradictory.

A remaining gap, inherited from the parent entry: real coercivity is not \(H_a\), and real \(K\) of a nanoparticle is not the bulk \(K_1\). Surface anisotropy, grain-boundary structure, and dipolar coupling sit between the unit-cell anisotropy and the observed \(T_B\). QSA does not yet have a clean buffer / barrier specification for that mesoscale step. The existence of a volume-and-time collapse does not depend on closing it.

Brownian relaxation in a fluid is a different machine (the whole particle is the rotator). It can mimic a vanishing remanence without the crystalline latch having failed. That channel is noted so it is not folded into this entry.

Contrast with [curie-paramagnetism](curie-paramagnetism.md): a Curie \(1/T\) susceptibility is an ensemble of *never-latched* moments. Superparamagnetism is a latch that has become fast compared with the observer.

### 4.7 Overall Confidence in the QSA Mapping

**High** — \(K\), \(V\), \(T\), and \(\tau_m\) form a measured collapse surface that translates directly into the spatial-buffer clause of the magnetic latch; the open items are the mesoscale \(K_\mathrm{eff}\) step and the convention-not-cliff status of any one numerical factor, not the existence of the volume failure.

## Related entries

- [Permanent magnet (directional latch)](permanent-magnet-latch.md) — the same barrier, provisioned at bulk grain volume
- [Ferromagnetic hysteresis](ferromagnetic-hysteresis.md) — write / erase cycle; remanence and coercivity go to zero on this side of the blocking line
- [Magnetic domains](magnetic-domains.md) — how a large body partitions aligned volume; single-domain grains are the ones that can go superparamagnetic
- [Shape anisotropy](shape-anisotropy.md) — a geometry barrier that can dominate \(K_\mathrm{eff}\) in non-equant particles
- [Curie paramagnetism](curie-paramagnetism.md) — unlocked-spin ensemble with no latch to collapse
