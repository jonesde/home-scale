# Checks for the threshold batch (4): photoelectric-threshold,
# semiconductor-gap-absorption, x-ray-absorption-edge, pair-production,
# photoconductivity, coulomb-blockade, coherent-neutrino-scattering.
# Executed inside analysis/computed_checks.py; uses check, K_B and H_PLANCK
# from it. Names defined here carry a _T4 prefix so they cannot collide with
# constants defined by the other files in this directory.

_T4_E = 1.602176634e-19  # C, exact
_T4_C = 299792458.0  # m/s, exact
_T4_HC_EV_NM = H_PLANCK * _T4_C / _T4_E * 1e9  # eV nm
_T4_H_EV = 4.135667696e-15  # eV s, CODATA 2022
_T4_HBAR_EV = 6.582119569e-16  # eV s, CODATA 2022
_T4_K_EV = K_B / _T4_E  # eV/K
_T4_ME = 0.51099895069  # MeV, CODATA 2022
_T4_MP = 938.27208943  # MeV, CODATA 2022
_T4_MN = 939.56542194  # MeV, CODATA 2022
_T4_U = 931.49410372  # MeV, CODATA 2022

# --- library/photoelectric-threshold.md ---------------------------------------
_T4_PE = "library/photoelectric-threshold.md §4.3"
check(_T4_PE, "hc (eV nm)", _T4_HC_EV_NM, 1239.84, rtol=1e-5)
for _name, _phi, _lam in [
    ("Cs", 1.95, 636),
    ("K", 2.29, 541),
    ("Al", 4.25, 292),
    ("Ag", 4.33, 286),
    ("W and Cu", 4.55, 272),
    ("Pt", 5.41, 229),
]:
    check(_T4_PE, f"threshold wavelength, {_name} (nm)", _T4_HC_EV_NM / _phi, _lam, rtol=0.005)
check(_T4_PE, "Millikan h below the exact value (%)", (6.62607015 - 6.57) / 6.62607015 * 100, 0.8, rtol=0.1)
check(_T4_PE, "kT at 300 K (meV)", _T4_K_EV * 300 * 1e3, 25.85, rtol=1e-3)
check(_T4_PE, "kT(300 K) / 4.55 eV (%)", _T4_K_EV * 300 / 4.55 * 100, 0.57, rtol=0.02)
check("library/photoelectric-threshold.md §4.5", "W(100) minus polycrystalline W (eV)", 4.65 - 4.55, 0.10, rtol=0.01)
check("analysis/fragments/gold.jsonl", "4.55 eV in joules", 4.55 * _T4_E, 7.29e-19, rtol=0.002)

# --- library/semiconductor-gap-absorption.md ----------------------------------
_T4_SG = "library/semiconductor-gap-absorption.md §4.3"
for _name, _eg, _lam in [
    ("Si", 1.12, 1107),
    ("Ge", 0.661, 1876),
    ("GaAs", 1.424, 871),
    ("diamond, 5.6 eV", 5.6, 221),
    ("diamond, 5.46 eV", 5.46, 227),
]:
    check(_T4_SG, f"hc/Eg, {_name} (nm)", _T4_HC_EV_NM / _eg, _lam, rtol=0.003)
check(_T4_SG, "Varshni Si at 300 K (eV)", 1.17 - 4.73e-4 * 300**2 / (300 + 636), 1.125, rtol=0.001)
check(_T4_SG, "Varshni Ge at 300 K (eV)", 0.742 - 4.8e-4 * 300**2 / (300 + 235), 0.661, rtol=0.001)
check(_T4_SG, "Varshni GaAs at 300 K (eV)", 1.519 - 5.405e-4 * 300**2 / (300 + 204), 1.422, rtol=0.001)
check(_T4_SG, "Si gap, 0 K minus 300 K (meV)", (1.17 - 1.12) * 1e3, 50, rtol=0.01)
check(_T4_SG, "Ge gap, 0 K minus 300 K (meV)", (0.742 - 0.661) * 1e3, 81, rtol=0.01)
check(_T4_SG, "GaAs gap, 0 K minus 300 K (meV)", (1.519 - 1.424) * 1e3, 95, rtol=0.01)
check(_T4_SG, "Si 1/alpha at 550 nm (um)", 1e4 / 6.39e3, 1.6, rtol=0.03)
check(_T4_SG, "Si 1/alpha at 1000 nm (um)", 1e4 / 64, 156, rtol=0.005)
check(_T4_SG, "Si 1/alpha at 1100 nm (mm)", 10 / 3.5, 2.9, rtol=0.02)
check(_T4_SG, "Si 1/alpha at 1200 nm (cm)", 1 / 0.022, 45, rtol=0.02)
check(_T4_SG, "photon energy at 1200 nm (eV)", _T4_HC_EV_NM / 1200, 1.033, rtol=0.001)
check(_T4_SG, "1.12 eV minus the 1200 nm photon (meV)", (1.12 - _T4_HC_EV_NM / 1200) * 1e3, 87, rtol=0.01)
check(_T4_SG, "Si alpha(550 nm) / alpha(1200 nm)", 6.39e3 / 0.022, 2.9e5, rtol=0.02)
check("analysis/fragments/threshold-conversion.jsonl", "1.12 eV in joules", 1.12 * _T4_E, 1.794e-19, rtol=0.001)

# --- library/x-ray-absorption-edge.md -----------------------------------------
_T4_XR = "library/x-ray-absorption-edge.md §4.3"
check(_T4_XR, "Cu K jump ratio", 278.4 / 38.29, 7.27, rtol=0.002)
check(_T4_XR, "Cu L1 jump ratio", 9347 / 8242, 1.13, rtol=0.005)
check(_T4_XR, "Cu K wavelength (nm)", _T4_HC_EV_NM / 8978.9, 0.138, rtol=0.003)
check(_T4_XR, "hbar / 1.55 eV (fs)", _T4_HBAR_EV / 1.55 * 1e15, 0.42, rtol=0.02)
check(_T4_XR, "1.55 eV / 8978.9 eV", 1.55 / 8978.9, 1.7e-4, rtol=0.02)
check(_T4_XR, "h / 10 keV (s)", _T4_H_EV / 1e4, 4.1e-19, rtol=0.01)
check("analysis/fragments/threshold-conversion.jsonl", "8.9789 keV in joules", 8978.9 * _T4_E, 1.439e-15, rtol=0.001)

# --- library/pair-production.md -----------------------------------------------
_T4_PP = "library/pair-production.md §4.3"
check(_T4_PP, "2 me c^2 (MeV)", 2 * _T4_ME, 1.0220, rtol=1e-5)
check(_T4_PP, "4 me c^2 (MeV)", 4 * _T4_ME, 2.0440, rtol=1e-5)
check(_T4_PP, "recoil term, proton (keV)", 2 * _T4_ME**2 / _T4_MP * 1e3, 0.56, rtol=0.01)
check(_T4_PP, "recoil term, 12C (eV)", 2 * _T4_ME**2 / (12 * _T4_U) * 1e6, 47, rtol=0.01)
check(_T4_PP, "me c^2 (keV)", _T4_ME * 1e3, 511.0, rtol=1e-4)
check(_T4_PP, "pair share of Pb attenuation at 1.5 MeV (%)", 1.806e-3 / 5.222e-2 * 100, 3.5, rtol=0.02)


def _t4_cross(e1: float, d1: float, e2: float, d2: float) -> float:
    """Linear interpolation of the energy at which a difference changes sign."""
    return e1 + (e2 - e1) * (-d1) / (d2 - d1)


# XCOM, cm^2/g: (pair nuclear + pair electron) minus incoherent scattering.
check(
    _T4_PP,
    "pair = incoherent in Pb (MeV)",
    _t4_cross(4.5, 1.939e-2 + 5.768e-5 - 2.121e-2, 5.0, 2.148e-2 + 7.769e-5 - 1.978e-2),
    4.7,
    rtol=0.02,
)
check(
    _T4_PP,
    "pair = incoherent in C (MeV)",
    _t4_cross(25, 6.576e-3 + 8.372e-4 - 7.685e-3, 26, 6.693e-3 + 8.599e-4 - 7.451e-3),
    26,
    rtol=0.02,
)
check(_T4_PP, "nuclear-field pair coefficient, Pb / C at 10 MeV", 3.671e-2 / 3.854e-3, 9.5, rtol=0.01)
check("analysis/fragments/threshold-conversion.jsonl", "2 me c^2 in joules", 2 * _T4_ME * 1e6 * _T4_E, 1.637e-13, rtol=0.001)
check("analysis/fragments/threshold-conversion.jsonl", "4 me c^2 in joules", 4 * _T4_ME * 1e6 * _T4_E, 3.275e-13, rtol=0.001)
check("analysis/fragments/threshold-conversion.jsonl", "me c^2 in joules", _T4_ME * 1e6 * _T4_E, 8.187e-14, rtol=0.001)

# --- library/photoconductivity.md ---------------------------------------------
_T4_PC = "library/photoconductivity.md §4.3"
check(_T4_PC, "hc / 0.661 eV (nm)", _T4_HC_EV_NM / 0.661, 1876, rtol=0.001)
check(_T4_PC, "1876 nm against 1.8 um (%)", (_T4_HC_EV_NM / 0.661 / 1800 - 1) * 100, 4, rtol=0.1)
check(_T4_PC, "115 um in meV", _T4_HC_EV_NM / 115e3 * 1e3, 10.8, rtol=0.005)
check(_T4_PC, "10.8 meV / 0.661 eV (%)", _T4_HC_EV_NM / 115e3 / 0.661 * 100, 1.6, rtol=0.03)
check(_T4_PC, "10.8 meV / k (K)", _T4_HC_EV_NM / 115e3 / _T4_K_EV, 125, rtol=0.005)
check(_T4_PC, "10.8 meV / kT at 1.8 K", _T4_HC_EV_NM / 115e3 / (_T4_K_EV * 1.8), 70, rtol=0.01)
check(_T4_PC, "Si Eg / 2kT at 300 K", 1.12 / (2 * _T4_K_EV * 300), 21.7, rtol=0.005)
check(_T4_PC, "GaAs 5 ns to Ge 1 ms (orders of magnitude)", log(1e-3 / 5e-9) / log(10), 6, rtol=0.15)

# --- library/coulomb-blockade.md ----------------------------------------------
_T4_CB = "library/coulomb-blockade.md §4.3"
check(_T4_CB, "e^2/2C at 1 fF (ueV)", _T4_E / 2e-15 * 1e6, 80, rtol=0.005)
check(_T4_CB, "e^2/2C at 1 fF over k (K)", _T4_E**2 / 2e-15 / K_B, 0.93, rtol=0.005)
check(_T4_CB, "e^2/C at 1 fF (ueV)", _T4_E / 1e-15 * 1e6, 160, rtol=0.005)
check(_T4_CB, "e^2/C at 1 fF over k (K)", _T4_E**2 / 1e-15 / K_B, 1.86, rtol=0.005)
check(_T4_CB, "e^2/2C at 1 aF (meV)", _T4_E / 2e-18 * 1e3, 80, rtol=0.005)
check(_T4_CB, "e^2/2C at 1 aF over k (K)", _T4_E**2 / 2e-18 / K_B, 930, rtol=0.005)
check(_T4_CB, "C for e^2/C = 100 meV (aF)", _T4_E / 0.1 * 1e18, 1.6, rtol=0.01)
check(_T4_CB, "e/C at 1 fF (mV)", _T4_E / 1e-15 * 1e3, 0.16, rtol=0.01)
check(_T4_CB, "h/e^2 (ohm)", H_PLANCK / _T4_E**2, 25812.807, rtol=1e-7)
check(_T4_CB, "R C for 100 kohm, 1 fF (ns)", 1e5 * 1e-15 * 1e9, 0.1, rtol=1e-6)
check("analysis/fragments/threshold-conversion.jsonl", "e^2/2C at 1 fF in joules", _T4_E**2 / 2e-15, 1.283e-23, rtol=0.001)

# --- library/coherent-neutrino-scattering.md ----------------------------------
_T4_CN = "library/coherent-neutrino-scattering.md §4.3"
check(_T4_CN, "IBD threshold (MeV)", ((_T4_MN + _T4_ME) ** 2 - _T4_MP**2) / (2 * _T4_MP), 1.806, rtol=2e-4)


def _t4_tmax(e_mev: float, a_u: float) -> float:
    """Maximum nuclear recoil energy in MeV for elastic scattering of a massless projectile."""
    m = a_u * _T4_U
    return 2 * e_mev**2 / (m + 2 * e_mev)


check(_T4_CN, "max recoil, Ge at 1.8 MeV (eV)", _t4_tmax(1.8, 72.63) * 1e6, 96, rtol=0.01)
check(_T4_CN, "max recoil, Ge at 8 MeV (keV)", _t4_tmax(8.0, 72.63) * 1e3, 1.9, rtol=0.01)
check(_T4_CN, "max recoil, Cs at 30 MeV (keV)", _t4_tmax(30.0, 132.905) * 1e3, 14.5, rtol=0.005)
check(_T4_CN, "N^2 for 133Cs", 78**2, 6084, rtol=1e-9)
check(_T4_CN, "N^2 for 40Ar", 22**2, 484, rtol=1e-9)
check(_T4_CN, "N^2 ratio, Cs / Ar", 78**2 / 22**2, 12.6, rtol=0.005)
check(_T4_CN, "relative uncertainty, CsI count (%)", 22 / 134 * 100, 16, rtol=0.03)
check(_T4_CN, "relative uncertainty, Ar cross section (%)", 0.7 / 2.2 * 100, 32, rtol=0.02)
check(_T4_CN, "relative uncertainty, reactor count (%)", 106 / 395 * 100, 27, rtol=0.02)
check("analysis/fragments/threshold-conversion.jsonl", "1.806 MeV in joules", 1.806e6 * _T4_E, 2.894e-13, rtol=0.001)
check("analysis/fragments/threshold-conversion.jsonl", "optical period at 1.12 eV (fs)", _T4_H_EV / 1.12 * 1e15, 3.7, rtol=0.01)
