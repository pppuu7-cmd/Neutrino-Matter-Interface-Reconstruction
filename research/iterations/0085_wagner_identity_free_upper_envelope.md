# NMIR iteration 0085 — Wagner identity-free B-L upper-bound envelope

Date: 2026-09-08
Prospective contract: `research/prereg/0085_wagner_identity_free_upper_envelope.md`, frozen commit `de4862e8c620a4782531bcb8d994bfb1294ca076`.
Parser-conformance amendments: `research/amendments/0085_source_caption_parser_conformance.md` and `research/amendments/0085_source_caption_parser_conformance_r1.md`.
Final authoritative classification: **PASS_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE**
`NMIR_READINESS: 98%`.

## Scientific question
Can the unresolved naming of the four blue Figure-6 Wagner traces be bypassed without guessing EW/EW94/EW99 identities by constructing a source-authorized, identity-free pointwise strongest published B-L upper-limit curve from every validated primary vector component?

## Primary authority
Primary source: Wagner et al., arXiv `1207.2442v1`, Figure 6 left panel.

The exact source TeX says the left panel shows `95 % CL upper bounds` on the strength of a vector Yukawa interaction coupled to `q~=B-L`; the body independently describes 95% CL limits on the magnitude of the Yukawa strength for `B-L` charge.

Therefore each retained Figure-6 data curve is individually an upper-limit curve: points above that individual curve are excluded and points below it are allowed by that individual published result. The 0085 envelope is **not** a joint statistical combination; it is only the pointwise strongest among individually published limits.

Exact EPS: `WEP_figure6.eps`.
SHA256: `4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882`.

Frozen 0072b transforms retained unchanged:
- `log10(lambda/m) = 3.0018224354393763*x_eps - 7.051566622680237`;
- `log10(|alpha_tilde|) = 1.650456736852946*y_eps - 12.69366318007594`;
- `m_V[eV] = 1.973269804e-7/lambda[m]`;
- `|g_BL| = 2.70463357586823e-19*sqrt(|alpha_tilde|)`.

## Authoritative hosted provenance
Final conformance run:
- run `34174047570`
- job `101899820199`
- head commit `fd9e495002533411b11b55e82c0df1392572c3a4`
- artifact `10036642116`
- GitHub artifact ZIP digest `sha256:8b8df51229ed18e34ca415cd15404a0250f79329bcbe42f9cf0a100abf55a404`
- independently downloaded ZIP SHA256 `8b8df51229ed18e34ca415cd15404a0250f79329bcbe42f9cf0a100abf55a404`
- raw JSON SHA256 `a73cef7477ed604f9c8d03b137cec02fbd50b1dab415a452959a3127b76e6313`.

All dedicated conformance tests passed, the frozen scientific audit passed, the artifact uploaded, and fail-closed classification enforcement passed.

## Retained source-native topology
The frozen Figure-6 parser gives exactly:
- blue: 4 retained connected components;
- red: 1;
- orange: 1;
- magenta: 2;
- total: 8.

All eight retained components are x-monotonic and transform to finite positive masses/couplings. No disconnected component is bridged. In particular, the old 0072d result that one blue source trace is printed in two disconnected pieces remains respected.

The old `SCIENTIFIC_FAIL_WAGNER_BLUE_IDENTITY` therefore remains valid **for assigning the names EW/EW94/EW99 to the four blue geometric components**. 0085 does not overturn that result. It proves instead that the names are unnecessary for the identity-free strongest-limit object.

## Numerical diagnostics
- component count: `8`;
- topology: PASS;
- all components x-monotonic: PASS;
- all transformed quantities finite/positive: PASS;
- maximum EPS transform round-trip residual: `8.881784197001252e-16`;
- frozen tolerance: `1e-9`;
- anonymous component name/order invariance: `0.0 decade`;
- frozen tolerance: `1e-12 decade`;
- fine-grid/shared-point reproduction: `0.0 decade`;
- frozen tolerance: `1e-10 decade`.

## Authoritative Wagner identity-free envelope
Object name:

`POINTWISE_STRONGEST_PUBLISHED_WAGNER_95CL_UPPER_LIMIT`.

Global NMIR lower clip: `m_V >= 1e-6 eV`.

Source-supported mass interval after clipping:

`1.0e-6 eV <= m_V <= 6.845530367110015e-6 eV`.

In log10 mass this is one contiguous support run:

`-6.0 <= log10(m_V/eV) <= -5.164592898649604`.

The 20,001-point uniform grid plus source-native vertices yields `20,020` supported envelope points. Over this clipped support, the same anonymous component `blue_3` is pointwise strongest at all `20,020` authoritative grid/vertex samples. This does **not** authorize naming `blue_3` as EW, EW94 or EW99.

Representative endpoints:
- at `m_V = 1e-6 eV`: `g_BL = 1.4919699084771585e-22`;
- at `m_V = 6.845530367110015e-6 eV`: `g_BL = 1.2097149888731938e-21`.

Across the supported envelope samples the coupling spans from `1.4919699084771585e-22` to `1.2097149888731938e-21`.

Excluded-side semantics:

`g_BL > g_Wagner_env(m_V)` is excluded by at least one individual published Wagner 95% CL upper-bound curve wherever the identity-free envelope has source support.

This must **not** be described as a statistically combined 95% CL curve. It is a pointwise lower envelope of individually published 95% CL upper limits.

## Historical non-authoritative runs
- first 0085 hosted implementation stopped before scientific audit on test import-path infrastructure failure;
- run `34173707219`, job `101898844487`, artifact `10036532329`, raw JSON SHA256 `6dccff400ca6e463226fe5d9032974e0b0b89b8f71288153fa243380d69a5890`, ZIP SHA256 `3e30868869e340a2bca1867d92a8863a325f9c718860d9b814acc1df2eb41ae5`, returned a provisional `BLOCKED_*` only because the source-caption parser failed to recognize exact TeX wording `$95 \%$ CL upper bounds`. Its geometry is numerically identical to the final r1 result and it is retained as `INFRASTRUCTURE_FAIL_SOURCE_CAPTION_PARSER_CONFORMANCE`;
- subsequent regression-only runs stopped before scientific audit while the exact source-style `$...$` math delimiter/whitespace normalization was corrected. They carry no scientific classification.

## Scientific consequence
0085 closes the Wagner **curve-name-independent side/envelope authority**. The unresolved blue identities no longer prevent using the strongest primary Wagner upper-limit curve as an anonymous F8 ledger object.

This is a material closure of a previously explicit external-constraint uncertainty class, so `NMIR_READINESS` advances from 97% to **98%**. This percentage measures reproducibility/funnel maturity only; it is not a probability that B-L new physics exists, not a discovery significance, and not publication probability.

The Wagner result affects only a narrow ultralight interval around `1e-6`–`6.85e-6 eV` after the NMIR global lower clip. It does not replace fifth-force, cosmology, CEvNS or stellar/SN constraints elsewhere.

## What remains open
The external B-L constraint program is not yet globally complete:
- Wagner has an authoritative anonymous strongest-limit curve, but no cross-family union/composition is authorized by 0085;
- fifth-force has only the long-range asymptotic anchor, with no finite-mass continuation authorized;
- Hong exact finite-mass geometry remains blocked by approximate `O(0.1 MeV)` endpoints;
- BBN geometry remains blocked;
- Cerdeño vector geometry remains retired under the no-raster/manual contract;
- COHERENT/global combined-likelihood authority remains incomplete;
- scenario-conditioned Majorana/Dirac cosmology branches remain alternatives, not unionized;
- Shin–Yun T/L and BODY_NATIVE/CONCLUSION_SUMMARY remain separate objects.

BSM response/enhancement calculations therefore remain locked pending a dedicated external-envelope completion/composition audit and formal unlock gate.

## Exact next direction
Do **not** immediately union Wagner with the other families. First audit the remaining high-value missing 0071 constraint authority, especially the COHERENT combined-likelihood/global-contour branch, or formally classify it as non-actionable if the required primary likelihood/response authority is unavailable. Once all surviving families are independently authoritative or explicitly retired/blocked, preregister a separate scenario-aware cross-family composition/completeness gate.

## Guards
No raster/OCR/manual digitization. No visual blue-name assignment. No interpolation across disconnected source components. No extrapolation outside Wagner support. No joint-95%-CL claim. No cross-family B-L union in 0085. No post-hoc y clip/finite excluded-area claim beyond the one-sided upper-limit curve. No BSM response/enhancement scan until separately unlocked.
