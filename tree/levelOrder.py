# 二叉树层序遍历，输出一维数组
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        res = []
        # 存放指针的队列
        a_queue = deque()
        a_queue.append(root)  # 根指针放入队列
        while a_queue:
            # 指针出队列
            x = a_queue.popleft()
            if x.left:
                a_queue.append(x.left)
            if x.right:
                a_queue.append(x.right)
            res.append(x.val)
        return res


if __name__ == "__main__":
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.left = p2
    p1.right = p3
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p2.left = p4
    p3.right = p5
    print(Solution().levelOrder(p1))



