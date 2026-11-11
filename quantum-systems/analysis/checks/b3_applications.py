# Checks for the application files revised on 2026-11-11 (batch 3):
# application/EM-CSAM.md, EM-CSAM-Pitch.md, bonded-magnets.md, thin-film-optics.md,
# percolation-dual-switch.md, depolarization-fuse.md.
# Executed in the namespace of analysis/computed_checks.py: uses check, K_B, MU_0,
# pi and sqrt from that module. Every other name is defined here with a _B3 prefix,
# so this file does not depend on the load order of the other check files.
#
# Three kinds of input appear below and are kept apart in the comments:
#   library  - a number stated in a sourced library file (file named)
#   hardware - a planning value or model result from em-csam/ (not a measurement)
#   computed - arithmetic on the two above

import cmath as _b3_cmath

# --- library inputs ------------------------------------------------------------
# electrical-resistivity.md §4.3: specific action at the start of melting, A^2 s m^-4
_B3_ACTION = {"Cu": 8.05e16, "Al": 2.52e16, "Ni": 1.72e16, "Fe": 1.28e16}
_B3_ACTION_FE_MELTED = 1.47e16
_B3_ACTION_FE_BURST = 3.61e16
_B3_RHO_E_CU = 1.678e-8  # ohm m at 293 K
# melting.md §4.3: room-temperature densities used for its volumetric column, kg m^-3
_B3_DENSITY = {"Cu": 8960.0, "Al": 2699.0, "Ni": 8902.0, "Fe": 7874.0}
# melting.md §4.3: 300 K to fully liquid, and enthalpy of fusion, kJ kg^-1
_B3_TO_LIQUID = {"Cu": 673.0, "Al": 1062.0, "Fe": 1297.0}
_B3_FUSION = {"Cu": 207.0, "Al": 397.0, "Fe": 247.0}
# skin-effect.md §4.3: copper diffusion coefficient lambda = 0.116 sqrt(t), SI
_B3_LAMBDA_CU = 0.116
# elasticity.md §4.3
_B3_BULK_SOUND_CU = 3920.0  # sqrt(K/rho), m/s

# --- hardware inputs (em-csam/EM-CSAM-ConceptTechnical.md §3, tools/shot_model.py) ---
_B3_LPRIME = 0.4e-6  # H/m, planning value; range 0.3-0.5
_B3_BORE = 0.5e-3  # m, square bore
_B3_SLUG = 1.0e-3  # m, reference slug length
_B3_BARREL = 0.1  # m


def _b3_v_melt(metal: str, lprime: float = _B3_LPRIME, length: float = _B3_SLUG) -> float:
    """Velocity at which a solid slug on plain rails reaches melt-onset action.

    Momentum: integral I^2 dt = 2 m v / L'. Current crosses a section length x height,
    m = density x length x height x gap, square bore (height = gap), so
    g = 2 density v / (L' length).
    """
    return _B3_ACTION[metal] * lprime * length / (2.0 * _B3_DENSITY[metal])


def _b3_action_fraction(metal: str, v: float) -> float:
    return v / _b3_v_melt(metal)


def _b3_melt_onset_kj(metal: str) -> float:
    """Heat from 300 K to the melting point, before fusion, kJ/kg."""
    return _B3_TO_LIQUID[metal] - _B3_FUSION[metal]


def _b3_r_for_heat(e_kj_kg: float, v: float, lprime: float = _B3_LPRIME) -> float:
    """Slug resistance (ohm) at which Joule heat per kg, 2 R v / L', equals e."""
    return e_kj_kg * 1e3 * lprime / (2.0 * v)


def _b3_film_r_pct(n: float, k: float, d_nm: float, lam_nm: float = 550.0, n_sub: float = 1.0) -> float:
    """Reflectance (%) of one absorbing layer, normal incidence (Airy formula)."""
    nn = complex(n, k)
    beta = 2.0 * pi * nn * d_nm / lam_nm
    r01 = (1.0 - nn) / (1.0 + nn)
    r12 = (nn - n_sub) / (nn + n_sub)
    phase = _b3_cmath.exp(2j * beta)
    return 100.0 * abs((r01 + r12 * phase) / (1.0 + r01 * r12 * phase)) ** 2


# --- application/EM-CSAM.md §2.1 -------------------------------------------------
_B3_21 = "application/EM-CSAM.md §2.1"
for _v, _ka, _ms in ((300.0, 2.1, 0.67), (500.0, 3.5, 0.40), (800.0, 5.7, 0.25)):
    _force = 2e-6 * _v**2 / (2.0 * _B3_BARREL)  # 2 mg slug, constant acceleration
    check(_B3_21, f"constant current for 2 mg at {_v:g} m/s (kA)", sqrt(2.0 * _force / _B3_LPRIME) / 1e3, _ka, 0.03)
    check(_B3_21, f"transit time at {_v:g} m/s (ms)", 2.0 * _B3_BARREL / _v * 1e3, _ms, 0.02)

# --- application/EM-CSAM.md §2.2 -------------------------------------------------
_B3_22 = "application/EM-CSAM.md §2.2"
for _v, _mm in ((300.0, 0.42), (800.0, 0.26)):
    check(_B3_22, f"velocity skin depth 2 lambda, 1 mm contact at {_v:g} m/s (mm)", 2 * _B3_LAMBDA_CU * sqrt(1e-3 / _v) * 1e3, _mm, 0.02)
for _metal, _mid, _lo, _hi in (("Cu", 1800, 1350, 2250), ("Al", 1870, 1400, 2330), ("Ni", 390, 290, 480), ("Fe", 325, 245, 405)):
    check(_B3_22, f"melt-onset velocity, {_metal}, 1 mm slug, L' 0.4 (m/s)", _b3_v_melt(_metal), _mid, 0.015)
    check(_B3_22, f"melt-onset velocity, {_metal}, L' 0.3 (m/s)", _b3_v_melt(_metal, 0.3e-6), _lo, 0.015)
    check(_B3_22, f"melt-onset velocity, {_metal}, L' 0.5 (m/s)", _b3_v_melt(_metal, 0.5e-6), _hi, 0.015)
for _v, _pct in ((300.0, 17), (500.0, 28), (800.0, 45), (1000.0, 56)):
    check(_B3_22, f"Cu share of melt-onset action at {_v:g} m/s (%)", 100 * _b3_action_fraction("Cu", _v), _pct, 0.03)
check(_B3_22, "Fe action at 500 m/s over melt-onset action", _b3_action_fraction("Fe", 500.0), 1.5, 0.03)
check(_B3_22, "Fe action at 500 m/s over burst action (%)", 100 * _b3_action_fraction("Fe", 500.0) * _B3_ACTION["Fe"] / _B3_ACTION_FE_BURST, 55, 0.02)
check(_B3_22, "Fe melting-complete over melt-onset action", _B3_ACTION_FE_MELTED / _B3_ACTION["Fe"], 1.15, 0.01)
check(_B3_22, "current density, 1 kA through 1 mm x 0.5 mm (kA/mm2)", 1e3 / (_B3_SLUG * _B3_BORE) / 1e9, 2, 0.001)
check(_B3_22, "current density, 4 kA through 1 mm x 0.5 mm (kA/mm2)", 4e3 / (_B3_SLUG * _B3_BORE) / 1e9, 8, 0.001)
check(_B3_22, "earlier hardware table at L' 0.45, Cu (m/s; was quoted as about 2000)", _b3_v_melt("Cu", 0.45e-6), 2000, 0.02)
check(_B3_22, "earlier hardware table at L' 0.45, Fe (m/s; was quoted as about 370)", _b3_v_melt("Fe", 0.45e-6), 370, 0.02)
check(_B3_22, "Cu heat to melt onset, 673 - 207 (kJ/kg)", _b3_melt_onset_kj("Cu"), 466, 0.001)
for _v, _onset, _liquid in ((300.0, 0.31, 0.45), (500.0, 0.19, 0.27)):
    check(_B3_22, f"R for melt onset at {_v:g} m/s (mOhm)", _b3_r_for_heat(466.0, _v) * 1e3, _onset, 0.03)
    check(_B3_22, f"R for fully liquid at {_v:g} m/s (mOhm)", _b3_r_for_heat(673.0, _v) * 1e3, _liquid, 0.03)
_B3_R_SOLID = _B3_RHO_E_CU * _B3_BORE / (_B3_SLUG * _B3_BORE)  # current crosses the 0.5 mm gap
check(_B3_22, "solid Cu slug resistance across the gap (mOhm)", _B3_R_SOLID * 1e3, 0.017, 0.02)
check(_B3_22, "melt-onset R over solid R at 500 m/s", _b3_r_for_heat(466.0, 500.0) / _B3_R_SOLID, 11, 0.02)
check(_B3_22, "melt-onset R over solid R at 300 m/s", _b3_r_for_heat(466.0, 300.0) / _B3_R_SOLID, 19, 0.03)
_B3_MEAN_RHO = 466e3 * _B3_DENSITY["Cu"] / _B3_ACTION["Cu"]  # energy per volume over action
check(_B3_22, "mean resistivity implied by Cu action and enthalpy (ohm m)", _B3_MEAN_RHO, 5.2e-8, 0.01)
check(_B3_22, "that mean over the 293 K resistivity", _B3_MEAN_RHO / _B3_RHO_E_CU, 3.1, 0.01)
check(_B3_22, "rail loading, 1 kA over 0.5 mm of rail height (kA/mm)", 1.0 / 0.5, 2, 0.001)
check(_B3_22, "rail loading, 4 kA over 0.5 mm of rail height (kA/mm)", 4.0 / 0.5, 8, 0.001)
check(_B3_22, "2 kA/mm as a share of 44 kA/mm (%)", 100 * 2 / 44, 5, 0.1)
check(_B3_22, "8 kA/mm as a share of 44 kA/mm (%)", 100 * 8 / 44, 18, 0.02)

# --- application/EM-CSAM.md §2.3 -------------------------------------------------
_B3_23 = "application/EM-CSAM.md §2.3"
check(_B3_23, "Cu margin against 570 m/s", 1800 / 570, 3.2, 0.02)
check(_B3_23, "Cu margin against 500 m/s", 1800 / 500, 3.6, 0.01)
check(_B3_23, "Cu margin against 460 m/s", 1800 / 460, 3.9, 0.01)
check(_B3_23, "Al margin against 825 m/s", 1870 / 825, 2.3, 0.02)
check(_B3_23, "Al margin against 775 m/s", 1870 / 775, 2.4, 0.01)
check(_B3_23, "Al margin against 660 m/s", 1870 / 660, 2.8, 0.02)
check(_B3_23, "Al margin against 620 m/s", 1870 / 620, 3.0, 0.01)
check(_B3_23, "Fe margin against 750 m/s", 325 / 750, 0.43, 0.01)
check(_B3_23, "Fe margin against 700 m/s", 325 / 700, 0.46, 0.01)
for _v, _kj, _pct in ((300.0, 45, 10), (500.0, 125, 27), (800.0, 320, 69)):
    check(_B3_23, f"kinetic energy at {_v:g} m/s (kJ/kg)", _v**2 / 2 / 1e3, _kj, 0.001)
    check(_B3_23, f"that as a share of Cu melt-onset heat (%)", 100 * _v**2 / 2 / 466e3, _pct, 0.04)
check(_B3_23, "Al heat to melt onset, 1062 - 397 (kJ/kg)", _b3_melt_onset_kj("Al"), 665, 0.001)
check(_B3_23, "Fe heat to melt onset, 1297 - 247 (kJ/kg)", _b3_melt_onset_kj("Fe"), 1050, 0.001)
check(_B3_23, "velocity whose kinetic energy equals Cu melt-onset heat (m/s)", sqrt(2 * 466e3), 965, 0.002)
check(_B3_23, "same for Al (m/s)", sqrt(2 * 665e3), 1150, 0.005)
check(_B3_23, "same for Fe (m/s)", sqrt(2 * 1050e3), 1450, 0.002)
_B3_LEFT = 466.0 - 570.0**2 / 2 / 1e3  # kJ/kg left for Joule heat at 570 m/s
check(_B3_23, "Cu heat budget left at 570 m/s (kJ/kg)", _B3_LEFT, 304, 0.003)
check(_B3_23, "R that uses that budget at 570 m/s (mOhm)", _b3_r_for_heat(_B3_LEFT, 570.0) * 1e3, 0.11, 0.04)
check(_B3_23, "that R over the solid slug", _b3_r_for_heat(_B3_LEFT, 570.0) / _B3_R_SOLID, 6.4, 0.02)
check(_B3_23, "200 m/s over the bulk sound speed of Cu (%)", 100 * 200 / _B3_BULK_SOUND_CU, 5, 0.03)
check(_B3_23, "800 m/s over the bulk sound speed of Cu (%)", 100 * 800 / _B3_BULK_SOUND_CU, 20, 0.03)
check(_B3_23, "acoustic transit of a 20 um particle (ns)", 20e-6 / _B3_BULK_SOUND_CU * 1e9, 5, 0.03)
check(_B3_23, "acoustic transit of a 1 mm slug (us)", 1e-3 / _B3_BULK_SOUND_CU * 1e6, 0.26, 0.03)

# --- application/EM-CSAM.md §2.4 -------------------------------------------------
_B3_24 = "application/EM-CSAM.md §2.4"
check(_B3_24, "air Paschen floor 327 V over a 55 V bank", 327 / 55, 6, 0.02)
check(_B3_24, "air Paschen floor 352 V over an 18 V bank", 352 / 18, 20, 0.03)
check(_B3_24, "gap at which 18 V reaches 350 V/um (um)", 18 / 350, 0.05, 0.03)
check(_B3_24, "gap at which 55 V reaches 100 V/um (um)", 55 / 100, 0.55, 0.001)
check(_B3_24, "plasma armature across 0.5 mm: 45 V falls plus 141 V/cm (V)", 45 + 141 * 0.05, 52, 0.002)
check(_B3_24, "2 kA/mm2 in kA/cm2", 2 * 100, 200, 0.001)
check(_B3_24, "8 kA/mm2 in kA/cm2", 8 * 100, 800, 0.001)
check(_B3_24, "one gram-force per ampere at 1 kA (N)", 9.80665e-3 * 1e3, 10, 0.02)
check(_B3_24, "one gram-force per ampere at 4 kA (N)", 9.80665e-3 * 4e3, 39, 0.01)
check(_B3_24, "Lorentz force, 2 mg to 300 m/s in 100 mm (N)", 2e-6 * 300**2 / (2 * _B3_BARREL), 0.9, 0.001)
check(_B3_24, "Lorentz force, 2 mg to 800 m/s in 100 mm (N)", 2e-6 * 800**2 / (2 * _B3_BARREL), 6.4, 0.001)

# --- application/EM-CSAM.md §3.3 -------------------------------------------------
check("application/EM-CSAM.md §3.3", "current at which a 0.8 T per 2 kA rail field reaches 0.23 T (kA)", 0.23 / 0.8 * 2, 0.6, 0.05)

# --- application/EM-CSAM-Pitch.md §6.1 and bonded-magnets.md §1 --------------------
_B3_FER = "application/EM-CSAM-Pitch.md §6.1; application/bonded-magnets.md §1"
check(_B3_FER, "hard ferrite 25 kT sphere at 300 K, K1 0.36 MJ/m3 (nm)", (150 * K_B * 300 / (pi * 0.36e6)) ** (1 / 3) * 1e9, 8.2, 0.005)
check(_B3_FER, "hard ferrite 25 kT sphere at 300 K, K1 0.32 MJ/m3 (nm)", (150 * K_B * 300 / (pi * 0.32e6)) ** (1 / 3) * 1e9, 8.5, 0.005)
# permanent-magnet-latch.md quotes "about 29 000 kT"; K1 is 4.3-4.9 MJ/m3, mid-range used here.
check("application/bonded-magnets.md §1", "KV/kT of a 30 nm Nd2Fe14B cube at 300 K, K1 4.6 MJ/m3", 4.6e6 * (30e-9) ** 3 / (K_B * 300), 29000, 0.05)
_B3_P = "application/EM-CSAM-Pitch.md"
check(_B3_P, "other pulse cuts over the 2 sqrt(Dt) rule, low end (0.80 / 2)", 0.80 / 2, 0.4, 0.001)
check(_B3_P, "other pulse cuts over the 2 sqrt(Dt) rule, high end (1.27 / 2)", 1.27 / 2, 0.65, 0.03)

# --- application/thin-film-optics.md, percolation-dual-switch.md -------------------
# Guards on the reflectance figures those files repeat from reflection.md §4.3
# (Ag, Johnson and Christy, 0.060 + 3.597i at 550 nm).
_B3_TFO = "application/thin-film-optics.md; application/percolation-dual-switch.md"
for _d, _free, _glass in ((5.0, 14, 14), (10.0, 39, 34), (20.0, 74, 69), (50.0, 96, 96)):
    check(_B3_TFO, f"Ag film {_d:g} nm, free-standing R (%)", _b3_film_r_pct(0.060, 3.597, _d), _free, 0.04)
    check(_B3_TFO, f"Ag film {_d:g} nm on glass, R from the air side (%)", _b3_film_r_pct(0.060, 3.597, _d, n_sub=1.5), _glass, 0.04)

# --- application/depolarization-fuse.md §1 ----------------------------------------
_B3_DEP = "application/depolarization-fuse.md §1"
_B3_EPS0 = 1.0 / (MU_0 * 299792458.0**2)
check(_B3_DEP, "uncompensated field P/eps0 for P = 0.263 C/m2 (V/m)", 0.263 / _B3_EPS0, 3.0e10, 0.02)
check(_B3_DEP, "3e7 V/m as a share of it (%)", 100 * 3e7 / (0.263 / _B3_EPS0), 0.10, 0.03)
check(_B3_DEP, "4e7 V/m as a share of it (%)", 100 * 4e7 / (0.263 / _B3_EPS0), 0.13, 0.04)
check(_B3_DEP, "six unit cells of 0.40 nm (nm)", 6 * 0.40, 2.4, 0.001)

# --- em-csam hardware notes: qualifiers added 2026-11-11 ---------------------
_HW3 = "em-csam/EM-CSAM-ConceptTechnical.md §3.5, DesignReview-2026-11.md B4"
check(_HW3, "Cu melt onset per mm at L' = 0.45 (m/s), the earlier table's value", 8.0e16 * 1e-3 * 0.45e-6 / (2 * 8960), 2000)
check(_HW3, "Cu melt onset per mm at L' = 0.40 (m/s)", 8.0e16 * 1e-3 * 0.40e-6 / (2 * 8960), 1800)
check(_HW3, "Cu margin against the measured 570 m/s at L' = 0.40", 8.0e16 * 1e-3 * 0.40e-6 / (2 * 8960) / 570, 3.15)
check(_HW3, "Paschen minimum over bank voltage, 327 V / 55 V", 327 / 55, 6, 0.06)
check(_HW3, "Paschen minimum over bank voltage, 352 V / 18 V", 352 / 18, 20)
