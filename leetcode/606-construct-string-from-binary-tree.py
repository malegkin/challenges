# https://leetcode.com/problems/construct-string-from-binary-tree/
# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the
#     preorder traversal way, and return it.
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the
# original binary tree.
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -1000 <= Node.val <= 1000
import unittest
from core.graphs import TreeNode, generate_binary_tree
from time import perf_counter
from typing import Optional


class Solution:
    """
        DepthFirst Search Recursive Solution
        Time Complexity: O(n)
        Auxiliary Space: O(n)
    """
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node: TreeNode) -> str:
            if not node: return ""
            l_str = f"({dfs(node.left)})"   if node.left or node.right else ''
            r_str = f"({dfs(node.right)})"  if node.right else ''
            return f"{node.val}{l_str}{r_str}"

        return dfs(root)


class IterativeSolution:
    """
        DepthFirst Search Iterative Solution
        Time Complexity: O(n)
        Auxiliary Space: O(n)
    """
    def tree2str(self, root: Optional[TreeNode]) -> str:
        out = ""
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                out += ")"
                continue

            out += f"({str(node.val)}"

            if not node.left and node.right:
                out += "()"
            if node.right:
                stack.append(None)
                stack.append(node.right)
            if node.left:
                stack.append(None)
                stack.append(node.left)

        return out[1:]


class OneLineSolution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return "" if not root else str(root.val) \
                                   + (f"({self.tree2str(root.left)})" if root.left or root.right else '') \
                                   + (f"({self.tree2str(root.right)})" if root.right else '')


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for solution_class in [Solution, IterativeSolution, OneLineSolution]:
            for case, expected in [
                [[1, 2, 3, 4], "1(2(4))(3)"],
                [[1, 2, 3, None, 4], "1(2()(4))(3)"]
            ]:
                print(f"run test {solution_class} ({case}):")
                solution = solution_class()
                self.assertEqual(solution.tree2str(TreeNode.list2graph(case)), expected)

    def test_performance(self):
        graph = generate_binary_tree()
        for solution_class in [Solution, IterativeSolution, OneLineSolution]:
            solution = solution_class()
            tik = perf_counter()
            for _ in range(1000):
                solution.tree2str(graph)
            tok = perf_counter()
            print(f"{solution_class}: {(tok-tik):.5}")

