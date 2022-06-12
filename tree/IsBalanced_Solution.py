# 判断是不是平衡二叉树
# step 1：第一个函数递归遍历二叉树所有节点。
# step 2：对于每个节点判断，调用第二个函数获取子树深度。
# step 3：第二个函数递归获取子树深度，只需要不断往子节点深度遍历，累加左右深度的较大值。
# step 4：根据深度判断该节点下的子树是否为平衡二叉树。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 求树的高度
    def deep(self, root: TreeNode):
        if root is None:
            return 0
        # 分别求左右子树的高度
        left = self.deep(root.left)
        right = self.deep(root.right)
        return left + 1 if left > right else right + 1

    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        if pRoot is None:
            return True
        h1 = self.deep(pRoot.left)
        h2 = self.deep(pRoot.right)
        # 左右子树高度差符合范围
        if h1 - h2 > 1 or h1 - h2 < -1:
            return False
        # 左右子树本身必须都是平衡二叉树
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

