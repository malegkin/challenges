# https://leetcode.com/problems/time-needed-to-inform-all-employees/

#   A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one
# with headID.
#   Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th
# employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.
#   The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his
# direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent
# news.
#   The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i]
# minutes, all his direct subordinates can start spreading the news).
#   Return the number of minutes needed to inform all the employees about the urgent news.

#   Constraints:
# 1 <= n <= 10^5
# 0 <= headID < n
# manager.length == n
# 0 <= manager[i] < n
# manager[headID] == -1
# informTime.length == n
# 0 <= informTime[i] <= 1000
# informTime[i] == 0 if employee i has no subordinates.
# It is guaranteed that all the employees can be informed.


from collections import defaultdict
from typing import List
from unittest import TestCase
from functools import cache


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employees = defaultdict(list)
        for employee_id, manager_id in enumerate(manager):
            employees[manager_id].append(employee_id)

        @cache
        def _dfs(head_id: int) -> int:
            return max(list(map(_dfs, employees[head_id])) or [0]) + informTime[head_id]

        return _dfs(headID)


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [(1, 0, [-1], [0]), 0],
            [(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]), 1]
        ]:
            print(f"run test{case}")
            self.assertEqual(expected, Solution().numOfMinutes(*case))
