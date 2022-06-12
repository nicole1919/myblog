# 合并二叉树
# 已知两颗二叉树，将它们合并成一颗二叉树。合并规则是：都存在的结点，就将结点值加起来，否则空的位置就由另一个树的结点来代替
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return
        if not t1 and t2:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        if t1.left:
            self.mergeTrees(t1.left, t2.left)
        else:
            t1.left = t2.left
        if t1.right:
            self.mergeTrees(t1.right, t2.right)
        else:
            t1.right = t2.right
        return t1


