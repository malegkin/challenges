# #Medium
# https://leetcode.com/problems/online-stock-span/
# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the
# current day. The span of the stock's price today is defined as the maximum number of consecutive days (starting from
# today and going backward) for which the stock price was less than or equal to today's price.
# For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be
# [1,1,1,2,1,4,6].
# Implement the StockSpanner class:
#       StockSpanner() Initializes the object of the class.
#       int next(int price) Returns the span of the stock's price given that today's price is price.

from unittest import TestCase
from typing import List, Tuple


class StockSpanner:
    def __init__(self):
        self.prices: List[Tuple[int, int]] = []

    def next(self, price: int) -> int:
        out: int = 1
        while self.prices and self.prices[-1][0] <= price:
            out += self.prices.pop()[1]

        self.prices.append((price, out))
        return out


class TestSolution(TestCase):
    def test_solution(self):
        for case, expected in [
            [[[100], [80], [60], [70], [60], [75], [85]], [1, 1, 1, 2, 1, 4, 6]]
        ]:
            ss = StockSpanner()
            for i in range(len(case)):
                self.assertEqual(expected[i], ss.next(case[i]))

    def test_pefomance(self):
        ss = StockSpanner()
        for i in range(1, 1000_000):
            self.assertEqual(i, ss.next(i))

