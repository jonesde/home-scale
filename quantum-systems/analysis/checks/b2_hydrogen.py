# Checks for library/hydrogen-in-metals.md (batch 2-B).
# Executed inside analysis/computed_checks.py; uses K_B, check, exp, log, sqrt from it.

R_GAS = 8.314462618  # J/(mol K), CODATA 2022 (exact)
K_B_EV = 8.617333262e-5  # eV/K
T_ROOM = 298.0  # K
T_HOT = 573.0  # K (300 degC)
ATM_KPA = 101.325

# Molar masses (g/mol) and molar volumes (m^3/mol): KnowledgeDoor elements handbook [S30]
M_NI = 58.693
M_H = 1.008
VM_FE = 7.09e-6


def h_ni(t_k: float, p_pa: float) -> float:
    """H/Ni from Hagi 1986: S = 2.2e-6 exp(-10.8 kJ/RT) mol H2 / (mol Ni Pa^1/2) [S1]."""
    return 2.0 * 2.2e-6 * exp(-10.8e3 / (R_GAS * t_k)) * sqrt(p_pa)


def h_cu(t_k: float, p_pa: float) -> float:
    """H/Cu from Hagi 1986: S = 1.4e-5 exp(-37.6 kJ/RT) mol H2 / (mol Cu Pa^1/2) [S1]."""
    return 2.0 * 1.4e-5 * exp(-37.6e3 / (R_GAS * t_k)) * sqrt(p_pa)


def h_fe(t_k: float, p_mpa: float) -> float:
    """H/Fe from San Marchi & Somerday Table 2.1, iron:
    S = 180.1 exp(-23.66 kJ/RT) mol H2 m^-3 MPa^-1/2 [S2]."""
    return 2.0 * 180.1 * exp(-23.66e3 / (R_GAS * t_k)) * sqrt(p_mpa) * VM_FE


def vant_hoff_kpa(a_kj: float, b_j_k: float, t_k: float) -> float:
    """Plateau pressure from ln(P/1 atm) = A/RT + B/R [S7]."""
    return exp(a_kj * 1e3 / (R_GAS * t_k) + b_j_k / R_GAS) * ATM_KPA


D_NI = 9.2e-7 * exp(-41.4e3 / (R_GAS * T_ROOM))  # m^2/s, Hagi 1986 [S1]
D_PD = 0.006e-4 * exp(-0.23 / (K_B_EV * T_ROOM))  # m^2/s, Heuser et al. 2014 [S17]
D_FE = 7.23e-8 * exp(-5.69e3 / (R_GAS * T_ROOM))  # m^2/s, Kiuchi & McLellan via [S18]

A_PD = 3.889  # angstrom, pure Pd [S3]
A_NI = 3.5238  # angstrom [S15]
A_NIH = 3.731  # angstrom [S15]
LAMBDA_NI = 34e-6  # magnitude; mid-value of -33 (computed) and -35 (measured) [S29]
ALPHA_NI = 13.4e-6  # 1/K at 25 degC [S30]

_H = "library/hydrogen-in-metals.md §4.3"

# Solubility
check(_H, "H/Ni at 298 K, 1 bar", h_ni(T_ROOM, 1e5), 1.8e-5)
check(_H, "H/Ni at 298 K, 20 bar", h_ni(T_ROOM, 20e5), 8.0e-5)
check(_H, "H/Ni at 298 K, 50 bar", h_ni(T_ROOM, 50e5), 1.3e-4)
check(_H, "H/Ni at 298 K, 300 bar", h_ni(T_ROOM, 300e5), 3.1e-4)
check(_H, "H/Ni at 573 K, 1 bar", h_ni(T_HOT, 1e5), 1.4e-4)
check(_H, "H/Cu at 298 K, 1 bar", h_cu(T_ROOM, 1e5), 2.3e-9)
check(_H, "H/Cu at 573 K, 1 bar", h_cu(T_HOT, 1e5), 3.3e-6)
check(_H, "H/Fe at 298 K, 1 bar", h_fe(T_ROOM, 0.1), 5.7e-8)
check(_H, "H/Fe at 573 K, 1 bar", h_fe(T_HOT, 0.1), 5.6e-6)
check(_H, "Ni, 300 bar: hydrogen by mass (wt ppm)", h_ni(T_ROOM, 300e5) * M_H / M_NI * 1e6, 5.3)
check(_H, "Ni, 1 bar: hydrogen by mass (wt ppm)", h_ni(T_ROOM, 1e5) * M_H / M_NI * 1e6, 0.31)
check(_H, "Tertiary 0.00005 wt% as H/Ni", 5e-7 * M_NI / M_H, 2.9e-5)
check(_H, "H2 taken up by 1 g Ni at 300 bar (micromol)", h_ni(T_ROOM, 300e5) / 2 / M_NI * 1e6, 2.6)
check(_H, "Ideal-gas H2 in 1 cm^3 at 300 bar, 298 K (mmol)", 300e5 * 1e-6 / (R_GAS * T_ROOM) * 1e3, 12.1, 0.01)
check(
    _H,
    "Pressure drop from 1 g Ni in 1 cm^3 at 300 bar (bar)",
    300 * (h_ni(T_ROOM, 300e5) / 2 / M_NI) / (300e5 * 1e-6 / (R_GAS * T_ROOM)),
    0.065,
)
check(_H, "Pd (0.68) over Ni solubility at 1 bar, 298 K", 0.68 / h_ni(T_ROOM, 1e5), 3.8e4)
check(_H, "Ni hydride formation pressure over 300 bar", 6000 / 300, 20, 0.001)
check(_H, "Ni hydride decomposition pressure over 300 bar", 3400 / 300, 11)
check(_H, "Ni hydride: formation over decomposition pressure", 6.0 / 3.4, 1.8)

# Pd plateau from van't Hoff constants
check(_H, "Pd-H plateau at 298 K, Sharpe constants (kPa)", vant_hoff_kpa(-36, 88, T_ROOM), 2.0)
check(_H, "Pd-D plateau at 298 K, Sharpe constants (kPa)", vant_hoff_kpa(-32, 88, T_ROOM), 9.8)
check(_H, "Pd-H plateau at 298 K, Lasser constants (kPa)", vant_hoff_kpa(-37.8, 93.9, T_ROOM), 1.9)
check(_H, "Pd-D plateau at 298 K, Lasser constants (kPa)", vant_hoff_kpa(-33.7, 93.7, T_ROOM), 9.8)
check(_H, "D over H plateau ratio, Sharpe", vant_hoff_kpa(-32, 88, T_ROOM) / vant_hoff_kpa(-36, 88, T_ROOM), 5.0)
check(_H, "Pressure factor from 0.7 to 0.9 H/Pd at 1.5 decades per 0.1", 10 ** (1.5 * 2), 1000, 0.001)

# Lattice expansion
check(_H, "beta-PdH0.58 lattice parameter, Benck calibration (A)", 3.9321 + 0.1719 * 0.58, 4.032, 0.001)
check(_H, "Pd alpha to beta linear strain, tertiary constants (%)", (4.025 / A_PD - 1) * 100, 3.5)
check(_H, "Pd alpha to beta volume strain, tertiary constants (%)", ((4.025 / A_PD) ** 3 - 1) * 100, 10.9, 0.02)
check(_H, "Pd linear strain at 0.58, Benck calibration (%)", ((3.9321 + 0.1719 * 0.58) / A_PD - 1) * 100, 3.7)
check(_H, "Pd linear strain at 0.58, factor 0.063 (%)", 0.063 * 0.58 * 100, 3.7)
check(_H, "Pd film lattice increase 3.892 to 4.063 A (%)", (4.063 / 3.892 - 1) * 100, 4.4)
check(_H, "Ni to NiH linear strain (%)", (A_NIH / A_NI - 1) * 100, 5.9)
check(_H, "Ni to NiH volume strain (%)", ((A_NIH / A_NI) ** 3 - 1) * 100, 18.7, 0.02)

# Strain scale
check(_H, "Ni polycrystal magnetostriction from single-crystal constants (ppm)", (2 * -46 + 3 * -24) / 5, -33)
check(_H, "Pd hydride misfit over Ni magnetostriction", (4.025 / A_PD - 1) / LAMBDA_NI, 1000, 0.05)
check(_H, "Ni hydride misfit over Ni magnetostriction", (A_NIH / A_NI - 1) / LAMBDA_NI, 1700, 0.05)
check(_H, "Thermal strain of Ni over 10 K", ALPHA_NI * 10, 1.3e-4)
check(_H, "10 K thermal strain over magnetostriction", ALPHA_NI * 10 / LAMBDA_NI, 3.9)
check(_H, "Temperature change whose strain equals the magnetostriction (K)", LAMBDA_NI / ALPHA_NI, 2.5)

# Diffusion
check(_H, "D of H in Ni at 298 K (m^2/s)", D_NI, 5.1e-14)
check(_H, "D of H in Pd at 298 K (m^2/s)", D_PD, 7.7e-11)
check(_H, "D of H in Fe at 298 K (m^2/s)", D_FE, 7.3e-9)
check(_H, "Ni, 1 um, x^2/D (s)", 1e-12 / D_NI, 20)
check(_H, "Pd, 1 um, x^2/D (ms)", 1e-12 / D_PD * 1e3, 13)
check(_H, "Fe, 1 um, x^2/D (ms)", 1e-12 / D_FE * 1e3, 0.14)
check(_H, "Ni, 100 um, x^2/D (h)", 1e-8 / D_NI / 3600, 55)
check(_H, "Pd, 100 um, x^2/D (s)", 1e-8 / D_PD, 130)
check(_H, "Fe, 100 um, x^2/D (s)", 1e-8 / D_FE, 1.4)
check(_H, "Ni, sqrt(D t) in 10 us (nm)", sqrt(D_NI * 10e-6) * 1e9, 0.71)
check(_H, "Ni, sqrt(D t) in 100 us (nm)", sqrt(D_NI * 100e-6) * 1e9, 2.3)
check(_H, "Pd, sqrt(D t) in 100 us (nm)", sqrt(D_PD * 100e-6) * 1e9, 88)
check(_H, "Fe, sqrt(D t) in 100 us (nm)", sqrt(D_FE * 100e-6) * 1e9, 850)

# Size and trapping
check(_H, "Nanocube size at which Tc(L) = 566 - 2381/L reaches 300 K (nm)", 2381 / (566 - 300), 9.0)
check(_H, "Tc of a 30 nm nanocube (K)", 566 - 2381 / 30, 487)
check(_H, "0.23 eV in kJ/mol", 0.23 * 96.485, 22)
check(_H, "0.31 eV in kJ/mol", 0.31 * 96.485, 30)
check(_H, "50 kJ/mol in eV", 50 / 96.485, 0.52)
check(_H, "50 kJ/mol over kT at 298 K", 50e3 / (R_GAS * T_ROOM), 20)
check(_H, "0.23 eV over kT at 298 K", 0.23 / (K_B_EV * T_ROOM), 9.0)
check(_H, "Boltzmann factor for 50 kJ/mol at 298 K", exp(-50e3 / (R_GAS * T_ROOM)), 1.7e-9)
check(_H, "Boltzmann factor for 50 kJ/mol at 473 K", exp(-50e3 / (R_GAS * 473.0)), 3.0e-6)
check(
    _H,
    "Rate gain for a 50 kJ/mol trap from 298 K to 473 K",
    exp(-50e3 / (R_GAS * 473.0)) / exp(-50e3 / (R_GAS * T_ROOM)),
    1750,
)

# --- application/EM-LENR.md (rewrite of 2026-11-13) and the three related application files
_A = "application/EM-LENR.md"
check(_A, "Gain in H/Ni from 20 to 300 bar, sqrt(15)", sqrt(300 / 20), 3.9)
check(_A, "Relative pressure drop, 1 g Ni in 1 cm^3 at 300 bar", (h_ni(T_ROOM, 300e5) / 2 / M_NI) / (300e5 * 1e-6 / (R_GAS * T_ROOM)), 2.2e-4)
check(_A, "Ni over Fe lattice solubility at 1 bar, 298 K", h_ni(T_ROOM, 1e5) / h_fe(T_ROOM, 0.1), 310)
check(_A, "D(Pd) over D(Ni) at 298 K", D_PD / D_NI, 1500)
check(_A, "Pd, sqrt(D t) in 10 us (nm)", sqrt(D_PD * 10e-6) * 1e9, 28)
check(_A, "Pd misfit over 35 ppm magnetostriction", (4.025 / A_PD - 1) / 35e-6, 1000)
check(_A, "Pd misfit over 40 ppm magnetostriction", (4.025 / A_PD - 1) / 40e-6, 870)
check(_A, "Ni hydride misfit over 35 ppm magnetostriction", (A_NIH / A_NI - 1) / 35e-6, 1700)
check(_A, "Ni hydride misfit over 40 ppm magnetostriction", (A_NIH / A_NI - 1) / 40e-6, 1500)
check(_A, "Thermal strain of Ni per kelvin over 35 ppm (fraction)", ALPHA_NI / 35e-6, 0.38)
check(_A, "Hydrogen in 1 g Ni at 300 bar (micrograms)", h_ni(T_ROOM, 300e5) * M_H / M_NI * 1e6, 5.3)
check(_A, "Plateau pressure of Pd-H (2.0 kPa) as a fraction of 20 bar", 2.0e3 / 20e5, 1e-3)
