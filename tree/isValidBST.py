# 给定一个二叉树根节点，请你判断这棵树是不是二叉搜索树。
# 二叉搜索树满足每个节点的左子树上的所有节点均严格小于当前节点且右子树上的所有节点均严格大于当前节点。
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 第一种方法，中序遍历，然后判断所得数组是否为升序
    def inorder(self, a_list, root):
        if root is None:
            return None
        if root.left:
            self.inorder(a_list, root.left)
        a_list.append(root.val)
        if root.right:
            self.inorder(a_list, root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        a_list = []
        self.inorder(a_list, root)
        for i in range(len(a_list) - 1):
            if a_list[i] >= a_list[i + 1]:
                return False
        return True
    # 第二种方法，设置全局变量pre，指向前序遍历的前一个值
    # step 1：首先递归到最左，初始化maxLeft与pre。
    # step 2：然后往后遍历整棵树，依次连接pre与当前节点，并更新pre。
    # step 3：左子树如果不是二叉搜索树返回false。
    # step 4：判断当前节点是不是小于前置节点，更新前置节点。
    # step 5：最后由右子树的后面节点决定。
    pre = -sys.maxsize - 1

    def isValidBST2(self, root: TreeNode) -> bool:
        if root is None:
            return True
        self.isValidBST2(root.left)
        if self.pre >= root.val:
            return False
        self.pre = root.val
        self.isValidBST2(root.right)
        return True

