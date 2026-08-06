# EM-CSAM Driver Board – Consolidated Shopping List (v0.1)

**Notes for builders**
- Quantities show **typical first build → designed maximum**. Populate only what you need.
- Prices are approximate USD (mid-2026 street prices) and will fluctuate. Check current stock.
- Prefer Digi-Key / Mouser for reliable authentic parts on first builds. AliExpress / LCSC are fine for many passives and once you have a working prototype.
- Always verify pin-compatible alternatives before ordering large quantities.
- High-current MOSFETs and capacitors benefit from buying a few extras.

| Component | Qty (min→max) | Primary Recommendation | Good Alternatives | Approx. Unit Price | Recommended Retailers | Notes |
|-----------|---------------|------------------------|-------------------|--------------------|-----------------------|-------|
| Main electrolytic capacitor | 6→12 | 4700 µF 63 V low-ESR (snap-in or radial, ~22×40 mm) | Nichicon, Rubycon, Panasonic low-ESR equivalents; generic low-ESR 63 V | $1.50–4.00 | Digi-Key, Mouser, AliExpress | Parallel is fine; match voltage rating strictly |
| Local film decoupling | 4→8 | 100 nF–1 µF 100 V film | Any good film or C0G/NP0 ceramic 100 V+ | $0.20–0.80 | Digi-Key, Mouser, LCSC | Place close to MOSFET drains |
| Power MOSFET | 4→8 | IRFP4568PBF (150 V, TO-247) | IRFP4668, IPT015N10N5, similar 100–150 V low-Rds(on) TO-247 | $3.50–8.00 | Digi-Key, Mouser, LCSC, AliExpress | Buy extras; paralleling requires individual gate resistors |
| Gate resistor | 8 | 4.7 Ω or 10 Ω 0.25–0.5 W | Any 1% metal film in that range | $0.05–0.15 | Digi-Key, Mouser, LCSC | One per MOSFET footprint |
| Gate-Source resistor (optional) | 8 | 10 kΩ 0.25 W | Any | $0.03–0.10 | Digi-Key, Mouser, LCSC | Helps keep gate defined when off |
| Gate-drive optocoupler | 1 | HCPL-3120 / HCPL-J312 | FOD3182, TLP250, other 2 A+ gate-drive optos | $3.00–6.00 | Digi-Key, Mouser | Core isolation part – buy genuine |
| Gate buffer (optional but recommended) | 1 | TC4420 or UCC27511 | TC4429, other 4–9 A low-side drivers | $1.00–2.50 | Digi-Key, Mouser, LCSC | Improves switching with multiple FETs |
| Isolated DC-DC (gate drive supply) | 1 | 12 V or 15 V 1–2 W isolated module (SIP or similar) | Murata, Recom, Traco, generic Bxx12S-1W style | $4.00–9.00 | Digi-Key, Mouser, AliExpress | Must be isolated |
| Current sensor | 1 | Allegro ACS772 or ACS780 (100–200 A version) | ACS37200, or low-inductance shunt + amplifier | $6.00–12.00 | Digi-Key, Mouser | Hall sensor is easiest for isolation |
| Preconditioning H-bridge | 1 | BTS7960 module or discrete IR2104 + FETs | Any decent 5–20 A H-bridge or half-bridge driver | $5.00–15.00 | Amazon, AliExpress, Digi-Key | Can be a ready module for first build |
| Bleeder resistors | 2–4 | 1–2 kΩ 5–10 W wirewound or thick film | Any power resistor of suitable value | $0.80–2.50 | Digi-Key, Mouser, AliExpress | Total dissipation sized for safe discharge time |
| Snubber components | 2–4 | RC or RCD set (e.g. 10–47 Ω + 0.1–1 µF) | Tune during testing | $0.50–2.00 | Digi-Key, Mouser | Values finalized on the bench |
| Freewheel / TVS | 1–2 | Fast diode or TVS rated > bus voltage | Ultrafast diode or bidirectional TVS | $1.00–4.00 | Digi-Key, Mouser | Across switch or rails |
| Charge indicator LED + resistor | 1 set | Standard 3–5 mm LED + series resistor | Any | $0.20 | Everywhere | Visible when bank is charged |
| Logic connectors / headers | assorted | 0.1″ headers, JST, or screw terminals | — | $1–5 total | Digi-Key, Mouser, Amazon | FIRE, PWM, sense, power |
| PCB | 1 | Custom 2.0–2.4 mm, 2–3 oz copper | JLCPCB, PCBWay, or home CNC | $15–60 | JLCPCB, PCBWay | 2 oz minimum recommended |
| Bus bar / flexible copper stock | as needed | 0.3–0.5 mm+ copper sheet or the custom multi-layer strip | — | Variable | Metals suppliers, Amazon | External high-current path |
| Copper spreader washers / plates | 4–8 | 1–2 mm copper sheet cut to size | — | Low | Metals suppliers | For bolted rail and cable joints |
| Bolts / hardware | assorted | M5 or M6 stainless + steel washers | — | $5–15 | Hardware store, McMaster | 2-bolt clamp system per rail |

**Approximate total for a minimal first build (4 FETs + 6 caps + core electronics):** $80–160 depending on sources and how many parts you already have.

**Builder advice**
- Order a few extra MOSFETs and capacitors – they are the parts most likely to be stressed during bring-up.
- For the very first board, prioritise Digi-Key/Mouser for the optocoupler, MOSFETs, and current sensor.
- Once the design is proven, many of the passives and even the FETs can move to LCSC or AliExpress.
- Keep a small stock of the custom flexible copper strip and 1–2 mm copper plate on hand for the high-current connections.
