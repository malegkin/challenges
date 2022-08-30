# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

import unittest


def is_palindrome(s: str, start: int = 0, end: int = None) -> bool:
    end = len(s) - 1 if end is None else end

    for i in range((end - start + 1) // 2):
        if s[start + i] != s[end - i]:
            return False
    return True


class BruteForceSolution:
    """
    Time Complexity: O(n*n^2) TimeLimit Exceeded
    Auxiliary Space: O(n)
    """
    def longestPalindrome(self, s: str) -> str:
        out = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i + 1 > len(out) and is_palindrome(s, i, j):
                    out = s[i:j+1]

        return out


class Solution:
    """
    Time Complexity: O(n^2) 924 ms, faster than 70.56%
    Auxiliary Space: O(1)
    """
    def longestPalindrome(self, s: str) -> str:
        out = ""
        #  find for each character of string the maximum palindrome for which is the center
        for i in range(len(s)):
            # print(f"I=={i}")
            # check even length palindrome
            start, end = i, i+1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if (end - start + 1) > len(out):
                    out = s[start:end+1]
                    # print(f"even {start} - {end} == {out}")

                end += 1
                start -= 1

            # check odd length
            start, end = i, i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if (end - start + 1) > len(out):
                    out = s[start:end+1]
                    # print(f"odd {start} - {end} == {out}")

                end += 1
                start -= 1

        return out


class TestSolution(unittest.TestCase):
    def test_is_palindrom_function(self):
        for s, expected in [
            ["a",   True],
            ["ab",  False],
            ["aba", True],
            ["abba", True],
            ["abbc", False]
        ]:
            self.assertEqual(is_palindrome(s), expected)

    def test_solution(self):
        for solution_class in [BruteForceSolution, Solution]:
            solution = solution_class()
            for (s, expected) in [
                ["a", ["a"]],
                ["ccc", ["ccc"]],
                ["babad", ["bab", "aba"]],
                ["cabbbba", ["abbbba"]],
            ]:
                print(f"start test: {solution_class} '{s}'")
                self.assertIn(solution.longestPalindrome(s), expected)

    def test_long_string(self):

        s = "wgjtmwgpfnoeisdozatlhfvcqzlsffkoxrsdjhryqtppdeqrkjabodgtmkthwmtmerxlazsfdogsrwtswhbqclpcagfjlfuyvsnummfjmmxpdhupwkztnwcbppbbwfnwfaoazmautdiutzkwfqibglhypfamgxzsfctapkjimmyazulehprmzfvhaxzbobhvsbxscimjnmibivwbenfrhsudmpmkkbphjyrgjficjvfosrnhdsnjqtaycmyorpujyloozeeinqfsesuauqmsxmoafoszqrzbgechluecfdxulmcxxbiqvqkohlgqlqxierzbyradeoebbdhyjdkiaezfphfetiyelelunryvmczewjwkfrgjvdbouorqymmamkonncostamlpyrxoxnccbilnqdqbeieqncitfgitluvzxildtsiaipbskicepbvhtfdgxfiyywznzdstzvayjmwvlolhtvpekyakajeixdjkbbdlttldbbkjdxiejakaykepvthlolvwmjyavztsdznzwyyifxgdfthvbpeciksbpiaistdlixzvultigfticnqeiebqdqnlibccnxoxryplmatsocnnokmammyqrouobdvjgrfkwjwezcmvyrnuleleyitefhpfzeaikdjyhdbbeoedarybzreixqlqglhokqvqibxxcmluxdfceulhcegbzrqzsofaomxsmquausesfqnieezoolyjuproymcyatqjnsdhnrsofvjcifjgryjhpbkkmpmdushrfnebwvibimnjmicsxbsvhbobzxahvfzmrpheluzaymmijkpatcfszxgmafpyhlgbiqfwkztuidtuamzaoafwnfwbbppbcwntzkwpuhdpxmmjfmmunsvyufljfgacplcqbhwstwrsgodfszalxremtmwhtkmtgdobajkrqedpptqyrhjdsrxokffslzqcvfhltazodsieonfpgwmtjgw"
        for solution_class in [BruteForceSolution, Solution]:
            solution = solution_class()
            solution.longestPalindrome(s)
