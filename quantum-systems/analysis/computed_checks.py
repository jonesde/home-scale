#!/usr/bin/env python3
"""Arithmetic behind every "Computed here" number in a sourced effect file.

The first-wave library carried a factor-of-ten slip for months because nobody
recomputed a cube root. This file is the guard against that class of error.

Each entry recomputes one number from its cited inputs and compares the result
with the figure the library quotes. `rebuild.py` runs these first and fails if
any quoted figure has drifted from its recomputation. When a "Computed here"
number changes in an effect file, change it here in the same edit.

Run alone to print the table:

    python3 analysis/computed_checks.py
"""

from __future__ import annotations

from math import exp, log, pi, sqrt
from pathlib import Path

# CODATA 2022 exact SI values.
K_B = 1.380649e-23  # J/K
H_PLANCK = 6.62607015e-34  # J s
MU_0 = 1.25663706127e-6  # N/A^2 (CODATA 2022 recommended value)


def stable_volume(k_j_m3: float, t_k: float, multiple: float) -> float:
    """Volume at which K V = multiple * k_B T."""
    return multiple * K_B * t_k / k_j_m3


def cube_edge_nm(volume_m3: float) -> float:
    return volume_m3 ** (1.0 / 3.0) * 1e9


def sphere_diameter_nm(volume_m3: float) -> float:
    return (6.0 * volume_m3 / pi) ** (1.0 / 3.0) * 1e9


def bloch_wall_width_nm(a_j_m: float, k_j_m3: float) -> float:
    return pi * sqrt(a_j_m / k_j_m3) * 1e9


def bloch_wall_energy_mj_m2(a_j_m: float, k_j_m3: float) -> float:
    return 4.0 * sqrt(a_j_m * k_j_m3) * 1e3


def magnetostatic_density(js_tesla: float) -> float:
    """(mu0/2) Ms^2 written with the polarization Js = mu0 Ms, in J/m^3."""
    return js_tesla**2 / (2.0 * MU_0)


def prolate_n_long(aspect: float) -> float:
    """Demagnetizing factor along the long axis of a prolate spheroid (Osborn 1945)."""
    m = aspect
    root = sqrt(m * m - 1.0)
    return (m / root * log(m + root) - 1.0) / (m * m - 1.0)


def prolate_delta_n(aspect: float) -> float:
    """N_transverse - N_long for a prolate spheroid; trace of N is 1."""
    n_long = prolate_n_long(aspect)
    return (1.0 - n_long) / 2.0 - n_long


# (where the figure is quoted, what it is, recomputed value, quoted value, relative tolerance)
CHECKS: list[tuple[str, str, float, float, float]] = []


def check(where: str, what: str, computed: float, quoted: float, rtol: float = 0.05) -> None:
    """Register one check. The default tolerance allows for a figure quoted to two digits."""
    CHECKS.append((where, what, computed, quoted, rtol))


CM1_TO_GHZ = 29.9792458  # 1 cm^-1 in GHz (c is exact)

# --- library/antiferromagnetic-order.md --------------------------------------
_AFM = "library/antiferromagnetic-order.md §4.3"
check(_AFM, "theta/T_N, MnO (610 K / 116 K)", 610 / 116, 5.3)
check(_AFM, "theta/T_N, FeO (570 K / 198 K)", 570 / 198, 2.9)
check(_AFM, "theta/T_N, CoO (330 K / 291 K)", 330 / 291, 1.1)
check(_AFM, "theta/T_N, NiO (2000 K / 525 K)", 2000 / 525, 3.8)
check(_AFM, "MnO resonance 27.5 cm^-1 in THz", 27.5 * CM1_TO_GHZ / 1e3, 0.82)
check(_AFM, "NiO resonance 36.6 cm^-1 in THz", 36.6 * CM1_TO_GHZ / 1e3, 1.10)
check(_AFM, "FeF2 resonance 52.7 cm^-1 in THz", 52.7 * CM1_TO_GHZ / 1e3, 1.58)
check(_AFM, "k T_N / h for MnO (118 K) in THz", K_B * 118 / H_PLANCK / 1e12, 2.5)
check(_AFM, "k T_N / h for NiO (523 K) in THz", K_B * 523 / H_PLANCK / 1e12, 10.9)
check(_AFM, "MnO resonance as a fraction of k T_N / h", 0.82 / 2.46, 0.33)
check(_AFM, "NiO resonance as a fraction of k T_N / h", 1.10 / 10.9, 0.10)

OE_TO_A_M = 1e3 / (4.0 * pi)  # 1 Oe in A/m

# --- library/ferromagnetic-hysteresis.md -------------------------------------
_HYS = "library/ferromagnetic-hysteresis.md §4.3"
check(_HYS, "alnico 1707 Oe in kA/m", 1707 * OE_TO_A_M / 1e3, 136)
check(_HYS, "mu0 Hc = 1.2 T in kA/m", 1.2 / MU_0 / 1e3, 955)
check(_HYS, "mu0 Hc = 3.0 T in MA/m", 3.0 / MU_0 / 1e6, 2.39)
check(_HYS, "HcJ = 960 kA/m as mu0 HcJ in T", 960e3 * MU_0, 1.21)
check(_HYS, "coercivity ratio, 960 kA/m over 2 A/m", 960e3 / 2, 4.8e5)
check(_HYS, "coercivity ratio, 960 kA/m over 0.3 A/m", 960e3 / 0.3, 3.2e6)
check(_HYS, "decades in a ratio of 4.8e5", log(4.8e5) / log(10), 5.7)
check(_HYS, "decades in a ratio of 3.2e6", log(3.2e6) / log(10), 6.5)
check(_HYS, "Ms of Nd2Fe14B from 1.61 T, in MA/m", 1.61 / MU_0 / 1e6, 1.28)
check(_HYS, "Hc/Ms, first sintered Nd-Fe-B (960 kA/m, 1.61 T)", 960e3 / (1.61 / MU_0), 0.75)
check(_HYS, "Ms of Fe from 2.15 T, in MA/m", 2.15 / MU_0 / 1e6, 1.71)
check(_HYS, "Hc/Ms, polycrystalline Fe at 10 A/m", 10 / (2.15 / MU_0), 5.8e-6)
check(_HYS, "Hc/Ms, polycrystalline Fe at 100 A/m", 100 / (2.15 / MU_0), 5.8e-5)
check(_HYS, "Fe Curie point 770 C in K", 770 + 273.15, 1043, 0.001)
check(_HYS, "Nd2Fe14B Curie point 312 C in K", 312 + 273.15, 585, 0.001)
check(_HYS, "Nd2Fe14B Curie point 320 C in K", 320 + 273.15, 593, 0.001)
# Quoted from the source, recomputed here as a unit check only.
check(_HYS, "Landauer limit k_B T ln 2 at 300 K in zJ", K_B * 300 * log(2) * 1e21, 2.8)
check(_HYS, "6.09 zJ in units of k_B T at 300 K", 6.09e-21 / (K_B * 300), 1.45)

# --- library/magnetic-domains.md ---------------------------------------------
_DOM = "library/magnetic-domains.md §4.3"
check(_DOM, "single-domain diameter of Fe, twice 6 nm", 2 * 6, 12, 0.001)
check(_DOM, "single-domain diameter of Co, twice 34 nm", 2 * 34, 68, 0.001)
check(_DOM, "single-domain diameter of Ni, twice 16 nm", 2 * 16, 32, 0.001)
check(_DOM, "single-domain diameter of BaFe12O19, twice 290 nm", 2 * 290, 580, 0.001)
check(_DOM, "single-domain diameter of Nd2Fe14B, twice 107 nm", 2 * 107, 214, 0.001)
check(_DOM, "single-domain diameter of SmCo5, twice 764 nm", 2 * 764, 1528, 0.001)
check(_DOM, "Nd2Fe14B wall width, A = 7.7 pJ/m, K1 = 4.9 MJ/m3, in nm", bloch_wall_width_nm(7.7e-12, 4.9e6), 3.9)
check(_DOM, "Nd2Fe14B wall width, A = 7.7 pJ/m, K1 = 4.3 MJ/m3, in nm", bloch_wall_width_nm(7.7e-12, 4.3e6), 4.2)
check(_DOM, "Nd2Fe14B wall energy, K1 = 4.9 MJ/m3, in mJ/m2", bloch_wall_energy_mj_m2(7.7e-12, 4.9e6), 25)
check(_DOM, "Nd2Fe14B wall energy, K1 = 4.3 MJ/m3, in mJ/m2", bloch_wall_energy_mj_m2(7.7e-12, 4.3e6), 23)
check(
    _DOM,
    "Nd2Fe14B single-domain diameter, K1 = 4.9 MJ/m3, 1.61 T, in nm",
    72 * sqrt(7.7e-12 * 4.9e6) / (2 * magnetostatic_density(1.61)) * 1e9,
    214,
    0.01,
)
check(
    _DOM,
    "Nd2Fe14B single-domain diameter, K1 = 4.3 MJ/m3, 1.61 T, in nm",
    72 * sqrt(7.7e-12 * 4.3e6) / (2 * magnetostatic_density(1.61)) * 1e9,
    201,
    0.01,
)
check(_DOM, "2.0 microerg/cm in pJ/m", 2.0e-6 * 1e-7 / 1e-2 * 1e12, 20, 0.001)
check(_DOM, "exchange stiffness ratio, Fe (20 / 8.3)", 20 / 8.3, 2.4)
check(_DOM, "exchange stiffness ratio, Co (25 / 10.3)", 25 / 10.3, 2.4)
check(_DOM, "exchange stiffness ratio, Ni (8 / 3.4)", 8 / 3.4, 2.4)
check(_DOM, "square root of the exchange ratio 2.4", sqrt(2.4), 1.55, 0.01)
check(_DOM, "Fe wall width, A = 8.3 pJ/m, K1 = 0.05 MJ/m3, in nm", bloch_wall_width_nm(8.3e-12, 0.05e6), 40)
check(_DOM, "Fe wall width, A = 20 pJ/m, K1 = 0.05 MJ/m3, in nm", bloch_wall_width_nm(20e-12, 0.05e6), 63, 0.01)
check(_DOM, "wall energy ratio, Fe (2.6 / 1.2)", 2.6 / 1.2, 2.2)
check(_DOM, "wall energy ratio, BaFe12O19 (9 / 5.7)", 9 / 5.7, 1.6)
check(_DOM, "wall energy ratio, SmCo5 (120 / 77)", 120 / 77, 1.6)
check(_DOM, "wall energy ratio, Nd2Fe14B (27 / 25)", 27 / 25, 1.1)
check(_DOM, "Kittel particle size 2e-6 cm in nm", 2e-6 * 1e-2 * 1e9, 20, 0.001)
check(_DOM, "Kittel film thickness 3e-5 cm in nm", 3e-5 * 1e-2 * 1e9, 300, 0.001)

# --- library/shape-anisotropy.md ---------------------------------------------
_SHP = "library/shape-anisotropy.md §4.3"
check(_SHP, "delta N, prolate spheroid, aspect ratio 2", prolate_delta_n(2), 0.240, 0.005)
check(_SHP, "delta N, prolate spheroid, aspect ratio 5", prolate_delta_n(5), 0.416, 0.005)
check(_SHP, "delta N, prolate spheroid, aspect ratio 10", prolate_delta_n(10), 0.470, 0.005)
check(_SHP, "delta N at aspect ratio 2 over the needle limit 0.5", prolate_delta_n(2) / 0.5, 0.48, 0.02)
check(_SHP, "delta N at aspect ratio 5 over the needle limit 0.5", prolate_delta_n(5) / 0.5, 0.83, 0.02)
check(_SHP, "delta N at aspect ratio 10 over the needle limit 0.5", prolate_delta_n(10) / 0.5, 0.94, 0.02)
check(_SHP, "(mu0/2) Ms^2 for Fe at 2.15 T, in MJ/m3", magnetostatic_density(2.15) / 1e6, 1.84, 0.005)
check(_SHP, "(mu0/2) Ms^2 for Ni at 0.61 T, in MJ/m3", magnetostatic_density(0.61) / 1e6, 0.15)
check(_SHP, "(mu0/2) Ms^2 for Ni at 0.62 T, in MJ/m3", magnetostatic_density(0.62) / 1e6, 0.15)
check(_SHP, "Fe over Ni scale, Ni at 0.61 T", magnetostatic_density(2.15) / magnetostatic_density(0.61), 12)
check(_SHP, "Fe over Ni scale, Ni at 0.62 T", magnetostatic_density(2.15) / magnetostatic_density(0.62), 12)
check(_SHP, "(mu0/2) Ms^2 for Nd2Fe14B at 1.61 T, in MJ/m3", magnetostatic_density(1.61) / 1e6, 1.03, 0.005)
check(_SHP, "Fe needle maximum of K_shape, in MJ/m3", 0.5 * magnetostatic_density(2.15) / 1e6, 0.92, 0.005)
check(_SHP, "Fe K_shape at aspect ratio 2, in MJ/m3", prolate_delta_n(2) * magnetostatic_density(2.15) / 1e6, 0.44, 0.02)
check(_SHP, "Fe K_shape at aspect ratio 5, in MJ/m3", prolate_delta_n(5) * magnetostatic_density(2.15) / 1e6, 0.77, 0.02)
check(_SHP, "Fe K_shape at aspect ratio 10, in MJ/m3", prolate_delta_n(10) * magnetostatic_density(2.15) / 1e6, 0.86, 0.02)
check(_SHP, "Fe needle maximum over Fe K1 (0.92 / 0.05)", 0.92 / 0.05, 18)
check(_SHP, "Fe needle maximum over hard-ferrite K1 (0.92 / 0.36)", 0.92 / 0.36, 2.6)
check(_SHP, "Fe needle maximum over hard-ferrite K1 (0.92 / 0.32)", 0.92 / 0.32, 2.9)
check(_SHP, "Nd2Fe14B K1 over Fe needle maximum (4.3 / 0.92)", 4.3 / 0.92, 4.7)
check(_SHP, "Nd2Fe14B K1 over Fe needle maximum (4.9 / 0.92)", 4.9 / 0.92, 5.3)
check(_SHP, "SmCo5 K1 over Fe needle maximum (17.2 / 0.92)", 17.2 / 0.92, 19)
check(_SHP, "Fe needle field Ms/2 from 4 pi Ms = 21.4 kG, in kOe", 21.4 / 2, 10.7, 0.001)
check(_SHP, "1600 Oe over 10.7 kOe", 1600 / 10700, 0.15)
check(_SHP, "2000 Oe over 10.7 kOe", 2000 / 10700, 0.19)
check(_SHP, "1600 Oe in kA/m", 1600 * OE_TO_A_M / 1e3, 127, 0.005)
check(_SHP, "2000 Oe in kA/m", 2000 * OE_TO_A_M / 1e3, 159, 0.005)
check(_SHP, "127 kA/m over 100 A/m", 127e3 / 100, 1.3e3)
check(_SHP, "127 kA/m over 10 A/m", 127e3 / 10, 1.3e4)


# --- library/permanent-magnet-latch.md ---------------------------------------
_PML = "library/permanent-magnet-latch.md §4.3"
check(_PML, "K1 ratio Nd2Fe14B / Fe, low (4.3 MJ/m3 over 48 kJ/m3)", 4.3e6 / 48e3, 90)
check(_PML, "K1 ratio Nd2Fe14B / Fe, high (4.9 MJ/m3 over 48 kJ/m3)", 4.9e6 / 48e3, 102)
check(_PML, "960 kA/m as mu0*H in tesla", MU_0 * 960e3, 1.2)
check(_PML, "coercivity as a fraction of the 7.65 T anisotropy field", 1.2 / 7.65, 0.16)
check(_PML, "coercivity as a fraction of the 6.7 T anisotropy field", 1.2 / 6.7, 0.18)
check(_PML, "ideal-grain coercivity over ideal nucleation field (3.94 T / 6.09 T)", 3.94 / 6.09, 0.65)
check(_PML, "V = 25 kT / K1 at 300 K, K1 = 4.9 MJ/m3 (m3)", stable_volume(4.9e6, 300, 25), 2.1e-26)
check(_PML, "V = 25 kT / K1 at 300 K, K1 = 4.3 MJ/m3 (m3)", stable_volume(4.3e6, 300, 25), 2.4e-26)
check(_PML, "sphere diameter of that volume, K1 = 4.9 (nm)", sphere_diameter_nm(stable_volume(4.9e6, 300, 25)), 3.4)
check(_PML, "sphere diameter of that volume, K1 = 4.3 (nm)", sphere_diameter_nm(stable_volume(4.3e6, 300, 25)), 3.6)
check(_PML, "cube edge of that volume, K1 = 4.9 (nm)", cube_edge_nm(stable_volume(4.9e6, 300, 25)), 2.8)
check(_PML, "cube edge of that volume, K1 = 4.3 (nm)", cube_edge_nm(stable_volume(4.3e6, 300, 25)), 2.9)
check(_PML, "KV/kT of a 30 nm cube at K1 = 4.5 MJ/m3 (the first version's figure)", 4.5e6 * (30e-9) ** 3 / (K_B * 300), 29000)

# --- library/superparamagnetism.md -------------------------------------------
_SPM = "library/superparamagnetism.md §4.3"
TEN_YEARS_S = 10 * 365.25 * 86400
check(_SPM, "ln(100 s / 1e-9 s)", log(100 / 1e-9), 25.3)
check(_SPM, "ln(10 years / 1e-9 s)", log(TEN_YEARS_S / 1e-9), 40.3)
check(_SPM, "ln(1e-8 s / 1e-9 s), Mössbauer window", log(1e-8 / 1e-9), 2.3)
check(_SPM, "Nd2Fe14B sphere at 25 kT, K1 = 4.9 (nm)", sphere_diameter_nm(stable_volume(4.9e6, 300, 25)), 3.4)
check(_SPM, "Nd2Fe14B sphere at 25 kT, K1 = 4.3 (nm)", sphere_diameter_nm(stable_volume(4.3e6, 300, 25)), 3.6)
check(_SPM, "Nd2Fe14B sphere at 60 kT, K1 = 4.9 (nm)", sphere_diameter_nm(stable_volume(4.9e6, 300, 60)), 4.6)
check(_SPM, "Nd2Fe14B sphere at 60 kT, K1 = 4.3 (nm)", sphere_diameter_nm(stable_volume(4.3e6, 300, 60)), 4.8)
check(_SPM, "magnetite sphere at 25 kT, K = 13.5 kJ/m3 (nm)", sphere_diameter_nm(stable_volume(13.5e3, 300, 25)), 24.5)
check(_SPM, "magnetite cubic barrier K1/12 (kJ/m3)", 13.5 / 12, 1.1)
check(_SPM, "magnetite sphere at 25 kT on the cubic barrier (nm)", sphere_diameter_nm(stable_volume(13.5e3 / 12, 300, 25)), 56)
check(_SPM, "Fe blocking diameter, K1 = 48 kJ/m3 (nm; tabulated 16)", sphere_diameter_nm(stable_volume(48e3, 300, 25)), 16)
check(_SPM, "Co blocking diameter, K1 = 530 kJ/m3 (nm; tabulated 7)", sphere_diameter_nm(stable_volume(530e3, 300, 25)), 7)
check(_SPM, "Ni blocking diameter, K1 = 5 kJ/m3 (nm; tabulated 34)", sphere_diameter_nm(stable_volume(5e3, 300, 25)), 34)
check(_SPM, "K1 ratio Nd2Fe14B / magnetite, low", 4.3e6 / 13.5e3, 320)
check(_SPM, "K1 ratio Nd2Fe14B / magnetite, high", 4.9e6 / 13.5e3, 360)
check(_SPM, "diameter ratio magnetite / Nd2Fe14B", 24.5 / 3.5, 7)
check(_SPM, "retention-time factor for +10 % diameter near 25 kT", exp(25.3 * (1.1**3 - 1)), 4000, rtol=0.1)
check(_SPM, "extra diameter needed for ten years instead of 100 s", (40.3 / 25.3) ** (1 / 3) - 1, 0.17)
check(_SPM, "effective over bulk anisotropy of 5 nm magnetite (356 / 13.5)", 356 / 13.5, 26)
check(_SPM, "blocking temperature ratio with and without the pin (290 K / 10 K)", 290 / 10, 29)


# Later batches keep their checks one file per cluster in analysis/checks/*.py.
# Each file is executed in this module's namespace, so it can use check(), the
# constants and the helpers above, and may define helpers of its own. Add a
# file there rather than growing this one; two editors can then work at once.
for _path in sorted((Path(__file__).resolve().parent / "checks").glob("*.py")):
    exec(compile(_path.read_text(encoding="utf-8"), str(_path), "exec"), globals())

def run_checks(verbose: bool = False) -> int:
    failures = []
    for where, what, computed, quoted, rtol in CHECKS:
        ok = abs(computed - quoted) <= rtol * abs(quoted) if quoted else abs(computed) <= rtol
        if verbose:
            mark = "ok  " if ok else "FAIL"
            print(f"{mark} {where}: {what}: computed {computed:.4g}, quoted {quoted:.4g}")
        if not ok:
            failures.append(
                f"{where}: {what}: computed {computed:.4g} but the library quotes {quoted:.4g}"
            )
    if failures:
        raise SystemExit("computed check failed:\n  " + "\n  ".join(failures))
    return len(CHECKS)


if __name__ == "__main__":
    n = run_checks(verbose=True)
    print(f"{n} computed values agree with the figures quoted in library/")
