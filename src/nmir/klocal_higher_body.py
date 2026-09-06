from __future__ import annotations

from dataclasses import dataclass
import cmath
import math
import random
from typing import Iterable, Sequence


Support = frozenset[int]
PauliString = tuple[str, ...]
Matrix = list[list[complex]]


@dataclass(frozen=True)
class LocalTerm:
    support: Support
    pauli: PauliString
    coeff: float


PAULI: dict[str, Matrix] = {
    "I": [[1 + 0j, 0j], [0j, 1 + 0j]],
    "X": [[0j, 1 + 0j], [1 + 0j, 0j]],
    "Y": [[0j, -1j], [1j, 0j]],
    "Z": [[1 + 0j, 0j], [0j, -1 + 0j]],
}


def contiguous_supports(n: int, size: int, periodic: bool) -> list[Support]:
    if n <= 0 or size <= 0 or size > n:
        raise ValueError("require 1 <= size <= n")
    out: list[Support] = []
    seen: set[Support] = set()
    starts = range(n) if periodic else range(n - size + 1)
    for start in starts:
        s = frozenset((start + j) % n for j in range(size))
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def all_pair_supports(n: int) -> list[Support]:
    return [frozenset((i, j)) for i in range(n) for j in range(i + 1, n)]


def max_incidence(n: int, supports: Sequence[Support]) -> int:
    counts = [0] * n
    for s in supports:
        for site in s:
            counts[site] += 1
    return max(counts, default=0)


def overlapping_triple_count(current: Sequence[Support], hamiltonian: Sequence[Support]) -> int:
    count = 0
    for x in current:
        for y in hamiltonian:
            if not (x & y):
                continue
            union = x | y
            for z in current:
                if z & union:
                    count += 1
    return count


def frozen_triplet_bound(n: int, k: int, l: int, d_o: int, d_h: int) -> int:
    return n * k * (k + l) * d_o * d_o * d_h


def frozen_m1_bound(n: int, k: int, l: int, d_o: int, d_h: int, o0: float, h0: float) -> float:
    return 2.0 * n * k * (k + l) * d_o * d_o * d_h * o0 * o0 * h0


def pauli_anticommutes(a: PauliString, b: PauliString) -> bool:
    odd = 0
    for x, y in zip(a, b):
        if x == "I" or y == "I" or x == y:
            continue
        odd ^= 1
    return bool(odd)


def random_local_term(n: int, support: Support, bound: float, rng: random.Random) -> LocalTerm:
    chars = ["I"] * n
    for site in support:
        chars[site] = rng.choice(("X", "Y", "Z"))
    coeff = rng.uniform(-bound, bound)
    return LocalTerm(support=support, pauli=tuple(chars), coeff=coeff)


def nested_local_commutator_amplitude(z: LocalTerm, h: LocalTerm, x: LocalTerm) -> float:
    if not (x.support & h.support):
        return 0.0
    if not pauli_anticommutes(h.pauli, x.pauli):
        return 0.0
    # [h,x] is a single Pauli string times a phase. For deciding whether z
    # commutes with that product, XOR the anticommutation parities with h and x.
    anti_with_product = pauli_anticommutes(z.pauli, h.pauli) ^ pauli_anticommutes(z.pauli, x.pauli)
    if not anti_with_product:
        return 0.0
    return 4.0 * abs(z.coeff * h.coeff * x.coeff)


def _kron(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] * b[p][q] for j in range(len(a[0])) for q in range(len(b[0]))]
            for i in range(len(a)) for p in range(len(b))]


def pauli_matrix(p: PauliString, coeff: float = 1.0) -> Matrix:
    out: Matrix = [[1 + 0j]]
    for c in p:
        out = _kron(out, PAULI[c])
    return [[coeff * v for v in row] for row in out]


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mat_scale(a: Matrix, c: complex) -> Matrix:
    return [[c * v for v in row] for row in a]


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return mat_add(mat_mul(a, b), mat_scale(mat_mul(b, a), -1.0))


def sum_terms(terms: Sequence[LocalTerm]) -> Matrix:
    if not terms:
        raise ValueError("terms required")
    nsites = len(terms[0].pauli)
    dim = 2 ** nsites
    out: Matrix = [[0j for _ in range(dim)] for _ in range(dim)]
    for term in terms:
        out = mat_add(out, pauli_matrix(term.pauli, term.coeff))
    return out


def random_unit_vector(dim: int, rng: random.Random) -> list[complex]:
    v = [complex(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)) for _ in range(dim)]
    norm = math.sqrt(sum(abs(x) ** 2 for x in v))
    return [x / norm for x in v]


def expectation(v: Sequence[complex], a: Matrix) -> complex:
    av = [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(v))]
    return sum(v[i].conjugate() * av[i] for i in range(len(v)))


def measured_m1(current_terms: Sequence[LocalTerm], h_terms: Sequence[LocalTerm], state: Sequence[complex]) -> float:
    o = sum_terms(current_terms)
    h = sum_terms(h_terms)
    nested = commutator(o, commutator(h, o))
    return abs(0.5 * expectation(state, nested))


def random_model(n: int, k: int, l: int, periodic: bool, seed: int, o0: float = 1.0, h0: float = 1.0):
    rng = random.Random(seed)
    os = contiguous_supports(n, k, periodic)
    hs = contiguous_supports(n, l, periodic)
    ot = [random_local_term(n, s, o0, rng) for s in os]
    ht = [random_local_term(n, s, h0, rng) for s in hs]
    state = random_unit_vector(2 ** n, rng)
    return os, hs, ot, ht, state


def classify_growing_coordination(n: int) -> dict[str, object]:
    supports = all_pair_supports(n)
    d_o = max_incidence(n, supports)
    return {
        "n": n,
        "term_count": len(supports),
        "d_o": d_o,
        "fixed_coordination": False,
        "classification": "OUTSIDE_SCOPE_GROWING_COORDINATION",
    }
