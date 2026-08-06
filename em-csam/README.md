# EM-CSAM with Micro Railgun Array

EM-CSAM stands for: electromagnetic cold spray additive manufacturing

People mostly think of the high current plasma based railgun designs. The difference between a large railgun and a micro one is the large one must vaporize the conductor to get enough energy to fire. With a micro railgun our goal is to NOT vaporize (or plasmize really) the material being accelerated.

It has to be scaled down far enough that it can pass sufficient current through the projectile material to reach target speeds without vaporizing the material. Less conductive materials can be fired, even saltwater, but with increasing heat from electrical resistance at the same current and of course requiring higher voltage to reach that current. For example, it could fire saltwater at 1000m/s, but it would have to vaporize it because the resistivity in saltwater is high enough that it will get too hot to stay in liquid form.

Copper should reach 1km/s without melting because of its high conductivity (under 500C vs copper melt at 1085C, so with room to spare for friction and other things not accounted for in simple formulas). Steel is another matter, even getting to 500m/s will liquify the steel. This means there is no point getting to higher velocities because the velocity required for cold sintering force is a moot point. What this really means is that steel and other similar lower conductivity material can be launched with some heat in it at a much lower speed to achieve a weak, or perhaps even strong, sintering bind. Steel could also be launched in liquid form and applied to sufficiently durable and/or progressively cooled surfaces.

There are still bore wear concerns, but not like with a plasma state railgun where it is difficult to not also vaporize part of the barrel as the projectile progresses down it in a plasma state.

The first question for practicality is whether the math is right, and how much current needs to be added for barrel friction, etc. After that there are questions of material feed and control and such. Being relatively low voltages and currents with fast solid state switching the circuits are pretty simple (like in PWM motor controllers). Voltage and wave shape gives us a lot of control over the current delivered to the circuit in small time windows (using current and/or pulse width to tune velocity). From there it borrows from the work done for other CSAM methods.

## 5 Advanced Powder & Carrier Blends for Local Manufacturing

This is the result of a little AI analysis, progressing toward viability. These are just a few of the many potential viable combinations.

Note that these do not yet take into account contamination from the rail material, which depending on the energy level and rail materials is anywhere between a non-issue to an engineered part of the process (ie intentionally consume the rails to mix the desired output metal). In theory, rails can be made of any conductive material, even lower conductivity if you need/want loss/contamination as part of the process.

The general design philosophy is to use electrical flow and electro-magnetism to heat and accelerate material. For the simplest physical mechanics for a consumable or high-maintenance barrel surface, the simple 2 rail design wins. The frame or arm that moves it around, the material feeder, firing control circuitry and batteries, etc are all reusable. Many carrier fluids are reusable. The main weakness of the 2 rail type of linear accelerator is not a weakness, just a design variable.

The barrel should be made with an extremely simple/cheap process, and with simple/cheap materials... unless an exotic output is needed, then the barrel may cost significantly more but be consumed as part of the process meaning minimal material waste due to the loss of the most load-bearing machine component. That "waste" is just another part of the intended final material.

The downside is you can't do anything you want, only certain combinations of materials are viable.

It just so happens that there are some really useful outputs that can likely be produced pretty easily this way, and enable creating exotic alloys on the fly.

Here are those AI assisted examples:

---

The table below details specific input materials, the resulting alloy matrix, and how the chemical mechanics operate during the deposition flash.

| Powder Blend (The Input)                     | Carrier Fluid (The Matrix)         | Target Material Produced          | The Chemical / Physical Mechanism                                                                                      |
| -------------------------------------------- | ---------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Pure Iron (Fe)**                           | CNT-Loaded Mineral Oil             | **High-Carbon Tool Steel**        | Carbon nanotubes dissolve directly into the liquid iron pool, forming martensitic steel phases.                        |
| **Pure Titanium (Ti)**                       | Ultra-Pure Glycerol (Zero-Residue) | **Commercial Pure (CP) Titanium** | Glycerol flash-vaporizes into hydrogen gas, acting as a local shielding atmosphere to prevent embrittlement.           |
| **Pure Aluminum (Al) + Silicon (Si) Powder** | Isoparaffinic Solvent Oil          | **Al-Si Cast-Grade Alloys**       | The zero-residue oil lifts the oxide layer via micro-cavitation, letting Al and Si fuse into low-shrinkage parts.      |
| **Iron (Fe) + Chromium (Cr) Powders**        | Non-aqueous CNT Slurry             | **Hard-Faced Tooling Steel**      | The carbon and chromium fuse on impact into Chromium Carbides (\(Cr_{3}C_{2}\)), forming high-wear agricultural edges. |
| **Pure Copper (Cu)**                         | Graphene-Loaded Light Oil          | **Graphene-Copper Composite**     | The plasma melts the copper while leaving graphene flakes intact, yielding ultra-high-conductivity wire.               |
The 3 Core Rules for Engineering Custom Blends

To discover additional variations at your workbench using your **Genmitsu CNC** to route the test channels, evaluate your raw ingredients against these metrics:

1. Viscosity vs. Particle Suspension (Stokes' Law)

Metal powder is highly dense (\(7.8\text{ g/cm}^3\) for iron) and will settle to the bottom of a thin fluid in minutes, clogging your syringe pump. Your carrier fluid must be thick enough to maintain an emulsion.

- _The Fix:_ Use high-viscosity synthetic oils or add a clean thickening agent like **Ethylcellulose** to your volatile carrier solvents to keep the powders in a permanent suspension.

2. The Boiling Point Differential

The carrier fluid's boiling point must be significantly lower than the metal powder's melting point.

- _Why:_ You want the fluid to flash-vaporize out of the way _before_ the metal particles completely melt. If the oil takes too long to vaporize, it will trap gas bubbles inside the cooling metal puddle, resulting in highly porous, structurally weak parts.

3. Oxygen Scavenging (The Self-Shielding Effect)

Since this is an at-home lab where an industrial vacuum chamber is impractical, your fluid can help fight oxidation. Using a carrier fluid high in hydrogen and carbon (like basic **Ethanol or Glycerol**) means that the plasma flash turns the fluid into a localized cloud of Hydrogen (\(H_{2}\)) and Carbon Monoxide (\(CO\)). These gases aggressively consume any stray oxygen in the immediate print zone, forming a protective barrier that prevents your metal from burning up.
