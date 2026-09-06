# NMIR Iteration 0003 — Decay→Capture Reconstruction and Energy-Gap Benchmark

Date: 2026-09-06 (Europe/Stockholm)

## Strongest result of this iteration

For beta-decaying nuclei, published neutrino-capture theory explicitly shows that the beta decay and the corresponding neutrino-capture process use the same invariant weak amplitude (for unobserved polarization), and that measured beta-decay observables can be used to reconstruct the capture strength.

This gives NMIR a direct inverse-design principle:

`measured weak decay -> infer matrix element -> construct crossed/inverse neutrino capture -> rank capture target`.

For allowed/superallowed transitions the capture strength can be expressed through the measured comparative half-life `ft`, modulo the known outgoing-electron phase space, Fermi function and convention/unit conversion.

This is stronger than a qualitative time-reversal analogy: it is an established quantitative connection.

## Existing real-world examples

Two classic radiochemical solar-neutrino targets are exactly production↔capture pairs:

- Ar-37 electron capture to Cl-37 + nu_e; solar nu_e capture on Cl-37 produces Ar-37 + e-; threshold ~0.814 MeV.
- Ge-71 electron capture to Ga-71 + nu_e; solar nu_e capture on Ga-71 produces Ge-71 + e-; threshold ~0.233 MeV.

The Ge-71 half-life has recently been remeasured precisely at ~11.468 d. These examples show that decay information can constrain the inverse/crossed capture cross section in practice.

## Machine-readable catalog started

Created `data/inverse_transition_seed.csv` with initial benchmark/research candidates:

- Cl-37 / Ar-37;
- Ga-71 / Ge-71;
- H-3 / He-3 thresholdless neutrino-capture benchmark;
- Ho-163 / Dy-163 low-Q electron-capture / resonant candidate.

The catalog will later be expanded from evaluated nuclear data rather than hand-entered candidates.

## Energy-gap benchmark

Radiochemical rates use

`1 SNU = 1e-36 captures / target atom / s`.

Using the measured combined gallium solar capture rate `66.1 SNU`, isotopically pure Ga-71 has approximately

`5.61e-10 captures/s/kg`.

If each successful capture deposited an optimistic reference energy of exactly `1 MeV`, the corresponding normalization is only

`P_dep ~ 8.99e-23 W/kg`.

Therefore the multiplicative enhancement needed to reach even `1 W/kg` is approximately

`1.11e22`.

This is a normalization benchmark, not a claim that Ga capture deposits exactly 1 MeV on average.

## Interpretation

The energy problem is now quantitatively much sharper:

- ordinary solar charged-current capture is real;
- it directly embodies the user's production↔capture intuition;
- but present Standard-Model rates are ~22 orders of magnitude below a 1 W/kg engineering target under the optimistic 1-MeV-per-capture normalization.

Therefore NMIR must search for *parametric* enhancement, not incremental detector optimization.

Candidate sources of such enhancement that remain scientifically legitimate:

1. very strong allowed/superallowed inverse transitions with favorable `ft`;
2. narrow resonant two-body capture where flux overlaps the line;
3. environmental/atomic tuning that improves line overlap without violating integrated-strength bounds;
4. large target density and repeated/secondary capture chains;
5. nonequilibrium prepared media;
6. only after SM ceiling: BSM mediators/operators surviving all constraints.

## Spin/magnon branch status

Retained, but demoted for bulk energy capture relative to nuclear absorption because a soft collective excitation deposits a tiny fraction of MeV neutrino energy. It remains important for detection and for testing whether collective axial response can alter total weak opacity.

## New code

- `src/nmir/capture_metrics.py` converts SNU to captures/s/kg and deposited W/kg for a supplied physical deposition energy.
- `tests/test_capture_metrics.py` fixes the Ga-71 66.1-SNU normalization and target-enhancement metric.
- `theory/BETA_DECAY_INVERSE_CAPTURE.md` freezes the `ft`-based reconstruction logic and its unit/convention caution.

## Next gates

1. Reproduce one published neutrino-capture cross section from a measured `ft` value with full SI conversion.
2. Reproduce Cl-37 and Ga-71 benchmark cross sections/rates from primary literature.
3. Build the automated nuclear-transition catalog from evaluated decay data.
4. Rank transitions by both event-rate objective and deposited-power objective.
5. Investigate whether resonant capture can overcome the flux-bandwidth penalty.
6. Continue the sum-rule-preserving axial spin-response calculation in parallel.

## Maturity audit

- Problem formulation: 50%
- Operator inventory: 28%
- Production↔absorption formalism: 28%
- Many-body response taxonomy: 22%
- Numerical framework: 24%
- Constraint/literature ledger: 22%
- Inverse-transition catalog: 8%
- Standard-Model ceiling: 7%
- Engineered-medium scan: 5%
- BSM residual search: 0%

Overall NMIR research maturity (audit estimate): **~15%**.

No practical energy-harvesting mechanism has been found. The important advance is that NMIR now has a quantitative path from measured neutrino-production/weak-decay physics to inverse capture, plus a numerical scale for how large an enhancement would actually be required.
