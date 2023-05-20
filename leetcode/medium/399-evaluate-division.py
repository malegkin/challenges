# https://leetcode.com/problems/evaluate-division/

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi]
# and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer
# for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and
# that there is no contradiction.

# Constraints:
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.

from abc import ABC, abstractmethod
from collections import defaultdict, deque
from typing import List, Dict
from unittest import TestCase


class AbstractSolution(ABC):

    def __init__(self):
        self._graph: Dict[str, Dict[str, float]] = defaultdict(dict)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self._graph.clear()

        for [u, v], val in zip(equations, values):
            self._graph[u][v] = val
            self._graph[v][u] = 1 / val

        return [self._solve(*q) if q[0] in self._graph and q[1] in self._graph else -1.0
                for q in queries]

    @abstractmethod
    def _solve(self, x, y) -> float:
        pass


class DFSSolution(AbstractSolution):

    def _solve(self, x, y, visited=None) -> float:
        visited = set() if visited is None else visited

        visited.add(x)

        for key, val in self._graph[x].items():
            if key == y:
                return val

        for neighbor, weight in self._graph[x].items():
            if neighbor not in visited:
                if -1 != (out := weight * self._solve(neighbor, y, visited)):
                    return out

        return -1.0


class BFSSolution(AbstractSolution):

    def _solve(self, x, y):
        visited = set()
        queue = deque([(x, 1.0)])

        while queue:
            node, value = queue.popleft()

            if node == y:
                return value

            visited.add(node)

            for neighbor, weight in self._graph[node].items():
                if neighbor not in visited:
                    queue.append((neighbor, value * weight))

        return -1.0

class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]),
             [6.00000,0.50000,-1.00000,1.00000,-1.00000]],
            [([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]),
             [3.75000,0.40000,5.00000,0.20000]],
            [([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]),
            [0.50000,2.00000,-1.00000,-1.00000]]
        ]:
            for solution in [DFSSolution, BFSSolution]:
                print(f"run test {solution.__name__} {case}")
                self.assertListEqual(expected, solution().calcEquation(*case))