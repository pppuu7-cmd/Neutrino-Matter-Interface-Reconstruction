from math import isclose

from nmir.cevns_threshold import (
    AR40_ATOMIC_MASS_U,
    ar40_reference_map,
    nuclear_mass_mev,
    recoil_max_mev,
    source_min_energy_mev,
)


def test_forward_inverse_roundtrip():
    masses = [1.0e3, 1.0e4, 4.0e4, 1.2e5]
    energies = [0.1, 0.42, 0.8618, 1.44, 10.0, 20.0]
    for m in masses:
        for e in energies:
            t = recoil_max_mev(e, m)
            recovered = source_min_energy_mev(t, m)
            assert isclose(recovered, e, rel_tol=1e-12, abs_tol=1e-15)


def test_monotonicity():
    m = 4.0e4
    assert recoil_max_mev(1.0, m) < recoil_max_mev(2.0, m)
    assert recoil_max_mev(1.0, 2.0e4) > recoil_max_mev(1.0, 4.0e4)


def test_ar40_40ev_source_opening_map():
    result = ar40_reference_map(40.0)
    assert result["open"]["pp_endpoint"] is False
    assert result["open"]["pep_line"] is True
    assert result["open"]["b8_endpoint"] is True
    # Be7 is the deliberately interesting boundary case; freeze the exact result.
    assert result["open"]["be7_line"] is False
    assert 0.86 < result["source_min_energy_mev"] < 0.87


def test_ar40_mass_positive():
    assert nuclear_mass_mev(AR40_ATOMIC_MASS_U) > 3.7e4
