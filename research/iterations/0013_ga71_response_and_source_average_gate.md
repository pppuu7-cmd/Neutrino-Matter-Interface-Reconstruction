# Iteration 0013 — Ga-71 response freeze and source-average validation

Date: 2026-09-06

## Goal

Advance G3 by freezing an authoritative energy-dependent `nu_e + 71Ga -> 71Ge + e-` response suitable for arbitrary spectral folding, and validate that the interpolation plus already-frozen spectral inputs reproduce published source-averaged cross sections before introducing oscillated solar fluxes.

## Source frozen

Primary response source: J. N. Bahcall, *Gallium solar neutrino experiments: Absorption cross sections, neutrino spectra, and predicted event rates*, Phys. Rev. C 56, 3391 (1997).

The numerical specific-energy tables associated with the paper give best, -3 sigma and +3 sigma cross sections versus neutrino energy in units of `1e-46 cm^2`. NMIR copied the 58 tabulated energies from 0.240 to 30 MeV into `data/ga71_bahcall1997_response.csv` and implemented fail-closed interpolation in `src/nmir/ga71_response.py`.

The response is set to zero at/below the physical capture threshold and fails closed above the frozen 30-MeV table rather than extrapolating.

## Prospective source-average gate

Before inspecting hosted numerical output, `scripts/ga71_unoscillated_benchmark.py` froze tolerances against Bahcall Table VI standard-spectrum source averages:

- pp: 1.5%
- pep: 4%
- Be7: 0.5%
- N13: 2.5%
- O15: 2.5%
- F17: 2.5%

B8 and hep were intentionally excluded from this identity gate because the current NMIR manifest pins the later Ortiz-2000 B8 choice and a separately frozen hep spectrum; comparing those to Bahcall's 1997 source-average values would mix spectral conventions.

## Authoritative hosted scientific result

Workflow: `NMIR Ga71 benchmark`

- run: `34017366528`
- job: `101443416887`
- head: `a3fb3dcceafeecb4cdda59bf6459437c33d7050f`
- conclusion: SUCCESS
- artifact: `9984322724`
- artifact ZIP SHA256: `fc162d6807a3f087aaf8086c6558d16e1c1358f497fc751b48cb6d97d66a0f4f`

Results in units of `1e-46 cm^2`:

| source | computed | published | relative error | frozen tolerance | gate |
|---|---:|---:|---:|---:|---|
| pp | 11.74399 | 11.72 | 0.2047% | 1.5% | PASS |
| pep | 205.624 | 204.0 | 0.7961% | 4% | PASS |
| Be7 | 71.71590 | 71.7 | 0.0222% | 0.5% | PASS |
| N13 | 60.45132 | 60.4 | 0.0850% | 2.5% | PASS |
| O15 | 113.88247 | 113.7 | 0.1605% | 2.5% | PASS |
| F17 | 114.56221 | 113.9 | 0.5814% | 2.5% | PASS |

This establishes that the frozen specific-energy response plus the pinned pp/CNO spectra reproduce the published Ga-71 standard-spectrum averages without tuning after result inspection.

## CI diagnosis and repair authority

The first same-head baseline CI run `34017366468` failed for a non-scientific regression mistake: the new test expected 59 response rows while the frozen table correctly contains 58. The scientific benchmark itself had already passed. The test cardinality was corrected in commit `cd429081a35d04aa5b44c2e69a0c694320064ccd`; no response values, interpolation rule, benchmark tolerances, spectra or physics criteria were changed.

Post-fix/recovery-head baseline CI is authoritative:

- run `34017446027`
- job `101443639628`
- head `2d61abe7fe7816e838a7b8ea9281a34e61b4e145`
- conclusion SUCCESS
- `71 passed in 0.18s`
- baseline physics executable also completed successfully.

Classification: **infrastructure/test FAIL repaired; scientific Ga-71 source-average gate PASS; post-fix CI PASS.**

## Scientific consequence

G3 now has an externally validated Ga-71 response function capable of true spectral folding. The next gate is no longer a nuclear-response lookup problem: it is the actual oscillated solar folding

`B16 flux × pinned spectral shape × component production-averaged Pee(E) × Ga71 sigma(E)`

for both GS98 and AGSS09met, with component and total SNU recorded prospectively. Only after that result is reproduced/validated should NMIR convert Ga capture into deposited power and move to Cl-37.

NMIR_READINESS: 29%
