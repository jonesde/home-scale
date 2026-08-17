---
id: exchange-bias
title: Exchange Bias (Pinned-Loop Shift)
status: formal
family: latched-order
constraints:
  - energy-barrier
  - thermal
  - field-threshold
  - spatial-buffer
confidence_data: high
confidence_mapping: medium
related:
  - antiferromagnetic-order
  - ferromagnetic-hysteresis
  - permanent-magnet-latch
  - superparamagnetism
  - magnetic-domains
updated: 2026-08-17
---

# Exchange Bias (Pinned-Loop Shift)

### 4.1 Effect Name

Exchange bias (pinned-loop shift)

### 4.2 Macroscopic Observation

A ferromagnet in contact with an antiferromagnet, after cooling in a magnetic field through the antiferromagnet’s blocking temperature, shows a hysteresis loop that is shifted along the field axis rather than centered at \(H = 0\). The shift is the exchange-bias field \(H_\mathrm{ex}\). Raising the temperature through that blocking temperature, or removing the AFM layer, returns a centered loop. The shifted remanent state is then held at zero continuous power.

### 4.3 Established Quantitative Boundaries

- Classic observation: Meiklejohn and Bean (1956), Co particles with a CoO shell, field-cooled through the oxide’s Néel region. The same shift is the measured signature of FM / AFM bilayers (Co/CoO, Fe/FeO, and metallic Mn-alloy pins such as FeMn, IrMn, PtMn).
- Blocking temperature \(T_B\) of the *pin*: \(H_\mathrm{ex}\to 0\) as \(T\to T_B^-\). \(T_B \le T_N\) of the AFM. \(T_B\) tracks AFM thickness and grain size and can lie well below the bulk Néel point; it is a measured collapse of the *shift*, not a second name for \(T_N\).
- Loop shift: the FM loop is centered at \(-H_\mathrm{ex}\) (opposite the cooling field in the usual convention). An increase of the FM coercivity often accompanies the shift; the two numbers are not the same artifact.
- Thickness: \(H_\mathrm{ex}\) falls as the FM layer is made thicker, empirically close to \(1/t_\mathrm{FM}\) over a working window. Too thin an AFM layer also kills the shift (the pin itself is under-provisioned).
- Training: the first loops after field-cooling need not coincide with later loops. That is a measured relaxation of the pin, not a separate effect in this filing.
- Holding the shifted remanent point costs zero continuous power. Energy is spent to field-cool (set the pin) and to traverse the shifted loop (write the FM).

**Data confidence:** High as a class — existence of \(H_\mathrm{ex}\), collapse at \(T_B \le T_N\), and the \(1/t_\mathrm{FM}\) trend are multiply reproduced. A given stack’s \(H_\mathrm{ex}\) and \(T_B\) are medium (interface, grain size, and set protocol).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Shifted-loop accounting: the FM hysteresis of [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) is recentered from \(H = 0\) to \(H = -H_\mathrm{ex}\). Switching thresholds sit near \(-H_\mathrm{ex}\pm H_c\), not at \(\pm H_c\).
- Meiklejohn–Bean interface form:

  \[
  H_\mathrm{ex} \approx \frac{J_\mathrm{ex}}{\mu_0 M_s t_\mathrm{FM}}
  \]

  \(J_\mathrm{ex}\) is an *effective* interface energy density fitted to the shift. It is not the bulk AFM exchange, and it is typically far smaller than a naive monolayer-moment estimate. The \(1/t_\mathrm{FM}\) factor is the part that tracks thickness data.
- Thermal envelope: \(H_\mathrm{ex}(T)\to 0\) at \(T_B\), with \(T_B \le T_N\) of the AFM pin ([antiferromagnetic-order](antiferromagnetic-order.md)).
- Setting protocol: a cooling field through \(T_B\) selects the pin direction. Without that field-cool (or an equivalent setting step) the shift is absent or averaged away.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** Two nested latches plus an interface:
  1. An AFM volume that can itself remain ordered and blocked (\(T < T_B\), thickness / grain above the pin’s own buffer).
  2. An FM film or particle thick enough to carry a readable moment, thin enough that the interface pin is not diluted below a usable \(H_\mathrm{ex}\).
  3. A shared interface. There is no exchange-bias loop in a separated AFM and FM of the same materials.

- **Clock rate / latency.** Setting the pin is a thermal write: the field-cool must pass through \(T_B\) on a laboratory cooling clock. Subsequent FM writes are ordinary hysteresis clocks (sweep + wall motion) on a loop whose center has already been offset. AFM exchange rates underneath the pin are fast compared with either of those.

- **Energy barriers or thresholds.** The AFM is a cancelled latch. At the interface a net pin remains and adds a unidirectional barrier on the FM. That barrier holds the *offset* at zero continuous power. The FM still has its own bidirectional anisotropy barrier. \(H_\mathrm{ex}\) is the field equivalent of the pin; \(H_c\) is still the half-width of the FM cycle.

- **Dominant failure modes.**
  - Thermal: \(T > T_B\) of the pinned layer \(\to H_\mathrm{ex}\to 0\) \(\to\) centered loop. The FM may still be ordered (\(T_C\) of the FM is a different cliff).
  - Spatial: AFM too thin or too finely grained \(\to\) pin unblocked; FM too thick \(\to H_\mathrm{ex}\) diluted as \(1/t_\mathrm{FM}\).
  - Field: a sufficiently large reverse field can drag or train the pin (the interface is not infinitely stiff). That is a rewrite of the second latch, not just of the FM.
  - Chemical / mechanical: oxidation, interdiffusion, or delamination destroys the interface buffer.

- **Emergent constant or stable output.** A stable offset \(-H_\mathrm{ex}\) of the FM loop, and a remanent FM state whose zero-field point is no longer symmetric, held at zero continuous power below \(T_B\).

### 4.6 Internal Consistency Notes

Two latches in series match the data: the AFM collapse at \(T_B\) removes the shift and leaves the FM loop; the FM collapse at its own \(T_C\) or \(H_c\) cycle is the inner write. Zero hold power on the shifted remanence is the same latch accounting as the parent magnet. The \(1/t_\mathrm{FM}\) trend is a buffer-dilution clause on the FM side.

The mapping is not closed on the interface. Fitted \(J_\mathrm{ex}\) is orders of magnitude below bulk exchange; roughness, uncompensated spins, and grain-level AFM domains are the named ingredients in the standard description and are not reduced here to a QSA buffer / barrier number. Why \(T_B\) so often lies well below bulk \(T_N\) is the same finite-size / grain problem and is not given a portable \(KV\) line. Training is recorded as a pin relaxation without a node-level clock. Those are gaps, not contradictions.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(T_B\), the loop shift, and the two-latch topology are solid, but \(H_\mathrm{ex}\) and \(T_B/T_N\) remain interface- and grain-level data without a closed specification.

## Related entries

- [antiferromagnetic-order](antiferromagnetic-order.md) — the cancelled latch that supplies the pin
- [ferromagnetic-hysteresis](ferromagnetic-hysteresis.md) — the FM loop that is shifted
- [permanent-magnet-latch](permanent-magnet-latch.md) — the inner FM remanent state
- [superparamagnetism](superparamagnetism.md) — thermal / volume unblocking of a magnetic latch; \(T_B\) of the pin is the analog
- [magnetic-domains](magnetic-domains.md) — FM and AFM domain structure at the interface
