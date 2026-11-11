# Checks for the optics batch: reflection, plasma-frequency-cutoff,
# surface-plasmon-resonance, refraction-dielectric, casimir-force.
# Snippet for analysis/computed_checks.py. Uses K_B, H_PLANCK, MU_0, check and
# math's exp, log, pi, sqrt from that file.

import cmath as _cmath
from math import sin as _sin, radians as _radians

# Constants not yet in computed_checks.py. c and e are exact SI values; m_e is
# the CODATA 2022 value (the same names and values as in checks-b1-electric.py
# and checks-b1-skin.py). eps_0 and the classical electron radius are derived.
C_LIGHT = 299792458.0  # m/s
E_CHARGE = 1.602176634e-19  # C
M_ELECTRON = 9.1093837139e-31  # kg
N_AVOGADRO = 6.02214076e23  # 1/mol
EPS_0 = 1.0 / (MU_0 * C_LIGHT**2)  # F/m
R_ELECTRON = E_CHARGE**2 / (4.0 * pi * EPS_0 * M_ELECTRON * C_LIGHT**2)  # m, classical electron radius
HBAR = H_PLANCK / (2.0 * pi)


def intensity_depth_nm(lam_nm: float, k: float) -> float:
    """Intensity e-folding length lambda / (4 pi k)."""
    return lam_nm / (4.0 * pi * k)


def bulk_reflectance(n: float, k: float) -> float:
    """Normal-incidence reflectance of a thick metal in vacuum."""
    nn = complex(n, k)
    return abs((1.0 - nn) / (1.0 + nn)) ** 2


def film_rt(n: float, k: float, d_nm: float, lam_nm: float, n_sub: float = 1.0) -> tuple[float, float]:
    """R and T of one absorbing layer between vacuum and a substrate (Airy formula, normal incidence)."""
    nn = complex(n, k)
    beta = 2.0 * pi * nn * d_nm / lam_nm
    r01 = (1.0 - nn) / (1.0 + nn)
    r12 = (nn - n_sub) / (nn + n_sub)
    phase = _cmath.exp(2j * beta)
    r = (r01 + r12 * phase) / (1.0 + r01 * r12 * phase)
    t = (2.0 / (1.0 + nn)) * (2.0 * nn / (nn + n_sub)) * _cmath.exp(1j * beta) / (1.0 + r01 * r12 * phase)
    return abs(r) ** 2, n_sub * abs(t) ** 2


def film_r_pct(n: float, k: float, d_nm: float, lam_nm: float = 550.0, n_sub: float = 1.0) -> float:
    return 100.0 * film_rt(n, k, d_nm, lam_nm, n_sub)[0]


def film_t_pct(n: float, k: float, d_nm: float, lam_nm: float = 550.0, n_sub: float = 1.0) -> float:
    return 100.0 * film_rt(n, k, d_nm, lam_nm, n_sub)[1]


def thickness_for_fraction_nm(n: float, k: float, fraction: float, lam_nm: float = 550.0, n_sub: float = 1.0) -> float:
    """Thickness at which film reflectance reaches `fraction` of the bulk value (bisection)."""
    target = fraction * bulk_reflectance(n, k)
    lo, hi = 0.0, 200.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if film_rt(n, k, mid, lam_nm, n_sub)[0] < target:
            lo = mid
        else:
            hi = mid
    return lo


def plasma_energy_ev(n_m3: float) -> float:
    """Free-electron plasma energy hbar * sqrt(n e^2 / (eps0 m)) in eV."""
    return HBAR * sqrt(n_m3 * E_CHARGE**2 / (EPS_0 * M_ELECTRON)) / E_CHARGE


def plasma_frequency_mhz(n_m3: float) -> float:
    return sqrt(n_m3 * E_CHARGE**2 / (EPS_0 * M_ELECTRON)) / (2.0 * pi) / 1e6


def ev_to_nm(energy_ev: float) -> float:
    return H_PLANCK * C_LIGHT / (energy_ev * E_CHARGE) * 1e9


def ev_to_fs(energy_ev: float) -> float:
    """Period h / E in femtoseconds."""
    return H_PLANCK / (energy_ev * E_CHARGE) * 1e15


def spp_lengths(n: float, k: float, lam_nm: float, eps_d: float = 1.0) -> tuple[float, float, float]:
    """Single-interface surface plasmon: (intensity 1/e run in um, field 1/e depth in the
    dielectric in nm, field 1/e depth in the metal in nm)."""
    eps_m = complex(n, k) ** 2
    k0 = 2.0 * pi / lam_nm
    ksp = k0 * _cmath.sqrt(eps_m * eps_d / (eps_m + eps_d))
    kzd = _cmath.sqrt(eps_d * k0 * k0 - ksp * ksp)
    kzm = _cmath.sqrt(eps_m * k0 * k0 - ksp * ksp)
    return 1.0 / (2.0 * ksp.imag) / 1e3, 1.0 / abs(kzd.imag), 1.0 / abs(kzm.imag)


def three_layer_r(n1: float, n2: complex, n3: float, d_nm: float, lam_nm: float, theta_deg: float, pol: str = "p") -> float:
    """Reflectance of prism / film / outer medium at internal angle theta."""
    k0 = 2.0 * pi / lam_nm
    kx = n1 * k0 * _sin(_radians(theta_deg))

    def kz(index):
        v = _cmath.sqrt(index * index * k0 * k0 - kx * kx)
        return v if v.imag >= 0 else -v

    k1, k2, k3 = kz(n1), kz(n2), kz(n3)
    if pol == "p":
        r12 = (k1 / n1**2 - k2 / n2**2) / (k1 / n1**2 + k2 / n2**2)
        r23 = (k2 / n2**2 - k3 / n3**2) / (k2 / n2**2 + k3 / n3**2)
    else:
        r12 = (k1 - k2) / (k1 + k2)
        r23 = (k2 - k3) / (k2 + k3)
    phase = _cmath.exp(2j * k2 * d_nm)
    return abs((r12 + r23 * phase) / (1.0 + r12 * r23 * phase)) ** 2


def kretschmann_min_pct(n: float, k: float, d_nm: float, lam_nm: float, n_prism: float = 1.515) -> float:
    """Minimum p-polarised reflectance over 42-89 degrees, prism / metal / air, in percent."""
    return 100.0 * min(
        three_layer_r(n_prism, complex(n, k), 1.0, d_nm, lam_nm, a / 50.0) for a in range(2100, 4450)
    )


def sellmeier_1(coeffs: list[float], lam_um: float) -> float:
    """refractiveindex.info formula 1: n^2 - 1 = C0 + sum Ci lam^2 / (lam^2 - Cj^2)."""
    s = 1.0 + coeffs[0]
    for i in range(1, len(coeffs), 2):
        s += coeffs[i] * lam_um**2 / (lam_um**2 - coeffs[i + 1] ** 2)
    return sqrt(s)


def sellmeier_2(coeffs: list[float], lam_um: float) -> float:
    """refractiveindex.info formula 2: n^2 - 1 = C0 + sum Ci lam^2 / (lam^2 - Cj)."""
    s = 1.0 + coeffs[0]
    for i in range(1, len(coeffs), 2):
        s += coeffs[i] * lam_um**2 / (lam_um**2 - coeffs[i + 1])
    return sqrt(s)


def gas_formula_6(coeffs: list[float], lam_um: float) -> float:
    """refractiveindex.info formula 6: n - 1 = C0 + sum Ci / (Cj - lam^-2)."""
    s = 1.0 + coeffs[0]
    for i in range(1, len(coeffs), 2):
        s += coeffs[i] / (coeffs[i + 1] - lam_um**-2)
    return s


def xray_delta(rho_g_cm3: float, z: float, a_g_mol: float, energy_kev: float) -> float:
    """Free-electron index decrement n_e r_e lambda^2 / (2 pi)."""
    n_e = rho_g_cm3 * 1e6 / a_g_mol * N_AVOGADRO * z
    lam = H_PLANCK * C_LIGHT / (energy_kev * 1e3 * E_CHARGE)
    return n_e * R_ELECTRON * lam * lam / (2.0 * pi)


# Optical constants at 550 nm, interpolated from the tabulations cited in
# library/reflection.md (n, k).
AG_JC = (0.0596, 3.5974)  # Johnson and Christy 1972
AG_MCPEAK = (0.0438, 3.6101)  # McPeak et al. 2015
AG_YANG = (0.053, 3.485)  # Yang et al. 2015
AG_RAKIC_BB = (0.145, 3.190)  # Rakic et al. 1998, Brendel-Bormann fit
AG_RAKIC_LD = (0.134, 3.172)  # Rakic et al. 1998, Lorentz-Drude fit
AL_RAKIC = (1.0152, 6.6273)  # Rakic 1995
AL_RAKIC_BB = (0.965, 6.400)  # Rakic et al. 1998, Brendel-Bormann fit
AL_MCPEAK = (0.7894, 5.8519)  # McPeak et al. 2015
AL_CHENG = (0.5906, 5.2762)  # Cheng et al. 2016

# --- library/reflection.md ---------------------------------------------------
_REF = "library/reflection.md §4.3"
check(_REF, "Ag Johnson-Christy depth at 550 nm (nm)", intensity_depth_nm(550, AG_JC[1]), 12.2, 0.01)
check(_REF, "Ag McPeak depth at 550 nm (nm)", intensity_depth_nm(550, AG_MCPEAK[1]), 12.1, 0.01)
check(_REF, "Ag Yang depth at 550 nm (nm)", intensity_depth_nm(550, AG_YANG[1]), 12.6, 0.01)
check(_REF, "Ag Rakic BB fit depth at 550 nm (nm)", intensity_depth_nm(550, AG_RAKIC_BB[1]), 13.7, 0.01)
check(_REF, "Ag Rakic LD fit depth at 550 nm (nm)", intensity_depth_nm(550, AG_RAKIC_LD[1]), 13.8, 0.01)
check(_REF, "Al Rakic 1995 depth at 550 nm (nm)", intensity_depth_nm(550, AL_RAKIC[1]), 6.6, 0.01)
check(_REF, "Al Rakic BB fit depth at 550 nm (nm)", intensity_depth_nm(550, AL_RAKIC_BB[1]), 6.8, 0.01)
check(_REF, "Al McPeak depth at 550 nm (nm)", intensity_depth_nm(550, AL_MCPEAK[1]), 7.5, 0.01)
check(_REF, "Al Cheng depth at 550 nm (nm)", intensity_depth_nm(550, AL_CHENG[1]), 8.3, 0.01)
check(_REF, "Ag shortest depth, McPeak at 650 nm, k = 4.460 (nm)", intensity_depth_nm(650, 4.460), 11.6, 0.01)
check(_REF, "Ag longest depth, Rakic LD fit at 450 nm, k = 2.328 (nm)", intensity_depth_nm(450, 2.328), 15.4, 0.01)
check(_REF, "Al shortest depth, Rakic 1995 at 450 nm, k = 5.454 (nm)", intensity_depth_nm(450, 5.454), 6.6, 0.01)
check(_REF, "Al longest depth, Cheng at 450 nm, k = 4.297 (nm)", intensity_depth_nm(450, 4.297), 8.3, 0.01)
check(_REF, "Ag amplitude depth, low end (twice 11.6 nm)", 2 * 11.6, 23, 0.02)
check(_REF, "Ag amplitude depth, high end (twice 15.4 nm)", 2 * 15.4, 31, 0.02)
check(_REF, "Al amplitude depth, low end (twice 6.6 nm)", 2 * 6.6, 13, 0.02)
check(_REF, "Al amplitude depth, high end (twice 8.3 nm)", 2 * 8.3, 17, 0.03)
check(_REF, "Ag Johnson-Christy bulk R at 550 nm (%)", 100 * bulk_reflectance(*AG_JC), 98.3, 0.002)
check(_REF, "Ag McPeak bulk R at 550 nm (%)", 100 * bulk_reflectance(*AG_MCPEAK), 98.8, 0.002)
check(_REF, "Ag Yang bulk R at 550 nm (%)", 100 * bulk_reflectance(*AG_YANG), 98.4, 0.002)
check(_REF, "Ag Rakic BB fit bulk R at 550 nm (%)", 100 * bulk_reflectance(*AG_RAKIC_BB), 95.0, 0.002)
check(_REF, "Ag Rakic LD fit bulk R at 550 nm (%)", 100 * bulk_reflectance(*AG_RAKIC_LD), 95.3, 0.002)
check(_REF, "Al Rakic 1995 bulk R at 550 nm (%)", 100 * bulk_reflectance(*AL_RAKIC), 91.5, 0.002)
check(_REF, "Al Rakic BB fit bulk R at 550 nm (%)", 100 * bulk_reflectance(*AL_RAKIC_BB), 91.4, 0.002)
check(_REF, "Al McPeak bulk R at 550 nm (%)", 100 * bulk_reflectance(*AL_MCPEAK), 91.6, 0.002)
check(_REF, "Al Cheng bulk R at 550 nm (%)", 100 * bulk_reflectance(*AL_CHENG), 92.2, 0.002)
check(_REF, "Ag lowest measured-set bulk R, Yang at 450 nm, n = 0.053, k = 2.610 (%)", 100 * bulk_reflectance(0.053, 2.610), 97.3, 0.002)
check(_REF, "Ag highest measured-set bulk R, Johnson-Christy at 650 nm, n = 0.052, k = 4.409 (%)", 100 * bulk_reflectance(0.052, 4.409), 99.0, 0.002)
check(_REF, "Ag lowest fit bulk R, Rakic LD at 450 nm, n = 0.136, k = 2.328 (%)", 100 * bulk_reflectance(0.136, 2.328), 91.9, 0.002)
check(_REF, "Ag highest fit bulk R, Rakic LD at 650 nm, n = 0.146, k = 3.937 (%)", 100 * bulk_reflectance(0.146, 3.937), 96.5, 0.002)
check(_REF, "Al lowest bulk R, McPeak at 650 nm, n = 1.246, k = 6.852 (%)", 100 * bulk_reflectance(1.246, 6.852), 90.4, 0.002)
check(_REF, "Al highest bulk R, Cheng at 450 nm, n = 0.390, k = 4.297 (%)", 100 * bulk_reflectance(0.390, 4.297), 92.4, 0.002)
# Thin-film table, 550 nm, normal incidence, bulk constants.
check(_REF, "film R, Ag free-standing, 3 nm (%)", film_r_pct(*AG_JC, 3), 5.4, 0.02)
check(_REF, "film R, Ag free-standing, 5 nm (%)", film_r_pct(*AG_JC, 5), 13.6, 0.01)
check(_REF, "film R, Ag free-standing, 10 nm (%)", film_r_pct(*AG_JC, 10), 38.9, 0.005)
check(_REF, "film R, Ag free-standing, 20 nm (%)", film_r_pct(*AG_JC, 20), 73.8, 0.005)
check(_REF, "film R, Ag free-standing, 30 nm (%)", film_r_pct(*AG_JC, 30), 88.1, 0.005)
check(_REF, "film R, Ag free-standing, 50 nm (%)", film_r_pct(*AG_JC, 50), 96.4, 0.005)
check(_REF, "film R, Ag free-standing, 100 nm (%)", film_r_pct(*AG_JC, 100), 98.3, 0.005)
check(_REF, "film T, Ag free-standing, 3 nm (%)", film_t_pct(*AG_JC, 3), 93.3, 0.005)
check(_REF, "film T, Ag free-standing, 5 nm (%)", film_t_pct(*AG_JC, 5), 84.3, 0.005)
check(_REF, "film T, Ag free-standing, 10 nm (%)", film_t_pct(*AG_JC, 10), 58.0, 0.005)
check(_REF, "film T, Ag free-standing, 20 nm (%)", film_t_pct(*AG_JC, 20), 23.3, 0.01)
check(_REF, "film T, Ag free-standing, 30 nm (%)", film_t_pct(*AG_JC, 30), 9.5, 0.02)
check(_REF, "film T, Ag free-standing, 50 nm (%)", film_t_pct(*AG_JC, 50), 1.7, 0.05)
check(_REF, "film R, Ag on glass n = 1.5, 3 nm (%)", film_r_pct(*AG_JC, 3, n_sub=1.5), 7.8, 0.02)
check(_REF, "film R, Ag on glass, 5 nm (%)", film_r_pct(*AG_JC, 5, n_sub=1.5), 13.8, 0.01)
check(_REF, "film R, Ag on glass, 10 nm (%)", film_r_pct(*AG_JC, 10, n_sub=1.5), 34.2, 0.005)
check(_REF, "film R, Ag on glass, 20 nm (%)", film_r_pct(*AG_JC, 20, n_sub=1.5), 68.5, 0.005)
check(_REF, "film R, Ag on glass, 30 nm (%)", film_r_pct(*AG_JC, 30, n_sub=1.5), 85.3, 0.005)
check(_REF, "film R, Ag on glass, 50 nm (%)", film_r_pct(*AG_JC, 50, n_sub=1.5), 95.8, 0.005)
check(_REF, "film R, Ag on glass, 100 nm (%)", film_r_pct(*AG_JC, 100, n_sub=1.5), 98.3, 0.005)
check(_REF, "film R, Al Rakic 1995, 3 nm (%)", film_r_pct(*AL_RAKIC, 3), 30.0, 0.005)
check(_REF, "film R, Al Rakic 1995, 5 nm (%)", film_r_pct(*AL_RAKIC, 5), 49.9, 0.005)
check(_REF, "film R, Al Rakic 1995, 10 nm (%)", film_r_pct(*AL_RAKIC, 10), 74.2, 0.005)
check(_REF, "film R, Al Rakic 1995, 20 nm (%)", film_r_pct(*AL_RAKIC, 20), 87.5, 0.005)
check(_REF, "film R, Al Rakic 1995, 30 nm (%)", film_r_pct(*AL_RAKIC, 30), 90.5, 0.005)
check(_REF, "film R, Al Rakic 1995, 50 nm (%)", film_r_pct(*AL_RAKIC, 50), 91.5, 0.005)
check(_REF, "film R, Al Rakic 1995, 100 nm (%)", film_r_pct(*AL_RAKIC, 100), 91.5, 0.005)
check(_REF, "film R, Al McPeak, 3 nm (%)", film_r_pct(*AL_MCPEAK, 3), 22.4, 0.005)
check(_REF, "film R, Al McPeak, 5 nm (%)", film_r_pct(*AL_MCPEAK, 5), 41.2, 0.005)
check(_REF, "film R, Al McPeak, 10 nm (%)", film_r_pct(*AL_MCPEAK, 10), 68.4, 0.005)
check(_REF, "film R, Al McPeak, 20 nm (%)", film_r_pct(*AL_MCPEAK, 20), 85.4, 0.005)
check(_REF, "film R, Al McPeak, 30 nm (%)", film_r_pct(*AL_MCPEAK, 30), 89.8, 0.005)
check(_REF, "film R, Al McPeak, 50 nm (%)", film_r_pct(*AL_MCPEAK, 50), 91.4, 0.005)
check(_REF, "film R, Al McPeak, 100 nm (%)", film_r_pct(*AL_MCPEAK, 100), 91.6, 0.005)
check(_REF, "film R, Al Cheng, 5 nm (%)", film_r_pct(*AL_CHENG, 5), 34, 0.02)
check(_REF, "film R, Al Cheng, 10 nm (%)", film_r_pct(*AL_CHENG, 10), 63, 0.02)
check(_REF, "half of bulk R, Ag free-standing (nm)", thickness_for_fraction_nm(*AG_JC, 0.5), 12.2, 0.01)
check(_REF, "half of bulk R, Ag on glass (nm)", thickness_for_fraction_nm(*AG_JC, 0.5, n_sub=1.5), 13.7, 0.01)
check(_REF, "half of bulk R, Al Rakic 1995 free-standing (nm)", thickness_for_fraction_nm(*AL_RAKIC, 0.5), 4.5, 0.02)
check(_REF, "half of bulk R, Al McPeak free-standing (nm)", thickness_for_fraction_nm(*AL_MCPEAK, 0.5), 5.6, 0.02)
check(_REF, "half of bulk R, Al McPeak on glass (nm)", thickness_for_fraction_nm(*AL_MCPEAK, 0.5, n_sub=1.5), 5.9, 0.02)
check(_REF, "90 % of bulk R, Ag free-standing (nm)", thickness_for_fraction_nm(*AG_JC, 0.9), 31, 0.03)
check(_REF, "90 % of bulk R, Ag on glass (nm)", thickness_for_fraction_nm(*AG_JC, 0.9, n_sub=1.5), 33, 0.03)
check(_REF, "90 % of bulk R, Al Rakic 1995 free-standing (nm)", thickness_for_fraction_nm(*AL_RAKIC, 0.9), 14, 0.03)
check(_REF, "90 % of bulk R, Al McPeak free-standing (nm)", thickness_for_fraction_nm(*AL_MCPEAK, 0.9), 17, 0.03)
# Plasma energies and periods.
check(_REF, "free-electron plasma energy, Al, n = 1.81e29 m^-3 (eV)", plasma_energy_ev(1.81e29), 15.8, 0.005)
check(_REF, "free-electron plasma energy, Ag, n = 5.86e28 m^-3 (eV)", plasma_energy_ev(5.86e28), 8.99, 0.005)
check(_REF, "measured Al plasmon over free-electron value (15.0 / 15.8)", 15.0 / 15.8, 0.95, 0.01)
check(_REF, "measured Ag plasmon over free-electron value (3.78 / 8.99)", 3.78 / 8.99, 0.42, 0.01)
check(_REF, "plasma period at 15.0 eV (fs)", ev_to_fs(15.0), 0.28, 0.02)
check(_REF, "plasma period at 9.0 eV (fs)", ev_to_fs(9.0), 0.46, 0.01)
check(_REF, "plasma period at 3.8 eV (fs)", ev_to_fs(3.8), 1.1, 0.02)
check(_REF, "plasma period at 15.0 eV (as)", ev_to_fs(15.0) * 1e3, 276, 0.005)
check(_REF, "plasma period at 9.0 eV (as)", ev_to_fs(9.0) * 1e3, 460, 0.005)
check(_REF, "optical period at 550 nm (fs)", 550e-9 / C_LIGHT * 1e15, 1.8, 0.03)
# Silver edge from the Johnson-Christy tabulation.
check(_REF, "Ag bulk R at 381.5 nm, n = 0.05, k = 1.864 (%)", 100 * bulk_reflectance(0.05, 1.864), 95.6, 0.002)
check(_REF, "Ag bulk R at 320.4 nm, n = 0.81, k = 0.392 (%)", 100 * bulk_reflectance(0.81, 0.392), 5.5, 0.01)
check(_REF, "Ag bulk R at 300.9 nm, n = 1.34, k = 0.964 (%)", 100 * bulk_reflectance(1.34, 0.964), 16, 0.03)
check(_REF, "photon energy at 320.4 nm (eV)", H_PLANCK * C_LIGHT / (320.4e-9 * E_CHARGE), 3.87, 0.002)
# Lattice planes and carrier densities.
check(_REF, "Ag (111) spacing a / sqrt(3), a = 4.0862 A (A)", 4.0862 / sqrt(3), 2.359, 0.0005)
check(_REF, "Al (111) spacing a / sqrt(3), a = 4.04958 A (A)", 4.04958 / sqrt(3), 2.338, 0.0005)
check(_REF, "Ag planes in 11.6 nm", 116 / 2.359, 49, 0.01)
check(_REF, "Ag planes in 15.4 nm", 154 / 2.359, 65, 0.01)
check(_REF, "Al planes in 6.6 nm", 66 / 2.338, 28, 0.01)
check(_REF, "Al planes in 8.3 nm", 83 / 2.338, 36, 0.02)
check(_REF, "Ag planes in 10 nm (first version's lower figure)", 100 / 2.359, 42, 0.01)
check(_REF, "Ag planes in 20 nm (first version's upper figure)", 200 / 2.359, 85, 0.01)
check(_REF, "thickness of 7 Ag(111) monolayers (nm)", 7 * 0.2359, 1.65, 0.005)
check(_REF, "thickness of 10 Ag(111) monolayers (nm)", 10 * 0.2359, 2.4, 0.02)
check(_REF, "Al carrier density, 3 electrons x 4 atoms / a^3 (m^-3)", 12 / (4.04958e-10) ** 3, 1.81e29, 0.005)
check(_REF, "Ag carrier density, 1 electron x 4 atoms / a^3 (m^-3)", 4 / (4.0862e-10) ** 3, 5.86e28, 0.005)
check(_REF, "film T, Ag free-standing, 100 nm (%)", film_t_pct(*AG_JC, 100), 0.03, 0.1)
check(_REF, "width of the Ag edge, 381.5 nm to 320.4 nm (nm)", 381.5 - 320.4, 61, 0.01)
check(_REF, "film R, Ag free-standing, 3 nm, as quoted in §4.6 (%)", film_r_pct(*AG_JC, 3), 5, 0.1)

# --- library/plasma-frequency-cutoff.md --------------------------------------
_PFC = "library/plasma-frequency-cutoff.md §4.3"
check(_PFC, "free-electron plasma energy, Al, n = 18.1e28 m^-3 (eV)", plasma_energy_ev(18.1e28), 15.8, 0.005)
check(_PFC, "free-electron plasma energy, Na, n = 2.65e28 m^-3 (eV)", plasma_energy_ev(2.65e28), 6.04, 0.005)
check(_PFC, "free-electron plasma energy, K, n = 1.40e28 m^-3 (eV)", plasma_energy_ev(1.40e28), 4.39, 0.005)
check(_PFC, "free-electron plasma energy, Rb, n = 1.15e28 m^-3 (eV)", plasma_energy_ev(1.15e28), 3.98, 0.005)
check(_PFC, "free-electron plasma energy, Cs, n = 0.91e28 m^-3 (eV)", plasma_energy_ev(0.91e28), 3.54, 0.005)
check(_PFC, "free-electron plasma energy, Ag, n = 5.86e28 m^-3 (eV)", plasma_energy_ev(5.86e28), 8.99, 0.005)
check(_PFC, "hc/E at 15.8 eV (nm)", ev_to_nm(15.8), 78.5, 0.005)
check(_PFC, "hc/E at 6.04 eV (nm)", ev_to_nm(6.04), 205, 0.005)
check(_PFC, "hc/E at 4.39 eV (nm)", ev_to_nm(4.39), 282, 0.005)
check(_PFC, "hc/E at 3.98 eV (nm)", ev_to_nm(3.98), 311, 0.005)
check(_PFC, "hc/E at 3.54 eV (nm)", ev_to_nm(3.54), 350, 0.005)
check(_PFC, "hc/E at 8.99 eV (nm)", ev_to_nm(8.99), 138, 0.005)
check(_PFC, "hc/E at 15.0 eV, measured Al (nm)", ev_to_nm(15.0), 82.7, 0.002)
check(_PFC, "hc/E at 15.3 eV, measured Al (nm)", ev_to_nm(15.3), 81.0, 0.002)
check(_PFC, "hc/E at 5.75 eV, measured Na (nm)", ev_to_nm(5.75), 216, 0.005)
check(_PFC, "hc/E at 3.80 eV, measured K (nm)", ev_to_nm(3.80), 326, 0.005)
check(_PFC, "hc/E at 3.40 eV, measured Rb (nm)", ev_to_nm(3.40), 365, 0.005)
check(_PFC, "hc/E at 2.90 eV, measured Cs (nm)", ev_to_nm(2.90), 428, 0.005)
check(_PFC, "hc/E at 3.78 eV, measured Ag (nm)", ev_to_nm(3.78), 328, 0.005)
check(_PFC, "measured over model, Al low (15.0 / 15.8)", 15.0 / 15.8, 0.95, 0.01)
check(_PFC, "measured over model, Al high (15.3 / 15.8)", 15.3 / 15.8, 0.97, 0.01)
check(_PFC, "measured over model, Na (5.75 / 6.04)", 5.75 / 6.04, 0.95, 0.01)
check(_PFC, "measured over model, K (3.80 / 4.39)", 3.80 / 4.39, 0.87, 0.01)
check(_PFC, "measured over model, Rb (3.40 / 3.98)", 3.40 / 3.98, 0.85, 0.01)
check(_PFC, "measured over model, Cs (2.90 / 3.54)", 2.90 / 3.54, 0.82, 0.01)
check(_PFC, "measured over model, Ag (3.78 / 8.99)", 3.78 / 8.99, 0.42, 0.01)
check(_PFC, "shortfall of K below the free-electron value (%)", 100 * (1 - 3.80 / 4.39), 13, 0.05)
check(_PFC, "shortfall of Cs below the free-electron value (%)", 100 * (1 - 2.90 / 3.54), 18, 0.05)
check(_PFC, "shortfall of Al (15.3 eV) below the free-electron value (%)", 100 * (1 - 15.3 / 15.8), 3, 0.1)
check(_PFC, "shortfall of Na below the free-electron value (%)", 100 * (1 - 5.75 / 6.04), 5, 0.05)
check(_PFC, "Ag free-electron over measured plasmon (8.99 / 3.78)", 8.99 / 3.78, 2.4, 0.02)
check(_PFC, "largest gap between transparency onset and plasmon wavelength, Cs (440 - 428 nm)", 440 - 428, 12, 0.01)
check(_PFC, "gap between transparency onset and plasmon wavelength, K (326 - 315 nm)", 326 - 315, 11, 0.01)
check(_PFC, "gap between transparency onset and plasmon wavelength, Na (216 - 210 nm)", 216 - 210, 6, 0.01)
check(_PFC, "gap between transparency onset and plasmon wavelength, Rb (365 - 360 nm)", 365 - 360, 5, 0.01)
check(_PFC, "Ag bulk R at 381.5 nm, n = 0.05, k = 1.864 (%)", 100 * bulk_reflectance(0.05, 1.864), 95.6, 0.002)
check(_PFC, "Ag bulk R at 320.4 nm, n = 0.81, k = 0.392 (%)", 100 * bulk_reflectance(0.81, 0.392), 5.5, 0.01)
check(_PFC, "Ag bulk R at 300.9 nm, n = 1.34, k = 0.964 (%)", 100 * bulk_reflectance(1.34, 0.964), 16, 0.03)
check(_PFC, "photon energy at 320.4 nm (eV)", H_PLANCK * C_LIGHT / (320.4e-9 * E_CHARGE), 3.87, 0.002)
check(_PFC, "Ag decay length at 550 nm, k = 3.597 (nm)", intensity_depth_nm(550, 3.597), 12, 0.02)
check(_PFC, "Ag decay length at 320.4 nm, k = 0.392 (nm)", intensity_depth_nm(320.4, 0.392), 65, 0.01)
check(_PFC, "Ag decay length at 300.9 nm, k = 0.964 (nm)", intensity_depth_nm(300.9, 0.964), 25, 0.01)
check(_PFC, "wavelength span from the Ag window to renewed absorption (320.4 - 300.9 nm)", 320.4 - 300.9, 20, 0.03)
check(_PFC, "plasma period at 15.0 eV, Al (fs)", ev_to_fs(15.0), 0.28, 0.02)
check(_PFC, "plasma period at 5.75 eV, Na (fs)", ev_to_fs(5.75), 0.72, 0.01)
check(_PFC, "plasma period at 3.80 eV, K (fs)", ev_to_fs(3.80), 1.1, 0.02)
check(_PFC, "plasma period at 9.0 eV, Ag free-electron (fs)", ev_to_fs(9.0), 0.46, 0.01)
check(_PFC, "plasma period at 3.8 eV, Ag measured (fs)", ev_to_fs(3.8), 1.1, 0.02)
check(_PFC, "plasma frequency at 1e10 m^-3 (MHz)", plasma_frequency_mhz(1e10), 0.90, 0.01)
check(_PFC, "plasma frequency at 1e11 m^-3 (MHz)", plasma_frequency_mhz(1e11), 2.84, 0.005)
check(_PFC, "plasma frequency at 1e12 m^-3 (MHz)", plasma_frequency_mhz(1e12), 8.98, 0.005)
check(_PFC, "plasma period at 1e10 m^-3 (us)", 1 / plasma_frequency_mhz(1e10), 1.1, 0.02)
check(_PFC, "plasma period at 1e11 m^-3 (us)", 1 / plasma_frequency_mhz(1e11), 0.35, 0.01)
check(_PFC, "plasma period at 1e12 m^-3 (us)", 1 / plasma_frequency_mhz(1e12), 0.11, 0.02)
check(_PFC, "density ratio, Ag over 1e12 m^-3", 5.86e28 / 1e12, 5.9e16, 0.01)
check(_PFC, "density ratio, Al over 1e11 m^-3", 1.81e29 / 1e11, 1.8e18, 0.01)

# --- library/surface-plasmon-resonance.md ------------------------------------
_SPR = "library/surface-plasmon-resonance.md §4.3"
EPS_WATER = 1.7778  # n^2 of water at 589.3 nm, 20.0 C (Daimon and Masumura)
AU_JC_633 = (0.183, 3.433)  # Johnson and Christy, interpolated
AG_JC_633 = (0.056, 4.278)
AU_MCPEAK_633 = (0.143, 3.610)  # McPeak et al., interpolated
AG_MCPEAK_633 = (0.0513, 4.318)
AU_JC_550 = (0.424, 2.472)
AU_JC_450 = (1.383, 1.916)
AG_JC_450 = (0.040, 2.648)
check(_SPR, "Kretschmann minimum R, Au 40 nm at 633 nm (%)", kretschmann_min_pct(*AU_JC_633, 40, 633), 6, 0.1)
check(_SPR, "Kretschmann minimum R, Au 45 nm at 633 nm (%)", kretschmann_min_pct(*AU_JC_633, 45, 633), 0.9, 0.1)
check(_SPR, "Kretschmann minimum R, Au 50 nm at 633 nm (%)", kretschmann_min_pct(*AU_JC_633, 50, 633), 0.6, 0.1)
check(_SPR, "Kretschmann minimum R, Au 60 nm at 633 nm (%)", kretschmann_min_pct(*AU_JC_633, 60, 633), 15, 0.05)
check(_SPR, "Kretschmann minimum R, Ag 45 nm at 633 nm (%)", kretschmann_min_pct(*AG_JC_633, 45, 633), 13, 0.05)
check(_SPR, "Kretschmann minimum R, Ag 50 nm at 633 nm (%)", kretschmann_min_pct(*AG_JC_633, 50, 633), 2.9, 0.05)
check(_SPR, "Kretschmann minimum R, Ag 55 nm at 633 nm (%)", kretschmann_min_pct(*AG_JC_633, 55, 633), 1.0, 0.1)
check(_SPR, "Kretschmann minimum R, Ag 60 nm at 633 nm (%)", kretschmann_min_pct(*AG_JC_633, 60, 633), 7, 0.1)
check(_SPR, "Kretschmann minimum R, Au 30 nm at 550 nm (%)", kretschmann_min_pct(*AU_JC_550, 30, 550), 8, 0.05)
check(_SPR, "Kretschmann minimum R, Au 40 nm at 550 nm (%)", kretschmann_min_pct(*AU_JC_550, 40, 550), 0.03, 0.3)
check(_SPR, "Kretschmann minimum R, Au 50 nm at 550 nm (%)", kretschmann_min_pct(*AU_JC_550, 50, 550), 8, 0.06)
check(_SPR, "run length, Ag-air 633 nm, Johnson-Christy (um)", spp_lengths(*AG_JC_633, 633)[0], 65, 0.02)
check(_SPR, "dielectric depth, Ag-air 633 nm, Johnson-Christy (nm)", spp_lengths(*AG_JC_633, 633)[1], 419, 0.005)
check(_SPR, "metal depth, Ag-air 633 nm, Johnson-Christy (nm)", spp_lengths(*AG_JC_633, 633)[2], 23, 0.02)
check(_SPR, "run length, Ag-air 633 nm, McPeak (um)", spp_lengths(*AG_MCPEAK_633, 633)[0], 73, 0.02)
check(_SPR, "dielectric depth, Ag-air 633 nm, McPeak (nm)", spp_lengths(*AG_MCPEAK_633, 633)[1], 423, 0.005)
check(_SPR, "metal depth, Ag-air 633 nm, McPeak (nm)", spp_lengths(*AG_MCPEAK_633, 633)[2], 23, 0.02)
check(_SPR, "run length, Ag-water 633 nm (um)", spp_lengths(*AG_JC_633, 633, EPS_WATER)[0], 25, 0.03)
check(_SPR, "dielectric depth, Ag-water 633 nm (nm)", spp_lengths(*AG_JC_633, 633, EPS_WATER)[1], 230, 0.005)
check(_SPR, "metal depth, Ag-water 633 nm (nm)", spp_lengths(*AG_JC_633, 633, EPS_WATER)[2], 22, 0.03)
check(_SPR, "run length, Ag-air 450 nm (um)", spp_lengths(*AG_JC_450, 450)[0], 13, 0.03)
check(_SPR, "dielectric depth, Ag-air 450 nm (nm)", spp_lengths(*AG_JC_450, 450)[1], 176, 0.005)
check(_SPR, "metal depth, Ag-air 450 nm (nm)", spp_lengths(*AG_JC_450, 450)[2], 25, 0.02)
check(_SPR, "run length, Au-air 633 nm, Johnson-Christy (um)", spp_lengths(*AU_JC_633, 633)[0], 9.8, 0.01)
check(_SPR, "dielectric depth, Au-air 633 nm, Johnson-Christy (nm)", spp_lengths(*AU_JC_633, 633)[1], 332, 0.005)
check(_SPR, "metal depth, Au-air 633 nm, Johnson-Christy (nm)", spp_lengths(*AU_JC_633, 633)[2], 28, 0.02)
check(_SPR, "run length, Au-air 633 nm, McPeak (um)", spp_lengths(*AU_MCPEAK_633, 633)[0], 15, 0.03)
check(_SPR, "dielectric depth, Au-air 633 nm, McPeak (nm)", spp_lengths(*AU_MCPEAK_633, 633)[1], 350, 0.005)
check(_SPR, "metal depth, Au-air 633 nm, McPeak (nm)", spp_lengths(*AU_MCPEAK_633, 633)[2], 27, 0.02)
check(_SPR, "run length, Au-water 633 nm (um)", spp_lengths(*AU_JC_633, 633, EPS_WATER)[0], 3.7, 0.02)
check(_SPR, "dielectric depth, Au-water 633 nm (nm)", spp_lengths(*AU_JC_633, 633, EPS_WATER)[1], 180, 0.005)
check(_SPR, "metal depth, Au-water 633 nm (nm)", spp_lengths(*AU_JC_633, 633, EPS_WATER)[2], 27, 0.02)
check(_SPR, "run length, Au-air 550 nm (um)", spp_lengths(*AU_JC_550, 550)[0], 1.3, 0.02)
check(_SPR, "dielectric depth, Au-air 550 nm (nm)", spp_lengths(*AU_JC_550, 550)[1], 207, 0.005)
check(_SPR, "metal depth, Au-air 550 nm (nm)", spp_lengths(*AU_JC_550, 550)[2], 33, 0.02)
check(_SPR, "run length, Au-air 450 nm (um)", spp_lengths(*AU_JC_450, 450)[0], 0.4, 0.05)
check(_SPR, "dielectric depth, Au-air 450 nm (nm)", spp_lengths(*AU_JC_450, 450)[1], 219, 0.005)
check(_SPR, "metal depth, Au-air 450 nm (nm)", spp_lengths(*AU_JC_450, 450)[2], 35, 0.02)
check(_SPR, "dielectric depth over wavelength, Ag-air 633 nm", 419 / 633, 0.66, 0.01)
check(_SPR, "dielectric depth over wavelength, Ag-air 633 nm, McPeak", 423 / 633, 0.67, 0.01)
check(_SPR, "dielectric depth over wavelength, Ag-water 633 nm", 230 / 633, 0.36, 0.02)
check(_SPR, "dielectric depth over wavelength, Ag-air 450 nm", 176 / 450, 0.39, 0.01)
check(_SPR, "dielectric depth over wavelength, Au-air 633 nm", 332 / 633, 0.52, 0.01)
check(_SPR, "dielectric depth over wavelength, Au-air 633 nm, McPeak", 350 / 633, 0.55, 0.01)
check(_SPR, "dielectric depth over wavelength, Au-water 633 nm", 180 / 633, 0.28, 0.02)
check(_SPR, "dielectric depth over wavelength, Au-air 550 nm", 207 / 550, 0.38, 0.01)
check(_SPR, "dielectric depth over wavelength, Au-air 450 nm", 219 / 450, 0.49, 0.01)
check(_SPR, "Ag over Au run length at 633 nm, Johnson-Christy (65 / 9.8)", 65 / 9.8, 7, 0.06)
check(_SPR, "Ag over Au run length at 633 nm, McPeak (73 / 15)", 73 / 15, 5, 0.03)
check(_SPR, "Re eps of Ag at 300 nm from n = 1.345, k = 0.985", 1.345**2 - 0.985**2, 0.84, 0.005)
check(_SPR, "Im eps of Ag at 300 nm from n = 1.345, k = 0.985", 2 * 1.345 * 0.985, 2.65, 0.005)
check(_SPR, "p-polarised R, 30 nm Ag on a 1.488 prism, 300 nm, 55 degrees (%)", 100 * three_layer_r(1.488, complex(1.345, 0.985), 1.0, 30, 300, 55, "p"), 0.4, 0.15)
check(_SPR, "s-polarised R, same film and angle (%)", 100 * three_layer_r(1.488, complex(1.345, 0.985), 1.0, 30, 300, 55, "s"), 22, 0.03)

# --- library/refraction-dielectric.md ----------------------------------------
_RFR = "library/refraction-dielectric.md §4.3"
_D_LINE = 0.5893  # um
_WATER_20C = [0, 5.684027565e-1, 5.101829712e-3, 1.726177391e-1, 1.821153936e-2, 2.086189578e-2, 2.620722293e-2, 1.130748688e-1, 1.069792721e1]
check(_RFR, "water at 20.0 C, 589.3 nm (Daimon and Masumura)", sellmeier_2(_WATER_20C, _D_LINE), 1.33335, 0.00002)
check(_RFR, "fused silica, 589.3 nm (Malitson)", sellmeier_1([0, 0.6961663, 0.0684043, 0.4079426, 0.1162414, 0.8974794, 9.896161], _D_LINE), 1.45840, 0.00002)
check(_RFR, "N-BK7, 589.3 nm (SCHOTT)", sellmeier_2([0, 1.03961212, 0.00600069867, 0.231792344, 0.0200179144, 1.01046945, 103.560653], _D_LINE), 1.51673, 0.00002)
check(_RFR, "diamond, 589.3 nm (Peter)", sellmeier_1([0, 0.3306, 0.1750, 4.3356, 0.1060], _D_LINE), 2.4173, 0.00005)
check(_RFR, "standard air, 589.3 nm (Ciddor)", gas_formula_6([0, 0.05792105, 238.0185, 0.00167917, 57.362], _D_LINE), 1.000277, 0.000001)
check(_RFR, "optical permittivity of water, 1.33335 squared", 1.33335**2, 1.7778, 0.0001)
check(_RFR, "static over optical permittivity of water (80.10 / 1.7778)", 80.10 / 1.7778, 45, 0.01)
check(_RFR, "X-ray delta, Si at 3 keV", xray_delta(2.33, 14, 28.0855, 3), 5.4e-5, 0.02)
check(_RFR, "X-ray delta, Si at 8.05 keV", xray_delta(2.33, 14, 28.0855, 8.05), 7.4e-6, 0.02)
check(_RFR, "X-ray delta, Si at 20 keV", xray_delta(2.33, 14, 28.0855, 20), 1.2e-6, 0.02)
check(_RFR, "X-ray delta, Si at 1 keV", xray_delta(2.33, 14, 28.0855, 1), 4.8e-4, 0.02)
check(_RFR, "X-ray delta, water at 3 keV", xray_delta(1.0, 10, 18.015, 3), 2.6e-5, 0.02)
check(_RFR, "X-ray delta, water at 8.05 keV", xray_delta(1.0, 10, 18.015, 8.05), 3.6e-6, 0.02)
check(_RFR, "X-ray delta, water at 20 keV", xray_delta(1.0, 10, 18.015, 20), 5.8e-7, 0.02)
check(_RFR, "X-ray delta, Au at 8.05 keV", xray_delta(19.3, 79, 196.97, 8.05), 5.0e-5, 0.02)
check(_RFR, "optical period at 450 nm (fs)", 450e-9 / C_LIGHT * 1e15, 1.50, 0.005)
check(_RFR, "optical period at 550 nm (fs)", 550e-9 / C_LIGHT * 1e15, 1.83, 0.005)
check(_RFR, "optical period at 650 nm (fs)", 650e-9 / C_LIGHT * 1e15, 2.17, 0.005)

# --- library/casimir-force.md ------------------------------------------------
_CAS = "library/casimir-force.md §4.3"
check(_CAS, "K_C = pi h c / 480 (N m^2)", pi * H_PLANCK * C_LIGHT / 480, 1.300e-27, 0.001)
check(_CAS, "ideal plate pressure at 1 um (mPa)", pi**2 * HBAR * C_LIGHT / (240 * (1e-6) ** 4) * 1e3, 1.30, 0.002)
check(_CAS, "ideal plate pressure at 0.1 um (Pa)", pi**2 * HBAR * C_LIGHT / (240 * (0.1e-6) ** 4), 13.0, 0.002)
check(_CAS, "measured over ideal coefficient (1.22 / 1.30)", 1.22 / 1.30, 0.94, 0.005)
check(_CAS, "hbar c / 2d at d = 100 nm (eV)", HBAR * C_LIGHT / (2 * 100e-9) / E_CHARGE, 0.99, 0.01)
check(_CAS, "hbar c / 2d at d = 1 um (eV)", HBAR * C_LIGHT / (2 * 1e-6) / E_CHARGE, 0.10, 0.02)
check(_CAS, "hbar c / d at d = 100 nm (eV)", HBAR * C_LIGHT / 100e-9 / E_CHARGE, 1.97, 0.005)
check(_CAS, "hbar c / d at d = 1 um (eV)", HBAR * C_LIGHT / 1e-6 / E_CHARGE, 0.20, 0.02)
check(_CAS, "thermal length hbar c / kT at 300 K (um)", HBAR * C_LIGHT / (K_B * 300) * 1e6, 7.6, 0.01)
