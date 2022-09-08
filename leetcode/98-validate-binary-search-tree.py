# Medium
# https://leetcode.com/problems/validate-binary-search-tree/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -2^31 <= Node.val <= 2^31 - 1

import sys
import random
import unittest
from timeit import timeit
from typing import Optional, List, Tuple

from core.graphs import TreeNode
from core.graphs.binary_search_tree import BST


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes: List[Tuple[TreeNode, int, int]] = [(root, sys.maxsize, -sys.maxsize - 1)]

        while nodes:
            node, less, greater = nodes.pop()
            if node.val >= less or node.val <= greater:
                return False

            if node.left:
                nodes.append((node.left, min(less, node.val), greater))
            if node.right:
                nodes.append((node.right, less, max(greater, node.val)))

        return True


# Time complexity of inorder traversal is O(n)
# Fun fact: Inorder traversal leads to a sorted array if it is
# a Valid Binary Search. Tree.
class InorderSolution(object):
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values: List[int] = []

        def inorder(node: Optional[TreeNode]) -> None:
            if node:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)

        inorder(root)

        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for solution_class in [Solution, InorderSolution]:
            for case, expected in [
                [[2, 1, 3], True],
                [[5, 1, 4, None, None, 3, 6], False]
            ]:
                print(f"run: {solution_class.__name__} {case}")
                self.assertEqual(expected,
                                 solution_class().isValidBST(TreeNode.list2graph(case)))

    def test_compare_solutions_performance(self):
        values: List[int] = sorted(list({random.randint(-sys.maxsize, sys.maxsize) for _ in range(1000)}))
        graph = BST.list2graph(values)

        for solution_class in [Solution, InorderSolution]:
            print(f"{solution_class.__name__}: time: "
                  f"{timeit(lambda: solution_class().isValidBST(graph), number=1000):.3f} s")
