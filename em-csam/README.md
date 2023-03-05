## EM-CSAM with Micro Railgun Array

EM-CSAM stands for: electromagnetic cold spray additive manufacturing

People mostly think of the high current plasma based railgun designs. The difference between a large railgun and a micro one is the large one must vaporize the conductor to get enough energy to fire. With a micro railgun our goal is to NOT vaporize (or plasmize really) the material being accelerated.

It has to be scaled down far enough that it can pass sufficient current through the projectile material to reach target speeds without vaporizing the material. I don't know where that velocity vs scale point that avoids vaporizing different materials might be, but for this particular scenario there isn't much heat involved as long as the material being accelerated is very electrically conductive, similar conductivity to the metal rails also carrying the current.

Less conductive materials can be fired, even saltwater, but with increasing heat from electrical resistance at the same current and of course requiring higher voltage to reach that current. For example, it could fire saltwater at 1000m/s, but it would have to vaporize it because the resistivity in saltwater is high enough that it will get too hot to stay in liquid form.

There are still bore wear concerns, but not like with a plasma state railgun where it is difficult to not also vaporize part of the barrel as the projectile progresses down it in a plasma state.

The first question for practicality is whether the math is right, and how much current needs to be added for barrel friction, etc. After that there are questions of material feed and control and such. Being relatively low voltages and currents with fast solid state switching the circuits are pretty simple (like in PWM motor controllers). Voltage and wave shape gives us a lot of control over the current delivered to the circuit in small time windows (using current and/or pulse width to tune velocity). From there it borrows from the work done for other CSAM methods.
