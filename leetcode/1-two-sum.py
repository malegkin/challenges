# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

import unittest
from typing import List


class Solution:
    """ n^2 solution"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                if x + y == target:
                    return [i, j+i+1]


class TestSolution(unittest.TestCase):
    def test_simple_sum(self):
        s = Solution()
        for t in [[[2, 7, 11, 15], 9, [0, 1]],
                  [[3, 2, 4], 6, [1, 2]],
                  ]:
            self.assertListEqual(t[2], s.twoSum(t[0], t[1]))


if __name__ == 'main':
    unittest.main()
