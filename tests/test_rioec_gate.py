import math

import pytest

from nmir.rioec_gate import (
    resonance_area_numeric,
    rioec_cross_section_density,
    smooth_profile_overlap_ratio,
    source_flavor_factor,
)


def test_rioec_flavor_gate_blocks_ordinary_solar_neutrinos():
    for particle in ("nu_e", "nu_mu", "nu_tau"):
        assert source_flavor_factor(particle) == 0.0
    assert source_flavor_factor("anti-nu_e") == 1.0


def test_unknown_particle_class_fails_closed():
    with pytest.raises(ValueError):
        source_flavor_factor("solar")


def test_resonance_peak_can_grow_while_area_stays_fixed():
    B0 = 3.7e-42
    E_R = 0.1
    wide = 1e-3
    narrow = 1e-9
    assert rioec_cross_section_density(E_R, E_R, narrow, B0) > 1e5 * rioec_cross_section_density(E_R, E_R, wide, B0)
    area_wide = resonance_area_numeric(E_R, wide, B0)
    area_narrow = resonance_area_numeric(E_R, narrow, B0)
    assert math.isclose(area_wide, B0, rel_tol=1e-5)
    assert math.isclose(area_narrow, B0, rel_tol=1e-5)
    assert math.isclose(area_wide, area_narrow, rel_tol=1e-12)


def test_smooth_source_overlap_tends_to_area_times_local_spectral_density():
    # A physical resonance eV/sub-eV wide against a keV-scale continuum has
    # gamma/source-scale << 1.  Use 1e-5 as a conservative numerical stress.
    ratio = smooth_profile_overlap_ratio(1e-5)
    assert abs(ratio - 1.0) < 1e-3


def test_overlap_decreases_when_source_is_not_broad_relative_to_resonance():
    assert smooth_profile_overlap_ratio(1.0) < smooth_profile_overlap_ratio(1e-3)
