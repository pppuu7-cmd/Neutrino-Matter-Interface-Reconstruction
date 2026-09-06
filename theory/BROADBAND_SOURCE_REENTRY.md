# Broadband-source re-entry in thresholded CEvNS target optimization

Last updated: 2026-09-06
Status: analytic interpretation of validated iteration 0045; not a standalone preregistered scientific gate.

## 1. Single-source envelope

In the low-q, heavy-target limit with approximately fixed weak charge per nucleon,

`Q_W = qbar A`, `M ~= A m_u`,

and a monoenergetic source `s` with neutrino energy `E_s`, the CEvNS rate per detector mass above a recoil threshold `T` has the approximate form

`R_s(A,T) = C_s A [1 - A/Amax_s(T)]^2_+`,

where `[x]_+ = max(x,0)`,

`Amax_s(T) = 2 E_s^2 / (m_u T)`,

and `C_s` contains source flux, weak constants and the `E_s^2` normalization.

The unique interior single-source optimum is

`Astar_s(T) = Amax_s(T)/3 = 2 E_s^2/(3 m_u T)`.

Thus for **one** source the preferred target mass decreases monotonically as `1/T`.

## 2. Broadband objective

For multiple neutrino sources,

`R_total(A,T) = A sum_s C_s [1 - A/Amax_s(T)]^2_+`.

This is not the same optimization problem as replacing the source by one effective energy. Each source has its own kinematic support boundary

`A < Amax_s(T)`.

As `T` changes, the set of source terms contributing at a particular target mass changes discontinuously in derivative and potentially discontinuously in the identity of the global maximizing target.

## 3. Why heavy-target re-entry is possible

Consider two source classes:

- `L`: lower neutrino energy, larger flux (solar Be7-like);
- `H`: higher neutrino energy, smaller flux (solar B8-like), with `E_H >> E_L`.

Because

`Amax_H/Amax_L = (E_H/E_L)^2 >> 1`,

there is a threshold range where a heavy target `A_h` satisfies

`A_h >= Amax_L(T)`

but

`A_h << Amax_H(T)`.

In that regime the lower-energy source contributes essentially zero to `A_h`, while the high-energy source still sees the target as well inside its recoil support.

Meanwhile a lighter target `A_l < Amax_L(T)` can retain the high-flux lower-energy source.

The global competition is then schematically

`R(A_l,T) ~= A_l [ C_L(1-A_l/Amax_L)^2 + C_H(1-A_l/Amax_H)^2 ]`,

versus

`R(A_h,T) ~= A_h C_H(1-A_h/Amax_H)^2`.

At intermediate threshold the first expression can win, producing a lighter optimum. At larger threshold the lower-energy term becomes strongly phase-space suppressed even for the lighter optimum; the second expression can then overtake it, causing the global optimum to **re-enter the heavy-target branch**.

No new interaction or coherence enhancement is involved. It is a change in which source dominates the thresholded objective.

## 4. General source-switch condition

For any source `s`, a target `A` loses source support when approximately

`T >= Tclose_s(A) = 2 E_s^2/(A m_u)`.

A source-regime transition is therefore expected near thresholds where the previously dominant high-flux source approaches `Tclose` for the target family that had been optimal below the transition.

For a higher-energy source `h`, the corresponding close scale is larger by

`Tclose_h(A)/Tclose_l(A) = (E_h/E_l)^2`.

This scale separation makes source-regime re-entry generic in principle for sufficiently broadband spectra with sufficiently separated energies and non-negligible high-energy flux.

## 5. Consequence for inverse design

There is no general monotonic law

`A_opt(T) decreases with T`

for a broadband source.

The correct inverse object is instead a piecewise target/source phase map

`(A_opt(T), s_dom(T))`.

Iteration 0043 gives the local monoenergetic law inside each source-dominated regime. Iteration 0045 demonstrates numerically that the full solar objective can move

`heavy -> intermediate -> lighter -> heavy`

as the dominant accepted source changes from Be7-like to B8-like. Active iteration 0046 is prospectively testing the exact crossover topology.

## 6. Practical target regret

A practical detector material need not coincide with the mathematical winner. Define

`regret_i(T) = 1 - R_i(T)/R_best(T)`.

If a practical material has small regret but a much better achievable transfer function or scalable mass, it can dominate the engineering optimum. The validated 0045 points already show Ar40 regret of only ~21% at 10 eV and ~14% at 20 eV, whereas its regret rises to ~70% at 40 eV.

This makes threshold reduction particularly valuable for metastable argon: it can simultaneously reduce target regret and reopen the high-flux Be7 source regime.

## 7. Scope guards

- The analytic envelope neglects exact isotope-mass deviations, form factors and detailed spectral shapes; exact calculations remain authoritative near endpoints.
- A solar continuum/thermal line cannot be replaced by one energy when precise crossover locations are required.
- Re-entry is target/source matching, not enhancement of the weak interaction.
- Detector accepted-rate optimization still requires `epsilon_NR(T)`, background, live time and mass scalability.
- This note explains a mechanism seen in 0045; literature novelty of the specific phase topology remains OPEN pending `research/CEVNS_NOVELTY_AUDIT.md` and broader search.
