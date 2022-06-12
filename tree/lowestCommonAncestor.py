class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        if root is None:
            return -1
        # 保证p是较小值
        if p > q:
            p, q = q, p
        if p < q < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p <= root.val <= q:
            return root.val
        if root.val < p < q:
            return self.lowestCommonAncestor(root.right, p, q)

if __name__ == "__main__":
    p7 = TreeNode(7)
    p1 = TreeNode(1)
    p0 = TreeNode(0)
    p4 = TreeNode(4)
    p3 = TreeNode(3)
    p5 = TreeNode(5)
    p12 = TreeNode(12)
    p7.left = p1
    p7.right = p12
    p1.left = p0
    p1.right = p4
    p4.left = p3
    p4.right = p5
    i = Solution().lowestCommonAncestor(p7, 0, 3)
    print(i)
