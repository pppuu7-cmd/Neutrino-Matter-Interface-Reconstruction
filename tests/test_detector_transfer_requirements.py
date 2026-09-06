import math

import pytest

from nmir.detector_transfer_requirements import (
    RATES,
    feasibility,
    ideal_events_per_year,
    required_effective_mass_kg,
    required_eta,
)


def test_ar_threshold_topology_for_10kg_10events_per_year():
    eta10 = required_eta(RATES["Ar40_10eV"], 10.0, 10.0)
    eta20 = required_eta(RATES["Ar40_20eV"], 10.0, 10.0)
    eta40 = required_eta(RATES["Ar40_40eV"], 10.0, 10.0)
    assert feasibility(eta10) == "RATE_FEASIBLE_TRANSFER_TARGET"
    assert feasibility(eta20) == "RATE_FEASIBLE_TRANSFER_TARGET"
    assert feasibility(eta40) == "RATE_IMPOSSIBLE_AT_FIXED_MASS"


def test_eta_identity():
    rate = RATES["Ar40_10eV"]
    eta = required_eta(rate, 10.0, 10.0)
    assert math.isclose(ideal_events_per_year(rate, 10.0) * eta, 10.0, rel_tol=1e-15)


def test_effective_mass_identity():
    for rate in RATES.values():
        m = required_effective_mass_kg(rate, 1.0)
        assert math.isclose(ideal_events_per_year(rate, m), 1.0, rel_tol=1e-15)


def test_invalid_inputs_fail_closed():
    with pytest.raises(ValueError):
        required_eta(0.0, 10.0, 1.0)
    with pytest.raises(ValueError):
        required_eta(1.0, 0.0, 1.0)
    with pytest.raises(ValueError):
        required_effective_mass_kg(-1.0, 1.0)
