# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
# You are playing a game that contains multiple characters, and each of the characters has two main properties:
# attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei]
# represents the properties of the ith character in the game.
# A character is said to be weak if any other character has both attack and defense levels strictly greater than this
# character's attack and defense levels. More formally, a character i is said to be weak if there exists another
# character j where attackj > attacki and defensej > defensei.
# Return the number of weak characters.
# Constraints:
# 2 <= properties.length <= 10^5
# properties[i].length == 2
# 1 <= attack[i], defense[i] <= 10^5

from typing import List
from unittest import TestCase


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # order by attack desc
        properties.sort(key=lambda x: (-x[0], x[1]))

        out = 0
        max_defense = 0

        for _, defense in properties:
            if defense < max_defense:
                out += 1
            else:
                max_defense = defense

        return out


class TestSolution(TestCase):
    def test_solution(self):
        for solution_class in [Solution]:
            for case, expected in [
                [[[2, 2], [3, 3]], 1],
                [[[1, 5], [10, 4], [4, 3]], 1],
                [[[5, 5], [6, 3], [3, 6]], 0],
                [[[9, 5], [8, 4], [7, 6], [6, 6], [6, 5], [6, 4], [1, 1]], 4]
            ]:
                print(f"run test {solution_class.__name__} {case}")
                self.assertEqual(expected, solution_class().numberOfWeakCharacters(case))
