# Preregistration 0079 — B-L long-range/fifth-force primary authority audit

Date frozen: 2026-09-07
Parent: 0078c `PASS_SOLAR_CEVNS_B_L_EXCLUDED_REGION / PASS_PARTIAL_B_L_EXTERNAL_ENVELOPE`, immutable commit `7fb6cee3ad6f6129d04cc12d00a319096498db6a`.

## Scientific question

Can the low-mass B-L fifth-force family required by the global 0071 envelope be supplied by a primary, reproducible authority with an exact convention map into NMIR `(m_V,g_BL)` and an explicit excluded-side/range-of-validity statement, without reviving unresolved Wagner curve semantics or reading a raster plot manually?

0079 is an **authority/materialization audit only**. It must not publish a new `(m_V,g_BL)` limit until the exact conversion and finite-range applicability are frozen from primary source text/equations.

## Frozen primary sources

Audit these primary sources in this order:

1. Pierre Fayet, *MICROSCOPE limits on the strength of a new force, with comparisons to gravity and electromagnetism*, Phys. Rev. D 99, 055043 (2019), arXiv:`1809.04991v2`, DOI `10.1103/PhysRevD.99.055043`.
2. Pierre Fayet, *MICROSCOPE limits for new long-range forces and implications for unified theories*, arXiv:`1712.00856` (published version if source metadata identifies it unambiguously).

The frozen 0071 ledger already identifies the MICROSCOPE/Fayet family as relevant long-range B-L authority. Reviews/secondary summaries may locate files but may not supply the scientific mapping.

## Frozen source facts to verify before calculation

The source audit must extract from primary source bytes/text, not from memory or secondary prose:

- exact definition of the B-L interaction coefficient (`epsilon_{B-L}`, `alpha_g`/`bar alpha_g`, or equivalent);
- whether the quoted limit is on a signed coupling, absolute coupling, squared force strength, or force relative to gravity;
- confidence convention (e.g. 2 sigma) and whether statistical/systematic errors are already combined;
- the exact relation among `epsilon_{B-L}`, electric charge `e`, `alpha_g`/`bar alpha_g`, and source/test-body B-L charges;
- whether in the paper's convention an NMIR gauge interaction `g_BL (B-L)` maps exactly to `g_BL = e * |epsilon_{B-L}|`, or whether an additional normalization factor is present;
- physical range assumption behind the quoted MICROSCOPE bound and any explicit Yukawa-range/mass dependence supplied by the primary source;
- whether the source gives a numerical finite-range curve/table/formula, or only a strictly long-range/asymptotic bound.

No numerical conversion into `g_BL` may be committed before all applicable items above are resolved.

## Frozen provenance procedure

1. obtain the exact primary arXiv source archive/PDF for the frozen version and record byte size + SHA256;
2. persist a machine-readable authority ledger containing the exact source identifiers/hashes and verbatim equation/section identifiers (brief quotations only where needed; otherwise formula transcription);
3. if the source contains author numerical tables/code, hash-pin them;
4. if it contains a vector finite-range plot, audit vector/raster integrity before any coordinate extraction under a separately frozen subgate;
5. if it contains only an analytic asymptotic long-range limit, record that scope exactly and do not extrapolate it to arbitrary mediator mass.

## Frozen classifications

- `PASS_FIFTH_FORCE_B_L_ASYMPTOTIC_AUTHORITY`: exact primary coupling/convention/CL/range authority is sufficient to materialize a **strictly long-range/asymptotic** B-L limit in a later preregistered calculation, but no finite-mass contour is supplied.
- `PASS_FIFTH_FORCE_B_L_FINITE_RANGE_AUTHORITY`: additionally, a reproducible primary numerical/vector/analytic Yukawa-range dependence exists and is sufficient for a separately preregistered finite-mass materialization.
- `PARTIAL_FIFTH_FORCE_AUTHORITY`: primary source improves provenance but at least one mandatory convention or range item remains unresolved; no new B-L numerical limit is authorized.
- `SCIENTIFIC_FAIL_FIFTH_FORCE_AUTHORITY`: primary source contradicts the assumed B-L mapping or lacks a usable B-L constraint in the audited scope after successful access.
- `INFRASTRUCTURE_FAIL`: primary source cannot be obtained/parsed before scientific inspection.

## Decision tree

- `PASS_FIFTH_FORCE_B_L_FINITE_RANGE_AUTHORITY` -> freeze 0079a finite-range `(m_V,g_BL)` materialization with exact source hashes, formulas/axes, units, side authority and pre-result tolerances.
- `PASS_FIFTH_FORCE_B_L_ASYMPTOTIC_AUTHORITY` -> freeze 0079a only for the asymptotic domain explicitly supported by the source; do not invent a Yukawa turn-off. Then continue searching a separate finite-range primary family for the global envelope.
- PARTIAL/FAIL -> do not convert or extrapolate; return to another 0071 required family (stellar/SN or cosmology) rather than relaxing this gate.

## Guards

No raster/manual contour reading. No post-result convention factor. No assumption that `above a line` is excluded unless primary semantics say so. No use of unresolved Wagner blue-family identities. No BSM response/enhancement calculation in 0079.

## Readiness

Freezing 0079 does not change readiness. `NMIR_READINESS` remains 92% until a reproducible scientific gate closes.