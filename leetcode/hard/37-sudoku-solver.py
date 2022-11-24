# https://leetcode.com/problems/sudoku-solver/description/
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
#   Each of the digits 1-9 must occur exactly once in each row.
#   Each of the digits 1-9 must occur exactly once in each column.
#   Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

import string
from typing import List, Tuple, Set
from unittest import TestCase


class Solution:
    digits = set(string.digits[1:])

    def _get_empty_cell(self) -> Tuple[int, int]:
        """
            return a first random free position or (-1, -1)
        """
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if self.board[x][y] == '.':
                    return x, y

        return -1, -1

    def _get_row(self, x, y) -> Set[chr]:
        return set(self.board[x])

    def _get_column(self, x, y):
        return set([row[y] for row in self.board])

    def _get_box(self, x, y):
        result = set()
        for rx in range(x // 3 * 3, x // 3 * 3 + 3):
            result.update(self.board[rx][y // 3 * 3:y // 3 * 3 + 3])
        return result

    def _get_posible(self, rx, cx):
        return self.digits - self._get_box(rx, cx) - self._get_row(rx, cx) - self._get_column(rx, cx)

    def _dfs(self) -> bool:
        x, y = self._get_empty_cell()
        if x == -1:
            return True

        for number in self._get_posible(x, y):
            self.board[x][y] = number
            if self._dfs():
                return True
            self.board[x][y] = "." # reset the number

        return False

    def __init__(self):
        self.board = None

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self._dfs()


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [[["5", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
             [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
              ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
              ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
              ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
              ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
              ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
              ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
              ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
              ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]]]:
            Solution().solveSudoku(case)
            self.assertCountEqual(expected, case)
