# EM-CSAM with Micro Railgun Array

EM-CSAM stands for: electromagnetic cold spray additive manufacturing

People mostly think of the high current plasma based railgun designs. The difference between a large railgun and a micro one is the large one must vaporize the conductor to get enough energy to fire. With a micro railgun our goal is to NOT vaporize (or plasmize really) the material being accelerated.

It has to be scaled down far enough that it can pass sufficient current through the projectile material to reach target speeds without vaporizing the material. Less conductive materials can be fired, even saltwater, but with increasing heat from electrical resistance at the same current and of course requiring higher voltage to reach that current. For example, it could fire saltwater at 1000m/s, but it would have to vaporize it because the resistivity in saltwater is high enough that it will get too hot to stay in liquid form.

Copper should reach 1km/s without melting because of its high conductivity (under 500C vs copper melt at 1085C, so with room to spare for friction and other things not accounted for in simple formulas). Steel is another matter, even getting to 500m/s will liquify the steel. This means there is no point getting to higher velocities because the velocity required for cold sintering force is a moot point. What this really means is that steel and other similar lower conductivity material can be launched with some heat in it at a much lower speed to achieve a weak, or perhaps even strong, sintering bind. Steel could also be launched in liquid form and applied to sufficiently durable and/or progressively cooled surfaces.

There are still bore wear concerns, but not like with a plasma state railgun where it is difficult to not also vaporize part of the barrel as the projectile progresses down it in a plasma state.

The first question for practicality is whether the math is right, and how much current needs to be added for barrel friction, etc. After that there are questions of material feed and control and such. Being relatively low voltages and currents with fast solid state switching the circuits are pretty simple (like in PWM motor controllers). Voltage and wave shape gives us a lot of control over the current delivered to the circuit in small time windows (using current and/or pulse width to tune velocity). From there it borrows from the work done for other CSAM methods.

## Potential Powder, Carrier, and Rail Combinations

This is the result of a little AI analysis, progressing toward viability. These are just a few of the many potential viable combinations.

Note that these do not yet take into account contamination from the rail material, which depending on the energy level and rail materials is anywhere between a non-issue to an engineered part of the process (ie intentionally consume the rails to mix the desired output metal). In theory, rails can be made of any conductive material, even lower conductivity if you need/want loss/contamination as part of the process.

The general design philosophy is to use electrical flow and electro-magnetism to heat and accelerate material. For the simplest physical mechanics for a consumable or high-maintenance barrel surface, the simple 2 rail design wins. The frame or arm that moves it around, the material feeder, firing control circuitry and batteries, etc are all reusable. Many carrier fluids are reusable. The main weakness of the 2 rail type of linear accelerator is not a weakness, just a design variable.

The barrel should be made with an extremely simple/cheap process, and with simple/cheap materials... unless an exotic output is needed, then the barrel may cost significantly more but be consumed as part of the process meaning minimal material waste due to the loss of the most load-bearing machine component. That "waste" is just another part of the intended final material.

The downside is you can't do anything you want, only certain combinations of materials are viable.

It just so happens that there are some really useful outputs that can likely be produced fairly easily this way (relative to alternatives), and enable creating exotic alloys on the fly.

Here are those AI assisted examples (updated version with Grok 4.5):

---

Early process development focuses on matching metal powder, carrier fluid, and rail material. The rails are an active part of the system: they erode and contribute material to every deposit. This can be treated as contamination or as intentional alloying depending on the application.

### Highest-Priority Design Considerations

1. **Suspension Stability**
   Metal powders are dense and settle quickly. The carrier must keep particles suspended for the required working time. High viscosity or suitable thickeners are normally required.

2. **Gas Chemistry & Metal-Specific Sensitivity**
   Carrier decomposition products become the local atmosphere during the deposition flash. Carbon- and hydrogen-rich carriers can provide useful reducing conditions for many metals, but hydrogen is harmful to titanium and some other reactive metals. Match carrier chemistry to the powder’s sensitivities (H, C, O, N).

3. **Electrical Behavior & Rail Compatibility**
   The slurry must support clean current initiation and flow. Rail material erodes into the deposit on every shot—choose rails that are either compatible with the target chemistry or deliberately used as an alloying source.

### Recommended Starting Combinations – Home / Maker Labs

These prioritize lower reactivity, manageable handling, and good availability for early splat testing.

| Powder | Carrier | Preferred Rails | Notes |
|--------|---------|-----------------|-------|
| Copper | Light mineral oil, isoparaffinic solvent, or low-viscosity synthetic oil (± light graphite/graphene) | Copper or Aluminum | Best overall starting point. Forgiving electrical and thermal behavior; good chance of coherent metallic deposits. |
| Aluminum + Silicon | Isoparaffinic or light synthetic oil | Aluminum or Copper | Classic casting-alloy system. Silicon improves fluidity. Keep powder on the coarser side and use good ventilation. |
| Iron or low-alloy steel | Mineral oil or light synthetic oil (± controlled fine graphite) | Steel or Copper | Readily available and useful for learning consolidation and carbon control. Monitor carbon pickup. |

### Recommended Combinations – Industrial / Higher-Performance Targets

These can address more demanding materials but require industrial-level safety controls, powder handling, and process engineering.

| Powder | Carrier | Preferred Rails | Notes |
|--------|---------|-----------------|-------|
| Titanium | Low-hydrogen / carefully selected carrier (avoid glycerol-type hydrogen sources) | Specialized or coated rails | High value target, but hydrogen embrittlement and oxygen affinity make it significantly more difficult and hazardous. |
| Iron + Chromium (± carbon source) | Non-aqueous slurry with controlled carbon activity | Steel or Cr-containing rails | Aimed at wear-resistant hard-facing layers with chromium carbides. |
| Copper + higher graphene loading | Engineered carrier designed to protect graphene | Copper | High-conductivity composite target. Dispersion quality and graphene survival are the main challenges. |

**Development sequence recommendation**
Begin with the copper-based maker-lab systems. Once coherent deposits are repeatable, expand into aluminum–silicon and controlled iron systems. Attempt titanium and other highly reactive or high-performance combinations only after solid process control and appropriate facilities are in place.
