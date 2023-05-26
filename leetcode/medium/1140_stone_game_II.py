# https://leetcode.com/problems/stone-game-ii/

# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile
# has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.
#
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
#
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.
# Then, we set M = max(M, X).
#
# The game continues until all the stones have been taken.
#
# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
# x
# Constraints:
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10^4

from functools import lru_cache
from typing import List, Tuple
from unittest import TestCase


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(maxsize=10_000)
        def _dp(i: int = 0, m: int = 1, is_alice: bool = True) -> Tuple[int, int]:
            if i + 2*m >= len(piles):
                piles_sum = sum(piles[i:])
                out = (piles_sum, 0) if is_alice else (0, piles_sum)
                # print(f"dp({i=}, {m=}, {is_alice=}) = {out=}")
                return out

            js = 0
            out = (0, 0)
            for j in range(i, i + 2*m):
                js += piles[j]
                a, b = _dp(j + 1, max(m, j - i + 1), not is_alice)
                a, b = (a + js, b) if is_alice else (a, b + js)
                if is_alice:
                    out = (a, b) if a > out[0] else out
                else:
                    out = (a, b) if b > out[1] else out

            # print(f"dp({i=}, {m=}, {is_alice=}) = {out=}")
            return out

        return _dp()[0]


class Solutionaa:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        memo = {}

        def dfs(i: int, M: int, isAlice: bool):
            """
            DP with memoization
                Args:
                    i: current starting index
                    M: M in the problem description
                    isAlice: whether the player is Alice or not
                Return
                    A tuple indicating the game outcome, where the first element is Alice's score and the second
                    element is Bob's score
            """
            # base case: alice or bob can pick all remaining piles
            if i >= N - 2 * M:
                s = sum(piles[i:])
                return (s, 0) if isAlice else (0, s)

            # recursive step: each player will maximize its gain
            if (i, M, isAlice) not in memo:
                s, a, b = 0, float('-inf'), float('-inf')
                for j in range(i, i + 2 * M):
                    s += piles[j]
                    nxt = dfs(j + 1, max(M, j - i + 1), not isAlice)
                    if isAlice and s + nxt[0] > a:
                        a, b = s + nxt[0], nxt[1]
                    elif not isAlice and s + nxt[1] > b:
                        a, b = nxt[0], s + nxt[1]
                memo[i, M, isAlice] = (a, b)

            return memo[i, M, isAlice]

        return dfs(0, 1, True)[0]


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [[2,7,9,4,4], 10],
            [[1,2,3,4,5,100], 104],
            [[3111,4303,2722,2183,6351,5227,8964,7167,9286,6626,2347,1465,5201,7240,5463,8523,8163,9391,8616,5063,7837,7050,1246,9579,7744,6932,7704,9841,6163,4829,7324,6006,4689,8781,621], 112766]
        ]:
            print(f"run test {case}")
            self.assertEqual(expected, Solution().stoneGameII(case))
