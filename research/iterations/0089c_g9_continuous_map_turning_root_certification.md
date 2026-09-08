# NMIR iteration 0089c — G9 continuous-map turning-root certification

Date: 2026-09-08
Classification: **PASS_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION**

## Prospective authority

Scientific contract: `research/prereg/0089c_g9_continuous_map_turning_root_certification.md`, frozen before result-dependent root inspection in commit `1f96b318b437d6a5aecf815ef829ef09a8adc7e6`; bulk-audit amendment `d2840a3974c2e4f6b530fa703410663a87dd0e50` changed implementation/audit coverage only and did not relax scientific criteria.

Inherited continuous projection authority: iteration 0089b, pinned Model-S Git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`.

Scope is turning-root certification only. No accepted area, radial kernel, finite-source convolution, persistent-source utility or gain is authorized by this PASS.

## Hosted scientific authority

- run/job: `34214036230 / 102021451956`
- scientific head: `92f58076f32eb9a977c8fc1d1ccea9b171214527`
- artifact: `10051169835`, `nmir-g9-0089c-continuous-map-turning-roots`, 1226 zipped bytes
- artifact ZIP SHA256: `3897ec7ff193b133ebff195f181472da27b3ff098129855527d1debd5e3684d2`
- inner `g9_0089c_result.json` SHA256: `097f0cc4a2aa2ff900d5bf1e47b2f36da088bbb567fb7d9bc325d5ea50077f8d`
- dedicated tests: `3 passed in 0.14s`

The raw Actions job log was inspected directly. The artifact ZIP was downloaded independently, its SHA256 matched GitHub artifact metadata exactly, and the extracted JSON was hashed independently. The green workflow status was not used as scientific evidence by itself. A failing baseline CI run on the same head is classified separately as infrastructure and does not alter this scientific artifact.

## Raw scientific result

The continuous piecewise-linear projection/derivative cross-check passed at 79 points:
- maximum derivative symmetric relative discrepancy: `3.227517559539168e-14`;
- maximum focal symmetric relative discrepancy: `5.486245728015033e-16`;
- maximum projected-mass symmetric relative discrepancy: `2.2200669216010985e-16`.

For every control, Q32 and Q64 found exactly one turning root; all 2400 interior source-knot stress checks passed; 153663 original-map finite-difference midpoint checks per control passed, with exactly one midpoint skipped only inside the already certified turning-root bracket.

### Control b0/Rsun = 0.020
- `z = 23.97365833326344 AU`
- turning root `x = 0.01150432239489928`
- certified bracket `[0.011502268749999999, 0.011504674999999999]`
- orientation `+1`
- original-map FD replica root absolute offsets at denominators 4096/8192/16384: `1.8358231601567354e-11`, `5.507469133525511e-11`, `9.179115453838982e-11`
- generating-root recovery: `x0 = 0.019999999999963623`, absolute error `3.6377151291233645e-14`.

### Control b0/Rsun = 0.024
- `z = 24.07633010302372 AU`
- turning root `x = 0.013783440937996098`
- certified bracket `[0.013781625, 0.0137844796875]`
- orientation `+1`
- FD replica root absolute offsets: `2.177953650761566e-11`, `2.177953650761566e-11`, `1.0889768600752525e-10`
- generating-root recovery: `x0 = 0.023999999999956344`, absolute error `4.365605099643233e-14`.

### Control b0/Rsun = 0.030
- `z = 24.263861625478885 AU`
- turning root `x = 0.01718034337813724`
- certified bracket `[0.0171768859375, 0.0171804375]`
- orientation `+1`
- FD replica root absolute offsets: `1.3548138305674584e-11`, `1.3548138305674584e-11`, `1.3548138305674584e-11`
- generating-root recovery: `x0 = 0.029999999999972715`, absolute error `2.7283730830163222e-14`.

## Interpretation

This closes the numerical uncertainty that blocked 0076/0077 at the turning-point level: the 0089b continuous Model-S map now has reproducibly certified radial turning roots for all three frozen observer controls. It does **not** imply that accepted preimage areas are correct, that a global multi-image radial kernel passes, or that a persistent source yields useful focusing.

The next calculation must be separately preregistered and must use these certified turning roots to partition the signed continuous map into monotone branches before solving `y=0,+r,-r`. The inherited 0077 area/containment/refinement criteria remain at 0.5% or stronger; no result-selected grid repair is allowed.

NMIR_READINESS remains 98% because this is a reproducible scientific PASS but does not yet establish the global radial kernel or persistent-source utility.
