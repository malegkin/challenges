# https://leetcode.com/problems/median-of-two-sorted-arrays/
# hard
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n))

from typing import List
import unittest


class Solution:
    @staticmethod
    def mergeNums(nums1: List[int], nums2: List[int]) -> List[int]:
        out = []

        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                out.append(nums1[i1])
                i1 += 1
            else:
                out.append(nums2[i2])
                i2 += 1

        out = out + nums1[i1:]
        out = out + nums2[i2:]

        return out

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.mergeNums(nums1, nums2)

        if len(nums) % 2 == 0:
            return (float(nums[len(nums)//2]) + float(nums[len(nums)//2 - 1])) / 2
        else:
            return float(nums[len(nums)//2])


class TestSolution(unittest.TestCase):
    def test_mergeNums(self):
        for nums1, nums2, nums in [[[1], [2, 3], [1, 2, 3]],
                                   [[1, 2, 5], [3, 4], [1, 2, 3, 4, 5]],
                                   [[2, 4], [1, 3, 5], [1, 2, 3, 4, 5]]]:
            self.assertListEqual(nums, Solution.mergeNums(nums1, nums2))

    def test_solutuin(self):
        for nums1, nums2, median in [[[1, 3], [2], 2.0],
                                     [[1, 2], [3, 4], 2.5]]:
            solution = Solution()
            self.assertEqual(median, solution.findMedianSortedArrays(nums1, nums2))


if __name__ == 'main':
    unittest.main()

