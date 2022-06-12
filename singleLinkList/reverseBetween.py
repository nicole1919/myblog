# 将一个节点数为 size 链表 m 位置到 n 位置之间的区间反转，要求时间复杂度 O(n)，空间复杂度 O(1)。
# 例如：
# 给出的链表为 1-》2 -》3 -》4 -》5 -》NULL1→2→3→4→5→NULL, m=2,n=4m=2,n=4,
# 返回 1-》4-》3-》2-》5-》NULL 1→4→3→2→5→NULL
# 思路：遍历链表，保存前序节点，在m，n区间时，
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m > n:
            return False
        elif m == n:
            return head
        # 加个前序节点
        res = ListNode(-1)
        res.next = head
        # 前序节点
        pre = res
        # 当前节点
        cur = head
        for i in range(1, m):
            pre = cur
            cur = cur.next
        for i in range(m, n):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return res.next


if __name__ == "__main__":
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p = Solution().reverseBetween(p1, 2, 4)
    while p:
        print(p.val)
        p = p.next


