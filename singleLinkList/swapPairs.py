# 链表交换相邻的元素
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        res = ListNode(-1)
        res.next = head
        #前序节点
        pre = res
        cur = head
        while cur and cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
            pre = cur
            cur = cur.next
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
    p = Solution().swapPairs(p1)
    while p:
        print(p.val)
        p = p.next

