from scripts.audit_known_model_funnel_readiness import run_audit


def test_execution_framework_is_complete_but_terminal_authority_is_separate():
    result = run_audit()
    assert result["repository_execution_framework_ready"] is True
    assert result["repository_execution_framework_percent"] == 100
    assert all(result["files"].values())
    assert all(result["protocol"].values())
    assert all(all(gates.values()) for gates in result["per_model"].values())
    assert result["executable"]["0100_preflight_all_pass"] is True
    assert result["executable"]["0101_0104_preflight_all_pass"] is True
    # A missing external authority is a truthful BLOCKED state, not a reason to
    # relabel the repository execution apparatus as incomplete or a model as FAIL.
    assert result["interpretation"]["blocked_is_not_fail"] is True
