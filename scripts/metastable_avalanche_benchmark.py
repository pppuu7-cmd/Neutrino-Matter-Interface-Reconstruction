"""Hosted benchmark for NMIR passive metastable avalanche accounting."""

from __future__ import annotations

import json
import math
import random

from nmir.metastable_avalanche import (
    avalanche_event,
    cyclic_net_external_energy_requirement_ev,
    source_ledger_residual,
)


def main() -> None:
    control = avalanche_event(
        epsilon_nu_ev=1.0,
        stored_release_ev=1.0e6,
        barrier_ev=0.5,
    )

    stored_scan = {}
    for stored in [1.0, 1.0e3, 1.0e6, 1.0e9]:
        out = avalanche_event(epsilon_nu_ev=1.0, stored_release_ev=stored, barrier_ev=0.1)
        stored_scan[str(stored)] = {
            "signal_gain": out["signal_gain_over_neutrino_trigger"],
            "neutrino_energy_gain": out["neutrino_energy_gain"],
            "ideal_reset_work_ev": out["ideal_reset_work_ev"],
        }

    blocked = avalanche_event(epsilon_nu_ev=0.2, stored_release_ev=1.0e6, barrier_ev=0.5)
    assisted = avalanche_event(
        epsilon_nu_ev=0.2,
        stored_release_ev=1.0e6,
        barrier_ev=0.5,
        assist_ev=0.3,
    )

    rng = random.Random(173205)
    max_rel_residual = 0.0
    max_neutrino_gain = 0.0
    for _ in range(5000):
        enu = 10 ** rng.uniform(-6.0, 7.0)
        stored = 10 ** rng.uniform(-6.0, 15.0)
        barrier = enu * rng.uniform(0.0, 1.0)
        assist = 10 ** rng.uniform(-9.0, 4.0)
        out = avalanche_event(
            epsilon_nu_ev=enu,
            stored_release_ev=stored,
            barrier_ev=barrier,
            assist_ev=assist,
        )
        scale = max(1.0, abs(float(out["output_total_ev"])))
        max_rel_residual = max(max_rel_residual, abs(source_ledger_residual(out)) / scale)
        max_neutrino_gain = max(max_neutrino_gain, float(out["neutrino_energy_gain"]))

    recharge_1000 = cyclic_net_external_energy_requirement_ev(
        cycles=1000,
        stored_release_ev=1.0e6,
    )

    status = "PASS_METASTABLE_AVALANCHE_LEDGER"
    if not (
        control["triggered"] is True
        and math.isclose(float(control["signal_gain_over_neutrino_trigger"]), 1_000_001.0)
        and float(control["neutrino_energy_gain"]) == 1.0
        and blocked["triggered"] is False
        and assisted["triggered"] is True
        and math.isclose(float(assisted["output_assist_ev"]), 0.3)
        and max_rel_residual < 1e-12
        and max_neutrino_gain <= 1.0
        and math.isclose(recharge_1000, 1.0e9)
    ):
        status = "FAIL_METASTABLE_AVALANCHE_LEDGER"

    result = {
        "status": status,
        "one_ev_trigger_mev_reservoir": control,
        "stored_energy_scan": stored_scan,
        "subbarrier_without_assist_triggered": blocked["triggered"],
        "assisted_triggered": assisted["triggered"],
        "assisted_source_ledger": {
            "nu_ev": assisted["output_neutrino_ev"],
            "assist_ev": assisted["output_assist_ev"],
            "medium_ev": assisted["output_medium_ev"],
            "total_ev": assisted["output_total_ev"],
        },
        "random_trials": 5000,
        "max_random_source_ledger_relative_residual": max_rel_residual,
        "max_random_neutrino_energy_gain": max_neutrino_gain,
        "ideal_reset_work_1000_cycles_ev": recharge_1000,
        "interpretation": (
            "A passive metastable medium can amplify a neutrino-triggered event by an arbitrarily large "
            "factor using stored free energy, while source-resolved neutrino energy gain remains <=1. "
            "The released excess belongs to the medium/assist reservoir and cyclic reset must replenish it."
        ),
        "energy_harvesting_classification": "STRONG_NEGATIVE_SCOPED",
        "detector_control_classification": "PASS_SURVIVOR",
        "scope": (
            "source-resolved first-law ledger for passive metastable avalanche media; real switching kinetics, "
            "dark counts, thermal/quantum activation, microscopic neutrino trigger probability and materials remain open"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if status != "PASS_METASTABLE_AVALANCHE_LEDGER":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
