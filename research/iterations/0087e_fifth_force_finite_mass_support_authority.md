# NMIR iteration 0087e — B-L fifth-force finite-mass support authority

Date: 2026-09-08

## Classification

`BLOCKED_FIFTH_FORCE_FINITE_MASS_SUPPORT_AUTHORITY`

This is a source-authority blocker, not a physical no-go and not evidence that finite-mass fifth-force constraints are absent. The accepted Fayet/MICROSCOPE chain does not expose two source-authorized finite endpoints sufficient to materialize a finite mediator-mass support interval under the frozen no-invented-cutoff contract.

## Prospective authority

Frozen preregistration:
- `research/prereg/0087e_fifth_force_finite_mass_support_authority.md`
- prereg commit: `569bbd37b8e5fc1ee8568712e53ef02a622e07bd`

Frozen target from 0087b:

`6.845530367110015e-6 <= m_V <= 1.4057345497828417 eV`.

Allowed routes were fixed before the result:
1. source-explicit finite mediator-mass interval with two finite positive endpoints;
2. source-explicit finite force-range interval with two finite positive endpoints and authorized range-to-mass conversion;
3. source-explicit Yukawa response for the actual experiment together with an experiment-defined finite range domain sufficient to establish both endpoints.

Earth radius/diameter, orbital altitude, and arbitrary Yukawa suppression thresholds were explicitly forbidden as post-hoc endpoints.

## Exact primary provenance

The gate consumes the already validated 0079 authority ledger `data/fayet_fifth_force_authority_classification_0079.json`, SHA256:

`e3c78305d7474f9d7dbfa4b42903d9a211126d6cbcbb32f8d503a97e0d4d45a3`.

Exact primary source bytes remain:
- Fayet `arXiv:1809.04991v2`: `ed233fa73a149ba9801d442339a2c5fd3b5051c1dc2caa1584a000760fcff29b`;
- companion `arXiv:1712.00856v2`: `e058c6338db1151bf631a2c2c5eb09102cb521327227ff5288570e51744cc03d`.

The hosted audit independently confirmed that these hashes match the validated 0079 ledger.

## Reproducible implementation

- scientific script commit: `2e065e126978bca9778b84709983d2882ff55bd2`
- dedicated regression tests commit: `aafa088ad7361a7fd0d71024e2da1afea30f08a6`
- fail-closed hosted workflow commit/head: `e40d77f51513b3a20db979c961b1b44010be8d13`
- persistent machine ledger commit: `d72baf87b08a42bbc1b195f799e605e751ae0ede`

## Hosted scientific authority

- run: `34184676660`
- job: `101930508258`
- artifact: `10040096596`
- artifact size: `1138 bytes`
- artifact ZIP SHA256: `e390cbad96636b986dec893e6c071b200a0da13aba9242d2298dc2ee769afc5f`
- raw JSON SHA256: `16b32b5846c70d8590888301644f1a8d4f3ae219a89a57892dc8260b2484691d`
- dedicated regression tests: `3 passed in 0.11s`

The raw job log was inspected directly. The Actions artifact ZIP was downloaded independently; its SHA256 matched GitHub's artifact digest, and the extracted JSON independently reproduced the raw JSON SHA256 above. Green workflow status alone was not used as scientific authority.

## Frozen-route result

### Route A — explicit finite mass interval

FAIL TO AUTHORIZE. No accepted primary source provides a pair of finite positive mediator-mass endpoints for the MICROSCOPE B-L constraint.

### Route B — explicit finite force-range interval

FAIL TO AUTHORIZE. No accepted primary source provides a pair of finite positive force-range endpoints sufficient for a finite mass interval.

### Route C — source-explicit Yukawa response plus experiment-defined finite domain

The companion source does contain a Yukawa potential proportional to `exp(-r/lambda_U)/r`, but the validated authority ledger contains no finite-range curve/table and no experiment-defined finite domain with both endpoints. Qualitative references to terrestrial dimensions or satellite altitude therefore cannot be promoted into a cutoff.

Result: no route passes.

## Scientific meaning

The strict long-range/asymptotic 0079/0079a MICROSCOPE/Fayet result remains valid and unchanged. What fails is only the attempted promotion from that asymptote to a reproducible finite-mass support interval.

Therefore fifth-force finite-mass support remains `UNRESOLVED_MASS_SUPPORT_THREAT` for the 0087b low-mass topology target. No finite fifth-force polygon is added, no target overlap is claimed, and no BSM response/enhancement scan is authorized.

## Next funnel gate

Move to the localized Esseili-Kribs BBN tail identified by 0087b: only `1.0 .. 1.4057345497828417 eV`, or `2.7840644564136232%` of the target log-mass width. Before any result-dependent BBN calculation, freeze a separate gate that asks whether source-authorized analytical/tabulated information can resolve that tail without reopening the already blocked 0081a vector-calibration route or borrowing the CMB transform.

## Readiness

`NMIR_READINESS: 98%` — unchanged. 0087e reproducibly localizes another authority blocker but does not add a finite exclusion object or complete the global B-L envelope.
