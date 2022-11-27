# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# Given an integer array nums, return the number of all the arithmetic subsequences of nums.
# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between
# any two consecutive elements is the same:
#       For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
#       For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array:
#    For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# The test cases are generated so that the answer fits in 32-bit integer.
# Constraints:
#       1  <= nums.length <= 1000
#       -2^31 <= nums[i] <= 2^31 - 1

from unittest import TestCase
from typing import List, Dict, Set
from collections import defaultdict
from itertools import chain


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diffs = [defaultdict(int) for _ in range(len(nums))]

        out = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[:i]):
                diffs[i][b-a] += diffs[j][b-a] + 1
                out += diffs[j][b-a]

        return out


class TestSolution(TestCase):
    def test_solution(self) -> None:
        for sc in [Solution]:
            for case, expected in [
                [[2, 4, 6, 8, 10], 7],      # [2,4,6], [2,4,6,8], [2,4,6,8,10], [4,6,8], [4,6,8,10], [6,8,10], [2,6,10]
                [[7, 7, 7, 7, 7],  16],     # any subsequence of this array is arithmetic
                                            # 0,1,2 + 0,1,2,3 + 0,1,2,3,4
                [[2, 3, 1], 0],
                [[1, 2, 3], 1],
                [[1, 2, 3, 4], 3],
                [[1, 2, 3, 4, 5], 7],       # 1,2,3 + 1,2,3,4 + 1,2,3,4,5 + 2,3,4+ 2,3,4,5 + 3,4,5 + 1,3,5
                [[1, 2, 3, 4, 5, 6], 12],   # 1,2,3 + 1,2,3,4 + 1,2,3,4,5 + 1,2,3,4,5,6 + 2,3,4 + 2,3,4,5 + 2,3,4,5,6
                                            # 3,4,5 + 3,4,5,6 + 4,5,6 + 1,3,5 + 2,4,6
                [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 968],
                [[1, 1, 1, 1, 1], 16],
                [[1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3], 57],  # ({1} = 16) + ({3} = 16) + (5*5) == 57
                [[1, 1, 1, 2, 3, 1, 3, 3, 3, 3, 1], 47],  # ({1} = 16) + ({3} = 16) + (3*5) == 47
                [[1, 1, 1, 2, 3, 4, 5, 6, 1, 7, 7, 7, 7, 7, 1, 8, 8, 8, 8, 9], 510],  # (1*5 = 16) + (7*5 = 16) +(8*4 = 5) +
                                                                                      # 1,2,3 * 3 +

            ]:
                print(f"run test {sc.__name__} {case}")
                self.assertEqual(expected, sc().numberOfArithmeticSlices(case))

