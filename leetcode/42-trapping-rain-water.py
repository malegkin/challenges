# https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
# it can trap after raining.
# Constraints:
#   n == height.length
#   1 <= n <= 2 * 10^4
#   0 <= height[i] <= 10^5

from typing import List


class Solution:
    """
        Time Complexity: O(n)
        Auxiliary Space: O(1)
    """
    def trap(self, height: List[int]) -> int:
        out = 0

        max_left, max_right = height[0], height[-1]
        i, j = 1, len(height) - 2

        while i <= j:
            max_left = max(max_left, height[i])
            max_right = max(max_right, height[j])
            if max_left < max_right:
                out += max_left - height[i]
                i += 1
            else:
                out += max_right - height[j]
                j -= 1

        return out


