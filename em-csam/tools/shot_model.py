#!/usr/bin/env python3
"""EM-CSAM shot model: capacitor bank -> half-bridge -> series inductor -> rails -> moving slug.

Standard library only. This is a first-order planning tool, not a validated simulator.
Every default below is an ASSUMPTION until measured (see em-csam/TestPlan.md):

  esr       25 mOhm per 4700 uF can at 1-10 kHz (Nichicon publishes no HF ESR)
  r_fixed   4 mOhm  (conducting FET group + bars/joints + air-core coil)
  r_rail    34 mOhm/m for both rails together (skin-limited, ~1 kHz pulse)
  lprime    0.4 uH/m (plausible range 0.3-0.5 for flat side-by-side rails)
  r_slug    0.2 mOhm (a well-sintered slug; loose paste is orders of magnitude higher)
  v_diode   1.3 V (LS body diodes carrying the freewheel tail)
  no friction, no wall drag, no vapor pressure, rigid slug

Circuit model
  While the bank voltage is positive and the high-side group is on:
      Vc - I*(ESR + R) - I*(L' + 2M')*v - B*gap*v = L * dI/dt
  Afterwards the load current freewheels through the low-side diodes:
      -Vd - I*R - I*(L' + 2M')*v - B*gap*v = L * dI/dt
  Force on the slug:  F = (L'/2 + M') * I^2 + B * gap * I
  with L = L0 + (L' + 2M') * x.

Usage
  python3 shot_model.py tables      # every table quoted in the docs
  python3 shot_model.py shot --cans 6 --volts 18 --l0 1e-6 --mass 1e-6 --b 0.8
  python3 shot_model.py selftest
"""
import argparse
import math
import sys

MU0 = 4e-7 * math.pi

# IRFP4568 thermal model (Foster terms from an older datasheet revision; approximate).
FOSTER_R = (0.06336, 0.11088, 0.11484)      # K/W
FOSTER_TAU = (0.000278, 0.005836, 0.053606)  # s

# Action to melt onset from room temperature, A^2 s / m^4 (Tucker & Toth, SAND-75-0041).
ACTION_MELT = {"Cu": 8.0e16, "Al": 2.5e16, "Fe": 1.3e16, "Zn": 1.1e16, "Sn": 1.7e15}
DENSITY = {"Cu": 8960, "Al": 2700, "Fe": 7870, "Zn": 7140, "Sn": 7300}
# Cold-spray critical velocity windows at 20 um, m/s (Schmidt et al. 2009). Fe uses the 316L window.
V_CRIT = {"Sn": (160, 180), "Zn": (360, 380), "Cu": (460, 500), "Al": (620, 660), "Fe": (700, 750)}
# (density, cp, T_melt K, indicative tensile strength Pa) for the Schmidt 2006 formula.
# Strengths are picked inside handbook ranges so the formula lands in the published windows;
# use the function for the trend with temperature, not for absolute values.
SCHMIDT = {"Cu": (8960, 385, 1356, 210e6), "Al": (2700, 900, 933, 120e6), "Zn": (7140, 388, 693, 130e6),
           "Sn": (7300, 228, 505, 20e6), "316L": (7990, 500, 1700, 560e6), "Ti": (4500, 520, 1941, 440e6)}

# Copper slug state thresholds, J/kg from 20 C.
E_MELT_ONSET, E_MOLTEN, E_BOIL_ONSET, E_VAPOR = 0.45e6, 0.65e6, 1.4e6, 6.1e6


# ---------------------------------------------------------------- geometry helpers
def kerrisk(s, w, h):
    """High-frequency inductance gradient of rectangular rails, uH/m (Kerrisk).
    s = rail separation, w = rail width away from the bore, h = rail height facing the bore."""
    f1 = 1 + 3.397 * (w / h) - 0.06603 * (w / h) * (s / h)
    f2 = 1.0077 + 2.7437 * (s / h) + 0.02209 * (w / h) + 0.2637 * (s / h) * (w / h)
    return (0.4406 - 0.0777 * math.log(f1)) * math.log(f2)


def _ellip_k(k):
    a, b = 1.0, math.sqrt(1 - k * k)
    for _ in range(40):
        a, b = (a + b) / 2, math.sqrt(a * b)
    return math.pi / (2 * a)


def coplanar(s, w):
    """Inductance gradient of two thin coplanar strips (width w, gap s), uH/m."""
    k = s / (s + 2 * w)
    return MU0 * _ellip_k(k) / _ellip_k(math.sqrt(1 - k * k)) * 1e6


def gap_flux(spread, s=0.5e-3, height=0.0, x_in=None, n=400):
    """Flux per metre crossing the bore gap per ampere, uH/m, from a strip pair carrying +/-I
    uniformly over a width `spread`, at `height` above the bore plane.
    height=0 with x_in at the gap edge is the rails themselves; height>0 is one augmenting turn-pair."""
    a = s / 2
    x_in = a + 1e-9 if x_in is None else x_in
    tot = 0.0
    for i in range(n):
        x0 = x_in + (i + 0.5) * spread / n
        tot += math.log(((x0 + a) ** 2 + height ** 2) / ((x0 - a) ** 2 + height ** 2))
    return MU0 / (2 * math.pi) * tot / n * 1e6


def skin_depth(rho, f):
    return math.sqrt(rho / (math.pi * f * MU0))


def schmidt_vcrit(material, temp_k=293.0):
    rho, cp, tm, su = SCHMIDT[material]
    t = min(temp_k, tm)
    return math.sqrt(1.2 * 4 * su * (1 - (t - 293.0) / (tm - 293.0)) / rho + 0.3 * cp * (tm - t))


def slug_state(e_per_kg):
    if e_per_kg < E_MELT_ONSET:
        return "solid"
    if e_per_kg < E_MOLTEN:
        return "melting"
    if e_per_kg < E_BOIL_ONSET:
        return "molten"
    if e_per_kg < E_VAPOR:
        return "boiling"
    return "vapor"


# ---------------------------------------------------------------- the shot
def shot(cans=6, c_can=4700e-6, esr=0.025, volts=18.0, l0=1e-6, mass=1e-6, lprime=0.4e-6,
         r_fixed=0.004, r_rail=0.034, r_slug=0.0002, b=0.0, b_start=0.02, gap=0.5e-3,
         maug=0.0, r_aug=0.0, barrel=0.1, v_diode=1.3, t_on=None, fets=4, rds_hot=0.011,
         dt=2e-8, t_max=8e-3):
    """Integrate one shot. Returns a dict of results in SI units."""
    c = cans * c_can
    r_esr = esr / cans
    lgrad = lprime + 2 * maug
    t = i = x = v = 0.0
    vc = volts
    ipk = act = e_slug = e_res = e_diode = 0.0
    hs = [0.0, 0.0, 0.0]
    ls = [0.0, 0.0, 0.0]
    hs_pk = ls_pk = 0.0
    exited = False
    i_exit = 0.0
    t_exit = None
    t_bank_end = None
    while t < t_max:
        inductance = l0 + lgrad * x
        r = r_fixed + r_aug + r_rail * x + r_slug
        bfield = b if x >= b_start else 0.0
        emf = i * lgrad * v + bfield * gap * v
        on = vc > 0 and (t_on is None or t < t_on)
        if on:
            di = (vc - i * (r_esr + r) - emf) / inductance * dt
            vc -= i / c * dt
            e_res += i * i * (r_esr + r) * dt
            p_hs, p_ls = (i / fets) ** 2 * rds_hot, 0.0
        else:
            if t_bank_end is None:
                t_bank_end = t
            di = (-v_diode - i * r - emf) / inductance * dt
            e_res += i * i * r * dt
            e_diode += i * v_diode * dt
            p_hs, p_ls = 0.0, (i / fets) * v_diode
        i = max(i + di, 0.0)
        force = (lprime / 2 + maug) * i * i + bfield * gap * i
        v += force / mass * dt
        x += v * dt
        act += i * i * dt
        e_slug += i * i * r_slug * dt
        ipk = max(ipk, i)
        for k in range(3):
            hs[k] += (p_hs * FOSTER_R[k] - hs[k]) / FOSTER_TAU[k] * dt
            ls[k] += (p_ls * FOSTER_R[k] - ls[k]) / FOSTER_TAU[k] * dt
        hs_pk, ls_pk = max(hs_pk, sum(hs)), max(ls_pk, sum(ls))
        t += dt
        if x >= barrel and not exited:
            exited, i_exit, t_exit = True, i, t
            break
        if i == 0.0 and t > 1e-4:
            break
    l_end = l0 + lgrad * min(x, barrel)
    ke = 0.5 * mass * v * v
    e_bank = 0.5 * c * (volts ** 2 - vc * abs(vc))
    return {
        "v": v, "exited": exited, "t_exit": t_exit, "t_bank_end": t_bank_end, "i_peak": ipk,
        "i_exit": i_exit, "e_muzzle": 0.5 * l_end * i_exit ** 2, "action": act, "ke": ke,
        "e_slug": e_slug, "e_slug_per_kg": e_slug / mass, "state": slug_state(e_slug / mass),
        "v_bank_end": vc, "charge": c * (volts - vc), "charge_avail": c * volts,
        "e_stored": 0.5 * c * volts ** 2, "e_res": e_res, "e_diode": e_diode,
        "i_per_fet": ipk / fets, "dtj_hs": hs_pk, "dtj_ls": ls_pk,
        "balance": e_bank - (e_res + e_diode + ke + 0.5 * l_end * i ** 2),
    }


def peak_into_short(**kw):
    """Peak current with the rails shorted by a fixed strap (a very heavy slug)."""
    kw = dict(kw)
    kw.update(mass=1.0, r_slug=0.0)
    return shot(**kw)["i_peak"]


def fmt_shot(r):
    exit_txt = "exits" if r["exited"] else "current ends in barrel"
    return (f"v={r['v']:5.0f} m/s  Ipk={r['i_peak']:5.0f} A ({r['i_per_fet']:3.0f}/FET)  "
            f"Iexit={r['i_exit']:5.0f} A  muzzle={r['e_muzzle']:4.2f} J  KE={r['ke'] * 1e3:5.0f} mJ  "
            f"slug={r['e_slug_per_kg'] / 1e6:4.2f} MJ/kg ({r['state']})  dTj={r['dtj_hs']:3.0f} K  {exit_txt}")


# ---------------------------------------------------------------- tables for the docs
def tables():
    print("## 1. Bank charge and energy (4700 uF cans)")
    for cans in (2, 6, 12):
        for volts in (30, 48, 55):
            c = cans * 4700e-6
            print(f"  {cans:2d} cans at {volts} V: C={c * 1e3:5.1f} mF  Q={c * volts:4.2f} C  E={0.5 * c * volts ** 2:5.1f} J")

    print("\n## 2. Charge a constant-current shot needs, Q = 2*sqrt(m*s/L'), barrel 100 mm")
    for mass, lp in ((2e-6, 0.6e-6), (1e-6, 0.4e-6), (0.5e-6, 0.4e-6), (0.25e-6, 0.4e-6), (1e-6, 0.3e-6)):
        print(f"  m={mass * 1e6:4.2f} mg  L'={lp * 1e6:.1f} uH/m:  Q={2 * math.sqrt(mass * 0.1 / lp):4.2f} C")

    print("\n## 3. Action, loss and efficiency (constant current, 100 mm, L'=0.4 uH/m)")
    for mass, vel in ((1e-6, 300), (2e-6, 300), (2e-6, 500), (0.25e-6, 400)):
        action = 2 * mass * vel / 0.4e-6
        for r in (0.010, 0.020):
            print(f"  m={mass * 1e6:4.2f} mg v={vel}: action={action:5.0f} A2s  I_flat={math.sqrt(action * vel / 0.2):5.0f} A  "
                  f"R={r * 1e3:2.0f} mOhm: loss={r * action:5.1f} J  efficiency={0.5 * mass * vel ** 2 / (r * action) * 100:4.2f} %")

    print("\n## 4. Inductance gradient estimates, uH/m (gap 0.5 mm)")
    for w in (2e-3, 4e-3, 8e-3, 12e-3):
        print(f"  thin coplanar strips, width {w * 1e3:4.1f} mm: {coplanar(0.5e-3, w):.3f}")
    for w, h in ((0.5, 0.5), (2, 0.5), (4, 0.5), (8, 0.5), (8, 1.0), (8, 1.5)):
        print(f"  Kerrisk high-frequency, width {w:4.1f} mm, height {h:.1f} mm: {kerrisk(0.5, w, h):.3f}")
    for spread in (0.2e-3, 0.5e-3, 1e-3, 2e-3, 4e-3):
        print(f"  flux crossing the gap, current spread {spread * 1e3:.1f} mm into the rail: {gap_flux(spread):.3f}")

    print("\n## 5. Augmenting turn-pair coupling M', uH/m (4 mm strip from the gap edge)")
    for height in (0.5e-3, 0.75e-3, 1.0e-3, 1.5e-3, 2.0e-3, 3.0e-3):
        print(f"  {height * 1e3:4.2f} mm above the bore plane: {gap_flux(4e-3, height=height, x_in=0.25e-3):.3f}")

    print("\n## 6. Skin depth, mm")
    for name, rho in (("copper", 1.72e-8), ("aluminium 6101", 3.0e-8), ("slug at 1e-6 ohm-m", 1e-6), ("slug at 1e-5 ohm-m", 1e-5)):
        print(f"  {name:20s} " + "  ".join(f"{f / 1e3:g} kHz: {skin_depth(rho, f) * 1e3:6.3f}" for f in (1e3, 2e4, 2e5, 1e6)))

    print("\n## 7. Peak current into a shorted barrel, A per volt (sets the voltage ceiling for 4+4 FETs = 1.4 kA)")
    for cans, l0 in ((6, 2e-6), (6, 1e-6), (2, 2e-6), (2, 1e-6)):
        for esr in (0.025, 0.015):
            apv = peak_into_short(cans=cans, l0=l0, esr=esr, volts=20.0) / 20.0
            print(f"  {cans} cans, {l0 * 1e6:.0f} uH, ESR {esr * 1e3:.0f} mOhm/can: {apv:5.1f} A/V -> 1.4 kA at {1400 / apv:4.1f} V; at 30 V: {apv * 30:5.0f} A")

    print("\n## 8. What the on-hand kit should reach (idealised solid slug)")
    cases = [
        ("2 cans 30 V 2 uH, plain, 1 mg", dict(cans=2, volts=30, l0=2e-6)),
        ("2 cans 30 V 2 uH, plain, 0.25 mg", dict(cans=2, volts=30, l0=2e-6, mass=0.25e-6)),
        ("6 cans 18 V 1 uH, plain, 1 mg", dict()),
        ("6 cans 18 V 1 uH, magnet 0.8 T, 1 mg", dict(b=0.8)),
        ("6 cans 18 V 1 uH, magnet 0.8 T, 0.5 mg", dict(b=0.8, mass=0.5e-6)),
        ("6 cans 18 V 1 uH, magnet 0.8 T, 0.25 mg", dict(b=0.8, mass=0.25e-6)),
        ("6 cans 22 V, 8 aug. turns, 1 mg", dict(volts=22, l0=2.6e-6, maug=0.35e-6, r_aug=0.006)),
        ("6 cans 22 V, 8 aug. turns + magnet, 1 mg", dict(volts=22, l0=2.6e-6, maug=0.35e-6, r_aug=0.006, b=0.8)),
        ("6 cans 22 V, 8 aug. turns + magnet, 0.5 mg", dict(volts=22, l0=2.6e-6, maug=0.35e-6, r_aug=0.006, b=0.8, mass=0.5e-6)),
        ("6 cans 30 V 1 uH, magnet, 1 mg, 6+6 FETs", dict(volts=30, b=0.8, fets=6)),
        ("6 cans 55 V 1 uH, magnet, 1 mg, 8+8 FETs", dict(volts=55, b=0.8, fets=8)),
    ]
    for name, kw in cases:
        print(f"  {name:44s} {fmt_shot(shot(**kw))}")

    print("\n## 9. Slug resistance window (6 cans 18 V 1 uH, magnet 0.8 T, 0.5 mg)")
    for r_slug in (0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.02, 0.1):
        r = shot(b=0.8, mass=0.5e-6, r_slug=r_slug)
        print(f"  R_slug={r_slug * 1e3:6.1f} mOhm: v={r['v']:4.0f} m/s  slug={r['e_slug'] :5.2f} J = {r['e_slug_per_kg'] / 1e6:5.2f} MJ/kg ({r['state']})")

    print("\n## 10. Action margin: melt-onset velocity per mm of solid slug vs cold-spray critical velocity (L'=0.45)")
    for mat in ("Cu", "Al", "Zn", "Fe", "Sn"):
        vmax = ACTION_MELT[mat] * 1e-3 * 0.45e-6 / (2 * DENSITY[mat])
        lo, hi = V_CRIT[mat]
        print(f"  {mat}: melt onset at {vmax:5.0f} m/s per mm of slug; critical velocity {lo}-{hi}; margin {vmax / ((lo + hi) / 2):4.2f}")

    print("\n## 11. Critical velocity vs particle temperature (Schmidt 2006 formula, indicative)")
    for mat in ("Sn", "Zn", "Cu", "Al", "316L", "Ti"):
        tm = SCHMIDT[mat][2]
        temps = [293, 293 + 0.25 * (tm - 293), 293 + 0.5 * (tm - 293), 293 + 0.75 * (tm - 293)]
        print(f"  {mat:5s} " + "  ".join(f"{t - 273:4.0f} C: {schmidt_vcrit(mat, t):4.0f}" for t in temps))

    print("\n## 12. Sensitivity of the magnet case (6 cans 18 V 1 uH, 0.5 mg) to the assumptions")
    for name, kw in (("baseline", {}), ("L'=0.3", dict(lprime=0.3e-6)), ("L'=0.5", dict(lprime=0.5e-6)),
                     ("ESR 15 mOhm/can", dict(esr=0.015)), ("ESR 50 mOhm/can", dict(esr=0.05)),
                     ("magnet 0.6 T", dict(b=0.6)), ("no magnet", dict(b=0.0))):
        args = dict(b=0.8, mass=0.5e-6)
        args.update(kw)
        print(f"  {name:18s} {fmt_shot(shot(**args))}")


# ---------------------------------------------------------------- self test
def selftest():
    ok = True

    def check(name, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok = ok and good
        print(f"  {'ok ' if good else 'FAIL'} {name}: got {got:.4f}, want {want:.4f} +/- {tol}")

    print("Kerrisk fit against the values tabulated in LA-9401-MS (s = 10 mm):")
    check("h=20 w=5", kerrisk(10, 5, 20), 0.347, 0.002)
    check("h=2 w=1", kerrisk(10, 1, 2), 1.007, 0.002)
    check("h=w=s=10", kerrisk(10, 10, 10), 0.456, 0.002)
    print("Energy balance (bank energy = losses + kinetic + magnetic):")
    for name, kw in (("plain", {}), ("magnet", dict(b=0.8)), ("augmented", dict(maug=0.35e-6, r_aug=0.006, l0=2.6e-6, volts=22))):
        r = shot(**kw)
        check(f"{name} balance / stored", r["balance"] / r["e_stored"], 0.0, 0.01)
    print("Skin depth of copper at 200 kHz (mm):")
    check("copper 200 kHz", skin_depth(1.72e-8, 2e5) * 1e3, 0.148, 0.002)
    print("Required charge for the concept-table case (2 mg, 100 mm, 0.6 uH/m):")
    check("Q", 2 * math.sqrt(2e-6 * 0.1 / 0.6e-6), 1.155, 0.005)
    print("PASS" if ok else "FAILED")
    return 0 if ok else 1


def main(argv=None):
    p = argparse.ArgumentParser(description="EM-CSAM first-order shot model")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("tables", help="print every table quoted in the docs")
    sub.add_parser("selftest", help="check the helpers and the energy balance")
    s = sub.add_parser("shot", help="one shot with explicit parameters")
    s.add_argument("--cans", type=int, default=6)
    s.add_argument("--volts", type=float, default=18.0)
    s.add_argument("--l0", type=float, default=1e-6, help="series inductance incl. stray, H")
    s.add_argument("--mass", type=float, default=1e-6, help="slug mass, kg")
    s.add_argument("--lprime", type=float, default=0.4e-6, help="inductance gradient, H/m")
    s.add_argument("--esr", type=float, default=0.025, help="ESR per can, ohm")
    s.add_argument("--r-fixed", type=float, default=0.004)
    s.add_argument("--r-slug", type=float, default=0.0002)
    s.add_argument("--b", type=float, default=0.0, help="magnet field in the bore, T")
    s.add_argument("--b-start", type=float, default=0.02, help="where the magnet zone starts, m")
    s.add_argument("--maug", type=float, default=0.0, help="total augmenting coupling M', H/m")
    s.add_argument("--r-aug", type=float, default=0.0)
    s.add_argument("--barrel", type=float, default=0.1)
    s.add_argument("--t-on", type=float, default=None, help="high-side on-time, s (default: until the bank is empty)")
    s.add_argument("--fets", type=int, default=4, help="FETs per leg")
    a = p.parse_args(argv)
    if a.cmd == "tables":
        tables()
        return 0
    if a.cmd == "selftest":
        return selftest()
    if a.cmd == "shot":
        r = shot(cans=a.cans, volts=a.volts, l0=a.l0, mass=a.mass, lprime=a.lprime, esr=a.esr,
                 r_fixed=a.r_fixed, r_slug=a.r_slug, b=a.b, b_start=a.b_start, maug=a.maug,
                 r_aug=a.r_aug, barrel=a.barrel, t_on=a.t_on, fets=a.fets)
        print(fmt_shot(r))
        print(f"bank: {r['charge']:.2f} C used of {r['charge_avail']:.2f} C, {r['e_stored']:.1f} J stored, "
              f"ends at {r['v_bank_end']:.1f} V; resistive loss {r['e_res']:.1f} J; diode loss {r['e_diode']:.2f} J")
        return 0
    p.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
