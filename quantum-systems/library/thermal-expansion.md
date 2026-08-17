---
id: thermal-expansion
title: Thermal Expansion (Anharmonic Length Change)
status: formal
family: lattice-modes
constraints:
  - mechanical-lattice
  - thermal
confidence_data: high
confidence_mapping: medium
related:
  - phonon-dispersion
  - debye-cutoff
  - elasticity
  - melting
  - thermal-conductivity-phonon
  - magnetostriction
  - speed-of-sound
  - thermal-equilibrium-temperature
updated: 2026-08-17
---

# Thermal Expansion (Anharmonic Length Change)

### 4.1 Effect Name

Thermal expansion (anharmonic length change)

### 4.2 Macroscopic Observation

A metal rod lengthens when heated and shortens when cooled, reversibly, well below melting. The fractional change per kelvin is small. Invar (Fe–Ni near the 36 wt% Ni composition) is the everyday exception: its length is nearly independent of temperature around room temperature. A purely harmonic spring lattice would not do this — its mean bond length is independent of amplitude — yet every real crystal’s wells are anharmonic enough to produce a measurable \(\alpha\), except where a second channel cancels it.

### 4.3 Established Quantitative Boundaries

- Linear expansivity \(\alpha = (1/L)(\partial L/\partial T)\). Metals as a class: \(\alpha \sim 10^{-6}\)–\(10^{-5}\,\mathrm{K^{-1}}\) near room temperature (handbook examples in that window: Al \(\sim 2\times 10^{-5}\,\mathrm{K^{-1}}\), Fe \(\sim 1\times 10^{-5}\,\mathrm{K^{-1}}\)).
- Invar: \(\alpha\) near zero around room temperature, not because the lattice has become harmonic, but because a magnetic / volume-magnetostriction channel cancels the ordinary anharmonic term (`magnetostriction`).
- Harmonic limit: if the restoring wells are purely quadratic, \(\langle x\rangle\) is independent of \(T\) and \(\alpha = 0\). Observed expansion is therefore a statement that the wells are anharmonic.
- Low temperature: \(\alpha\to 0\) as \(T\to 0\), tracking the vanishing of the lattice heat capacity (`debye-cutoff`).
- High temperature: \(\alpha\) continues until the grid fails (`melting`). There is no single \(\alpha\)-defined collapse temperature analogous to \(T_m\) or \(T_C\).
- Grüneisen connection (descriptive): a number \(\gamma\) of order one for many solids ties \(\alpha\) to the bulk modulus and to \(C_V\). \(\gamma\to 0\) is the harmonic-limit statement in that language.

**Data confidence:** High — metal \(\alpha\) in the \(10^{-6}\)–\(10^{-5}\,\mathrm{K^{-1}}\) class, Invar’s near-zero window, \(\alpha\to 0\) as \(T\to 0\), and the harmonic-lattice theorem are standard. A particular alloy’s \(\alpha(T)\) curve is medium.

### 4.4 Standard Mathematical Description

Recorded as descriptive relations, not as axioms.

- Definition:

  \[
  \alpha = \frac{1}{L}\left(\frac{\partial L}{\partial T}\right)_P, \qquad
  \alpha_V = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_P \approx 3\alpha
  \]

  for an isotropic solid.

- Grüneisen (descriptive identity used in the literature):

  \[
  \gamma = \frac{3\alpha B}{C_V\rho} = -\frac{d\ln\omega}{d\ln V}
  \]

  The second form says \(\gamma\) is the volume sensitivity of the lattice clocks (`phonon-dispersion`). A harmonic spectrum has \(\gamma = 0\) and therefore \(\alpha = 0\).

- Quasi-harmonic statement: the measured \(\omega(q)\) shifts with volume; occupying those modes at finite \(T\) then shifts the equilibrium volume. This organizes data. It does not supply a single hardware number for “how anharmonic” a given well is.

No equation in this entry predicts Invar’s cancellation from the Fe–Ni composition. That cancellation is data, read as two channels summing to near zero.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume.** A mechanically coupled lattice whose wells are not purely quadratic, large enough for a macroscopic length to be defined. The harmonic grid that already produces `speed-of-sound`, `elasticity`, and `debye-cutoff` is *not* sufficient: expansion is the anharmonic correction to that same hardware. Invar adds a magnetic volume channel on top of the lattice term.

- **Clock rate / latency.** There is no separate expansion clock. The lattice clocks are the phonon spectrum; \(\alpha(T)\) is the thermal occupation of those modes acting through \(\gamma\). The laboratory length change follows the thermal equilibration time of the specimen (`thermal-equilibrium-temperature`), not an atomic period.

- **Energy barriers or thresholds.** No latched barrier and no single threshold number. The operating condition is \(\gamma \neq 0\) (anharmonic wells) plus a finite \(T\). The stated collapse is the harmonic limit \(\gamma\to 0\), which is a condition on the wells rather than a measured \(T\) or \(E\).

- **Dominant failure modes.**
  - Anharmonicity: \(\gamma \to 0\) (purely harmonic springs) → \(\alpha = 0\). This is the taxonomy collapse. It is a limiting condition, not a laboratory switch one flips on a given metal.
  - Thermal, low: \(T\to 0\) → \(C_V\to 0\) → \(\alpha\to 0\) even if \(\gamma\) is finite.
  - Thermal / mechanical, high: melting → the solid’s \(\alpha\) is no longer the spec.
  - Compensation: a second channel (Invar volume magnetostriction) cancels the lattice term → \(\alpha \approx 0\) without harmonic wells. That is not the harmonic-limit collapse.

- **Emergent constant or stable output.** A small, material-typical \(\alpha(T)\) (metals \(10^{-6}\)–\(10^{-5}\,\mathrm{K^{-1}}\) class) as the averaged length change of an anharmonic, thermally occupied grid.

### 4.6 Internal Consistency Notes

It is internally consistent that the *harmonic* machine of `elasticity` / `speed-of-sound` / `debye-cutoff` produces moduli, a long-wave slope, and a finite mode count, and still produces \(\alpha = 0\). Expansion is not a fourth reading of the same harmonic springs; it is the leading correction. Umklapp in `thermal-conductivity-phonon` draws on the same anharmonicity, so the two entries should not assign contradictory \(\gamma\).

The mapping is medium because anharmonicity is the stated condition and not a single hardware number. There is no measured \(\gamma_c\) at which expansion “turns on.” Invar shows that \(\alpha\approx 0\) can also be a cancellation, which must not be misread as \(\gamma = 0\).

QSA does not derive the \(10^{-6}\)–\(10^{-5}\,\mathrm{K^{-1}}\) class from node-well shapes. It takes that class as data and names the resource (anharmonicity) whose removal would kill the effect.

### 4.7 Overall Confidence in the QSA Mapping

**Medium** — the harmonic-lattice theorem, the metal \(\alpha\) class, and the Invar contrast correctly identify anharmonicity as the missing resource, but that resource is not pinned to one measured hardware number the way \(\omega_p\) or \(T_m\) is.

## Related entries

- [phonon-dispersion](phonon-dispersion.md) — \(\omega(q)\) whose volume shift is \(\gamma\)
- [debye-cutoff](debye-cutoff.md) — \(C_V(T)\) that \(\alpha\) tracks at low \(T\)
- [elasticity](elasticity.md) — harmonic \(C\) that expansion corrects
- [melting](melting.md) — the high-\(T\) end of the same wells
- [thermal-conductivity-phonon](thermal-conductivity-phonon.md) — umklapp from the same anharmonicity
- [magnetostriction](magnetostriction.md) — Invar’s cancelling volume channel
- [speed-of-sound](speed-of-sound.md) — long-wave clocks that shift with volume
- [thermal-equilibrium-temperature](thermal-equilibrium-temperature.md) — the ensemble \(T\) that occupies the modes
