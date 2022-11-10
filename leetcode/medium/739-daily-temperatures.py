# #Medium
# https://leetcode.com/problems/daily-temperatures/description/
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
# is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for
# which this is possible, keep answer[i] == 0 instead.

from typing import List, Tuple
from unittest import TestCase


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ts: List[Tuple[int, int]] = []
        out: List[int] = [0]*len(temperatures)

        for i in range(len(temperatures)):
            # days = 0
            # while ts and temperatures[~i] > ts[~0][0]:
            #     days += ts[~0][1] + 1
            #     ts.pop()
            # ts.append((temperatures[~i], days))
            # out[~i] = days
            if temperatures[~i] > ts[~0][0]:
                ts[~0][1] += 1

            print(ts)

        return out


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [[88, 73, 74, 75, 71, 69, 72, 76, 73], [0, 1, 1, 4, 2, 1, 1, 0, 0]],
        ]:
            print(f"run test {case}")
            self.assertListEqual(expected, Solution().dailyTemperatures(case))

