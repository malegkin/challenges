# https://leetcode.com/problems/stone-game-ii/

# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile
# has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.
#
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
#
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.
# Then, we set M = max(M, X).
#
# The game continues until all the stones have been taken.
#
# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
# x
# Constraints:
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10^4

from typing import List, Tuple, Optional
from unittest import TestCase
from collections import deque


class LRUCache(dict):
    def __init__(self, max_size: Optional[int], **kwargs):
        super().__init__(**kwargs)
        self._max_size = max_size
        self._lru = deque()

    def __getitem__(self, key):
        if self._max_size is not None:
            self._lru.remove(key)
            self._lru.append(key)
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if self._max_size is not None:
            while len(self._lru) >= self._max_size:
                last = self._lru.popleft()
                del self[last]

            self._lru.append(key)
        return super().__setitem__(key, value)


def memoization(maxsize):
    _lru = LRUCache(max_size=maxsize)
    def wrapper(foo):
        def inner(*args, **kwargs):
            if len(kwargs) > 0:
                raise Exception("ooo")

            if args not in _lru:
                _lru[args] = foo(*args)

            return _lru[args]

        return inner
    return wrapper


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @memoization(maxsize=None)
        def _dp(i: int = 0, m: int = 1, is_alice: bool = True) -> Tuple[int, int]:
            if i + 2*m >= len(piles):
                piles_sum = sum(piles[i:])
                out = (piles_sum, 0) if is_alice else (0, piles_sum)
                # print(f"dp({i=}, {m=}, {is_alice=}) = {out=}")
                return out

            js = 0
            out = (0, 0)
            for j in range(i, i + 2*m):
                js += piles[j]
                a, b = _dp(j + 1, max(m, j - i + 1), not is_alice)
                a, b = (a + js, b) if is_alice else (a, b + js)
                if is_alice:
                    out = (a, b) if a > out[0] else out
                else:
                    out = (a, b) if b > out[1] else out

            # print(f"dp({i=}, {m=}, {is_alice=}) = {out=}")
            return out

        return _dp()[0]


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [[2,7,9,4,4], 10],
            [[1,2,3,4,5,100], 104],
            [[3111,4303,2722,2183,6351,5227,8964,7167,9286,6626,2347,1465,5201,7240,5463,8523,8163,9391,8616,5063,7837,7050,1246,9579,7744,6932,7704,9841,6163,4829,7324,6006,4689,8781,621], 112766],
            [[5819,9551,3626,8100,6991,4067,581,3914,895,9859,3463,4463,851,1993,6596,408,2950,5818,1433,6552,8416,837,7084,5066,1514,6417,9411,9331,5321,7705,1376,6956,6964,2371,5858,9570,6367,9973,7921,2004,8642,8935,861,3857,7807,5708,5020,4558,9641,2286,7931,9637,7542,5899,3814,491,6356,9458,9074,8037,7722,5403,7363,8774,9165,3799,7304,2596,2319,5555,3382,8311,6396,7246,2193,7019,3019,4814,6450,1934,9388,4501,909,215,1656,3799,6611,8907,739,2678,1342,8707,4648,4223,5271,5970,9702,9413,6121,3915],276186 ],
            [[2370,1306,2155,5531,9889,2452,5197,2623,8564,8804,71,1879,2153,1781,5372,9327,6143,5253,3887,2333,2385,7492,6274,6506,7740,3894,9108,1509,9248,926,9599,443,5920,7367,5831,2012,544,8928,9981,316,7589,7165,5267,2464,8013,1538,2283,3252,1998,2535,6376,5640,7168,4325,1900,6930,7020,4719,7633,2836,6668,6784,113,5283,7318,528,9122,3731,1920,5235,2758,4666,6303,4991,4330,8739,3028,7733,8563,1454,3555,7191,1606,8498,6547,6295,6971,2808,3349,6097,3440,7855], 0]
        ]:
            print(f"run test {case}")
            self.assertEqual(expected, Solution().stoneGameII(case))

    def test_lru_cache(self):
        lru = LRUCache(max_size=3)
        lru[1] = 321
        lru[2] = 321
        lru[3] = 321
        lru[1]

        assert lru == {1: 321, 2: 321, 3: 321}
        lru[4] = 321

        assert lru == {1: 321, 3: 321, 4: 321}
        lru[5] = 321

        assert lru == {1: 321, 4: 321, 5: 321}
        lru[6] = 321
        assert lru == {4: 321, 5: 321, 6: 321}
