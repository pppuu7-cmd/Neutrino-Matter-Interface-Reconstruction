from __future__ import annotations

DAYS_PER_YEAR = 365.25
RATES = {
    "Ar40_10eV": 6.486648607e-3,
    "Ar40_20eV": 3.617516800e-3,
    "Ar40_40eV": 1.161110164e-3,
    "Si28_10eV": 4.3476963498860904e-3,
    "Ge74_10eV": 7.871654050e-3,
    "Se82_10eV": 8.212077955e-3,
}


def ideal_events_per_year(rate_per_kg_day: float, mass_kg: float) -> float:
    if rate_per_kg_day < 0 or mass_kg < 0:
        raise ValueError("rate and mass must be nonnegative")
    return rate_per_kg_day * mass_kg * DAYS_PER_YEAR


def required_eta(rate_per_kg_day: float, mass_kg: float, goal_events_per_year: float) -> float:
    if rate_per_kg_day <= 0 or mass_kg <= 0 or goal_events_per_year < 0:
        raise ValueError("rate/mass must be positive and goal nonnegative")
    return goal_events_per_year / ideal_events_per_year(rate_per_kg_day, mass_kg)


def required_effective_mass_kg(rate_per_kg_day: float, goal_events_per_year: float) -> float:
    if rate_per_kg_day <= 0 or goal_events_per_year < 0:
        raise ValueError("rate must be positive and goal nonnegative")
    return goal_events_per_year / (rate_per_kg_day * DAYS_PER_YEAR)


def feasibility(eta: float) -> str:
    return "RATE_FEASIBLE_TRANSFER_TARGET" if eta <= 1.0 else "RATE_IMPOSSIBLE_AT_FIXED_MASS"
