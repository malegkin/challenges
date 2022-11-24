# https://leetcode.com/problems/valid-sudoku/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#   Each row must contain the digits 1-9 without repetition.
#   Each column must contain the digits 1-9 without repetition.
#   Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
#   A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#   Only the filled cells need to be validated according to the mentioned rules.

# Constraints:
#   board.length == 9
#   board[i].length == 9
#   board[i][j] is a digit 1-9 or '.'

from unittest import TestCase
from typing import List
from string import digits
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def _is_valid_block(block: List[str]) -> bool:
            cntr = Counter(block)
            cntr.pop(".")
            for k, v in cntr.items():
                if k not in digits or v != 1:
                    return False

            return True

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                block = []
                for i in range(9):
                    block.append(board[x + i // 3][y + i % 3])
                if not _is_valid_block(block):
                    return False

        for y in range(9):
            block = []
            for x in range(9):
                block.append(board[x][y])
            if not _is_valid_block(block):
                return False

        return all(_is_valid_block(board[x]) for x in range(9))


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
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]], True],
            [[["8", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False],

        ]:
            self.assertEqual(expected, Solution().isValidSudoku(case))
