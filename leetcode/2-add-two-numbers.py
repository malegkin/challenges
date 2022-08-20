# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

import unittest
from typing import Optional, Union, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeIterator:
    def __init__(self, ln: Optional[ListNode] = None):
        self._ln = ln

    def __iter__(self):
        return self

    def __next__(self):
        if self._ln is not None:
            out = self._ln
            self._ln = self._ln.next
            return out

        raise StopIteration


class NumberList:
    def __init__(self, value: Union[int, List[int], ListNode] = 0):
        if isinstance(value, int):
            self._init_from_int(value)
        elif isinstance(value, list):
            self._init_from_list(value)
        elif isinstance(value, ListNode):
            self._begin = value
        else:
            raise ValueError("value must be int or list[int]")

    def __int__(self) -> int:
        out = 0
        for i, it in enumerate(ListNodeIterator(self._begin)):
            out += pow(10, i) * it.val
        return out

    def _init_from_int(self, value: int):
        return self._init_from_list([int(c) for c in str(value)])

    def _init_from_list(self, value: List[int]):
        _last = None
        for val in value:
            _last = ListNode(val, next=_last)

        self._begin = _last

    def get_begin(self) -> ListNode:
        return self._begin


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _last = None
        _begin = None
        next_add = 0

        while l1 is not None or l2 is not None:
            val = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + next_add
            next_add = val // 10
            val = val % 10

            if _last is None:
                _last = ListNode(val)
                _begin = _last
            else:
                _last.next = ListNode(val)
                _last = _last.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if next_add > 0:
            _last.next = ListNode(next_add)

        return _begin


class SolutionByNumberList:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = int(NumberList(l1)) + int(NumberList(l2))
        return NumberList(out).get_begin()


class TestSolution(unittest.TestCase):
    def test_int_to_number_list_and_back_converter(self):
        for i in [0, 1, 12, 123456789]:
            self.assertEqual(i, int(NumberList(i)))

    def test_solution(self):
        for solution_class in [Solution, SolutionByNumberList]:
            solution = solution_class()
            for x, y, z in [[0, 0, 0], [1, 2, 3], [12, 34, 46], [123, 45, 168], [99, 1, 100]]:
                self.assertEqual(z, int(NumberList(
                    solution.addTwoNumbers(NumberList(x).get_begin(), NumberList(y).get_begin()))
                ))


if __name__ == 'main':
    unittest.main()
