# NMIR preregistration 0084a — Shin–Yun SN1987A analytical excluded-band semantics

Date frozen: 2026-09-08
Parent authority: 0084 `PASS_SHIN_YUN_B_L_REVISION_SCOPE_AUTHORITY`.

## Scientific question
Before any finite-area materialization, can exact Shin–Yun `2110.03362v2` source TeX establish a non-ambiguous analytical topology for the SN1987A B-L transverse and longitudinal branches, including the relation between the body statement `m_gamma' < 2 m_e` and the conclusion summary `m_gamma' < 1 MeV` for the high-coupling allowed/trapping side?

## Frozen source/provenance
- exact source archive SHA256: `7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd`;
- exact source-native TeX only;
- 0084 raw contexts may be used only as pointers back to exact source statements, not as a substitute for source semantics.

## Frozen semantic objects
Transverse candidate source statements:
- low-coupling/free-streaming boundary: `e' < 1e-11` for `m_gamma' < 20 MeV`;
- high-coupling allowed/trapping boundary in body: `e' > 1.5e-8` allowed for `m_gamma' < 2 m_e`;
- conclusion summary: same `e' > 1.5e-8` allowed for `m_gamma' < 1 MeV`.

Longitudinal candidate source statements:
- low-coupling allowed boundary: `e' m_gamma' < 7.4e-10 MeV` for `m_gamma' < 20 MeV`;
- high-coupling allowed boundary in body: `e' m_gamma' > 1.2e-5 MeV` allowed for `m_gamma' < 2 m_e`;
- conclusion summary: same product boundary allowed for `m_gamma' < 1 MeV`.

## Frozen criteria
### PASS_SHIN_YUN_SN1987A_BAND_SEMANTICS
Requires all of:
1. exact source text explicitly identifies the relevant SN1987A regions as excluded and separately calls the high-coupling side allowed/reabsorbed/trapped or equivalent;
2. transverse and longitudinal boundaries are separately identifiable and must not be merged;
3. the body and conclusion high-coupling relations have the same coupling/product boundary and differ only in the source-stated mass-domain wording (`2 m_e` versus `1 MeV`), with no source text assigning them to different physical branches;
4. no statement authorizes interpreting the low-coupling boundary as exclusion of all larger couplings;
5. exact-domain output for any later geometry is frozen as **source-statement-conditioned**: body-domain and conclusion-domain variants must remain distinct unless a later externally grounded constant/convention gate proves a numerical identity/order. 0084a itself may not silently replace one by the other.

### BLOCKED_SHIN_YUN_SN1987A_BAND_SEMANTICS
Use if source text cannot establish allowed/excluded side or physical branch identity without figure/manual interpretation, or if body/conclusion statements are genuinely contradictory in coupling/product boundary rather than merely differing in mass-domain summary wording.

### SCIENTIFIC_FAIL
Use only for an explicit source contradiction of the frozen topology premise. Parser/extraction failures are infrastructure failures.

## Infrastructure vs scientific failure
Archive/hash/download/parser/test/serialization failure -> infrastructure failure. A false positive/negative demonstrated by raw source context -> implementation defect; repair without changing this contract and rerun.

## Prohibited in 0084a
- no area calculation;
- no conversion of `2 m_e` to MeV using an external constant;
- no choice of `<1 MeV` or `<2m_e` as the single universal endpoint;
- no NMIR `g_BL` convention conversion;
- no union with Hong, solar CEvNS, cosmology, fifth-force, or other families;
- no raster/OCR/manual contour reading;
- no BSM response/enhancement calculation.

## Frozen next action
PASS -> record immutable semantics and then preregister 0084b for source-native analytical geometry/convention mapping, with any needed electron-mass constant and global plotting clip frozen before computation. BLOCKED/FAIL -> retain 0084 analytical anchors but do not materialize an SN1987A polygon; move to another missing 0071 family.
