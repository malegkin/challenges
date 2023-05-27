# https://leetcode.com/problems/stone-game-iii/

#   1. Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each
# stone has an associated value which is an integer given in the array stoneValue.
#   2. Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones
# from the first remaining stones in the row.
#   3. The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.
#   4. The objective of the game is to end with the highest score, and the winner is the player with the highest score
# and there could be a tie. The game continues until all the stones have been taken.
#   5. Assume Alice and Bob play optimally.
#   6. Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.
#   Constraints:
# 1 <= stoneValue.length <= 5 * 10^4
# -1000 <= stoneValue[i] <= 1000


from unittest import TestCase
from typing import Tuple, List
from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def _dp(i: int = 0, is_alice_turn: bool = True) -> Tuple[int, int]:
            # return optimal game scores for Alice and Bob when start the game from i'th stone

            if i >= len(stoneValue):
                return 0, 0

            out = (-1_000_000, -1_000_000)
            for j in range(min(3, len(stoneValue) - i)):
                j_sum = sum(stoneValue[i:i+j+1])
                j_out = _dp(i + j + 1, not is_alice_turn)
                j_out = (j_out[0] + j_sum, j_out[1]) if is_alice_turn else (j_out[0], j_out[1] + j_sum)
                out = j_out if (is_alice_turn and out[0] < j_out[0]) or (not is_alice_turn and out[1] < j_out[1]) \
                    else out

            return out

        out = _dp()
        print(out)
        if out[0] == out[1]:
            return "Tie"

        return "Alice" if out[0] > out[1] else "Bob"


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [[1, 2, 3, -9], "Alice"],
            [[1, 2, 3, 6], "Tie"],
            [[1, 2, 3, 7], "Bob"]
        ]:
            print(f"run test {case}")
            self.assertEqual(expected, Solution().stoneGameIII(case))
