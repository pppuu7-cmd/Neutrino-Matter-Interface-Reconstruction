# NMIR iteration 0086 — B-L external-family completeness/actionability audit

Date: 2026-09-08
Prospective contract: `research/prereg/0086_b_minus_l_external_family_completeness_actionability.md`, frozen commit `0ec016c249883825d5c658c816766f6c23c1375d` before this classification.
Final classification: **BLOCKED_B_L_EXTERNAL_FAMILY_MISSING_COLLIDER_FIXED_TARGET**
`NMIR_READINESS: 98%`.

## Scientific question
Has the original 0071 five-family external-constraint program reached a state where every mandatory family is either reproducibly authoritative or explicitly blocked/retired, so that a later cross-family composition can be preregistered without silently dropping a family?

## Frozen 0071 family list
The authoritative 0071 contract requires, in the same gauge-complete `L_int = g_BL V_mu J_{B-L}^mu` convention over `1e-6 eV <= m_V <= 10 GeV`:
1. low-energy laboratory neutrino scattering / CEvNS / neutrino-electron;
2. collider/fixed-target visible/invisible searches;
3. stellar/SN;
4. cosmology;
5. fifth-force/EP/long-range.

No family may be treated as covered merely because it appears as a label on another source's summary plot.

## Family-by-family audit
### 1. Low-energy laboratory neutrino scattering — AUTHORITATIVE
0085 recovery lineage contains 0078c `PASS_SOLAR_CEVNS_B_L_EXCLUDED_REGION / PASS_PARTIAL_B_L_EXTERNAL_ENVELOPE`, a reproducibly materialized primary De Romeri solar-CEvNS excluded region in the frozen B-L convention. COHERENT combined-likelihood reproduction remains separately blocked at 0074c, but that blocker does not erase the independently authoritative low-energy solar-CEvNS object.

### 2. Collider/fixed-target visible/invisible — MISSING_UNAUDITED
Repository search across research/code/data records found no independent numbered iteration, preregistered authority audit, or source-specific same-convention collider/fixed-target constraint object. Searches for the family terms and common source labels (`collider`, `fixed-target`, `beam dump`, `NA64`, `BaBar`) returned no independent repository authority.

This family was mandatory already in prospective 0071. Its absence cannot be repaired by treating review/summary curves embedded in another family's figure as primary authority.

### 3. Stellar/SN — AUTHORITATIVE with explicit residual blockers
0084b `PASS_SHIN_YUN_SN1987A_ANALYTICAL_GEOMETRY_AUTHORITY` supplies reproducible primary source-text finite low-mass band geometries, while Hong/Cerdeño residual routes remain explicitly blocked/retired. This satisfies actionability accounting for the family without pretending every stellar/SN source is materialized.

### 4. Cosmology — AUTHORITATIVE with scenario alternatives / explicit BBN blocker
0080d supplies hard-CMB Majorana and Dirac excluded geometries; 0080e preserves them as alternative scenario-conditioned branches. 0081 fixes BBN semantics and 0081a explicitly blocks BBN vector geometry. The family is therefore represented and its unresolved subroute is explicit rather than silently omitted.

### 5. Fifth-force / EP / long-range — AUTHORITATIVE asymptotic + explicit finite-mass blocker
0079/0079a provide the long-range MICROSCOPE/Fayet asymptotic `g_BL < 2.5437058144595744e-25` (conservative `2.5e-25` at 2 sigma), while finite-mass Yukawa continuation is explicitly unauthorized. The family is represented and the finite-range limitation is explicit.

## Controlling result
Exactly one mandatory 0071 family is `MISSING_UNAUDITED`: collider/fixed-target visible/invisible searches.

Therefore the frozen PASS criterion fails and the correct classification is:

`BLOCKED_B_L_EXTERNAL_FAMILY_MISSING_COLLIDER_FIXED_TARGET`.

This is not evidence that collider/fixed-target constraints are weak or absent physically. It is a source-of-truth completeness blocker: NMIR has not yet independently audited them in the frozen gauge-complete B-L convention.

## Scientific consequence
A scenario-aware cross-family global envelope cannot yet be preregistered as complete, because doing so would silently omit one of the five families prospectively required by 0071. BSM response/enhancement remains locked.

The next highest-value gate is therefore not another CEvNS/cosmology/stellar refinement and not a material scan. It is a **collider/fixed-target primary-authority audit** that freezes exact primary sources, coupling/decay assumptions, mass support, confidence-level/excluded-side semantics, and whether source-native numerical materialization is possible without raster/manual digitization.

## Readiness
`NMIR_READINESS` remains **98%**. The audit exposes a genuine missing mandatory family but does not itself add a new reproducible exclusion object.

## Guards
No cross-family union in 0086. No review-figure contour promotion. No raster/OCR/manual extraction. No BSM response scan. No reopening 0074c absent genuinely new primary numerical benchmark authority. No assumption that a collider/fixed-target limit for a generic dark photon maps to B-L without exact source coupling/decay mapping.
