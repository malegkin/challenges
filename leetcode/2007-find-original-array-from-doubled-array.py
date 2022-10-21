# https://leetcode.com/problems/find-original-array-from-doubled-array/
# An integer array original is transformed into a doubled array changed by appending twice the value of every element in
# original, and then randomly shuffling the resulting array.
# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an
# empty array. The elements in original may be returned in any order.
# Constraints:
#   1 <= changed.length <= 10^5
#   0 <= changed[i] <= 10^5

import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        out = list()
        doubled = defaultdict(int)
        for c in sorted(changed, key=lambda x: -x):
            if doubled[c*2] > 0:
                out.append(c)
                doubled[c*2] -= 1
            else:
                doubled[c] += 1

        # print(f"{out=} {doubled=}")
        return out if len(out)*2 == len(changed) else []


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for solution_class in [Solution]:
            for case, expected in [
                [[1], []],
                [[6, 3, 0, 1], []],
                [[1, 3, 4, 2, 6, 8], [1, 3, 4]],
                [[4, 8, 2, 16, 1, 8], [1, 4, 8]]
            ]:
                print(f"run_test {solution_class.__name__} {case}")
                self.assertListEqual(expected, sorted(solution_class().findOriginalArray(case)))
