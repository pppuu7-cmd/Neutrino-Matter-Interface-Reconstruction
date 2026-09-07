# NMIR prereg 0082a — B-L stellar/SN semantic and scope authority

Date frozen: 2026-09-08
Status: **PROSPECTIVE / NO 0082a FIGURE-CAPTION OR SCOPE RESULT INSPECTED**
Parent: 0082 `PASS_B_L_STELLAR_SN_PRIMARY_SOURCE_ASSET_AUTHORITY`.

## Question
Using only the exact versioned primary source archives already authorized by 0082, can we determine reproducibly which source-native figure asset(s) actually carry each paper's `U(1)_{B-L}` stellar/SN exclusion or bound, what mass/coupling convention those figures use, what physical observable each curve family represents, and the exact limited revision relation of Shin–Yun 2022 to earlier SN1987A work — without reading numerical contour geometry or choosing curves by visual appearance?

## Frozen source authority
Use exactly:
1. Hong–Shin–Yun `2012.05427v3`, archive SHA256 `6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc`.
2. Cerdeño et al. `2106.11660v3`, archive SHA256 `f70c812c983fbe911e9a298ed7dd2a06d8199a13b5d9b0500633d014af65de5d`.
3. Shin–Yun `2110.03362v2`, archive SHA256 `7af77fa64e46b53e901f88e3a8ef118effcb598dcd505e16e16d3aa31ab049bd`.

Only TeX/source text and source-native files from those exact archives are authority. 0082 candidate asset inventories may be used only to verify file identity; they do not by themselves select a scientific curve.

## Frozen deterministic semantic audit
For every source:
1. Parse complete TeX `figure`/`figure*` environments and pair every `\\includegraphics{...}` token with the caption and label in the **same environment**. Resolve the token to an exact archive member.
2. A figure is a `B-L constraint figure` only if its source-native caption or immediately associated source text explicitly contains a B-L/U(1)B-L identity **and** at least one constraint/bound/exclusion semantic token. Asset filename alone is insufficient.
3. Classify every accepted figure by source-native physical-scope tokens, without importing scope from another paper: `SN1987A`, `NS1987A`, `Cas_A`, `young_neutron_star_cooling`, `medium_effects`, `transverse`, `longitudinal`, `global_summary/other_constraints`.
4. Preserve all accepted B-L constraint figures when they encode distinct physical scopes. Do not force a single controlling asset if the source itself uses multiple observable-specific constraint figures.
5. Reject an asset from scientific-control status if its associated caption is only a diagram, cooling history, spectrum, hint/preference region, or generic model illustration without constraint/bound/exclusion semantics.

## Frozen parameter-convention audit
For every source, search source-native text/equations near model-definition and constraint sections for:
- the B-L gauge coupling symbol/convention;
- mediator/gauge-boson mass symbol and units/convention;
- any explicit rescaling or relation between the plotted coupling and a differently named parameter.

`PASS_PARAMETER_CONVENTION` requires a source-native, internally consistent mapping to a mass variable and a B-L coupling variable. It is acceptable for symbols to differ between papers; no cross-paper numerical conversion may be invented in 0082a. If the source defines a coupling through another parameter, preserve the exact definition for a later conversion gate.

## Frozen Shin–Yun revision/supersession rule
The later source may authorize **only** the scope it explicitly states it revisits, strengthens, replaces, corrects or newly adds.

Machine-audit body-text windows containing `revisit/reconsider/improve/stronger/previous/earlier` together with B-L and SN/NS context. Record whether source-native text explicitly establishes:
- revised SN1987A transverse bound;
- newly excluded longitudinal region;
- revision/replacement of NS1987A or young-neutron-star cooling bounds;
- revision/replacement of Cas A bounds.

Absence of an explicit replacement statement **cannot** be converted into a supersession claim. Thus if only SN1987A revision is explicitly supported, later composition may update only that branch while retaining Hong young-NS/Cas-A authority as a separate candidate family.

## PASS
`PASS_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY` iff all of the following hold:
- all three exact source hashes match 0082 authority;
- every source has at least one source-native B-L constraint figure with deterministic same-environment caption/include identity;
- each accepted figure has a nonempty source-native scope classification;
- each source has `PASS_PARAMETER_CONVENTION`;
- Shin–Yun revision semantics explicitly establish at least the SN1987A revision plus transverse/longitudinal scope required by 0082, with broader supersession claims left false unless explicitly sourced.

## PARTIAL / BLOCKED
- `PASS_PARTIAL_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY`: source/parameter semantics are secured but one source has multiple scientifically plausible same-scope constraint assets that cannot be deterministically disambiguated before vector inspection; preserve all candidates and do not select by appearance.
- `BLOCKED_B_L_STELLAR_SN_SEMANTIC_SCOPE_AUTHORITY`: a source lacks source-native B-L constraint caption/body identity, lacks a recoverable mass/coupling convention, or the Shin–Yun revision scope cannot be tied to B-L/SN semantics.
- Parser/archive/network/dependency failures are infrastructure failures, never scientific BLOCKED.

## Guards
- No PDF drawing/path/color inspection in 0082a.
- No axis pixel-coordinate calibration or numerical contour extraction.
- No manual/raster digitization or point picking.
- No cross-paper union/intersection.
- No automatic replacement of Hong young-NS/Cas-A by Shin–Yun.
- No conversion between coupling conventions unless explicitly source-defined and separately audited later.
- No global B-L envelope or BSM response/enhancement scan.

## Next action
- PASS -> separately preregister 0082b vector-integrity + axis/curve identity gate for the source-authorized constraint assets, preserving distinct SN1987A vs young-NS/Cas-A branches.
- PARTIAL -> 0082b may inspect all retained same-scope vector candidates but may not choose one based on desired geometry.
- BLOCKED -> retire only the affected source/scope branch and continue the remaining 0071 external families.

`NMIR_READINESS` remains 94% unless 0082a closes a genuinely material semantic ambiguity; no excluded area is added here.
