# NMIR prereg 0087d — COHERENT B-L mass-support-only authority

Date: 2026-09-08

## Motivation
Iteration 0087b identifies the robust low-mass partial-topology target

`6.845530367110015e-6 <= m_V <= 1.4057345497828417 eV`

at the inward stress ceiling `log10(g_BL)=-5`.

COHERENT remains `UNRESOLVED_MASS_SUPPORT_THREAT`. Iteration 0074c blocks an independently reconstructed **combined CsI+Ar likelihood** because the permitted primary routes do not supply a non-circular external numerical combined-likelihood benchmark. That blocker does not by itself answer the narrower question of the mediator-mass support actually authorized by the primary B-L analysis.

0087d therefore asks for mass support only. It must not evaluate a B-L likelihood, reproduce a contour, infer a coupling boundary, or weaken 0074c.

## Frozen primary identity
- Cadeddu et al., JHEP 01 (2021) 116;
- arXiv `2008.05022v3` exact version;
- source URL: `https://export.arxiv.org/e-print/2008.05022v3`;
- the fetched archive SHA256 and every candidate figure SHA256 must be recorded in the hosted artifact before any result is promoted;
- the source must internally match the Cadeddu COHERENT CsI+Ar B-L analysis semantics already frozen in 0074/0074c. A mismatched source version is an input-authority blocker.

The exact arXiv version identifier is the frozen source identity. No later paper/version may be silently substituted.

## Scientific question
Does the primary Cadeddu source uniquely certify a finite mediator-mass support interval for its B-L COHERENT analysis, and if so is that interval mass-disjoint from the 0087b robust low-mass target?

## Frozen authority routes
Evaluate both routes independently and report their outcomes.

### Route A — explicit source-text B-L mass/scan interval
After TeX comment stripping, identify text or figure-caption contexts that simultaneously contain B-L/B−L semantics and the mediator mass symbol (`M_Z'`, `M_{Z'}`, equivalent source-native notation) or an unambiguous phrase such as `mediator mass`/`Z' mass`.

PASS_A requires a unique finite positive interval with both numerical endpoints and physical mass units explicitly attached or unambiguously shared by a syntactic range expression. Allowed examples include explicit `from ... to ...`, `between ... and ...`, `a < M_Z' < b`, or a finite plotted/scanned range stated in the caption/text.

Forbidden:
- deriving an endpoint from qualitative words only;
- using a benchmark point as an endpoint;
- inferring the scan range from detector recoil support;
- importing a secondary review range;
- interpreting `M_Z' -> 0` as a finite lower endpoint.

### Route B — source-native B-L figure x-axis/frame authority
If the TeX source contains a figure environment whose caption/text explicitly identifies the B-L coupling-versus-mediator-mass constraints, resolve its `includegraphics` asset from the same exact archive.

Route B may use only source-native text spans and vector frame geometry of that figure. It may not use curve paths/colors/legend identities or y-axis values.

Frozen acceptance:
1. the figure asset must be vector-native (PDF/EPS/SVG-like source) or otherwise expose machine-readable text anchors; raster-only figures are BLOCKED for Route B;
2. x-axis identity must explicitly be mediator mass with a physical unit;
3. at least 3 distinct major x tick anchors must be reconstructed from source-native text, spanning at least 2 decades;
4. no missing sign or exponent may be synthesized from vector strokes or visual inspection;
5. a linear log-axis fit must have positive slope and max residual <=0.015 decade;
6. the outer accepted major ticks must coincide with a unique scientific plot-frame x extent within 1.5 source coordinate units, or the caption/source text must explicitly state that the plotted range terminates at those endpoints;
7. the finite mass support is exactly the two source-authorized outer endpoints; no extrapolation beyond the frame.

If several B-L figures exist, only a figure/caption explicitly corresponding to the Cadeddu CsI+Ar constraint analysis may be used. Multiple incompatible qualifying intervals => BLOCKED, not visual selection.

## Cross-route consistency
If A and B both PASS, their endpoints must agree within 0.03 decade per endpoint. Larger disagreement is `SCIENTIFIC_FAIL_COHERENT_MASS_SUPPORT_SOURCE_INCONSISTENCY`. If only one route passes, that route may independently authorize the interval.

## Frozen threat comparison
For certified COHERENT interval `[a,b]` and target `[t0,t1] = [6.845530367110015e-6, 1.4057345497828417] eV`:
- `PROVABLY_MASS_DISJOINT` iff `b < t0` or `a > t1`;
- otherwise `MASS_OVERLAP_THREAT`, including endpoint contact.

Report logarithmic separation for disjoint intervals or logarithmic overlap width/fraction for overlap.

## Classification
- `PASS_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY` if at least one frozen source-native route uniquely certifies the finite interval, all passing routes are mutually consistent, and the threat comparison is computed.
- `BLOCKED_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY` if no route can uniquely certify a finite interval under the frozen rules.
- `SCIENTIFIC_FAIL_COHERENT_MASS_SUPPORT_SOURCE_INCONSISTENCY` only if independently authoritative routes contradict.
- source download/archive/parser/test failures before scientific evaluation are infrastructure failures.

## Guards
No B-L likelihood evaluation. No combined-likelihood validation claim. No weakening or reopening of 0074c. No benchmark interpolation. No y-axis calibration. No curve/path/color/legend identity. No raster/OCR/manual digitization. No visual sign recovery. No global B-L allowed-region claim. No BSM response/enhancement scan.
