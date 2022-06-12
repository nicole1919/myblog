# 二叉搜索树，转换成双向链表
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表
# 注意:
# 1.要求不能创建任何新的结点，只能调整树中结点指针的指向。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继
# 2.返回链表中的第一个节点的指针
# 3.函数返回的TreeNode，有左右指针，其实可以看成一个双向链表的数据结构
# 4.你不用输出双向链表，程序会根据你的返回值自动打印输出
# 输入描述：二叉树的根节点
# 返回值描述：双向链表的其中一个头节点。
# 思路：递归

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    head = None
    pre = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        # 左侧递归
        self.Convert(pRootOfTree.left)
        if not self.pre:
            self.head = pRootOfTree
            self.pre = pRootOfTree
        else:
            # 双向链表构造
            self.pre.right = pRootOfTree
            pRootOfTree.left = self.pre
            # pre向后移动
            self.pre = pRootOfTree
        self.Convert(pRootOfTree.right)
        # 返回头节点
        return self.head


