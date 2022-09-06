# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by
# the null value (See examples).

# Constraints:
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]

from typing import List, Dict
from collections import defaultdict


class Node:
    def __init__(self, val=None, children: List['Node'] = None):
        self.val = val
        self.children = children


class Solution:
    """
    BreadthFirstSearch Solution
    Time Complexity: O(n)
    Auxiliary Space: O(n)
    """
    def levelOrder(self, root: Node) -> List[List[int]]:
        if root is None: return []

        out: List[List[int]] = []
        nodes: List[Node] = [root]

        while nodes:
            out.append([node.val for node in nodes])
            nodes = [children for node in nodes for children in node.children if node is not None and node.children is not None]

        return out


class DfsSolution:
    """
    DepthFirst Search Solution
    Time Complexity: O(n)
    Auxiliary Space: O(n)
    """
    def levelOrder(self, root: Node) -> List[List[int]]:
        levels: Dict[int, List[int]] = defaultdict(list)

        def dfs(node: Node, level: int = 0) -> None:
            if node:
                return

            levels[level].append(node.val)
            for children in node.children:
                dfs(children, level+1)

        dfs(root)
        return list(levels.values())


