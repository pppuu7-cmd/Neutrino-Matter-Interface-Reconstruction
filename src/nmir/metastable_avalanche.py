"""Source-resolved energy accounting for passive metastable avalanche media."""

from __future__ import annotations


def avalanche_event(
    *,
    epsilon_nu_ev: float,
    stored_release_ev: float,
    barrier_ev: float,
    assist_ev: float = 0.0,
) -> dict[str, float | bool]:
    """Return deterministic trigger eligibility and ideal source-resolved ledger.

    This is an accounting model, not a switching-rate model.  It deliberately
    attributes stored free-energy release to the medium rather than to the
    incident neutrino.
    """
    vals = (epsilon_nu_ev, stored_release_ev, barrier_ev, assist_ev)
    if any(x < 0.0 for x in vals):
        raise ValueError("all energies must be non-negative")

    eligible = epsilon_nu_ev + assist_ev >= barrier_ev
    if not eligible:
        return {
            "triggered": False,
            "output_total_ev": 0.0,
            "output_neutrino_ev": 0.0,
            "output_medium_ev": 0.0,
            "output_assist_ev": 0.0,
            "signal_gain_over_neutrino_trigger": 0.0,
            "neutrino_energy_gain": 0.0,
            "ideal_reset_work_ev": 0.0,
        }

    total = epsilon_nu_ev + assist_ev + stored_release_ev
    signal_gain = total / epsilon_nu_ev if epsilon_nu_ev > 0.0 else float("inf")
    nu_gain = 1.0 if epsilon_nu_ev > 0.0 else 0.0
    return {
        "triggered": True,
        "output_total_ev": total,
        "output_neutrino_ev": epsilon_nu_ev,
        "output_medium_ev": stored_release_ev,
        "output_assist_ev": assist_ev,
        "signal_gain_over_neutrino_trigger": signal_gain,
        "neutrino_energy_gain": nu_gain,
        "ideal_reset_work_ev": stored_release_ev,
    }


def source_ledger_residual(event: dict[str, float | bool]) -> float:
    """Return total output minus source-resolved output components."""
    return float(event["output_total_ev"]) - (
        float(event["output_neutrino_ev"])
        + float(event["output_medium_ev"])
        + float(event["output_assist_ev"])
    )


def cyclic_net_external_energy_requirement_ev(
    *,
    cycles: int,
    stored_release_ev: float,
    dissipative_overhead_ev_per_cycle: float = 0.0,
) -> float:
    """Lower bound on external reset/recharge energy for repeated operation."""
    if cycles < 0:
        raise ValueError("cycles must be non-negative")
    if stored_release_ev < 0.0 or dissipative_overhead_ev_per_cycle < 0.0:
        raise ValueError("energies must be non-negative")
    return cycles * (stored_release_ev + dissipative_overhead_ev_per_cycle)
