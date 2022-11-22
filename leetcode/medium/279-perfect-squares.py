# https://leetcode.com/problems/perfect-squares/
# Given an integer n, return the least number of perfect square numbers that sum to n.
#
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer
# with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
# Constraints:
#   1 <= n <= 10_000
import sys
from unittest import TestCase
from functools import cache
from typing import List, Optional

sys.setrecursionlimit(100_000)


class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [x*x for x in range(1, 100)]     # 1, 4, 9, 16, 25, 36, 49, 64, 81
        perfect_squares_set = set(perfect_squares)

        queue, cache = [n], {n: 1}

        while queue:
            val = queue.pop(0)
            if val in perfect_squares_set:
                return cache[val]

            for ps in perfect_squares:
                if val - ps > 0 and val - ps not in cache:
                    queue.append(val - ps)
                    cache[val - ps] = cache[val] + 1
        return -1


class SolutionBruteForce:
    def numSquares(self, n: int) -> int:
        perfect_squares = [x*x for x in range(1, 100)]     # 1, 4, 9, 16, 25, 36, 49, 64, 81
        perfect_squares_set = set(perfect_squares)

        @cache
        def get_nums(x: int) -> int:
            if x in perfect_squares_set:
                return 1

            return min([get_nums(x - ps) for ps in perfect_squares if ps < x]) + 1

        return get_nums(n)


class SolutionList:
    def numSquares(self, n: int) -> int:
        perfect_squares = [x*x for x in range(1, 100)]     # 1, 4, 9, 16, 25, 36, 49, 64, 81
        perfect_squares_set = set(perfect_squares)

        @cache
        def get_nums(x: int) -> List[int]:
            if x in perfect_squares_set:
                return [x]

            return min([get_nums(x - ps) + [ps] for ps in perfect_squares if ps < x], key=len)

        return len(get_nums(n))


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, SolutionBruteForce]:
            for case, expected in [
                [12, 3],        # 4+4+4
                [13, 2],        # 9+4
                [6337, 2],
                [6922, 2]
            ]:
                print(f"run_test {sc.__name__} {case}")
                self.assertEqual(expected, sc().numSquares(case))
