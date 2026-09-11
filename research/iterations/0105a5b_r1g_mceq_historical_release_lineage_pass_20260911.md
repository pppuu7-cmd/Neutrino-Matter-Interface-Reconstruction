# 0105a5b R1g — MCEq historical release lineage

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Classification: `PASS_0105A5B_R1G_MCEQ_HISTORICAL_RELEASE_LINEAGE_BYTE_LOCKED_NONDISCOVERY`

## Frozen scope
R1g was prospectively defined after R1f PASS. It queried official GitHub commit metadata only for the complete frozen set of 11 stable, non-prerelease MCEq release tags predating the IceCube publication boundary. It did not inspect README/source/blob/tree/archive payloads and did not execute any DeepCore 3nu likelihood or observed-residual calculation.

## Authoritative execution
- prereg commit: `85e8641fc1dcdc1e498313cc99f81dc47521fef5`
- implementation commit: `d95218c78f5fbfecb1a4c138fb848279756b539e`
- guards commit: `9038f7cce149bfc8d668af3afcc774e848a644ce`
- execution head: `c0f1c1a55b07bfb128098d9182f178896bd61a75`
- run/job/artifact: `34571400149/103174092287/10187896928`
- artifact name: `deepcore-r1g-mceq-historical-release-lineage`
- provider artifact digest: `sha256:3b3e8acc74727673ac4260011a8c49cdbe6a4177bdb87149e6493864b3be6e46`
- connector-downloaded/repacked ZIP SHA256: `7484388157d81899974739e7e1307d6174931fa7f357ee0b07ffd5befe2d7ade`
- inner `result.json` SHA256: `ba5eb82cea3d0c3c2200735c06567ea9d92ed321143c82120848696db8d0c2df`

The provider digest and connector-downloaded ZIP SHA256 are intentionally recorded as distinct values because the downloaded bundle was repackaged by the connector; no equality claim is made between those two container hashes. The inner result hash is independently computed from the extracted `result.json`.

## Result
All 11 preregistered historical stable MCEq tags resolved through official provider metadata to exact 40-hex commit SHAs. The frozen release set was not ranked, pruned, or selected after inspection.

This is an authority/provenance NONDISCOVERY PASS only. It establishes an immutable historical candidate lineage; it does **not** establish which MCEq release/commit IceCube used, does not define Barr nuisance transformations, does not close DIS/CSMS implementation authority, and does not authorize standalone DeepCore standard-3nu reproduction.

## Authorization boundary
R1d remains `BLOCKED_0105A5B_R1D_EXTERNAL_COMPUTATIONAL_AUTHORITY_INCOMPLETE`.

The next dependent MCEq step, if undertaken, must be separately preregistered before target inspection and may use only a provenance-qualified IceCube/provider authority corpus to distinguish the frozen 11-candidate lineage. It must not choose a version by comparing source behavior or by optimizing agreement with DeepCore outputs. No source/tree/blob/archive inspection is authorized by R1g alone.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
