# https://leetcode.com/problems/maximum-subsequence-score/
# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose
# a subsequence of indices from nums1 of length k.
#
# For chosen indices i0, i1, ..., ik - 1, your score is defined as:
#
# The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik-1]).
# Return the maximum possible score.
#
# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or
# no elements.
#
# Constraints:
#
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[j] <= 10^5
# 1 <= k <= n

from typing import List
from heapq import heappush, heappop
from unittest import TestCase


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        out = s = 0
        pq = []
        for i in range(len(nums)):
            heappush(pq, nums[i][0])
            s += nums[i][0]

            if i >= k:
               s -= heappop(pq)

            if i+1 >= k:
                out = max(out, s*nums[i][1])

        return out


class PQ:
    def __init__(self):
        self._pq = []

    def push(self, n: int):
        self._pq.append(n)
        self._pq = sorted(self._pq)

    def pop(self) -> int:
        out = self._pq[0]
        self._pq = self._pq[1:]
        return out

class SolutionPQ:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        out = s = 0
        pq = PQ()
        for i in range(len(nums)):
            pq.push(nums[i][0])
            s += nums[i][0]

            if i >= k:
               s -= pq.pop()

            if i+1 >= k:
                out = max(out, s*nums[i][1])

        return out

class TestSolution(TestCase):
    def test_solution(self):
        for cs in [SolutionPQ, Solution]:
            for case, expected in [
                [([1, 3, 3, 2], [2, 1, 3, 4], 3), 12],
                [([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1), 30],
                [([2,1,14,12], [11,7,13,6], 3), 168],
                [([23,16,20,7,3], [19,21,22,22,12], 3), 1121]
            ]:
                print(f"run test {cs.__name__} {case}")
                self.assertEqual(expected, cs().maxScore(*case))

