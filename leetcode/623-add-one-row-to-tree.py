# https://leetcode.com/problems/add-one-row-to-tree/

# Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth
# depth.
# Note that the root node is at depth 1.
# The adding rule is:
#   1. Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value
#   val as cur's left subtree root and right subtree root.
#   2. cur's original left subtree should be the left subtree of the new left subtree root.
#   3. cur's original right subtree should be the right subtree of the new right subtree root.
#   4. If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new
#   root of the whole original tree, and the original tree is the new root's left subtree.

from unittest import TestCase
from typing import Optional
from core.graphs import TreeNode


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        for _ in range(depth - 1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        for node in row:
            node.left, node.left.left = TreeNode(val), node.left
            node.right, node.right.right = TreeNode(val), node.right
        return dummy.left


class DfsSolution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode], h, dr):
            if h == depth:
                tmp = TreeNode(val)
                # if not node: return tmp
                if dr == 0:
                    tmp.left = node
                else:
                    tmp.right = node
                return tmp

            if not node:
                return node

            node.left = dfs(node.left, h + 1, 0)
            node.right = dfs(node.right, h + 1, 1)
            return node

        return dfs(root, 1, 0)


class TestSolution(TestCase):
    def test_solution(self):
        for cs in [Solution, DfsSolution]:
            for root, val, depth, expected in [
                [[4, 2, 6, 3, 1, 5], 1, 2, [4, 1, 1, 2, None, None, 6, 3, 1, 5]],
                [[4, 2, None, 3, 1], 1, 3, [4, 2, None, 1, 1, 3, None, None, 1]]
            ]:
                print(f"run_case {cs.__name__} {root}")
                self.assertCountEqual(expected, TreeNode.graph2list(cs().addOneRow(TreeNode.list2graph(root), val, depth)))
