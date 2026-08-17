---
id: josephson-effect
title: Josephson Effect (Weak-Link Phase Current)
status: formal
family: gapped-coherence
constraints:
  - spatial-buffer
  - clock-latency
  - energy-barrier
  - thermal
  - field-threshold
confidence_data: high
confidence_mapping: high
related:
  - superconductivity
  - meissner
  - flux-quantization
  - type-ii-critical-field
  - superfluid-helium-4
  - quantum-hall-effect
updated: 2026-08-17
---

# Josephson Effect (Weak-Link Phase Current)

### 4.1 Effect Name

Josephson effect (weak-link phase current)

### 4.2 Macroscopic Observation

Two superconducting electrodes separated by a thin insulating barrier, a short normal-metal bridge, or a geometric constriction pass a dissipationless current at zero DC voltage up to a junction-specific critical current \(I_c\). Above \(I_c\) a finite DC voltage appears across the link. That voltage is locked to a microwave frequency: the junction oscillates, and an applied microwave tone produces constant-voltage Shapiro steps. Thickening the barrier sends \(I_c\) to zero. Warming either electrode through its critical temperature removes the effect.

### 4.3 Established Quantitative Boundaries

- Voltage–frequency lock (AC Josephson relation, used as a voltage standard):

  \[
  \nu = \frac{2e}{h}\,V \approx 483.6\,\mathrm{MHz\,\mu V^{-1}}
  \]

  Equivalently \(V = (h/2e)\,\nu = \Phi_0\,\nu\), with \(\Phi_0 = h/2e = 2.0678\times 10^{-15}\,\mathrm{Wb}\).

- Shapiro steps under microwave irradiation at frequency \(f\) sit at the discrete voltages \(V_n = n\,h f / 2e\) (\(n = 0, \pm 1, \pm 2, \ldots\)).
- \(I_c\) is set by the junction (area, barrier transparency, electrode gap) and is not a universal constant. It is a measured operating point of that weak link.
- SIS oxide barriers that still carry a usable weak-link current are a few nanometres thick. A thicker continuous insulator drives \(I_c \to 0\); the electrodes then behave as two separate superconductors.
- Magnetic flux through the junction area of order \(\Phi_0\) modulates \(I_c\) (Fraunhofer diffraction in a uniform rectangular junction). A field that drives the electrodes normal is a different, coarser collapse, owned by [superconductivity](superconductivity.md) / [type-ii-critical-field](type-ii-critical-field.md).
- Both electrodes must sit below their own \(T_c\). There is no Josephson current between two normal metals at the same barrier thickness.

**Data confidence:** High — the voltage–frequency ratio is a metrological constant; Shapiro steps, the few-nanometre SIS window, and the \(I > I_c\) / \(T > T_c\) collapses are multiply reproduced.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Current–phase and voltage–phase relations:

  \[
  I = I_c\sin\phi, \qquad \frac{d\phi}{dt} = \frac{2e}{\hbar}V
  \]

  \(\phi\) is the gauge-invariant phase difference across the link. The second equation is the AC lock of §4.3.

- Zero-voltage branch: a DC supercurrent exists only for \(|I| \le I_c\). For \(|I| > I_c\) the junction is on a resistive branch and \(V \neq 0\).
- Magnetic modulation of a uniform rectangular junction:

  \[
  I_c(\Phi) = I_c(0)\left|\frac{\sin(\pi\Phi/\Phi_0)}{\pi\Phi/\Phi_0}\right|
  \]

  The period is the same \(\Phi_0\) as in [flux-quantization](flux-quantization.md).

- Resistively shunted junction (RSJ) bookkeeping of the voltage-carrying state uses the junction capacitance and a shunt resistance as circuit elements. Those parameters fit \(I\)–\(V\) curves; they are not used here as a mechanism claim.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested buffers. (1) Each electrode must itself be a superconducting condensate — the hardware of [superconductivity](superconductivity.md), with that entry’s \(T_c\), coherence length, and gap. (2) The electrodes must be coupled by a *weak* link whose thickness sits in a narrow window: a few nanometres for an SIS barrier. Thicker, and the coupling resource is starved (\(I_c \to 0\)). Absent, and the two sides are one superconductor with no junction degree of freedom. The load-bearing node of *this* artifact is the phase difference \(\phi\) across that under-coupled spatial buffer.

- **Clock rate / latency.** The AC Josephson lock is the clock: \(\nu / V \approx 483.6\,\mathrm{MHz\,\mu V^{-1}}\). A microvolt bias oscillates at hundreds of megahertz; a millivolt bias sits in the sub-terahertz. Shapiro steps are the same clock read out against an external microwave drive. This is a frequency locked to a voltage, not a plasma-period screening cycle.

- **Energy barriers or thresholds.** \(I_c\) is the current threshold that protects the zero-voltage branch. The electrode gap (whatever its microscopic origin) is the energy scale that vanishes at \(T_c\) and takes \(I_c\) with it. A flux of order \(\Phi_0\) through the junction is a field threshold that suppresses \(I_c\) without first destroying the electrodes.

- **Dominant failure modes.**
  - Spatial: barrier too thick (or too opaque) \(\to I_c \to 0\) \(\to\) no weak-link current.
  - Current: \(I > I_c\) \(\to\) finite DC voltage; the zero-voltage branch is gone.
  - Thermal: \(T > T_c\) in either electrode \(\to\) parent condensate gone.
  - Field: flux through the junction of order \(\Phi_0\) collapses \(I_c\); a still larger field that exceeds the electrode \(H_c\) / \(H_{c2}\) destroys the electrodes themselves.

- **Emergent constant or stable output.** A dissipationless weak-link current at \(V = 0\) for \(|I| \le I_c\), and a universal voltage–frequency lock \(V = (h/2e)\,\nu\) once a voltage is present. The lock is the synchronized output used as a voltage standard.

### 4.6 Internal Consistency Notes

The four collapses — thick barrier, \(I > I_c\), \(T > T_c\), flux of order \(\Phi_0\) — sit where a weak-link machine with a current threshold and a voltage-locked clock should fail. The same \(\Phi_0\) appears here and in [flux-quantization](flux-quantization.md); that is a consistency check, not two constants.

A remaining gap: the measured charge increment in \(h/2e\) is *taken* from the voltage–frequency lock and from the flux quantum. QSA does not derive why the increment is \(2e\) rather than \(e\) from node rules alone. That increment is recorded as data. No pairing story is required to locate the collapses, and none is added.

The RSJ circuit elements (\(C\), \(R\)) fit which voltage-carrying branch is observed; they do not change the hardware window or the lock. They are left as descriptive bookkeeping.

A chargeless analog of a weak-link current exists in helium-4 apertures; that comparison belongs on [superfluid-helium-4](superfluid-helium-4.md) and does not alter the electrical specifications here.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the voltage–frequency lock, the few-nanometre SIS window, and the \(I_c\) / \(T_c\) / \(\Phi_0\) collapses are sharp measured boundaries and translate directly into buffer, clock, threshold, and failure-envelope specifications; the open item is the origin of the \(2e\) increment, not the location of the collapses.

## Related entries

- [superconductivity](superconductivity.md) — parent gapped condensate; both electrodes must sit inside that envelope
- [meissner](meissner.md) — same condensate, field-expulsion artifact; not the weak-link current
- [flux-quantization](flux-quantization.md) — same \(\Phi_0\); a closed loop rather than a single link
- [type-ii-critical-field](type-ii-critical-field.md) — electrode-scale field collapse (\(H_{c2}\)) and vortex entry, distinct from junction Fraunhofer modulation
- [superfluid-helium-4](superfluid-helium-4.md) — chargeless coherence; weak-link / aperture analog
- [quantum-hall-effect](quantum-hall-effect.md) — the complementary metrological lock (\(R_K = h/e^2\))
