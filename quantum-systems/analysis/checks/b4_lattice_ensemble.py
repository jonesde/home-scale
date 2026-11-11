# Checks for batch 4 (light): library/phonon-dispersion.md, debye-cutoff.md,
# mossbauer-effect.md, thermal-equilibrium-temperature.md, ideal-gas-pressure.md,
# blackbody-spectrum.md, stefan-boltzmann.md, brownian-motion.md and
# johnson-nyquist-noise.md. Executed inside analysis/computed_checks.py, so
# check(), exp, log, pi, sqrt, K_B, H_PLANCK and CM1_TO_GHZ are available.

# CODATA 2022 exact values and one measured constant.
_C = 299792458.0  # m/s
_E = 1.602176634e-19  # C
_NA = 6.02214076e23  # 1/mol
_HBAR = H_PLANCK / (2 * pi)
_U = 1.66053906892e-27  # kg, atomic mass constant
_SIGMA = 2 * pi**5 * K_B**4 / (15 * _C**2 * H_PLANCK**3)
_B_WIEN = 2.897771955e-3  # m K


def _thz(theta_k: float) -> float:
    """Debye frequency k*Theta/h in THz."""
    return K_B * theta_k / H_PLANCK / 1e12


# --- library/phonon-dispersion.md ----------------------------------------------
_PD = "library/phonon-dispersion.md §4.3"
check(_PD, "Si zone-centre optical mode, 15.5 THz in cm^-1", 15.5e3 / CM1_TO_GHZ, 517, 0.002)
check(_PD, "diamond zone-centre optical mode, 39.9 THz in cm^-1", 39.9e3 / CM1_TO_GHZ, 1331, 0.001)
check(_PD, "2 pi / a, Si (1/m)", 2 * pi / 5.431e-10, 1.16e10, 0.01)
check(_PD, "2 pi / a, diamond (1/m)", 2 * pi / 3.567e-10, 1.76e10, 0.01)
check(_PD, "Debye frequency, Al 427.7 K (THz)", _thz(427.7), 8.9, 0.01)
check(_PD, "Debye frequency, Si 640 K (THz)", _thz(640), 13.3, 0.01)
check(_PD, "Debye frequency, diamond 1860 K (THz)", _thz(1860), 38.8, 0.01)

# --- library/debye-cutoff.md ----------------------------------------------------
_DC = "library/debye-cutoff.md §4.3"
check(_DC, "Debye frequency, Pb 105 K (THz)", _thz(105), 2.2, 0.02)
check(_DC, "Debye frequency, Si 640 K (THz)", _thz(640), 13.3, 0.01)
check(_DC, "Debye frequency, diamond 1860 K (THz)", _thz(1860), 38.8, 0.01)
check(_DC, "3R (J/mol/K)", 3 * K_B * _NA, 24.94, 0.001)
check(_DC, "Pb C_p / 3R", 26.84 / (3 * K_B * _NA), 1.08, 0.01)
check(_DC, "Si heat capacity per atom / 3k", 0.7 * 2.329 / 5e22 / (3 * K_B), 0.79, 0.01)
check(_DC, "diamond heat capacity per atom / 3k", 0.52 * 3.515 / 1.764e23 / (3 * K_B), 0.25, 0.01)
check(_DC, "Pb melting point / Debye temperature", 600.612 / 105, 5.7, 0.01)

# --- library/mossbauer-effect.md ------------------------------------------------
_MB = "library/mossbauer-effect.md §4.3"
_E57 = 14412.9 * _E  # J
_TAU57 = 98.3e-9 / log(2)
_G57 = _HBAR / _TAU57  # J
_ER57 = _E57**2 / (2 * 56.93539195 * _U * _C**2)
_K57 = _E57 / (_HBAR * _C)
check(_MB, "57Fe mean life (ns)", _TAU57 * 1e9, 141.8, 0.001)
check(_MB, "57Fe natural width (neV)", _G57 / _E * 1e9, 4.64, 0.002)
check(_MB, "57Fe free-atom recoil energy (meV)", _ER57 / _E * 1e3, 1.96, 0.005)
check(_MB, "E_R / Gamma", _ER57 / _G57, 4.2e5, 0.02)
check(_MB, "E_R / k (K)", _ER57 / K_B, 22.7, 0.005)
check(_MB, "Doppler velocity for one width (mm/s)", _C * _G57 / _E57 * 1e3, 0.097, 0.01)
check(_MB, "diffusion width, D = 0.6e-9 m2/s (meV)", 2 * _HBAR * _K57**2 * 0.6e-9 / _E * 1e3, 4.2, 0.01)
check(_MB, "diffusion width / Gamma, D = 0.6e-9 m2/s", 2 * _HBAR * _K57**2 * 0.6e-9 / _G57, 9e5, 0.02)
check(_MB, "D at which diffusion width equals Gamma (m2/s)", _G57 / (2 * _HBAR * _K57**2), 6.6e-16, 0.01)

# --- library/thermal-equilibrium-temperature.md ---------------------------------
_TE = "library/thermal-equilibrium-temperature.md §4.3"
_VN2 = sqrt(8 * K_B * 293.15 / (pi * 2 * 14.007 * _U))
check(_TE, "kT at 300 K (J)", K_B * 300, 4.142e-21, 0.001)
check(_TE, "kT at 300 K (meV)", K_B * 300 / _E * 1e3, 25.85, 0.001)
check(_TE, "ideal-gas fractional energy fluctuation, N = 100", sqrt(2 / (3 * 100)), 0.08, 0.03)
check(_TE, "ideal-gas fractional energy fluctuation, N = 1e6", sqrt(2 / (3 * 1e6)), 0.0008, 0.03)
check(_TE, "mean speed of N2 at 293.15 K (m/s)", _VN2, 471, 0.002)
check(_TE, "collision time in air, 66 nm / mean speed (s)", 66e-9 / _VN2, 1.4e-10, 0.01)

# --- library/ideal-gas-pressure.md ----------------------------------------------
_IG = "library/ideal-gas-pressure.md §4.3"
_N0 = 101325 / (K_B * 273.15)
_N20 = 101325 / (K_B * 293.15)
check(_IG, "Loschmidt constant P/kT (1/m3)", _N0, 2.686780e25, 1e-6)
check(_IG, "kT at 300 K (meV)", K_B * 300 / _E * 1e3, 25.85, 0.001)
check(_IG, "n at 293.15 K, 101.325 kPa (1/m3)", _N20, 2.50e25, 0.002)
check(_IG, "mean free path at 100 Pa from 66 nm (um)", 66e-9 * 101325 / 100 * 1e6, 67, 0.01)
check(_IG, "mean free path at 1 Pa from 66 nm (mm)", 66e-9 * 101325 * 1e3, 6.7, 0.01)
check(_IG, "collision time (s)", 66e-9 / _VN2, 1.4e-10, 0.01)
check(_IG, "molecules per cubic micrometre at n0", _N0 * 1e-18, 2.7e7, 0.01)
check(_IG, "molecules in a cube of side 66 nm", _N20 * 66e-9**3, 7e3, 0.03)
check(_IG, "molecules in a cube of side 64 nm", _N20 * 64e-9**3, 6.6e3, 0.01)
check(_IG, "molecules in a cube of side 68 nm", _N20 * 68e-9**3, 7.9e3, 0.01)
check(_IG, "count scatter, N = 2.7e7 (%)", 100 / sqrt(_N0 * 1e-18), 0.02, 0.05)
check(_IG, "count scatter, N = 7e3 (%)", 100 / sqrt(_N20 * 66e-9**3), 1.2, 0.02)

# --- library/blackbody-spectrum.md ----------------------------------------------
_BB = "library/blackbody-spectrum.md §4.3"
check(_BB, "Wien constant from h, c, k (m K)", H_PLANCK * _C / (4.965114231744276 * K_B), 2.897772e-3, 1e-6)
check(_BB, "lambda_max at 300 K (um)", _B_WIEN / 300 * 1e6, 9.66, 0.001)
check(_BB, "lambda_max at 5772 K (nm)", _B_WIEN / 5772 * 1e9, 502, 0.001)
check(_BB, "lambda_max at 2.725 K (mm)", _B_WIEN / 2.725 * 1e3, 1.06, 0.005)
check(_BB, "kT/h at 300 K (THz)", K_B * 300 / H_PLANCK / 1e12, 6.25, 0.001)

# --- library/stefan-boltzmann.md ------------------------------------------------
_SB = "library/stefan-boltzmann.md §4.3"
check(_SB, "sigma from h, c, k (W/m2/K4)", _SIGMA, 5.670374419e-8, 1e-9)
check(_SB, "sigma T^4 at 300 K (W/m2)", _SIGMA * 300**4, 459, 0.001)
check(_SB, "black exchange 300 K to 77 K (W/m2)", _SIGMA * (300**4 - 77**4), 457, 0.001)
check(_SB, "polished Al, emissivity 0.05, 300 K (W/m2)", 0.05 * _SIGMA * 300**4, 23, 0.01)
check(_SB, "lambda_max at 300 K (um)", _B_WIEN / 300 * 1e6, 9.66, 0.001)
check(_SB, "doubling T multiplies exitance by", 2**4, 16, 1e-9)

# --- library/brownian-motion.md -------------------------------------------------
_BM = "library/brownian-motion.md §4.3"
_ETA_W = 1.0020e-3  # Pa s, water at 20 C (Kaye and Laby)
_D1UM = K_B * 293.15 / (6 * pi * _ETA_W * 0.5e-6)
_D1MM = K_B * 293.15 / (6 * pi * _ETA_W * 0.5e-3)
check(_BM, "D, 1 um diameter sphere in water at 20 C (m2/s)", _D1UM, 4.3e-13, 0.01)
check(_BM, "rms displacement per axis in 1 s, 1 um sphere (um)", sqrt(2 * _D1UM) * 1e6, 0.93, 0.01)
check(_BM, "D, 1 mm diameter sphere (m2/s)", _D1MM, 4.3e-16, 0.01)
check(_BM, "rms displacement per axis in 1 s, 1 mm sphere (nm)", sqrt(2 * _D1MM) * 1e9, 29, 0.02)
check(_BM, "momentum relaxation time, 1 um sphere, 1000 kg/m3 (ns)", 2 * 1000 * 0.5e-6**2 / (9 * _ETA_W) * 1e9, 55, 0.01)

# --- library/johnson-nyquist-noise.md -------------------------------------------
_JN = "library/johnson-nyquist-noise.md §4.3"
check(_JN, "sqrt(4kTR), 1 kOhm at 300 K (nV/rtHz)", sqrt(4 * K_B * 300 * 1000) * 1e9, 4.07, 0.001)
check(_JN, "sqrt(4kTR), 50 Ohm at 300 K (nV/rtHz)", sqrt(4 * K_B * 300 * 50) * 1e9, 0.91, 0.001)
check(_JN, "kT/h at 300 K (THz)", K_B * 300 / H_PLANCK / 1e12, 6.25, 0.001)
check(_JN, "kT/h at 4 K (GHz)", K_B * 4 / H_PLANCK / 1e9, 83, 0.005)
check(_JN, "kT/h at 1 K (GHz)", K_B / H_PLANCK / 1e9, 21, 0.01)

# --- fragment rows --------------------------------------------------------------
_FR = "analysis/fragments (batch 4 rows)"
check(_FR, "mossbauer-effect:energy_barrier:line-width, 14.4129 keV in J", _E57, 2.31e-15, 0.002)
check(_FR, "mossbauer-effect:clock_latency:nuclear-lifetime (s)", _TAU57, 1.418e-7, 0.001)
check(_FR, "debye-cutoff:clock_latency:omega-d-ceiling, Pb 105 K (Hz)", _thz(105) * 1e12, 2.2e12, 0.02)
