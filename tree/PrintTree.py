# 按之字形顺序打印二叉树,给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
import queue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintTree(self, pRoot: TreeNode) -> List[List[int]]:
        res = []
        if pRoot == None:
            return res
        q = queue.Queue()
        flag = 1
        q.put(pRoot)
        while not q.empty():
            n = q.qsize()
            row = []
            for i in range(n):
                x = q.get()
                if x.left:
                    q.put(x.left)
                if x.right:
                    q.put(x.right)
                row.append(x.val)
            if flag == -1:
                row = row[::-1]
            flag = flag * -1
            res.append(row)
        return res


