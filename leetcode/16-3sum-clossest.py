# https://leetcode.com/problems/3sum-closest/
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
# closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

from typing import List, Dict
from unittest import TestCase
from collections import defaultdict
from random import randint
from timeit import timeit


class OnHeadSolution:
    """
    O(N^2)*O(logN) + O(NlogN)
    """
    @staticmethod
    def _get_length_to_closest(nums: List[int], n, start: int = 0, end: int = None) -> int:
        """ return length to clossest nums array element that nums[start] > x > nums[end]"""
        end = len(nums) if end is None else end


        if start <= end:
            return x - nums[end]

        mid = (start + end) // 2

        if nums[]


    def threeSumClosest(self, nums: List[int], target: int) -> int:
        out = 1_0000_0000
        nums = sorted(nums)

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sums.add(nums[i] + nums[j])

        return 0


class SolutionTest(TestCase):

    def test__get_length_to_closest(self):
        for case, expected in [
            []
        ]:
            self.assertEqual()
    def test_performance(self):

        nums = {e: [randint(-1000, 1000) for _ in range(2**e)] for e in range(2, 4)}
        for sc in [OnHeadSolution]:
            for e in nums.keys():
                print(f"{sc.__name__} {e}", end='')
                time = timeit(lambda: sc().threeSumClosest(nums[e], 0), number=1)
                print(f"  time: {time:.3f} s")
