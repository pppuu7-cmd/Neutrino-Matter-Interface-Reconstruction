# NMIR iteration 0025 — G8 integrated resonance-strength / spectral-overlap formal gate

Date: 2026-09-06
Status: **G8_FORMAL_PASS**
Readiness after promotion: `NMIR_READINESS: 48%` (audit estimate)

## Scientific problem
A narrow nuclear/atomic resonance can have an enormous peak cross section, so ranking resonant candidates by `sigma_peak` alone can create a false appearance of huge neutrino opacity or power. NMIR therefore requires an integrated-strength and source-overlap gate before any resonant candidate may enter the G3 energy ledger.

Ordinary continuum charged-current capture `nu + A -> B* + e-` is not automatically such a resonance because the outgoing charged lepton carries continuously variable kinetic energy. The isolated Breit-Wigner gate applies only to genuine two-body/bound-state/recoilless or otherwise isolated-resonance kinematics.

## Preregistered identity
The contract was frozen before hosted output in `research/resonance_overlap_prereg.md`, commit `31bd2467140cdfcfeede18de115934904849eb3d`.

For

`sigma(E)=pi/k_r^2 * g * Gamma_in*Gamma_out / ((E-Er)^2+(Gamma/2)^2)`,

the exact narrow-resonance area is

`I_sigma = 2*pi^2/k_r^2 * g * Gamma_in * Gamma_out/Gamma`.

Since `Gamma_out<=Gamma`,

`I_sigma <= 2*pi^2/k_r^2 * g * Gamma_in`.

Thus line narrowing can increase the peak but cannot create integrated weak entrance strength.

For any non-negative incident differential flux `phi(E)`,

`R_per_target = integral phi(E)sigma(E)dE <= sup(phi) * I_sigma`.

For a normalized source line profile `rho(E)`,

`<sigma> <= ||rho||_infinity * I_sigma`.

No delta-function source is allowed to evade this bound. The current bookkeeping-only monoenergetic pep line is explicitly not G8 resonance authority until a physical solar pep profile is frozen.

## Hosted implementation
- formal code commit `5c8e75e38168a156d983e9e1113c49bf52db6435`;
- regression tests commit `48b791fa1a486578353e70c15218761081d1f5a1`;
- benchmark commit `dcb28c55abb7fd3537b2c39a66ae04e2d59b1e75`;
- hosted head `8c778ccecc9df3f579fef178b068762c5476fc10`.

Hosted authority:
- workflow `NMIR G8 resonance overlap`;
- run `34038642747`;
- job `101501241557`;
- artifact `9990968127`;
- artifact ZIP SHA256 `db13ac11dbd5cba7aaa76465987265c710dd64ff10cea28617edd9c298d239c5`.

Same-head baseline CI run `34038642903`: SUCCESS.

## Raw result
The Breit-Wigner area was evaluated numerically at total widths
`1e-3, 1e-6, 1e-9, 1e-12, 1e-15` with fixed entrance width and fixed `Gamma_out/Gamma=0.5`.

| diagnostic | result |
|---|---:|
| max numeric-vs-analytic area relative error | `6.3661977016e-5` |
| area invariance error across 1e6 narrowing test | `0.0` |
| peak gain after narrowing width by 1e6 | `1.0e6` |
| area / entrance-width area bound | `0.5` |
| max Gaussian/Lorentzian overlap / supremum bound | `0.8797668563` |
| status | **G8_FORMAL_PASS** |

The area numerical error is dominated by the intentionally finite Lorentzian integration domain and remains inside the preregistered `1e-4` criterion for all widths spanning twelve decades.

## Interpretation
A large resonant peak is not a free enhancement mechanism. At fixed weak entrance strength, narrowing redistributes cross section into a taller and narrower line; the integrated area remains tied to `Gamma_in`. A solar-neutrino power claim must therefore supply:
1. a physical resonant channel, not ordinary continuum CC capture mislabeled as a resonance;
2. target-specific weak `Gamma_in` or equivalent measured decay/ft strength;
3. `Gamma_out/Gamma` and any recoil-free/environmental factors;
4. a physical incident solar spectral profile and line broadening;
5. the actual energy convolution.

Only after these are frozen may a resonant target enter G3 W/kg ranking.

This is a **formal G8 PASS**, not yet a numerical resonant W/kg ceiling. The largest remaining G3 nuclear loophole is now the first-forbidden/higher-multipole one-body sector plus target-specific resonant entrance-width authority.

## Literature anchor
D. Suzuki et al., Phys. Lett. B 687 (2010) 144–148, DOI `10.1016/j.physletb.2010.03.024`, explicitly discusses very large resonant-neutrino peak cross sections and strong attenuation of the mean cross section from line broadening/energy spread.
