# https://leetcode.com/problems/number-of-provinces/
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and
# city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
# connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Constraints:
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]


from unittest import TestCase
from typing import List, Dict, Set, Tuple
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected: Dict[int, List[int]] = defaultdict(list)
        visited: Set[int] = set()

        for i in range(len(isConnected)):
            connected[i] = [j for j in range(len(isConnected)) if isConnected[i][j] == 1]

        def _dfs(city_id: int):
            for next_city_id in connected[city_id]:
                if next_city_id not in visited :
                    visited.add(next_city_id)
                    _dfs(next_city_id)


        out = 0
        for i in connected.keys():
            for j in connected[i]:
                if j not in visited:
                    _dfs(j)
                    out += 1

        return out


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [[[1,1,0],
              [1,1,0],
              [0,0,1]], 2],
            [[[1,0,0],
              [0,1,0],
              [0,0,1]], 3],
            [[[1,0,0,0,1,0], #((1,5), (5,6)) && ((2,3), (3,4))
              [0,1,1,0,0,0],
              [0,1,1,1,0,0],
              [0,0,1,1,0,0],
              [1,0,0,0,1,1],
              [0,0,0,0,1,1]], 2],
            [[[1, 0, 0, 1],  # (1,4), (2,3) (3,4)
              [0, 1, 1, 0],
              [0, 1, 1, 1],
              [1, 0, 1, 1]], 1]
        ]:
            print(f"run test {case}")
            self.assertEqual(expected, Solution().findCircleNum(case))
