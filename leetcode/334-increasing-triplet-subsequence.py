# https://leetcode.com/problems/increasing-triplet-subsequence/
# Given an integer array nums, return true if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
# Constraints:
#   1 <= nums.length <= 5 * 10**5
#   -2**31 <= nums[i] <= 2**31 - 1
# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

from typing import List
from unittest import TestCase


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = secondMin = float('inf')
        for n in nums:
            if n <= first:
                if second < float('inf'):
                    secondMin = first
                first = n
            elif n <= second:
                second = n
            else:
                secondMin = first if secondMin == float('inf') else secondMin
                print(f"triplet = [{secondMin}, {second}, {n}]")
                return True
        return False


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, Solution2]:
            for nums, expected in [
                [[1, 2, 3, 4, 5], True],
                [[5, 4, 3, 2, 1], False],
                [[2, 1, 5, 0, 4, 6], True],
                [[2, 0, 6, 4, 5], True],
                [[5, 4, 6, 0, 8], True],
                [[5, 1, 5, 5, 0, 8], True],
                [[4, 5, 1, 6], True],
                [[5, 1, 0, 6, 1, 2, 0, 7, 1, 0], True]
            ]:
                print(f"run {sc.__name__}({nums})")
                self.assertEqual(expected, sc().increasingTriplet(nums))
