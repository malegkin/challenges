# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

import unittest
from typing import List


class Solution:
    """ O(n^2) head-on solution
    Runtime: 5317 ms, faster than 20.15% of Python3 online submissions for Two Sum.
    Memory Usage: 14.9 MB, less than 95.54% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                if x + y == target:
                    return [i, j+i+1]


class Solution2:
    """ O(n) solution
        Runtime: 71 ms, faster than 87.77% of Python3 online submissions for Two Sum.
        Memory Usage: 15.3 MB, less than 24.20% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, x in enumerate(nums):
            if target - x in index:
                return [index[target - x], i]
            index[x] = i


class TestSolution(unittest.TestCase):
    def test_simple_sum(self):
        for solution_class in [Solution, Solution2]:
            s = solution_class()
            for t in [[[2, 7, 11, 15], 9, [0, 1]],
                      [[3, 2, 4], 6, [1, 2]],
                      ]:
                self.assertListEqual(t[2], s.twoSum(t[0], t[1]))


if __name__ == 'main':
    unittest.main()
