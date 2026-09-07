# NMIR prereg 0082b — B-L stellar/SN vector integrity and native-axis authority

Date frozen: 2026-09-08
Status: **PROSPECTIVE / NO CONTROLLING PDF CONTENT INSPECTED**
Parent: 0082a `PASS_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY`.

## Question
Are the three source-authorized final B-L constraint-summary PDF assets machine-native vector figures with enough source-native text and numerical tick anchors to support a later fully reproducible axis calibration, without raster/manual digitization and without inspecting or selecting constraint curves by color/path geometry?

## Frozen source + asset authority
Use only the exact versioned arXiv source archives and exact controlling assets selected prospectively from 0082a TeX semantics:

1. Hong–Shin–Yun 2021:
   - arXiv `2012.05427v3`
   - archive SHA256 `6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc`
   - asset `B-LConstraints.pdf`
   - native parameter semantics: B-L gauge coupling denoted `e'`; gauge-boson mass denoted `m_{gamma'}` / equivalent TeX form.

2. Cerdeño et al. 2021:
   - arXiv `2106.11660v3`
   - archive SHA256 `f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d`
   - asset `Figures/BL_constraints.pdf`
   - native parameter semantics: `g_{B-L}` and vector mediator `Z'` mass `m_{Z'}`.

3. Shin–Yun 2022:
   - arXiv `2110.03362v2`
   - archive SHA256 `7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd`
   - asset `B-L_Constraints.pdf`
   - native parameter semantics: B-L gauge coupling denoted `e'`; gauge-boson mass denoted `m_{gamma'}` / equivalent TeX form.

No other figures are eligible in 0082b. In particular, Cerdeño `medium_effects_BL.pdf`, Hong cooling/hint assets and Shin–Yun spectral/cooling assets are not substitutes.

## Frozen asset-integrity procedure
For each exact source archive:
1. Fetch raw archive bytes and verify the frozen archive SHA256 before extracting anything.
2. Extract the exact controlling PDF member and record its byte count and SHA256.
3. Open exactly page 1 with PyMuPDF; require a single-page controlling plot or classify BLOCKED if the source-native asset is multi-page and no page identity was frozen by 0082a.
4. Record page width/height, drawing count, path-item count, image-XObject count and extractable word/span count.
5. `PASS_VECTOR_NATIVE` requires:
   - `image_xobject_count == 0`;
   - `drawing_count >= 10`;
   - at least 10 extractable words/spans.
   Failure of these frozen conditions is `BLOCKED_VECTOR_NATIVE_ROUTE`, not an invitation to raster digitize.

## Frozen native-axis text requirements
No axis convention may be imported from another paper.

For each PDF, source-native extractable text must establish all of:
1. a mass-axis identity consistent with the paper's native mediator-mass semantics, through either an explicit mass symbol/name plus a recognized energy unit (`eV`, `keV`, `MeV`, `GeV`) or an unambiguous source-native axis title containing both mass context and unit;
2. a B-L coupling-axis identity consistent with the source's own convention (`e'`/epsilon-like prime symbol for Hong/Shin; `g_{B-L}`/g-like B-L label for Cerdeño). The exact glyph may differ after PDF text extraction, but the identity must be source-native and cannot be inferred from curve position;
3. evidence that the two axes are logarithmic from source-native tick values spanning at least three orders of magnitude on each axis. Do not infer log scaling from equal visual spacing alone.

If the PDF text extraction fragments mathematical glyphs, deterministic normalization may join immediately adjacent source-native spans on the same text line, but may not invent missing symbols.

## Frozen numerical anchor sufficiency
Numerical anchors are text-derived only; no manual point picking.

For each PDF:
1. Parse numeric/scientific-notation tick labels from source-native words/spans, supporting ordinary decimal forms and powers-of-ten forms such as `10^-6`, `10−6`, `10⁻⁶`, or split adjacent `10` + exponent spans.
2. Classify tick anchors geometrically only by page-relative axis bands:
   - x-axis candidate labels: centers in the bottom 22% of the page and horizontally within the central 90%;
   - y-axis candidate labels: centers in the left 22% of the page and vertically within the central 90%.
3. Remove duplicate numerical values per axis.
4. Require at least **4 distinct major numerical anchors on x** and **4 on y**.
5. Require each accepted axis anchor set to span at least **3.0 decades** in numerical value.

These page-relative bands and counts are frozen prospectively. They may be implementation-debugged only for PDF text fragmentation that leaves the scientific geometry unchanged; the 22%, 90%, >=4 and >=3-decade criteria cannot be relaxed after result inspection.

## PASS
`PASS_B_L_STELLAR_SN_VECTOR_AXIS_AUTHORITY` iff all three controlling PDFs independently satisfy:
- exact archive provenance;
- exact asset extraction + asset SHA record;
- `PASS_VECTOR_NATIVE`;
- native mass-axis and coupling-axis identity;
- >=4 distinct source-text numeric anchors on each axis;
- >=3.0-decade span on each axis.

## BLOCKED / SCIENTIFIC_FAIL
- `BLOCKED_B_L_STELLAR_SN_VECTOR_AXIS_AUTHORITY`: any controlling source asset lacks sufficient vector/text/axis/anchor authority under the frozen rules. This retires only that source's geometry route; no raster/manual fallback.
- `SCIENTIFIC_FAIL_...` is reserved for a reproducible contradiction, e.g. the source-authorized controlling PDF has axis semantics incompatible with the source-native B-L mass/coupling convention, not merely insufficient extractable information.
- Dependency/parser/network/archive failures are infrastructure/implementation failures and must not be mislabeled scientific BLOCKED/FAIL.

## Guards
- No PDF drawing color/style/path semantic selection.
- No contour or filled-region extraction.
- No excluded-side assignment.
- No axis fit/calibration from pixel/PDF coordinates in 0082b; only anchor sufficiency/inventory.
- No cross-paper coupling conversion (`e'` is not silently renamed `g_{B-L}`).
- No cross-paper union/intersection or supersession.
- No global B-L envelope, response/enhancement scan or gain composition.

## Next action
- PASS -> prospectively preregister 0082c native-axis calibration + source-own curve semantic identity, separately per paper, using the now-hashed controlling PDF bytes and frozen anchor inventories.
- BLOCKED -> retire the blocked source's vector-geometry route and continue only independently authorized remaining branches or other 0071 families.

`NMIR_READINESS` remains 94% in 0082b; vector/axis authority alone does not create a new excluded region.
