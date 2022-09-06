import unittest
from random import randint
from typing import Optional, List
from collections import deque


class Node:
    def __init__(self, val: int, children: List['Node'] = None):
        self.val = val
        self.children = list() if children is None else children

    def __str__(self):
        return f"Node{{val: {self.val}, children:{', '.join(self.children)}}}"

    @staticmethod
    def list2graph(values: List[int] = None) -> Optional['Node']:
        if values is None or len(values) == 0:
            return None

        values = deque(values)
        root = Node(values.popleft())
        values.popleft()

        nodes = [root]

        while len(nodes) > 0:
            next_level_nodes = []
            for node in nodes:
                while values and (val := values.popleft()) is not None:
                    node.children.append(Node(val))
                next_level_nodes.extend(node.children)

            nodes = next_level_nodes

        return root

    def graph2list(self):
        out = []

        nodes_groups = [[self]]
        while len(nodes_groups) > 0:
            next_level_nodes_groups = []
            for nodes in nodes_groups:
                for node in nodes:
                    out.append(node.val)
                    next_level_nodes_groups.append(node.children)
                out.append(None)
            nodes_groups = next_level_nodes_groups

        while out[-1] is None:
            out.pop()

        return out


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode{{val: {self.val}, left:{self.left}, right:{self.right}}}"

    @staticmethod
    def list2graph(values: List[int] = None) -> Optional['TreeNode']:
        if values is None or len(values) == 0:
            return None

        values = deque(values)
        root = TreeNode(values.popleft())
        nodes = [root]

        while len(nodes) > 0:
            next_level_nodes = []
            for node in nodes:
                node.left  = None if len(values) == 0 else values.popleft()
                node.left  = None if node.left is None else TreeNode(node.left)
                node.right = None if len(values) == 0 else values.popleft()
                node.right = None if node.right is None else TreeNode(node.right)
                next_level_nodes.extend([n for n in [node.left, node.right] if n is not None])

            nodes = next_level_nodes

        return root

    def graph2list(self):
        out = []

        nodes_groups = [[self]]
        while len(nodes_groups) > 0:
            next_level_nodes_groups = []
            for nodes in nodes_groups:
                for node in nodes:
                    if node is not None:
                        out.append(node.val)
                        next_level_nodes_groups.append([node.left, node.right])
                    else:
                        out.append(None)
            nodes_groups = next_level_nodes_groups

        while out[-1] is None:
            out.pop()

        return out


def generate_binary_tree(nodes_number: int = 1000,
                         min_val: int = -10000, max_val: int = 10000) -> Optional[TreeNode]:
    if nodes_number <= 0:
        return None

    lef_nodes_number = randint(0, nodes_number // 2)
    right_nodes_number = nodes_number - lef_nodes_number - 1

    return TreeNode(randint(min_val, max_val),
                    generate_binary_tree(lef_nodes_number, min_val, max_val),
                    generate_binary_tree(right_nodes_number, min_val, max_val))


class TestGraph(unittest.TestCase):
    def test_node_list2graph(self):
        for case in [
            [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
             None, 14],
            [1, None, 3, 2, 4, None, 5, 6]
        ]:
            self.assertListEqual(case, Node.list2graph(case).graph2list())

    def test_binary_tree_list2graph(self):
        for case in [
            [1, 0, 1, 0, 0, 0, 1],
            [1, None, 0, 0, 1],
            [1, None, 1, None, 1]
        ]:

            self.assertListEqual(case, TreeNode.list2graph(case).graph2list())
