# NMIR preregistration 0087f — localized B-L BBN-tail actionability authority

Date frozen: 2026-09-08
Status: PROSPECTIVE — frozen before any new BBN tail result-dependent extraction or calculation.

## Scientific question

Can the accepted primary Esseili–Kribs authority resolve whether the already localized BBN family can exclude or allow the **entire** remaining 0087b high-mass tail of the robust low-mass candidate,

`1.0 <= m_V <= 1.4057345497828417 eV`,

without reopening the blocked 0081a vector-calibration/threshold-identity route under weaker criteria and without borrowing the CMB calibration?

This is an actionability/completeness gate only. It is not a global B-L recomposition and does not authorize a BSM response/enhancement scan.

## Frozen provenance

Primary source:
- Esseili–Kribs `arXiv:2308.07955v2` source archive SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`.

Source-native BBN vector assets already validated in 0081a:
- Majorana Fig.7 `Presentation/CnstrntPlotMajoranaYp.pdf`, SHA256 `4326f3ac9ba29e515aa22afafef27d08c05d0e6be04db605c4706418c6cd8926`;
- Dirac Fig.8 `Presentation/CnstrntPlotDiracYp.pdf`, SHA256 `14d9afe16f4c38f1d3c08f97ccf086a570739b18731b0b6ffee97fe4b9e63b15`.

Accepted semantics from 0081:

`Delta Y_p = Y_p(BSM) - Y_p(SM) = 0.008` at 95% C.L., signed rather than absolute-value semantics.

Accepted 0081a blocker:
- only two source-native labeled x major anchors (`0.1`, `1`) were independently machine recoverable;
- no unique source-native vector identity for the `Delta Y_p=0.008` threshold survived the frozen identity rules;
- therefore no BBN polygon or borrowed CMB transform is authorized.

Accepted 0087b target/tail:
- full conservative target mass envelope: `6.845530367110015e-6 .. 1.4057345497828417 eV`;
- BBN mass-support overlap: `1.0 .. 1.4057345497828417 eV`;
- overlap width: `0.1479033189422942 decade`;
- overlap fraction of target log-width: `0.027840644564136232` = `2.7840644564136232%`.

Majorana and Dirac remain separate physical scenarios. No union/intersection or post-hoc selection of the stronger scenario is allowed.

## Allowed authority routes

The routes below are evaluated independently and in order. The gate may PASS only through source-authorized information that spans the **entire** frozen tail for the relevant scenario.

### Route A — exact analytical/textual BBN coupling authority

PASS-capable only if the exact primary source gives an analytical relation, numerical coupling bound/function, or equivalent exact statement whose domain explicitly covers the entire `1.0 .. 1.4057345497828417 eV` tail and whose semantics are sufficient to determine the `Delta Y_p=0.008` allowed/excluded side for Majorana and/or Dirac without using plot geometry.

A qualitative sentence, isolated benchmark, asymptotic statement, or mass-only support is insufficient.

### Route B — machine-readable numerical table/data authority

PASS-capable only if exact primary source bytes contain machine-readable numerical data covering the entire frozen tail, with unique mass and coupling values tied unambiguously to `Delta Y_p=0.008` and to the Majorana/Dirac scenario identity.

Interpolation is allowed only inside a source-provided ordered table that brackets the full tail; no extrapolation beyond source points is allowed. Any interpolation rule must be frozen before evaluation and use the source's stated axis variables/units.

### Route C — genuinely new source-native vector authority

The already blocked 0081a route is **not** rerun with relaxed criteria. Route C can become actionable only if a genuinely new primary/source-native asset or metadata, absent from the accepted 0081a input set, independently supplies the missing x-axis calibration and unique `Delta Y_p=0.008` path identity while satisfying the unchanged 0081a criteria.

The CMB transform may not be borrowed. The x-anchor requirement may not be lowered. Color/adjacency tolerances may not be changed after inspection. Raster/OCR/manual digitization is forbidden.

If no genuinely new primary asset exists, Route C is classified blocked by inheritance from 0081a.

## Frozen classifications

### PASS

`PASS_BBN_TAIL_ACTIONABILITY_AUTHORITY`

Only if at least one allowed route supplies sufficient source-authorized coupling-side information over the **entire** `1.0 .. 1.4057345497828417 eV` tail for at least one separately identified cosmology scenario, so that a later preregistered topology-recomposition gate can determine whether that scenario's candidate tail survives or is excluded.

PASS does **not** itself modify the 0087 topology and does not authorize BSM scanning.

### BLOCKED

`BLOCKED_BBN_TAIL_ACTIONABILITY_AUTHORITY`

If primary authority establishes only mass support, isolated/partial benchmarks, qualitative behavior, or coupling information that does not cover the entire tail; or if coupling geometry remains dependent on the blocked 0081a vector route.

BLOCKED means the full 0087b candidate cannot be promoted to a complete global allowed component. The most that can later be certified from present missing-family knowledge is a topology statement restricted below `1 eV`, subject to the other already recorded family blockers. It is not a physical exclusion of the tail.

### SCIENTIFIC FAIL

`SCIENTIFIC_FAIL_BBN_TAIL_AUTHORITY_CONSISTENCY`

Only if exact primary-source evidence under the same definitions directly contradicts an accepted 0081/0087b authority statement. Parser misses, unavailable source bytes, archive corruption, dependency/runtime errors, or hashing failures are infrastructure failures, not scientific FAIL.

### INFRASTRUCTURE FAIL

Use an `INFRASTRUCTURE_FAIL_*` classification if exact frozen source bytes/hashes cannot be verified, extraction cannot be reproduced, or implementation/runtime errors prevent evaluating the frozen routes.

## Frozen guards

- no raster/OCR/manual digitization;
- no borrowing CMB axis calibration;
- no lowering the 0081a anchor-count requirement;
- no post-result color/style/path choice;
- no threshold reinterpretation away from signed `Delta Y_p=0.008` at 95% C.L.;
- no Majorana/Dirac union/intersection or strongest-case selection;
- no extrapolation from a partial BBN table/benchmark to the entire tail;
- no use of mass-support overlap alone as an exclusion statement;
- no global B-L allowed-region claim;
- no BSM response/enhancement scan.

## Next action frozen before result

If PASS: prospectively preregister a separate scenario-aware topology recomposition gate using only the newly authorized BBN tail object plus already accepted geometries.

If BLOCKED: preserve the unresolved BBN tail explicitly; do not promote the full candidate to a complete global B-L allowed region. Return to completeness/final-lock audit and, if useful, formulate only a restricted-below-1-eV statement whose scope is explicit. BSM remains locked.

If SCIENTIFIC FAIL: reconcile the contradicted authority before any further composition.
