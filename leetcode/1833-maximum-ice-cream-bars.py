# https://leetcode.com/problems/maximum-ice-cream-bars/
# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the
# ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as
# possible.
# Return the maximum number of ice cream bars the boy can buy with coins coins.
# Note: The boy can buy the ice cream bars in any order.
# Constraints:
#   costs.length == n
#   1 <= n <= 10**5
#   1 <= costs[i] <= 10**5
#   1 <= coins <= 10**8


from typing import List
from unittest import TestCase
from bisect import bisect_right
from itertools import accumulate


class Solution:
    """
        Time complexity: O(NlogN)
        Space complexity: O(N)
    """
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        out = 0
        costs = sorted(costs)

        while out < len(costs) and coins >= costs[out]:
            coins -= costs[out]
            out += 1

        return out


class SolutionOneLiner:
    """
        Time complexity: O(NlogN)
        Space complexity: O(N)
    """
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return bisect_right(list(accumulate([0] + sorted(costs))), coins) - 1


class TestSolution(TestCase):
    def test_solution(self):
        for solution in [Solution, SolutionOneLiner]:
            for case, expected in [
                [([1, 3, 2, 4, 1], 7), 4],
                [([10, 6, 8, 7, 7, 8], 5), 0],
                [([1, 6, 3, 1, 2, 5], 20), 6]
            ]:
                print(f"run_test {solution.__name__} {case}")
                self.assertEqual(expected, solution().maxIceCream(*case))
