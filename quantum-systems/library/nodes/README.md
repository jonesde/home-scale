# Node library

Constituents consumed by QSA machines. **Not** effect catalog rows. Do not add these slugs to [`../INDEX.md`](../INDEX.md).

A **node** is a microscopic constituent (elementary, composite, or quasiparticle). It is not a design and not a seventh family. Conventional particle names stay on the title.

Operating rules and the rule amendment live in the [top-level README](../../README.md) §5 and [AGENTS.md](../../AGENTS.md). This file is only the operating manual for `library/nodes/`.

---

## What a card is

One kebab-case file per constituent. Frontmatter feeds the `node` table. The body is a short identity card, **not** the locked 7-part effect template.

| `origin` | Use |
|---|---|
| `forced` | A library collapse already requires this constituent. Rebuild fails if it has no `implication_node` edge. |
| `cataloged` | Well-measured species, no library collapse yet. Cannot use `membership = forces`. |
| `predicted` | Theorized species with a named would-be observation. Cannot be evidence. |

Identity specs (mass, charge, spin, lifetime, PDG MC ID) are **taken** from a pinned edition. They are not extracted cliffs. If a card and an effect file disagree about a failure envelope, the **effect file wins**.

---

## Pinned sources (reference, do not vendor)

| Edition | What we take | Do not copy |
|---|---|---|
| [PDG 2026](https://pdg.lbl.gov/2026/html/computer_read.html) *Review of Particle Physics* ([mass_width_2026.txt](https://pdg.lbl.gov/2026/mcdata/mass_width_2026.txt), [API](https://pdg.lbl.gov/2026/api/index.html)) | `pdgid`, mass, charge, lifetime/width on admitted cards | Resonance zoo, error columns, SQLite dumps |
| PDG Monte Carlo Particle Numbering Scheme | Integer IDs (electron `11`, positron `-11`, photon `22`) | Unofficial codes for quasiparticles |
| [CODATA 2022](https://physics.nist.gov/constants) ([allascii.txt](https://physics.nist.gov/cuu/Constants/Table/allascii.txt)) | *m_e* and other constants already used in effect files | The full constants list |

When an edition rolls, update this pin and the handful of copied numbers. Rebuild stays stdlib-only: no `pip install particle`. NIST ASD is **not** imported; shell gates stay on the X-ray / ionization effect files.

Quasiparticles (`phonon`, `directional-moment`) and class nodes (`nucleus`, host `ion`) have `pdgid` NULL.

---

## Admission filter (`cataloged`)

A cataloged card is allowed only if at least one holds:

1. It is a parent or contrast of a forced node (proton / neutron as what `nucleus` is made of).
2. An existing effect file already names it as hardware.
3. A design would be under-specified without naming it (rare; not a back door).

That is comprehensive inside relevant scope, not every PDG line. Rebuild warns on a cataloged node with zero edges.

Do not add muon, tau, neutrinos, *W*, *Z*, Higgs, quarks, or a dark-sector species until a file names them or a predicted observation exists.

---

## File conventions

Copy [`_template.md`](_template.md). Adding, renaming, or deleting a card means updating [`INDEX.md`](INDEX.md) in the same change.

Body sections (locked for this grain):

1. Name
2. Taken specifications
3. Forced by
4. Consumed as
5. Open
6. Contrast
