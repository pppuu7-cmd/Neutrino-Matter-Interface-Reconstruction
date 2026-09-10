# 0105a6h — Ar content-addressed semantic-file recovery result

Date: 2026-09-10
Gate: `NMIR-V2-0105A6H`
Classification: `BLOCKED_0105A6H_SEMANTIC_FILE_BYTE_EQUIVALENCE_INCOMPLETE`
Scope: transport / byte-equivalence only; NONDISCOVERY

## Frozen parent / authority

Preregistration commit: `baadcc1d01740eba72da806959c71ae49f18e483`.
Frozen untrusted byte carrier: `Newtrinos-org/Newtrinos.jl` commit `fa87689ddedae1929e33d66ad1f0efa1b7cce206`.
Scientific authority remains the official COHERENT Zenodo byte lock from 0105a3; the carrier is not promoted to scientific authority.

0105a3 normalized manifest SHA256: `5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`.
Official Ar record: Zenodo `3903810`, DOI `10.5281/zenodo.3903810`.

## Authoritative hosted execution

Execution head: `1ab1f0acc91c13d4e3075661c55af513fac4a0d7`.
Run/job: `34489395472 / 102911871576`.
Artifact: `10157049923`, `nmir-v2-0105a6h-argon-content-addressed-semantic-recovery`.
Dedicated deterministic guards: `5 passed`.

Provider artifact ZIP SHA256: `670099bbc11e28ccb3a083d73bb8affcd5cec2c1a98f53614b2f9b3ca765a5da`.
Independent downloaded ZIP SHA256: `670099bbc11e28ccb3a083d73bb8affcd5cec2c1a98f53614b2f9b3ca765a5da`.
Inner `result.json` SHA256: `68c3bd83e9a26de0bc3dac14b1c4fde396d23c7bf4e780fa5046c8219413c340`.

Green workflow status alone was not used as a scientific or authority PASS; the raw log and artifact bytes were consumed and independently hashed.

## Frozen four-file result

1. `LArParametersAnlA.yaml`
   - classification: `ACCEPTED_AS_OFFICIAL_BYTE_EQUIVALENT`
   - size: `4906`
   - MD5: `cc9f2c60ce0c17809453e0caad9c4a38`
   - SHA256: `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`
   - all frozen size/MD5/SHA256 gates: PASS.

2. `readYAMLParameters.py`
   - classification: `REJECTED_NOT_BYTE_EQUIVALENT`
   - transport result from the prospectively frozen carrier/path: HTTP 404.
   - no semantic substitution or guessed replacement is allowed.

3. `PlotExtractedData.C`
   - classification: `REJECTED_NOT_BYTE_EQUIVALENT`
   - transport result from the prospectively frozen carrier/path: HTTP 404.
   - no semantic substitution or guessed replacement is allowed.

4. `CENNS10AnlAEfficiency.txt`
   - classification: `ACCEPTED_AS_OFFICIAL_BYTE_EQUIVALENT`
   - size: `1804`
   - MD5: `77139f1bb79dcf972a3a0ecc28a4a8f5`
   - SHA256: `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`
   - all frozen size/MD5/SHA256 gates: PASS.

Accepted count: `2 / 4`.

## Classification

The frozen gate requires all four named files to be byte-identical to the already-authoritative 0105a3 identities. Because two files were not delivered by the frozen carrier, the only allowed classification is:

`BLOCKED_0105A6H_SEMANTIC_FILE_BYTE_EQUIVALENCE_INCOMPLETE`.

This is an authority/transport BLOCKED classification, not a scientific failure of the Standard Model and not evidence for BSM physics.

The two accepted files may be read semantically because their byte identity is exact; authority remains the official 0105a3 Zenodo lock. The missing two files remain unavailable under this gate and may not be reconstructed manually or replaced by analogous implementations.

## Permissions

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

No likelihood fit, observed-minus-null residual, BSM scan, significance calculation or post-result nuisance choice is authorized by this result.

## Exact next permitted action

A new transport-only recovery gate may prospectively target the two still-missing exact official byte identities (`readYAMLParameters.py`, `PlotExtractedData.C`) using an independently frozen carrier/source and the unchanged 0105a3 size+MD5+SHA256 acceptance rule. Alternatively, a restored official Zenodo direct route may be retried under its already-frozen official-provider contract. No semantic use of those two files is allowed before exact byte identity is established.