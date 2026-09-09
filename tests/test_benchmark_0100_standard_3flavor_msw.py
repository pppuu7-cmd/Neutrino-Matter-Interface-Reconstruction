import numpy as np

from scripts.benchmark_0100_standard_3flavor_msw import (
    NUFIT61_IO,
    NUFIT61_NO,
    effective_mass_squared_flavor,
    evolve_constant_density,
    mass_squared_eigenvalues,
    matter_a_eV2,
    pmns_matrix,
    probability_vector,
    propagate_profile,
    pure_flavor,
    relativistic_mass_correction_scale,
    run_preflight,
    synthetic_profile,
    vacuum_probability_direct,
)


def test_pmns_unitarity_no_io():
    for p in (NUFIT61_NO, NUFIT61_IO):
        u = pmns_matrix(p)
        assert np.max(np.abs(u.conjugate().T @ u - np.eye(3))) <= 1e-12


def test_probability_normalization_constant_density():
    for p in (NUFIT61_NO, NUFIT61_IO):
        for alpha in range(3):
            out = evolve_constant_density(pure_flavor(alpha), 1234.5, p, 5.0, rho_g_cm3=80.0, ye=0.5)
            probs = probability_vector(out)
            assert abs(np.sum(probs) - 1.0) <= 1e-12
            assert np.all(np.isfinite(probs))
            assert np.all(probs >= -1e-12)
            assert np.all(probs <= 1.0 + 1e-12)


def test_vacuum_reduction_against_direct_formula():
    for p in (NUFIT61_NO, NUFIT61_IO):
        for alpha in range(3):
            out = evolve_constant_density(pure_flavor(alpha), 1234.5, p, 5.0, rho_g_cm3=0.0)
            probs = probability_vector(out)
            for beta in range(3):
                direct = vacuum_probability_direct(alpha, beta, 1234.5, p, 5.0)
                assert abs(probs[beta] - direct) <= 1e-12


def test_zero_density_removes_matter_term():
    for p in (NUFIT61_NO, NUFIT61_IO):
        h0 = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=0.0, ye=0.1)
        h1 = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=0.0, ye=0.9)
        assert np.max(np.abs(h0 - h1)) <= 1e-15


def test_antineutrino_matter_sign_flip():
    p = NUFIT61_NO
    hnu = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=100.0, ye=0.5, antineutrino=False)
    hnu0 = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=0.0, ye=0.5, antineutrino=False)
    hbar = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=100.0, ye=0.5, antineutrino=True)
    hbar0 = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=0.0, ye=0.5, antineutrino=True)
    assert np.real(hnu[0, 0] - hnu0[0, 0]) > 0
    assert np.real(hbar[0, 0] - hbar0[0, 0]) < 0
    assert np.isclose(
        np.real(hnu[0, 0] - hnu0[0, 0]),
        -np.real(hbar[0, 0] - hbar0[0, 0]),
        rtol=0,
        atol=1e-15,
    )


def test_high_density_matter_term_dominates():
    vacuum_scale = np.max(np.abs(mass_squared_eigenvalues(NUFIT61_NO)))
    matter_scale = abs(matter_a_eV2(1.0e10, 0.5, 5.0))
    assert matter_scale / vacuum_scale >= 1e4


def test_frozen_synthetic_profile_step_convergence():
    psi0 = pure_flavor(0)
    r32, rho32, ye32 = synthetic_profile(3200)
    r64, rho64, ye64 = synthetic_profile(6400)
    p32 = probability_vector(propagate_profile(psi0, r32, rho32, ye32, NUFIT61_NO, 5.0))
    p64 = probability_vector(propagate_profile(psi0, r64, rho64, ye64, NUFIT61_NO, 5.0))
    assert np.max(np.abs(p32 - p64)) < 1e-4


def test_g9_ultrarelativistic_mass_scale_guard():
    assert relativistic_mass_correction_scale(0.46, 0.5) < 5e-13


def test_preflight_cannot_be_terminal_physics_pass():
    result = run_preflight()
    assert result["preflight_all_pass"] is True
    assert result["terminal_physics_execution_allowed"] is False
    assert result["terminal_status_ceiling"] == "BLOCKED_0100_SOURCE_PROFILE_UNPINNED"
