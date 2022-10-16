# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all
# the jobs j where 0 <= j < i).#
# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each
# day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.
# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
# Constraints:
    # 1 <= jobDifficulty.length <= 300
    # 0 <= jobDifficulty[i] <= 1000
    # 1 <= d <= 10

import functools
from typing import List
from unittest import TestCase


class Solution:
    def minDifficulty(self, job_difficulty: List[int], days: int) -> int:
        n = len(job_difficulty)
        if n < days:
            return -1

        @functools.cache
        def dfs(i: int, d: int) -> int:
            if d == 1:
                return max(job_difficulty[i:])
            res, maxd = 2**31-1, 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, job_difficulty[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res

        return dfs(0, days)


class SolutionDpOnStak:
    def minDifficulty(self, job_difficulty: List[int], days: int) -> int:
        n = len(job_difficulty)
        if n < days:
            return -1

        dp, dp2 = [2**31-1] * n, [0] * n
        for day in range(days):
            stack = []
            for i in range(day, n):
                dp2[i] = dp[i - 1] + job_difficulty[i] if i else job_difficulty[i]
                while stack and job_difficulty[stack[-1]] <= job_difficulty[i]:
                    j = stack.pop()
                    dp2[i] = min(dp2[i], dp2[j] - job_difficulty[j] + job_difficulty[i])
                if stack:
                    dp2[i] = min(dp2[i], dp2[stack[-1]])
                stack.append(i)
            dp, dp2 = dp2, dp

        return dp[-1]


class TestSolution(TestCase):
    def test_solution(self):
        for solution in [Solution, SolutionDpOnStak]:
            for case, expected in [
                [([1, 1, 1], 3), 3],
                [([9, 9, 9], 4), -1],
                [([6, 5, 4, 3, 2, 1], 2), 7]
            ]:
                print(f"run_test {solution.__name__} {case}")
                self.assertEqual(expected, solution().minDifficulty(*case))
