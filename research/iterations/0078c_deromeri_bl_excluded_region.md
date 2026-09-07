# NMIR iteration 0078c — De Romeri et al. combined solar-CEvNS B-L excluded region

Date: 2026-09-07
Prospective contract: `research/prereg/0078c_deromeri_bl_excluded_region.md`.
Parent PASS: 0078b `PASS_COMBINED_SOLAR_CEVNS_B_L_VECTOR_CALIBRATION`, run/job `34154728073/101844079794`, artifact `10030555477`, raw JSON SHA256 `785605b660efeabf13d1825bf8f66fa4a1e4d4f8675514c45f76cd036a5171de`.

## Classification

**`PASS_SOLAR_CEVNS_B_L_EXCLUDED_REGION`** with secondary classification **`PASS_PARTIAL_B_L_EXTERNAL_ENVELOPE`**.

This closes 0078 as `PASS_NEW_EXECUTABLE_SURVIVOR_BSM` for the new combined solar-CEvNS B-L constraint family only. It does not complete the global 0071 envelope and does not authorize any BSM response/enhancement calculation.

## Frozen primary authority

- arXiv source: `2603.00554`
- source archive SHA256: `09ab22f753ac3f5fbde5be65ac50926de67b0638550366d158aadcfde8e92564`
- vector asset: `vector_BL_PnX_XnT_LZ_combined.pdf`
- asset SHA256: `ace761499623535907263e780a6e96a17474adf418d3f9363dae8e28bc5e7a39`
- source TeX identity: right panel vector B-L; primary filled magenta region is the combined XENONnT + PandaX-4T + LZ 90% CL exclusion.

0078c used the 0078b affine calibration verbatim and did not refit axes or infer excluded side from line geometry.

## Hosted authority and artifact inspection

- workflow: `NMIR 0078c solar-CEvNS B-L excluded region`
- run/job: `34155151971/101845330760`
- workflow head: `a0bdaf4619a4da37f8ecd93445f8cbaf2c509e5b`
- artifact: `10030703063`, `nmir-0078c-bl-excluded-region`, 6673 bytes
- artifact ZIP SHA256 from GitHub metadata and independent downloaded-byte check: `ea59df50c4f1cbb5938effd455bdc0528b91b95753f0cfdc393437efe98a9378`
- artifact payload: `deromeri_bl_excluded_region_0078c.json`, 25272 bytes
- independently computed payload SHA256: `0339cfbcfd2ccc5689fdb82473082ffe9ebb26964ed255411952e98b72047ca5`
- repository-persisted machine result: `data/deromeri_bl_excluded_region_0078c.json`
- result persistence commit: `dd43ebba8c1e6ff4f58899f63cab7641758eac60`

The artifact ZIP itself was downloaded and inspected; the scientific classification below comes from the artifact payload, not from the green workflow status.

## Frozen topology gates

The primary filled magenta object yields one valid clipped polygon component in the frozen domain
`-5 <= log10(m_V/GeV) <= 1`, `-8 <= log10(g_BL) <= -2`.

Machine result:

- excluded log-space area: `12.51987545543835 decade^2`
- polygon components: `1`
- representative interior point: `(-2.6847500623811644, -3.3601483009520727)`
- distance of that point to plot boundary: `1.3601483009520727` decades
- stroke-only boundary-control points: `50`
- fraction within `0.05` decade of filled-union boundary: `1.0` (PASS)
- 32-vs-64 cubic subdivision area difference: `0.0`
- symmetric-difference relative area: `0.0`

Thus the filled primary region passes closure/validity/clipping/subdivision/boundary-control criteria without topology repair, smoothing, convex hull, manual digitization, or excluded-side inference.

## Combination audit

The new solar-CEvNS region is a valid standalone 90% CL external exclusion family. Existing families are not silently promoted:

- COHERENT 0074c remains `BLOCKED_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY` and is not combined;
- Wagner 0072 remains `PARTIAL_PASS_WAGNER_VECTOR_CURVES`; global excluded-side authority is unresolved and is not assumed;
- global 0071 remains incomplete.

Therefore the correct combined classification is only `PASS_PARTIAL_B_L_EXTERNAL_ENVELOPE`.

## Scientific consequence

A previously missing reproducible B-L constraint family is now machine-readable in the common `(m_V,g_BL)` convention, with explicit primary excluded-side authority. This is a genuine external-constraint scientific PASS and not merely documentation or CI progress.

The global 0071 B-L envelope is still incomplete. No response/enhancement scan is authorized until remaining required primary families controlling the frozen `1e-6 eV <= m_V <= 10 GeV` interval have reproducible geometry/numerics plus excluded-side authority and a formal global-envelope gate passes.

## Exact next action

Prospectively select the highest-value remaining primary family needed by 0071. Priority should be a low-mass long-range/fifth-force family because it controls a region not supplied by the new solar-CEvNS exclusion. Freeze source/convention/side authority and an admissible machine-readable materialization route before extracting any new contour values. Do not reuse unresolved Wagner blue-family semantics or infer `above/below` from a line after inspection.

## Readiness

`NMIR_READINESS: 92%`.

Increase by one point from 91% is justified by a new reproducible scientific external-exclusion gate with independently inspected artifact bytes. The global B-L envelope and BSM response remain open/locked.