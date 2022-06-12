# 判断一棵树是否为二叉树
# 思路：层序遍历，利用队列存储结果，出现过空，则标记flag，若后面再没有空，则为完全二叉树，否则不是完全二叉树
import queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        q = queue.Queue()
        q.put(root)  # 入队
        flag = False
        while not q.empty():  # 队列不为空
            sz = q.qsize()  # 队列元素个数
            for i in range(sz):
                cur = q.get()  # 出队元素
                # 标记第一次遇到空节点
                if not cur:
                    flag = True
                else:
                    # 后续访问已经遇到空节点了，说明经过了叶子
                    if flag:
                        return False
                    q.put(cur.left)
                    q.put(cur.right)
        return True

