# https://leetcode.com/problems/minimum-average-difference/
# You are given a 0-indexed integer array nums of length n.
#
# The average difference of the index i is the absolute difference between the average of the first i + 1 elements of
# nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.
#
# Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.
#
# Note:
#   The absolute difference of two numbers is the absolute value of their difference.
#   The average of n elements is the sum of the n elements divided (integer division) by n.
#   The average of 0 elements is considered to be 0.
# Constraints:
#     1 <= nums.length <= 10^5
#     0 <= nums[i] <= 10^5


from unittest import TestCase
from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        out_i, out_val = 0, right
        for i, num in enumerate(nums):
            left, right = left + num, right - num
            if out_val > (current :=  abs(left // (i + 1) - (0 if i == len(nums) - 1 else right // (len(nums) - i - 1)))):
                out_i, out_val = i, current

            print(f"{left=} {right=} {out_i=} {out_val=} {current=}")

        return out_i


class TestSolution(TestCase):
    def test_solution_case_1(self):
        """
        - The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
        - The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
        - The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
        - The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
        - The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
        - The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
        The average difference of index 3 is the minimum average difference so return 3.
        :return:
        """
        self.assertEqual(3, Solution().minimumAverageDifference([2, 5, 3, 9, 5, 3]))

    def test_solution(self):
        for case, expected in [
            [[1], 0],
            [[1, 1, 1, 1, 1], 0],
            [[0, 1, 0, 1, 0, 1], 0]
        ]:
            print(f"run test {case}")
            self.assertEqual(expected, Solution().minimumAverageDifference(case))

