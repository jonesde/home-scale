---
origin: logically-derived
not_an_effect_entry: true
updated: 2026-08-17
---

# Operating envelopes

The **inside** of each first-wave cliff: what is true while the machine is working. Inherited from [`design-spec-sheets.md`](design-spec-sheets.md) and downward `entails`. No new measurements. If this note disagrees with an effect file, the effect file wins.

Constraint reasoning still locates the machine from the erase row. This note only writes the complement so “normal operation” is not left implicit.

---

## collective-screening

| | |
|---|---|
| **Inside** | Connected metal / polarizable volume ≳ optical *δ* or RF skin; drive *ω* below *ω_p* (or the Ag interband-shifted edge); incident field present. Output is a re-radiated beam / confined AC current. Extra hold-power 0 W. |
| **Outside** | Thickness / percolation ≲ 5–10 nm, or *ω* above the plasma / interband edge. |

Nodes: `electron` as `population`; `photon` as `input`.

---

## anisotropy-latch

| | |
|---|---|
| **Inside** | Grain with *KV* above the observation-window escape line; *T < T_C*; lattice intact. Remanent *M* at 0 W. |
| **Outside** | *T > T_C*; *KV* too small (superparamagnetism); lattice shock. Write/erase is the *M*–*H* loop, not the hold. |

Nodes: `directional-moment` as `latch-cell`; `ion` as `matrix`.

---

## polar-latch

| | |
|---|---|
| **Inside** | Polar volume that stands depolarization; *T < T_C*; *E* = 0. Remanent *P* at 0 W. |
| **Outside** | *T > T_C*; *E > E_c*; volume too small. *E_c* / dead layer still mesoscale. |

Nodes: `directional-moment` as `latch-cell`; `ion` as `matrix`.

---

## gapped-condensate

| | |
|---|---|
| **Inside** | *T < T_c*; *H* below the relevant critical field; *I < I_c*; connected condensate on *ξ* / *λ* class lengths. *R* = 0; expulsion only below *H_c* / *H_c1*. Persistent current at 0 V. |
| **Outside** | *T_c*, *H_c* / *H_c2*, *I_c*. Mixed state can keep *R* = 0 after expulsion fails if vortices are pinned. |

Node: `electron` as `population`. The 2*e* increment is not a node.

---

## chargeless-superflow

| | |
|---|---|
| **Inside** | Connected ⁴He with *ρ_s* > 0; *T < T_λ*; *v < v_c*. Persistent circulation *h*/*m*₄ at 0 W. |
| **Outside** | *T > T_λ*; *v > v_c*; solidification. No London *λ*, no *χ* = −1. |

No first-wave node.

---

## energy-gate

| | |
|---|---|
| **Inside** | Input at or above the named gate (*φ*, *E_g*, *I*, *E_b*, 2*m_e c*², *B_d*, *E_c*, or a pyro / muon opener). One event is *N* = 1 (or one ν+A). The product leaves. |
| **Outside** | Under-threshold input (non-occurrence). Pair channel also closed in empty space. μCF also closed with no muon. Pyro-fusion closed with no Δ*T* or no D. CEνNS leaves the *N*² window when *qR* ≳ 1. |

Nodes: `electron` `single`; `photon` `input`; `positron` `product`; `nucleus` `recoil`; `muon` / `neutrino` `input`; `proton` / `neutron` `product`.

---

## oscillator-grid

| | |
|---|---|
| **Inside** | Ordered ion grid; drive on an allowed *ω*(**q**) below *ω_D*; *T* below *T_m*; *ℓ* finite for heat current. Long-wave *v_s* = √(*C*/*ρ*). |
| **Outside** | *ω > ω_D* (mode absent); *T → T_m*; yield / fracture; *ℓ* collapsed. |

Nodes: `ion` `matrix`; `phonon` `mode`.

---

## ensemble-average

| | |
|---|---|
| **Inside** | Enough independent contributors; observation slower than the exchange window. Stable *T*, *P* = *nkT*, Planck curve, *γT*, *χ* = *C*/*T*, Nyquist, Brownian *D*. |
| **Outside** | Too few contributors; observation inside the window; a latch or gap replaces the population. |

Nodes: `electron` `average`; `photon` `average`. No universal *N*.

---

## exchange-pin

| | |
|---|---|
| **Inside** | AFM + FM + interface; *T < T_B* of the pin. Loop shift held at 0 W. |
| **Outside** | *T > T_B* (*T_B* ≤ *T_N*). FM remanence can remain. |

Node: `directional-moment` as `latch-cell`.
