# EM-CSAM References

Annotated sources behind the November 2026 design review ([`DesignReview-2026-11.md`](DesignReview-2026-11.md)) and the documents it corrected.

**How to read this file**

- Each entry has an ID. Other documents cite a source as the ID linked to the source itself, for example [RG-KERRISK82](https://www.osti.gov/servlets/purl/5222337). Look the ID up here for the summary.
- "Says" is what the source reports, with its numbers. "Used for" is the claim it supports in these notes.
- Access notes are honest about how the source was read. Several publisher pages were paywalled or blocked, so some numbers come from abstracts, patent text, or secondary copies. Those are marked.
- Section 11 lists what was looked for and **not** found. Do not cite those items as established.

Retrieved 2026-11-10.

**Link check, 2026-11-10.** Each link was fetched once by script. 67 of 84 answered normally. The rest:

- **Refused to a script (HTTP 403) but ordinary web pages:** Digi-Key and Farnell product pages, MDPI, ResearchGate, DOAJ, CORE, CDC Stacks, SpecialChem, SVC, ScienceGate. Open them in a browser.
- **Did not respond on the day:** the DoD fact sheet at p2infohouse.org (PA-EPD), the UHasselt thesis PDF (CH-FORMATE), and the Tomsk library record (PC-EEW, carbides). They are kept because they were read during the review; treat them as possibly dead.
- **Corrected:** the first link recorded for PA-VADER returned "not found" and was replaced with the publisher's page for the same paper.

---

## 1. Component datasheets

| ID | Part | Source | Says (values relied on) | Access |
|---|---|---|---|---|
| DS-IRFP4568 | Infineon IRFP4568PbF | [Datasheet Rev. 2.1, 2024-11-25](https://www.infineon.com/dgdl/irfp4568pbf.pdf?fileId=5546d462533600a4015356310e811e5b) | 150 V. RDS(on) 4.8 mΩ typ / 5.9 mΩ max at 25 °C. ID 171 A (silicon limit), IDM 684 A. Qg 151 nC typ / 227 max; Ciss 10.47 nF, Coss 977 pF, Crss 203 pF. EAS 763 mJ. Body diode ISM 684 A, trr 110 ns, Qrr 515 nC. RthJC 0.29 K/W. VGS ±30 V, VGS(th) 3–5 V. | Read as text. The transient thermal curve (Fig. 13) is an image; ZthJC ≈ 0.021 / 0.063 / 0.081 K/W at 100 µs / 500 µs / 1 ms was **calculated** from the Foster terms printed on an older revision, and should be checked against Fig. 13. |
| DS-UCC21551 | TI UCC21551 | [SLUSEW9D, June 2024](https://www.ti.com/lit/ds/symlink/ucc21551.pdf) | Suffix A = 5 V UVLO (turn-on 6.0 V typ), B = 8 V, C = 12 V (needs ≥13.5 V), D = 17 V. Only the A is sold in SOIC-16 (DW); B/C/D are SOIC-14 (DWK). 4 A source / 6 A sink. VCCI 3.0–5.5 V. Dead time tDT[ns] = 8.6·RDT[kΩ] + 13. DT open or tied to VCCI: no interlock, both outputs can be high. EN active-high with 90 kΩ pull-down. Recommends ~10 µF + ≤100 nF at each VDD and RC input filters. CMTI ≥125 V/ns. | Read as text. The minimum recommended VDD for the A is printed as 6.7 V in one table and 6.5 V in another. |
| DS-ACS772 | Allegro ACS772ECB-200B-PFF-T | [ACS772-DS Rev. 21, 2025-03-17](https://www.allegromicro.com/-/media/files/datasheets/acs772-datasheet.pdf) | ±200 A, 10 mV/A at 5 V, zero at VCC/2. 200 kHz small-signal bandwidth, 2.5 µs response, 0.67 V/µs output slew. Output clamps near the rails beyond range; magnetic offset after overload ≤0.4 A. Overcurrent 1200 A at 25 °C for **1 s** (1 s on / 99 s off). Conductor 100 µΩ. Isolation 4800 VRMS. | Read as text. |
| DS-LGU | Nichicon LGU2A472MELC | [LGU catalog](https://www.nichicon.co.jp/english/series_items/catalog_pdf/e-lgu.pdf) | 4700 µF 100 V, 35 × 50 mm. tan δ 0.20 at 120 Hz, so ESR ≤ ~56 mΩ at 120 Hz. Ripple 4.14 A rms at 105 °C. No ESR or impedance at 10–100 kHz is published. | Read as text. |
| DS-LGU-GUIDE | Nichicon application guidelines | [Guidelines PDF](https://www.mouser.lt/pdfDocs/nichicon-gxc-app-guidelines.pdf) | Standard aluminium electrolytics should not be used where rapid, very frequent charge/discharge is required; consult the maker. | Read as text. |
| DS-B32774 | TDK B32774D4106K000 | [MKP B32774–B32778](https://www.tdk-electronics.tdk.com/inf/20/20/db/fc_2009/MKP_B32774_778.pdf) | 10 µF 450 VDC. ESR 10.9 mΩ (10 kHz), ESL 24 nH, dV/dt 30 V/µs, IRMS 8.0 A. Peak current î = C·dV/dt ≈ 300 A (calculated). The 22 µF part: 5.4 mΩ, 30 nH, ≈660 A. | Read as text. |
| DS-R12P | Recom R12P212S | [RxxP2xx, Rev. 9-2024](https://recom-power.com/pdf/Econoline/RxxP2xx.pdf) | Unregulated 12 V → 12 V, 2 W. Load regulation 10 % typ; no-load output can sit ~10 % high. Isolation 6.4 kVDC, 1.5–10 pF. Maximum capacitive load 680 µF. | Read as text. |
| DS-T9A | TE T9AS1D12-12 | [TE product page copy](https://tvsat.com.pl/PDF/1/1-1393210-3.pdf); [family datasheet copy](https://zoro.com/static/cms/enhanced_pdf/Waldom%20Electronics_engxxdsxx1308242xxt9axx0806xx6983ec.pdf) | SPST-NO, AgCdO. 30 A is the 240 VAC rating. The only DC rating is 20 A at 28 VDC resistive. Contact resistance 75 mΩ initial. Coil 12 V, 1 W. Operate/release 15 ms max. | Third-party copies of the TE documents. |
| DS-5KP | Littelfuse 5KP58A | [Datasheet copy](https://cdn.eicom.ru/media/PDF24/69681.pdf) | Standoff 58 V. Breakdown 64.4–71.2 V. Clamp 93.6 V at 54.5 A. 5 kW for a 10/1000 µs pulse. Forward (unidirectional) IFSM 400 A, VF ≤3.5 V at 100 A. | Third-party copy. |
| DS-MBR20100 | Vishay MBR20100CT | [Doc 88672](https://assets.rs-online.com/v1698967684/Datasheets/8209c593df7f907f3184c5a5cc9a980e.pdf) | 100 V. 10 A per diode, 20 A total. IFSM 150 A per diode. VF ≤0.80 V at 10 A. | Older revision. |
| DS-MUR1560 | onsemi MUR1560G | [MUR1520/D Rev. 11](https://www.onsemi.com/download/data-sheet/pdf/mur1520-d.pdf) | 600 V, 15 A, IFSM 150 A, trr 60 ns. | Read as text. |
| DS-HS25 | Arcol/Ohmite HS25 10R | [HS series sheet](https://static.chipdip.ru/lib/017/DOC027017802.pdf) | 25 W on the standard heatsink, 9 W without. No overload or joule rating is given for the HS25. | Third-party copy. |
| DS-C350 | Kemet C350C104F1G5TA | [Digi-Key page](https://www.digikey.com/en/products/detail/kemet/C350C104F1G5TA/6562499) | 0.1 µF, 100 V, C0G, radial, 10.16 mm pitch. "F" is ±1 % and expensive; the ±5 % part is C350C104**J**1G5TA. | Distributor page. |
| DS-PA0006 | Chip Quik PA0006 | [Digi-Key page](https://www.digikey.com/en/products/detail/chip-quik-inc/PA0006/5014721); [Farnell PA0006C](https://cpcireland.farnell.com/proto-advantage/pa0006c/smd-adaptor-soic-16-to-dip/dp/PC02844) | SOIC-16 to DIP-16 adapter, 0.7″ × 0.8″. Farnell lists the PA0006**C** as "300 mil body SOIC-16 to 600 mil DIP". | The Digi-Key page gives no body width. Confirm the wide-body fit and the DIP row spacing before relying on it. |

---

## 2. Railgun physics and augmentation

- **RG-KERRISK82** — J. F. Kerrisk, "Current Diffusion in Rail-Gun Conductors", Los Alamos LA-9401-MS, June 1982. [OSTI](https://www.osti.gov/servlets/purl/5222337)
  - *Says:* Tabulates the high-frequency inductance gradient L′ for rectangular rails. The fit L′[µH/m] = [0.4406 − 0.0777·ln F1]·ln F2 reproduces its Table I (0.347, 1.007 and 0.456 µH/m for the cases checked). For 10 × 10 mm copper rails L′ rises from 0.466 to about 0.62 µH/m within ~0.15 ms as current diffuses in.
  - *Used for:* L′ of flat rails; why L′ depends on pulse length.
  - *Access:* Open. The original fit report (LA-9092-MS) was not retrieved, so its stated validity range is unknown; the flat-rail geometry here is outside any range it was probably fitted on.

- **RG-ASGARI19** — Asgari et al., *Advanced Electromagnetics* 8(1), 2019. [PDF](https://www.aemjournal.org/index.php/AEM/article/download/961/443/4084)
  - *Says:* For a permanent-magnet augmented railgun, F = ½L′I² + B₀·I·S. The magnet term dominates when B₀ ≫ L′I/(2S). Augmentation "increases railgun efficiency, especially in low current railguns". FEM gives 2.02× force at 30 kA with four magnets. Typical L′ 0.4–0.7 µH/m.
  - *Used for:* Magnet augmentation and why it suits a low-current launcher.
  - *Access:* Open. Its printed Kerrisk formula carries a spurious µ₀ factor.

- **RG-GALLANT02** — Gallant & Lehmann (ISL), 20th Int. Symp. on Ballistics, 2002. [PDF](https://researchportal.rma.ac.be/ws/portalfiles/portal/8004700/ParallelAugmentedRailguns.pdf)
  - *Says:* For augmenting rails, F = ½L′·I_R² + M′·I_R·I_A. On a 15 mm bore, peak rail current fell from 180 to 127 kA at about the same velocity. Effective L′ varied 0.41–0.46 µH/m along the shot.
  - *Used for:* Series augmentation force law and its effect on peak current.
  - *Access:* Open.

- **RG-KATSUKI95** — Katsuki et al., *Rev. Sci. Instrum.* 66(8):4227, 1995. [INIS record](https://inis.iaea.org/records/vvaxe-vj462)
  - *Says:* Experimental comparison of a conventional and a permanent-magnet augmented railgun at about 20 kA; reports a benefit.
  - *Access:* Abstract only; no number retrieved.

- **RG-HARTKE97** — Hartke, Naval Postgraduate School MS thesis, Dec 1997 (DTIC ADA341268).
  - *Says:* A 44 cm capacitor-fed low-voltage railgun went 85 % faster with a permanent-magnet field.
  - *Access:* Summary only; no open link retrieved.

- **RG-NPS15** — Naval Postgraduate School thesis on multi-turn augmentation, 2015. [Calhoun](https://calhoun.nps.edu/handle/10945/2855)
  - *Says:* "Significant performance enhancement" from series and multi-turn augmentation.
  - *Access:* Record page.

- **RG-MCNAB03** — I. R. McNab, *IEEE Trans. Magn.* 39(1):295, 2003. [PDF](https://research.lifeboat.com/ieee.em.pdf)
  - *Says:* In a constant-current breech-fed railgun the magnetic energy left in the barrel equals the muzzle kinetic energy, so efficiency is at most 50 %. Copper rails reach melt at about 44 kA per mm of rail height.
  - *Used for:* Efficiency framing; residual inductive energy at exit.
  - *Access:* Open copy.

- **RG-TUCKER75** — Tucker & Toth, Sandia SAND-75-0041. [OSTI](https://www.osti.gov/servlets/purl/4229184-1IbmTb/)
  - *Says:* Action to reach melt from room temperature, converted to A²·s/m⁴: Cu ≈ 8.0×10¹⁶, Al 2.5×10¹⁶, Fe 1.3×10¹⁶, W 2.4×10¹⁶, Zn 1.1×10¹⁶, Sn 1.7×10¹⁵.
  - *Used for:* Action margin per material.
  - *Access:* Open scan. The copper entry is hard to read in the text layer; on the page image it is 80492 A²·s/mm⁴ at the start of melting, which confirms 8.0×10¹⁶ A²·s/m⁴ (re-read 2026-11-11). It was also cross-checked against bond-wire fusing data. A 2013 *IEEE Trans. Plasma Sci.* paper found these values do not match its own measurements for Cu, Al and Ti, so treat them as ±tens of percent.

- **RG-WOODS96** — Woods, "Analysis of the Armature-Rail Interface in Solid Armature Railguns", Institute for Advanced Technology report IAT.R 0120 (1996). [DTIC](https://apps.dtic.mil/sti/tr/pdf/ADA320642.pdf)
  - *Says:* Behind a moving contact of length a at speed V the current in the rail is confined to a depth of about 2√(D·a/V), set by the transit time and not by the pulse length.
  - *Used for:* Velocity skin effect: about 0.73 mm at 100 m/s and 0.33 mm at 500 m/s for a 1 mm slug on copper (arithmetic in `quantum-systems/analysis/checks/`).
  - *Access:* Open, full text read. A model; no direct measurement was opened.

- **EM-MORITZ11** — Moritz, "Eddy currents in accelerator magnets", arXiv:1103.1800. [arXiv](https://arxiv.org/abs/1103.1800)
  - *Says:* A field step diffuses into a conductor with an error-function profile; the usual depth rule is 2√(Dt) with D = ρ/μ₀ (after Knoepfel, not opened).
  - *Used for:* Single-pulse penetration into the rails, in place of the steady skin depth.
  - *Access:* Open, full text read.

- **RG-MUZZLE** — Muzzle-arc suppression: US 4,714,003 (muzzle shunt loop), US 4,733,595 (ZnO varistor suppressor), US 4,938,113 (arrestor at the muzzle).
  - *Says:* Without a path for the residual current, a large voltage builds at the rail ends and arcs. The shunt's resistance and inductance have to be matched to the launcher.
  - *Access:* Cited by number; patent text only.

---

## 3. Closest prior art

The top-level README once said no close cousin had been found. These are the closest.

- **PA-EPD** — University of Texas Center for Electromechanics, "electromagnetic powder deposition". [US 6,329,025 B1](https://patents.google.com/patent/US6329025B1/en) (Bacon, Davis, Sledge, Polizzi, Uglum, Weldon, Zowarka; filed 1998, granted 2001, now expired). [DoD fact sheet](https://p2infohouse.org/ref/11/10452.htm). Paper: Zowarka et al., *IEEE Trans. Magn.* 35(1):268, 1999.
  - *Says:* A railgun with an argon plasma armature "snowplows" the gas in the bore into a shock-compressed column moving at about 4.2 km/s. Powder fed through side ports is dragged to more than 2 km/s. Bore about 12.7 × 12.7 mm, rails ≥50 cm, about 150 kA peak, ~120 µs pulse, 28 mF bank, 30 Hz bursts. Preliminary coatings reported bond strength equal to the base metal and under 3 % porosity.
  - *Why it matters here:* It is a railgun used for powder deposition, but at 100× the current, with a plasma armature, and with the gas (not the slug) as the working body. It shows the gas-drag route to true particle velocities, which is the "carrier flash" regime in these notes.
  - *Access:* Patent and fact sheet open; paper not retrieved. Why it was not commercialised: not found.

- **PA-EMAPS** — Kitamura et al., "electromagnetically accelerated plasma spraying", *J. Therm. Spray Technol.* 12:70–76, 2003. [Springer](https://link.springer.com/article/10.1361/105996303770348519)
  - *Says:* A coaxial pulsed plasma gun (about 100 kA for about 300 µs) accelerates about 1 g of pre-injected powder to 1–3 km/s. Boron carbide coatings reached about 2600 HV.
  - *Access:* Abstract.

- **PA-ELTEPS** — Tamura group, electrothermal-explosion powder spray. [2002](https://link.springer.com/article/10.1361/105996302770349032), [2006](https://link.springer.com/article/10.1007/s11666-006-5008-4)
  - *Says:* A discharge through a refractory powder column (WC, TaC, ZrB₂, TiN–TiB₂) delivers about 2–3× the energy needed to melt it. Jet front above 3 km/s in one study and about 900 m/s for TiB₂; coatings densify as particle speed rises from ~780 to over 900 m/s.
  - *Why it matters here:* This is the "exploding slug" regime done on purpose.
  - *Access:* Abstracts. Stored energy and voltage not found.

- **PA-VADER** — Vader Systems / Xerox ElemX magnetohydrodynamic liquid-metal jetting. Vader, Vader, Karampelas, Furlani, "Advances in Magnetohydrodynamic Molten Metal Jet Printing", [TechConnect Briefs 2016, vol. 4, pp. 41–45](https://briefs.techconnect.org/papers/advances-in-magnetohydrodynamic-molten-metal-jet-printing/); [ElemX brochure](https://xerox.com/downloads/usa/en/3d-printing/ElemX-3D-Printer-Brochure.pdf)
  - *Says:* A pulsed coil induces current in molten aluminium and ejects 250–1000 µm droplets at several m/s, 50–1000 Hz sustained. The ElemX quotes up to 400 drops/s and 0.24 mm minimum layer.
  - *Why it matters here:* The low-velocity, molten end of Lorentz-force metal printing.
  - *Access:* Publisher abstract page and brochure. The numbers were read from a PDF copy of the paper that is no longer at its original address.

- **PA-OCE** — Océ, US 9,593,403 (priority 2014).
  - *Says:* Electrodes pass current through a metal melt sitting between permanent magnets; a pulsed current in a steady field ejects droplets. Targets copper, silver and gold.
  - *Why it matters here:* The direct-current, magnet-augmented cousin of this head, for liquid metal.
  - *Access:* Patent text; no journal data found.

- **PA-LIFT** — Laser-induced forward transfer of high-viscosity metal pastes (Universidad Politécnica de Madrid with Princeton). [UPM archive](https://oa.upm.es/77023/)
  - *Says:* Silver pastes of about 250 Pa·s can be transferred, in a narrow process window.
  - *Access:* Record page.

---

## 4. Pulsed-power practice

- **PP-KWELD** — keenlab kWeld spot welder. [Product page](https://www.keenlab.de/index.php/portfolio-item/kweld/)
  - *Says:* 2000 A maximum switch current (tested to 2800 A with reduced life) from a 5–15 V source through paralleled MOSFETs. Current is read from the drop across the MOSFETs' on-resistance. Energy is metered in joules per weld, with a watchdog and lead-resistance calibration.
  - *Used for:* A working reference for kA pulses through paralleled FETs at low voltage; the strap or nickel-strip weld as a dummy load.
  - *Access:* Open. The MOSFET type comes from forum posts.

- **PP-PARALLEL** — Application notes on paralleling MOSFETs: TI SLPA020, Nexperia AN50005, International Rectifier AN-941, Microsemi APT0402, onsemi AND90108.
  - *Says:* Give each device its own gate resistor. Imbalance comes from part-to-part spread and is worst at the switching edges. Equalise common-source inductance. In avalanche the device with the lowest breakdown voltage takes most of the energy, so clamp the overvoltage rather than rely on avalanche.
  - *Access:* Cited by document number.

---

## 5. Cold-spray bonding windows

- **CS-SCHMIDT09** — Schmidt, Assadi, Gärtner, Richter, Stoltenhoff, Kreye, Klassen, *J. Therm. Spray Technol.* 18:794–808, 2009. [Table](https://www.researchgate.net/figure/alues-of-critical-velocity-for-bonding-assuming-a-particle-size-of-20-lm-Material-Melting_tbl1_225516724)
  - *Says:* Critical velocity for bonding at 20 µm particle size: Sn 160–180, Zn 360–380, Cu 460–500, Al 620–660, 316L 700–750, Ti 700–890, Ta 490–650 m/s.
  - *Used for:* The material ladder.
  - *Access:* Table seen as a figure caption. A nickel value (610–680) was not confirmed.

- **CS-SCHMIDT06** — Schmidt, Gärtner, Assadi, Kreye, *Acta Mater.* 54:729–742, 2006. Seen through the [Hussain review](https://www.nottingham.ac.uk/research/groups/cse/documents/peer-reviewed-journal-papers-2016/8-cold-spraying-of-titanium-a-review-of-bonding-mechanisms-microstructure-and-properties.pdf).
  - *Says:* v_cr = √[F1·4σ_u(1 − (T_i − T_R)/(T_m − T_R))/ρ + F2·c_p(T_m − T_i)] with F1 = 1.2, F2 = 0.3. Below a critical diameter heat leaks away too fast for adiabatic shear. Upscaled tests fired 20 mm copper balls at steel. Titanium measurements run 505–750 m/s depending on powder. Powder oxygen matters: copper from 0.02 to 0.38 wt % O raised the critical velocity from about 300 to 610 m/s.
  - *Used for:* Temperature and size trends; oxygen sensitivity.
  - *Access:* Secondary (review).

- **CS-MORIDI14** — Moridi, Hassani-Gangaraj, Guagliano, Dao, *Surf. Eng.* 30:369, 2014. [Open copy](https://re.public.polimi.it/bitstream/11311/968457/4/Cold%20spray%20coating_11311-968457_Guagliano_1.pdf)
  - *Says:* Raising particle temperature lowers the critical velocity. Review of coatings including NdFeB composites.
  - *Access:* Open.

- **CS-SIZE13** — Particle-size fit, *J. Therm. Spray Technol.* 2013. [Springer](https://link.springer.com/article/10.1007/s11666-013-0023-8)
  - *Says:* v_cr ≈ 900·d^−0.19 for Cu and 316L; the effect is small above about 50 µm.
  - *Access:* Abstract.

- **CS-DOWDING20** — Dowding et al., *Acta Mater.* 2020. [OSTI](https://www.osti.gov/servlets/purl/1658603)
  - *Says:* Larger aluminium particles bond at lower speed (810 → 770 m/s across the range tested).
  - *Access:* Open.

- **CS-LIPIT** — Hassani-Gangaraj, Veysset, Nelson, Schuh, single-particle impact tests. [arXiv:1612.08081](https://arxiv.org/abs/1612.08081)
  - *Says:* Critical bonding speed is about 0.15 × the bulk sound speed. Aluminium about 810–825 m/s at 10–14 µm.
  - *Access:* Open.

- **CS-WARM** — NIMS "warm spraying". [Press release 2012](https://archive.nims.go.jp/eng/news/press/2012/06/p201206140.html)
  - *Says:* A modified HVOF process heats particles below melting; 30 µm titanium reached about 1000 m/s.
  - *Used for:* Hot-but-solid particles as an established idea.
  - *Access:* Open.

---

## 6. Powder conduction and electrical sintering

- **PC-FALCON05** — Falcon & Castaing, *Am. J. Phys.* 2005 (arXiv cond-mat/0407773). [ar5iv](https://ar5iv.labs.arxiv.org/html/cond-mat/0407773)
  - *Says:* A chain of oxidised metal beads measures 10⁴–10⁷ Ω at low current (force-dependent), then drops irreversibly to 1–10 Ω. The voltage saturates per contact at 0.4 V for stainless steel, 0.3 V for brass and 0.2 V for bronze; copper was not measured. The contact spots reach about 1050 °C (micro-welding); the plateau is that regime.
  - *Used for:* Why powder paste is high-resistance until its contacts weld, and the 0.2–0.4 V per contact range. Corrected 2026-11-11: earlier notes quoted 0.4 V as if it applied to copper.
  - *Access:* Open.

- **PC-CREYSSELS09** — Creyssels, Falcon, Castaing, Powders & Grains 2009, *AIP Conf. Proc.* 1145. [PDF](https://labo.msc.u-paris.fr/~falcon/AIP09.pdf)
  - *Says:* Copper powder (50–110 µm) compressed to 30 N/mm² follows R ∝ P^−1.8, controlled by the oxide film.
  - *Used for:* Compaction as a conductivity lever.
  - *Access:* Open.

- **PC-SOLDERPASTE** — Electrical conduction in solder paste. [CORE](https://core.ac.uk/download/288386976.pdf)
  - *Says:* Resistance is set by the few contact spots where the oxide is thin or broken; a high field lowers it by breaking the oxide.
  - *Access:* Open. No numeric resistivity found.

- **PC-FRITTING** — Fritting technical note. [PA3FWM](https://www.pa3fwm.nl/technotes/tn17a.html)
  - *Says:* Gives "1 mA and a few volts" for wetting a contact. It does not give a fritting time; an earlier summary here said "a few volts for a few microseconds", which the note does not say (corrected 2026-11-11).
  - *Access:* Informal note.

- **PC-ALIOUAT22** — Aliouat et al., "Investigation of Electrical Transitions in the First Steps of Spark Plasma Sintering", *Materials* 15, 4096 (2022). [DOI](https://doi.org/10.3390/ma15124096)
  - *Says:* A bed of 87.5 µm copper powder carrying 1200 nm of oxide sits near 10⁸ Ω, then the voltage climbs to a peak (15.6, 24.3 and 33.4 V for 0.30, 0.40 and 0.50 mm beds) and collapses by five orders of magnitude at about 0.4 mA; no plateau. The breakdown field falls with compaction, 57 kV/m unloaded to 18 kV/m at 300 MPa. The welded bridges are 10–15 µm and a mechanical shock breaks them.
  - *Used for:* The conditioning-bus voltage needed for an oxidised copper fill, and the fragility of a conditioned slug.
  - *Access:* Open, full text read. A deliberately thick oxide; a native oxide should need less.

- **PC-DEGEN06** — Degen, Nagler, Horn & Kaesen, "Parametric Study of Contact Fritting for Improved CRes Stability", Southwest Test Workshop 2006. [PDF](https://www.swtest.org/swtw_library/2006proc/PDF/S04_02_Degen.pdf)
  - *Says:* A-fritting (film puncture) occurs below 2.5 V on aluminium probe pads and is complete in about 150 µs.
  - *Used for:* The time and voltage scale of film puncture, in place of the PC-FRITTING misquote.
  - *Access:* Open conference slides; secondary to Holm.

- **PC-FRITFIELD** — Fritting field of surface films: Deringer-Ney, *Ney Contact Manual* (rev. 2022) [PDF](https://deringerney.com/wp-content/uploads/2022/04/Ney-Contact-Manual-Revised-1st-Edition.pdf); US 7,061,259 [patent](https://patents.google.com/patent/US7061259B2/en).
  - *Says:* Films puncture at 10⁵–10⁶ V/cm (10⁷–10⁸ V/m).
  - *Used for:* Film puncture as a field threshold, separate from the 0.2–0.4 V thermal plateau.
  - *Access:* Open secondaries. Holm's *Electric Contacts* itself was not opened.

- **PC-ALLEN08** — Allen et al. (VTT), "Electrical sintering of nanoparticle structures", *Nanotechnology* 19:175201, 2008. [VTT record](https://cris.vtt.fi/en/publications/electrical-sintering-of-nanoparticle-structures/)
  - *Says:* Conductivity rises by more than five orders of magnitude, to 3.7×10⁷ S/m at best. The main transition takes under 2 µs "due to strong positive feedback induced by the voltage boundary condition".
  - *Used for:* Conditioning is electrical sintering and runs away under voltage drive.
  - *Access:* Record and abstract.

- **PC-HUMMELGARD11** — Hummelgård et al., *PLoS ONE* 6:e17209, 2011. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3044741)
  - *Says:* A series resistor limits the runaway "but not removing the effect completely".
  - *Used for:* Ballast-resistor conditioning.
  - *Access:* Open.

- **PC-ARANDA21** — Aranda et al., *Metals* 11:616, 2021. [DOAJ](https://doaj.org/article/482d455bc7ab44769df3f2e4cf8685c7)
  - *Says:* Review of capacitor-discharge consolidation of powders; heating in microseconds to milliseconds.
  - *Access:* Record. Current densities not retrieved.

- **PC-EEW** — Electrical explosion of wires. [Review](https://doi.org/10.1023/B:NANO.0000006069.45073.0b); [energy study](https://earchive.tpu.ru/jspui/bitstream/11683/34704/1/dx.doi.org-10.1088-1757-899X-142-1-012020.pdf); [carbides in hydrocarbons](https://vufind.lib.tpu.ru/vufind/Record/646876)
  - *Says:* Specific energy of 0.4–1.8 times the sublimation energy gives 20–100 nm powders at about 25 kWh/kg. Exploding W, Ti or Al wire in hydrocarbons produces carbides.
  - *Used for:* The exploding-slug regime and what a hydrocarbon carrier does in it.
  - *Access:* Mixed.

---

## 7. Carrier chemistry and metallic carriers

- **CH-DGA** — Oil decomposition in arcs. [Dissolved gas analysis overview](https://limswiki.org/index.php/Dissolved_gas_analysis); US 3,224,952.
  - *Says:* Acetylene is the signature gas of arcing in transformer oil, and hydrogen comes with it. A sustained arc in fuel oil gave 25–35 % C₂H₂, 5–10 % C₂H₄ and the rest mainly H₂.
  - *Used for:* What a mineral-oil carrier turns into.
  - *Access:* Overview and patent. No measured composition for flash heating, and no soot yields.

- **CH-FORMATE** — Copper formate and reducing media. [UHasselt](https://documentserver.uhasselt.be/bitstream/1942/27642/3/MarchalW_draft2018_1_IC.pdf); [Osaka thesis](https://ir.library.osaka-u.ac.jp/repo/ouka/all/73557/30795_Dissertation.pdf); [Mater. Trans. 63(5)](https://www.jstage.jst.go.jp/article/matertrans/63/5/63_MT-N2021004/_html/-char/en)
  - *Says:* Copper formate decomposes at about 200–220 °C (amine complexes at 100–150 °C) to Cu + 2CO₂ + H₂. Copper nanoparticles sintered under formic-acid vapour at 200 °C reached about 2.2× bulk resistivity. Commercial copper die-attach pastes run at 250–275 °C for 3–5 min.
  - *Used for:* Self-reducing carriers.
  - *Access:* Open. No source found showing ethylene glycol itself reduces the oxide in a paste.

- **CH-GALLIUM** — Gallium and Galinstan. [Ga–Cu paste (NSF)](https://par.nsf.gov/servlets/purl/10188018); [ORNL](https://www.ornl.gov/publication/liquid-solid-mixtures-ga-metal-infused-cu-microparticles-and-nanoparticles-microscale); [Galinstan](https://en.wikipedia.org/wiki/Galinstan); [gallium embrittlement of aluminium](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11901249/); [arXiv 1604.07473](https://arxiv.org/pdf/1604.07473)
  - *Says:* Galinstan conducts 3.46×10⁶ S/m (2.9×10⁻⁷ Ω·m). Copper powder in liquid gallium hardens to CuGa₂ over hours to days at room temperature. Gallium penetrates aluminium grain boundaries quickly even without stress. Tungsten and tantalum resist gallium best; copper in Galinstan for nine weeks showed only minor surface traces.
  - *Used for:* A conductive, alloying carrier, and its hard limit (no aluminium).
  - *Access:* Open.

- **CH-TLPS** — Transient-liquid-phase sintering pastes.
  - *Says:* Cu₆Sn₅ melts at 415 °C and Cu₃Sn at 676 °C, so a paste processed at 120–260 °C gives a joint that survives above 300 °C. A Cu@Sn–Bi paste reached 481 µΩ·cm after a 200 °C cure. Kirkendall voids are hard to avoid in Cu–Sn.
  - *Access:* **No primary link retrieved.** Numbers come from the literature check and need a pinned source before being relied on.

- **CH-AL** — Aluminium chemistry. [Aluminium carbide](https://en.wikipedia.org/wiki/Aluminium_carbide); [Metals 10(3):368, 2020](https://www.mdpi.com/2075-4701/10/3/368/htm); US 5,156,326; SAE 971861.
  - *Says:* Al₄C₃ forms above about 500 °C and hydrolyses in humid air to Al(OH)₃ and methane; silicon suppresses it. Hydrogen is far more soluble in liquid than in solid aluminium, which drives porosity. Nocolok flux (KAlF₄ with K₃AlF₆) starts melting near 560 °C and breaks up the oxide film.
  - *Access:* Mixed. HF release during brazing itself was not found in a source.

- **CH-NICRBSI** — Self-fluxing NiCrBSi alloys: US 4,192,672; US 4,401,724.
  - *Says:* Boron and silicon form low-melting glasses that act as flux and lower the alloy's melting point.
  - *Access:* Patent text. The usual 1000–1100 °C fusing temperature was not found in these sources.

---

## 8. Rail and insulator materials

- **MT-CUH** — Hydrogen embrittlement of oxygen-bearing copper. [Metals 14(5):588](https://www.mdpi.com/2075-4701/14/5/588)
  - *Says:* ETP copper (C11000) carries 0.02–0.04 % oxygen as Cu₂O. Hydrogen diffuses in, forms steam at the oxide, and opens grain-boundary voids. Supplier data put the risk above about 370 °C in reducing atmospheres.
  - *Used for:* Avoiding C110 rails under a hydrogen-rich carrier vapour.
  - *Access:* Open. Immunity of phosphorus-deoxidized grades was not directly confirmed.

- **MT-C145** — Tellurium copper C14500. [Concast data sheet](https://www.concast.com/files/C14500.pdf)
  - *Says:* P 0.004–0.012 %, Te 0.40–0.70 %; phosphorus-deoxidized. Conductivity 93 % IACS (90–96 %).
  - *Access:* Open.

- **MT-C18150** — CuCrZr, RWMA Class 2. [Alcavil](https://alcavil.pages.dev/en/materials/class-2-c18150)
  - *Says:* ≥75 % IACS, typically 80–85 %. Softens at about 500 °C.
  - *Access:* Supplier page.

- **MT-GLIDCOP** — GlidCop dispersion-strengthened copper. [Overview](https://en.wikipedia.org/wiki/Glidcop)
  - *Says:* AL-15 is 92 % IACS, AL-25 87 %; little softening after high-temperature exposure.
  - *Access:* Overview.

- **MT-WCU** — Tungsten–copper 75W–25Cu, RWMA Class 11. [EPoS data sheet](https://eposintering.com/wp-content/uploads/2014/09/Material-Datasheet-W-Cu-20250312.pdf)
  - *Says:* 40–46 % IACS. Used for EDM electrodes because it wears less.
  - *Access:* Supplier page.

- **MT-RAILCOAT** — Cold-sprayed CuCrZr–W coating on railgun rails, *J. Mater. Res. Technol.* 2023. [DOAJ](https://doaj.org/article/7666ef35a8fe4eefba41fe0c597a9b15)
  - *Says:* The coating eroded less than oxide-dispersion copper.
  - *Access:* Record.

- **MT-CTI** — Comparative tracking index. [CMC table](https://www.cmc.de/en/cti-kriechstromfestigkeit)
  - *Says:* PTFE and PE sit in group I (≥600 V). PEI, PEEK and PI sit in group IIIb (100–174 V).
  - *Used for:* PEI and PEEK are poor choices for an arc-facing bore wall.
  - *Access:* Open.

- **MT-ARC** — Arc resistance (ASTM D495). [SpecialChem](https://www.specialchem.com/plastics/guide/arc-resistance)
  - *Says:* POM 200–220, PFA 180, PEI 128, PEEK 40 (seconds).
  - *Access:* Open.

- **MT-ULTEM** — Ultem 1000. [Data sheet](https://Protolabs.com/media/1020056/ultem-resin_1000_americas_technical_data_sheet.pdf)
  - *Says:* CTI 150 V.
  - *Access:* Open.

- **MT-ABLATE** — Polymers in arc chutes, *Plasma Chem. Plasma Process.* 2024. [Springer](https://link.springer.com/article/10.1007/s11090-024-10451-1); [Bendig 2019](https://ppt.fel.cvut.cz/articles/2019/Bendig.pdf)
  - *Says:* POM, PA6 and PTFE ablate and release gas; POM loses about twice the mass of PTFE.
  - *Access:* Abstract and open paper. No source found that directly shows aromatic polymers char to conductive carbon; the general literature says organics fail by tracking or carbonisation.

- **MT-MACOR** — Macor machinable glass-ceramic. [Accuratus](https://accuratus.com/macormats.html)
  - *Says:* 800 °C continuous, 1000 °C peak. Hexagonal boron nitride is quoted elsewhere at 850 °C in air and survives a 400 °C water quench against 200 °C for Macor.
  - *Access:* Supplier page.

- **MT-LAVA** — Grade A lava (pyrophyllite). [Professional Plastics](https://professionalplastics.com/LAVA?XLT_TO=en)
  - *Says:* Machined soft, then fired at 1010–1095 °C; usable to about 1150 °C afterwards.
  - *Access:* Supplier page.

---

## 9. Adjacent processes

- **AD-ESD** — Electrospark deposition. [PNNL overview](https://www.svc.org/clientuploads/directory/resource_library/02_087.pdf); [parameter study](https://tribology.rs/journals/2024/2024-1/2-1508.pdf)
  - *Says:* Spark energies up to 10 J, pulses of a few microseconds, 0.1–4 kHz. A Ti6Al4V study used 0.68–4.4 µF and 0.005–0.045 J per pulse. Too much energy cracks the coating; too little gives a weak one.
  - *Used for:* Another use for the same pulse driver.
  - *Access:* Open.

- **AD-MAGNET** — Cold-sprayed permanent magnets. Lamarre & Bernier, *J. Therm. Spray Technol.* 28:1709, 2019. [Springer](https://link.springer.com/doi/10.1007/s11666-019-00917-6); [euspen 2024](https://euspen.eu/knowledge-base/ICE24196.pdf)
  - *Says:* NdFeB powder is cold-sprayed with an aluminium binder; the hard NdFeB fractures but is trapped by the deforming aluminium and keeps its magnetic properties. A separate group reports Br = 414 mT and Hcj = 854 kA/m.
  - *Used for:* Printed magnets exist, but with a conducting binder.
  - *Access:* Abstract; open conference paper. Energy product not found.

- **AD-CUCERAMIC** — Copper on ceramics and Cu–W. [ASME IPACK 2021](https://www.sciencegate.app/document/10.1115/ipack2021-69270); [W@Cu powder](https://aminer.org/pub/64aae5b2d68f896efa7b50e7/simulation-and-experimental-study-on-cold-sprayed-wcu-composite-with-high-retainability)
  - *Says:* Copper on AlN needs a roughened or treated surface for interlocking. Copper on sprayed alumina reached 8.3–11.4 MPa pull-off. On polymers the substrate erodes. Cold-sprayed Cu–W tops out near 52 wt % W unless core-shell powder is used.
  - *Access:* Records.

---

## 10. Safety

- **SF-DUST** — Metal powder explosibility. [CDC / Fauske](https://stacks.cdc.gov/view/cdc/195110/cdc_195110_DS1.pdf); [IChemE Hazards 30](https://www.icheme.org/media/25710/hazards-30-paper-47-gakhar.pdf)
  - *Says:* Atomised aluminium Kst 64–274 bar·m/s, above 500 for fine or nano grades; minimum ignition energy about 50 mJ or lower. Titanium 21.9 mJ at 45 µm and under 1 mJ at 3 µm.
- **SF-FUME** — Metal fume fever. [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK583199/)
  - *Says:* Onset 3–12 h after exposure, resolves in 24–48 h. Zinc and copper fume both cause it. OSHA limit for ZnO fume 5 mg/m³.
- **SF-NICKEL** — Nickel. [CAREX Canada](https://www.carexcanada.ca/?p=9614)
  - *Says:* Nickel compounds are IARC Group 1; metallic nickel Group 2B; also a skin sensitiser.
- **SF-MIST** — Oil mist. [IChemE Hazards XXIII](https://www.icheme.org/media/9045/xxiii-paper-43.pdf)
  - *Says:* Oil mist can burn below the liquid's flash point. Lower explosive limits run from about 5 to 100 g/m³ depending on droplet size and fuel.

---

## 11. Looked for and not found

Do not state these as sourced facts.

- A critical velocity for nickel in the Schmidt 2009 table.
- Holm's *Electric Contacts* itself (the fritting field is now sourced as a range through two secondaries, PC-FRITFIELD).
- A per-contact saturation voltage for copper beads or copper powder, and any contact data for a powder-in-oil or moving slurry armature.
- A direct measurement of the velocity-skin current layer against speed (model formulas only, RG-WOODS96).
- A numeric resistivity for uncured solder paste or metal powder in oil.
- Published high-frequency ESR, or any pulse-discharge rating, for the Nichicon LGU cans.
- A pulse or joule rating for the HS25 resistor.
- Head-to-head arc-erosion data for molybdenum, tungsten and graphite rails.
- A source showing PEI or PEEK char to conductive carbon under arcing (their low tracking index is sourced).
- Primary sources for the transient-liquid-phase paste numbers in CH-TLPS.
- The fusing temperature of NiCrBSi alloys, and the fume composition of fluoride flux during brazing.
- Cold-sprayed soft magnetic composites, and cold-sprayed Cu–Cr contacts.
- Why the UT-CEM powder deposition process was not commercialised.
- An open copy of Hartke's 1997 thesis.
