# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b
# == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

# Constraints:
# 1 <= a, b, c <= 10^9


from unittest import TestCase
from typing import List


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        out = 0

        while not a == b == c == 0:
            a, a_mod = divmod(a, 2)
            b, b_mod = divmod(b, 2)
            c, c_mod = divmod(c, 2)

            if a_mod + b_mod == 2 and c_mod == 0:
                out += 2
            elif a_mod + b_mod == 0 and c_mod == 1:
                out += 1
            elif a_mod != b_mod and c_mod == 0:
                out += 1

        return out

class Solution2:

    @staticmethod
    def __int_to_binary(n: int) -> List[int]:
        out = []
        while n > 0:
            out.append(n%2)
            n = n // 2

        return list(reversed(out)) if len(out) > 0 else [0]

    def minFlips(self, a: int, b: int, c: int) -> int:
        out = 0
        a, b, c = list(map(self.__int_to_binary, [a, b, c]))
        n = max(len(a), len(b), len(c))
        a, b, c = list(map(lambda l: [0]*(n-len(l)) + l, [a, b, c]))

        for i in range(n):
            if a[i] + b[i] == 2:
                out += 0 if c[i] == 1 else 2
            elif a[i] + b[i] == 1:
                out += 0 if c[i] == 1 else 1
            else:
                out += 1 if c[i] == 1 else 0

        return out

class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, Solution2]:
            for case, expected in [
                [(2, 6, 5), 3],
                [(4, 2, 7), 1],
                [(1, 2, 3), 0],
                [(7, 7, 7), 0]
            ]:
                print(f"run test {sc.__name__=} {case=}")
                self.assertEqual(expected, sc().minFlips(*case))
