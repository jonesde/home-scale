# Checks for the lattice cluster of batch 2-A: library/magnetostriction.md,
# elasticity.md, melting.md, speed-of-sound.md, thermal-expansion.md and
# thermal-conductivity-phonon.md. Executed inside analysis/computed_checks.py,
# so check(), log, sqrt and the constants defined there are available.

# Kaye & Laby 2.2.2 (20 °C): Young's E, shear G, bulk K in Pa; Poisson ratio.
_E_NI_SOFT, _E_NI_HARD, _NU_NI = 199.5e9, 219.2e9, 0.312
_E_CU, _G_CU, _K_CU = 129.8e9, 48.3e9, 137.8e9
_E_AL, _G_AL, _K_AL = 70.3e9, 26.1e9, 75.5e9
_G_NI, _K_NI = 76.0e9, 177.3e9
_E_FE, _E_STEEL = 211.4e9, 211.9e9
# NIST X-ray table: density (kg/m3) and Z/A, which gives the molar mass (g/mol).
_RHO = {"Cu": 8960.0, "Al": 2699.0, "Fe": 7874.0, "Ni": 8902.0, "Zn": 7133.0, "Sn": 7310.0}
_MOLAR = {
    "Cu": 29 / 0.45636,
    "Al": 13 / 0.48181,
    "Fe": 26 / 0.46556,
    "Ni": 28 / 0.47708,
    "Zn": 30 / 0.45879,
    "Sn": 50 / 0.42120,
}
# NIST-JANAF: H - H(298.15 K) in kJ/mol at 300 K, crystal at T_m, liquid at T_m.
_JANAF = {
    "Cu": (0.045, 29.660, 42.798),
    "Al": (0.045, 17.982, 28.693),
    "Fe": (0.046, 58.645, 72.452),
    "Ni": (0.048, 47.361, 64.516),
    "Zn": (0.047, 10.825, 18.147),
}
# Johnson & Cook 1983 Table 1: A (MPa) and strain-rate constant C.
_JC = {
    "Cu": (90.0, 0.025),
    "Ni": (163.0, 0.006),
    "Armco": (175.0, 0.060),
    "1006": (350.0, 0.022),
    "2024": (265.0, 0.015),
    "4340": (792.0, 0.014),
}


def _poly(l100: float, l111: float) -> float:
    """Random-polycrystal average (2 λ100 + 3 λ111) / 5."""
    return (2 * l100 + 3 * l111) / 5


def _fusion_kj_kg(el: str) -> float:
    _, h_s, h_l = _JANAF[el]
    return (h_l - h_s) / _MOLAR[el] * 1e3


def _to_melt_kj_kg(el: str) -> float:
    h300, _, h_l = _JANAF[el]
    return (h_l - h300) / _MOLAR[el] * 1e3


# --- library/magnetostriction.md ------------------------------------------------
_MS = "library/magnetostriction.md §4.3"
check(_MS, "Ni polycrystal average, room temperature (ppm)", _poly(-46, -24), -33, 0.02)
check(_MS, "Ni polycrystal average, T near 0 (Nieves) (ppm)", _poly(-60, -35), -45, 0.02)
check(_MS, "Ni polycrystal average, 0 K (Hutchinson) (ppm)", _poly(-57, -28), -40, 0.02)
check(_MS, "Fe polycrystal average, room temperature (ppm)", _poly(20, -21), -4.6, 0.02)
check(_MS, "Terfenol-D polycrystal average (ppm)", _poly(90, 1640), 1020, 0.01)
check(_MS, "300 Oe as mu0 H (T)", 300e-4, 0.030, 0.01)
check(_MS, "650 Oe as mu0 H (T)", 650e-4, 0.065, 0.01)
check(_MS, "Ni sphere demagnetizing field Js/3 (T)", 0.60 / 3, 0.20, 0.01)
check(_MS, "Ni sphere applied field to saturate (T)", 0.60 / 3 + 300e-4, 0.23, 0.01)
check(_MS, "clamped stress E*lambda, soft Ni, 35 ppm (MPa)", _E_NI_SOFT * 35e-6 / 1e6, 7.0, 0.01)
check(_MS, "clamped stress E*lambda, hard Ni, 40 ppm (MPa)", _E_NI_HARD * 40e-6 / 1e6, 8.8, 0.01)
check(_MS, "film form lambda E/(1+nu), 35 ppm (MPa)", 35e-6 * _E_NI_SOFT / (1 + _NU_NI) / 1e6, 5.3, 0.01)
check(_MS, "7.0 MPa as a share of 163 MPa (%)", 7.0 / 163 * 100, 4.3, 0.02)
check(_MS, "8.8 MPa as a share of 163 MPa (%)", 8.8 / 163 * 100, 5.4, 0.02)
check(_MS, "Ni elastic strain at yield, 163 MPa / 199.5 GPa", 163e6 / _E_NI_SOFT, 8.2e-4, 0.01)
check(_MS, "yield strain over 35 ppm", 163e6 / _E_NI_SOFT / 35e-6, 23, 0.02)
check(_MS, "Ni thermal strain for 10 K", 13.4e-6 * 10, 1.34e-4, 0.001)
check(_MS, "10 K thermal strain over 35 ppm", 13.4e-6 * 10 / 35e-6, 3.8, 0.02)
check(_MS, "10 K thermal strain over 40 ppm", 13.4e-6 * 10 / 40e-6, 3.4, 0.02)
check(_MS, "temperature rise matching 35 ppm (K)", 35 / 13.4, 2.6, 0.02)
check(_MS, "temperature rise matching 40 ppm (K)", 40 / 13.4, 3.0, 0.02)
check(_MS, "elastic energy density at 35 ppm (J/m3)", 0.5 * _E_NI_SOFT * (35e-6) ** 2, 122, 0.01)
check(_MS, "Ni volumetric heat capacity (J/m3/K)", 8900 * 446, 3.97e6, 0.002)
check(_MS, "temperature rise equal to that energy (K)", 0.5 * _E_NI_SOFT * (35e-6) ** 2 / (8900 * 446), 3.1e-5, 0.02)
check(_MS, "Ni 0 K over room temperature, smallest ratio", 28 / 24, 1.2, 0.03)
check(_MS, "Ni 0 K over room temperature, largest ratio", 35 / 24, 1.5, 0.03)

# --- library/elasticity.md --------------------------------------------------------
_EL = "library/elasticity.md §4.3"
for _name, _e, _quoted in [
    ("Cu", _E_CU, 6.9e-4),
    ("Ni", _E_NI_SOFT, 8.2e-4),
    ("Armco", _E_FE, 8.3e-4),
    ("1006", _E_STEEL, 1.65e-3),
    ("2024", _E_AL, 3.8e-3),
    ("4340", _E_STEEL, 3.7e-3),
]:
    check(_EL, f"yield strain A/E, {_name}", _JC[_name][0] * 1e6 / _e, _quoted, 0.02)
for _name, _q6, _q9 in [
    ("Cu", 1.35, 1.52),
    ("Ni", 1.08, 1.12),
    ("Armco", 1.83, 2.24),
    ("1006", 1.30, 1.46),
    ("2024", 1.21, 1.31),
    ("4340", 1.19, 1.29),
]:
    check(_EL, f"Johnson-Cook rate factor at 1e6 /s, {_name}", 1 + _JC[_name][1] * log(1e6), _q6, 0.005)
    check(_EL, f"Johnson-Cook rate factor at 1e9 /s, {_name}", 1 + _JC[_name][1] * log(1e9), _q9, 0.005)
check(_EL, "ideal shear strength over G, Al (%)", 1.85e9 / _G_AL * 100, 7.1, 0.02)
check(_EL, "ideal shear strength over G, Cu (%)", 2.65e9 / _G_CU * 100, 5.5, 0.02)
check(_EL, "Cu ideal shear over shear yield, Tresca", 2650 / (90 / 2), 59, 0.02)
check(_EL, "Cu ideal shear over shear yield, von Mises", 2650 / (90 / sqrt(3)), 51, 0.02)
check(_EL, "Al ideal shear over 2024 shear yield, Tresca", 1850 / (265 / 2), 14, 0.02)
check(_EL, "Al ideal shear over 2024 shear yield, von Mises", 1850 / (265 / sqrt(3)), 12, 0.02)
check(_EL, "erosion over critical velocity, sqrt(4.8/1.2)", sqrt(4.8 / 1.2), 2.0, 0.001)
check(_EL, "erosion over critical velocity, sqrt(1.2/0.3)", sqrt(1.2 / 0.3), 2.0, 0.001)
for _name, _k, _c, _v in [("Cu", _K_CU, 3920, 588), ("Al", _K_AL, 5290, 793), ("Ni", _K_NI, 4460, 669)]:
    check(_EL, f"bulk sound speed sqrt(K/rho), {_name} (m/s)", sqrt(_k / _RHO[_name]), _c, 0.002)
    check(_EL, f"0.15 x bulk sound speed, {_name} (m/s)", 0.15 * sqrt(_k / _RHO[_name]), _v, 0.002)


def _schmidt(su_pa: float, rho: float, cp: float, tm: float, f1: float = 1.2, f2: float = 0.3) -> float:
    """Schmidt et al. 2006 critical velocity for a particle at 293 K (m/s)."""
    return sqrt(f1 * 4 * su_pa / rho + f2 * cp * (tm - 293.0))


check(_EL, "Schmidt formula, Cu, tensile strength 200 MPa (m/s)", _schmidt(200e6, 8960, 383, 1358), 479, 0.003)
check(_EL, "Schmidt formula, Cu, tensile strength 400 MPa (m/s)", _schmidt(400e6, 8960, 383, 1358), 580, 0.003)
check(_EL, "Schmidt formula, Al, tensile strength 90 MPa (m/s)", _schmidt(90e6, 2699, 875, 933.45), 573, 0.003)
check(_EL, "Schmidt formula, Al, tensile strength 150 MPa (m/s)", _schmidt(150e6, 2699, 875, 933.45), 659, 0.003)
check(_EL, "Schmidt erosion velocity, Cu, 200 MPa (m/s)", _schmidt(200e6, 8960, 383, 1358, 4.8, 1.2), 958, 0.003)

# --- library/melting.md -----------------------------------------------------------
_ME = "library/melting.md §4.3"
for _el, _fus_mol, _fus_kg, _tot_mol, _tot_kg, _tot_m3 in [
    ("Cu", 13.14, 207, 42.75, 673, 6.03),
    ("Al", 10.71, 397, 28.65, 1062, 2.87),
    ("Fe", 13.81, 247, 72.41, 1297, 10.21),
    ("Ni", 17.16, 292, 64.47, 1098, 9.78),
    ("Zn", 7.32, 112, 18.10, 277, 1.97),
]:
    _h300, _hs, _hl = _JANAF[_el]
    check(_ME, f"enthalpy of fusion, {_el} (kJ/mol)", _hl - _hs, _fus_mol, 0.001)
    check(_ME, f"enthalpy of fusion, {_el} (kJ/kg)", _fusion_kj_kg(_el), _fus_kg, 0.003)
    check(_ME, f"300 K to liquid at T_m, {_el} (kJ/mol)", _hl - _h300, _tot_mol, 0.001)
    check(_ME, f"300 K to liquid at T_m, {_el} (kJ/kg)", _to_melt_kj_kg(_el), _tot_kg, 0.002)
    check(_ME, f"300 K to liquid at T_m, {_el} (GJ/m3)", _to_melt_kj_kg(_el) * _RHO[_el] / 1e6, _tot_m3, 0.003)
for _el, _share in [("Cu", 31), ("Al", 37), ("Fe", 19), ("Ni", 27), ("Zn", 40)]:
    check(_ME, f"fusion share of the 300 K to melt enthalpy, {_el} (%)", _fusion_kj_kg(_el) / _to_melt_kj_kg(_el) * 100, _share, 0.03)
# Tin: two heat-capacity points (K&L 2.3.6), extrapolated linearly, plus 7.0 kJ/mol.
_cp_sn_300 = 0.221 + (0.240 - 0.221) * (300 - 273) / 100
_cp_sn_tm = 0.221 + (0.240 - 0.221) * (505.078 - 273) / 100
_sn_sensible = (_cp_sn_300 + _cp_sn_tm) / 2 * (505.078 - 300)
_sn_fusion = 7.0 / _MOLAR["Sn"] * 1e3
check(_ME, "Sn sensible heat 300 K to T_m (kJ/kg)", _sn_sensible, 50, 0.02)
check(_ME, "Sn enthalpy of fusion (kJ/kg)", _sn_fusion, 59, 0.01)
check(_ME, "Sn 300 K to liquid (kJ/kg)", _sn_sensible + _sn_fusion, 109, 0.01)
check(_ME, "Sn 300 K to liquid (GJ/m3)", (_sn_sensible + _sn_fusion) * _RHO["Sn"] / 1e6, 0.80, 0.01)
check(_ME, "Al melting-point shift per kbar (K)", 7.0e-8 * 1e8, 7.0, 0.001)
check(_ME, "Sn melting-point shift per kbar (K)", 3.3e-8 * 1e8, 3.3, 0.001)
check(_ME, "Zn melting-point shift per kbar (K)", 4.3e-8 * 1e8, 4.3, 0.001)
check(_ME, "Al melting-point shift per atmosphere (mK)", 7.0e-8 * 101325 * 1e3, 7.1, 0.01)
check(_ME, "Au 2.5 nm corrected melting point (K)", 47 + 273.15, 320, 0.002)
check(_ME, "Au 2.5 nm uncorrected melting point (K)", 400 + 273.15, 673, 0.002)
check(_ME, "Au 4.1 nm transition (K)", 509 + 273.15, 782, 0.002)
check(_ME, "Au 1.6 nm transition (K)", 132 + 273.15, 405, 0.002)
check(_ME, "Au bulk melting point (K)", 1064 + 273.15, 1337, 0.001)
check(_ME, "Au 2.5 nm corrected, share of bulk T_m", 320 / 1337, 0.25, 0.05)
check(_ME, "Au 2.5 nm uncorrected, share of bulk T_m", 673 / 1337, 0.50, 0.02)
check(_ME, "Au 4.1 nm transition, share of bulk T_m (%)", 782 / 1337 * 100, 58, 0.02)
check(_ME, "Au 1.6 nm transition, share of bulk T_m (%)", 405 / 1337 * 100, 30, 0.02)
check(_ME, "Cu: JANAF minus ITS-90 melting point (K)", 1358 - 1357.77, 0.3, 0.3)

# --- library/speed-of-sound.md ----------------------------------------------------
_SS = "library/speed-of-sound.md §4.3"
check(_SS, "dry air at 20 C from 331.46 m/s at 0 C (m/s)", 331.46 * sqrt(293.15 / 273.15), 343.4, 0.0005)
check(_SS, "Cu v_L from K and G (m/s)", sqrt((_K_CU + 4 * _G_CU / 3) / _RHO["Cu"]), 4750, 0.002)
check(_SS, "Cu v_T from G (m/s)", sqrt(_G_CU / _RHO["Cu"]), 2322, 0.002)
check(_SS, "Al v_L from K and G (m/s)", sqrt((_K_AL + 4 * _G_AL / 3) / _RHO["Al"]), 6393, 0.002)
check(_SS, "Al v_T from G (m/s)", sqrt(_G_AL / _RHO["Al"]), 3110, 0.002)
check(_SS, "Ni v_L from K and G (m/s)", sqrt((_K_NI + 4 * _G_NI / 3) / _RHO["Ni"]), 5595, 0.002)
check(_SS, "Ni v_T from G (m/s)", sqrt(_G_NI / _RHO["Ni"]), 2922, 0.002)
check(_SS, "5 m of air at 343.5 m/s (ms)", 5 / 343.5 * 1e3, 14.6, 0.005)
check(_SS, "5 m of steel rod at 5196 m/s (ms)", 5 / 5196 * 1e3, 0.96, 0.005)
check(_SS, "5 cm of steel rod at 5196 m/s (us)", 0.05 / 5196 * 1e6, 9.6, 0.005)
check(_SS, "mild steel v_T over v_L", 3235 / 5960, 0.54, 0.01)
check(_SS, "CO2 speed step across relaxation (%)", (293 / 280 - 1) * 100, 5, 0.1)
check(_SS, "largest gap between computed and measured solid speeds (%)", (6393 / 6374 - 1) * 100, 0.3, 0.05)

# --- library/thermal-expansion.md -------------------------------------------------
_TE = "library/thermal-expansion.md §4.3"
check(_TE, "Cu strain for 100 K", 16.5e-6 * 100, 1.65e-3, 0.001)
check(_TE, "Al strain for 100 K", 23.1e-6 * 100, 2.31e-3, 0.001)
check(_TE, "Ni strain for 10 K", 13.4e-6 * 10, 1.34e-4, 0.001)
check(_TE, "Fe over Invar expansivity at 293 K", 11.8 / 0.13, 91, 0.01)
check(_TE, "Invar expansivity, 500 K over 293 K", 5.1 / 0.13, 39, 0.01)
check(_TE, "Al expansivity, 800 K over 100 K", 34.0 / 12.2, 2.8, 0.01)
check(_TE, "Cu 100 K thermal strain over yield strain", 16.5e-6 * 100 / (90e6 / _E_CU), 2.4, 0.02)
check(_TE, "Cu yield strain 90 MPa / 129.8 GPa", 90e6 / _E_CU, 6.9e-4, 0.01)

# --- library/thermal-conductivity-phonon.md ---------------------------------------
_TC = "library/thermal-conductivity-phonon.md §4.3"
check(_TC, "410 W/cm/K in W/m/K", 410 * 100, 41000, 0.001)
check(_TC, "enriched diamond at 104 K over natural at room temperature", 41000 / 2200, 19, 0.02)
check(_TC, "isotopically pure over natural diamond", 3100 / 2200, 1.4, 0.01)
check(_TC, "phonon share of kappa, Cu (%)", 17.61 / 378.52 * 100, 4.7, 0.02)
check(_TC, "phonon share of kappa, Al (%)", 8.14 / 233.89 * 100, 3.5, 0.02)
check(_TC, "phonon share of kappa, Ni (%)", 14.50 / 115.59 * 100, 12.5, 0.02)
check(_TC, "glass mean free path 1e-4 cm in um", 1e-4 * 1e4, 1.0, 0.001)
