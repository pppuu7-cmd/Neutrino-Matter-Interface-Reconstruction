# 0096 interim 100-m receiver shard audit — NON-TERMINAL

Date: 2026-09-09
Authoritative workflow run: `34319781596`
Authoritative head: `eff5996612f31c093e82a9ae0cdfdb859da8cb9a`
Parent prereg: `research/prereg/0096_v2_g9_betelgeuse_central_support_certification.md`
Frozen contract commit: `5e8048a3d77b504bba6a79a077a1c9e153f8cb19`

**This file is an interim audit only. It is not the 0096 terminal classification.** The final 0096 verdict still requires all 36 primary families, primary aggregation, exact 8193-node sensitivity union for the globally worst primary family, and the authoritative final artifact.

## Shard A — control 0 / receiver 100 m / 190 pc / source radius 100 km

Artifact name: `nmir-v2-g9-0096-primary-0-2-190-100`
Artifact id: `10093894490`
GitHub artifact digest: `sha256:8901d596bc501445735105285cc329445eb26e421e98fe19ca9835c6b047ca06`
Independently downloaded ZIP SHA256: `8901d596bc501445735105285cc329445eb26e421e98fe19ca9835c6b047ca06`
Inner file: `g9_0096_primary_0_2_190_100.json`
Independent inner JSON SHA256: `8736ea7d2c476d55b1e332bfd4588ec395fdd89bc630b13dbd90396e7cdceb36`

Validated provenance / invariants:
- `status = SHARD_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN`
- `head_sha = eff5996612f31c093e82a9ae0cdfdb859da8cb9a`
- `contract = 5e8048a3d77b504bba6a79a077a1c9e153f8cb19`
- `parent_evaluator_blob = 4bedc9431b428292f1b09613f603bea82597f9b5`
- `model_s_blob = e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`
- `receiver_m = 100.0`
- `source_distance_pc = 190.0`
- `source_radius_km = 100.0`
- `grid_count = evaluated_count = 4097`
- `all_ge2 = true`
- `batch_scalar_max_rel = 4.466366117002431e-14`
- `point_control_relative_error = 1.915060916270862e-11`

Numerical scale:
- axis exact `mu = 28521652.82294609`
- minimum `mu_min = 314.2207802786686`
- minimum occurs at frozen endpoint index 4096, `beta = 50 mas`, `d = 869369.8902878346 m`
- exact endpoint `mu = 314.2207802786686`
- threshold margin `mu_min / 2 = 157.1103901393343`

## Shard B — control 1 / receiver 100 m / 222 pc / source radius 100 km

Artifact name: `nmir-v2-g9-0096-primary-1-2-222-100`
Artifact id: `10093866495`
GitHub artifact digest / independently downloaded ZIP SHA256: `492451fc36bdcf522f58d59ea76c724f91ee1398fdecfe760be3f21107ea16ed`
Inner JSON independent SHA256: `d93d14fb4f4221c5fb2e8f61a3323bf02a6edc19ccb120b6449d3cc385776ec9`

Validated values:
- `status = SHARD_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN`
- `receiver_m = 100.0`
- `source_distance_pc = 222.0`
- `source_radius_km = 100.0`
- `grid_count = 4097`
- `all_ge2 = true`
- axis exact `mu = 24004959.335769247`
- `mu_min = 311.70926556996454`
- minimum occurs at endpoint index 4096, `beta = 50 mas`, `d = 873093.1328556284 m`
- exact endpoint `mu = 311.70926556996454`
- threshold margin `mu_min / 2 = 155.85463278498227`

## Interim interpretation
These are the first independently inspected 100-m receiver families from the authoritative 0096 execution. Both retain more than 155x multiplicative margin above the frozen `mu >= 2` threshold across their full 4097-point central-support grids, with the sampled minimum occurring at the 50-mas endpoint.

This substantially reduces concern that receiver-radius scaling alone will destroy the 50-mas support, but it does **not** authorize any of the following:
- a terminal 0096 PASS;
- global monotonicity outside the 50-mas interval;
- repair/reinterpretation of the blocked 0093 topology;
- detector event-rate gain;
- interaction gain;
- deposited-energy gain;
- useful neutrino power.

## State when this audit was written
The authoritative 0096 run remained `in_progress`. At the latest artifact check, 24 of 36 frozen primary-family raw artifacts were present (66.7% of the primary Cartesian family). No primary aggregate, sensitivity authority, or terminal `nmir-v2-g9-0096-authoritative` artifact existed yet.

Exact next authority action remains unchanged: wait for all frozen primary jobs, aggregate all 36, run the exact 8193-node sensitivity union for the globally worst primary family, and independently validate the final artifact before assigning a terminal 0096 classification.
