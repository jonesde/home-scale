# Taxonomy

Effects are filed by **what kind of machine behavior produces the macroscopic output**, specifically by the **dominant collapse** of that output. Conventional physics names stay on the entry titles and in the index so the catalog remains searchable. They are not the spine.

If later entries refuse to sit cleanly in these families, that is an internal-consistency finding. Record the mismatch on the entry; do not invent a seventh family to hide it until several effects share the same leftover collapse type.

---

## Assignment rule

1. Name the macroscopic effect and its **dominant collapse threshold**.
2. Put the file in the family whose collapse type matches that threshold.
3. Tag secondary constraints in frontmatter; do not duplicate the file.
4. If two collapse types are equally load-bearing, prefer the family that matches the **minimum hardware condition for the effect to exist at all** (buffer, gap, or barrier present), and list the other facet under `related`.

`family` is singular. There is no second primary family.

---

## Families

### 1. Collective field response

`family: collective-field-response`

Many charged nodes must occupy a minimum coherent volume and synchronize before a stable macroscopic electromagnetic output appears.

Typical collapse: **spatial under-provisioning** of the responding volume, or **loss of collective phase** (including drive frequency above the collective mode).

Examples: reflection, refraction / dielectric polarization, skin effect, plasma-frequency cutoff, surface plasmon resonance.

### 2. Latched order

`family: latched-order`

An energy barrier holds a directional or configurational state at **zero continuous power**. Energy is spent only to write or erase.

Typical collapse: **thermal over-barrier**, **volume too small to keep the barrier above kT** (superparamagnetic / superparaelectric limit), or **mechanical destruction of the latch matrix**.

Examples: permanent magnet, ferromagnetic hysteresis, ferroelectric remanence, superparamagnetism.

### 3. Gapped coherence

`family: gapped-coherence`

A protected collective mode with critical temperature, field, and/or current.

Typical collapse: **gap closure** or **coherence-length / critical-field / critical-current violation**.

Examples: superconductivity (zero resistance), Meissner effect, Josephson effect, superfluidity.

**Split rule.** Zero-resistance transport and Meissner field expulsion are related and separately filed. Their quantitative boundaries and failure envelopes are not the same artifact. Cross-link them.

### 4. Threshold conversion

`family: threshold-conversion`

A discrete energetic (or field) gate. Below threshold the conversion does not occur; above it, it does.

Typical collapse / non-occurrence: **under-threshold input**.

Examples: photoelectric effect, work function / thermionic emission, semiconductor absorption edge, pair production, dielectric breakdown.

### 5. Lattice modes

`family: lattice-modes`

The ion grid as coupled mechanical oscillators. Boundaries come from dispersion, group velocity, and the point at which the lattice can no longer carry the mode.

Typical collapse: **cutoff of the allowed mode**, **scattering that destroys the mean free path**, or **loss of crystalline order**.

Examples: phonon dispersion, speed of sound, Debye cutoff, melting, phonon thermal conductivity.

A lattice failure that only *erases some other latch* (for example shock-demagnetization) is tagged `mechanical-lattice` on that other entry. The lattice entry owns the grid; the latch entry owns the latch.

### 6. Ensemble averages

`family: ensemble-averages`

Stable macroscopic constants or spectra that exist only as the averaged output of a large synchronized population. The hardware scale here is statistical: below a minimum N the average is not a stable law.

Typical collapse: **too few independent contributors**, or **drive / observation faster than the averaging window**.

Examples: thermal equilibrium temperature, ideal-gas pressure, blackbody spectrum, Johnson–Nyquist noise.

---

## Constraint tags

These are cross-cuts, not families. Use only:

| Tag | Use when the load-bearing limit is… |
|---|---|
| `spatial-buffer` | a minimum length, thickness, grain size, or coherent volume |
| `clock-latency` | a response time, precession rate, plasma period, or frequency cutoff |
| `energy-barrier` | an activation or anisotropy barrier that protects a state |
| `mechanical-lattice` | crystalline order, strain, or shock as the failing resource |
| `field-threshold` | an applied E or B that gates or destroys the effect |
| `thermal` | kT, a Curie / Néel / critical temperature, or a blocking temperature |

---

## What this spine is for

Textbook domains (optics, magnetism, condensed matter) group effects by apparatus and historical field. QSA is testing whether distinct textbook effects share a machine class — buffer-starved collective response, barrier-latched memory, gapped condensate, and so on.

Other indices (by conventional domain, by medium, by confidence) can be added later as generated views. The Markdown files remain the source of truth. Cross-cutting queries live in the analysis layer ([`../analysis/`](../analysis/README.md), local `qs-analysis.db`). Do not treat the database as a second science wiki.

Constituents consumed by these families live in [`nodes/`](nodes/README.md). They are not a seventh family.
