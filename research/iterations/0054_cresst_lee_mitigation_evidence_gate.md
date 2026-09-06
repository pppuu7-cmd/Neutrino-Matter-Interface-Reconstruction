# Iteration 0054 — CRESST LEE mitigation evidence gate

Date: 2026-09-06
Gate: G2 demonstrated LEE suppression/discrimination
Hosted-audit status: `PASS_LEE_MITIGATION_EVIDENCE_AUDIT`
Scientific classification: `MECHANISM_SURVIVOR_QUANTITATIVE_GAP_OPEN`

## Frozen authority
Prospective contract: `research/prereg/0054_cresst_lee_mitigation_evidence_gate.md`.
Prereg commit: `c0052cf2c0f636cf4e176f987d233bbb3a4f4032`.
Machine-readable evidence ledger: `data/cresst_lee_mitigation_evidence.csv`.
Scientific workflow head: `9b11f3bee1b70bdce87063eb66e16be25fcbf4f6`.
Hosted run/job: `34059455141 / 101557243909`.
Artifact: `9996995011`, `lee-mitigation-evidence-result`.
Artifact ZIP SHA256: `baa710c01b2a548df0f32188627b53429b8f68f213c4cca5403586b81e5fd531`.
Raw hosted log inspected: `5 passed`; fail-closed benchmark returned both `PASS_LEE_MITIGATION_EVIDENCE_AUDIT` and the frozen scientific classification.

## Primary evidence audit
### DoubleTES 2024 — experimentally demonstrated mechanism
Primary authority: CRESST Collaboration, G. Angloher et al., Eur. Phys. J. C 84, 1001 (2024), DOI `10.1140/epjc/s10052-024-13282-8`, arXiv:2404.02607.

Closed observations:
- two identical TES readouts separate a diagonal absorber/bulk population from low-energy populations that appear in only one TES;
- the conservative absorber selection requires the two reconstructed sensor energies to differ by no more than 35%;
- applying this cut is reported to significantly reduce near-threshold events;
- the single-TES component is therefore a genuine experimentally demonstrated taggable LEE component;
- a separate absorber-band LEE component survives and has measured above-ground time dependence `10.2 ± 1.1 d` in the 28–50 eV band;
- the paper says the single-TES component could be efficiently tagged, but does not publish a public numerically comparable pre/post rejection factor plus bulk-signal acceptance over the 0053 10–300 eV window;
- datasets/code are available on reasonable request rather than as a public machine-readable rate table.

Therefore DoubleTES closes the **existence of a discrimination handle**, but not the multiplicative suppression factor needed by NMIR.

### CRESST next-generation report — projection, not measured suppression
Primary authority: CRESST Collaboration, G. Angloher et al., *The CRESST experiment towards the next generation of sub GeV direct dark matter detection*, Communications Physics, DOI `10.1038/s42005-025-02476-5`, preprint arXiv:2505.01183.

The report:
- identifies detector-intrinsic effects as currently dominating the LEE evidence picture;
- foresees DoubleTES as the future baseline because of its capability to reject the single-TES LEE component;
- projects roughly 10× LEE reduction after ~450 d and 100× after ~900 d under long stable cryogenic operation;
- explicitly uses 10× and 100× as upgrade sensitivity benchmarks/projections, not as already demonstrated detector-wide suppression factors in a configuration quantitatively comparable with 0053.

### SOS low-threshold cross-check
CRESST PRD 110, 083038 (2024) demonstrates a 0.6-g SOS detector with `6.7 ± 0.2 eV` threshold and `1.0 ± 0.2 eV` baseline resolution. This strengthens the low-threshold technology branch but does not provide a directly comparable measured LEE suppression factor for the 0053 Si stress because target composition/configuration and analysis window differ.

## Frozen numerical residual-gap audit
0053 5σ, 30% background-normalization nuisance required total improvement:
`G0053 = 4.1485517170734453e9`.

Treating the CRESST 10× and 100× values strictly as **projection-only stress factors**:
- after 10×: residual required improvement `4.1485517170734453e8`;
- after 100×: residual required improvement `4.148551717073445e7`.

Thus even the optimistic 100× benchmark retires only two orders of magnitude from a gap exceeding nine orders of magnitude under the deliberately severe 0053 fixed-LEE-per-kg extrapolation.

## Scientific classification
`MECHANISM_SURVIVOR_QUANTITATIVE_GAP_OPEN`.

This is not a failure of DoubleTES. It means:
1. a physically relevant discrimination mechanism is experimentally real;
2. current public evidence does not yet supply the measured, comparable rejection×acceptance number required to retire a definite fraction of the 0053 gap;
3. future measured intrinsic LEE reduction and/or topology rejection can be inserted directly once a comparable dataset is published.

## Exact next gate
Convert the surviving detector problem into a factorized engineering/scientific budget rather than treating a billion-scale rejection as one monolithic cut. Freeze orthogonal factors for:
- intrinsic LEE reduction per kg;
- DoubleTES/topology classification;
- time-domain likelihood separation using measured LEE decay versus steady solar flux;
- segmentation/coincidence/veto rejection;
- retained CEvNS signal acceptance.

Derive the combinations required to reach the 0051 5σ budget and identify which factors have demonstrated experimental anchors versus which remain aspirational. Do not multiply factors that are not shown independent.