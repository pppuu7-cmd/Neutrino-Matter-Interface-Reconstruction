# Iteration 0090b-r2 — endpoint-regularized radial measure scientifically BLOCKED

Date: 2026-09-08
Parent prereg: `research/prereg/0090b_g9_endpoint_regularized_radial_measure_authority.md`, frozen commit `c46110eecf6fae9719d37f8f3a378206c2706324`.
Preflight-scope amendment: `research/prereg/0090b_amendment_preflight_scope.md`, frozen commit `350ed2cb6da6485f230e429c0d35b18938d64e56`.
Execution head: `cf9904f7a3c65601d13982c2e76b9cfd9fcd51f4`.
Run: `34265645704`.
Job: `102194200480`.
Artifact: `10071689978` (`nmir-g9-0090b-endpoint-regularized-radial-measure`).

## Classification
`BLOCKED_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE`.

Reason from the authoritative payload:
`endpoint-regularized normalization exceeds frozen threshold: external_d_over_s=1.1`.

This is a scientific numerical BLOCKED result under the prospectively frozen 0090b H1/H2 criteria. It is not an infrastructure failure, not a source-geometry scientific failure, and not a physical no-survivor result.

## Hosted evidence
The amended preflight completed successfully: `4 passed`.
The unchanged authority evaluator then executed and wrote the scientific payload with contract `c46110eecf6fae9719d37f8f3a378206c2706324` on exact head `cf9904f7a3c65601d13982c2e76b9cfd9fcd51f4`.

Frozen scientific settings were unchanged from the parent preregistration:
- transformed coordinate `u(t)=sqrt(d^2+s^2-2*d*s*cos(t))`;
- fixed Gauss-Legendre replicas L/H = `32/64` in `t`;
- non-centred normalization tolerance `2e-10` for both replicas;
- L/H agreement tolerance `2e-10`;
- centred tolerance `2e-14`;
- scale-invariance tolerance `2e-12`;
- fixed analytic controls and all 90 physical source geometries.

The evaluator stopped at the prospectively fixed external analytic control `s=1 cm`, `d/s=1.1`. No order, tolerance, tuple, interval or source geometry was changed after inspection.

## Artifact integrity
Actions upload digest / independently downloaded ZIP SHA256:
`9c2ccebcdf24dd65780788ec39e1bda3ad6a8f251ee9a85acde72f322ce120d7`.

Inner `g9_0090b_result.json` SHA256 from the job log / independent extraction:
`d442cea592cb5028374adf373e05ef40427fb8fb8cdea0a3a24c59b0a58dc04d`.

Independent extraction reproduces the exact four-field authority payload:
- `status = BLOCKED_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE`;
- `reason = endpoint-regularized normalization exceeds frozen threshold: external_d_over_s=1.1`;
- `contract = c46110eecf6fae9719d37f8f3a378206c2706324`;
- `head_sha = cf9904f7a3c65601d13982c2e76b9cfd9fcd51f4`.

## Interpretation
0090b answers its narrow authority question negatively: the fixed endpoint-regularized `t` formulation with the preregistered L/H orders cannot certify the exact displaced-disk radial measure to the frozen tolerance over its complete fixed control set.

0090b does **not** test a lens accepted area, receiver convolution, `mu_real`, a `mu>=2` survivor, named-source realizability, duty cycle, detector response or BSM enhancement. Therefore no physical G9 exclusion follows from this result.

The parent preregistration explicitly forbids post-result order escalation. 0090b is immutable and must not be rescued by increasing 32/64 or relaxing `2e-10`.

## Next action
Move to a mathematically independent, prospectively frozen source-coordinate formulation whose uniform-disk probability measure is normalized by construction rather than by a separate displaced-radius quadrature. Any later lens-convolution computation must remain a separate preregistered gate and may not promote 0090/0090a/0090b retroactively. Full 1350-point scanning remains forbidden. BSM response/enhancement remains LOCKED.
