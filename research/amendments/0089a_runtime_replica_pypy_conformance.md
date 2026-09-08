# NMIR amendment 0089a — runtime replica / PyPy conformance

Date frozen: 2026-09-08
Parent prereg: `research/prereg/0089a_g9_frozen_map_turning_root_certification.md`, frozen scientific contract commit `e350cd19beec7c9d3ca9f43a439337ef9e88a099`.

## Reason
The first hosted CPython 3.11 execution of 0089a entered the full frozen Model-S audit after all dedicated regression tests passed, but the audit is computationally heavy because R4/R5 intentionally evaluate the original authoritative finite trapezoidal map at every preregistered confirmation/stress point. Before any 0089a Model-S root positions, derivative signs, boundary turns, or scientific classification were observed, freeze a runtime-only replica so the same source can be executed under PyPy without changing any scientific criterion.

## Frozen conformance contract
- Use the exact repository source files and exact scientific preregistration already frozen for 0089a.
- Do not change Q32, Q64, boundary offsets, `tau_D`, root widths, finite-difference step scales, tolerances, observer controls, Model-S bytes, signed-map implementation, derivative implementation, R1-R5 logic, generating controls, or classification taxonomy.
- The replica may change only the Python runtime from CPython 3.11 to a hosted PyPy 3.x runtime supported by `actions/setup-python`.
- Run the same dedicated test file and the same `scripts/g9_frozen_map_root_cert_0089a.py` entry point.
- Upload the same machine-readable JSON under a separately named artifact.

## Prospective interpretation
1. A terminal artifact from either runtime is not accepted from workflow colour alone; raw JSON and logs must be inspected.
2. If both runtimes terminate scientifically, their status, Model-S hash, root counts/positions/orientations, boundary-turn sets and frozen control outcomes must agree within the already frozen 0089a numerical tolerances. Any unexplained runtime-dependent scientific discrepancy is `BLOCKED_G9_FROZEN_MAP_RUNTIME_CONFORMANCE` and neither result is promoted.
3. If one runtime terminates scientifically and the other terminates only by runner timeout/capacity before producing a scientific JSON, the completed runtime may be authoritative after ordinary artifact/log verification; timeout/capacity is infrastructure-only and cannot override the scientific result.
4. If both terminate only by runtime/capacity failure, 0089a remains infrastructure-incomplete; no scientific BLOCKED/FAIL/PASS is inferred.
5. No result-selected scientific tuning is permitted after either runtime output is seen.

This amendment changes execution capacity only. It does not authorize kernel/area/one-ring/finite-source/persistent-source/BSM work.