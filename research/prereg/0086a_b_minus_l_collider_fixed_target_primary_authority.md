# NMIR preregistration 0086a — B-L collider/fixed-target primary-authority audit

Date frozen: 2026-09-08
Status: PROSPECTIVE
Parent: iteration 0086 `BLOCKED_B_L_EXTERNAL_FAMILY_MISSING_COLLIDER_FIXED_TARGET`.

## Scientific question
Can the mandatory 0071 collider/fixed-target visible/invisible family be closed with primary, same-convention U(1)_{B-L} authority over any nonzero part of `1e-6 eV <= m_V <= 10 GeV`, without importing a generic dark-photon contour through an unproven coupling/branching-ratio map?

## Scope
This is an authority/discovery gate, not a contour extraction gate. Identify a minimal set of primary experimental or primary phenomenology sources that explicitly constrain gauged B-L (or provide an exact model mapping sufficient to do so), and freeze:
- exact citation/version/date/source bytes or stable primary URL;
- interaction convention and mapping to `L_int = g_BL V_mu J_{B-L}^mu`;
- visible/invisible decay assumptions, including neutrino and any right-handed-neutrino channels where relevant;
- mass support and confidence-level semantics;
- excluded side/band semantics;
- whether numerical source-native data/code/vector geometry exist for reproducible materialization.

Do not materialize a final exclusion contour in 0086a; any numerical extraction requires a child preregistration after source/convention authority passes.

## Candidate-source rule
Search primary literature/official experiment releases directly. Reviews and global summary plots may be used only to discover primary citations, never as contour authority. Generic dark-photon limits count only if the source itself or a separately frozen exact derivation establishes production and decay mapping for B-L under stated assumptions.

## Acceptance criteria
`PASS_B_L_COLLIDER_FIXED_TARGET_PRIMARY_AUTHORITY` if at least one primary source supplies an explicit B-L constraint with exact coupling/decay assumptions and enough source-native information to support a prospectively defined child materialization gate over nonzero mass support.

`PASS_B_L_COLLIDER_FIXED_TARGET_ANALYTICAL_BOUND_AUTHORITY` if the source gives exact/tabulated analytical or pointwise limits directly in B-L convention even without vector contour assets.

`BLOCKED_B_L_COLLIDER_FIXED_TARGET_NUMERICAL_MATERIALIZATION` if explicit primary B-L limits exist but source-native numerical/analytical geometry is insufficient under the no-raster/manual rule.

`BLOCKED_B_L_COLLIDER_FIXED_TARGET_MODEL_MAPPING` if only generic dark-photon/vector limits are available and an exact B-L production/decay mapping cannot be frozen from primary authority.

## Guards
No raster/OCR/manual digitization. No review contour as authority. No epsilon->g_BL substitution by electric-charge analogy alone. No neglect of B-L neutrino decays or right-handed-neutrino assumptions. No post-result choice of visible/invisible branch. No cross-family union or BSM response calculation.

## Next action
On PASS: prospectively freeze 0086b for exact numerical/analytical materialization of the strongest source-authorized collider/fixed-target object(s), preserving distinct decay/scenario assumptions. On BLOCKED: record exact missing authority and return to the remaining funnel without silently treating the family as constrained.
