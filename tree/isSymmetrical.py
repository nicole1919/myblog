# 给定一棵二叉树，判断其是否是自身的镜像（即：是否对称）
# step 1：两种方向的前序遍历，同步过程中的当前两个节点，同为空，属于对称的范畴。
# step 2：当前两个节点只有一个为空或者节点值不相等，已经不是对称的二叉树了。
# step 3：第一个节点的左子树与第二个节点的右子树同步递归对比，第一个节点的右子树与第二个节点的左子树同步递归比较。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recursion(self, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return self.recursion(root1.left, root2.right) and self.recursion(root1.right, root2.left)

    def isSymmetrical(self, pRoot: TreeNode) -> bool:
        return self.recursion(pRoot, pRoot)
