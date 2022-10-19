# https://leetcode.com/problems/push-dominoes/
# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push
# some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the
# dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or
# already fallen domino.
# You are given a string dominoes representing the initial state where:
#   dominoes[i] = 'L', if the ith domino has been pushed to the left,
#   dominoes[i] = 'R', if the ith domino has been pushed to the right, and
#   dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.

from unittest import TestCase


class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        prev_dominoes = ''
        while dominoes != prev_dominoes:
            prev_dominoes = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')
            dominoes = dominoes.replace('R.', 'RR')
            dominoes = dominoes.replace('.L', 'LL')

        return dominoes.replace('xxx', 'R.L')


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            ["..L.", "LLL."],
            ["RR.L", "RR.L"],
            [".R..", ".RRR"],
            ["R.R.L", "RRR.L"],
            [".L.R...LR..L..", "LL.RR.LLRRLL.."]
        ]:
            self.assertEqual(expected, Solution().pushDominoes(case))
