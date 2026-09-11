# 0105a5b R1f — MCEq official repository metadata preflight result

Date: 2026-09-11
Scope: NMIR v2 only. NMIR v1 remains frozen at `NMIR_READINESS: 100%`.

## Classification

`PASS_0105A5B_R1F_MCEQ_REPOSITORY_METADATA_PINNABLE_NONDISCOVERY`

This is metadata/provenance NONDISCOVERY PASS only. It does not close R1d and does not authorize standard-3nu reproduction.

## Hosted provenance

- prereg `e03be43919e6b4d0883b4b41042aa4dfa9ab968d`
- implementation `e85b91943174349122669b87e02913f521c977af`
- guards `1d230b1b147381a57b60583f320cb08575f5b978`
- execution `b4d08f8721a62a284efccd471f613fa77b3b9338`
- run/job/artifact `34571151184/103173333848/10187807256`
- provider artifact digest and independent ZIP SHA256 `b2a64662ffd778b313558a857ce51806622f6a13e8bcb60137180619e1ed4339`
- independent inner `result.json` SHA256 `7ccaf2a0ea0428eb538317ba927ad4e66d396c5d8ffe6e1f4ccd83364cebedc9`
- canonical pre-self-field result SHA256 `d505482d7fadcdcca94b32c2559c117524ff617587c710ce32580cff2ee0b873`

All exact frozen GitHub REST metadata endpoints returned HTTP 200 JSON. Repository identity is exactly `mceq-project/MCEq`, owner `mceq-project`, archived=false. No README, source file, tree/blob, archive, documentation content, scientific output or nuisance response was fetched.

Response byte locks:
- repository metadata: 6301 bytes, SHA256 `4c1426d51c77f34fe66a359ccd01b82daefdb5a844ab15422ea48cf8df31b94c`;
- releases metadata: 53704 bytes, SHA256 `1b11ee403d0e0d17b98dcd03a9ed887b0ee6e00fd18c654ead895bc9597a4b0a`;
- tags metadata: 8247 bytes, SHA256 `e0ce4f778656f766e2ed8cf981f728f6f5ac6ce1b3e829fd9567f306b3f40f4d`.

The official metadata exposes immutable tag commit SHAs, including historical release tags before the IceCube publication, so software states are mechanically pin-able. However metadata alone does not identify which MCEq revision IceCube used and does not map B4RITM `BarrWP/BarrWM/BarrYP/BarrYM/BarrZP/BarrZM` or `DIS-CSMS` to executable transformations.

Therefore `BLOCKED_0105A5B_R1D_EXTERNAL_COMPUTATIONAL_AUTHORITY_INCOMPLETE` remains unchanged.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
