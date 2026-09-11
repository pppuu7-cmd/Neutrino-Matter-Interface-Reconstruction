# 0105a6q5c — validated Argon official semantic four-file byte lock

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5C`
Classification: `BLOCKED_0105A6Q5C_ZENODO_DIRECT_TRANSPORT_FAILURE`
Scope: official Zenodo direct transport + exact byte identity only; NONDISCOVERY.

## Prospective chain

- parent q5b PASS record: `dcafed65cf9cbce3d8d87329425bf75e1c68b209`
- preregistration: `dc855ab6367ecb7ac095ac2e7d36db358cef8b2a`
- implementation: `5a7fc01db49fa046da8eb51b035b57ae1b9511f9`
- guards: `a8294f8a6b0007fc3f53a1d4a2ec7a68a7d9822d`
- execution head: `abea2d68f3332582a061b7cbbe0d7a5a6fa13f3d`

## Hosted validation

- run/job/artifact: `34548467774/103106110445/10179890554`
- dedicated guards: `8 passed`
- provider artifact ZIP SHA256: `6fa1e9bdc24eaebb3bb68906632cba21ee1b4569eed9a49961202d809dc24bb8`
- independently downloaded ZIP SHA256: `6fa1e9bdc24eaebb3bb68906632cba21ee1b4569eed9a49961202d809dc24bb8`
- independent inner `result.json` SHA256: `473044172e0ed9cbcefa45999f67175a0aa45737f65cb666a76e88702d287b82`

Green Actions success was not treated as scientific PASS. Raw artifact classification and errors were inspected against the frozen q5c gate.

## Result

All four exact q5b-frozen Zenodo API content endpoints returned `HTTP 406 NOT ACCEPTABLE` before payload acquisition:

- `CENNS10AnlAEfficiency.txt`: HTTP 406;
- `readYAMLParameters.py`: HTTP 406;
- `PlotExtractedData.C`: HTTP 406;
- `LArParametersAnlA.yaml`: HTTP 406.

Therefore `EXACT_MATCH_COUNT=0` because no file payload was available to evaluate size/MD5/SHA256. This is a transport/infrastructure BLOCKED result, not an official-byte mismatch and not a scientific FAIL. The frozen q5c byte criteria are unchanged.

The q5c implementation sent `Accept: application/octet-stream`; the uniform 406 response across all four exact endpoints permits only a prospectively preregistered transport-header repair. It does not permit changing URLs, expected byte identities, provider, or scientific criteria.

No scientific file content was inspected or persisted; no pseudo-data, likelihood, systematic MC or observed BSM residual was evaluated.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next allowed action

A new q5c1 transport-only repair may repeat the same four exact Zenodo URLs and same frozen size+MD5+SHA256 identities while removing the over-specific `Accept: application/octet-stream` request header (using normal HTTP content negotiation). No other criterion may change. q5c remains historically BLOCKED.