# Checks for batch B1 (electric): electrical-contacts, dielectric-breakdown,
# ionization-threshold, work-function-thermionic.
# Meant to be merged into analysis/computed_checks.py; uses its names
# (K_B, H_PLANCK, check, exp, log, pi, sqrt) and defines the constants below.

# CODATA 2022 values not yet in computed_checks.py.
E_CHARGE = 1.602176634e-19  # C (exact)
C_LIGHT = 299792458.0  # m/s (exact)
M_ELECTRON = 9.1093837139e-31  # kg
EPS_0 = 8.8541878188e-12  # F/m
G_N = 9.80665  # m/s^2, standard gravity (kgf and gf to newtons)
ATM_TORR = 760.0


def kohlrausch_t(volts: float, t0_k: float, lorenz: float = 2.45e-8) -> float:
    """Hottest temperature in a constriction: Tm^2 - T0^2 = U^2 / 4L."""
    return sqrt(t0_k**2 + volts**2 / (4.0 * lorenz))


def kohlrausch_v(tm_k: float, t0_k: float, lorenz: float = 2.45e-8) -> float:
    """Voltage across a constriction whose hottest point is at tm_k."""
    return 2.0 * sqrt(lorenz * (tm_k**2 - t0_k**2))


def schumann_kv(pd_bar_cm: float) -> float:
    """Kuffel eq. (5.103) for air: Vb in kV, pd in bar cm."""
    return 6.72 * sqrt(pd_bar_cm) + 24.36 * pd_bar_cm


def schottky_ev(field_v_m: float) -> float:
    """Barrier lowering e*sqrt(eF / 4 pi eps0), expressed in eV."""
    return sqrt(E_CHARGE * field_v_m / (4.0 * pi * EPS_0))


# --- library/electrical-contacts.md ------------------------------------------
_CON = "library/electrical-contacts.md §4.3"
_RHO_CU = 1.65e-8  # ohm m
check(_CON, "Cu constriction rho/2a at a = 0.1 um, in mOhm", _RHO_CU / (2 * 0.1e-6) * 1e3, 83)
check(_CON, "Cu constriction rho/2a at a = 1 um, in mOhm", _RHO_CU / (2 * 1e-6) * 1e3, 8.3)
check(_CON, "Cu constriction rho/2a at a = 10 um, in mOhm", _RHO_CU / (2 * 10e-6) * 1e3, 0.83)
_H_CU = 120 * G_N * 1e6  # 120 kg/mm^2 in Pa
check(_CON, "Cu multispot (rho/2) sqrt(pi H / F) at 0.01 N, in mOhm", _RHO_CU / 2 * sqrt(pi * _H_CU / 0.01) * 1e3, 5.0)
check(_CON, "Cu multispot resistance at 1 N, in mOhm", _RHO_CU / 2 * sqrt(pi * _H_CU / 1) * 1e3, 0.50)
check(_CON, "Cu multispot resistance at 100 N, in mOhm", _RHO_CU / 2 * sqrt(pi * _H_CU / 100) * 1e3, 0.050)
check(_CON, "rho/a for a 10 um Cu spot, in mOhm", _RHO_CU / 10e-6 * 1e3, 1.65, 0.005)
check(_CON, "the slide's 1.7 mOhm over rho/2a", 1.7 / (_RHO_CU / (2 * 10e-6) * 1e3), 2)
check(_CON, "Kohlrausch temperature at 0.2 V from 290 K", kohlrausch_t(0.2, 290), 702, 0.002)
check(_CON, "Kohlrausch temperature at 0.3 V from 290 K", kohlrausch_t(0.3, 290), 1001, 0.002)
check(_CON, "Kohlrausch temperature at 0.4 V from 290 K", kohlrausch_t(0.4, 290), 1310, 0.002)
check(_CON, "Kohlrausch temperature at 0.43 V from 290 K", kohlrausch_t(0.43, 290), 1404, 0.002)
check(_CON, "spot thermal time C a^2 / 4 lambda, Cu, a = 10 um (s; source 2.2e-7)", 3.44 * (10e-4) ** 2 / (4 * 4), 2.2e-7)
check(_CON, "spot thermal time, Cu, a = 1 um (s)", 3.44 * (1e-4) ** 2 / (4 * 4), 2.2e-9)
check(_CON, "Kohlrausch melting voltage of Cu, 1083 C from 293 K", kohlrausch_v(1083 + 273.15, 293), 0.41, 0.02)
check(_CON, "Kohlrausch melting voltage of Al, 660 C from 293 K", kohlrausch_v(660 + 273.15, 293), 0.28, 0.02)
check(_CON, "Kohlrausch voltage to reach 1800 C from 293 K", kohlrausch_v(1800 + 273.15, 293), 0.64, 0.01)
check(_CON, "fritting voltage, 2 nm film at 1e7 V/m", 1e7 * 2e-9, 0.02, 0.001)
check(_CON, "fritting voltage, 2 nm film at 1e8 V/m", 1e8 * 2e-9, 0.2, 0.001)
check(_CON, "fritting voltage, 10 nm film at 1e7 V/m", 1e7 * 10e-9, 0.1, 0.001)
check(_CON, "fritting voltage, 10 nm film at 1e8 V/m", 1e8 * 10e-9, 1, 0.001)
check(_CON, "fritting voltage, 100 nm film at 1e7 V/m", 1e7 * 100e-9, 1, 0.001)
check(_CON, "fritting voltage, 100 nm film at 1e8 V/m", 1e8 * 100e-9, 10, 0.001)
check(_CON, "bead chain, 5.8 V over 13 beads (14 contacts)", 5.8 / 14, 0.41, 0.02)
check(_CON, "Cu powder bed field, 15.6 V over 0.30 mm, in kV/m", 15.6 / 0.30e-3 / 1e3, 52, 0.01)
check(_CON, "Cu powder bed field, 24.3 V over 0.40 mm, in kV/m", 24.3 / 0.40e-3 / 1e3, 61, 0.01)
check(_CON, "Cu powder bed field, 33.4 V over 0.50 mm, in kV/m", 33.4 / 0.50e-3 / 1e3, 67, 0.01)
check(_CON, "volts per 87.5 um layer at 52 kV/m", 52e3 * 87.5e-6, 4.6, 0.02)
check(_CON, "volts per 87.5 um layer at 66.8 kV/m", 66.8e3 * 87.5e-6, 5.8, 0.02)
check(_CON, "lowest per-layer voltage over the 0.4 V plateau (more than ten)", 52e3 * 87.5e-6 / 0.4, 11.4, 0.02)
check(_CON, "volts per layer at 56.6 kV/m (unloaded)", 56.6e3 * 87.5e-6, 5.0, 0.02)
check(_CON, "volts per layer at 17.6 kV/m (300 MPa)", 17.6e3 * 87.5e-6, 1.5, 0.03)
check(_CON, "plasma armature, 45 V plus 1 cm at 141 V/cm", 45 + 141 * 1.0, 186, 0.001)
check(_CON, "one gram-force per ampere, in N per kA", 1e-3 * G_N * 1e3, 9.8, 0.005)
_CON_D = "library/electrical-contacts.md data confidence and §4.6"
check(_CON_D, "Fe melting voltage dispute, 0.6 V over 0.19 V (factor of three)", 0.6 / 0.19, 3, 0.06)
check(_CON_D, "Ni melting voltage dispute, 0.65 V over 0.16 V (factor of four)", 0.65 / 0.16, 4, 0.03)

# --- library/dielectric-breakdown.md -----------------------------------------
_DBD = "library/dielectric-breakdown.md §4.3"
check(_DBD, "air, 31.6 kV across 1.0 cm, in MV/m", 31.6e3 / 1.0e-2 / 1e6, 3.16, 0.001)
check(_DBD, "Schumann fit at 0.1 bar cm, in kV/cm", schumann_kv(0.1) / 0.1, 45.6, 0.002)
check(_DBD, "Schumann fit at 1 bar cm, in kV/cm", schumann_kv(1.0) / 1.0, 31.1, 0.002)
check(_DBD, "Schumann fit at 10 bar cm, in kV/cm", schumann_kv(10.0) / 10.0, 26.5, 0.002)
check(_DBD, "Paschen-minimum gap at 1 atm, air 0.55 torr cm, in um", 0.55 / ATM_TORR * 1e4, 7.2, 0.01)
check(_DBD, "Paschen-minimum gap at 1 atm, air 0.567 torr cm, in um", 0.567 / ATM_TORR * 1e4, 7.5, 0.01)
check(_DBD, "Paschen-minimum gap at 1 atm, N2 0.65 torr cm, in um", 0.65 / ATM_TORR * 1e4, 8.6, 0.01)
check(_DBD, "Paschen-minimum gap at 1 atm, N2 0.67 torr cm, in um", 0.67 / ATM_TORR * 1e4, 8.8, 0.01)
check(_DBD, "Paschen-minimum gap at 1 atm, H2 1.05 torr cm, in um", 1.05 / ATM_TORR * 1e4, 13.8, 0.005)
check(_DBD, "Paschen-minimum gap at 1 atm, H2 1.15 torr cm, in um", 1.15 / ATM_TORR * 1e4, 15.1, 0.005)
check(_DBD, "Paschen-minimum gap at 1 atm, Ar 0.9 torr cm, in um", 0.9 / ATM_TORR * 1e4, 11.8, 0.005)
check(_DBD, "Paschen-minimum gap at 1 atm, He 4.0 torr cm, in um", 4.0 / ATM_TORR * 1e4, 52.6, 0.002)
check(_DBD, "air minimum tables differ, 352 V - 327 V", 352 - 327, 25, 0.001)
check(_DBD, "H2 minimum tables differ, 273 V - 230 V", 273 - 230, 43, 0.001)
check(_DBD, "H2 minimum tables differ, as a fraction of 230 V", (273 - 230) / 230, 0.19, 0.03)
check(_DBD, "field at the air minimum, 327 V over 0.567 torr cm at 1 atm, in MV/m", 327 / (0.567 / ATM_TORR * 1e-2) / 1e6, 44, 0.01)
check(_DBD, "field at the air minimum, 352 V over 0.55 torr cm at 1 atm, in MV/m", 352 / (0.55 / ATM_TORR * 1e-2) / 1e6, 49, 0.01)
check(_DBD, "pressure at which a 1 mm air gap is at the minimum, 0.55 torr cm, in torr", 0.55 / 0.1, 5.5, 0.001)
check(_DBD, "pressure at which a 1 mm air gap is at the minimum, 0.567 torr cm, in torr", 0.567 / 0.1, 5.7, 0.01)
check(_DBD, "H2 below air, Naidu pair (327 - 273 V)", 327 - 273, 54, 0.001)
check(_DBD, "H2 below air, Kuffel pair (352 - 230 V)", 352 - 230, 122, 0.001)
_N_AIR_CM3 = 101325 / (K_B * 293.15) / 1e6  # number density at 1 atm, 20 C
check(_DBD, "number density at 1 atm and 20 C, in cm^-3", _N_AIR_CM3, 2.50e19, 0.005)
check(_DBD, "limiting field of air, 0.30 x 3.61e-15 V cm^2 x N, in kV/cm", 0.30 * 3.61e-15 * _N_AIR_CM3 / 1e3, 27, 0.01)
check(_DBD, "limiting field of N2, 0.36 x 3.61e-15 V cm^2 x N, in kV/cm", 0.36 * 3.61e-15 * _N_AIR_CM3 / 1e3, 32.5, 0.005)
check(_DBD, "limiting field of H2, 0.18 x 3.61e-15 V cm^2 x N, in kV/cm", 0.18 * 3.61e-15 * _N_AIR_CM3 / 1e3, 16, 0.02)
check(_DBD, "H2 over air (0.18 / 0.30)", 0.18 / 0.30, 0.6, 0.001)
check(_DBD, "H2 over N2 (0.18 / 0.36)", 0.18 / 0.36, 0.5, 0.001)
# Quoted from the source (Kuffel), recomputed here as a check on the closed form.
check(_DBD, "Townsend minimum for air, e (B/A) ln(1 + 1/gamma), A = 12, B = 365, gamma = 0.02", exp(1) * 365 / 12 * log(1 + 1 / 0.02), 325, 0.002)
check(_DBD, "oil, 60 kV across 2.5 mm, in MV/m", 60e3 / 2.5e-3 / 1e6, 24, 0.001)
check(_DBD, "oil, 88 kV across 2.5 mm, in MV/m", 88e3 / 2.5e-3 / 1e6, 35, 0.01)
check(_DBD, "Martin oil fit, 1 us and 1 cm^2, in MV/cm", 0.5 / (1 ** (1 / 3) * 1**0.1), 0.5, 0.001)
check(_DBD, "Martin oil fit, 1 us and 100 cm^2, in MV/cm", 0.5 / (1 ** (1 / 3) * 100**0.1), 0.32, 0.02)
check(_DBD, "Martin oil fit, 100 us and 1 cm^2, in MV/cm", 0.5 / (100 ** (1 / 3) * 1**0.1), 0.11, 0.03)
check(_DBD, "thinnest-film end of the range, 154 kV/mm in V/m", 154e3 / 1e-3, 1.5e8, 0.03)
check(_DBD, "thickest-field end of the range, 600 kV/mm in V/m", 600e3 / 1e-3, 6e8, 0.001)
check(_DBD, "thickness exponent, polyimide 303 to 154 kV/mm over 25 to 125 um", log(303 / 154) / log(125 / 25), 0.42, 0.01)
check(_DBD, "thickness exponent, polyester 600 to 80 kV/mm over 6 to 350 um", log(600 / 80) / log(350 / 6), 0.50, 0.01)
check(_DBD, "thickness exponent, pulsed thin sheets 5.5 to 3.0 MV/cm over 6.35 to 254 um", log(5.5 / 3.0) / log(254 / 6.35), 0.16, 0.03)
check(_DBD, "17 MV/in in MV/m", 17e6 / 0.0254 / 1e6, 670, 0.002)
check(_DBD, "2 MV/in in MV/m", 2e6 / 0.0254 / 1e6, 79, 0.005)
_DBD_M = "library/dielectric-breakdown.md §4.5"
check(_DBD_M, "span of gas strengths at equal density (2.4 / 0.006)", 2.4 / 0.006, 400, 0.001)

# --- library/ionization-threshold.md -----------------------------------------
_ION = "library/ionization-threshold.md §4.3"
_I_H = 13.598434599702  # eV
check(_ION, "Lyman limit hc / I for H, in nm", H_PLANCK * C_LIGHT / (_I_H * E_CHARGE) * 1e9, 91.175, 0.00001)
check(_ION, "kT at 300 K, in eV", K_B * 300 / E_CHARGE, 0.02585, 0.0002)
check(_ION, "kT at 293.15 K, in eV", K_B * 293.15 / E_CHARGE, 0.02526, 0.0002)
check(_ION, "I / kT for H at 300 K", _I_H * E_CHARGE / (K_B * 300), 526, 0.001)
check(_ION, "I / kT for H at 293.15 K", _I_H * E_CHARGE / (K_B * 293.15), 538, 0.001)
check(_ION, "I / k for H, in K", _I_H * E_CHARGE / K_B, 1.58e5, 0.002)
check(_ION, "spread of H2 determinations (15.98 - 15.37 eV)", 15.98 - 15.37, 0.6, 0.02)
check(_ION, "spread of spectroscopic H2 values (15.4259 - 15.4256 eV), in meV", (15.4259 - 15.4256) * 1e3, 0.3, 0.01)

# --- library/work-function-thermionic.md -------------------------------------
_WFT = "library/work-function-thermionic.md §4.3"
_PHI_W = 4.55  # eV
check(_WFT, "30,500 K as an energy, in eV", 30500 * K_B / E_CHARGE, 2.63, 0.002)
check(_WFT, "barrier lowering by a thorium monolayer (4.55 - 2.63 eV)", 4.55 - 2.63, 1.92, 0.001)
check(_WFT, "W face spread, first set (5.25 - 4.47 eV)", 5.25 - 4.47, 0.78, 0.001)
check(_WFT, "W face spread, second set (5.05 - 4.39 eV)", 5.05 - 4.39, 0.66, 0.001)
check(_WFT, "kT at 300 K, in meV", K_B * 300 / E_CHARGE * 1e3, 25.85, 0.0002)
check(_WFT, "kT at 2500 K, in eV", K_B * 2500 / E_CHARGE, 0.2154, 0.0003)
check(_WFT, "phi / kT for W (4.55 eV) at 300 K", _PHI_W * E_CHARGE / (K_B * 300), 176, 0.001)
check(_WFT, "phi / kT for W (4.55 eV) at 2500 K", _PHI_W * E_CHARGE / (K_B * 2500), 21.1, 0.002)
check(_WFT, "Boltzmann factor for W at 300 K", exp(-_PHI_W * E_CHARGE / (K_B * 300)), 3.7e-77, 0.02)
check(_WFT, "Boltzmann factor for W at 2500 K", exp(-_PHI_W * E_CHARGE / (K_B * 2500)), 6.7e-10, 0.01)
check(_WFT, "phi / k for W, in K", _PHI_W * E_CHARGE / K_B, 5.28e4, 0.001)
check(_WFT, "Richardson constant 4 pi e m k^2 / h^3, in A m^-2 K^-2", 4 * pi * E_CHARGE * M_ELECTRON * K_B**2 / H_PLANCK**3, 1.2017e6, 0.0001)
check(_WFT, "A0 over the thoriated-tungsten A (120.17 / 3.0)", 120.17 / 3.0, 40, 0.005)
check(_WFT, "Schottky coefficient at 1 MV/m, in eV", schottky_ev(1e6), 0.0379, 0.002)
check(_WFT, "Schottky lowering at 1 MV/m, in eV", schottky_ev(1e6), 0.038, 0.005)
check(_WFT, "Schottky lowering at 10 MV/m, in eV", schottky_ev(1e7), 0.12, 0.001)
check(_WFT, "Schottky lowering at 50 MV/m, in eV (source 0.268)", schottky_ev(5e7), 0.268, 0.002)
check(_WFT, "Schottky lowering at 100 MV/m, in eV", schottky_ev(1e8), 0.38, 0.005)
check(_WFT, "Schottky lowering at 1 GV/m, in eV", schottky_ev(1e9), 1.2, 0.001)
check(_WFT, "Child-Langmuir prefactor (4 eps0 / 9) sqrt(2 e / m), in A V^-1.5", 4 * EPS_0 / 9 * sqrt(2 * E_CHARGE / M_ELECTRON), 2.334e-6, 0.0002)
check(_WFT, "photoelectric threshold 2575 angstrom, in eV", H_PLANCK * C_LIGHT / (2575e-10 * E_CHARGE), 4.81, 0.002)
check(_WFT, "W thermionic against photoelectric (4.81 - 4.71 eV)", 4.81 - 4.71, 0.1, 0.01)
check(_WFT, "Pd thermionic against photoelectric (4.99 - 4.97 eV)", 4.99 - 4.97, 0.02, 0.01)
