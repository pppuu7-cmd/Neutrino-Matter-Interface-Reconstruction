# NMIR amendment 0087d — starred `includegraphics` parser conformance

Date: 2026-09-08

## Trigger
The first hosted 0087d scientific run `34180767007` returned `BLOCKED_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY` with `candidate_BL_mass_figures=[]`.

A subsequent **infrastructure-only source-semantic diagnostic** (`34180982609`) inspected only exact TeX captions / includegraphics syntax from the same frozen arXiv `2008.05022v3` archive. It did not inspect figure coordinates, axes, ticks, paths, y values, likelihoods or numerical mass support.

The diagnostic established that the exact source contains the B-L constraints figure environment with source caption semantics:
- excluded regions in the `M_{Z'}-g_{Z'}` plane for the `B-L` model;
- COHERENT Ar, CsI and combined constraints;
- source assets `Coherent_Results_B-L.pdf` and `Comparison_B-L.pdf`.

The source invokes those assets with standard LaTeX starred syntax:

`\includegraphics*[...]{...}`

The base 0087d regex accepted only `\includegraphics[...]` and therefore returned an empty graphics list even though the frozen semantic figure condition was satisfied.

## Classification of the first run
The zero-candidate result of run `34180767007` is reclassified as:

`INFRASTRUCTURE_FAIL_SOURCE_FIGURE_PARSER_CONFORMANCE`

It is **not** an authoritative scientific BLOCKED result.

## Allowed repair
Only figure-asset invocation parsing may change:
- accept both `\includegraphics{...}` and `\includegraphics*{...}`;
- retain the same optional argument handling and exact archive-relative asset resolution;
- retain all frozen semantic qualification, mass-axis, tick-count, no-sign-synthesis, fit residual, frame, cross-route and threat-comparison criteria;
- no figure coordinates or numerical mass endpoints were inspected before this repair.

No scientific threshold, source identity, target interval, PASS/BLOCKED/FAIL consequence or guard changes.

## Guard
No likelihood evaluation. No 0074c reopening. No y calibration. No curve/path/color/legend identity. No raster/OCR/manual digitization. No visual sign recovery. No post-result mass-range tuning.
