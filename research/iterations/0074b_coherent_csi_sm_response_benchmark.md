# Iteration 0074b — COHERENT CsI first-observation SM response benchmark

## Classification

**PASS_COHERENT_CSI_SM_RESPONSE_BENCHMARK**

This result is subordinate to the prospective contract frozen in `research/prereg/0074b_coherent_csi_sm_response_benchmark.md` at commit `c47769b51c186f2b1eda2aed72c02e5ca6eb7030`. No PASS criterion was weakened after seeing a result, and no B−L scan was performed.

## Frozen external target and response chain

The benchmark target was the first-observation Standard Model prediction `173 ± 48` CEvNS events; the fitted excess `134 ± 22` was explicitly forbidden as a benchmark target. The response chain used the same-analysis fixed QF 0.0878, light yield 13.348 PE/keVee, Poisson PE smearing, and published acceptance. The released first-observation analysis grids define `6 <= PE < 30`; the authoritative implementation therefore separates the wide numerical Poisson support from that analysis ROI and gives zero event-selection weight outside PE 6..29.

## Authoritative scientific result

Hosted run/job: `34140558778 / 101801362484`

Head used by the run: `1fe2821033ce8b384f3ef1b5500ce942e91a7bad`

Artifact: `10025718339`, 828 bytes

Artifact ZIP SHA256: `177ca00c47990c3917627f8febe3fd5b2561e984c41e2a6316b32168c14a44d9`

The raw job log was inspected directly. Six dedicated tests passed, the frozen benchmark ran, and the raw result classified itself as `PASS_COHERENT_CSI_SM_RESPONSE_BENCHMARK`.

Fine calculation (`n_t=4000`):

- Cs-133 νe: 25.371500548276167
- Cs-133 prompt νμ: 15.479815629312736
- Cs-133 anti-νμ: 37.57608984898328
- Cs-133 total: 78.42740602657219
- I-127 νe: 24.00248129037442
- I-127 prompt νμ: 15.220315349165682
- I-127 anti-νμ: 35.19406959285722
- I-127 total: 74.41686623239733
- **Total: 152.8442722589695 events**

The total lies inside the prospectively frozen interval `[125, 221]` events.

Numerical refinement from `n_t=1000` to `n_t=4000` was `9.408514258279292e-08`, far below the frozen 0.5% ceiling. The maximum omitted Poisson probability was `2.3314683517128287e-15`, below `1e-8`. All isotope/flavor contributions were finite and non-negative. Disabling acceptance increased the count to 444.96597491730245; setting the form factor to unity increased it to 352.1840873381009. A +1% QF or +1% light-yield perturbation increased the count to 154.66729168860792. All frozen guards passed.

The machine-readable authority record is `data/coherent_csi_sm_0074b.json` (commit `f0bfe484d301f459b7a4a2a4686db6f2eb98a478`).

## Fail-closed implementation chronology

Three non-authoritative attempts are intentionally retained rather than erased:

1. Run `34140156775` stopped in dedicated tests before the benchmark because a 100-bin Poisson numerical support left a `4.18e-8` tail, above the frozen `1e-8` guard. This is an implementation fail-closed, not a scientific FAIL.
2. Run/job `34140406355 / 101800883715` produced 161.42374070335802 events and artifact `10025662636`, but inspection showed that the implementation applied the logistic acceptance above the released `PE < 30` support. Because exact support was already a frozen requirement, this run is **IMPLEMENTATION_INVALID / NEVER SCIENTIFIC AUTHORITY**. The target and criteria were not changed.
3. Run `34140540384` was an intermediate sequential code/test mismatch while explicit ROI handling was being installed; it is infrastructure-only and not scientific authority.

The final implementation explicitly separates numerical Poisson convergence support (`n < 160`) from the physical analysis selection (`6 <= PE < 30`).

## Scientific meaning

This PASS validates the independent first-observation CsI SM source → CEvNS → recoil → fixed-QF/light-yield → Poisson PE → acceptance response normalization at the deliberately broad published `173 ± 48` external benchmark. It does **not** validate the exact Cadeddu combined CsI+Ar profile likelihood, any B−L exclusion contour, or any NMIR BSM enhancement.

## Next action

Before any B−L mass/coupling scan, prospectively freeze and then reproduce the combined CsI+Ar SM/background likelihood using the hash-pinned official inputs, exact analysis bins, nuisance conventions, and a non-circular primary benchmark/tolerance. Only a PASS of that combined-likelihood reproduction may unlock a prospectively frozen B−L exclusion calculation.
