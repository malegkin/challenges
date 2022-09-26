# https://leetcode.com/problems/satisfiability-of-equality-equations/
# You are given an array of strings equations that represent relationships between variables where each string
# equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase
# letters (not necessarily different) that represent one-letter variable names.
# Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false
# otherwise.
# Constraints:
#     1 <= equations.length <= 500
#     equations[i].length == 4
#     equations[i][0] is a lowercase letter.
#     equations[i][1] is either '=' or '!'.
#     equations[i][2] is '='.
#     equations[i][3] is a lowercase letter.

from string import ascii_lowercase
from typing import List, Set, Tuple
from unittest import TestCase


class ElegantSolution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x) -> chr:
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        uf = {a: a for a in ascii_lowercase}
        for a, e, _, b in equations:
            if e == "=":
                uf[find(a)] = find(b)

        # print(f"{dict({u[0]: u[1] for u in uf.items() if u[0] != u[1]})}")
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equals: List[Set[chr]] = []
        nequals: List[Tuple[chr, chr]] = []

        for eq in equations:
            if eq[1] == '!':
                if eq[0] == eq[3]:
                    return False
                nequals.append((eq[0], eq[3]))
            else:
                for equal in equals:
                    if eq[0] in equal:
                        equal.add(eq[3])
                        eq = None
                        break
                    elif eq[3] in equal:
                        equal.add(eq[0])
                        eq = None
                        break
                if eq != None:
                    equals.append({eq[3], eq[0]})

        # print(f"{equations} => {equals}: {nequals}")

        for i in range(len(equals)):
            for j in range(i, len(equals)):
                if equals[i] is not None:
                    if len(equals[i].intersection(equals[j])) > 0:
                        equals[i], equals[j] = None, equals[i].union(equals[j])

        # print(f"{equations} => {equals}: {nequals}")

        for nequal in nequals:
            for equal in [eq for eq in equals if eq is not None]:
                if nequal[0] in equal and nequal[1] in equal:
                    return False

        return True


class TestSolution(TestCase):

    def test_solution(self):
        for solution_class in [Solution, ElegantSolution]:
            for case, expected in [
                [["a!=a"], False],
                [["a==b", "e==c", "b==c", "a!=e"], False],
                [["a==b", "b==c", "g==a"], True],
                [["b==b", "b==e", "e==c", "d!=e"], True],
                [["a==b", "b==c", "c==d", "e==d", "f==e", "f==g", "a!=g"], False],
                [["a==b", "b!=a"], False],
                [["a==b", "b==a"], True]
            ]:
                print(f"run {solution_class.__name__} {case}")
                self.assertEqual(expected, solution_class().equationsPossible(case))
