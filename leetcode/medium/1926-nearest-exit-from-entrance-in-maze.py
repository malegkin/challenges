# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+').
# You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of
# the cell you are initially standing at.
# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot
# step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell
# that is at the border of the maze. The entrance does not count as an exit.
# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
# Constraints:
#   maze.length == m
#   maze[i].length == n
#   1 <= m, n <= 100
#   maze[i][j] is either '.' or '+'.

from typing import List, Deque, Tuple
from unittest import TestCase
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x_min, x_max, y_min, y_max = 0, len(maze) - 1, 0, len(maze[0]) - 1
        steps: Deque[Tuple[int, int, int]] = deque([(*entrance, 0)])

        while steps:
            x, y, s = steps.popleft()

            if x < x_min or x > x_max or y < y_min or y > y_max or maze[x][y] == '+':
                continue

            if x in [x_min, x_max] or y in [y_min, y_max]:
                if s > 0:
                    return s

            maze[x][y] = '+'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                steps.append((x + dx, y + dy, s + 1))

        return -1


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]), 1],
            [([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]), 2],
            [([[".", "+"]], [0, 0]), -1]
        ]:
            print(f"run test {case}")
            self.assertEqual(expected, Solution().nearestExit(*case))
