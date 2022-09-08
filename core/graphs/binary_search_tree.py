from typing import List, Optional
from .base import TreeNode


class BST(TreeNode):
    @staticmethod
    def list2graph(values: List[int] = None) -> Optional[TreeNode]:
        if values:
            mid_num = len(values)//2
            node = TreeNode(values[mid_num])
            node.left = BST.list2graph(values[:mid_num])
            node.right = BST.list2graph(values[mid_num+1:])
            return node