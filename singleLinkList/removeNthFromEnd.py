# 删除链表的倒数第n个节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类
# @param n int整型
# @return ListNode类


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        res = ListNode(-1)
        res.next = head
        pre = res
        for i in range(0, n):
            if fast:
                fast = fast.next
            else:
                return res.next
        while fast:
            fast = fast.next
            slow = slow.next
            pre = pre.next
        pre.next = slow.next
        return res.next
