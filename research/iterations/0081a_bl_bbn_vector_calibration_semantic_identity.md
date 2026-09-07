# NMIR iteration 0081a — B-L BBN vector calibration + semantic identity

Date: 2026-09-08
Classification: **BLOCKED_COSMOLOGY_B_L_BBN_VECTOR_CALIBRATION_SEMANTIC_IDENTITY**

## Authority order
Authoritative prospective contract: `research/prereg/0081a_bl_bbn_vector_calibration_semantic_identity.md`, commit `ad37205e6a30188f4129fdca8e0d49a156ab6e36`.
Implementation details were frozen before vector-result inspection in `research/prereg/0081a_implementation_freeze_authority.md`, commit `27ac3703547c67f5e130baba9b884688ef176a13`.

A later parallel prereg `research/prereg/0081a_bl_bbn_axis_calibration.md`, commit `ee5ef6972a8433ab2b59fb80c56b26bd23fac168`, is non-authoritative because it was created after the authoritative 0081a contract. Its output is not used to select or reinterpret this result.

## Primary inputs
Esseili–Kribs arXiv `2308.07955v2`, source SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`.

Native vector assets:
- Majorana Fig.7 `Presentation/CnstrntPlotMajoranaYp.pdf`, SHA256 `4326f3ac9ba29e515aa22afafef27d08c05d0e6be04db605c4706418c6cd8926`;
- Dirac Fig.8 `Presentation/CnstrntPlotDiracYp.pdf`, SHA256 `14d9afe16f4c38f1d3c08f97ccf086a570739b18731b0b6ffee97fe4b9e63b15`.

0081 had already frozen the observational criterion as signed
`Delta Y_p = Y_p(BSM)-Y_p(SM) = 0.008` at 95% C.L.

## Hosted result
Authoritative run/job: `34165337031/101875151196`
Artifact: `10033955293`
Raw JSON SHA256: `daf2f687d8d817ce20f9568aeb27843ff7fe8b9d7e94391dffb844946b41f34e`
Artifact ZIP SHA256: `d5c1495ce4a1dee6928093aec79de0b3aea8dddcc76e21b93082263afae4445a`
Dedicated tests: `4 passed`.

Persistent result ledger: `data/esseili_kribs_bbn_vector_0081a_authority.json`, commit `dfccfe08dee2ad7922749dcebc56175fffed51f1`.

## Why BLOCKED is valid
### 1. Independent x-axis calibration authority is insufficient
The BBN PDFs expose only two labeled x-axis major anchors in extractable source-native text: `0.1` and `1`. The authoritative prereg required at least four distinct major tick anchors when enough authority is exposed and explicitly required BLOCKED rather than borrowing the CMB transform when the native BBN assets do not provide enough independent anchors.

The same PDFs expose four y-axis labels (`10^-11` through `10^-8`), but both physical axes must be independently recoverable. Therefore the x-axis authority gap alone is sufficient for BLOCKED.

### 2. `Delta Y_p=0.008` vector identity is not unique
Each panel contains one textual `0.008` threshold label. The frozen text-color route finds no unique scientific vector style matching the threshold text color. The preregistered 2.5-PDF-point adjacency fallback is also ambiguous:
- Majorana: multiple non-overlay blue styles lie at essentially the same nearest distance (~`1.58246 pt`);
- Dirac: multiple non-overlay blue styles reach distance `0` to the label neighborhood.

The dashed-red CMB overlay was correctly identified and excluded, so the ambiguity is among remaining BBN-native blue styles rather than the known CMB overlay.

The implementation-freeze rules prohibit changing color tolerances, adjacency radius, choosing a darker/lighter blue after seeing the output, or using manual/raster inspection. Therefore no unique threshold path may be promoted.

## Scientific meaning
This is **not** a failure of BBN physics, not evidence that the Esseili–Kribs calculation is wrong, and not a statement that no BBN B-L bound exists. It is a reproducibility/provenance BLOCKED result under the frozen no-manual-inference contract: the published native PDF does not provide enough independently machine-identifiable authority to materialize the `Delta Y_p=0.008` excluded polygon without extra assumptions.

Per the preregistered decision tree, the current BBN-geometry route stops here. No 0081b polygon is authorized.

## Next funnel step
Return to the incomplete 0071 external B-L envelope and audit an independent missing primary family. Highest-value next family: stellar/SN constraints (e.g. primary SN1987A / stellar-cooling authorities already referenced in the 0071 ledger), beginning with a prospective source-asset/provenance gate before extracting any contour.

## Readiness
`NMIR_READINESS: 94%` — unchanged. BLOCKED is informative and closes a route, but it does not add a new materialized excluded region.
