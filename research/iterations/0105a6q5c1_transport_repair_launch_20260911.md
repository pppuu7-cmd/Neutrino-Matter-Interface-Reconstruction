# NMIR v2 iteration — q5b PASS, q5c transport BLOCKED, q5c1 launched

Date: 2026-09-11

## Validated closes

q5b is validated `PASS_0105A6Q5B_ARGON_OFFICIAL_SEMANTIC_FILE_CANDIDATES_LOCATED_NONDISCOVERY`, record commit `dcafed65cf9cbce3d8d87329425bf75e1c68b209`, run/job/artifact `34548230167/103105373901/10179807293`, provider+independent ZIP SHA256 `01d42376bd95006de11d09cb39411ddfb7b9871d495a17dd8f34f85fc4c85236`, inner result SHA256 `a4952c906ab7bbd513b0fafa661078ab3cfa181575bb5aeaaf48bf1cd7a22444`. Complete returned set is four files: `CENNS10AnlAEfficiency.txt`, `readYAMLParameters.py`, `PlotExtractedData.C`, `LArParametersAnlA.yaml`.

q5c is validated `BLOCKED_0105A6Q5C_ZENODO_DIRECT_TRANSPORT_FAILURE`, record commit `2858c33ebf1d75cfbe82d949d8a838b0815a2cb4`, run/job/artifact `34548467774/103106110445/10179890554`, provider+independent ZIP SHA256 `6fa1e9bdc24eaebb3bb68906632cba21ee1b4569eed9a49961202d809dc24bb8`, inner result SHA256 `473044172e0ed9cbcefa45999f67175a0aa45737f65cb666a76e88702d287b82`. All four exact Zenodo content endpoints returned HTTP 406 before payload acquisition, so this is transport BLOCKED, not byte mismatch or scientific FAIL.

## Active prospective repair

q5c1 preregistration commit `cf3d7bebc1aae654ec09a78284c6f3162df4f9df` freezes the only transport change: omit q5c's explicit `Accept: application/octet-stream` header. Exact URLs, sizes, MD5, SHA256, provider and four-file set are unchanged.

Implementation `6780c281b78b1e6aa117c623aefcfea4de17e1a4`; guards `5fa9ababe4a518e0becf1ad8dff4c2e74c629f0a`; hosted execution head `6099d9f73c4d67b43aa0b65c4953fdfcffe8e736`; dedicated run `34548561838` queued at last validation. Do not duplicate it.

No semantic content inspection, pseudo-data generation, likelihood evaluation, systematic MC or observed BSM residual inspection is authorized by q5b/q5c/q5c1.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`

Exact continuation: consume terminal q5c1 raw job and artifact; independently verify ZIP/inner hashes and all four exact byte identities. Only q5c1 PASS may authorize a separately preregistered bounded semantic audit over the complete four-file set.