# 二叉树的前序遍历
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #方法未通过ac
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        a_list = []
        if root is None:
            return []
        else:
            a_list.append(root.val)
            # extend 函数，可以讲返回的list元素拆分出来，追加到a_list中
            a_list.extend(self.preorderTraversal1(root.left))
            a_list.extend(self.preorderTraversal(root.right))
        return a_list

    def preorder(self, a_list: List[int], root: TreeNode):
        # 遇到空节点则返回
        if root is None:
            return
        # 先遍历根节点
        a_list.append(root.val)
        # 再去左子树
        self.preorder(a_list, root.left)
        # 最后去右子树
        self.preorder(a_list, root.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 添加遍历结果的数组
        a_list = []
        # 递归前序遍历
        self.preorder(a_list, root)
        return a_list


if __name__ == "__main__":
    r1 = TreeNode(1)
    # print(Solution().preorderTraversal1(r1)) # 方法未通过ac
    print(Solution().preorderTraversal(r1))


