# 0105a6q5a1 — validated ORNL release-page structure diagnostic

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5A1`
Classification: `PASS_0105A6Q5A1_ORNL_ZENODO_3903810_LINK_STRUCTURALLY_PRESENT_NONDISCOVERY`
Scope: provenance/page-structure diagnostic only; NONDISCOVERY.

## Frozen preregistration and implementation chain

- parent q5a validated record commit: `d7c888741d0c7c807c5cdfa8c6083593ac8a1b47`
- preregistration commit: `f0c211182f71d7b27f3093e15ce29646072f5582`
- implementation commit: `b292979cfe9fe70bea7ed1449b5d59867b0e49c5`
- guard commit: `a9839c1e8f38ac6d2993b3b50a30b7d975916958`
- execution head: `e195e6c460e850d748b6abfc2cb81be0cb6dbbe7`

## Hosted validation

- run: `34547901624`
- job: `103104375353`
- artifact: `10179689972`, `nmir-v2-0105a6q5a1-ornl-release-page-structure`
- dedicated guards: `5 passed`
- provider artifact ZIP SHA256: `0ee3a407c1ee732ed3ed4cb5e552ab10a3adf90d0629d7ccbd88771e31c09172`
- independently downloaded ZIP SHA256: `0ee3a407c1ee732ed3ed4cb5e552ab10a3adf90d0629d7ccbd88771e31c09172`
- independent inner `result.json` SHA256: `406dea5479695c68ee82caf358d3aef43e54412538ebf00d1f5fb9d193237640`

Green Actions success was not treated as scientific PASS; raw result and artifact bytes were checked against the frozen q5a1 gate.

## Result

The frozen ORNL endpoint returned HTTP 200 with 76,265 bytes and payload SHA256 `7ed4bcc3f99d494b134418d060a122c8c7531c7c3b738350bcb09ea715b804f9`. The page contained 28 HTML anchors. Exactly one anchor explicitly targets the frozen Zenodo record:

- literal href: `https://zenodo.org/record/3903810#.X1GgHS2z3Ra`
- resolved host: `zenodo.org`
- resolved path: `/record/3903810`
- visible anchor text: `https://zenodo.org/record/3903810#.XvFaFOd7nIV`

Thus `zenodo_3903810_anchor_count=1`, satisfying the prospectively frozen q5a1 PASS condition.

This explains q5a without rewriting it: q5a required the same anchor's visible text to include both `Data release` and `argon`, which it does not. Therefore q5a remains historically `BLOCKED_0105A6Q5A_ORNL_RELEASE_ROUTE_FAILURE`, while q5a1 independently establishes that the first-party ORNL page structurally links to exact Zenodo record 3903810.

## Hard guards retained

No discovered link was followed. `scientific_release_content_inspected=false`; `pseudo_data_generated=false`; `likelihood_evaluated=false`; `observed_bsm_residual_inspected=false`.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next allowed action

q5a1 PASS authorizes only a separately prospectively preregistered repaired provenance-binding gate using structural href identity for the ORNL -> Zenodo edge while retaining the exact 0105a3, Zenodo and arXiv identities. It does not authorize q5b content inspection or any BSM/null/systematic execution.