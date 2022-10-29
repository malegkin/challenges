# https://leetcode.com/problems/string-compression-ii/description/
# Hard
# Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated
# 2 or more times) with the concatenation of the character and the number marking the count of the characters (length
# of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the
# compressed string becomes "a2bc3".
# Notice that in this problem, we are not adding '1' after single characters.
#
# Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.
#
# Find the minimum length of the run-length encoded version of s after deleting at most k characters.

# Constraints:
#   1 <= s.length <= 100
#   0 <= k <= s.length
# s contains only lowercase English letters.

from functools import cache
from unittest import TestCase


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def f(start, pre, last_count, left) -> int:
            if left < 0:
                return 1_0000_000
            if len(s) - start <= left:
                return 0

            if s[start] == pre:
                incr = 1 if last_count in (1, 9, 99) else 0
                return incr + f(start + 1, pre, last_count + 1, left)
            else:
                keep = 1 + f(start + 1, s[start], 1, left)
                delete = f(start + 1, pre, last_count, left - 1)
                return min(keep, delete)

        return f(0, "", 0, k)


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [("aaabcccd", 2), 4],
            [("aabbaa", 2), 2],
            [("aaaaaaaaaaa", 0), 3],
            [("bbaabdacddabaddbcaacbccaaccaadbdcdddcabbbadadcb", 16), 19]
        ]:
            print(f"run_test {case}")
            self.assertEqual(expected, Solution().getLengthOfOptimalCompression(*case))
