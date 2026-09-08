# Iteration 0093 — G9 CCSN alignment-footprint topology BLOCKED

Date: 2026-09-09
Classification: `BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY`

## Frozen authority
- preregistration: `research/prereg/0093_g9_ccsn_alignment_footprint_expansion.md`
- prereg commit: `ffaa7706bf335b301833fe49754297b804cf713a`
- execution head: `66eb5bcfcc9abf9240cb0b5716665143fbbab8ff`
- workflow: `.github/workflows/0093-g9-ccsn-alignment-footprint.yml`
- run: `34279135188`
- aggregate job: `102244800175`
- authoritative aggregate artifact: `10077508208`

The frozen 0093 protocol evaluated 18 families = 3 observer controls x 3 receiver radii x 2 frozen CCSN source radii, each on 257 prospectively fixed logarithmic offsets from 100 m to the map-derived strict no-overlap ceiling, with threshold-straddling brackets refined by exactly 32 geometric-midpoint bisections.

## Raw Actions / artifact validation
All nine science matrix jobs completed successfully and the aggregate completed successfully. The aggregate raw log explicitly reports `BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY`.

The aggregate job downloaded all nine shard artifacts and verified their GitHub Actions SHA256 digests before aggregation. The authoritative aggregate was then independently downloaded outside the Actions job and hashed:
- artifact ZIP SHA256: `1bef56077626433de111870e8c41c6a5460f8c6cc7d332b58171ded2015c73e6`
- inner `g9_0093_result.json` SHA256: `9a5aea9e1d3fd00a16781870e93ee95956a3886ed47edb3a244155ce0dd23a5b`

Both hashes match the upload/raw-job evidence. The artifact head is exactly `66eb5bcfcc9abf9240cb0b5716665143fbbab8ff`.

## Scientific result
The calculation is numerically valid, but the frozen sampled topology is not single-crossing. Aggregate facts:
- `family_count = 18`
- `shard_count = 9`
- total sampled re-entry count = `39`
- minimum sampled contiguous-prefix last-survivor offset = `82560159.41660324 m`
- maximum sampled contiguous-prefix last-survivor offset = `553635628.884269 m`
- conservative first refined threshold crossing lower endpoint = `85899345.85116383 m`
- its corresponding angular offset = `2.366489184413326e-5 rad = 4.8812343310886375 arcsec`
- widest first-crossing lower endpoint in the frozen families = `580464275.2321923 m`, corresponding to `33.38419478963213 arcsec`
- map-derived no-overlap ceilings are about `6.65e8 m`; the aggregate no-overlap checks reached `mu=1` as required.

The conservative family itself has `7` sampled re-entries and `15` threshold straddles. Across the 18 families, repeated `mu<2 -> mu>=2` re-entry occurs 39 times. Under the prospectively frozen taxonomy, this is exactly the condition for `BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY` rather than PASS.

## Interpretation
This is not a physical no-go and does not erase the 0090f finite-source PASS. It means the 0093 finite-grid scan discovered multi-band offset topology too complex to summarize as one globally valid alignment radius under its frozen crossing protocol.

The first crossing, contiguous-prefix values and later survivor islands are descriptive authority only. They must not be promoted post hoc to a theorem that all offsets below one radius survive, nor may the grid/order be densified after seeing the result under the same gate.

For the mandatory NMIR-v1 post-0093 actionability audit, the topology block must be propagated conservatively. A future actionability gate may use the fixed map-derived no-overlap ceiling as a generous absolute support bound, and/or explicitly carry the first-contiguous-region uncertainty, but may not reinterpret 0093 as `PASS_G9_CCSN_ALIGNMENT_FOOTPRINT_EXPANDED`.

0092b-a2 remains independently terminally external-authority blocked for v1. No detector/material/BSM gain or neutrino-supplied-power multiplication is authorized.
