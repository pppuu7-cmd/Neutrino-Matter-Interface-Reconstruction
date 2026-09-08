# NMIR preregistration 0086 — B-L external-family completeness/actionability audit

Date frozen: 2026-09-08
Status: PROSPECTIVE
Parent authority: 0085 `PASS_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE`.

## Scientific question
Before any cross-family B-L union/composition or BSM-response unlock, has the original 0071 external-constraint program actually closed every required primary family in the same `L_int = g_BL V_mu J_{B-L}^mu` convention, or is a mandatory family still missing rather than explicitly blocked/retired?

This is a documentary class-level gate. It performs no BSM response calculation and no cross-family numerical union.

## Frozen required families
Use exactly the five families prospectively required by 0071 commit `80d93debb2a20e35d6e06fa3000591f82ffbd1a8` over `1e-6 eV <= m_V <= 10 GeV`:
1. low-energy laboratory neutrino scattering / CEvNS / neutrino-electron scattering;
2. collider/fixed-target visible/invisible searches, with decay assumptions explicit;
3. stellar/SN production, cooling and trapping;
4. cosmological BBN/CMB/free-streaming;
5. fifth-force/equivalence-principle/long-range-force.

## Exact inputs/provenance
Audit only repository authority through 0085 plus primary sources already frozen by those iterations. Search repository code/data/research records for each family. A family is not considered covered merely because a review or another family's plot contains it.

For any newly claimed primary source, freeze exact citation/version and source bytes/hash before using it for a result-dependent contour calculation. This 0086 gate may identify a candidate source, but may not materialize a new contour without a child preregistration.

## Frozen statuses per family
Each family must receive exactly one status:
- `AUTHORITATIVE`: at least one reproducible same-convention primary constraint object exists, with scope/side/assumptions preserved;
- `BLOCKED_EXPLICIT`: applicable primary constraint exists but the exact NMIR materialization route is blocked for a prospectively recorded scientific-authority reason;
- `RETIRED_EXPLICIT`: a previously attempted route is explicitly retired and no silent numerical use is permitted;
- `MISSING_UNAUDITED`: no independent repository authority closes the family.

`BLOCKED_EXPLICIT` or `RETIRED_EXPLICIT` does not mean the physical constraint is absent; it means NMIR cannot use that route quantitatively under current rules.

## Acceptance criteria
`PASS_B_L_EXTERNAL_FAMILY_COMPLETENESS_ACTIONABILITY` only if all five required families are `AUTHORITATIVE`, `BLOCKED_EXPLICIT`, or `RETIRED_EXPLICIT`, with no `MISSING_UNAUDITED`, and the audit demonstrates that a later conservative scenario-aware composition can be defined without silently dropping a mandatory family.

`BLOCKED_B_L_EXTERNAL_FAMILY_MISSING_<FAMILY>` if any required family is `MISSING_UNAUDITED`. The exact missing family becomes the next highest-value gate. If more than one is missing, choose the one expected to dominate the largest uncovered mass interval; do not run a material/source scan.

`SCIENTIFIC_FAIL_B_L_EXTERNAL_LEDGER_INCONSISTENT_CONVENTION` only if existing authoritative families cannot be mapped consistently to the frozen gauge-complete B-L convention without an actual contradiction, not merely because of absent data.

## Guards
- No cross-family union/intersection in 0086.
- No BSM response/enhancement calculation.
- No revival of 0074c combined COHERENT likelihood without genuinely new primary numerical benchmark authority.
- No review-figure contour promoted to primary authority.
- No raster/OCR/manual digitization.
- No family considered covered by another family's plot label.
- No finite-mass continuation of the 0079a asymptotic fifth-force anchor.
- Preserve Majorana/Dirac alternatives and Shin–Yun T/L + BODY_NATIVE/CONCLUSION_SUMMARY alternatives.

## Next action
On PASS: preregister a separate scenario-aware cross-family composition/completeness geometry gate with explicit treatment of blocked/retired intervals and uncovered support. On BLOCKED missing-family: freeze a child primary-authority audit for that family before any numerical contour extraction.

Readiness changes only for a reproducible scientific closure; documentation volume alone earns no credit.
