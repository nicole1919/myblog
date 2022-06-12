# 二叉树中和为某一值的路径(一)
# 给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径。
# 1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点
# 2.叶子节点是指没有子节点的节点
# 3.路径只能从父节点到子节点，不能从子节点到父节点
# 4.总节点数目为n

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        # 结束条件：为叶子结点，并且路径之和为sum
        if not root.left and not root.right and sum - root.val == 0:
            return True
        # 递归左右子树
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


