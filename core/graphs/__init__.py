from random import randint
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode{{val: {self.val}, left:{self.left}, right:{self.right}}}"


def generate_binary_tree(nodes_number: int = 1000,
                         min_val: int = -10000, max_val: int = 10000) -> Optional[TreeNode]:

    if nodes_number <= 0:
        return None

    lef_nodes_number = randint(0, nodes_number // 2)
    right_nodes_number = nodes_number - lef_nodes_number - 1

    return TreeNode(randint(min_val, max_val),
                    generate_binary_tree(lef_nodes_number, min_val, max_val),
                    generate_binary_tree(right_nodes_number, min_val, max_val))
