# https://leetcode.com/problems/binary-tree-pruning/
# Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has
# been removed.
# A subtree of a node 'node' is 'node' plus every node that is a descendant of 'node'.

import unittest
from typing import Optional
from core.graphs import TreeNode


class Solution:
    """
        DepthFirst Search Solution
        Time Complexity: O(n)
        Auxiliary Space: O(1)
    """
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode) -> Optional[TreeNode]:
            if node is None:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val == 0 and node.left is None and node.right is None:
                return None

            return node

        return dfs(root)


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for case, expected in [
            [[1, None, 0, 0, 1], [1, None, 0, None, 1]],
            [[1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]],
            [[1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1]]
        ]:
            solution = Solution()
            self.assertListEqual(solution.pruneTree(TreeNode.list2graph(case)).graph2list(), expected)
