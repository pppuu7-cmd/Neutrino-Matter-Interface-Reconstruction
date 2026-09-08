# NMIR iteration 0087d — COHERENT B-L mass-support-only authority

Date: 2026-09-08

## Classification

`BLOCKED_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY`

This is a scoped source-authority blocker only. It does not weaken 0074c, does not evaluate a B-L likelihood, and does not imply that COHERENT is mass-disjoint from the 0087b low-mass topology candidate.

## Prospective authority

Frozen preregistration:
- `research/prereg/0087d_coherent_mass_support_only_authority.md`
- prereg commit: `02032a0823180ae029a5a641b48a496252ed812d`
- exact source: Cadeddu et al., arXiv `2008.05022v3`
- exact fetched archive SHA256: `389a2f651d3e1ed158ecac19a08ca956972e61b414386306a53d27538d29c943`
- frozen target: `6.845530367110015e-6 <= m_V <= 1.4057345497828417 eV`.

## Parser-conformance history

The initial/r1/r2 paths are not authoritative science. r1 repaired standard starred `includegraphics`, but r2 still admitted event-rate figures merely because their captions contained B-L and a benchmark mediator mass. That violated the original Route-B requirement for an explicit coupling-versus-mediator-mass constraint figure.

- r2 run/job: `34181665826/101921828232`
- r2 artifact: `10039115681`
- independently checked r2 ZIP SHA256: `1d4946a9195366aa4f5639c9c283d141455c2684a82ad3b2f40a3173aa1f7819`
- independently checked r2 JSON SHA256: `179c4a11b4b834fbd4128ac2b9441c905579d6c260fcea3db8791a9c8bffd901`
- r2 reclassification: `INFRASTRUCTURE_FAIL_ROUTE_B_CONSTRAINT_SEMANTIC_CONFORMANCE`.

The r3 amendment was frozen before the r3 hosted result:
- amendment: `research/amendments/0087d_route_b_constraint_semantic_conformance_r3.md`
- amendment commit: `5db8546940730d7a657cb5de45594264266e9862`
- implementation commit: `d239d379480523d30b5fc02875af59750d941766`
- test commit: `6391ad7e431464db380b2b5278dc28deaa8785c0`
- workflow commit/head: `ee12988191a85f576700c3944a330518dab62306`.

r3 changed only the Route-B semantic predicate to enforce the original preregistered requirement: literal B-minus-L plus explicit exclusion/constraint/limit semantics in a coupling-versus-mediator-mass plane. No scientific threshold, source bytes, tick logic, frame tolerance, target interval, or consequence changed.

## Authoritative hosted r3

- workflow: `.github/workflows/0087d-r3-coherent-mass-support-only.yml`
- run/job: `34181815894/101922266159`
- artifact: `10039164892`
- artifact ZIP SHA256 from GitHub and independent download: `d3a85d1157563d301d6f00c8910a86962071fbd71c590ef9c7cdc2622b43089d`
- independently extracted raw JSON SHA256: `17e812f4f3f41849e2117b0af6089bace833235f7287ef003d96ed97e4cc25a2`
- parser/regression tests: `10 passed`.

The workflow conclusion is failure only because the frozen scientific audit exits nonzero on BLOCKED; artifact upload completed successfully.

## Route A — explicit source-text finite B-L mass interval

`passed=false`

- unique explicit finite intervals: `0`
- reason: `no_unique_explicit_BL_mass_interval`.

No finite mediator-mass support interval is therefore authorized from source text.

## Route B — exact source-native B-L constraint figures

After r3 conformance the candidate set contains only the two assets belonging to source figure `fig:B-L_limits`:

1. `Coherent_Results_B-L.pdf`
   - SHA256: `46c75e3fa73a4cf6ce11060c021dcb68c92a2538ddd1cd16480f25fc234231a4`
   - vector-native; image XObjects: `0`
   - mediator-mass axis identity: PASS
   - x-axis unit: `MeV`
   - accepted source-native major x ticks: `2` (`10^-5`, `10^4`)
   - frozen minimum: `>=3`
   - result: `fewer_than_3_source_native_x_ticks`.

2. `Comparison_B-L.pdf`
   - SHA256: `5b944eedd5cdbde97387dadd8ef1285c14916670779e9fca958e68743cdb8945`
   - vector-native; image XObjects: `0`
   - mediator-mass axis identity: PASS
   - x-axis unit: `GeV`
   - accepted source-native major x ticks: `1` (`10^-6`)
   - frozen minimum: `>=3`
   - result: `fewer_than_3_source_native_x_ticks`.

Thus no Route-B x fit or scientific plot-frame endpoint interval is authorized. Missing signs/exponents are not synthesized from vector strokes or visual inspection.

## Consequence

`certified_mass_support_eV = null`; `threat_result = null`.

COHERENT remains an unresolved mass-support threat to the 0087b candidate. This blocker is independent of and does not reopen the older combined-likelihood numerical-benchmark blocker 0074c.

## Guard

No B-L likelihood. No combined-likelihood validation claim. No y-axis calibration. No curve/path/color/legend identity. No raster/OCR/manual digitization. No visual exponent/sign recovery. No global B-L allowed-region claim. No BSM response/enhancement scan.

## Next gate

The unresolved finite-support threats left by 0087b after 0087c and 0087d are Cerdeño, COHERENT and finite-mass fifth-force, while BBN is a separately localized `1..1.4057 eV` overlap threat. Cerdeño and COHERENT are now source-authority BLOCKED under the no-manual contract. The next highest-value executable class-level question is therefore a prospectively frozen finite-mass fifth-force/Yukawa source-authority audit: determine whether primary fifth-force/EP sources themselves authorize a finite mediator-mass/range applicability interval without extrapolating the strict long-range 0079/0079a asymptote.
