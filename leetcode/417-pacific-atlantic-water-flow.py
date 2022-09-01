# https://leetcode.com/problems/pacific-atlantic-water-flow/ There is an m x n rectangular island that borders both
# the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic
# Ocean touches the island's right and bottom edges. The island is partitioned into a grid of square cells. You are
# given an m x n integer matrix heights where heights[ r][c] represents the height above sea level of the cell at
# coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly
# north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
# Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (
# ri, ci) to both the Pacific and Atlantic oceans.

# Constraints:
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105


import unittest
from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
            Time Complexity: O(n*m)
            Auxiliary Space: O(n*m)
        """

        def _coord2int(i: int, j: int) -> int:
            """ representing 2D coordinates as a integer """
            return (i << 16) | j

        def _dfs(i: int, j: int, prev_height: int, coords: Set[int]) -> None:
            """ depth-first search ocean connected coords"""
            # out of bounds
            if i < 0 or i == m or j < 0 or j == n:
                return

            if _coord2int(i, j) in coords:
                return

            height = heights[i][j]
            # water can't flow to a higher height
            if height < prev_height:
                return

            # add current point to ocean reachable coords list
            coords.add(_coord2int(i, j))

            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                _dfs(i + di, j + dj, height, coords)

        ###########
        m, n = len(heights), len(heights[0])

        pacific_coords = set()

        # top row
        for j in range(n):
            _dfs(0, j, 0, pacific_coords)

        # left col
        for i in range(m):
            _dfs(i, 0, 0, pacific_coords)

        atlantic_coords = set()

        # right col
        for i in range(m):
            _dfs(i, n - 1, 0, atlantic_coords)

        # bottom row
        for j in range(n):
            _dfs(m - 1, j, 0, atlantic_coords)

        # intersection of coords reachable from both Pacific and Atlantic
        return [[coord >> 16, coord & 0xFF] for coord in (pacific_coords & atlantic_coords)]


class TestSolution(unittest.TestCase):
    def test_solution(self):

        for solution_class in [Solution]:
            solution = solution_class()
            for heights, expected in [
                [
                    [[1]],
                    [[0, 0]]
                ], [
                    [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
                    [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
                ]
            ]:
                self.assertListEqual(sorted(solution.pacificAtlantic(heights)), sorted(expected))