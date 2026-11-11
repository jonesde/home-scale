# Checks for library/skin-effect.md and library/electrical-resistivity.md (batch 1-A).
# Meant to be merged into analysis/computed_checks.py. Uses K_B, H_PLANCK, MU_0, check,
# exp, log, pi, sqrt from that module. Needs one extra stdlib name, erfc, and three
# local constants / helpers defined below.

from math import erfc  # not yet imported in computed_checks.py

E_CHARGE = 1.602176634e-19  # C (exact)
C_LIGHT = 299792458.0  # m/s (exact)


def skin_depth(rho_ohm_m: float, f_hz: float, mu_r: float = 1.0) -> float:
    """Steady sinusoidal skin depth sqrt(rho / (pi f mu0 mu_r)), in metres."""
    return sqrt(rho_ohm_m / (pi * f_hz * MU_0 * mu_r))


def erfc_inverse(y: float) -> float:
    """x such that erfc(x) = y, by bisection on 0..5."""
    lo, hi = 0.0, 5.0
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if erfc(mid) > y:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


RHO_CU_IACS = 1.7241e-8  # ohm m, NBS Handbook 100
RHO_CU = 1.678e-8  # ohm m at 293 K, Matula 1979
RHO_AG = 1.587e-8  # ohm m at 293 K, Matula 1979
RHO_AL = 2.650e-8  # ohm m at 293 K, Desai et al. 1984
RHO_STEEL_1020 = 15.90e-8  # ohm m, IEEE Std 80 Table 1
D_CU = RHO_CU_IACS / MU_0  # magnetic diffusivity of IACS copper, m^2/s

# --- library/skin-effect.md ---------------------------------------------------
_SKIN = "library/skin-effect.md §4.3"
check(_SKIN, "exp(-4): amplitude left at four skin depths", exp(-4), 0.018)
check(_SKIN, "IACS conductivity from 1.7241 microohm cm (S/m)", 1 / RHO_CU_IACS, 5.80e7, 0.002)
# Steady table, Cu IACS
check(_SKIN, "Cu IACS, 50 Hz (mm)", skin_depth(RHO_CU_IACS, 50) * 1e3, 9.35, 0.005)
check(_SKIN, "Cu IACS, 60 Hz (mm)", skin_depth(RHO_CU_IACS, 60) * 1e3, 8.53, 0.005)
check(_SKIN, "Cu IACS, 1 kHz (mm)", skin_depth(RHO_CU_IACS, 1e3) * 1e3, 2.09, 0.005)
check(_SKIN, "Cu IACS, 1 MHz (um)", skin_depth(RHO_CU_IACS, 1e6) * 1e6, 66.1, 0.005)
check(_SKIN, "Cu IACS, 1 GHz (um)", skin_depth(RHO_CU_IACS, 1e9) * 1e6, 2.09, 0.005)
# Steady table, pure Cu
check(_SKIN, "Cu pure, 50 Hz (mm)", skin_depth(RHO_CU, 50) * 1e3, 9.22, 0.005)
check(_SKIN, "Cu pure, 60 Hz (mm)", skin_depth(RHO_CU, 60) * 1e3, 8.42, 0.005)
check(_SKIN, "Cu pure, 1 kHz (mm)", skin_depth(RHO_CU, 1e3) * 1e3, 2.06, 0.005)
check(_SKIN, "Cu pure, 1 MHz (um)", skin_depth(RHO_CU, 1e6) * 1e6, 65.2, 0.005)
check(_SKIN, "Cu pure, 1 GHz (um)", skin_depth(RHO_CU, 1e9) * 1e6, 2.06, 0.005)
# Steady table, Ag
check(_SKIN, "Ag, 50 Hz (mm)", skin_depth(RHO_AG, 50) * 1e3, 8.97, 0.005)
check(_SKIN, "Ag, 60 Hz (mm)", skin_depth(RHO_AG, 60) * 1e3, 8.19, 0.005)
check(_SKIN, "Ag, 1 kHz (mm)", skin_depth(RHO_AG, 1e3) * 1e3, 2.00, 0.005)
check(_SKIN, "Ag, 1 MHz (um)", skin_depth(RHO_AG, 1e6) * 1e6, 63.4, 0.005)
check(_SKIN, "Ag, 1 GHz (um)", skin_depth(RHO_AG, 1e9) * 1e6, 2.00, 0.005)
# Steady table, Al
check(_SKIN, "Al, 50 Hz (mm)", skin_depth(RHO_AL, 50) * 1e3, 11.6, 0.005)
check(_SKIN, "Al, 60 Hz (mm)", skin_depth(RHO_AL, 60) * 1e3, 10.6, 0.005)
check(_SKIN, "Al, 1 kHz (mm)", skin_depth(RHO_AL, 1e3) * 1e3, 2.59, 0.005)
check(_SKIN, "Al, 1 MHz (um)", skin_depth(RHO_AL, 1e6) * 1e6, 81.9, 0.005)
check(_SKIN, "Al, 1 GHz (um)", skin_depth(RHO_AL, 1e9) * 1e6, 2.59, 0.005)
# Published copper formulas, as a cross-check of the cited values
check(_SKIN, "65.2 mm/sqrt(f) coefficient for rho = 1.68e-8 (mm)", skin_depth(1.68e-8, 1.0) * 1e3, 65.2, 0.005)
check(_SKIN, "6.56e-2 f^-1/2 at 340 MHz (um; source 3.56)", 6.56e-2 / sqrt(340e6) * 1e6, 3.56, 0.005)
# Steel 1020
check(_SKIN, "steel 1020, mu_r 100, 60 Hz (mm)", skin_depth(RHO_STEEL_1020, 60, 100) * 1e3, 2.6, 0.02)
check(_SKIN, "steel 1020, mu_r 100, 1 kHz (mm)", skin_depth(RHO_STEEL_1020, 1e3, 100) * 1e3, 0.63, 0.02)
check(_SKIN, "steel 1020, mu_r 100, 1 MHz (um)", skin_depth(RHO_STEEL_1020, 1e6, 100) * 1e6, 20, 0.02)
check(_SKIN, "steel 1020, mu_r 1, 60 Hz (mm)", skin_depth(RHO_STEEL_1020, 60) * 1e3, 26, 0.02)
check(_SKIN, "steel 1020, mu_r 1, 1 kHz (mm)", skin_depth(RHO_STEEL_1020, 1e3) * 1e3, 6.3, 0.02)
check(_SKIN, "steel 1020, mu_r 1, 1 MHz (mm)", skin_depth(RHO_STEEL_1020, 1e6) * 1e3, 0.20, 0.02)
# Scaling with resistivity
check(_SKIN, "sqrt(10)", sqrt(10), 3.2, 0.02)
check(_SKIN, "Cu IACS, 200 kHz (mm)", skin_depth(RHO_CU_IACS, 2e5) * 1e3, 0.148, 0.005)
check(_SKIN, "10 x IACS resistivity, 200 kHz (mm)", skin_depth(10 * RHO_CU_IACS, 2e5) * 1e3, 0.47, 0.01)
check(_SKIN, "100 x IACS resistivity, 200 kHz (mm)", skin_depth(100 * RHO_CU_IACS, 2e5) * 1e3, 1.48, 0.005)
# Pulse conventions, in units of sqrt(D t)
check(_SKIN, "1/e point of erfc, 2 * erfc_inverse(1/e)", 2 * erfc_inverse(exp(-1)), 1.27, 0.005)
check(_SKIN, "flux-equivalent depth 2/sqrt(pi)", 2 / sqrt(pi), 1.13, 0.005)
check(_SKIN, "steady delta at f = 1/(2t), sqrt(2/pi)", sqrt(2 / pi), 0.80, 0.005)
check(_SKIN, "steady delta at f = 1/(2t) from the formula, over sqrt(D t)", skin_depth(RHO_CU_IACS, 1 / (2 * 1e-4)) / sqrt(D_CU * 1e-4), 0.80, 0.005)
check(_SKIN, "span of the four pulse rules, 2 / sqrt(2/pi)", 2 / sqrt(2 / pi), 2.5, 0.01)
check(_SKIN, "D of IACS copper (m2/s)", D_CU, 0.0137, 0.005)
check(_SKIN, "sqrt(D) of IACS copper (m s^-1/2)", sqrt(D_CU), 0.117, 0.005)
# Pulse table, IACS copper
for _t, _pub, _e, _flux, _steady, _f in (
    (1e-6, 0.23, 0.15, 0.13, 0.093, 500e3),
    (1e-4, 2.3, 1.5, 1.3, 0.93, 5e3),
    (2e-4, 3.3, 2.1, 1.9, 1.3, 2.5e3),
    (7e-4, 6.2, 3.9, 3.5, 2.5, 714),
):
    _root = sqrt(D_CU * _t) * 1e3  # mm
    check(_SKIN, f"pulse {_t:g} s, 2 sqrt(D t) (mm)", 2 * _root, _pub, 0.03)
    check(_SKIN, f"pulse {_t:g} s, 1/e of erfc (mm)", 2 * erfc_inverse(exp(-1)) * _root, _e, 0.03)
    check(_SKIN, f"pulse {_t:g} s, flux depth (mm)", 2 / sqrt(pi) * _root, _flux, 0.03)
    check(_SKIN, f"pulse {_t:g} s, steady delta at f = 1/(2t) (mm)", skin_depth(RHO_CU_IACS, 1 / (2 * _t)) * 1e3, _steady, 0.03)
    check(_SKIN, f"pulse {_t:g} s, half-period frequency (Hz)", 1 / (2 * _t), _f, 0.002)
check(_SKIN, "steady delta at 1 MHz below the smallest 1 us pulse figure (ratio)", skin_depth(RHO_CU_IACS, 1e6) / skin_depth(RHO_CU_IACS, 500e3), 0.71, 0.01)
# Field left at depth at the end of the pulse
check(_SKIN, "erfc at 3 mm after 0.2 ms", erfc(3e-3 / (2 * sqrt(D_CU * 2e-4))), 0.20, 0.03)
check(_SKIN, "erfc at 3 mm after 0.7 ms", erfc(3e-3 / (2 * sqrt(D_CU * 7e-4))), 0.49, 0.03)
check(_SKIN, "erfc at 4 mm after 0.2 ms", erfc(4e-3 / (2 * sqrt(D_CU * 2e-4))), 0.09, 0.03)
check(_SKIN, "erfc at 4 mm after 0.7 ms", erfc(4e-3 / (2 * sqrt(D_CU * 7e-4))), 0.36, 0.03)
# Velocity skin effect (Woods: lambda = coefficient * sqrt(a / V))
check(_SKIN, "worked case 18.3 mm at 500 m/s, coefficient 0.116 (mm)", 0.116 * sqrt(18.3e-3 / 500) * 1e3, 0.70, 0.01)
check(_SKIN, "worked case 18.3 mm at 500 m/s, coefficient 0.219 (mm)", 0.219 * sqrt(18.3e-3 / 500) * 1e3, 1.32, 0.01)
check(_SKIN, "transit time, 1 mm at 100 m/s (us)", 1e-3 / 100 * 1e6, 10, 0.001)
check(_SKIN, "transit time, 1 mm at 500 m/s (us)", 1e-3 / 500 * 1e6, 2, 0.001)
check(_SKIN, "2 lambda, 1 mm at 100 m/s (mm)", 2 * 0.116 * sqrt(1e-3 / 100) * 1e3, 0.73, 0.01)
check(_SKIN, "2 lambda, 1 mm at 500 m/s (mm)", 2 * 0.116 * sqrt(1e-3 / 500) * 1e3, 0.33, 0.01)
# Anomalous regime
check(_SKIN, "mean free path from rho*l = 6.8e-16 and rho = 1.68e-8 (nm)", 6.8e-16 / 1.68e-8 * 1e9, 40, 0.02)
check(_SKIN, "delta / l at 340 MHz (3.56 um / 39 nm)", 3.56e-6 / 39e-9, 91, 0.01)
check(_SKIN, "frequency where delta = 39 nm, pure Cu (THz)", RHO_CU / (pi * MU_0 * (39e-9) ** 2) / 1e12, 2.8, 0.02)
check(_SKIN, "frequency where delta = 39 nm, IACS Cu (THz)", RHO_CU_IACS / (pi * MU_0 * (39e-9) ** 2) / 1e12, 2.9, 0.02)
check(_SKIN, "omega tau at 2.9 THz, tau = 2.46e-14 s", 2 * pi * 2.9e12 * 2.46e-14, 0.45, 0.02)
check(_SKIN, "Cu IACS, 0.7 kHz (mm)", skin_depth(RHO_CU_IACS, 700) * 1e3, 2.5, 0.02)
check(_SKIN, "Cu IACS, 4 kHz (mm)", skin_depth(RHO_CU_IACS, 4e3) * 1e3, 1.0, 0.05)
check(_SKIN, "delta / l at 0.7 kHz (l = 39 nm)", skin_depth(RHO_CU_IACS, 700) / 39e-9, 6.4e4, 0.02)
check(_SKIN, "delta / l at 4 kHz (l = 39 nm)", skin_depth(RHO_CU_IACS, 4e3) / 39e-9, 2.7e4, 0.02)
# Optical depths
check(_SKIN, "Ag intensity depth at 495.9 nm, k = 3.093 (nm)", 495.9 / (4 * pi * 3.093), 12.8, 0.005)
check(_SKIN, "Al intensity depth at 516.6 nm, k = 6.2418 (nm)", 516.6 / (4 * pi * 6.2418), 6.6, 0.01)
check(_SKIN, "Ag amplitude depth at 495.9 nm (nm)", 495.9 / (2 * pi * 3.093), 25.5, 0.005)
check(_SKIN, "Al amplitude depth at 516.6 nm (nm)", 516.6 / (2 * pi * 6.2418), 13.2, 0.005)
check(_SKIN, "frequency of 495.9 nm light (THz)", C_LIGHT / 495.9e-9 / 1e12, 604, 0.002)
check(_SKIN, "steady formula for Ag at 495.9 nm (nm)", skin_depth(RHO_AG, C_LIGHT / 495.9e-9) * 1e9, 2.6, 0.02)
check(_SKIN, "steady formula over measured amplitude depth, Ag", skin_depth(RHO_AG, C_LIGHT / 495.9e-9) * 1e9 / 25.5, 0.10, 0.03)
# Plasma periods h / (hbar omega_p)
check(_SKIN, "plasma period, Ag 9.01 eV (fs)", H_PLANCK / (9.01 * E_CHARGE) * 1e15, 0.46, 0.01)
check(_SKIN, "plasma period, Cu 10.83 eV (fs)", H_PLANCK / (10.83 * E_CHARGE) * 1e15, 0.38, 0.01)
check(_SKIN, "plasma period, Al 14.98 eV (fs)", H_PLANCK / (14.98 * E_CHARGE) * 1e15, 0.28, 0.02)
_SKIN6 = "library/skin-effect.md §4.5–§4.6"
check(_SKIN6, "published pulse depth over steady half-period depth at 100 us (2.3 / 0.93)", 2.3 / 0.93, 2.5, 0.02)
check(_SKIN6, "l / delta at 340 MHz", 39e-9 / 3.56e-6, 1e-2, 0.15)

# --- library/electrical-resistivity.md ------------------------------------------
_RES = "library/electrical-resistivity.md §4.3"
# Temperature coefficients: slope between the 273 K and 300 K rows over the 293 K value
check(_RES, "temperature coefficient, Ag (1/K)", (1.629 - 1.467) / (300 - 273.15) / 1.587, 0.0038, 0.02)
check(_RES, "temperature coefficient, Cu (1/K)", (1.725 - 1.543) / (300 - 273.15) / 1.678, 0.0040, 0.02)
check(_RES, "temperature coefficient, W (1/K)", (5.44 - 4.82) / (300 - 273) / 5.28, 0.0043, 0.02)
check(_RES, "temperature coefficient, Al (1/K)", (2.733 - 2.417) / (300 - 273) / 2.650, 0.0044, 0.02)
check(_RES, "temperature coefficient, Fe (1/K)", (9.98 - 8.57) / (300 - 273) / 9.61, 0.0054, 0.02)
check(_RES, "temperature coefficient, Ni (1/K)", (7.20 - 6.16) / (300 - 273) / 6.93, 0.0056, 0.02)
check(_RES, "conductivity of pure Cu at 293 K (S/m)", 1 / RHO_CU, 5.96e7, 0.002)
check(_RES, "pure Cu conductivity above IACS (fraction)", RHO_CU_IACS / RHO_CU - 1, 0.027, 0.03)
check(_RES, "AISI 1010 at 14.3 microohm cm over IACS Cu", 14.3 / 1.7241, 8.3, 0.01)
check(_RES, "steel 1020 at 15.90 microohm cm over IACS Cu", 15.90 / 1.7241, 9.2, 0.01)
# Melting ratios
check(_RES, "liquid/solid at Tm, Cu (tabulated 2.07)", 21.01 / 10.171, 2.07, 0.005)
check(_RES, "liquid/solid at Tm, Ag (tabulated 2.06)", 17.30 / 8.415, 2.06, 0.005)
check(_RES, "liquid/solid at Tm, Al", 24.77 / 10.565, 2.34, 0.005)
check(_RES, "liquid/solid at Tm, Al, uncorrected solid", 24.77 / 10.74, 2.31, 0.005)
check(_RES, "liquid/solid at Tm, Ni", 82.2 / 60.2, 1.37, 0.005)
check(_RES, "liquid/solid at Tm, Fe", 135.2 / 128.2, 1.055, 0.002)
check(_RES, "liquid/solid at Tm, W", 131 / 120.8, 1.08, 0.005)
check(_RES, "exploding wire liquid/solid, Cu", 18.9 / 9.9, 1.91, 0.005)
check(_RES, "exploding wire liquid/solid, Ag", 15.9 / 8.6, 1.85, 0.005)
check(_RES, "exploding wire liquid/solid, Al", 23.1 / 11.2, 2.06, 0.005)
check(_RES, "exploding wire liquid/solid, Ni", 79.6 / 59.2, 1.34, 0.005)
check(_RES, "exploding wire liquid/solid, Fe", 123.6 / 119.2, 1.04, 0.005)
check(_RES, "exploding wire liquid/solid, W", 116.1 / 90.3, 1.29, 0.005)
# Lorenz ratio against the Sommerfeld value 2.443e-8
check(_RES, "Na Lorenz ratio below L0 (fraction)", 1 - 2.12 / 2.443, 0.13, 0.05)
check(_RES, "Nb Lorenz ratio above L0 (fraction)", 2.90 / 2.443 - 1, 0.19, 0.05)
check(_RES, "Cu Lorenz ratio (tertiary) below L0 (fraction)", 1 - 2.23 / 2.443, 0.09, 0.05)
# Specific action, A^2 s/mm^4 to 1e16 A^2 s/m^4 (factor 1e12)
for _metal, _raw, _quoted in (
    ("Cu melting begins", 80492, 8.05),
    ("Cu melting complete", 94228, 9.42),
    ("Cu burst", 173000, 17.3),
    ("Ag melting begins", 61682, 6.17),
    ("Ag melting complete", 71771, 7.18),
    ("Al melting begins", 25238, 2.52),
    ("Al melting complete", 32035, 3.20),
    ("Al burst", 65776, 6.58),
    ("W melting begins", 24270, 2.43),
    ("W melting complete", 27831, 2.78),
    ("Ni melting begins", 17233, 1.72),
    ("Ni melting complete", 21156, 2.12),
    ("Fe melting begins", 12806, 1.28),
    ("Fe melting complete", 14681, 1.47),
    ("Fe burst", 36105, 3.61),
):
    check(_RES, f"specific action, {_metal} (1e16 A2 s/m4)", _raw * 1e12 / 1e16, _quoted, 0.003)
check(_RES, "melt-onset action, Cu over Fe", 80492 / 12806, 6.3, 0.01)
check(_RES, "burst over melt-onset action, Cu", 173000 / 80492, 2.1, 0.03)
check(_RES, "burst over melt-onset action, Al", 65776 / 25238, 2.6, 0.02)
check(_RES, "burst over melt-onset action, Fe", 36105 / 12806, 2.8, 0.02)
# Time to melt onset at 1e10 A/m2, and current density for a given time
check(_RES, "time to melt onset at 1e10 A/m2, Cu (ms)", 8.05e16 / 1e10**2 * 1e3, 0.81, 0.01)
check(_RES, "time to melt onset at 1e10 A/m2, Al (ms)", 2.52e16 / 1e10**2 * 1e3, 0.25, 0.01)
check(_RES, "time to melt onset at 1e10 A/m2, Fe (ms)", 1.28e16 / 1e10**2 * 1e3, 0.13, 0.02)
check(_RES, "J for melt onset in 0.2 ms, Cu (kA/mm2)", sqrt(8.05e16 / 2e-4) / 1e9, 20, 0.01)
check(_RES, "J for melt onset in 0.7 ms, Cu (kA/mm2)", sqrt(8.05e16 / 7e-4) / 1e9, 11, 0.03)
check(_RES, "J for melt onset in 0.2 ms, Fe (kA/mm2)", sqrt(1.28e16 / 2e-4) / 1e9, 8.0, 0.01)
check(_RES, "J for melt onset in 0.7 ms, Fe (kA/mm2)", sqrt(1.28e16 / 7e-4) / 1e9, 4.3, 0.01)
# Adiabatic fusing model, IEEE Std 80 constants for steel 1020
check(
    _RES,
    "adiabatic action to fuse, steel 1020, 20 C to 1510 C (A2 s/m4)",
    3.28e6 / (0.00160 * RHO_STEEL_1020) * log((605 + 1510) / (605 + 20)),
    1.57e16,
    0.005,
)
check(_RES, "steel model over measured iron wire (1.57 / 1.28)", 1.57 / 1.28 - 1, 0.23, 0.03)
check(_RES, "Cu model figure over wire value (8.33 / 8.05)", 8.33 / 8.05 - 1, 0.03, 0.2)
check(_RES, "Al model figure over wire value (2.83 / 2.52)", 2.83 / 2.52 - 1, 0.12, 0.05)
# Size effect and powders
check(_RES, "Fuchs-Sondheimer surface term at d = mean free path, p = 0", 3 / 8, 0.375, 0.001)
check(_RES, "Al powder residual over pure Al (1.6e-5 / 2.650e-8)", 1.6e-5 / 2.650e-8, 600, 0.02)
check(_RES, "Fe powder residual over pure Fe (2.3e-6 / 9.61e-8)", 2.3e-6 / 9.61e-8, 24, 0.02)
check(_RES, "Ni powder residual over pure Ni (1.0e-6 / 6.93e-8)", 1.0e-6 / 6.93e-8, 14, 0.04)
check(_RES, "unreduced Cu compact over bulk, low (1e4 ohm m)", 1e4 / RHO_CU, 6e11, 0.01)
check(_RES, "unreduced Cu compact over bulk, high (1e5 ohm m)", 1e5 / RHO_CU, 6e12, 0.01)
check(_RES, "reduced Cu compact over bulk, plot floor 1e-6 ohm m", 1e-6 / RHO_CU, 60, 0.01)
check(_RES, "reduced Cu compact over bulk, plot floor 1e-5 ohm m", 1e-5 / RHO_CU, 600, 0.01)

# --- application/EM-CSAM.md §2.2 (numbers not already quoted in the two effect files) ---
_CSAM = "application/EM-CSAM.md §2.2"
check(_CSAM, "10 um particle radius over steady delta at 1 MHz", 10e-6 / skin_depth(RHO_CU_IACS, 1e6), 0.15, 0.02)
check(_CSAM, "10 um particle radius over steady delta at 2.5 kHz (quoted as under 0.01)", 10e-6 / skin_depth(RHO_CU_IACS, 2.5e3), 0.0076, 0.02)
check(_CSAM, "delta / l at 4 kHz, quoted as about 3e4", skin_depth(RHO_CU_IACS, 4e3) / 39e-9, 3e4, 0.12)
check(_CSAM, "delta / l at 0.7 kHz, quoted as about 6e4", skin_depth(RHO_CU_IACS, 700) / 39e-9, 6e4, 0.08)

# --- application/EM-CSAM-Pitch.md (pulse depths quoted in the state palette and annex)
_PITCH = "application/EM-CSAM-Pitch.md"
check(_PITCH, "2 sqrt(D t) in Cu at 1 us (mm)", 2 * sqrt(D_CU * 1e-6) * 1e3, 0.23)
check(_PITCH, "2 sqrt(D t) in Cu at 100 us (mm)", 2 * sqrt(D_CU * 100e-6) * 1e3, 2.3)
check(_PITCH, "2 sqrt(D t) in Cu at 0.2 ms (mm)", 2 * sqrt(D_CU * 0.2e-3) * 1e3, 3.3)
check(_PITCH, "2 sqrt(D t) in Cu at 0.7 ms (mm)", 2 * sqrt(D_CU * 0.7e-3) * 1e3, 6.2)
check(_PITCH, "1.13 sqrt(D t) in Cu at 1 us, low end of the quoted range (mm)", 1.13 * sqrt(D_CU * 1e-6) * 1e3, 0.13)
check(_PITCH, "1.13 sqrt(D t) in Cu at 100 us, low end of the quoted range (mm)", 1.13 * sqrt(D_CU * 100e-6) * 1e3, 1.3)
