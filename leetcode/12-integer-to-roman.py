# https://leetcode.com/problems/integer-to-roman/
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply
# X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#       I can be placed before V (5) and X (10) to make 4 and 9.
#       X can be placed before L (50) and C (100) to make 40 and 90.
#       C can be placed before D (500) and M (1000) to make 400 and 900.

# Given an integer, convert it to a roman numeral.

from unittest import TestCase


class Solution:
    @staticmethod
    def roman_magic(n: int, x: str, v: chr, i: chr):

        return ['', f"{i}", f"{i}{i}", f"{i}{i}{i}", f"{i}{v}", f"{v}", f"{v}{i}", f"{v}{i}{i}", f"{v}{i}{i}{i}",
                f"{i}{x}"][n]

    def intToRoman(self, num: int) -> str:
        out = "M" * (num // 1000)
        for (d, x, v, i) in [[1000, 'M', 'D', 'C'],
                             [100,  'C', 'L', 'X'],
                             [10,   'X', 'V', 'I']
                             ]:
            num -= d * (num // d)
            out += self.roman_magic((num // (d // 10)), x, v, i)

        return out


class SolutionOneLine:
    def intToRoman(self, num: int) -> str:
        return ''.join([
            ['', f"{i}", f"{i*2}", f"{i*3}", f"{i}{v}", f"{v}", f"{v}{i}", f"{v}{i*2}", f"{v}{i*3}", f"{i}{x}"][int(f"{num:04d}"[d])]
            for (d, x, v, i) in [[0, 'M', 'M', 'M'], [1, 'M', 'D', 'C'], [2, 'C', 'L', 'X'], [3, 'X', 'V', 'I']]
        ])


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, SolutionOneLine]:
            for case, expected in [
                [3, "III"],
                [58, "LVIII"],
                [1994, "MCMXCIV"]
            ]:
                print(f"run {sc.__name__} {case:04d}")
                self.assertEqual(expected, sc().intToRoman(case))





