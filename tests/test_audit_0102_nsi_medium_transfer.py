from scripts.audit_0102_nsi_medium_transfer import (
    effective_vector_epsilon,
    neutron_to_electron_ratio,
    run_audit,
)

import numpy as np
import pytest


def test_medium_transfer_audit_passes_nonterminal():
    result = run_audit()
    assert result["status"] == "PASS_0102_MEDIUM_TRANSFER_INTERFACE_AUDIT_NONTERMINAL"
    assert all(result["gates"].values())
    assert result["interpretation"]["electron_only_vector_maps_to_frozen_0102"] is True
    assert result["interpretation"]["earth_effective_epsilon_transferable_without_operator_identity"] is False
    assert result["interpretation"]["terminal_parameter_authority_closed"] is False
    assert result["interpretation"]["terminal_status_ceiling"] == "BLOCKED_0102_NSI_PARAMETER_AUTHORITY_UNPINNED"


def test_neutron_to_electron_ratio_known_points():
    assert neutron_to_electron_ratio(0.5) == pytest.approx(1.0)
    assert neutron_to_electron_ratio(1.0) == pytest.approx(0.0)
    assert neutron_to_electron_ratio(0.25) == pytest.approx(3.0)


def test_electron_only_effective_epsilon_is_composition_independent():
    eps = np.diag([0.1, -0.03, 0.02]).astype(np.complex128)
    zero = np.zeros((3, 3), dtype=np.complex128)
    for ye in (0.2, 0.5, 0.9):
        mapped = effective_vector_epsilon(eps, zero, zero, ye)
        np.testing.assert_allclose(mapped, eps, atol=1e-14, rtol=0.0)


def test_quark_effective_epsilon_changes_with_composition():
    zero = np.zeros((3, 3), dtype=np.complex128)
    eps_u = np.diag([0.05, 0.0, 0.0]).astype(np.complex128)
    a = effective_vector_epsilon(zero, eps_u, zero, 0.3)
    b = effective_vector_epsilon(zero, eps_u, zero, 0.8)
    assert not np.allclose(a, b, atol=1e-12, rtol=0.0)


def test_invalid_ye_is_rejected():
    with pytest.raises(ValueError):
        neutron_to_electron_ratio(0.0)
    with pytest.raises(ValueError):
        neutron_to_electron_ratio(1.1)
