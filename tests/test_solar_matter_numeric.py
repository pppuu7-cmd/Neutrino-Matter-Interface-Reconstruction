import pytest

from nmir.solar_matter import (
    SolarMatterSource,
    normalized_production_weights,
    parse_solar_matter_bytes,
    production_integrals,
    trapezoid_integral,
)


def _manifest():
    return {
        "toy": SolarMatterSource(
            model="toy",
            source_repo="x/y",
            source_commit="0" * 40,
            source_path="toy.dat",
            source_blob_sha="0" * 40,
            reference="toy",
            radius_column=0,
            density_log10_column=2,
            production_columns={
                "pp": 4,
                "pep": 5,
                "hep": 6,
                "Be7": 7,
                "B8": 8,
                "N13": 9,
                "O15": 10,
                "F17": 11,
            },
            density_units="cm^-3/N_A",
            notes="toy",
        )
    }


def _bytes():
    return (
        b"# toy\n"
        b"0.0 1.0 2.0 0.0 1 2 3 4 5 6 7 8\n"
        b"0.5 1.0 1.0 0.0 1 2 3 4 5 6 7 8\n"
        b"1.0 1.0 0.0 0.0 1 2 3 4 5 6 7 8\n"
    )


def test_trapezoid_integral_linear():
    assert trapezoid_integral([0.0, 0.5, 1.0], [0.0, 0.5, 1.0]) == pytest.approx(0.5)


def test_parser_and_integrals_without_identity_check():
    t = parse_solar_matter_bytes("toy", _bytes(), _manifest(), verify_blob=False)
    assert t.radius_rsun == pytest.approx((0.0, 0.5, 1.0))
    assert t.electron_density_mol_cm3 == pytest.approx((100.0, 10.0, 1.0))
    ints = production_integrals(t)
    assert ints["pp"] == pytest.approx(1.0)
    assert ints["F17"] == pytest.approx(8.0)


def test_normalized_weights_sum_to_one():
    t = parse_solar_matter_bytes("toy", _bytes(), _manifest(), verify_blob=False)
    w = normalized_production_weights(t, "B8")
    assert sum(w) == pytest.approx(1.0)
    assert all(x >= 0.0 for x in w)


def test_parser_rejects_nonmonotonic_radius():
    bad = _bytes().replace(b"0.5 1.0", b"0.0 1.0", 1)
    with pytest.raises(ValueError, match="non-monotonic"):
        parse_solar_matter_bytes("toy", bad, _manifest(), verify_blob=False)
