from pathlib import Path

import pytest

import nmir.se82_solar_fold as fold


def test_zero_weight_zero_energy_endpoint_does_not_call_pee(tmp_path: Path, monkeypatch):
    spectrum = tmp_path / "toy.csv"
    spectrum.write_text("0.0,0.0\n0.2,1.0\n0.3,1.0\n", encoding="utf-8")

    def fake_pee_function(_table, _component):
        def pee(energy):
            if energy <= 0.0:
                raise AssertionError("Pee must not be evaluated at a zero-weight E=0 endpoint")
            return 0.5
        return pee

    monkeypatch.setattr(fold, "_pee_function", fake_pee_function)
    rate, moment = fold._continuum("pp", 1.0, object(), spectrum, oscillated=True)
    assert rate >= 0.0
    assert moment >= 0.0
