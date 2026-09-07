# Iteration 0074c — COHERENT CsI+Ar combined-likelihood benchmark authority audit

## Classification

**BLOCKED_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY**

This documentary audit is subordinate to the prospective contract frozen in `research/prereg/0074c_coherent_combined_likelihood_benchmark_authority_audit.md` at commit `80d8ffaae102d8c5a3ba731dc1e8ae3b7e4d9d41`. No likelihood minimization was executed and no B−L mass/coupling point was evaluated.

## What the primary authority does fix

Cadeddu et al., JHEP 01 (2021) 116 / arXiv:2008.05022v3, fixes the detector-specific least-squares constructions used for its CsI+Ar limits.

For CsI, the analysis uses 12 energy bins `i=4..15` and

`chi2_CsI = sum_i [(Nexp_i - (1+alpha_c) NCEvNS_i - (1+beta_c) B_i)/sigma_i]^2 + (alpha_c/0.112)^2 + (beta_c/0.25)^2 + ((eta-1)/0.051)^2`.

For Ar, Analysis A uses `0 <= Eee < 120 keVee` in 12 ten-keVee bins and

`chi2_Ar = sum_i [(Nexp_i - eta_CEvNS NCEvNS_i - eta_PBRN B_PBRN_i - eta_LBRN B_LBRN_i)/sigma_i]^2`

plus Gaussian nuisance penalties with `sigma_CEvNS=13.4%` for fixed neutron radius, `sigma_PBRN=32%`, `sigma_LBRN=100%`; the BRN energy-shape term contributes an uncorrelated `1.7%` per-bin component to the variance. These conventions, together with the hash-pinned official releases, are enough to define a plausible combined implementation architecture.

The official data releases already frozen in iteration 0074 remain authoritative for exact bytes: CsI first observation DOI `10.5281/zenodo.1228631` and Ar Analysis A DOI `10.5281/zenodo.3903810`; their per-file SHA256 manifest is `data/coherent_primary_packages_0074_manifest.json`.

## Controlling failure of the prospective gate

The prereg required at least one external, non-circular **numerical combined-likelihood benchmark** with an explicit tolerance frozen before any reproduction. Accepted forms were: a published SM minimum chi-square/likelihood value, published profiled nuisance best-fit values plus a sufficient expectation, or an official same-release example-code likelihood reference point.

The permitted primary routes were exhausted:

1. The Cadeddu paper provides the detector chi-square formulas, bin supports, nuisance widths and exclusion contours, but no exact combined SM/background `chi2_min`, no complete profiled nuisance best-fit vector, and no tabulated same-analysis combined likelihood reference point.
2. The official CsI release provides the experimental binned data/response and basic analysis interaction material but not a CsI+Ar combined profile-likelihood output.
3. The official Ar release provides observed data, CEvNS/background PDFs, efficiency, YAML parameters, systematic-error files and reading/plotting helpers, but no combined CsI+Ar likelihood reference point.
4. The paper's statement that the universal-model `(g-2)_mu` region lies more than 120 in Delta-chi-square above the minimum is not an acceptable benchmark: it is not an exact SM/background reference point, does not specify a unique parameter point/tolerance adequate to validate the profile machinery, and is for the universal-model exclusion discussion rather than the required SM/background benchmark.

Therefore prospective criterion 5 fails. The gate cannot be converted into a numerical reproduction without inventing a post-hoc tolerance or promoting a secondary reproduction to authority, both explicitly forbidden.

## Frozen gate checklist

- exact CsI/Ar supports and binnings pinned: **PASS**;
- signal/background components mapped to primary release inputs or explicit analytic construction: **PASS**;
- nuisance parameters, widths and detector-specific structure pinned: **PASS**;
- least-squares/statistic convention pinned: **PASS**;
- non-circular primary numerical combined benchmark with pre-result tolerance: **FAIL / unavailable**.

Machine-readable audit: `data/coherent_combined_likelihood_authority_audit_0074c.json`, commit `17c41bf043015a3cf11dd5d33033f8ba3bc5451c`.

## Scientific meaning

This is not a failure of the COHERENT data and not evidence that the published B−L bound is wrong. It is a reproducibility-authority blocker under NMIR's stricter preregistration rule: the exact external numerical benchmark needed to validate an independently written combined profile likelihood is absent from the allowed primary routes.

The standalone 0074a Ar and 0074b CsI response PASSES remain valid. They may not be reinterpreted as validation of the combined likelihood.

## Next action

Retire this exact combined-likelihood B−L route unless a genuinely new primary source supplies a suitable combined numerical benchmark. No `(m_V,g_BL)` scan is permitted. Return to the highest-value actionable OPEN funnel class and require a genuinely new executable class-level route rather than weakening this blocker.
