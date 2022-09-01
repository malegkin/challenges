# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes
# with a value greater than X.
# Return the number of good nodes in the binary tree.
# Constraints:
#
# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].


import time
import random
import unittest
from typing import List, Tuple, Optional


def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{}:{}'.format(label, end - start))


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode{{val: {self.val}, left:{self.left}, right:{self.right}}}"


# Time complexity: O(N) as we visit every node only once.
# Auxiliary Space: O(H) where H is the height of the tree. In the worst case, H would be N
TREE_NODE_MIN_VALUE = -10 * 1000



class Solution:
    def goodNodes(self, root: TreeNode, path_max_value: int = TREE_NODE_MIN_VALUE) -> int:  # -10k -
        if root is None: return 0

        return sum([
            (1 if root.val >= path_max_value else 0),
            *[self.goodNodes(node, max(path_max_value, root.val)) for node in [root.left, root.right]]
        ])


class Solution2:
    def goodNodes(self, root: TreeNode, path_max_value: int = TREE_NODE_MIN_VALUE) -> int:  # -10k -
        if root is None: return 0

        return sum([
            (1 if root.val >= path_max_value else 0),
            self.goodNodes(root.left, max(path_max_value, root.val)),
            self.goodNodes(root.right, max(path_max_value, root.val))])


class Solution3:
    def goodNodes(self, root: TreeNode, path_max_value: int = TREE_NODE_MIN_VALUE) -> int:  # -10k -
        if root is None: return 0

        return (1 if root.val >= path_max_value else 0) + \
               self.goodNodes(root.left, max(path_max_value, root.val)) + \
               self.goodNodes(root.right, max(path_max_value, root.val))


# Time complexity: O(N) as we visit every node only once.
# Auxiliary Space: O(H) where H is the height of the tree. In the worst case, H would be N
class StackDfsSolution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        out: int = 1  # Root Node is always a good node.
        nodes: List[Tuple[TreeNode, int]] = [(root, root.val)]
        while len(nodes) > 0:
            node, path_max_val = nodes.pop()

            for n in [node.left, node.right]:
                if n is None:
                    continue

                if n.val >= path_max_val:
                    out += 1

                nodes.append((n, max(n.val, path_max_val)))

        return out


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for solution_class in [Solution, StackDfsSolution]:
            solution = solution_class()
            for root, expected in [
                [TreeNode(3,
                          TreeNode(1,
                                   TreeNode(3, None, None),
                                   None
                                   ),
                          TreeNode(4,
                                   TreeNode(1, None, None),
                                   TreeNode(5, None, None)
                                   )
                          )
                    , 4],
                [TreeNode(3,
                          TreeNode(3,
                                   TreeNode(4, None, None),
                                   TreeNode(2, None, None),
                                   ),
                          None)
                    , 3]
            ]:
                print(f"test: {solution_class} {root}")
                self.assertEqual(
                    solution.goodNodes(root), expected
                )

    @staticmethod
    def _generate_binary_tree(nodes_number: int = 1000,
                              min_val: int = -10000, max_val: int = 10000) -> Optional[TreeNode]:

        if nodes_number <= 0:
            return None

        lef_nodes_number = random.randint(0, nodes_number // 2)
        right_nodes_number = nodes_number - lef_nodes_number - 1

        return TreeNode(random.randint(min_val, max_val),
                        TestSolution._generate_binary_tree(lef_nodes_number, min_val, max_val),
                        TestSolution._generate_binary_tree(right_nodes_number, min_val, max_val))

    def test_benchmark(self):
        big_tree = TestSolution._generate_binary_tree(10 * 1000)
        good_nodes_numbers = None

        for solution_class in [StackDfsSolution, Solution, Solution2, Solution3]:
            tick = time.perf_counter()
            solution = solution_class()
            for _ in range(100):
                if good_nodes_numbers is None:
                    good_nodes_numbers = solution.goodNodes(big_tree)
                else:
                    self.assertEqual(good_nodes_numbers, solution.goodNodes(big_tree))
            tack = time.perf_counter()

            print(f"{solution_class}: {tack - tick:.5f}")
