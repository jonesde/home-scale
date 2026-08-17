---
id: electron-heat-capacity
title: Electron Heat Capacity (Fermi-Surface Average)
status: formal
family: ensemble-averages
constraints:
  - thermal
confidence_data: high
confidence_mapping: medium
related:
  - thermal-equilibrium-temperature
  - superconductivity
  - debye-cutoff
  - semiconductor-gap-absorption
  - johnson-nyquist-noise
updated: 2026-08-17
---

# Electron Heat Capacity (Fermi-Surface Average)

### 4.1 Effect Name

Electron heat capacity (Fermi-surface average)

### 4.2 Macroscopic Observation

The heat capacity of a normal metal at low temperature is linear in \(T\): after the phonon \(T^{3}\) piece is subtracted, a term \(\gamma T\) remains. The coefficient \(\gamma\) is a material constant of order \(1\,\mathrm{mJ\,mol^{-1}\,K^{-2}}\) for simple metals. At room temperature that electronic piece is a small correction on the much larger lattice heat capacity; it becomes the leading term only once the lattice contribution has frozen out. In a superconductor the linear term disappears below \(T_c\) and is replaced by an exponentially small remnant. Insulators and undoped semiconductors do not show a metallic \(\gamma T\) at all.

### 4.3 Established Quantitative Boundaries

- Observed low-temperature envelope in a normal metal:

  \[
  C = \gamma T + A T^{3}
  \]

  The linear piece is electronic; the cubic piece is the phonon contribution bounded by the [Debye cutoff](debye-cutoff.md).
- \(\gamma\) sits in a class of order \(1\,\mathrm{mJ\,mol^{-1}\,K^{-2}}\) for many simple metals and is material-specific (Cu \(\approx 0.70\,\mathrm{mJ\,mol^{-1}\,K^{-2}}\); Al \(\approx 1.35\,\mathrm{mJ\,mol^{-1}\,K^{-2}}\)). Heavy-fermion metals can be two to three orders of magnitude larger; that is the same envelope with a renormalized density of states, not a different law.
- The electronic term is a Fermi-surface average. Only a slice of width \(\sim kT\) about \(E_F\) can take up energy. The corresponding Fermi temperatures in ordinary metals are \(T_F\sim 10^{4}\)–\(10^{5}\,\mathrm{K}\) (Cu \(T_F\approx 8.2\times 10^{4}\,\mathrm{K}\)), so the participating fraction at laboratory \(T\) is \(T/T_F\ll 1\).
- As \(T\to 0\) in the normal state, \(\gamma T\) falls linearly through any fixed instrument floor. There is no sharp electronic cliff; the term vanishes into the noise.
- Below a superconducting gap the linear term is killed and \(C_e\) falls much faster than linear (BCS envelope \(\sim\exp(-\Delta/kT)\)). That collapse belongs with [superconductivity](superconductivity.md); it is recorded here as the gapped-spectrum failure of this average.
- A filled-gap insulator has no Fermi surface and no metallic \(\gamma T\).

**Data confidence:** High — \(\gamma\) values, the \(C=\gamma T+AT^{3}\) decomposition, Fermi temperatures, and the loss of the linear term in superconductors are handbook calorimetry. The precise \(\gamma\) of any one alloy is medium (sample-dependent); the class and the collapse types are not.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Sommerfeld expansion for a Fermi gas:

  \[
  C_e = \gamma T,\qquad \gamma = \frac{\pi^{2}}{3}D(E_F)\,k^{2}
  \]

  with \(D(E_F)\) the density of states at the Fermi energy. Equivalently, in free-electron form, \(\gamma \propto Nk/T_F\).
- Phonon companion at low \(T\): \(C_{\mathrm{ph}}=A T^{3}\), with \(A\) set by the Debye temperature. The two terms are separated experimentally by a plot of \(C/T\) versus \(T^{2}\).
- Gapped superconducting envelope (BCS, recorded as a fit to the collapse of the linear term):

  \[
  C_e(T\ll T_c)\propto e^{-\Delta/kT}
  \]

  plus a jump in \(C\) at \(T_c\). This entry does not own the gap; it owns the fact that a gap removes \(\gamma T\).

\(\gamma\) and \(T_F\) are material parameters taken from measurement (or from a band calculation that is itself fitted to measurement). They are not derived here from a primitive node count.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** The hardware is the Fermi-surface population — the electrons that lie within \(\sim kT\) of \(E_F\) and can change occupation when \(T\) changes. That is a *T-dependent* statistical buffer, of order \((T/T_F)N\), not a fixed node count. There is no universal \(N\) at which “electronic heat capacity begins.” A metal with no Fermi surface (gapped, insulating) has no such population at any \(N\). A normal metal has one at every \(T>0\), with a participating count that shrinks linearly toward zero.

- **Clock rate / latency.** No separate collective clock beyond the electronic and electron–phonon equilibration times of the host (typically picoseconds in ordinary metals). Calorimetry sits far above that window. The relevant energy scale is \(kT\) against \(E_F\) (or against a gap \(\Delta\), when one is present).

- **Energy barriers or thresholds.** The operating metallic envelope has no gap at \(E_F\). Opening a superconducting gap, or sitting in a semiconductor/insulator gap, removes the contributing slice. Those gaps are owned by [superconductivity](superconductivity.md) and [semiconductor gap absorption](semiconductor-gap-absorption.md); they appear here only as the threshold that kills \(\gamma T\).

- **Dominant failure modes.**
  - Thermal: \(T\to 0\) in the normal state → \(\gamma T\) falls into the calorimeter noise. The average is still defined; the output is no longer a usable reading.
  - Gapped spectrum: \(T<T_c\) in a superconductor, or a band gap at \(E_F\) → the linear term is absent. The contributing population has been removed, not merely cooled.
  - Lattice dominance: at higher \(T\) the \(AT^{3}\) (and then Dulong–Petit) phonon terms bury \(\gamma T\). That is a contrast-of-scale problem for the measurement, not a collapse of the electronic average.

- **Emergent constant or stable output.** A heat capacity linear in \(T\), with a material coefficient \(\gamma\), as the averaged energy uptake of the Fermi-surface slice.

### 4.6 Internal Consistency Notes

The participating-fraction picture (\(T/T_F\)) is internally consistent with the rest of the family: the macro output is an average over a thermal window, and shrinking that window shrinks the output. The superconducting and insulating collapses are consistent as well — they are replacements of the contributing population, the same class of failure already listed on the [temperature](thermal-equilibrium-temperature.md) entry.

The mapping does not compute \(\gamma\) from a node rule. QSA *takes* the measured \(\gamma\) (or \(D(E_F)\), or \(T_F\)) as the material specification. Heavy-fermion enhancements show that \(\gamma\) can move by orders of magnitude without changing the *form* \(C_e=\gamma T\); that is a renormalization of the same average, and it is recorded as such rather than as a new effect.

A gap that is incomplete (vanishing along directions on the Fermi surface, or pair-breaking) leaves a residual linear term. That is a known experimental complication and a reminder that “gapped” is a spectrum statement, not a synonym for \(T<T_c\). The superconductivity entry owns the details.

[Johnson–Nyquist noise](johnson-nyquist-noise.md) is another electrical readout of a thermal electronic population in a metal. It does not require a Fermi-surface linear specific heat to exist (a resistor still makes \(4kTR\Delta f\)), so the two entries share a bath but not a buffer number.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — \(\gamma T\), \(T_F\), and the gapped-spectrum collapse are well measured and translate into a \(T\)-dependent Fermi-surface buffer; the mapping does not derive \(\gamma\) and correctly refuses a single node-count cliff.

## Related entries

- [Thermal equilibrium temperature](thermal-equilibrium-temperature.md) — the bath average of which this is one electronic readout
- [Superconductivity](superconductivity.md) — gap that removes the linear term
- [Debye cutoff](debye-cutoff.md) — phonon \(T^{3}\) companion and the mode ceiling of the lattice piece
- [Semiconductor gap absorption](semiconductor-gap-absorption.md) — no Fermi surface, no metallic \(\gamma T\)
- [Johnson–Nyquist noise](johnson-nyquist-noise.md) — electrical fluctuation readout of a thermal electronic population
