# Checks for the gapped-coherence batch (4): superconductivity, meissner,
# josephson-effect, flux-quantization, type-ii-critical-field,
# superfluid-helium-4, bose-einstein-condensate, quantum-hall-effect,
# quantum-point-contact, neutron-gravitational-states.
# Executed inside analysis/computed_checks.py; uses check, pi, K_B and H_PLANCK
# from it. Names defined here carry a _G4 prefix.
import math as _g4m

_G4_E = 1.602176634e-19  # C, exact
_G4_HBAR = H_PLANCK / (2 * pi)
_G4_PHI0 = H_PLANCK / (2 * _G4_E)  # Wb
_G4_ME = 9.1093837139e-31  # kg, CODATA 2022
_G4_MN = 1.67492750056e-27  # kg, CODATA 2022 [S3 neutron file]
_G4_MALPHA = 6.6446573450e-27  # kg, CODATA 2022 [S3 helium file]
_G4_M4 = _G4_MALPHA + 2 * _G4_ME  # helium-4 atom, binding neglected
_G4_U = 1.66053906892e-27  # kg, CODATA 2022
_G4_G = 9.80665  # m/s^2, standard gravity

# --- library/superconductivity.md ---------------------------------------------
_G4_SC = "library/superconductivity.md §4.3"
# (gap meV, Tc K) from Table I of [S1]
_G4_GAP = {"Al": (0.175, 1.19), "Sn": (0.557, 3.73), "Pb": (1.365, 7.2), "Nb": (1.52, 9.25)}
for _g4_n, _g4_q in (("Al", 3.41), ("Sn", 3.47), ("Pb", 4.40), ("Nb", 3.81)):
    _g4_d, _g4_t = _G4_GAP[_g4_n]
    check(_G4_SC, f"2 Delta / k Tc, {_g4_n}", 2 * _g4_d * 1e-3 * _G4_E / (K_B * _g4_t), _g4_q, rtol=0.01)
for _g4_n, _g4_q in (("Al", 85), ("Sn", 269), ("Pb", 660), ("Nb", 735)):
    check(_G4_SC, f"gap frequency 2 Delta / h, {_g4_n} (GHz)", 2 * _G4_GAP[_g4_n][0] * 1e-3 * _G4_E / H_PLANCK / 1e9, _g4_q, rtol=0.01)
check("library/superconductivity.md §4.4", "xi for Bc2 = 14 T (nm)", _g4m.sqrt(_G4_PHI0 / (2 * pi * 14)) * 1e9, 4.8, rtol=0.02)
check("library/superconductivity.md §4.4", "flux quantum (Wb)", _G4_PHI0, 2.067833848e-15, rtol=1e-9)

# --- library/meissner.md ------------------------------------------------------
_G4_ME_ = "library/meissner.md §4.3"
check(_G4_ME_, "kappa Al (16 nm / 1600 nm)", 16 / 1600, 0.010)
check(_G4_ME_, "kappa Sn (50 / 230)", 50 / 230, 0.22)
check(_G4_ME_, "kappa Pb (40 / 90)", 40 / 90, 0.44)
check(_G4_ME_, "kappa Nb (85 / 30)", 85 / 30, 2.8)
check(_G4_ME_, "kappa Nb, second table (32 / 39)", 32 / 39, 0.82)
check(_G4_ME_, "kappa YBCO (90 nm / 1.41 nm)", 90 / 1.41, 64)
check(_G4_ME_, "type-II boundary 1/sqrt 2", 1 / _g4m.sqrt(2), 0.707, rtol=0.001)
check(_G4_ME_, "Nb penetration depth, ratio of the two tables", 85 / 32, 2.7)
check(_G4_ME_, "slab mid-plane field, d = lambda", 1 / _g4m.cosh(0.5), 0.89, rtol=0.01)
check(_G4_ME_, "slab mid-plane field, d = 3 lambda", 1 / _g4m.cosh(1.5), 0.43, rtol=0.02)
check(_G4_ME_, "slab mid-plane field, d = 10 lambda", 1 / _g4m.cosh(5.0), 0.013)

# --- library/josephson-effect.md ----------------------------------------------
_G4_JO = "library/josephson-effect.md §4.3"
check(_G4_JO, "Josephson constant (GHz/V)", 2 * _G4_E / H_PLANCK / 1e9, 483597.8484, rtol=1e-9)
check(_G4_JO, "frequency at 1 uV (MHz)", 2 * _G4_E / H_PLANCK * 1e-6 / 1e6, 483.6, rtol=0.001)
check(_G4_JO, "frequency at 1 mV (GHz)", 2 * _G4_E / H_PLANCK * 1e-3 / 1e9, 483.6, rtol=0.001)
check(_G4_JO, "step spacing at 10 GHz (uV)", _G4_PHI0 * 10e9 * 1e6, 20.7, rtol=0.005)
for _g4_n, _g4_q in (("Al", 0.35), ("Pb", 2.73), ("Nb", 3.04)):
    check(_G4_JO, f"gap voltage 2 Delta / e, {_g4_n} (mV)", 2 * _G4_GAP[_g4_n][0], _g4_q, rtol=0.01)
for _g4_n, _g4_q in (("Al", 85), ("Pb", 660), ("Nb", 735)):
    check(_G4_JO, f"gap frequency, {_g4_n} (GHz)", 2 * _G4_GAP[_g4_n][0] * 1e-3 * _G4_E / H_PLANCK / 1e9, _g4_q, rtol=0.01)

# --- library/flux-quantization.md ---------------------------------------------
check(
    "library/flux-quantization.md §4.3",
    "field of one flux quantum in a 10 um ring (uT)",
    _G4_PHI0 / (pi * (5e-6) ** 2) * 1e6,
    26,
    rtol=0.02,
)

# --- library/type-ii-critical-field.md ----------------------------------------
_G4_T2 = "library/type-ii-critical-field.md §4.3"
check(_G4_T2, "YBCO Hc2 anisotropy 638/153", 638 / 153, 4.2, rtol=0.02)
check(_G4_T2, "triangular lattice spacing at 1 T (nm)", _g4m.sqrt(2 * _G4_PHI0 / (_g4m.sqrt(3) * 1)) * 1e9, 49, rtol=0.01)
check(_G4_T2, "triangular lattice spacing at 6 T (nm)", _g4m.sqrt(2 * _G4_PHI0 / (_g4m.sqrt(3) * 6)) * 1e9, 20, rtol=0.01)
check(_G4_T2, "vortex density at 1 T (1/m^2)", 1 / _G4_PHI0, 4.8e14, rtol=0.01)
check(_G4_T2, "xi for 14 T (nm)", _g4m.sqrt(_G4_PHI0 / (2 * pi * 14)) * 1e9, 4.8, rtol=0.02)
check(_G4_T2, "Hc2 for xi = 30 nm (T)", _G4_PHI0 / (2 * pi * (30e-9) ** 2), 0.37, rtol=0.02)
check(_G4_T2, "Hc2 for xi = 39 nm (T)", _G4_PHI0 / (2 * pi * (39e-9) ** 2), 0.22, rtol=0.02)

# --- library/superfluid-helium-4.md -------------------------------------------
_G4_HE = "library/superfluid-helium-4.md §4.3"
_G4_N_HE = 146.1087 / _G4_M4  # 1/m^3, density at T_lambda [S1]
_G4_TC_HE = 2 * pi * _G4_HBAR**2 / (_G4_M4 * K_B) * (_G4_N_HE / 2.612) ** (2 / 3)
check(_G4_HE, "superfluid fraction, leading term at eps = 0.01", 2.403 * 0.01**0.6717, 0.11, rtol=0.02)
check(_G4_HE, "eps = 0.01 below T_lambda (mK)", 0.01 * 2.1768 * 1e3, 22, rtol=0.02)
check(_G4_HE, "helium-4 atomic mass (kg)", _G4_M4, 6.6465e-27, rtol=1e-4)
check(_G4_HE, "circulation quantum h/m4 (m^2/s)", H_PLANCK / _G4_M4, 9.97e-8, rtol=0.001)
check(_G4_HE, "number density at T_lambda (1/m^3)", _G4_N_HE, 2.20e28, rtol=0.005)
check(_G4_HE, "ideal-gas Tc at that density (K)", _G4_TC_HE, 3.15, rtol=0.005)
check(_G4_HE, "ideal-gas Tc over T_lambda, excess (%)", (_G4_TC_HE / 2.1768 - 1) * 100, 45, rtol=0.02)

# --- library/bose-einstein-condensate.md --------------------------------------
_G4_BE = "library/bose-einstein-condensate.md §4.3"
_G4_M_NA = 22.98977 * _G4_U
_G4_LAM_NA = H_PLANCK / _g4m.sqrt(2 * pi * _G4_M_NA * K_B * 2e-6)
check(_G4_BE, "zeta(3)^(-1/3)", 1.2020569 ** (-1 / 3), 0.94, rtol=0.002)
check(_G4_BE, "thermal wavelength of Na at 2 uK (nm)", _G4_LAM_NA * 1e9, 257, rtol=0.005)
check(_G4_BE, "critical density of Na at 2 uK (1/cm^3)", 2.612 / _G4_LAM_NA**3 / 1e6, 1.5e14, rtol=0.03)

# --- library/quantum-hall-effect.md -------------------------------------------
_G4_QH = "library/quantum-hall-effect.md §4.3"
_G4_GR = 1e6 * _g4m.sqrt(2 * _G4_E * _G4_HBAR * 45) / K_B  # K
check(_G4_QH, "von Klitzing constant (ohm)", H_PLANCK / _G4_E**2, 25812.80745, rtol=1e-9)
check(_G4_QH, "graphene Landau gap at 45 T (K)", _G4_GR, 2820, rtol=0.005)
check(_G4_QH, "that gap over kT at 300 K", _G4_GR / 300, 9.4, rtol=0.01)
check(_G4_QH, "magnetic length at 1 T (nm)", _g4m.sqrt(_G4_HBAR / _G4_E) * 1e9, 25.7, rtol=0.005)
check(_G4_QH, "magnetic length at 10 T (nm)", _g4m.sqrt(_G4_HBAR / (_G4_E * 10)) * 1e9, 8.1, rtol=0.005)
check(_G4_QH, "field for filling 2 at 3e15 /m^2 (T)", 3e15 * H_PLANCK / (2 * _G4_E), 6.2, rtol=0.005)

# --- library/quantum-point-contact.md -----------------------------------------
_G4_QP = "library/quantum-point-contact.md §4.3"
check(_G4_QP, "conductance quantum (S)", 2 * _G4_E**2 / H_PLANCK, 7.748091729e-5, rtol=1e-9)
check(_G4_QP, "1/G0 (ohm)", H_PLANCK / (2 * _G4_E**2), 12906, rtol=1e-4)
check(_G4_QP, "Fermi wavelength from 16 modes at 360 nm (nm)", 2 * 360 / 16, 45)

# --- library/neutron-gravitational-states.md ----------------------------------
_G4_NG = "library/neutron-gravitational-states.md §4.3"
_G4_Z0 = (_G4_HBAR**2 / (2 * _G4_MN**2 * _G4_G)) ** (1 / 3)
check(_G4_NG, "length scale z0 (um)", _G4_Z0 * 1e6, 5.87, rtol=0.002)
for _g4_a, _g4_z, _g4_en in ((2.338, 13.7, 1.41), (4.088, 24.0, 2.46), (5.521, 32.4, 3.32), (6.787, 39.8, 4.08)):
    check(_G4_NG, f"turning height, Airy zero {_g4_a} (um)", _g4_a * _G4_Z0 * 1e6, _g4_z, rtol=0.005)
    check(_G4_NG, f"level energy, Airy zero {_g4_a} (peV)", _G4_MN * _G4_G * _g4_a * _G4_Z0 / _G4_E * 1e12, _g4_en, rtol=0.005)
check(_G4_NG, "E1 / k (nK)", _G4_MN * _G4_G * 2.338 * _G4_Z0 / K_B * 1e9, 16, rtol=0.03)
check(_G4_NG, "peak vertical speed in the lowest state (cm/s)", _g4m.sqrt(2 * _G4_G * 2.338 * _G4_Z0) * 100, 1.6, rtol=0.03)
check(_G4_NG, "classical bounce period (ms)", 2 * _g4m.sqrt(2 * 2.338 * _G4_Z0 / _G4_G) * 1e3, 3.3, rtol=0.02)
check(_G4_NG, "transit of 10 cm at 10 m/s (ms)", 0.10 / 10 * 1e3, 10)
check(_G4_NG, "transit over bounce period", 10 / 3.35, 3, rtol=0.05)
check(_G4_NG, "kT at 300 K over level spacing 1 peV", K_B * 300 / _G4_E / 1e-12, 2.6e10, rtol=0.02)
