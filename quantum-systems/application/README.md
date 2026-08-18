# Applications

**Not operating procedures.** Analysis and design notes only. Unqualified readers should stop at [SAFETY.md](../SAFETY.md). Hydrogen, metal powder, pressure, pulsed current, high voltage, accelerators, and reactor halls are industrial hazards even at the small sizes named below. Envelope (home-scale vs industrial-until-mitigated) is a label on the file, not a reason the mapping is absent.

Device-centered uses of the QSA library. Concepts are allowed to repeat; the singular science source is [`../library/`](../library/INDEX.md). Derived spec sheets: [`../library/derived/`](../library/derived/README.md).

**Manufacturing hook (non-nuclear).** [EM-CSAM-Pitch](EM-CSAM-Pitch.md) is an opportunity brief for contacts and for people who might run a first splat series: structure plus function from the EM deposition head (coats, insulating magnets, linear tracks in a frame), then a labeled nano/fab fantasy. Nuclear, accelerator, and reactor-hall applications are a different folder job and are out of that file.

**Strongest of the new set** (QSA-distinct stacks, not used products):

1. [switchable-hydride-mirror](switchable-hydride-mirror.md) — screening × interstitial occupancy; closest to later home-scale packaging.
2. [polar-beam-gate](polar-beam-gate.md) — polar engine × beam-target D–D; not a DT tube.
3. [muon-hydrogen-gate](muon-hydrogen-gate.md) — extra-node H-isotope gate; bounds EM-LENR from the other side.

---

## Calibration and live problems

| File | Device | What it applies | Envelope |
|---|---|---|---|
| [thin-film-optics.md](thin-film-optics.md) | Mirrors, TCO, SPR chips | `collective-screening` (calibration case) | Lab coating |
| [bonded-magnets.md](bonded-magnets.md) | Bonded NdFeB, tape, ferrofluid | `anisotropy-latch` (handbook calibration) | Lab / magnet shop |
| [hydrogen-embrittlement.md](hydrogen-embrittlement.md) | Charged high-strength metal parts | Interstitial latch, no nuclear layer | Industrial H service |
| [hydride-storage.md](hydride-storage.md) | Metal-hydride bed / tank | Capacity vs pinned H | Industrial H service |
| [EM-LENR.md](EM-LENR.md) | Contained pulsed-coil cell (Steven E. Jones) | Defect-pinned interstitial latch; energy-gate last | Lab / industrial; nuclear search last |
| [EM-CSAM.md](EM-CSAM.md) | Micro-railgun deposition head + driver | Impact bonding, skin, breakdown, magnetostriction | Shop + same driver as experiment |

EM-LENR waits on Steven’s review for the nuclear/configuration claim. Isolate the interstitial latch first.

---

## New device concepts (not used products)

Used instruments under their usual names (SI ohm, FeRAM, SPR immunoassay, SET, alkali BEC kit, DT tube, spin-valve head) are excluded. These files are the QSA stack, not those products.

| File | Device concept | Machines | Envelope | Strength |
|---|---|---|---|---|
| [switchable-hydride-mirror.md](switchable-hydride-mirror.md) | H occupancy turns the screening buffer on/off | `collective-screening` × interstitial H | Lab / industrial film; nearest later home-scale | **Strongest combination** |
| [polar-beam-gate.md](polar-beam-gate.md) | Polar Δ*T* writes HV; ordinary D–D | `polar-latch` × `energy-gate` | Institutional until interlocked | **Strongest stacked gate** |
| [muon-hydrogen-gate.md](muon-hydrogen-gate.md) | Extra-node H-isotope cycle | `energy-gate` + muon | Accelerator only | **Strongest extra-node spec** |
| [exchange-pin-thermal-history.md](exchange-pin-thermal-history.md) | *H*<sub>ex</sub> trip through *T<sub>B</sub>*, *M<sub>r</sub>* can remain | Draft `exchange-pin` | Thin-film lab; sealed coupon later | Split that justifies the ninth design |
| [percolation-dual-switch.md](percolation-dual-switch.md) | One starve kills *R* and conducting-plate attraction | `collective-screening` + Casimir contrast | MEMS / thin-film lab | Fourth artifact of `coupled-screening-failure` |
| [coherence-window-recoil.md](coherence-window-recoil.md) | CEνNS vs IBD on the same flux | `energy-gate` as CEνNS | Reactor / spallation | Coherence window, not 1.8 MeV |
| [edge-orientation-inhibit.md](edge-orientation-inhibit.md) | In-plane *B* kills the plateau; not the SI ohm | Draft `edge-channel`; QPC contrast | Cryogenic high-*B* lab | Inhibit, not the resistance quantum |
| [depolarization-fuse.md](depolarization-fuse.md) | *P<sub>r</sub>* dies thinner than the depolarization envelope | `polar-latch` failure side | Ceramic / thin-film lab; no D | Electrical twin of *KV* collapse |

Do not scale inventory, muon current, Δ*T*, or pulse energy in search of a nuclear signature. Do not add a muon source or a pyroelectric crystal to the coil cell to “open” a gate.
