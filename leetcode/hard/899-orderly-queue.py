# #Hard
# https://leetcode.com/problems/orderly-queue/
# You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of
# the string..
# Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.
# Constraints:
#   1 <= k <= s.length <= 1000
#   s consist of lowercase English letters.



from unittest import TestCase
from collections import deque


class Solution:
    """
        Time Complexity: O(N ^ 2)
        Space Complexity: O(N)
    """

    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            # only cyclic strings: abc -> bca -> cab -> abc
            # python compare two string lexography
            return min(s[i:] + s[:i] for i in range(len(s)))

        # k == 2  like insertion sort: can move any character to any position by swapping two adjacent characters
        # abcdef -> bcdefa -> bdefac -> befacd -> bfacde -> bacdef

        return "".join(sorted(s))


class SolutionOneLine:
    def orderlyQueue(self, s: str, k: int) -> str:
        return min(s[i:] + s[:i] for i in range(len(s))) if k == 1 else ''.join(sorted(list(s)))


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [SolutionOneLine]:
            for case, expected in [
                [("cba", 1), "acb"],
                [("baaca", 3), "aaabc"]
            ]:
                print(f"run_test {sc.__name__} {case}")
                self.assertEqual(expected, sc().orderlyQueue(*case))
