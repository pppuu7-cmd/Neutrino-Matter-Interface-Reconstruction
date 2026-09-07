# NMIR iteration 0065 — observable-driven absolute short-range weak-current ceiling audit

Date: 2026-09-07
Classification: **PASS_NO_COEFFICIENT_INDEPENDENT_OBSERVABLE_MAP / RESIDUAL_OPEN**

## Funnel target
G3 / F4-F6. Test a genuinely different route from 0059 and 0062: whether inclusive measured Standard-Model electroweak/nuclear observables plus their sum-rule/response formalism provide a finite regulator/scheme-independent target-class ceiling on the absolute short-range two-/higher-body weak-current contribution.

## Prospective contract
Frozen before the result-dependent authority audit:
- `research/prereg/0065_g3_observable_driven_contact_ceiling.md`
- prereg commit `7f727dbfb509500c93b1d9502e8f3197ee1d18e7`.

The contract forbade EFT naturalness, fitted-LEC universality, selected-nucleus percent corrections as universal maxima, Ikeda promotion without an explicit two-body theorem, cancellation-blind inference from total observables, and reuse of the invalid 0062 hard-`lmax` argument.

## Frozen authority ledger
- `data/g3_observable_contact_authority_0065.json`
- ledger commit `ef72e39d37b7006902a2b7c6670411c21aec37d2`.

## Route 1 — inclusive weak response sum rules
Lovato et al. (Phys. Rev. Lett. 112, 182502 (2014), DOI `10.1103/PhysRevLett.112.182502`, arXiv `1401.2605`) calculate neutral-current response sum rules in `12C` with a specified realistic Hamiltonian and one-/two-body currents. They find a substantial two-body contribution, of order 30% in important response channels.

This is strong evidence that inclusive observables constrain and diagnose two-body currents. It is **not** the preregistered universal ceiling: the sum rule is the total response of a particular Hamiltonian/current realization. If `J=J_1+J_2`, the positive total strength contains `J_1^†J_1`, `J_2^†J_2`, and interference `J_1^†J_2+h.c.`. Positivity of the total observable alone does not isolate a coefficient-independent upper norm on an arbitrary short-range `J_2` when interference/cancellation is not removed by an additional theorem.

## Route 2 — Gamow-Teller / Ikeda information
Ekström et al. (Phys. Rev. Lett. 113, 262504 (2014), DOI `10.1103/PhysRevLett.113.262504`, arXiv `1406.4696`) compute consistent two-body-current effects in `14C` and `22,24O`; the two-body currents reduce the calculated summed Gamow-Teller strength, with reported `q^2≈0.84–0.92` relative to the conventional Ikeda benchmark. Ney, Engel & Schunck (Phys. Rev. C 105, 034349 (2022), DOI `10.1103/PhysRevC.105.034349`, arXiv `2112.14621`) show in heavy nuclei that two-body currents usually quench summed GT strength but can enhance individual low-lying transitions, with effects varying with neutron excess/density.

Therefore the ordinary Ikeda relation is not an audited coefficient-independent upper bound on an arbitrary two-body contact-current coefficient. Primary calculations instead show current- and target-dependent redistribution/modification. Treating `3(N-Z)` as a universal contact-current ceiling would violate the preregistered operator-content guard.

## Route 3 — ordinary muon capture
Muon capture is a valuable finite-q probe of electroweak currents, but the primary authority does not supply the required universal inequality. Marcucci et al. (Phys. Rev. Lett. 108, 052502 (2012), DOI `10.1103/PhysRevLett.108.052502`) constrain chiral LECs `c_D,c_E` using few-body binding energies and the triton GT matrix element, then predict muon-capture rates. Ricci et al. (arXiv `0912.1989`) explicitly state that their EFT two-body current contains a low-energy constant not determined from one-particle data or first principles in that formulation and extract it through capture-rate analysis. Modern deuteron and ab-initio nuclear capture studies continue to treat capture as a model/current validation observable with interaction/current/truncation uncertainties, not as an observable-only universal operator-norm theorem.

Thus muon capture can calibrate or test a chosen current/Hamiltonian scheme; it does not by itself bound the same short-range coefficient across arbitrary nuclei without the nuclear-theory mapping whose universality is precisely at issue.

## Scientific synthesis
All audited observable routes are physically useful, but none satisfies every prospective PASS criterion simultaneously:
1. finite explicit coefficient-independent ceiling;
2. regulator/scheme independence;
3. target-class transfer without a fresh fit/model calculation;
4. isolation of the short-range two-/higher-body contribution rather than only a total response with interference;
5. applicability to the passive solar-neutrino deposited-power envelope.

The key failure is structural, not merely lack of precision: measured inclusive strengths constrain **total physical response combinations**. Separating an arbitrary short-range sub-operator requires operator/Hamiltonian matching or a positivity/orthogonality theorem that the audited primary authorities do not supply.

## F10 classification
**`PASS_NO_COEFFICIENT_INDEPENDENT_OBSERVABLE_MAP / RESIDUAL_OPEN`**.

This closes the observable-driven universal-ceiling route under the frozen authority/scope. It does **not** prove that an arbitrary contact coefficient can be physically huge, and it does not close the underlying absolute short-range/contact-current residual. Instead it prevents NMIR from mislabelling measured beta/charge-exchange/muon-capture/inclusive-response agreement as a universal hard bound.

No numerical W/kg fold is authorized because no class-level coefficient ceiling passed F4-F6.

## Next funnel action
After reconciliation, do not repeat:
- selected-nucleus percent corrections as universal maxima;
- fitted `c_D`/contact LEC ranges as regulator-independent bounds;
- Ikeda `3(N-Z)` as an arbitrary two-body-current ceiling;
- total-response agreement while ignoring interference;
- hard `lmax≈kR` unitarity.

The G3 physical contact residual remains explicit. Further G3 work requires a genuinely new theorem/assumption, not another recasting of the same data. Re-rank the remaining independent OPEN gates after reconciliation; BSM remains locked until a formal unlock audit.

Because 0065 reproducibly closes an entire proposed class-level **bounding route** (while preserving the physical residual), readiness receives only one point of maturity credit.

`NMIR_READINESS: 88%`.
