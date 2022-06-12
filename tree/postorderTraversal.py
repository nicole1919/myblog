# 二叉树的后序遍历
# 定义树节点类型
from typing import List
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 后续遍历
    def postorder(self, a_list: List[int], root: TreeNode) -> List[int]:
        if root is None:
            return
        self.postorder(a_list, root.left)
        self.postorder(a_list, root.right)
        a_list.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        a_list = []
        sys.setrecursionlimit(1000)
        self.postorder(a_list, root)
        return a_list
