import math
import random

import pytest

from nmir.metastable_avalanche import (
    avalanche_event,
    cyclic_net_external_energy_requirement_ev,
    source_ledger_residual,
)


def test_mev_reservoir_one_ev_trigger_has_large_signal_but_unit_neutrino_gain():
    out = avalanche_event(
        epsilon_nu_ev=1.0,
        stored_release_ev=1.0e6,
        barrier_ev=0.5,
    )
    assert out["triggered"] is True
    assert math.isclose(float(out["signal_gain_over_neutrino_trigger"]), 1_000_001.0)
    assert math.isclose(float(out["neutrino_energy_gain"]), 1.0)
    assert math.isclose(source_ledger_residual(out), 0.0, abs_tol=1e-15)


def test_stored_energy_changes_signal_gain_not_neutrino_gain():
    trigger = 1.0
    gains = []
    for stored in [1.0, 1.0e3, 1.0e6, 1.0e9]:
        out = avalanche_event(epsilon_nu_ev=trigger, stored_release_ev=stored, barrier_ev=0.1)
        gains.append(float(out["signal_gain_over_neutrino_trigger"]))
        assert float(out["neutrino_energy_gain"]) == 1.0
    assert gains == [2.0, 1001.0, 1_000_001.0, 1_000_000_001.0]


def test_subbarrier_trigger_fails_closed_without_assist():
    out = avalanche_event(epsilon_nu_ev=0.2, stored_release_ev=1.0e6, barrier_ev=0.5)
    assert out["triggered"] is False
    assert float(out["output_total_ev"]) == 0.0


def test_assist_must_be_explicitly_accounted():
    out = avalanche_event(
        epsilon_nu_ev=0.2,
        stored_release_ev=1.0e6,
        barrier_ev=0.5,
        assist_ev=0.3,
    )
    assert out["triggered"] is True
    assert math.isclose(float(out["output_assist_ev"]), 0.3)
    assert math.isclose(source_ledger_residual(out), 0.0, abs_tol=1e-15)


def test_recharge_lower_bound_tracks_stored_release():
    assert cyclic_net_external_energy_requirement_ev(cycles=10, stored_release_ev=1e6) == 1e7
    assert cyclic_net_external_energy_requirement_ev(
        cycles=10, stored_release_ev=1e6, dissipative_overhead_ev_per_cycle=2e5
    ) == 1.2e7


def test_random_ledgers_conserve_sources():
    rng = random.Random(20260906)
    for _ in range(500):
        enu = 10 ** rng.uniform(-3.0, 6.0)
        stored = 10 ** rng.uniform(-3.0, 12.0)
        barrier = enu * rng.uniform(0.0, 1.0)
        assist = 10 ** rng.uniform(-6.0, 3.0)
        out = avalanche_event(
            epsilon_nu_ev=enu,
            stored_release_ev=stored,
            barrier_ev=barrier,
            assist_ev=assist,
        )
        scale = max(1.0, abs(float(out["output_total_ev"])))
        assert abs(source_ledger_residual(out)) / scale < 1e-12
        if out["triggered"]:
            assert float(out["neutrino_energy_gain"]) == 1.0


def test_negative_inputs_fail_closed():
    with pytest.raises(ValueError):
        avalanche_event(epsilon_nu_ev=-1, stored_release_ev=1, barrier_ev=0)
    with pytest.raises(ValueError):
        cyclic_net_external_energy_requirement_ev(cycles=-1, stored_release_ev=1)
