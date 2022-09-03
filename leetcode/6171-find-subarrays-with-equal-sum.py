# https://leetcode.com/contest/biweekly-contest-86/problems/find-subarrays-with-equal-sum/
# https://leetcode.com/problems/find-subarrays-with-equal-sum/

# Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.
#
# Return true if these subarrays exist, and false otherwise.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

from collections import defaultdict


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sub_arrays = defaultdict(int)
        for i in range(len(nums) - 1):
            sub_arrays[nums[i] + nums[i + 1]] += 1

        for sa in sub_arrays.values():
            if sa >= 2:
                return True

        return False

