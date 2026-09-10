# 0105a6 — COHERENT standalone SM/null semantics authority inventory

Date: 2026-09-10
Gate: `NMIR-V2-0105A6`
Stage: authority/provenance only

## Purpose

Determine prospectively whether the already byte-locked official COHERENT CsI and Ar releases contain enough collaboration-authored information to define a later standalone Standard-Model CEvNS/null reproduction without inventing bins, detector response, background model, nuisance conventions, normalizations, statistic, or thresholds.

This gate is upstream of every numerical SM/null reproduction and upstream of every observed BSM/model-agnostic residual.

## Frozen provenance

Authority begins with the official COHERENT/ORNL data-release route and the exact releases already closed by 0105a3:

- CsI Zenodo record `1228631`, DOI `10.5281/zenodo.1228631`, frozen version `1.0`, 13 files;
- Ar Zenodo record `3903810`, DOI `10.5281/zenodo.3903810`, frozen version `1.0`, 24 files;
- 0105a3 successful byte-lock run/attempt/job `34418207408/3/102834981270`, artifact `10147580844`;
- 0105a3 artifact ZIP SHA256 `b4d93c5e121ddbf503f9dd837fff1c356fd704342d48c5d243213ac599e26da4`;
- normalized 0105a3 manifest SHA256 `5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`.

No calibration-only dataset or secondary phenomenology reconstruction may replace either CEvNS event release. Official collaboration-authored companion/code material may be admitted only if provenance to the corresponding release is explicit and is recorded byte-for-byte or commit-for-commit before use.

## Frozen Stage-A scope

Stage A is an evidence inventory only. It may retrieve and hash the following already byte-locked release-side authority files and extract text for inspection:

### CsI
- `README` — SHA256 `978ab4a7e7b01a463dd7e9d4e8938573ad736b78447db79717b5d5b57922f097`;
- `coherent_parameters.yaml` — SHA256 `daa4f3feaeb5499cb1d876f8ea39f3cfd571f998a6ab92e9cdf552afc78b67e8`;
- `coherentCollaboration_dataReleaseCompanion_april2018.pdf` — SHA256 `dd0bc860c53712cd0ebc17ce0ffdb8b88f62f7b64dbdac6389d79782a18556c1`.

### Ar
- `LArParametersAnlA.yaml` — SHA256 `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`;
- `CENNS10DataReleaseCompanion.pdf` — SHA256 `ecfef10e2cb768f0d781b22e712b205fe2d56e5f8702a6054de80afddb1bc3dd`;
- `readYAMLParameters.py` — SHA256 `3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6`;
- `PlotExtractedData.C` — SHA256 `c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f`.

Stage A may also record the exact official ORNL data-release landing-page URL as provenance, but web-page text is not allowed to override byte-locked release content.

## Evidence fields to inventory

Without fitting or inspecting any BSM residual, record literal evidence relevant to these categories separately for CsI and Ar:

1. observable definition and analysis binning;
2. SM CEvNS signal construction or supplied CEvNS template semantics;
3. detector response/efficiency/quenching or energy-scale transformation required by the published analysis;
4. beam-related and steady-state/background components used by the published analysis;
5. nuisance parameters, prior widths/ranges and correlations/couplings where applicable;
6. normalization/exposure/flux quantities needed for the standalone SM expectation;
7. exact test statistic or likelihood form used for the published null/SM benchmark;
8. at least one collaboration-published numerical benchmark or likelihood behavior against which a later reproduction can be prospectively tolerance-tested.

Stage A must distinguish `literal release evidence`, `explicitly referenced collaboration authority`, and `not found`. It must not infer missing conventions from common practice.

## Frozen Stage-A classifications

- `PASS_0105A6_STAGE_A_AUTHORITY_INVENTORY_NONDISCOVERY`: every frozen authority file is fetched from the exact release, SHA256 matches 0105a3, text extraction succeeds where technically applicable, and a raw evidence inventory is emitted. This PASS means only that the inventory execution is reproducible; it does **not** mean that the likelihood authority is complete.
- `BLOCKED_0105A6_STAGE_A_AUTHORITY_TRANSPORT_OR_PARSE`: an exact frozen authority file cannot be retrieved/verified or its required text cannot be extracted after bounded retries. This is authority/transport BLOCKED, not scientific FAIL.
- `INFRASTRUCTURE_FAIL_0105A6_STAGE_A`: runner/dependency/runtime failure before the frozen evidence inventory can execute.

Completeness of the likelihood contract is classified only after raw Stage-A artifact inspection against the eight frozen evidence fields. Missing covariance/nuisance/statistic/benchmark authority must yield a later `BLOCKED`, never a hand-built replacement.

## Prohibited operations

Stage A and its classification must not:

- compute an observed-minus-SM residual;
- select bins after viewing such a residual;
- fit NSI, magnetic, light-mediator or any other BSM family;
- use generic Wilks thresholds;
- tune nuisance conventions or numerical tolerances from observed behavior;
- combine CsI and Ar significance;
- treat 0074a/0074b response PASSes as a substitute for this standalone null-authority audit.

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%` throughout 0105a6.

## Exact next step after Stage A

Consume the hosted Stage-A log and artifact, independently verify artifact and inner-file SHA256 values, then classify authority completeness against the eight frozen fields. Only a complete authority classification may permit a separate preregistered standalone SM/null numerical reproduction gate with exact formulas, units, nuisance treatment and numerical tolerances frozen before execution.