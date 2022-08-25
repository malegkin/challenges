# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.

import unittest


class HeadOnSolution:
    """ Runtime: O(n^3) 658 ms, faster than 13.67% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: O(n) - 14.1 MB, less than 50.26% of Python3 online submissions for Longest Substring Without Repeating Characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        out = 1
        for i in range(len(s) - 1):
            j = i
            while j < len(s) and s[j] not in s[i:j]:
                j += 1

            out = j-i if j-i > out else out

        return out


class Solution:
    """ Runtime: O(n) 101 ms ms, faster than 57.25% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: O(1) - 14.2 MB, less than 13.97% of Python3 online submissions for Longest Substring Without Repeating Characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        out = 0
        i, j = 0, 0
        index = {}
        for j in range(len(s)):
            if s[j] in index:
                out = max(j-i, out)
                for i in range(i, index[s[j]]):
                    del(index[s[i]])
                i = min(j, index[s[j]] + 1)
                index[s[j]] = j
            else:
                index[s[j]] = j

        return max(j-i+1, out)


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for solution_class in [HeadOnSolution, Solution]:
            solution = solution_class()
            for s, result in [["", 0], ["b", 1], ["a", 1], ["au", 2], ["abba", 2], ["bbbbb", 1], ["pwwkew", 3], ["abcabcbb", 3]]:
                print(f"test {solution_class} {s}")
                self.assertEqual(result, solution.lengthOfLongestSubstring(s))


if __name__ == 'main':
    unittest.main()
