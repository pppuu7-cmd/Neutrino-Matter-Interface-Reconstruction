import pytest

from nmir.cl37_source_average import be7_authority_oscillated_snu, load_cl37_source_averages


def test_cl37_source_average_table_identity():
    x = load_cl37_source_averages()
    assert x["pp"] == 0.0
    assert x["pep"] == pytest.approx(16.0e-46)
    assert x["Be7"] == pytest.approx(2.4e-46)
    assert x["B8"] == pytest.approx(1.06e-42)
    assert x["hep"] == pytest.approx(3.9e-42)


def test_be7_authority_rate_scale():
    # Representative B16-GS98 flux and validated Pee checkpoint.
    rate = be7_authority_oscillated_snu(4.93e9, 0.526972)
    assert rate == pytest.approx(0.6235, rel=2e-3)


def test_be7_authority_guards():
    with pytest.raises(ValueError):
        be7_authority_oscillated_snu(-1.0, 0.5)
    with pytest.raises(ValueError):
        be7_authority_oscillated_snu(1.0, 1.1)
