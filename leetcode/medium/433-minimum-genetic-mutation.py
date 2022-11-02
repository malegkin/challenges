# https://leetcode.com/problems/minimum-genetic-mutation/
# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined
# as one single character changed in the gene string.
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid
# gene string.
# Given the two gene strings 'start' and 'end' and the gene bank 'bank', return the minimum number of mutations needed
# to mutate from start to end. If there is no such a mutation, return -1.
# Note that the starting point is assumed to be valid, so it might not be included in the bank.
# Constraints:
# start.length == end.length == bank[i].length == 8
# start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
# 0 <= bank.length <= 10

from typing import Set, List, Union
from unittest import TestCase


class Solution:
    """
    Depth-First Search Solution
    Time Complexity: O(N*log(N))
    Space Complexity: O(N)
    """
    def minMutation(self, start: str, end: str, bank: Union[Set[str], List[str]]) -> int:

        def _is_one_diff_chars(s1: str, s2: str) -> int:
            return 1 == len([i for i in range(len(s1)) if s1[i] != s2[i]])

        if start == end:
            return 0

        bank = bank if isinstance(bank, set) else set(bank)
        out = {self.minMutation(b, end, bank - {b}) for b in bank if _is_one_diff_chars(start, b)}
        out.discard(-1)

        return min(out) + 1 if len(out) > 0 else -1


class SolutionBFS:
    """
    Breadth-First Search Solution
    Time Complexity: O(N*log(N))
    Space Complexity: O(N)
    """
    def minMutation(self, start: str, end: str, bank: Union[Set[str], List[str]]) -> int:

        def _is_one_diff_chars(s1: str, s2: str) -> int:
            return 1 == sum([1 for i in range(len(s1)) if s1[i] != s2[i]])

        stack = [(start, 0)]
        visited = set()
        while stack:
            cur, mutations = stack.pop()
            if cur == end:
                return mutations

            for b in bank:
                if b not in visited and _is_one_diff_chars(cur, b):
                    visited.add(b)
                    stack.append((b, mutations + 1))

        return -1


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, SolutionBFS]:
            for case, expected in [
                [("AACCGGTT", "AACCGGTA", ["AACCGGTA"]), 1],
                [("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]), 2],
                [("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]), 3]
            ]:
                print(f"run_test {sc.__name__} {case}")
                self.assertEqual(expected, sc().minMutation(*case))

