# https://leetcode.com/problems/find-duplicate-subtrees/
# Given the root of a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with the same node values.
# Constraints:
# The number of the nodes in the tree will be in the range [1, 10^4]
# -200 <= Node.val <= 200

import unittest
from timeit import timeit
from typing import List, Optional, Tuple
from collections import defaultdict
from core.tools.memory_usage import function_max_memory_usage
from core.graphs import TreeNode, generate_highest_binary_tree


"""
    DFS with subtree tuple ID caching
    Time Complexity: O(n)   
    Auxiliary Space: O(n)
"""
class Solution:
        def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
            def dfs(node: Optional[TreeNode]) -> Optional[int]:
                if node:
                    id = subtree_ids[node.val, dfs(node.left), dfs(node.right)]
                    subtrees[id].append(node)
                    return id

            subtrees = defaultdict(list)
            subtree_ids = defaultdict()
            subtree_ids.default_factory = subtree_ids.__len__
            dfs(root)

            return [roots[0] for roots in subtrees.values() if len(roots) > 1]


class StringSolution:
    """
    Time Complexity: O(n^2)
    Auxiliary Space: O(n^2)
    """
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: Optional[TreeNode]) -> str:
            if node:
                dfs_out = f"({node.val})({dfs(node.left)})({dfs(node.right)})"
                subtrees[dfs_out].append(node)
                return dfs_out

        subtrees = defaultdict(list)
        dfs(root)

        return [roots[0] for roots in subtrees.values() if len(roots) > 1]


class TuplifySolution:
    """
    Time Complexity: O(n^2)
    Auxiliary Space: O(n):
    """
    def findDuplicateSubtrees(self, root):
        def tuplify(node: Optional[TreeNode]) -> Tuple[int, Tuple, Tuple]:
            if node:
                tup = node.val, tuplify(node.left), tuplify(node.right)
                subtrees[tup].append(node)
                return tup

        subtrees = defaultdict(list)
        tuplify(root)

        return [roots[0] for roots in subtrees.values() if len(roots) > 1]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for solution_class in [Solution, StringSolution, TuplifySolution]:
            for case, expected in [
                [[1, 2, 3, 4, None, 2, 4, None, None, 4], [[2, 4], [4]]],
                [[2, 1, 1], [[1]]],
                [[2, 2, 2, 3, None, 3, None], [[2, 3], [3]]],
                [[0, 0, 0, 0, None, None, 0, None, None, None, 0], [[0]]]
            ]:
                solution = solution_class()
                print(f"test run {solution_class.__name__} {case}")
                self.assertCountEqual(
                    [result.graph2list() for result in solution.findDuplicateSubtrees(TreeNode.list2graph(case))],
                    expected
                )

    @staticmethod
    def foo_for_test_memory_usage(solution_class, e) -> None:
        solution_class().findDuplicateSubtrees(generate_highest_binary_tree(2**e))

    def test_memory_usage(self):
        """ worst case performance cache (according to the graph with the maximum height)"""
        for solution_class in [Solution, StringSolution, TuplifySolution]:
            print(f"Memory usage {solution_class.__name__}:")
            for e in range(10, 14):
                memory = function_max_memory_usage(
                    TestSolution.foo_for_test_memory_usage, args=(solution_class, e)
                )
                print(f"2^{e:2}:  \t memory: {memory:.1f} MB")

    def test_complexity(self):
        """ worst case performance cache (according to the graph with the maximum height)"""

        grpahs = [(e, generate_highest_binary_tree(2 ** e, 0, 0)) for e in range(10, 14)]

        for solution_class in [Solution, StringSolution, TuplifySolution]:
            solution = solution_class()
            print(f"Time complexity {solution_class.__name__}:")

            for e, graph in grpahs:
                time = timeit(lambda: solution.findDuplicateSubtrees(graph), number=10)
                print(f"2^{e:2}: time: {time:.3f} s")
