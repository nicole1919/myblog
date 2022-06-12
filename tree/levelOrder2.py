# 二叉树层序遍历，返回二维数组，每层返回一个数组
# 输入： {1,2}
# 返回值： [[1],[2]]
import queue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = queue.Queue()  # 创建队列,存放树节点指针
        q.put(root)
        cur = None
        while not q.empty():
            row = []
            n = q.qsize()
            for i in range(n):
                cur = q.get()
                row.append(cur.val)
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            # 将每层的list追加至返回列表中
            res.append(row)
        return res






