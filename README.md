# Home-Scale Democratized Production

A jig is a dance, a tool, and a secret. Life is a jig with a jig, and the jig is up. The jig we dance with is no less than our bodies and brains that build our intelligence and minds. The jig is up because we are beginning to understand automation and the emergent intelligent properties of neural networks — and because we can start to name, in ordinary handbook terms, what a piece of metal or a film will and will not do. The purpose of technology, and the purpose of life, is to further the goal of gaining intelligence and building our minds. Technology gives us the time we need, free of material concerns, to learn and grow. Technology also gives us a means and a process for learning and growing as we discover and improve it. This project is about collaborating to enable learning and growing, accessible to all intelligences.

This repo is one umbrella for three kinds of jig: **machines** you might actually copy (a small electromagnetic cold-spray head, a gantry it could ride), a **catalog of constraints** on what the material will do (Quantum Systems Analysis — utility and consistency, not a new physics church), and **notes on intelligence** (how we might think about the other dancer). Home-scale production only works if the machine is simple enough to share *and* the failure envelopes are named. The railgun does not prove the catalog. The catalog does not exist to sell the railgun. They live together because both are about making the dance copyable.

License: [CC0](LICENSE). Concepts and designs here are original thoughts and have **not** been patent-researched. That warning is sharpest for the micro-railgun work; see [EM-CSAM](#electromagnetic-cold-spray-em-csam).

---

## What's here

| Folder | What it is |
|---|---|
| [`em-csam/`](em-csam/README.md) | Hardware notes: micro-railgun deposition head, driver, powder / carrier / rails |
| [`quantum-systems/`](quantum-systems/README.md) | QSA effect library, analysis layer, and device applications (including the current EM-CSAM reading and pitch) |
| [`printer/`](printer/PrinterRequirementsDesigns.md) | Home-scale multi-head printer / gantry requirements |
| [`ai/`](ai/EzekielAGI.md) | Working notes on intelligence (not a product spec) |
| [`whitepaper/`](whitepaper/DemocratizedAccessToTechnologyWhitepaper.md) | 2023 argument for open, automated, home-scale production |

---

## Start here

| If you want… | Open first |
|---|---|
| What the head is for (coats, insulating magnets, tracks in a frame, labeled nano fantasy) | [`quantum-systems/application/EM-CSAM-Pitch.md`](quantum-systems/application/EM-CSAM-Pitch.md) |
| Isolation / campaigns / how the pulse writes those states | [`quantum-systems/application/EM-CSAM.md`](quantum-systems/application/EM-CSAM.md) |
| Barrel, driver, powder / carrier / rails (hardware) | [`em-csam/README.md`](em-csam/README.md) |
| The effect catalog (handbook names, collapse cliffs) | [`quantum-systems/library/INDEX.md`](quantum-systems/library/INDEX.md) |
| How to read the catalog | [`quantum-systems/README.md`](quantum-systems/README.md) · [`quantum-systems/SAFETY.md`](quantum-systems/SAFETY.md) |
| Printer / gantry requirements | [`printer/PrinterRequirementsDesigns.md`](printer/PrinterRequirementsDesigns.md) |
| AI / “wheels” notes | [`ai/EzekielAGI.md`](ai/EzekielAGI.md) |
| The 2023 access-to-technology argument | [`whitepaper/DemocratizedAccessToTechnologyWhitepaper.md`](whitepaper/DemocratizedAccessToTechnologyWhitepaper.md) |

---

## Electromagnetic cold spray (EM-CSAM)

A short-barrel **non-plasma** micro-railgun that throws a metered metal-powder armature (usually in a carrier) at a substrate. The goal is cold-spray class bonding — yield and oxide rupture, not a vapor armature — plus using the same pulse as a write: skin, strain, optional magnetic alignment, rails as an alloying source if you choose them that way.

The designs have **not** been patent-researched. From some brief looking, non-plasma micro-railguns are rare, and using an *array* of them for additive manufacturing is something I have yet to find a close cousin of. It would be really cool to find one (unless it is patented…).

The barrel is meant to be simple and cheap, or — if you need an exotic output — consumed as part of the deposit. Frame, feeder, and driver are reusable. You cannot do anything you want; only some powder / carrier / rail combinations are viable. It just happens that some useful outputs look easier this way than the alternatives, including alloys mixed on the fly.

**Read, in this order if you are new:**

1. [`quantum-systems/application/EM-CSAM-Pitch.md`](quantum-systems/application/EM-CSAM-Pitch.md) — what those states are *for* (non-nuclear). Not a protocol.
2. [`quantum-systems/application/EM-CSAM.md`](quantum-systems/application/EM-CSAM.md) — QSA reading of the same head: campaigns, knobs, falsifiers. Incorporates the later review. Not a protocol.
3. [`em-csam/README.md`](em-csam/README.md) — hardware, combinations, driver path.

Older concept math and board notes stay under [`em-csam/`](em-csam/). Prefer the two `quantum-systems/application/` files when they disagree with an early sketch.

Hydrogen-rich carriers on steel or titanium can charge a part that cracks later. Pulsed current and powder are ordinary industrial hazards. Details: [`quantum-systems/SAFETY.md`](quantum-systems/SAFETY.md).

---

## Quantum systems (QSA)

[Quantum Systems Analysis](quantum-systems/README.md) tests a finite-state-machine *reading* of quantum and condensed-matter effects. Macroscopic “laws” are treated as the averaged, synchronized output of constrained microscopic machines. The method reverse-engineers specs from **experimental collapse thresholds**: what the system cannot do, and the scale at which the output fails.

Evaluation is only **utility** (does the mapping produce a usable buffer / clock / barrier / failure envelope?) and **internal consistency**. No agency, purpose, or programmer language. These are theories and design notes, **not tested protocols**. Unqualified readers: stop at [`quantum-systems/SAFETY.md`](quantum-systems/SAFETY.md).

The science source of truth is the [effect library](quantum-systems/library/INDEX.md) (handbook names in the title so the catalog stays searchable). [Applications](quantum-systems/application/README.md) are device-centered readings of that library. Nuclear, accelerator, and reactor-hall applications are a **different job** from the manufacturing pitch; if you follow those links, start at SAFETY.

Further into the catalog, if you already know what you want:

- Thin-film optics / percolation / SPR — [`application/thin-film-optics.md`](quantum-systems/application/thin-film-optics.md)
- Bonded magnets, tape, ferrofluid — [`application/bonded-magnets.md`](quantum-systems/application/bonded-magnets.md)
- Hydrogen-switchable metal/window film — [`application/switchable-hydride-mirror.md`](quantum-systems/application/switchable-hydride-mirror.md)
- Charged steel / Ti as a process **warning** — [`application/hydrogen-embrittlement.md`](quantum-systems/application/hydrogen-embrittlement.md)
- Hydride tank capacity vs pinned residual — [`application/hydride-storage.md`](quantum-systems/application/hydride-storage.md)
- How to browse families and cliffs — [`library/INDEX.md`](quantum-systems/library/INDEX.md) · [`library/TAXONOMY.md`](quantum-systems/library/TAXONOMY.md)

---

## Printer

Notes toward a home-scale, multi-material, multi-head gantry (tabletop to garage). Long-term: independently sourceable. Near-term: COTS and other open machines (Voron-class) are allowed. The EM-CSAM head is one possible tool on that gantry, not the only one.

Open: [`printer/PrinterRequirementsDesigns.md`](printer/PrinterRequirementsDesigns.md).

---

## AI notes

Working notes on intelligence as a structure we are still learning to describe — not a product spec and not a claim that a biblical vision is a GPU.

Open: [`ai/EzekielAGI.md`](ai/EzekielAGI.md) · [`ai/MemoryWheels.md`](ai/MemoryWheels.md).

An initial, yet unforgettable, implementation of the Memory Wheels architecture: [jonesde/unforgettable](https://github.com/jonesde/unforgettable).

---

## Whitepaper

March 2023: open collaboration, automated manufacturing, and distributed means of production as one cycle — why the repo is public, and why “home-scale” is an access argument, not a hobby disclaimer.

Open: [`whitepaper/DemocratizedAccessToTechnologyWhitepaper.md`](whitepaper/DemocratizedAccessToTechnologyWhitepaper.md).

---

## Why this is public

This project is about open design thinking, for the benefit of all. That changes the nature of thinking and the goal of designs with the technology applied. Simple ideas are cast by the wayside by any who do not appreciate their power, but they are the best when seeking open solutions where simplicity and low cost is a benefit instead of a business risk. Open thinking is a path to innovation that the world is largely missing, especially for industrial scale needs. Because of the long-term dominance of closed, proprietary, and centrally controlled thinking, the field for innovation is ripe and waiting for harvest by those of us without… well, whatever it is that leads to closed thinking.

Is this the real reason open software is winning? We have realized the high cost and lack of need for the complex massive proprietary software it replaces, or being originally created deters proprietary competitors from entering the market with anything too similar. It is not that it is cheaper, it is that it is even necessarily better - and an important part of technology being better is also being cheaper, making open the right mindset for efficient innovation. Open software is not winning yet in every domain, and in some proprietary software may always have a market, but open software is winning in many small ways and in a few large ways, like Linux.

As of early 2026 LLM based AI agents have become sufficiently capable that the game is changing for open technology in dramatic ways. Community-created, and -used, software that is tuned primarily for that community is now accessible to a much wider audience of non-experts, with the assistance of AI. Marble ERP and the Moqui Ecosystem projects are designed and built to be customized and deployed by medium to large organizations with particular needs. With modern AI assistance these projects are now accessible by a much larger audience of organizations and even individuals for personal use (maybe a little something to help with tracking all that token spend...). This is increasingly true of more and more technology. With the help of AI, we can stand on the shoulders of a nation of giants, all at once, from nearly anywhere.

The same open bet is on the hardware notes and the effect catalog. CC0. Copy what is useful. Name what still needs validation, production design, and/or safety protocols.
