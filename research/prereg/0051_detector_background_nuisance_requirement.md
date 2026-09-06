# NMIR 0051 preregistration — detector background-normalization nuisance requirement

Date: 2026-09-06
Gate: G2 real detector transfer / accepted-background systematics
Status at preregistration: OPEN

## Question
How much does uncertainty in the accepted, analysis-indistinguishable background normalization tighten the one-year 3σ and 5σ background ceilings derived in iteration 0050?

## Frozen scope
This is a one-bin median-discovery Asimov/profile-likelihood requirement. It is not a detector-performance claim, not a raw environmental/trigger background model, and not a substitute for a recoil-dependent efficiency/background spectrum.

Signal scenarios are frozen from iteration 0050:
- `design_S10`: S = 10.0 accepted events/year.
- `Ar40_10eV_eta0p50`: S = 11.84624201853375 accepted events/year, 10 kg.
- `Ar40_20eV_eta0p75`: S = 9.909735084 accepted events/year, 10 kg.

Target significances: Z = 3 and 5.
Fractional background-normalization uncertainties: delta_B = {0, 0.10, 0.30, 0.50}, with sigma_b = delta_B * B.

## Frozen statistic
For sigma_b > 0 use the standard profile-likelihood Asimov discovery significance for a Poisson counting experiment with Gaussian background uncertainty:

`Z_A^2 = 2[(s+b) ln(((s+b)(b+sigma_b^2))/(b^2+(s+b)sigma_b^2)) - (b^2/sigma_b^2) ln(1 + sigma_b^2 s/(b(b+sigma_b^2)))]`.

For delta_B = 0 use the exactly-known-background limit from iteration 0050:

`Z_A^2 = 2[(s+b) ln(1+s/b)-s]`.

Primary/statistical authority: Cowan, Cranmer, Gross, Vitells, *Asymptotic formulae for likelihood-based tests of new physics*, Eur. Phys. J. C 71 (2011) 1554, arXiv:1007.1727; formula also implemented by ROOT/RooStats `AsimovSignificance`.

## Frozen computation
For every `(scenario, delta_B, Z)` invert `Z_A(s,B,delta_B)=Z` for the maximum positive accepted background `Bmax` using a deterministic bracketing/bisection solver.

Report:
- `Bmax events/year`;
- `Bmax/S`;
- for 10-kg Ar scenarios, `Bmax events/(kg year)`;
- tightening ratio `Bmax(delta_B)/Bmax(0)`;
- reconstructed Z and maximum relative inversion residual.

## Scientific PASS criteria
All must hold:
1. At `delta_B=0`, every `Bmax` reproduces iteration 0050 to relative tolerance <= 1e-10.
2. For each signal/Z, `Bmax` is non-increasing with delta_B and strictly decreases for positive delta_B.
3. Reconstructed Z has maximum relative inversion residual <= 1e-10.
4. For all tested scenarios, 5σ requires lower `Bmax` than 3σ at the same delta_B.
5. No negative/non-finite significance or background ceiling occurs.

If these pass, classify `PASS_BACKGROUND_NUISANCE_REQUIREMENT_MAP`. This closes only the counting-level normalization-nuisance gate. It does not validate any detector's achieved background uncertainty.

## Scientific FAIL
Any violation of the frozen criteria is retained as a scientific FAIL; the statistic, signal inputs, uncertainty grid and tolerances are not relaxed after seeing the result.

## Infrastructure FAIL
Import/package/runner/artifact failures are infrastructure-only and may be repaired minimally without changing physics/statistical criteria.

## Next action after PASS
Move to the first detector-specific transfer layer: frozen recoil-dependent `epsilon_NR(T,state)` / threshold turn-on and stability using measured calibration data. If no defensible 10–20 eV NR calibration exists for a candidate technology, record that branch as evidence-blocked rather than inventing efficiency.