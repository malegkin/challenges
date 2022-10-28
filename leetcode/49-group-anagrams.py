# https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

from typing import List
from collections import defaultdict, Counter
from itertools import groupby
from unittest import TestCase


class Solution:
    """
    Time complexity = O(N*log(N))
    Space complexity = O(N)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[''.join(sorted(s))].append(s)

        return list(groups.values())


class SolutionCounterHash:
    """
    Time complexity = O(N)
    Space complexity = O(N)
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[frozenset(Counter(s).items())].append(s)

        return list(groups.values())


class SolutionOneLine:
    """
    Time complexity = O(N*log(N))
    Space complexity = O(N)
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        return [list(g) for _, g in
                groupby(sorted(strs, key=lambda s: ''.join(sorted(s))), key=lambda s: ''.join(sorted(s)))]


class SolutionOneLine2:
    """
    Time complexity = O(N)
    Space complexity = O(N)
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def s_set(s: str):
            return frozenset(Counter(s).items())

        return [list(g) for _, g in
                groupby(sorted(strs, key=s_set), key=s_set)]


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, SolutionCounterHash, SolutionOneLine]:
            expected: List[List[str]]
            for case, expected in [
                [[""], [[""]]],
                [["a"], [["a"]]],
                [["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]],
            ]:
                print(f"run_test {sc.__name__} {case}")
                for o in sc().groupAnagrams(case):
                    o = sorted(o)
                    self.assertIn(o, expected)
                    expected.remove(o)
                self.assertEqual(expected, [])

