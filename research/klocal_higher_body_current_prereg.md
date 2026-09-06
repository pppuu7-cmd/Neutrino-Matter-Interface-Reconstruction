# Prospective contract — finite-range k-local weak-current first-moment bound

Date frozen: 2026-09-06
Gate: G3 genuine two-/higher-body current residual
Parent authorities: iterations 0027, 0028, 0031, 0033

## Scientific question

Can correlations among bounded finite-range two-/higher-body Standard-Model current operators produce a free superextensive energy-weighted neutrino response, even when every local current term and every local Hamiltonian term has bounded norm and bounded coordination at fixed density?

This gate addresses **scaling / collective correlation gain**, not the absolute numerical value of a nuclear EFT coefficient.

## Frozen operator class

Let

`O = sum_X o_X`

be the neutrino-coupled many-body operator. Each current term satisfies

- support size `|X| <= k`;
- operator norm `||o_X|| <= o0`;
- each site belongs to at most `d_O` current terms.

Let the passive target Hamiltonian be

`H = sum_Y h_Y`,

with

- support size `|Y| <= l`;
- `||h_Y|| <= h0`;
- each site belongs to at most `d_H` Hamiltonian terms.

`k,l,d_O,d_H,o0,h0` are fixed with system size `N`.

No assumption of a product state, weak correlations, perturbative eigenstates, or small entanglement is allowed. The expectation value may be taken in an arbitrary normalized state.

## Frozen sum-rule object

For the energy-weighted response first moment,

`m1(O) = (1/2) < [O†,[H,O]] >`.

Expand

`[O†,[H,O]] = sum_{Z,Y,X} [o_Z†,[h_Y,o_X]]`.

A triple can contribute only if

1. `X` overlaps `Y`; and
2. `Z` overlaps the support of `[h_Y,o_X]`, which is contained in `X union Y`.

Using `||[A,B]|| <= 2||A||||B||`, each contributing nested term obeys

`||[o_Z†,[h_Y,o_X]]|| <= 4 o0^2 h0`.

## Prospectively frozen combinatorial bound

With the incidence definitions above:

- number of current terms `n_O <= N d_O`;
- for any `X`, at most `k d_H` Hamiltonian terms overlap `X`;
- for any overlapping `(X,Y)`, the union has at most `k+l` sites, hence at most `(k+l)d_O` current terms `Z` can overlap it.

Therefore a deliberately loose but explicit bound is

`N_trip <= N * k*(k+l) * d_O^2 * d_H`,

and

`|m1| <= 2 N k(k+l) d_O^2 d_H o0^2 h0`.

The frozen claim to test/prove is only the **O(N)** scaling at fixed local parameters. Tightening the constant after seeing results is unnecessary and not part of PASS.

## Frozen scientific acceptance

### PASS_KLOCAL_EXTENSIVITY
All of the following hold:

1. the analytic overlap-count argument is internally consistent;
2. exhaustive small-system support enumeration never exceeds the frozen `N_trip` bound for a representative grid including `k=1,2,3`, `l=1,2,3`, periodic/open finite-range support families and multiple `N`;
3. explicit random finite-dimensional Hermitian matrix models satisfy the nested-commutator norm bound and measured `|m1|` does not exceed the analytic first-moment bound;
4. a scaling benchmark confirms that the frozen upper bound per site is N-independent when `k,l,d_O,d_H,o0,h0` are fixed;
5. an intentionally growing-coordination counterexample is included and is correctly classified OUTSIDE SCOPE rather than falsely bounded as local.

### SCIENTIFIC_FAIL
A valid in-scope support/model construction violates the analytic overlap or first-moment bound.

### INFRASTRUCTURE_FAIL
Code/test/workflow failure without a valid physics counterexample. Repair minimally; do not change the operator class or acceptance criteria.

## Interpretation frozen before results

A PASS would establish:

**bounded finite-range k-local current correlations cannot create a free superextensive energy-weighted response at fixed local norm/coordination.**

It would NOT establish:

- a universal absolute upper bound on `o0` for all nuclear two-/higher-body currents;
- a bound on genuinely long-range/growing-coordination current operators;
- a bound on active/driven systems whose external energy/resources scale with N;
- a BSM coupling bound;
- that selected-nucleus two-body amplitudes are universally <= some percentage.

Thus PASS would close the **collective scaling loophole** left by 0033, while the absolute microscopic coefficient/naturalness/data residual remains open and must be combined only qualitatively with the large bridge distance already measured in 0033.

## PASS next action

Reclassify the G3 residual from `GLOBAL_TWO_BODY_THEOREM OPEN` to a narrower state such as:

`FINITE_RANGE_KLOCAL_COLLECTIVE_SCALING CLOSED; ABSOLUTE_HIGHER_BODY_STRENGTH / LONG_RANGE_GROWING_COORDINATION OPEN`.

Then audit whether chiral-EFT power counting + empirical two-body-current data can provide a defensible absolute coefficient envelope without pretending selected nuclei are a universal theorem.

## FAIL next action

Preserve the counterexample and identify which locality/incidence step fails; do not replace it with a stronger hidden assumption after the fact.
