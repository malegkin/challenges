# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
# Constraints
# The number of nodes in the tree is in the range [1, 104].
# -10^5 <= Node.val <= 10^5
import time
import unittest
from typing import List, Dict, Optional, Tuple, Deque
from collections import defaultdict, deque
from core.graphs import TreeNode, generate_binary_tree

MIN_NODE_VALUE = -100*1000
# # Time complexity: O(N) as we visit every node only once.
# # Auxiliary Space: O(W) where W is the weight of the tree. In the worst case, W would be logN
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack: list[TreeNode] = [root]
        level_number: int = 0
        max_level_number: int = 0
        max_level_sum: int = MIN_NODE_VALUE

        while len(stack) > 0:
            level_sum = 0
            level_number += 1
            next_stack: list[TreeNode] = []

            for node in stack:
                level_sum += node.val

                next_stack.extend([n for n in [node.left, node.right] if n])

            if level_sum > max_level_sum:
                max_level_number = level_number
                max_level_sum = level_sum

            stack = next_stack

        return max_level_number


class Solution2:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack: list[TreeNode] = [root]
        level_number: int = 0
        max_level_number: int = 0
        max_level_sum: int = MIN_NODE_VALUE

        while len(stack) > 0:
            level_sum = 0
            level_number += 1
            next_stack: list[TreeNode] = []

            for node in stack:
                level_sum += node.val

                if node.left: next_stack.append(node.left)
                if node.right: next_stack.append(node.right)

            if level_sum > max_level_sum:
                max_level_number = level_number
                max_level_sum = level_sum

            stack = next_stack

        return max_level_number


class DfsSolution:

    def maxLevelSum(self, root: TreeNode) -> int:
        level_sum: Dict[int, int] = defaultdict(int)

        def dfs(node: TreeNode, level: int) -> None:
            if not node: return

            level_sum[level] += node.val
            dfs(node.left,  level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        return max(level_sum, key=level_sum.get)


class DfsSolution2:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sum = [0] * 100

        def dfs(node: TreeNode, level: int) -> None:
            if not node: return

            level_sum[level] += node.val
            dfs(node.left,  level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        return level_sum.index(max(level_sum))


class DfsSolution3:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sum = [0] * 100
        stack: List[Tuple[TreeNode, int]] = [(root, 1)]

        while len(stack) > 0:
            node, level = stack.pop()

            level_sum[level] += node.val
            stack.extend([(n, level + 1) for n in [node.left, node.right] if n])

        return level_sum.index(max(level_sum))


class DfsSolution4:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sum = [0] * 100
        stack: List[Tuple[TreeNode, int]] = [(root, 1)]

        while len(stack) > 0:
            node, level = stack.pop()

            level_sum[level] += node.val
            if node.left: stack.append((node.left, level + 1))
            if node.right: stack.append((node.right, level + 1))

        return level_sum.index(max(level_sum))


class DfsSolution5:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sum = [0] * 100
        stack: Deque[Tuple[TreeNode, int]] = deque()
        stack.append((root, 1))

        while len(stack) > 0:
            node, level = stack.pop()

            level_sum[level] += node.val
            if node.left: stack.append((node.left, level + 1))
            if node.right: stack.append((node.right, level + 1))

        return level_sum.index(max(level_sum))


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for solution_class in [Solution, Solution2, DfsSolution, DfsSolution2, DfsSolution3, DfsSolution4, DfsSolution5]:
            solution = solution_class()
            for root, expected in [
                [TreeNode(1,
                          TreeNode(7,
                                   TreeNode(7, None, None),
                                   TreeNode(-8, None, None),
                                   ),
                          TreeNode(0, None, None)
                          )
                    , 2]
            ]:
                print(f"test: {solution_class} {root}")
                self.assertEqual(
                    solution.maxLevelSum(root), expected
                )

    def test_perfomance(self):
        big_tree = generate_binary_tree(10 * 1000)

        for solution_class in [Solution, Solution2, DfsSolution, DfsSolution2, DfsSolution3, DfsSolution4, DfsSolution5]:
            tick = time.perf_counter()
            solution = solution_class()
            for _ in range(100):
                solution.maxLevelSum(big_tree)
            tack = time.perf_counter()

            print(f"{solution_class}: {tack - tick:.5f}")
