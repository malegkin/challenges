# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such
# that their sum is equal to the given target.

from typing import Optional, List, Set
from core.graphs import TreeNode
from unittest import TestCase


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = [root]
        numbers = set()

        while nodes:
            next_level_nodes = []
            for node in nodes:
                if k - node.val in numbers:
                    return True

                numbers.add(node.val)
                if node.right:
                    next_level_nodes.append(node.right)
                if node.left:
                    next_level_nodes.append(node.left)

            nodes = next_level_nodes

        return False


class SolutionDfs:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        numbers = set()

        def dfs(node: Optional[TreeNode]) -> bool:
            if k - node.val in numbers:
                return True
            numbers.add(node.val)

            return any(dfs(n) for n in [node.left, node.right] if n is not None)

        return dfs(root)


class TestSolution(TestCase):
    def test_solution(self):
        for sc in [Solution, SolutionDfs]:
            for root, k, expected in [
                [[5, 3, 6, 2, 4, None, 7], 9, True],
                [[5, 3, 6, 2, 4, None, 7], 28, False]
            ]:
                print(f"run_test {sc.__name__} {root}")
                self.assertEqual(expected, sc().findTarget(TreeNode.list2graph(root), k))
