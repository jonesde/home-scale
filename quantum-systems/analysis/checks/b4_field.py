# Checks for the light field batch (4): total-internal-reflection,
# faraday-rotation, cyclotron-resonance, aharonov-bohm.
# Executed inside analysis/computed_checks.py; uses check and math's pi from it.
# Names defined here carry a _F4 prefix so they cannot collide with constants
# defined by the other files in this directory.

import math as _F4_m

_F4_E = 1.602176634e-19  # C, exact
_F4_H = 6.62607015e-34  # J s, exact
_F4_ME = 9.1093837139e-31  # kg, CODATA 2022
_F4_EPS0 = 8.8541878188e-12  # F/m, CODATA 2022
_F4_C = 299792458.0  # m/s, exact
_F4_PC = 3.0857e16  # m


def _F4_theta_c(n1, n2=1.0):
    return _F4_m.degrees(_F4_m.asin(n2 / n1))


def _F4_depth(theta_deg, n1=1.50, n2=1.0):
    """Evanescent amplitude decay length in units of the vacuum wavelength."""
    s = _F4_m.sin(_F4_m.radians(theta_deg))
    return 1.0 / (2.0 * pi * _F4_m.sqrt(n1 * n1 * s * s - n2 * n2))


# --- library/total-internal-reflection.md -------------------------------------
_F4_TIR = "library/total-internal-reflection.md §4.3"
check(_F4_TIR, "critical angle, water 1.333 (deg)", _F4_theta_c(1.333), 48.6, rtol=0.005)
check(_F4_TIR, "critical angle, glass 1.50 (deg)", _F4_theta_c(1.50), 41.8, rtol=0.005)
check(_F4_TIR, "critical angle, polystyrene 1.49 (deg)", _F4_theta_c(1.49), 42.2, rtol=0.005)
check(_F4_TIR, "critical angle, diamond 2.42 (deg)", _F4_theta_c(2.42), 24.4, rtol=0.005)
check(_F4_TIR, "decay length at 60 deg (vacuum wavelengths)", _F4_depth(60), 0.19)
check(_F4_TIR, "decay length at 45 deg (vacuum wavelengths)", _F4_depth(45), 0.45)
check(_F4_TIR, "decay length at 45 deg, 633 nm (nm)", 633 * _F4_depth(45), 285)
check(_F4_TIR, "decay length at 42 deg (vacuum wavelengths)", _F4_depth(42), 1.85)
check(_F4_TIR, "42 deg minus the glass critical angle (deg)", 42 - _F4_theta_c(1.50), 0.2, rtol=0.06)
check(
    "analysis/fragments (total-internal-reflection:failure_mode:below-critical-angle)",
    "41.8 deg in rad",
    _F4_m.radians(41.8),
    0.730,
    rtol=0.005,
)

# --- library/faraday-rotation.md ----------------------------------------------
_F4_FAR = "library/faraday-rotation.md §4.3"
_F4_K = _F4_E**3 / (8 * pi**2 * _F4_EPS0 * _F4_ME**2 * _F4_C**3)  # 1/T
check(_F4_FAR, "45 deg path, TGG 131 rad/(T m), 1 T (mm)", (pi / 4) / 131 * 1e3, 6.0)
check(_F4_FAR, "45 deg path, TGG 38 rad/(T m), 1 T (cm)", (pi / 4) / 38 * 1e2, 2.1)
check(_F4_FAR, "45 deg path, silica 3.7 rad/(T m), 1 T (cm)", (pi / 4) / 3.7 * 1e2, 21)
check(_F4_FAR, "plasma prefactor in SI (1/T)", _F4_K, 2.63e-13, rtol=0.005)
check(_F4_FAR, "plasma prefactor against the tertiary 2.62e-13", _F4_K, 2.62e-13, rtol=0.01)
check(_F4_FAR, "prefactor in cm^-3 uG pc units", _F4_K * 1e6 * 1e-10 * _F4_PC, 0.81, rtol=0.01)
check(_F4_FAR, "wavelength squared at 150 MHz (m^2)", (_F4_C / 150e6) ** 2, 4.0)
check(_F4_FAR, "rotation at 150 MHz, RM 1 (rad)", 1 * (_F4_C / 150e6) ** 2, 4)
check(_F4_FAR, "rotation at 150 MHz, RM 4 (rad)", 4 * (_F4_C / 150e6) ** 2, 16)
check(_F4_FAR, "100 MHz over 9 MHz plasma frequency", 100 / 9, 11)
check(_F4_FAR, "200 MHz over 1 MHz plasma frequency", 200 / 1, 200)
check(_F4_FAR, "rotation ratio for doubled frequency", 2**2, 4)

# --- library/cyclotron-resonance.md -------------------------------------------
_F4_CYC = "library/cyclotron-resonance.md §4.3"
_F4_FC = _F4_E / (2 * pi * _F4_ME)  # Hz/T
check(_F4_CYC, "free-electron fc/B (GHz/T)", _F4_FC / 1e9, 27.99, rtol=0.001)
check(_F4_CYC, "spin over orbital, percent excess", (28024.9513861e6 / _F4_FC - 1) * 100, 0.116, rtol=0.01)
check(_F4_CYC, "GaAs 0.067 fc/B (THz/T)", _F4_FC / 0.067 / 1e12, 0.42)
check(_F4_CYC, "Ge transverse 0.082 fc/B (THz/T)", _F4_FC / 0.082 / 1e12, 0.34)
check(_F4_CYC, "Si transverse 0.19 fc/B (THz/T)", _F4_FC / 0.19 / 1e12, 0.15)
check(_F4_CYC, "tau for omega_c tau = 1, free electron, 1 T (ps)", 1 / (2 * pi * _F4_FC) * 1e12, 5.7)
check(_F4_CYC, "tau for omega_c tau = 1, GaAs, 1 T (ps)", 0.067 / (2 * pi * _F4_FC) * 1e12, 0.38)
check(_F4_CYC, "mobility for mu B = 1 at 1 T (cm^2/V s)", 1.0 / 1.0 * 1e4, 1e4)
check(_F4_CYC, "mu B at 100 cm^2/(V s) and 100 T", 100e-4 * 100, 1)
check(
    "analysis/fragments (cyclotron-resonance:clock_latency:omega-c)",
    "free-electron fc at 1 T (Hz)",
    _F4_FC,
    2.799e10,
    rtol=0.001,
)

# --- library/aharonov-bohm.md -------------------------------------------------
_F4_AB = "library/aharonov-bohm.md §4.3"
check(_F4_AB, "h/e (Wb)", _F4_H / _F4_E, 4.135667696e-15, rtol=1e-9)
check(_F4_AB, "twice the tabulated h/2e (Wb)", 2 * 2.067833848e-15, 4.135667696e-15, rtol=1e-9)
check(_F4_AB, "field per period, 1 um diameter loop (mT)", _F4_H / _F4_E / (pi * 0.5e-6**2) * 1e3, 5.3)
