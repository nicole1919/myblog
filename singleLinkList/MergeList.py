# 合并两个排序的链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def MergeList(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        if pHead1 is None and pHead2 is not None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        pre = cur = ListNode(-1)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        cur.next = pHead1 or pHead2
        return pre.next



