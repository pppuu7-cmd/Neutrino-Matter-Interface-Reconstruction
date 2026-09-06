# B16 solar-neutrino flux input provenance

Frozen for NMIR iteration 0007.

Primary model source:

- N. Vinyoles et al., **A New Generation of Standard Solar Models**, Astrophys. J. 835, 202 (2017), DOI: `10.3847/1538-4357/835/2/202`, arXiv:`1611.09867`.
- The primary paper defines two B16 ensembles based on the high-metallicity GS98 and low-metallicity AGSS09met compositions and provides detailed solar-model predictions, including neutrino fluxes.

Frozen component values in `solar_flux_b16.csv`:

| component | B16-GS98 flux [cm^-2 s^-1] | rel. unc. | B16-AGSS09met flux [cm^-2 s^-1] | rel. unc. |
|---|---:|---:|---:|---:|
| pp | 5.98e10 | 0.006 | 6.03e10 | 0.005 |
| pep | 1.44e8 | 0.010 | 1.46e8 | 0.009 |
| hep | 7.98e3 | 0.30 | 8.25e3 | 0.30 |
| Be7 | 4.93e9 | 0.06 | 4.50e9 | 0.06 |
| B8 | 5.46e6 | 0.12 | 4.50e6 | 0.12 |
| N13 | 2.78e8 | 0.15 | 2.04e8 | 0.14 |
| O15 | 2.05e8 | 0.17 | 1.44e8 | 0.16 |
| F17 | 5.29e6 | 0.20 | 3.26e6 | 0.18 |

Independent transcription cross-check used during freezing: the B16 values reproduced in later solar-neutrino review tables and in the data-driven solar reconstruction literature agree with the above central values and uncertainties.

## Scope guard

This file freezes **source-integrated unoscillated number fluxes only**. It does not yet freeze:

- continuum spectral shapes for pp, hep, B8, N13, O15, F17;
- Be7 branching fractions / line energies;
- pep line energy convention;
- MSW/vacuum survival probabilities;
- correlations among flux uncertainties.

Therefore this dataset is sufficient for provenance, normalization and line/component bookkeeping, but it is **not yet sufficient for a precision Ga-71/Cl-37 rate integral**. Those inputs must be frozen prospectively in the next gate rather than inferred ad hoc.
