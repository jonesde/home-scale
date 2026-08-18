---
origin: logically-derived
not_an_effect_entry: true
updated: 2026-08-17
---

# Node types (join view)

Which first-wave machines consume which constituents. **Not** the zoo catalog — that is [`../nodes/INDEX.md`](../nodes/INDEX.md). Numbers and identity specs live on the node cards. If this note disagrees with a card or an effect file, those win.

Derived from `design_node` ⋈ `node` and `implication_node`.

---

## Forced set

| Node | kind | `pdgid` | Designs (role) | Forcing collapse (examples) |
|---|---|---|---|---|
| `electron` | elementary | 11 | screening `population`; energy-gate `single`; ensemble `average`; gapped-condensate `population`; edge-channel `edge` | starve / *ω > ω_p*; *N* = 1; Fermi slice; QHE 2DEG |
| `photon` | elementary | 22 | energy-gate `input`; screening `input`; ensemble `average` | under-threshold gate; pair hardware; Planck curve |
| `muon` | elementary | 13 | energy-gate `input` | no muon / *τ_μ* / sticking |
| `proton` | elementary | 2212 | energy-gate `product` | deuteron photodisintegration |
| `neutron` | elementary | 2112 | energy-gate `product` (no design for the UCN well) | photodisintegration; gravity well; CEνNS |
| `neutrino` | elementary | 12 | energy-gate `input` | CEνNS |
| `positron` | elementary | −11 | energy-gate `product` | 511 keV line |
| `phonon` | quasiparticle | — | oscillator-grid `mode` | *ω_D*; *ℓ*; melt of the host grid |
| `ion` | composite | — | oscillator-grid `matrix`; both latches `matrix` | 3*N* modes; *T_m* |
| `nucleus` | composite | — | energy-gate `recoil` | no partner ⇒ pair channel closed |
| `directional-moment` | quasiparticle | — | anisotropy / polar / exchange-pin `latch-cell` | *KV* / polar well vs unlocked Curie |

`chargeless-superflow` has no first-wave node. ⁴He is not `electron` and is not yet a separate card.

---

## Roles that can hold a written state

Only `latch-cell` (and the pinned condensate, which is a design not a node) hold a written direction at 0 W. `input`, `average`, `mode`, and `product` do not. Empty space is under-provisioned (`nucleus` recoil).

---

## Leftover

`quantum-hall-effect:hardware_scale:2deg` **forces** `electron`. Draft `edge-channel` now consumes `role = edge`. That names the leftover; it does not derive *R_K*.

---

## Not in this join

Cooper pair (`fluxoid-increment-2e` stays a closure). Free quark. Tau, neutrino, *W*, *Z*, Higgs. Predicted dark-sector species. Proton / neutron wait on the cataloged admission filter as parents of `nucleus`.
