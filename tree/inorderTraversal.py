# 二叉树的中序遍历
from sys import setrecursionlimit
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, a_list: List[int], root: TreeNode) -> List[int]:
        if root is None:
            return
        self.inorder(a_list, root.left)
        a_list.append(root.val)
        self.inorder(a_list, root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 由于python存在最大的递归深度约束，这一步是更改最大深度的限制
        setrecursionlimit(1500)
        a_list = []
        self.inorder(a_list, root)
        return a_list
