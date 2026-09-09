# 0096 — v2 G9 Betelgeuse central-support certification

Date: 2026-09-09
Classification: `PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS`

## Frozen authority
- preregistration: `research/prereg/0096_v2_g9_betelgeuse_central_support_certification.md`
- preregistration commit: `5e8048a3d77b504bba6a79a077a1c9e153f8cb19`
- authoritative workflow head: `eff5996612f31c093e82a9ae0cdfdb859da8cb9a`
- authoritative Actions run: `34319781596`
- final job: `102416721251`
- authoritative artifact: `nmir-v2-g9-0096-authoritative`
- artifact ID: `10097881579`
- GitHub artifact digest / independently reproduced downloaded ZIP SHA256: `e75126cfe3d5a2f6ea90feb57d2d7873300c8da06134938c5d7bfd8e3f129ee7`
- inner `g9_0096_result.json` SHA256: `be3b85c526e02447ca903600d9776b1c9241f67c7a29705493d5e81fac4b8299`
- parent ray evaluator blob: `4bedc9431b428292f1b09613f603bea82597f9b5`
- Model S blob: `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`

### Hash correction note
The first immutable-record draft accidentally copied two hashes from an earlier local artifact-handling state (`b91a5117...` ZIP and `423ac94b...` inner JSON). They are superseded by the values above, which were re-derived from artifact ID `10097881579` after run completion. The ZIP SHA256 now exactly matches GitHub's own artifact `digest`, and the inner JSON SHA256 exactly matches the parent hash independently recorded by the successful 0097 workflow when it downloaded the authoritative 0096 artifact. This correction changes no science result, grid, family, status, or threshold.

## Frozen family and grids
The primary scan contained exactly 36 prospectively frozen families:
- 3 inherited observer-distance controls;
- receiver radii 1, 10, 100 m;
- source distances 190 and 222 pc;
- physical neutrino-source radii 21 and 100 km.

Each primary family was evaluated on exactly 4097 linearly spaced radial offsets from the exact axis to the frozen 50-mas endpoint. All 36 primary jobs completed successfully and all 36 primary families satisfied `mu >= 2` at every node.

The primary aggregate then selected the global worst family without manual intervention. The frozen sensitivity stage evaluated exactly the same selected family on an 8193-node grid partitioned into four deterministic chunks whose union is exactly all 8193 nodes. All sensitivity nodes also satisfy `mu >= 2`.

## Terminal numerical result
- global primary minimum: `mu_min = 305.9647832680237`
- global sensitivity minimum: `mu_min = 305.9647832680237`
- threshold: `mu >= 2`
- margin over threshold: about `152.98 x`
- worst family:
  - control index: `2`
  - receiver: `10 m`
  - source distance: `222 pc`
  - source radius: `100 km`
- worst sampled offset: frozen endpoint `50 mas`

The independent terminal-artifact inspection confirmed the primary and sensitivity minima agree and the terminal status is exactly:

`PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS`

The Actions run contained 42 jobs total: 36 primary-family jobs, one primary aggregate, four sensitivity chunks, and one final authority job; all completed successfully.

## Scientific meaning
0096 certifies the prospectively frozen **central 50-mas numerical lens-support region** for the Betelgeuse known-progenitor branch under the inherited Model-S ray evaluator and the frozen finite-source / finite-receiver family.

It does **not**:
- promote the non-monotone global 0093 geometry to a global footprint;
- close the v1 0092b-a2 5–50 MeV full nuclear-response / solar-opacity authority block;
- establish detector event-rate gain, interaction gain, deposited-energy gain, or useful-power gain;
- establish spacecraft engineering feasibility;
- infer a Betelgeuse explosion date or probability.

The ~44-mas optical photospheric diameter of Betelgeuse is not used as the neutrino-source size. The physical neutrino-source controls remain the prospectively frozen 21-km and 100-km radii.

## Consequence
The frozen parent condition for 0097 is satisfied. The v2 chain may proceed to the already-preregistered Betelgeuse line-tracking architecture gate, subject to exact parent provenance and the prospective downstream focal-half-line correction in 0097a.