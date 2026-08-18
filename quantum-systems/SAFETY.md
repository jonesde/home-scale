# Safety and how to read this repository

These files are **theories, mappings, and design notes**. They are **not** tested operating procedures, not a lab manual, and not a license to build or run hardware.

Nothing here has been validated as a safe or complete experimental protocol. If you do not already work under a competent lab, shop, or industrial safety program, do not treat geometry, pressures, pulse sizes, or material lists as instructions.

---

## What this repository is not

- Not a nuclear how-to. There is no demonstrated nuclear process here and no path offered to net energy or “yield.”
- Not a weapons or launcher design. The micro-railgun material is a short-barrel, joule-class deposition concept.
- Not a substitute for a safety review, pressure-vessel code, hydrogen-service practice, electrical lockout, or radiation program.

Do **not** scale inventory, pressure, or pulse energy in search of a nuclear signature. Do **not** skip isolation steps to “see neutrons.”

---

## Hazards that are easy to underestimate

People who have not worked in a lab or shop often miss that the following are routinely lethal or career-ending, even at the small sizes named in the notes.

**Hydrogen and deuterium.** Flammable. Small molecules leak through ordinary seals and fittings. A Schrader valve and HVAC tubing are **not** hydrogen service. A few tens of bar in a small tube is still stored energy. Mix with air in a volume and you have an explosion problem, not a “gas experiment.”

**Fine metal powder.** Dust clouds of Al, Mg, Ti, Fe, or similar can explode. Fine powder on skin or in a wound is a medical problem. Titanium and some reactive metals plus a hydrogen-rich carrier is a known bad combination (embrittlement and fire).

**Hydrogen + powder + pressure together.** The applications discuss H₂/D₂ over Ni, Pd, or steel powder in a small vessel. That stack is flammability + dust + stored pressure. It is an industrial hazard set. “Grams of powder” and “¼-inch tube” do not make it hobby-safe.

**Pulsed high current.** Capacitor banks and kiloampere-class pulses cause contact burns, flying molten metal, hearing damage, and unexpected motion of anything in the magnetic field. Low voltage (tens of volts) is not low hazard when the energy is dumped in microseconds. Treat every charged bank as live until you have a verified bleed.

**Beryllium copper (BeCu).** Named only as a possible high-pressure cell alloy. Machining, grinding, or abrading BeCu without a beryllium-controlled shop produces chronic toxic dust. **If you do not already have that shop, stay on copper** and stay at prototype pressures. Do not “upgrade” to BeCu as a casual step.

**Pressure vessels.** Threaded plugs, flare nuts, and crush washers fail from scratched faces, wrong torque, and hydrogen embrittlement of the *fittings*. A small ID does not make 150–300 bar a science-fair fitting.

**Unwanted hydrogen in a part.** Spraying steel or Ti with a hydrogen-rich carrier can charge the metal. Delayed cracking shows up later in a load-bearing part. A post-process bake is not optional folklore if you charged the alloy; it is also not a protocol specified here.

**Radiation search.** A neutron detector next to a pulsed D₂ cell is a *search*, not evidence you have a source. The pulse itself is a serious EMI and electrical hazard. Do not improvise shielding, isotopes, or “just a little more D₂.” Accelerator and reactor-hall mappings in the application directory are not beamline or hall SOPs. Do not scale muon current, crystal Δ*T*, or target inventory in search of a nuclear signature.

---

## How applications should be read

[EM-LENR](application/EM-LENR.md), [EM-CSAM](application/EM-CSAM.md), and the other files under [`application/`](application/README.md) name machines, knobs, and falsifiers so the *mapping* can be tested by people who already have the right facilities.

They are not:

- a build sequence,
- a pressure or electrical rating,
- a materials-handling SOP,
- or a claim that a described cell has been run.

If a number appears (bar, µs, nm, kA), it is a **class** from the analysis or from earlier concept notes, not a qualified set point.

---

## What we are not going to do

We will not strip the public science or the configuration mapping. We will not dress this as forbidden knowledge. The honest correction, if you already cloned an earlier commit, is this file and the hazard boxes on the application pages.

If you need a procedure, write one under a real safety program. Do not copy these notes into a lab notebook as “the protocol.”
