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
from collections import defaultdict, Counter
from itertools import chain


class Solution:
    @staticmethod
    def _is_near_chars(char1: Tuple[int, int], char2: Tuple[int, int]) -> bool:
        return (char1[0] - char2[0]) ** 2 + (char1[1] - char2[1]) ** 2 == 1

    def exist(self, board: List[List[str]], word: str) -> bool:
        chars: Dict[chr, List[Tuple[int, int]]] = defaultdict(list)
        for x in range(len(board)):
            for y in range(len(board[0])):
                chars[board[x][y]].append((x, y))

        cntr = Counter(word)
        for c in set(word):
            if len(chars[c]) < cntr[c]:
                return False

        if cntr[word[0]] > cntr[word[~0]]:  # inverse word if it's better
            word = word[::-1]

        visited: List[Tuple[int, int]] = []
        potential: List[List[Tuple[int, int]]] = [chars[word[0]][:]]  # copy array

        while potential:
            if len(potential[~0]) == 0:
                potential = potential[:~0]
                visited = visited[:~0]
                continue

            visited.append(potential[~0].pop())
            if len(visited) == len(word):
                break

            potential.append([char for char in chars[word[len(visited)]]
                              if char not in visited and self._is_near_chars(char, visited[~0])])

        return ''.join(board[v[0]][v[1]] for v in visited) == word


class SolutionDfs:
    def exist(self, board: List[List[str]], word: str) -> bool:
        chars: Dict[chr, List[Tuple[int, int]]] = defaultdict(list)
        for x in range(len(board)):
            for y in range(len(board[0])):
                chars[board[x][y]].append((x, y))

        cntr = Counter(word)
        for c in set(word):
            if len(chars[c]) < cntr[c]:
                return False

        if cntr[word[0]] > cntr[word[~0]]:  # inverse word if it's better
            word = word[::-1]

        m, n = len(board), len(board[0])

        def dfs(i, j, word_offset) -> bool:
            if word_offset == len(word):
                return True

            if 0 <= i < m and 0 <= j < n and board[i][j] == word[word_offset]:  # [2] found a letter
                board[i][j] = "#"  # [3] mark as visited
                adj = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]  # [4] iterate over adjacent cells...
                dp = any(dfs(ii, jj, word_offset + 1) for ii, jj in adj)  # [5] ...and try next letter
                board[i][j] = word[word_offset]  # [6] remove mark
                return dp  # [7] return search result

            return False  # [8] this DFS branch failed

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))    # for i,j in product(range(m), range(n)


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, SolutionDfs]:
            for case, expected in [
                [([["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], "SEE"), True],
                [([["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]], "ABCB"), False],
                [([["A", "B", "C", "E"],
                   ["S", "F", "E", "S"],
                   ["A", "D", "E", "E"]], "ABCEFSADEESE"), True],
                [([["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"]], "AAAAAAAAAAAAAAB"), False],
                [([["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "B", "A", "A", "A"]], "AAAAAAAAAAAAAAB"), True],
                [([["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "B"],
                   ["A", "A", "A", "A", "B", "A"]], "AAAAAAAAAAAAABB"), False]
            ]:
                print(f"run test {sc.__name__} {case}")
                self.assertEqual(expected, sc().exist(*case))
