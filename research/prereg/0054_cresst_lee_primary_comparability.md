# NMIR 0054 preregistration — CRESST LEE primary-data comparability / demonstrated suppression gate

Date: 2026-09-06
Gate: G2 detector background scalability
Status at preregistration: OPEN

## Question
Do newer primary CRESST detector results provide a quantitatively comparable, exposure-normalized low-energy-excess measurement from which NMIR can defensibly infer a demonstrated reduction factor relative to the 2023 0.35-g Si LEE stress used in iteration 0053?

This gate tests demonstrated technology progress, not theoretical possibility. It must fail closed if detector configuration, energy window, efficiency convention or spectral data are not comparable enough to support a number.

## Frozen primary authorities
A. Baseline authority already used by 0052/0053:
- CRESST Collaboration, G. Angloher et al., `Results on sub-GeV dark matter from a 10 eV threshold CRESST-III silicon detector`, Phys. Rev. D 107, 122003 (2023), arXiv:2212.12513.
- Baseline module mass 0.35 g; gross blind exposure 55.06 g day; central efficiency-corrected LEE fit over 10–300 eV frozen by 0053.

B. Newer SOS authority:
- CRESST Collaboration, G. Angloher et al., `First observation of single photons in a CRESST detector and new dark matter exclusion limits`, arXiv:2405.06527 (2024).
- Primary text anchors: SOS detector threshold `(6.7 ± 0.2) eV`, baseline resolution `(1.0 ± 0.2) eV`, final-spectrum exposure `0.138 kg day`; publication explicitly reports a steep LEE and a simulated energy-dependent full selection survival curve in its Fig. 5.

C. Newer DoubleTES authority:
- CRESST Collaboration, G. Angloher et al., `DoubleTES detectors to investigate the CRESST low energy background: results from above-ground prototypes`, arXiv:2404.02607 (2024).
- Primary text anchors: doubleTES separates absorber-like events from single-TES/sensor-proximate events; SOS prototype thresholds 27 eV and 20.5 eV for its two TES channels; absorber-band LEE remains significant below ~150 eV; above-ground rates are stated to be typically at least 1–2 orders of magnitude above underground rates; authors explicitly state further tests are needed to establish underground comparability.

No review/secondary source may supply the numerical suppression factor.

## Frozen comparability requirements
A numerical demonstrated LEE reduction factor may be reported only if all of the following are available from primary material without result-dependent tuning:
1. a common recoil/phonon-energy interval contained in both baseline and candidate detector published ranges, preferably 20–130 eV; if another interval is required it must be fixed before extracting candidate counts/rates;
2. exposure-normalized differential or integrated event rate in that common interval for both detectors;
3. compatible efficiency convention, or enough published efficiency information to transform both rates to the same convention;
4. detector mass/exposure normalization unambiguous;
5. no above-ground/underground comparison is converted into a detector-improvement factor unless environment is controlled or explicitly corrected by the primary analysis.

## Data-access hierarchy
Use in order:
1. machine-readable primary data/repository/supplement;
2. tabulated numbers in the primary paper;
3. digitization of a primary figure only if axes, normalization and efficiency convention are explicit and the digitization uncertainty can be estimated and frozen before comparing;
4. otherwise return BLOCKED.

## Outputs
- `COMPARABLE_PRIMARY_DATA` or `BLOCKED_BY_NONCOMPARABLE_PRIMARY_DATA` for each newer authority;
- if comparable: common window, rate_baseline, rate_candidate, efficiency convention, reduction factor `F_red=rate_baseline/rate_candidate`, uncertainty/envelope and provenance;
- if blocked: exact missing quantitative ingredient(s), with no invented factor;
- identify whether DoubleTES supplies an event-class discrimination mechanism even if it does not supply a comparable underground per-kg LEE reduction.

## Scientific PASS criteria
`PASS_DEMONSTRATED_LEE_REDUCTION` requires at least one newer primary dataset satisfying all five comparability requirements and yielding a finite positive `F_red` from reproducible primary numerical data.

`PASS_DISCRIMINATION_ONLY` is allowed if primary data demonstrate a separable sensor-proximate event class but do not supply an underground-comparable total LEE reduction factor. This does not close the 0053 total background gap.

`BLOCKED_BY_NONCOMPARABLE_PRIMARY_DATA` is the required classification if no newer primary dataset supports a defensible quantitative reduction factor.

No acceptance criterion may be relaxed after viewing candidate spectra.

## Infrastructure vs scientific failure
Failure to access a primary supplement/repository is infrastructure/data-access BLOCKED, not scientific evidence. Failure of the comparability conditions with accessible primary data is a scientific `BLOCKED_BY_NONCOMPARABLE_PRIMARY_DATA` outcome and is itself a useful funnel result.

## Next action
- On `PASS_DEMONSTRATED_LEE_REDUCTION`: multiply only the empirically validated intrinsic LEE-reduction factor into the 0053 technology-gap ledger and keep discrimination as a separate factor.
- On `PASS_DISCRIMINATION_ONLY`: quantify the maximum directly demonstrated tagged fraction only if primary event counts are recoverable; otherwise retain qualitative mechanism evidence and move to a detector with published machine-readable backgrounds.
- On `BLOCKED_BY_NONCOMPARABLE_PRIMARY_DATA`: stop trying to infer a CRESST suppression number from plots/prose and redirect G2 to a detector technology with published machine-readable low-energy background and NR acceptance, while preserving CRESST as the threshold/transfer benchmark.