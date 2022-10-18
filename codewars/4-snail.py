# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

from unittest import TestCase


def snail(snail_map):
    out = list()
    n = len(snail_map)
    if n == 1:
        return snail_map[0]

    for x in range(n):
        i = x
        for j in range(x, n - x):
            out.append(snail_map[i][j])
        for i in range(x + 1, n - x):
            out.append(snail_map[i][j])
        for j in range(n - x - 2, x - 1, -1):
            out.append(snail_map[i][j])
        for i in range(n - x - 2, x, -1):
            out.append(snail_map[i][j])

    return out


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]],
            [[[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
            [[[1, 2, 3, 1], [4, 5, 6, 4], [7, 8, 9, 7], [7, 8, 9, 7]], [1, 2, 3, 1, 4, 7, 7, 9, 8, 7, 7, 4, 5, 6, 9, 8]]
        ]:
            self.assertCountEqual(expected, snail(case))

