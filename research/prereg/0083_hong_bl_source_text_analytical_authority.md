# NMIR prereg 0083 — Hong–Shin–Yun B-L source-text analytical authority

Date frozen: 2026-09-08
Status: **PROSPECTIVE FOR MACHINE MATERIALIZATION; ABSTRACT-LEVEL LOW-MASS BOUND ALREADY PUBLICLY VISIBLE**
Parent: 0082c `BLOCKED_CERDENO_B_L_AXIS_CALIBRATION`.

## Frozen authority
Use only Hong, Shin & Yun, arXiv `2012.05427v3`, source archive SHA256 `6daae1b2d8491cb294a90ecb23d3bcee27c1a8b9dfe5674c2d47e12d735d24bc`.

The paper's public abstract already states an approximate low-mass B-L result (`e' < 10^-13` for gauge-boson mass below `O(0.1) MeV`). 0083 does **not** pretend that statement is an unseen numerical discovery. The prospective question is narrower and reproducibility-critical: can the exact source TeX authorize a machine-materializable analytical bound and, separately, an exact finite-mass domain without reading figure geometry?

## Frozen semantics
- Model: `U(1)_{B-L}` gauge boson.
- Source-native coupling symbol: `e'`; no conversion factor to another B-L convention may be introduced in 0083.
- Physical scope: young-neutron-star cooling in the source's own Cas A / SN1987A discussion. No blanket supersession by Shin–Yun 2022 is assumed; 0082a's scope guard remains controlling.
- This gate audits source text only. It does not combine Cas A and SN1987A into one global likelihood or union.

## Source-text extraction
1. Fetch the exact frozen arXiv source archive and verify SHA256 before inspection.
2. Inspect only source-native `.tex` files and their textual equation/caption content. Bibliography text is not numerical authority.
3. Normalize LaTeX spacing/macros only enough to search for B-L semantics, coupling inequalities, mass inequalities/domains and explicit cooling/source labels. Preserve the original matched source excerpts in the machine-readable result.
4. Figure pixels, raster/OCR, PDF path geometry, manual reading and cross-paper values are forbidden.

## Frozen classifications
### A. Analytical low-mass anchor
`PASS_HONG_B_L_SOURCE_TEXT_ANALYTICAL_ANCHOR` requires exact source text that jointly establishes:
- explicit `U(1)_{B-L}` / B-L semantics;
- an explicit upper bound on source-native coupling `e'` with a numerical value;
- a stated low-mass applicability domain in the same source discussion;
- enough context to identify the bound as a cooling constraint/result rather than a benchmark input or citation to another paper.

The low-mass domain may be approximate (e.g. `O(...)`) for **anchor-only** status. An approximate endpoint is not an exact polygon coordinate.

### B. Exact finite-mass materialization authority
`PASS_HONG_B_L_EXACT_FINITE_MASS_TEXT_AUTHORITY` additionally requires source text with a finite numerical mass boundary expressed as an actual inequality/equality/range for the B-L bound, not only `O(...)`, `~`, `approximately`, `about`, or a figure-only statement. The same source text must make the allowed/excluded coupling side unambiguous.

If A passes but B does not, classify:
`PASS_HONG_B_L_SOURCE_TEXT_ANALYTICAL_ANCHOR / BLOCKED_HONG_B_L_EXACT_FINITE_MASS_TEXT_AUTHORITY`.

If the source cannot even satisfy A, classify `BLOCKED_HONG_B_L_SOURCE_TEXT_ANALYTICAL_AUTHORITY`.

A textual contradiction between explicit source equations/statements under the same stated scope is `SCIENTIFIC_FAIL_HONG_B_L_SOURCE_TEXT_AUTHORITY`; parser/network/archive problems are infrastructure failures.

## No post-result rescue
Do not replace `O(0.1 MeV)` by `0.1 MeV`, choose a conservative endpoint after seeing the text, infer a mass edge from a plot, import Shin–Yun 2022 numbers, or reinterpret `e'` as another coupling convention. Any exact geometry later requires its own prospective contract.

## Consequence
- A+B PASS -> preregister a separate exact text-derived finite-mass excluded-geometry materialization gate.
- A PASS / B BLOCKED -> record only a source-qualified analytical/asymptotic low-mass anchor; do not assign excluded area; then audit Shin–Yun 2022 source text for exact revised SN1987A/NS1987A numerical authority or another missing 0071 family.
- A BLOCKED/FAIL -> retire Hong source-text numeric materialization and advance to another primary family.

`NMIR_READINESS: 94%` until a new reproducible excluded region or comparably material uncertainty class is closed.
