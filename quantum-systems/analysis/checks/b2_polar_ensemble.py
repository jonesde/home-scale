# Checks for the polar and ensemble batch: ferroelectric-remanence,
# ferroelectric-domains, piezoelectricity, electron-heat-capacity,
# curie-paramagnetism.
# Snippet for analysis/computed_checks.py. Uses K_B, MU_0, check and math's
# exp, pi, sqrt from that file. Names defined here carry a _PE prefix so they
# cannot collide with constants defined by the other files in this directory.

from math import tanh as _pe_tanh

_PE_EPS0 = 8.8541878188e-12  # F/m, CODATA 2022
_PE_MU_B = 9.2740100657e-24  # J/T, CODATA 2022
_PE_N_A = 6.02214076e23  # 1/mol, exact
_PE_R = _PE_N_A * K_B  # J/(mol K)


def _pe_c_to_k(t_c: float) -> float:
    return t_c + 273.15


def _pe_coth(x: float) -> float:
    return 1.0 / _pe_tanh(x)


def _pe_brillouin(s: float, x: float) -> float:
    """Brillouin function B_S(x) with x = g mu_B S B / kT."""
    a = (2.0 * s + 1.0) / (2.0 * s)
    b = 1.0 / (2.0 * s)
    return a * _pe_coth(a * x) - b * _pe_coth(b * x)


def _pe_debye_a(theta_k: float) -> float:
    """Low-temperature lattice coefficient A in C = A T^3, J/(mol K^4)."""
    return 12.0 * pi**4 * _PE_R / (5.0 * theta_k**3)


def _pe_gamma_free(z: float, t_f: float) -> float:
    """Free-electron gamma in mJ/(mol K^2) for z electrons per atom."""
    return 1e3 * pi**2 * z * _PE_R / (2.0 * t_f)


# --- library/ferroelectric-remanence.md ---------------------------------------
_FER = "library/ferroelectric-remanence.md §4.3"
check(_FER, "BaTiO3 Curie point, 120 C in K", _pe_c_to_k(120), 393, 0.002)
check(_FER, "PbTiO3 Curie point, 760 K in C", 760 - 273.15, 487, 0.002)
check(_FER, "PZT5H Curie point, 195 C in K", _pe_c_to_k(195), 468, 0.002)
check(_FER, "PZT5A Curie point, 365 C in K", _pe_c_to_k(365), 638, 0.002)
check(_FER, "LiNbO3 lower Curie point, 1413 K in C", 1413 - 273.15, 1140, 0.002)
check(_FER, "LiNbO3 upper Curie point, 1475 K in C", 1475 - 273.15, 1202, 0.002)
check(_FER, "LiTaO3 lower Curie point, 874 K in C", 874 - 273.15, 601, 0.002)
check(_FER, "LiTaO3 upper Curie point, 958 K in C", 958 - 273.15, 685, 0.002)
check(_FER, "BaTiO3 Ps, 0.263 C/m2 in uC/cm2", 0.263 * 1e6 / 1e4, 26.3, 0.002)
check(_FER, "PZT film Pr, 40 uC/cm2 in C/m2", 40e-6 * 1e4, 0.40, 0.002)
check(_FER, "coercive field 300 kV/cm in V/m", 300e3 * 100, 3e7, 0.002)
check(_FER, "coercive field 400 kV/cm in V/m", 400e3 * 100, 4e7, 0.002)
check(_FER, "unscreened slab field Ps/eps0 for 0.263 C/m2 (V/m)", 0.263 / _PE_EPS0, 3.0e10, 0.02)
check(_FER, "residual fraction, 3e7 V/m over Ps/eps0 (%)", 100 * 3e7 / (0.263 / _PE_EPS0), 0.10, 0.03)
check(_FER, "residual fraction, 4e7 V/m over Ps/eps0 (%)", 100 * 4e7 / (0.263 / _PE_EPS0), 0.13, 0.05)
check(_FER, "Kay-Dunn rise of Ec from 100 um to 200 nm, (500)^(2/3)", (100e-6 / 200e-9) ** (2.0 / 3.0), 63, 0.01)
check(_FER, "six unit cells of 0.40 nm (nm)", 6 * 0.40, 2.4, 0.002)
check(_FER, "three unit cells of 0.40 nm (nm)", 3 * 0.40, 1.2, 0.002)
check(_FER, "cell height implied by 24 A over 6 cells (nm)", 2.4 / 6, 0.40, 0.002)

# --- library/ferroelectric-domains.md -------------------------------------------
_FED = "library/ferroelectric-domains.md §4.3"
check(_FED, "one lattice constant of 0.40 nm (nm)", 1 * 0.40, 0.4, 0.002)
check(_FED, "two lattice constants of 0.40 nm (nm)", 2 * 0.40, 0.8, 0.002)
check(_FED, "PbTiO3 wall energy ratio 180/90, 132/35", 132 / 35, 3.8, 0.02)
check(_FED, "BaTiO3 180 wall energy, 16 erg/cm2 in mJ/m2", 16 * 1e-7 / 1e-4 * 1e3, 16, 0.002)
check(_FED, "head-to-head 180 wall bound charge 2 Ps (C/m2)", 2 * 0.263, 0.53, 0.01)
check(_FED, "head-to-head 90 wall bound charge sqrt(2) Ps (C/m2)", sqrt(2) * 0.263, 0.37, 0.01)
check(_FED, "PbTiO3 90 wall, 10 A in nm", 10 * 0.1, 1.0, 0.002)
check(_FED, "BaTiO3 90 wall, 50 A in nm", 50 * 0.1, 5, 0.002)
check(_FED, "stripe-domain films, 420 A in nm", 420 * 0.1, 42, 0.002)

# --- library/piezoelectricity.md ---------------------------------------------------
_PZ = "library/piezoelectricity.md §4.3"
check(_PZ, "d33 PZT5H over d11 quartz, 618/2.30", 618 / 2.30, 270, 0.01)
check(_PZ, "d33 PZT5H over d33 AlN, 618/5.6", 618 / 5.6, 110, 0.01)
check(_PZ, "strain of PZT5H at 1 MV/m", 618e-12 * 1e6, 6.2e-4, 0.01)
check(_PZ, "strain of quartz at 1 MV/m", 2.30e-12 * 1e6, 2.3e-6, 0.002)
check(_PZ, "quartz inversion, 573.3 C in K", _pe_c_to_k(573.3), 846, 0.002)
check(_PZ, "PZT5H Curie point, 195 C in K", _pe_c_to_k(195), 468, 0.002)
check(_PZ, "PZT5A Curie point, 365 C in K", _pe_c_to_k(365), 638, 0.002)
check(_PZ, "BaTiO3 Curie point, 120 C in K", _pe_c_to_k(120), 393, 0.002)
check(_PZ, "NBT depolarization below its Curie point, 325 - 187 (K)", 325 - 187, 138, 0.002)
check(_PZ, "quartz d11 fall from -196 C to 100 C (%)", 100 * (2.31 - 2.05) / 2.31, 11, 0.05)

# --- library/electron-heat-capacity.md ----------------------------------------------
_EHC = "library/electron-heat-capacity.md §4.3"
check(_EHC, "free-electron gamma Cu from T_F = 8.16e4 K (mJ/mol K2)", _pe_gamma_free(1, 8.16e4), 0.503, 0.005)
check(_EHC, "free-electron gamma Ag from T_F = 6.38e4 K", _pe_gamma_free(1, 6.38e4), 0.643, 0.005)
check(_EHC, "free-electron gamma Al from T_F = 13.6e4 K, z = 3", _pe_gamma_free(3, 13.6e4), 0.905, 0.005)
check(_EHC, "gamma measured over free-electron, Cu 0.695/0.505", 0.695 / 0.505, 1.38, 0.01)
check(_EHC, "gamma measured over free-electron, Al 1.35/0.912", 1.35 / 0.912, 1.48, 0.01)
check(_EHC, "gamma measured over free-electron, Ag 0.646/0.645", 0.646 / 0.645, 1.00, 0.01)
check(_EHC, "gamma Pd over gamma Cu, 9.42/0.695", 9.42 / 0.695, 13.6, 0.01)
check(_EHC, "gamma CeAl3 over gamma Cu, 1620/0.695", 1620 / 0.695, 2300, 0.02)
check(_EHC, "T/T_F for Cu at 300 K (%)", 100 * 300 / 8.16e4, 0.37, 0.02)
check(_EHC, "gamma T at 300 K, Cu (J/mol K)", 0.695e-3 * 300, 0.21, 0.03)
check(_EHC, "gamma T at 300 K, Al (J/mol K)", 1.35e-3 * 300, 0.41, 0.03)
check(_EHC, "gamma T at 300 K, Fe (J/mol K)", 4.90e-3 * 300, 1.47, 0.01)
check(_EHC, "gamma T at 300 K, Ni (J/mol K)", 7.04e-3 * 300, 2.11, 0.01)
check(_EHC, "electronic share of C at 300 K, Cu (%)", 100 * 0.695e-3 * 300 / 24.440, 0.85, 0.02)
check(_EHC, "electronic share of C at 300 K, Al (%)", 100 * 1.35e-3 * 300 / 24.200, 1.7, 0.03)
check(_EHC, "electronic share of C at 300 K, Fe (%)", 100 * 4.90e-3 * 300 / 25.10, 5.9, 0.02)
check(_EHC, "electronic share of C at 300 K, Ni (%)", 100 * 7.04e-3 * 300 / 26.07, 8.1, 0.02)
check(_EHC, "Debye A for Cu, theta = 344 K (mJ/mol K4)", 1e3 * _pe_debye_a(344), 0.0478, 0.01)
check(_EHC, "Debye A for Al, theta = 427.7 K (mJ/mol K4)", 1e3 * _pe_debye_a(427.7), 0.0248, 0.01)
check(_EHC, "crossing temperature sqrt(gamma/A), Cu (K)", sqrt(0.695e-3 / _pe_debye_a(344)), 3.8, 0.02)
check(_EHC, "crossing temperature sqrt(gamma/A), Al (K)", sqrt(1.35e-3 / _pe_debye_a(427.7)), 7.4, 0.02)
check(_EHC, "Al superconducting C_es/(gamma Tc) at T = Tc/2", 7.1 * exp(-1.34 * 2), 0.49, 0.02)
check(_EHC, "Al superconducting C_es/(gamma Tc) at T = Tc/4", 7.1 * exp(-1.34 * 4), 0.033, 0.03)
check(_EHC, "Al superconducting over normal at Tc/4 (%)", 100 * 7.1 * exp(-1.34 * 4) / 0.25, 13, 0.04)
check(_EHC, "Dulong-Petit 3R (J/mol K)", 3 * _PE_R, 24.9, 0.003)

# --- library/curie-paramagnetism.md ---------------------------------------------------
_CUR = "library/curie-paramagnetism.md §4.3"
check(_CUR, "mu_B / k (K/T)", _PE_MU_B / K_B, 0.6717, 0.0005)
check(_CUR, "kT / mu_B at 300 K (T)", 300 * K_B / _PE_MU_B, 447, 0.002)
check(_CUR, "kT / mu_B at 1 K (T)", 1 * K_B / _PE_MU_B, 1.49, 0.003)
check(_CUR, "mu_B B / kT at 1 T and 300 K", _PE_MU_B * 1.0 / (K_B * 300), 2.2e-3, 0.03)
check(_CUR, "departure from linearity x^2/3 at 1 T and 300 K", (_PE_MU_B / (K_B * 300)) ** 2 / 3, 1.7e-6, 0.03)
check(_CUR, "Brillouin argument, Cr3+ at 5 T and 1.29 K", 2 * 1.5 * _PE_MU_B * 5.0 / (K_B * 1.29), 7.8, 0.01)
check(_CUR, "B_3/2 at 5 T and 1.29 K (%)", 100 * _pe_brillouin(1.5, 2 * 1.5 * _PE_MU_B * 5.0 / (K_B * 1.29)), 99.6, 0.001)
check(_CUR, "B_3/2 at 1 T and 300 K (%)", 100 * _pe_brillouin(1.5, 2 * 1.5 * _PE_MU_B * 1.0 / (K_B * 300)), 0.37, 0.02)
check(
    _CUR,
    "molar Curie constant, S = 1/2, g = 2 (1e-6 m3 K/mol)",
    1e6 * _PE_N_A * MU_0 * _PE_MU_B**2 * 4 * 0.75 / (3 * K_B),
    4.71,
    0.003,
)
check(
    _CUR,
    "same in cgs (cm3 K/mol)",
    1e6 * _PE_N_A * MU_0 * _PE_MU_B**2 * 4 * 0.75 / (3 * K_B) / (4 * pi),
    0.375,
    0.003,
)
check(_CUR, "g^2 S(S+1) for S = 7/2 over S = 1/2", (4 * 3.5 * 4.5) / (4 * 0.5 * 1.5), 21, 0.001)
check(_CUR, "50 000 G in tesla", 50000 * 1e-4, 5, 0.001)
check(_CUR, "electron precession, 28 024.95 MHz/T in GHz/T", 28024.9513861e-3, 28.025, 0.0001)

# --- further ratios quoted in electron-heat-capacity.md §4.5-§4.6 -------------
check(_EHC, "gamma Fe over gamma Cu, 4.89/0.695", 4.89 / 0.695, 7, 0.02)
check(_EHC, "gamma Pd over gamma Cu, quoted as 14 in the 7-to-14 range", 9.42 / 0.695, 14, 0.04)
check(_EHC, "Pd measured gamma over band value, 9.42/5.6", 9.42 / 5.6, 1.7, 0.02)
check(_EHC, "Ni room-temperature C over 3R, within 5 %", 26.07 / (3 * _PE_R), 1.05, 0.01)
check(_EHC, "Al room-temperature C over 3R, within 5 %", 24.200 / (3 * _PE_R), 0.97, 0.01)
