---
id: muon-catalyzed-fusion
title: Muon-Catalyzed Fusion (Mass-Rescaled Nuclear Gate)
status: formal
family: threshold-conversion
constraints:
  - energy-barrier
  - clock-latency
  - spatial-buffer
confidence_data: high
confidence_mapping: high
related:
  - pair-production
  - ionization-threshold
  - photoelectric-threshold
updated: 2026-08-17
---

# Muon-Catalyzed Fusion (Mass-Rescaled Nuclear Gate)

### 4.1 Effect Name

Muon-catalyzed fusion (mass-rescaled nuclear gate)

### 4.2 Macroscopic Observation

A negative muon that stops in a hydrogen-isotope target (liquid or dense gas; no metal host required) forms a muonic molecule with two nuclei. Fusion products then appear — neutrons and helium from the d–t and d–d channels — at a rate set by how many muons stop and how many cycles each one completes. When the muon supply is removed, or after each muon decays or sticks to a helium nucleus, the fusion channel closes. The same target with no muons produces no such cycle. Defect inventory, cold work, and pulsed coils are not part of the apparatus.

### 4.3 Established Quantitative Boundaries

- Muon rest energy and lifetime (PDG 2026; Monte Carlo ID `13`):

  \[
  m_\mu c^2 = 105.658\,\mathrm{MeV},\qquad
  \frac{m_\mu}{m_e} \approx 206.8,\qquad
  \tau_\mu = 2.197\times 10^{-6}\,\mathrm{s}.
  \]

- The muonic Bohr radius is smaller than the electronic one by \(\sim m_\mu/m_e\). A dtμ or ddμ ion therefore holds the two nuclei close enough that fusion proceeds by tunneling on a timescale far below \(\tau_\mu\) once the molecule exists.
- d–t fusion energy release \(Q = 17.6\,\mathrm{MeV}\).
- Measured cycle yield in dense d–t: of order \(100\)–\(150\) fusions per stopped muon (Los Alamos / Jones class \(\sim 150\)). The hard ceiling is \(\alpha\)-sticking, not the nuclear \(Q\).
- Effective d–t sticking probability \(\omega_s\) in the \(0.5\)–\(0.6\,\%\) class. d–d sticking is much larger (\(\sim 10\,\%\) class), so the same machine yields fewer cycles in a deuterium-only target.
- p–p (and ordinary electronic hydrogen molecules) do not complete a useful fusion cycle on \(\tau_\mu\).
- Alvarez et al. (1956) saw the pd channel in a liquid-hydrogen bubble chamber. Later work used muon beams on cryogenic H/D/T targets. A metal lattice is not required and is not the gate.

**Data confidence:** High — \(m_\mu\), \(\tau_\mu\), the existence of the cycle, the isotope ordering (dt ≫ dd ≫ pp), and sticking as the yield limit are multiply reproduced. Any one target’s exact fusions-per-muon is medium (density, temperature, mix).

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Mass-rescaled Bohr radius (order-of-magnitude locator, not a derived QSA node count):

  \[
  a_\mu \sim \frac{m_e}{m_\mu}\,a_0 \approx \frac{a_0}{207}.
  \]

- Mean cycles per muon, limited by sticking and by decay:

  \[
  \langle n\rangle \lesssim \min\!\left(\frac{1}{\omega_s},\; \lambda_c\tau_\mu\right)
  \]

  with \(\lambda_c\) the cycle rate in the target. Sticking, not \(Q\), is the measured erase of the catalyst.
- Muon decay is the hard clock. After \(\tau_\mu\) the node is gone; there is no remnant catalysis at zero muon population.

These relations describe the observed cycle. They do not derive \(m_\mu\) and they do not compute a net-energy factory balance.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** One muon plus two hydrogen-isotope nuclei (a dtμ or ddμ ion) is the hardware for one catalysis cycle. Target density and volume are **capacity**: they raise \(\lambda_c\) and the number of stopped muons. They do not open the gate in a muon-free cell. There is no 10–20 nm metal film and no defect-cell \(KV\).

- **Clock rate / latency.** \(\tau_\mu = 2.197\,\mu\mathrm{s}\) is the hard stop. Molecular formation and fusion inside a formed dtμ ion sit far below that clock. Observation after the muon population is gone is not this effect.

- **Energy barriers or thresholds.** Not a latch. The muon mass rescales the well so the nuclear conversion occurs. The product leaves; the muon is recycled until it decays or sticks. Holding “the fused state” is not a 0 W memory.

- **Dominant failure modes.**
  - Missing node: no muon → the channel is closed at every lattice strain and every H/M. That is the collapse of this effect.
  - Clock: decay at \(\tau_\mu\) removes the catalyst.
  - Sticking: \(\omega_s\) erases the muon onto helium and caps \(\langle n\rangle\).
  - Isotope: pp (and electronic molecules) stay closed on this clock.
  - Supply: a cosmic-ray muon flux does not become this cycle just because a hydride is present; the macroscopic yield tracks stopped-muon inventory.

- **Emergent constant or stable output.** A fusion-product yield per stopped muon, of order \(10^2\) for dense d–t, set by supply × cycle × \((1-\omega_s)\), only while muons are present.

### 4.6 Internal Consistency Notes

The mapping closes on the same shape as [pair production](pair-production.md): a named extra node is mandatory hardware, and its absence shuts the channel even when energy is “enough” in some other variable (here, lattice compression or occupancy). Pair production’s extra node is a recoil nucleus; this entry’s extra node is the muon.

It is not a latch. Zero muons after the beam is dark means zero catalysis. That is the opposite of a remnant interstitial cell that can linger at 0 W.

It is not the interstitial object mapped in the EM-LENR application. That record’s collapses are blocking, bake-out, and defect inventory. This record’s collapses are missing muon, decay, and sticking. Equating them is a mapping error.

\(m_\mu\) and \(\tau_\mu\) are taken from PDG, the same honesty as taking \(m_e\) on pair production. Net electrical cost per muon (accelerator / factory) is a different bookkeeping problem and is not used to locate the gate.

### 4.7 Overall Confidence in the QSA Mapping

**High** — the muon requirement, the lifetime clock, sticking as the yield cap, and the isotope ordering are sharp measured boundaries and translate directly into buffer, clock, and failure-envelope specifications; the open item is factory net-energy, not the gate.

## Related entries

- [pair-production](pair-production.md) — another conversion that stays closed without a named extra node
- [ionization-threshold](ionization-threshold.md) — electronic unbinding of H; not this nuclear cycle
- [photoelectric-threshold](photoelectric-threshold.md) — *N* = 1 electron gate; different particle, different conversion
