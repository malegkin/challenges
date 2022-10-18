# https://leetcode.com/problems/3sum-closest/
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
# closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
# Constraints:
#
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10**4 <= target <= 10**4


from typing import List
from unittest import TestCase
from timeit import timeit
from random import randrange


class OnHeadSolution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        out = 1_0000_0000

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum_ij = nums[i] + nums[j]
                for k in range(j+1, len(nums)):
                    sum_ijk = sum_ij + nums[k]
                    out = sum_ijk if abs(target - out) > abs(target - sum_ijk) else out
                    if out == target:
                        return target

        return out


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current

        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key=lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k + 1]):
            if i > 0 and x == nums[i - 1]:
                continue
            current = self.KSumClosest(nums[i + 1:], k - 1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest


class TestSolution(TestCase):

    def test_solution(self):
        for sc in [OnHeadSolution, Solution]:
            for case, expected in [
                [[[-1, 2, 1, -4], 1], 2],
                [[[0, 0, 0], 1], 0]
            ]:
                print(f"{sc.__name__} {case}")
                self.assertEqual(expected, sc().threeSumClosest(*case))

    def test_performance(self):
        nums = {e: [randrange(-1000, 1000, 2) for _ in range(2**e)] for e in range(5, 10)}
        for sc in [OnHeadSolution, Solution]:
            for e in nums.keys():
                print(f"{sc.__name__} {e}", end='')
                time = timeit(lambda: sc().threeSumClosest(nums[e], 5), number=1)
                print(f"  time: {time:.3f} s")
