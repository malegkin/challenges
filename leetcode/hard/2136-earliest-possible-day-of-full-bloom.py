# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
# Hard
# You have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed
# takes time and so does the growth of a seed. You are given two 0-indexed integer arrays plantTime and growTime, of
# length n each:
#   plantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can work on planting
# exactly one seed. You do not have to work on planting the same seed on consecutive days, but the planting of a seed is
# not complete until you have worked plantTime[i] days on planting it in total.
#   growTime[i] is the number of full days it takes the ith seed to grow after being completely planted. After the last
#   day of its growth, the flower blooms and stays bloomed forever.
# From the beginning of day 0, you can plant the seeds in any order.
# Return the earliest possible day where all seeds are blooming.

from typing import List
from unittest import TestCase


class Solution:
    """
    Time Complexity: zip + sort + linear scan -> total O(N*lg(N))
    Space Complexity: O(n)

    1. select grow_time, plant_time order by grow, plant desc ## plant plants in desc order of growing and plant time
    2. get max of plant_time_total + grow_time of plants ## max - until all plants grow
    """
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        out = 0
        plant_time_total = 0

        for grow_time, plant_time in sorted(zip(growTime, plantTime), reverse=True):
            # print(f"{' '*plant_time_total}{'.'*plant_time}{'^'*grow_time}")
            plant_time_total += plant_time
            out = max(out, plant_time_total + grow_time)

        return out


class SolutionOneLine:
    def earliestFullBloom(self, pts: List[int], gts: List[int]) -> int:
        return max((ptt := ptt + pt if 'ptt' in locals() else pt) + gt for gt, pt in reversed(sorted(zip(gts, pts))))


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, SolutionOneLine]:
            for case, expected in [
                [([1], [1]), 2],
                [([1, 4, 3], [2, 3, 1]), 9],
                [([1, 2, 3, 2], [2, 1, 2, 1]), 9]
            ]:
                print(f"run_test {sc.__name__} {case}")
                self.assertEqual(expected, sc().earliestFullBloom(*case))

