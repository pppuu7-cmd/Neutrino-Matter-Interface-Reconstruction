# NMIR iteration 0072a — Wagner primary vector source materialization

Date: 2026-09-07
Parent gate: 0072 reproducible U(1)_{B-L} contour materialization.
Prospective amendment: `research/prereg/0072a_wagner_vector_extraction_amendment.md`, frozen before any contour coordinate was accepted.
Classification: **IN_PROGRESS_0072A / PRIMARY_VECTOR_ASSET_FOUND / CALIBRATION_OPEN**.

## Recovery and no-duplication check
The mandatory recovery chain was read before work. The latest 0072 route audit still had `PRIMARY_CONTOURS_MATERIALIZED=0`. Relevant Actions were inspected and no running scientific contour extraction was duplicated. Baseline green CI is treated only as infrastructure evidence.

## Primary source asset materially recovered
Wagner et al. arXiv:1207.2442 was fetched through the primary arXiv source-archive route. The source archive is a tar.gz of 2,733,483 bytes with SHA256

`c1fd33d880b5810ede631284ddb91738d5df8e1816c3f47f4bef58a9eaa4e6e3`.

It contains a true vector Figure-6 asset:

`WEP_figure6.eps`, 581,517 bytes, SHA256
`4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882`.

Therefore the earlier apparent raster-only blocker is retired. The raster HTML rendering remains forbidden; the EPS is the primary extraction authority.

## Prospective extraction contract
Before accepting any contour coordinates, amendment 0072a froze direct EPS parsing, logarithmic axis calibration from vector tick geometry plus printed source tick labels, maximum tick back-projection residual `2e-3` decades, exact preservation of named EW/EW94/EW99/Princeton/Moscow/LLR curves, fail-closed classification, and the already-frozen conversions

`|g_BL| = 2.70463357586823e-19*sqrt(|alpha_tilde|)`

and

`m_V[eV] = 1.973269804e-7/lambda[m]`.

No raster/manual point reading and no secondary contour authority are allowed.

## Reproducible tooling and parser hardening
Added:
- `scripts/materialize_wagner_source_0072.py` — source archive/member hashing and vector-asset discovery;
- `scripts/probe_wagner_eps_0072.py` — non-numerical EPS structure probe;
- `scripts/summarize_wagner_eps_paths_0072.py` — tiny fail-closed GRAF-EPS path interpreter;
- `scripts/summarize_wagner_geometry_0072.py` — compact color/panel geometry diagnostic;
- `.github/workflows/b-minus-l-wagner-source-audit.yml` — hosted reproducible source/geometry audit;
- `tests/test_wagner_eps_tokenizer_0072.py` — regression tests preventing comment/text letters from becoming PostScript drawing operators.

The first path parser result exposed an operand-stack contamination bug caused by nuisance PostScript operators. No scientific contour was accepted from that result. The parser was corrected and regression-tested before continuing.

## Hosted raw evidence
Hosted source/geometry audit run/job:

`34108986146 / 101700546328`

completed the materialization, raw-result display, repository persistence and artifact upload steps. Scientific use is based on the persisted raw JSON under the frozen contract, not on the green status.

Artifact:

`10013548194`

digest:

`sha256:d96bc23c4fd74161867259fe6a2f4b4dc79f83529b275919ca16201668da4cb8`.

## Corrected primary vector geometry
The corrected parser (`parser_version=1.3`) reproduces the same EPS SHA256 and resolves actual GRAF vector geometry. Examples:
- black axis/frame geometry has bbox `[0.885,0.169,11.931,4.844]`;
- an explicit right-panel bottom frame is the black segment `x=6.931..11.931` at `y=0.844`, with regularly spaced vector ticks;
- the pale-yellow right-panel fill is a genuine path with bbox `[6.931,1.066,11.931,4.844]`;
- the pale-yellow left-panel fill is a genuine path with bbox `[1.836,1.163,6.681,4.844]`;
- red and magenta left-panel exclusion candidates are represented as sequential 2-point vector segments, as expected for GRAF EPS output;
- blue/orange/pale-yellow geometry spans both panels and must not be identified by color alone.

These are structural facts only. No EPS coordinate has yet been converted to a scientific `(lambda, alpha_tilde)` contour point.

## Scientific status
**Closed inside 0072a:** the primary-vector-source availability question. Wagner Figure 6 is not limited to an unusable raster; a hash-pinned vector EPS exists and is reproducibly materialized.

**Still open inside 0072a:** deterministic left-panel axis calibration, named-curve identity/chaining, and validation against the frozen `2e-3`-decade criterion. Therefore `PRIMARY_CONTOURS_MATERIALIZED` remains 0 and there is no B-L global allowed region yet.

## Exact next action
1. Parse black frame/tick vectors to infer both panel boxes and all major tick coordinates.
2. Freeze the exact printed primary Figure-6 major tick values before any coordinate transform.
3. Fit the two log-axis maps and require the frozen residual tolerance.
4. Chain same-color sequential left-panel segments by exact endpoint continuity while excluding glyph/axis geometry.
5. Validate curve identity and exclusion sense, then emit the first primary machine-readable Wagner `(m_V,g_BL)` contour only if every 0072a criterion passes.

If the axis/curve identity is ambiguous, classify `SCIENTIFIC_FAIL_VECTOR_CALIBRATION` and move to the already-frozen independent PandaX/De-Romeri likelihood reproduction route. No manual raster digitization is permitted.

## Readiness
No readiness increase. This is a reproducible materialization advance, but the physical B-L exclusion contour is not yet frozen.
