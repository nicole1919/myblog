# 求二叉树的镜像，即将其所有左右子树交换
# 操作给定的二叉树，将其变换为源二叉树的镜像。
# step 1：先深度最左端的节点，遇到空树返回，处理最左端的两个子节点交换位置。
# step 2：然后进入右子树，继续按照先左后右再回中的方式访问。
# step 3：再返回到父问题，交换父问题两个子节点的值。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror(self, pRoot: TreeNode) -> TreeNode:
        if pRoot is None:
            return None
        left = self.Mirror(pRoot.left)
        right = self.Mirror(pRoot.right)
        pRoot.left = right
        pRoot.right = left
        return pRoot