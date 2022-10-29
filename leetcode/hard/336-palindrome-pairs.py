# https://leetcode.com/problems/palindrome-pairs/
# Hard
# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the
# concatenation of the two words words[i] + words[j] is a palindrome.
# Constraints:
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.

from typing import List
from unittest import TestCase


class Solution:
    # O(n^2)
    # Time Limit Exceeded
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s: str) -> bool:
            for i in range(len(s)//2):
                if s[i] != s[~i]:
                    return False

            return True

        out: List[List[int]] = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if len(words[i]) > 0 and len(words[j]) > 0 and words[i][0] != words[j][-1]:
                    continue
                if is_palindrome(words[i] + words[j]):
                    out.append([i, j])

        return out


class TestSolution(TestCase):
    def test_solution(self):
        for solution_class in [Solution]:
            for case, expected in [
                [["bat", "tab", "cat"], [[0, 1], [1, 0]]],
                [["a", ""], [[0, 1], [1, 0]]],
                [["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]]
            ]:
                print(f"run_test {solution_class.__name__} {case}")
                self.assertCountEqual(expected, solution_class().palindromePairs(case))
