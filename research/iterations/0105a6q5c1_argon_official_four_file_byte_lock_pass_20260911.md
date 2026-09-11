# 0105a6q5c1 — validated Argon official four-file byte lock after content-negotiation repair

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5C1`
Classification: `PASS_0105A6Q5C1_ARGON_OFFICIAL_FOUR_SEMANTIC_FILES_BYTE_LOCKED_NONDISCOVERY`
Scope: official Zenodo transport + exact byte identity only; NONDISCOVERY.

## Prospective chain

- q5c historical transport-BLOCKED record: `2858c33ebf1d75cfbe82d949d8a838b0815a2cb4`
- q5c1 preregistration: `cf3d7bebc1aae654ec09a78284c6f3162df4f9df`
- implementation: `6780c281b78b1e6aa117c623aefcfea4de17e1a4`
- guards: `5fa9ababe4a518e0becf1ad8dff4c2e74c629f0a`
- execution head: `6099d9f73c4d67b43aa0b65c4953fdfcffe8e736`

The only repair relative to q5c was omission of the explicit `Accept: application/octet-stream` header. Exact URLs, expected sizes, MD5s and SHA256s remained unchanged.

## Hosted validation

- run/job/artifact: `34548561838/103106394242/10179925214`
- dedicated guards: `7 passed`
- provider artifact ZIP SHA256: `16ade2b6287191e8318f61314c206b9e7c71c2935c861edcf97e262cd8780fcb`
- independently downloaded ZIP SHA256: `16ade2b6287191e8318f61314c206b9e7c71c2935c861edcf97e262cd8780fcb`
- independent inner `result.json` SHA256: `d0a0884101d977fe8b34814c939506a12b187f2b705d5fbcc6dd013f1c87dacd`

Green Actions success was not treated as scientific PASS; raw artifact bytes and all four file identities were independently checked.

## Exact four-file result

All four frozen Zenodo API endpoints returned HTTP 200 and matched exact size + MD5 + frozen 0105a3 SHA256:

- `CENNS10AnlAEfficiency.txt`: 1804 bytes; MD5 `77139f1bb79dcf972a3a0ecc28a4a8f5`; SHA256 `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`.
- `readYAMLParameters.py`: 1814 bytes; MD5 `708becd2d56cec1c2e672038581b8c7c`; SHA256 `3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6`.
- `PlotExtractedData.C`: 14020 bytes; MD5 `1161762465460efdda35d4494a0d8547`; SHA256 `c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f`.
- `LArParametersAnlA.yaml`: 4906 bytes; MD5 `cc9f2c60ce0c17809453e0caad9c4a38`; SHA256 `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`.

`EXACT_MATCH_COUNT=4`.

No scientific semantics were interpreted by q5c1; file content was not persisted in the artifact. No pseudo-data, likelihood evaluation, systematic MC or observed BSM residual inspection occurred.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next allowed action

A separately prospectively frozen bounded semantic-evidence inventory may inspect all four exact byte-locked files together. It must define evidence categories and extraction rules before content inspection and may not yet execute a likelihood or observed residual analysis.