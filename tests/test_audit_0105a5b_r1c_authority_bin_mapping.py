from scripts.audit_0105a5b_r1c_authority_bin_mapping import (
    COSZEN_EDGES,
    ENERGY_EDGES,
    PID_EDGES,
    strict_bin,
)


def test_pid_observed_and_mc_labels_share_authoritative_upper_bin_without_rounding():
    assert strict_bin(0.88, PID_EDGES) == 1
    assert strict_bin(0.875, PID_EDGES) == 1


def test_representative_energy_and_coszen_midpoint_labels_map_by_strict_interval():
    assert strict_bin(7.4, ENERGY_EDGES) == 0
    assert strict_bin(123.3, ENERGY_EDGES) == 9
    assert strict_bin(-0.945, COSZEN_EDGES) == 0
    assert strict_bin(0.045, COSZEN_EDGES) == 9


def test_boundary_value_fails_closed():
    for edges in (PID_EDGES, COSZEN_EDGES, ENERGY_EDGES):
        try:
            strict_bin(edges[1], edges)
        except ValueError:
            pass
        else:
            raise AssertionError("an exact boundary must not be assigned by the strict-interior rule")
