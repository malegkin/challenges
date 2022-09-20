# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
# Constraints:
#     1 <= nums1.length, nums2.length <= 1000
#     0 <= nums1[i], nums2[i] <= 100
from typing import List, Tuple
from unittest import TestCase
from collections import defaultdict


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        def dfs(n1: int, n2: int) -> int:
            if n1 >= len(nums1) or n2 >= len(nums2):
                return 0

            if nums1[n1] == nums2[n2]:
                return dfs(n1+1, n2+1) + 1

            return 0

        out = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                out = max(out, dfs(i, j))

        return out


class MSolution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = [[-1] * len(nums1) for _ in range(nums2)]

        def dfs(n1: int, n2: int) -> int:
            if n1 >= len(nums1) or n2 >= len(nums2):
                return 0

            if m[n1][n2] != -1:
                return m[n1][n2]

            if nums1[n1] == nums2[n2]:
                m[(n1, n2)] = dfs(n1+1, n2+1) + 1
                return m[(n1, n2)]

            return 0

        out = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                out = max(out, dfs(i, j))

        return out


class TestSolution(TestCase):
    def test_solution(self):
        for solution_class in [Solution]:
            for case, expected in [
                [[[1, 2, 3, 2, 1], [3, 2, 1, 4, 7]], 3],
                [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 5]
            ]:
                print(f"run_test {solution_class.__name__} {case}")
                self.assertEqual(expected, solution_class().findLength(*case))
