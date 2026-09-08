# NMIR iteration 0086a — B-L collider/fixed-target primary-authority audit

Date: 2026-09-08
Prospective contract: `research/prereg/0086a_b_minus_l_collider_fixed_target_primary_authority.md`, frozen commit `7e1305e67c40bd7b3cc2fadf08fca508380dc306` before source classification.
Final classification: **PASS_B_L_COLLIDER_FIXED_TARGET_PRIMARY_AUTHORITY**
`NMIR_READINESS: 98%`.

## Scientific question
Can the mandatory 0071 collider/fixed-target family be anchored to a primary source that explicitly constrains the same gauged U(1)_{B-L} benchmark, with coupling and decay/scenario assumptions stated strongly enough to support a separately preregistered numerical-materialization audit?

## Primary authority
A new primary source, later than the older NMIR ledger work, satisfies the authority requirement:

NA64 Collaboration, **“Improved limits on a new Z' in B-L scenarios with the NA64 experiment at CERN”**, arXiv `2606.17320v2`, submitted 2026-06-15 and revised 2026-06-30, report `CERN-EP-2026-166`.

Stable primary URL frozen in `data/na64_b_minus_l_primary_authority_0086a.json`.

The primary source explicitly studies U(1)_{B-L}, uses the full 2016–2022 NA64 electron dataset `(9.4 +/- 0.5)e11` electrons on target, and reports new constraints on the B-L coupling from fixed-target missing-energy production. It discusses electron-nucleus production and resonant e+e- annihilation, with enhanced sensitivity around the 200–300 MeV region.

## Coupling-convention authority
The source explicitly defines its B-L interaction and gives

`g_{Z'} = g_{B-L} = sqrt(4*pi*alpha_{B-L})`.

Under the NMIR 0071 convention

`L_int = g_BL V_mu J_{B-L}^mu`

with the standard B-L current, the source coupling is therefore directly the NMIR coupling:

`g_BL = g_{B-L} = g_{Z'}`.

No electric-charge analogy or post-result epsilon conversion is needed. Where the paper discusses a dark-photon production mapping, it itself states the relevant replacement `epsilon e -> g_{B-L}`; that source statement is not generalized beyond its stated production context.

## Decay/scenario authority
The source makes the invisible-width assumptions scientifically material rather than optional bookkeeping:
- anomaly cancellation requires right-handed-neutrino content;
- the unbroken B-L benchmark has Dirac neutrinos and three light right-handed neutrinos;
- below the e+e- threshold the mediator decays predominantly invisibly to neutrinos;
- broken/Majorana or other right-handed-neutrino realizations can change the invisible branching fraction;
- a dark-sector invisible benchmark is treated separately.

Therefore a child numerical gate must preserve source scenarios separately. It may not post-hoc choose the strongest visible/invisible branch or silently suppress right-handed-neutrino assumptions.

## Why this is a PASS but not yet a contour PASS
0086a freezes the missing mandatory family to an explicit primary same-convention B-L constraint. This closes the authority hole found by 0086.

However 0086a intentionally does **not** claim a numerical excluded polygon/curve. Exact source-native numerical/vector assets, confidence-level contour semantics, and reproducible geometry have not yet been audited under the no-raster/manual rule. Those are result-dependent and require a new prospective child contract.

Machine-readable authority ledger: `data/na64_b_minus_l_primary_authority_0086a.json`, commit `11c4fed171bcd18e433ca5d8c64f4c805418718f`.

## Scientific consequence
All five original 0071 families now have at least primary authority or an explicit scoped blocker/retirement in the repository. This does **not** yet authorize cross-family composition because the newly restored collider/fixed-target family lacks materialized numerical geometry.

The exact next gate is therefore a source-asset/materialization audit for the NA64 2026 B-L result, prospectively frozen before inspecting/extracting any numerical contour geometry.

## Readiness
`NMIR_READINESS` remains **98%**. Closing the missing family authority is substantive, but no new reproducible numerical exclusion object has yet been materialized.

## Guards
No raster/OCR/manual contour extraction. No generic dark-photon contour promoted to B-L without source mapping. No visible/invisible or Dirac/Majorana/right-handed-neutrino scenario union. No cross-family B-L union. No BSM response/enhancement scan.
