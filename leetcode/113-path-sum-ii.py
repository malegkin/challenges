# https://leetcode.com/problems/path-sum-ii/
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node
# values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


from typing import List, Optional, Tuple
from unittest import TestCase
from timeit import timeit
from core.graphs import TreeNode, generate_highest_binary_tree
from core.tools.memory_usage import function_max_memory_usage

# Best solution real complexity O(n) solution
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []

        # One path one love )
        def dfs(node: Optional[TreeNode], path: List[int], path_sum: int) -> None:
            if node:
                path.append(node.val)

                if not node.left and not node.right and path_sum == node.val:
                        # for primitive values, [:] is sufficient (although it is doing shallow copy)
                        out.append(path[:])
                else:
                    dfs(node.left, path, path_sum - node.val)
                    dfs(node.right, path, path_sum - node.val)

                # backtrack
                path.pop()

        dfs(root, [], targetSum)
        return out


# Classical solution, but real complexity O(n^2) == n(dfs) * n(each step new path create)
class DfsSolution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []

        def dfs(node: Optional[TreeNode], path, path_sum: int):
            if node:
                if not node.left and not node.right and path_sum == node.val:
                    path.append(node.val)
                    out.append(path)

                dfs(node.left,  path + [node.val], path_sum - node.val)
                dfs(node.right, path + [node.val], path_sum - node.val)

        dfs(root, [], targetSum)
        return out


class BfsSolution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        out: List[List[int]] = []
        queue: List[Tuple[TreeNode, List[int]]] = [(root, [root.val])]

        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right and sum(path) == targetSum:
                out.append(path)
            if node.left:
                queue.append((node.left,  path + [node.left.val]))
            if node.right:
                queue.append((node.right, path + [node.right.val]))

        return out


class TestSolution(TestCase):
    def test_solution(self):
        for solution_class in [Solution, DfsSolution, BfsSolution]:
            for root, targetSum, expected in [
                [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]]],
                [[1, 2, 3], 5, []],
                [[1, 2], 0, []]
            ]:
                print(f"run {solution_class.__name__} {root}")
                self.assertListEqual(expected, solution_class().pathSum(TreeNode.list2graph(root), targetSum))


    @staticmethod
    def foo_for_test_memory_usage(solution_class, e) -> None:
        solution_class().pathSum(generate_highest_binary_tree(2**e), 123)

    def test_memory_usage(self):
        """ worst case performance cache (according to the graph with the maximum height)"""
        for solution_class in [Solution, DfsSolution, BfsSolution]:
            print(f"Memory usage {solution_class.__name__}:")
            for e in range(10, 14):
                memory = function_max_memory_usage(
                    TestSolution.foo_for_test_memory_usage, args=(solution_class, e)
                )
                print(f"2^{e:2}:  \t memory: {memory:.1f} MB")

    def test_complexity(self):
        """ worst case performance cache (according to the graph with the maximum height)"""

        grpahs = [(e, generate_highest_binary_tree(2 ** e, 0, 0)) for e in range(10, 14)]

        for solution_class in [Solution, DfsSolution, BfsSolution]:
            print(f"Time complexity {solution_class.__name__}:")

            for e, graph in grpahs:
                time = timeit(lambda: solution_class().pathSum(graph, 123), number=10)
                print(f"2^{e:2}: time: {time:.3f} s")
