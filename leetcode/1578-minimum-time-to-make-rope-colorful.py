# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the
# ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks
# Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array
# neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
# Return the minimum time Bob needs to make the rope colorful.


from typing import List
from unittest import TestCase


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        out = prev_time = 0
        for i in range(len(colors)):
            if i > 0 and colors[i-1] != colors[i]:
                prev_time = 0
            out += min(prev_time, neededTime[i])
            prev_time = max(prev_time, neededTime[i])
        return out


class DpSolution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        def dp(colors: List[chr], times: List[int]) -> int:
            for_del = []

            i = 0
            while i+1 < len(colors):
                if colors[i] == colors[i+1]:
                    j = i if times[i] < times[i+1] else i+1
                    for_del.append(j)
                    i += 1
                i += 1

            if len(for_del) > 0:
                out = 0
                for i, j in enumerate(for_del):
                    colors.pop(j - i)
                    out += times.pop(j - i)

                return out + dp(colors, times)

            return 0

        return dp(list(colors), neededTime)


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, DpSolution]:
            for case, expected in [
                [["abaac", [1, 2, 3, 4, 5]], 3],
                [["abc", [1, 2, 3]], 0],
                [["aabaa", [1, 2, 3, 4, 1]], 2],
                [["cabbabbbaca", [6, 1, 8, 4, 1, 10, 6, 9, 10, 2, 10]], 19]
            ]:
                print(f"run_test {sc.__name__} {case}")
                self.assertEqual(expected, sc().minCost(*case))
