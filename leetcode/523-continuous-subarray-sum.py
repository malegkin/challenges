# https://leetcode.com/problems/continuous-subarray-sum/
# Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose
# elements sum up to a multiple of k, or false otherwise.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

# Constraints:
#   1 <= nums.length <= 10^5
#   0 <= nums[i] <= 10^9
#   0 <= sum(nums[i]) <= 2^31 - 1
#   1 <= k <= 2^31 - 1

# if sum(nums[i:j]) % k == 0  THEN  sum(nums[:j]) % k == sum(nums[:i]) % k

from typing import List
from unittest import TestCase
from itertools import accumulate, groupby


class Solution:
    """
    Time Complexity:    O(len(nums))
    Space Complexity:   O(min(len(nums), k)
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod, mods = 0, {0: -1}

        for i in range(len(nums)):
            mod = (mod + nums[i]) % k
            if mod in mods:
                if i - mods[mod] > 1:
                    return True
            else:
                mods[mod] = i

        return False


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution]:
            for case, expected in [
                [([6, 1], 6), False],
                [([2, 2, 2, 3], 6), True],
                [([2, 2, 1, 2, 2], 6), False],
                [([2, 2, 1, 2, 2, 2], 6), True],
                [([23, 2, 4, 6, 7], 6), True],
                [([23, 2, 6, 4, 7], 6), True],
                [([23, 2, 6, 4, 7], 13), False]
            ]:
                print(f"run_test {sc.__name__}, {case}")
                self.assertEqual(expected, sc().checkSubarraySum(*case))

