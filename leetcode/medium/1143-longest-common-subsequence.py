# LCS Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
# subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
# Constraints:
#        1 <= text1.length, text2.length <= 1000
#       text1 and text2 consist of only lowercase English characters.

from unittest import TestCase

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Idea: memo[i][j] = memo[i-1][j-1] + 1 if text1[j] == text2[j] else max(memo[i][j-1], memo[i-1][j])
        memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1) ]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    memo[i+1][j+1] = memo[i][j] + 1
                else:
                    memo[i+1][j+1] = max(memo[i+1][j], memo[i][j+1])
        return max((max(row) for row in memo))


class SolutionTest(TestCase):
    def test_solution(self):
        for case, expected in [
            [("abcde", "ace"), 3],
            [("abc", "abc"), 3],
            [("abc", "def"), 0]
        ]:
            print(f"run test {case}")
            self.assertEqual(expected, Solution().longestCommonSubsequence(*case))
