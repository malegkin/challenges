# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋
# denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
# Constraints:
#   The number of nodes in the list is in the range [1, 10**5].
#   1 <= Node.val <= 10**5

from typing import List, Optional
from core.graphs import ListNode
from unittest import TestCase


class TwoPointersSolution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next

        return head


class OnHeadSolution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        if length < 2:
            return None

        node = head
        for _ in range((length // 2) - 1):
            node = node.next

        node.next = None if node.next is None else node.next.next

        return head


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [OnHeadSolution, TwoPointersSolution]:
            for case, expected in [
                [[1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]],
                [[1, 2, 3, 4], [1, 2, 4]],
                [[2, 1], [2]],
                [[1], None],
                [None, None]
            ]:
                print(f"run_test {sc.__name__} {case}")
                if expected is None:
                    self.assertIsNone(sc().deleteMiddle(ListNode.list2graph(case)))
                else:
                    self.assertListEqual(expected, sc().deleteMiddle(ListNode.list2graph(case)).graph2list())
