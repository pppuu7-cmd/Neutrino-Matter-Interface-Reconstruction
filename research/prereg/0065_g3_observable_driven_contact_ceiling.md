# NMIR preregistration 0065 — observable-driven absolute short-range weak-current ceiling audit

Date frozen: 2026-09-07
Status at freeze: PROSPECTIVE / NO RESULT-DEPENDENT CLASSIFICATION INSPECTED
Parent authority: iteration 0064 returns the funnel to the remaining G3 absolute short-range/contact-current coefficient residual. Iterations 0059 and 0062 forbid reusing EFT naturalness/fitted-LEC universality or a hard `lmax≈kR` as a coefficient-independent theorem.

## Scientific question
Does Standard-Model electroweak/nuclear response theory plus **inclusive measured observables** provide a genuinely coefficient-independent, target-class upper ceiling on short-range two-/higher-body weak-current strength that can be propagated to passive solar-neutrino deposited power without assuming an EFT-naturalness prior or treating selected nuclei as universal maxima?

Candidate observable routes to audit prospectively:
1. inclusive ordinary muon capture / total weak-response sum rules;
2. beta-decay and charge-exchange strength distributions / Ikeda-type or related sum rules;
3. neutrino/antineutrino inclusive scattering spectral functions and current-current correlator dispersion/sum-rule relations;
4. electroweak response constraints tied to conserved/current-algebra relations where applicable.

## Required mapping for a class-level PASS
A route qualifies only if primary authority supplies or implies an inequality of the form

`||J_short||_class <= C_obs`

or an equivalent inclusive spectral-strength ceiling such that:
- `C_obs` is finite and has explicit normalization/units;
- the bound is independent of regulator/scheme and does not assume a fitted LEC range as universal;
- it applies to the relevant target class without a new free coefficient fit for each target;
- it controls the short-range two-/higher-body weak contribution itself, not only a total response after possible interference/cancellation with one-body terms;
- it is strong enough in principle to be propagated through the already frozen solar source set to an absolute deposited-power ceiling.

A target-specific measurement or a collection of percent-level corrections is evidence-distance only and does not satisfy this mapping.

## Prospective classifications
1. `PASS_OBSERVABLE_DRIVEN_CONTACT_CEILING`
   - at least one audited inclusive observable/theorem gives a regulator-independent finite target-class ceiling on the relevant short-range current contribution. Next action: freeze the numerical authority and propagate it to W/kg prospectively.

2. `PASS_NO_COEFFICIENT_INDEPENDENT_OBSERVABLE_MAP / RESIDUAL_OPEN`
   - audited observables constrain target-specific combinations/total responses or require nuclear-model/operator matching such that no universal short-range-current ceiling follows without extra assumptions. This closes the observable-driven route but leaves the physical coefficient residual open.

3. `BLOCKED_AUTHORITY_GAP`
   - a plausible formal mapping exists but the necessary primary normalization/data/theorem cannot be recovered sufficiently to classify it.

4. `FAIL_OBSERVABLE_MAPPING`
   - an initially proposed relation is found to constrain a different operator/channel, to depend on cancellations, or to be invalid for the required inclusive short-range contribution.

## Mandatory guards
- Do not promote Ikeda/one-body sum rules to a bound on arbitrary two-body contact-current coefficients unless the theorem explicitly includes them.
- Do not infer a bound on a hidden short-range term from agreement of a total observable when destructive interference is allowed unless a positivity/orthogonality theorem removes that ambiguity.
- Do not treat muon-capture, beta-decay or charge-exchange data from selected nuclei as a universal maximum.
- Do not use EFT truncation errors, `O(1)` naturalness, fitted `c_D` ranges or regulator scans as a hard universal coefficient bound.
- Do not reuse the invalid 0062 hard-`lmax` argument.
- Do not convert detector/event amplification into neutrino-energy gain.

## Evidence/provenance output
Freeze a machine-readable authority ledger in `data/g3_observable_contact_authority_0065.json` identifying each theorem/observable, operator content, positivity/interference properties, regulator/model dependence, target scope, and whether it satisfies every PASS criterion. Preserve the result in `research/iterations/0065_g3_observable_driven_contact_ceiling.md` and reconcile recovery/funnel.

## Scientific vs infrastructure failure
Unavailable source/API access or repository-write failure is infrastructure failure. A well-supported finding that no audited observable supplies the required coefficient-independent map is a scientific route closure, not infrastructure failure and not a theorem that arbitrary beyond-scope coefficients are impossible.
