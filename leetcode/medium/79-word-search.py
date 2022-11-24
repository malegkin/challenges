# https://leetcode.com/problems/word-search/
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once.
# Constraints:
#       m == board.length
#       n = board[i].length
#       1 <= m, n <= 6
#       1 <= word.length <= 15
#       board and word consists of only lowercase and uppercase English letters.
import typing
from typing import List, Tuple, Dict, Set
from unittest import TestCase
from collections import defaultdict


class Solution:
    @staticmethod
    def _is_near_chars(char1: Tuple[int, int], char2: Tuple[int, int]) -> bool:
        return (char1[0] - char2[0]) ** 2 + (char1[1] - char2[1]) ** 2 == 1

    def exist(self, board: List[List[str]], word: str) -> bool:
        chars: Dict[chr, List[Tuple[int, int]]] = defaultdict(list)
        x_min, x_max, y_min, y_max = 0, len(board) - 1, 0, len(board[0])

        for x in range(len(board)):
            for y in range(len(board[0])):
                chars[board[x][y]].append((x, y))


        return False


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [([["A", "B", "C", "E"],
               ["S", "F", "C", "S"],
               ["A", "D", "E", "E"]], "SEE"), True],
            [([["A", "B", "C", "E"],
               ["S", "F", "C", "S"],
               ["A", "D", "E", "E"]], "ABCB"), False]
        ]:
            print(f"run test {case}")
            self.assertEqual(expected, Solution().exist(*case))
