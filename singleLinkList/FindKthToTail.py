# 链表的倒数第k个节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param pHead ListNode类
# @param k int整型
# @return ListNode类


class Solution:
    def FindKthToTail(self, pHead: ListNode, k: int) -> ListNode:
        if pHead is None:
            return None
        fast = slow = pHead
        for i in range(0, k):
            if fast:
                fast = fast.next
            else:
                return None
        while fast:
            fast = fast.next
            slow = slow.next
        return slow