# NMIR iteration 0087c — Cerdeño mass-support-only authority

Date: 2026-09-08

## Classification

`BLOCKED_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY`

The Cerdeño stellar/SN transport family remains an unresolved mass-support threat to the robust 0087b low-mass topology candidate. This is an authority limitation, not a scientific exclusion or refutation.

## Prospective authority

- preregistration: `research/prereg/0087c_cerdeno_mass_support_only_authority.md`
- scientific question was frozen before source-derived result inspection: certify only finite mediator-mass support, with no y-axis calibration, curve/color/path/legend identity, raster/OCR/manual reading, or visual sign recovery.

Primary bytes:
- Cerdeño et al., arXiv `2106.11660v3`
- archive SHA256: `f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d`
- exact source-native asset: `Figures/BL_constraints.pdf`
- asset SHA256: `6557571159bd7d279e9b78e026c79c2974fd487db86dcf3f60b566e54318d07f`

## Parser-conformance amendment

The first hosted run stopped in regression testing before any source audit because the parser rejected standard positive exponent syntax `10^2`. This was classified as infrastructure/parser conformance, not science.

- amendment: `research/amendments/0087c_positive_exponent_parser_conformance.md`
- amendment commit: `23ebd6f84fb2d1063d47a431ce6c26392eb7edb2`
- r1 wrapper: `scripts/audit_cerdeno_mass_support_only_0087c_r1.py`
- wrapper commit: `cd580ca79d0d061028762c8e6120dcee865ab12c`

The repair only accepts source-native positive caret/superscript exponents and digits-only raised split exponents while continuing to reject ordinary `102` / `10 2`; it never synthesizes a missing minus sign. Scientific thresholds and consequences were unchanged.

## Authoritative hosted r1

- workflow: `.github/workflows/0087c-r1-cerdeno-mass-support-only.yml`
- head SHA: `65a4e75f13edd1aaff8ff5bf1880e721fbbad5a7`
- run: `34180495212`
- job: `101918439098`
- workflow conclusion: `failure` because the frozen scientific audit exits nonzero on BLOCKED; the artifact upload succeeded
- artifact: `10038724004`
- artifact ZIP SHA256: `1425c12db24d2a7c49d58c26ff43fa991de66b57948c6040a3b2d3ddbf105af7`
- raw JSON SHA256: `c322149758734053288b1c1de959c460d3cedd2544b5b158d2e4484b1daeab61`
- parser-conformance regression tests: PASS

## Route A — explicit source text

`passed=false`

- candidate explicit same-unit finite interval hits: `0`
- reason: `no_unique_simple_explicit_same_unit_interval`

No finite B-L mediator-mass support was promoted from TeX source text.

## Route B — source-native x-axis/frame only

The exact PDF remains source-native vector material:
- page size: `540 x 396` PDF points;
- text spans: `44`;
- image XObjects: `0`;
- mediator mass-axis identity: PASS;
- unique bottom-axis unit: `GeV`, source span `[GeV]` centered at x=`286.4910583496094`, y=`372.5050048828125`.

However, under the preregistered no-sign-synthesis parser only one signed major x tick was recoverable:
- exponent `0`, source-native fragments `['10','0']`, x center `447.4720001220703`.

Thus:
- accepted x tick count: `1`;
- frozen minimum: `>=3` signed major ticks spanning `>=2` decades;
- Route B reason: `fewer_than_3_signed_x_ticks`.

No x fit, frame-endpoint interval, or mass support is therefore authorized.

## Consequence for the 0087b candidate

The robust 0087b target remains:

`6.845530367110015e-6 <= m_V <= 1.4057345497828417 eV`.

Cerdeño receives no mass-disjointness clearance because its finite mass support is unresolved. No threat overlap or separation number is invented.

## Interpretation

0087c narrows the methodological uncertainty: the obstacle is not mediator-axis identity or units, but insufficient source-native signed major-tick text under the no-raster/no-manual contract. The retired 0082b provisional anchor inventory is not promoted.

Further attempts to reconstruct this particular PDF x-axis by visual sign recovery would violate the preregistered authority standard and are not a productive next step.

## Guard

No y-axis calibration. No curve/path/color/legend identity. No excluded-side assignment. No raster/OCR/manual sign recovery. No provisional-0082b endpoint import. No global B-L allowed-region claim. No BSM response/enhancement scan.

## Next gate

Move to COHERENT mass-support/actionability using primary machine-readable likelihood/release assets rather than figure digitization. The immediate question is whether the public COHERENT resources or primary source text define a finite B-L mediator-mass scan/support sufficient to classify overlap with the 0087b low-mass target without constructing a blocked global contour.
