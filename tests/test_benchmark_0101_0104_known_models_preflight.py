from scripts.benchmark_0101_0104_known_models_preflight import (
    run_0101,
    run_0102,
    run_0103,
    run_0104,
    run_all,
)


def _assert_nonterminal_pass(result, expected_status, expected_ceiling):
    assert result["status"] == expected_status
    assert all(result["gates"].values())
    assert result["terminal_physics_execution_allowed"] is False
    assert result["terminal_status_ceiling"] == expected_ceiling


def test_0101_sterile_preflight():
    _assert_nonterminal_pass(
        run_0101(),
        "PASS_0101_3P1_MATHEMATICAL_PREFLIGHT_NONTERMINAL",
        "BLOCKED_0101_STERILE_PARAMETER_AUTHORITY_UNPINNED",
    )


def test_0102_nsi_preflight():
    _assert_nonterminal_pass(
        run_0102(),
        "PASS_0102_NSI_MATHEMATICAL_PREFLIGHT_NONTERMINAL",
        "BLOCKED_0102_NSI_PARAMETER_AUTHORITY_UNPINNED",
    )


def test_0103_magnetic_spin_flavor_preflight():
    _assert_nonterminal_pass(
        run_0103(),
        "PASS_0103_MAGNETIC_SPIN_FLAVOR_MATHEMATICAL_PREFLIGHT_NONTERMINAL",
        "BLOCKED_0103_MAGNETIC_AND_FIELD_AUTHORITY_UNPINNED",
    )


def test_0104_light_mediator_preflight():
    _assert_nonterminal_pass(
        run_0104(),
        "PASS_0104_LIGHT_MEDIATOR_MATHEMATICAL_PREFLIGHT_NONTERMINAL",
        "BLOCKED_0104_MEDIATOR_PARAMETER_AND_RANGE_AUTHORITY_UNPINNED",
    )


def test_combined_suite_stays_nonterminal():
    result = run_all()
    assert result["preflight_all_pass"] is True
    assert result["terminal_physics_execution_allowed"] is False
    assert set(result["results"]) == {"0101", "0102", "0103", "0104"}
