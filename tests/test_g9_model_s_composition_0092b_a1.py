import importlib.util
from pathlib import Path
import numpy as np

SPEC = importlib.util.spec_from_file_location('m', Path('scripts/g9_model_s_composition_0092b_a1.py'))
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def test_simpson_quadratic_exact():
    n = 128
    x = np.linspace(0.0, 1.0, n + 1)
    got = m.simpson_uniform(x*x, 1.0/n)
    assert abs(got - 1.0/3.0) < 1e-14


def test_frozen_semantics_and_guards_present():
    text = Path('scripts/g9_model_s_composition_0092b_a1.py').read_text()
    assert '"nn": 2482' in text
    assert '"ivers": 210' in text
    assert 'var[:, 5]' in text
    assert 'var[:, 16]' in text
    assert 'PASS_G9_0092B_MODEL_S_COMPOSITION_AUTHORITY' in text
    assert 'BLOCKED_G9_0092B_COMPOSITION_NUMERICS' in text


def test_frozen_total_column_and_density_hash():
    assert m.SIGMA_TOTAL_AUTH == 2.9324883602905845e12
    assert m.LIMITED_SHA_AUTH == '65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc'
