# Checks for the nuclear-gate batch (3-A): muon-catalyzed-fusion,
# pyroelectric-fusion, deuteron-photodisintegration.
# Executed inside analysis/computed_checks.py; uses check and math's pi from it.
# Names defined here carry a _G3 prefix so they cannot collide with constants
# defined by the other files in this directory.

_G3_E = 1.602176634e-19  # C, exact
_G3_EPS0 = 8.8541878188e-12  # F/m, CODATA 2022
_G3_HC_EV_M = 1.23984198e-6  # eV m (h and c exact)

# --- library/muon-catalyzed-fusion.md -----------------------------------------
_G3_TAU_MU = 2.1969811e-6  # s, PDG 2026 [S1]
_G3_M_MU = 105.6583755  # MeV, PDG 2026 [S1]
_G3_MU_E = 206.7682827  # CODATA 2022 [S2]
_G3_A0 = 5.29177210544e-11  # m, CODATA 2022 [S3]
_G3_Q_DT = 17.6  # MeV [S9]
_G3_LAM_C = 1e8  # 1/s [S7]

_G3_MU = "library/muon-catalyzed-fusion.md §4.3"
check(_G3_MU, "a0 / (m_mu/m_e) (fm)", _G3_A0 / _G3_MU_E * 1e15, 256)
check(_G3_MU, "muon decay rate (1/s)", 1.0 / _G3_TAU_MU, 4.55e5)
check(_G3_MU, "fusion rate 1e12/s times tau_mu", 1e12 * _G3_TAU_MU, 2.2e6)
check(_G3_MU, "lambda_c tau_mu", _G3_LAM_C * _G3_TAU_MU, 220)
check(_G3_MU, "two limits of 300 combined", 1.0 / (1.0 / 300 + 1.0 / 300), 150)
check(
    _G3_MU,
    "yield at lambda_c = 1e8/s, sticking 0.45 %",
    1.0 / (0.0045 + 1.0 / (_G3_LAM_C * _G3_TAU_MU)),
    110,
)
check(_G3_MU, "energy per muon at 150 fusions (GeV)", 150 * _G3_Q_DT / 1e3, 2.64)
check(_G3_MU, "that energy in muon rest energies", 150 * _G3_Q_DT / _G3_M_MU, 25)
check(_G3_MU, "fusions to return 5 GeV", 5000 / _G3_Q_DT, 284)
check(_G3_MU, "fusions to return 8 GeV", 8000 / _G3_Q_DT, 455)
check(_G3_MU, "8 GeV at 40 % heat-to-electric", 8000 / _G3_Q_DT / 0.4, 1140)
check(_G3_MU, "shortfall factor, low", 5000 / _G3_Q_DT / 150, 1.9)
check(_G3_MU, "shortfall factor, high", 8000 / _G3_Q_DT / 0.4 / 150, 7.6)
check(
    "library/muon-catalyzed-fusion.md §4.6",
    "min(1/omega_s, lambda_c tau) at the same inputs",
    min(1 / 0.0045, _G3_LAM_C * _G3_TAU_MU),
    220,
)

# --- library/pyroelectric-fusion.md -------------------------------------------
_G3_GAMMA = 190e-6  # C m^-2 K^-1 [S2]
_G3_EPS_R = 46.0  # [S2]
_G3_D_CR = 0.010  # m [S2]


def _g3_pyro_v(d_t: float) -> float:
    """Ideal potential gamma dT d / (eps_r eps0), no charge loss [S2]."""
    return _G3_GAMMA * d_t * _G3_D_CR / (_G3_EPS_R * _G3_EPS0)


_G3_PY = "library/pyroelectric-fusion.md §4.3"
check(_G3_PY, "source neutrons, Geuther: 4 pi 138 / (0.4 x 0.41)", 4 * pi * 138 / (0.4 * 0.41), 10570)
check(_G3_PY, "source neutrons, Naranjo: 15300 / 0.18", 15300 / 0.18, 85000)
check(_G3_PY, "neutron energy, 3/4 of 3.27 MeV", 3.27 * 3 / 4, 2.45)
check(_G3_PY, "ideal potential, 25 K, 10 mm (kV)", _g3_pyro_v(25) / 1e3, 117)
check(_G3_PY, "ideal potential, 40 K, 10 mm (kV)", _g3_pyro_v(40) / 1e3, 187)
check(_G3_PY, "charge loss: 1 - 110 kV / ideal at 40 K", 1 - 110e3 / _g3_pyro_v(40), 0.40, rtol=0.06)
check(_G3_PY, "ions per second at 4 nA", 4e-9 / _G3_E, 2.5e10)
check(_G3_PY, "neutrons per ion", 1000 / (4e-9 / _G3_E), 4e-8)
check(_G3_PY, "beam power, 100 kV x 4 nA (W)", 1e5 * 4e-9, 4e-4)
check(_G3_PY, "neutron-branch power, 1000/s x 3.27 MeV (W)", 1000 * 3.27e6 * _G3_E, 5e-10, rtol=0.06)
check(_G3_PY, "neutron-branch power / beam power", 1000 * 3.27e6 * _G3_E / (1e5 * 4e-9), 1e-6, rtol=0.35)
check(_G3_PY, "130 degC in kelvin", 130 + 273.15, 403)
check(_G3_PY, "403 K / 874 K", (130 + 273.15) / 874, 0.46)

# --- library/deuteron-photodisintegration.md ----------------------------------
_G3_BD = 2.22456614  # MeV [S1]
_G3_MD = 1875.612945  # MeV [S2]
_G3_LAMBDA = 5.57671299e-13  # m [S1]
_G3_EGAM = _G3_HC_EV_M / _G3_LAMBDA / 1e6  # MeV

_G3_DP = "library/deuteron-photodisintegration.md §4.3"
check(_G3_DP, "capture photon energy from wavelength (MeV)", _G3_EGAM, 2.223248, rtol=1e-6)
check(_G3_DP, "deuteron recoil after capture (keV)", _G3_EGAM**2 / (2 * _G3_MD) * 1e3, 1.318, rtol=1e-3)
check(_G3_DP, "B_d minus capture photon (keV)", (_G3_BD - _G3_EGAM) * 1e3, 1.318, rtol=1e-3)
check(_G3_DP, "photodisintegration threshold (MeV)", _G3_BD * (1 + _G3_BD / (2 * _G3_MD)), 2.225885, rtol=1e-6)
check(_G3_DP, "threshold minus B_d (keV)", _G3_BD**2 / (2 * _G3_MD) * 1e3, 1.32, rtol=1e-2)
