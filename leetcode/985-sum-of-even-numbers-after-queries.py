# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# You are given an integer array nums and an array queries where queries[i] = [vali, indexi].
#
# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.
#
# Return an integer array answer where answer[i] is the answer to the ith query.
#
#

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(v for v in nums if v % 2 == 0)
        res: list[int] = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            nums[idx] += val

            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            res.append(even_sum)

        return res
