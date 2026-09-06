import pytest

from nmir.b8_historical_audit import (
    load_bahcall_lisi1996_spectrum,
    source_average_from_sparse_table,
)


def test_bahcall_lisi1996_spectrum_is_normalized():
    e, lam = load_bahcall_lisi1996_spectrum()
    assert len(e) == 160
    assert e[0] == pytest.approx(0.1)
    assert e[-1] == pytest.approx(16.0)


def test_matched_1996_improved_sparse_fold_near_published_average():
    # Bahcall et al. (1996) publish 1.14e-42 cm^2 using their full internal
    # response.  Sparse Table-II interpolation should agree at few-percent level.
    got = source_average_from_sparse_table("improved_1e46_cm2")
    assert got == pytest.approx(1.14e-42, rel=0.025)


def test_bu_sparse_column_with_1996_spectrum_matches_1996_recalculation():
    # Same 1996 paper states that using the older low-energy data with the new
    # spectrum gives 1.08e-42 cm^2; sparse BU tabulation should reproduce it.
    got = source_average_from_sparse_table("bahcall_ulrich_1e46_cm2")
    assert got == pytest.approx(1.08e-42, rel=0.02)
