# NMIR prereg 0082 — B-L stellar/SN primary source-asset authority

Date frozen: 2026-09-08
Status: **PROSPECTIVE / NO 0082 SOURCE ARCHIVE CONTENT INSPECTED**
Parent: 0081a `BLOCKED_COSMOLOGY_B_L_BBN_VECTOR_CALIBRATION_SEMANTIC_IDENTITY`.

## Question
Can the stellar/supernova part of the frozen 0071 `U(1)_{B-L}` external-constraint ledger be grounded in exact primary source archives with machine-native candidate assets for later contour materialization, without reading numerical values by eye from plots? Also, does the later Shin–Yun primary work need to be carried as an explicit update to the older Hong–Shin–Yun stellar/SN authority before any contour is chosen?

## Frozen primary-source set
Audit exactly these versioned primary archives:
1. Hong, Shin, Yun, *Cooling of young neutron stars and dark gauge bosons*, Phys. Rev. D 103, 123031 (2021), arXiv `2012.05427v3`, source URL `https://export.arxiv.org/e-print/2012.05427v3`.
2. Cerdeño, Cermeño, Pérez-García, Reid, *Medium effects in supernovae constraints on light mediators*, Phys. Rev. D 104, 063013 (2021), arXiv `2106.11660v3`, source URL `https://export.arxiv.org/e-print/2106.11660v3`.
3. Shin, Yun, *Dark gauge boson production from neutron stars via nucleon-nucleon bremsstrahlung*, JHEP 02 (2022) 133, arXiv `2110.03362v2`, source URL `https://export.arxiv.org/e-print/2110.03362v2`.

The third source was added prospectively after a literature refresh found that its abstract explicitly states that the SN1987A `U(1)_{B-L}` constraint is revisited, with stronger transverse-polarization exclusion and a new longitudinal-polarization excluded region. This gate does **not** assume that it supersedes every young-neutron-star result from the 2021 paper; it only requires that the later paper not be omitted from the source authority set.

## Frozen audit procedure
For each exact versioned archive:
1. Download raw source bytes and record SHA256 and byte count.
2. Open as the archive format supplied by arXiv and inventory every member name, size and extension.
3. Concatenate source text only from TeX-like text members (`.tex`, `.sty`, `.cls`, `.bib`, `.txt` where decodable) and verify the paper is explicitly about the relevant `B-L`/`U(1)_{B-L}` constraint, not merely citing another paper.
4. Inventory candidate machine-native assets separately:
   - vector/document: `.pdf`, `.eps`, `.ps`, `.svg`;
   - numerical/code: `.csv`, `.dat`, `.tsv`, `.json`, `.yaml`, `.yml`, `.py`, `.m`, `.nb`, `.ipynb`, `.root`;
   - raster-only: `.png`, `.jpg`, `.jpeg`, `.gif`, `.tif`, `.tiff`.
5. Search source-native TeX for figure/table/include commands and preserve the referenced filenames/tokens. Do not infer a contour identity from visual appearance.
6. Record source-native phrases/flags establishing whether the analysis concerns SN1987A, NS1987A/Cas A/young-neutron-star cooling, B-L coupling, medium effects, transverse/longitudinal modes, and whether the later Shin–Yun paper explicitly says the SN1987A result is revisited.

## Scientific acceptance
Per-source `PASS_SOURCE_AUTHORITY` requires all of:
- exact versioned archive fetch succeeds;
- archive SHA256 and member manifest are recorded;
- source text contains explicit B-L model/constraint semantics;
- at least one source-native candidate route exists for a later reproducible numerical materialization: a numerical/code asset **or** a vector/document figure asset referenced from the source.

Per-source `PARTIAL_SOURCE_AUTHORITY` is used when exact source and semantics are verified but only raster/no candidate machine-native materialization asset exists.

Overall `PASS_B_L_STELLAR_SN_PRIMARY_SOURCE_ASSET_AUTHORITY` requires all three sources to be `PASS_SOURCE_AUTHORITY` and the Shin–Yun source to contain explicit source-native evidence that the SN1987A B-L constraint is revisited. `PASS_PARTIAL_...` is allowed if exact source identity/semantics are secured for all three but one or more sources lack a machine-native contour route. `BLOCKED_...` is reserved for missing/inaccessible exact primary source or insufficient source-native B-L semantic identity. Parser/archive/dependency/network failures are infrastructure failures, not scientific BLOCKED.

## Guards
- No numerical contour extraction in 0082.
- No raster/manual digitization or point picking.
- No assumption that a PDF/EPS asset is vector-native until separately inspected.
- No Hong/Cerdeño/Shin-Yun curve union/intersection.
- No claim that Shin–Yun supersedes NS1987A/Cas-A cooling results unless a later semantic gate proves the exact scope.
- No global B-L envelope, response/enhancement scan, or multiplication of gains.

## Next action
- PASS -> separately preregister 0082a semantic/scope authority for the controlling stellar/SN curves, then inspect candidate vector/numerical assets before geometry.
- PARTIAL -> continue only through sources with authorized machine-native routes; preserve missing route as explicit blocker.
- BLOCKED -> retire the affected source route and return to another missing 0071 family; never substitute a secondary plot by eye.

`NMIR_READINESS` cannot increase at 0082 unless a source-authority uncertainty class is reproducibly closed; source inventory alone does not create a new excluded region.