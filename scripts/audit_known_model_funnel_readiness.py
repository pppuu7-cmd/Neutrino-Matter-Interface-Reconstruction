#!/usr/bin/env python3
"""Static + executable readiness audit for the NMIR known-model funnel.

The audit distinguishes repository execution-framework readiness from terminal
physics-authority readiness. A repository can be 100% execution-ready while a
specific benchmark correctly remains BLOCKED on an external authority input.
"""

from __future__ import annotations

import json
from pathlib import Path

from scripts.benchmark_0100_standard_3flavor_msw import run_preflight as run_0100
from scripts.benchmark_0101_0104_known_models_preflight import run_all as run_0101_0104

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "protocol": "research/benchmarks/KNOWN_MODEL_BENCHMARK_MATRIX.md",
    "0100_prereg": "research/prereg/0100_known_model_benchmark_standard_3flavor_msw.md",
    "0100_code": "scripts/benchmark_0100_standard_3flavor_msw.py",
    "0100_tests": "tests/test_benchmark_0100_standard_3flavor_msw.py",
    "0100_workflow": ".github/workflows/0100-standard-3flavor-msw-preflight.yml",
    "0100a_prereg": "research/prereg/0100a_farmer_source_profile_pinning.md",
    "0100a_code": "scripts/pin_0100a_farmer_profile.py",
    "0100a_tests": "tests/test_pin_0100a_farmer_profile.py",
    "0100a_workflow": ".github/workflows/0100a-pin-farmer-profile.yml",
    "0101_prereg": "research/prereg/0101_known_model_benchmark_3p1_sterile_preflight.md",
    "0102_prereg": "research/prereg/0102_known_model_benchmark_nsi_preflight.md",
    "0103_prereg": "research/prereg/0103_known_model_benchmark_magnetic_spin_flavor_preflight.md",
    "0104_prereg": "research/prereg/0104_known_model_benchmark_light_mediator_preflight.md",
    "0101_0104_code": "scripts/benchmark_0101_0104_known_models_preflight.py",
    "0101_0104_tests": "tests/test_benchmark_0101_0104_known_models_preflight.py",
    "0101_0104_workflow": ".github/workflows/0101-0104-known-model-preflight.yml",
}

EXPECTED_ORDER = ["0100", "0101", "0102", "0103", "0104"]
EXPECTED_CEILINGS = {
    "0100": "BLOCKED_0100_SOURCE_PROFILE_UNPINNED",
    "0101": "BLOCKED_0101_STERILE_PARAMETER_AUTHORITY_UNPINNED",
    "0102": "BLOCKED_0102_NSI_PARAMETER_AUTHORITY_UNPINNED",
    "0103": "BLOCKED_0103_MAGNETIC_AND_FIELD_AUTHORITY_UNPINNED",
    "0104": "BLOCKED_0104_MEDIATOR_PARAMETER_AND_RANGE_AUTHORITY_UNPINNED",
}


def file_gate() -> dict[str, bool]:
    return {key: (ROOT / rel).is_file() for key, rel in REQUIRED_FILES.items()}


def protocol_gate() -> dict[str, bool]:
    text = (ROOT / REQUIRED_FILES["protocol"]).read_text(encoding="utf-8")
    positions = [text.find(f"| {bench} |") for bench in EXPECTED_ORDER]
    return {
        "all_benchmarks_declared": all(pos >= 0 for pos in positions),
        "prospective_order_preserved": positions == sorted(positions),
        "pass_fail_blocked_semantics_present": all(word in text for word in ("PASS", "FAIL", "BLOCKED")),
        "common_reproducibility_axis_present": "REPRODUCIBILITY / PROVENANCE" in text,
    }


def executable_gate() -> tuple[dict, dict]:
    r0100 = run_0100()
    r_rest = run_0101_0104()
    per_model = {
        "0100": {
            "mathematical_preflight_pass": r0100["preflight_all_pass"] is True,
            "terminal_guard_closed": r0100["terminal_physics_execution_allowed"] is False,
            "ceiling_exact": r0100["terminal_status_ceiling"] == EXPECTED_CEILINGS["0100"],
        }
    }
    for bench in ("0101", "0102", "0103", "0104"):
        item = r_rest["results"][bench]
        per_model[bench] = {
            "mathematical_preflight_pass": item["status"].startswith("PASS_") and all(item["gates"].values()),
            "terminal_guard_closed": item["terminal_physics_execution_allowed"] is False,
            "ceiling_exact": item["terminal_status_ceiling"] == EXPECTED_CEILINGS[bench],
        }
    combined = {
        "0100_preflight_all_pass": r0100["preflight_all_pass"] is True,
        "0101_0104_preflight_all_pass": r_rest["preflight_all_pass"] is True,
        "all_terminal_guards_closed_before_authority": all(
            all(gates.values()) for gates in per_model.values()
        ),
    }
    return per_model, combined


def authority_state() -> dict:
    # These are deliberately based on committed lock files, never on network state.
    # The audit turns authority-ready only after an immutable terminal lock is
    # prospectively committed to the repository.
    locks = {
        "0100_source_profile_lock": ROOT / "research/locks/0100b_source_profile_terminal_lock.json",
        "0101_parameter_lock": ROOT / "research/locks/0101_sterile_parameter_terminal_lock.json",
        "0102_parameter_lock": ROOT / "research/locks/0102_nsi_parameter_terminal_lock.json",
        "0103_parameter_field_lock": ROOT / "research/locks/0103_magnetic_field_terminal_lock.json",
        "0104_parameter_range_lock": ROOT / "research/locks/0104_light_mediator_terminal_lock.json",
    }
    present = {key: path.is_file() for key, path in locks.items()}
    present_count = sum(present.values())
    required_count = len(present)
    return {
        "locks_present": present,
        "locks_present_count": present_count,
        "locks_required_count": required_count,
        "terminal_authority_lock_percent": round(100.0 * present_count / required_count, 1),
        "terminal_known_model_sweep_ready": all(present.values()),
    }


def run_audit() -> dict:
    files = file_gate()
    protocol = protocol_gate()
    per_model, executable = executable_gate()
    authority = authority_state()

    execution_framework_ready = (
        all(files.values())
        and all(protocol.values())
        and all(all(v.values()) for v in per_model.values())
        and executable["0100_preflight_all_pass"]
        and executable["0101_0104_preflight_all_pass"]
    )

    return {
        "audit": "NMIR-KNOWN-MODEL-FUNNEL-READINESS",
        "repository_execution_framework_ready": execution_framework_ready,
        "repository_execution_framework_percent": 100 if execution_framework_ready else 0,
        "files": files,
        "protocol": protocol,
        "per_model": per_model,
        "executable": executable,
        "authority": authority,
        "interpretation": {
            "execution_framework_ready_meaning": "all frozen benchmark slots 0100-0104 have the required repository apparatus and executable mathematical guards",
            "terminal_sweep_ready_meaning": "all externally required terminal authority locks are prospectively committed",
            "terminal_authority_lock_percent_meaning": "fraction of the five prospectively required external authority lock files currently committed; not a probability that the physics model is correct",
            "blocked_is_not_fail": True,
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
