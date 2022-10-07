# A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k
# events.)
# You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking
# between all the previous events.
# Implement the MyCalendarThree class:
# MyCalendarThree() Initializes the object.
# int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking
# in the calendar.

import bisect
from unittest import TestCase


class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.events, (start, 1))
        bisect.insort(self.events, (end, -1))
        cur_book = max_book = 0
        for event, t in self.events:
            cur_book += t
            max_book = max(max_book, cur_book)

        return max_book


class MyCalendarThreeNode:
    class _Node:
        def __init__(self, start, end, k):
            self.start = start
            self.end = end

            self.left = None
            self.right = None

            self.k = k

    def __init__(self):
        self.root = None
        self.k = 0

    def book(self, start: int, end: int) -> int:
        self.root = self.insert(self.root, start, end, 1)

        return self.k

    def insert(self, node, start, end, k):
        if node is None:
            self.k = max(self.k, k)
            return self._Node(start, end, k)
        if start == end:
            return node

        if start >= node.end:
            node.right = self.insert(node.right, start, end, k)
        elif node.start >= end:
            node.left = self.insert(node.left, start, end, k)
        else:
            startA, endA = min(node.start, start), max(node.start, start)
            startB, endB = min(node.end, end), max(node.end, end)

            node.left = self.insert(node.left, startA, endA, startA == node.start and node.k or k)
            node.right = self.insert(node.right, startB, endB, endB == node.end and node.k or k)

            node.start, node.end = endA, startB

            node.k += k
            self.k = max(node.k, self.k)

        return node


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [MyCalendarThree, MyCalendarThreeNode]:
            for cmds, args, expecteds in [
                [["book", "book", "book", "book", "book", "book"],
                 [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
                 [1, 1, 2, 3, 3, 3]
                 ]
            ]:
                s = sc()
                for i in range(len(cmds)):
                    self.assertEqual(expecteds[i], s.book(*args[i]))

