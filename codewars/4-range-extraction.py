# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

# A format for expressing an ordered list of integers is to use a comma separated list of either
#     individual integers
#     or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The
# range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at
# least 3 numbers. For example "12,13,15-17"
#
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
# in the range format.

from unittest import TestCase
from typing import List


def solution(args: List[int]) -> str:
    args = sorted(args)
    out: List[List[int]] = [[args[0], args[0]]]

    for i in range(1, len(args)):
        if args[i] - out[~0][~0] == 1:
            out[~0][~0] = args[i]
        else:
            out.append([args[i], args[i]])

    return ",".join([str(o[0]) if o[0] == o[1] else
                     f"{o[0]},{o[1]}" if o[1]-o[0] == 1 else f"{o[0]}-{o[1]}" for o in out])


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [[-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20], '-6,-3-1,3-5,7-11,14,15,17-20'],
            [[-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], '-3--1,2,10,15,16,18-20']
        ]:
            print(f"run_case {case}")
            self.assertEqual(expected, solution(case))
