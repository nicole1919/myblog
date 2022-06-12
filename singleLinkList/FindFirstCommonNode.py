# 返回两个链表的第一个公共结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        p1 = pHead1
        p2 = pHead2
        while p1 is not p2:
            if p1 is None:
                p1 = pHead2
            else:
                p1 = p1.next
            if p2 is None:
                p2 = pHead1
            else:
                p2 = p2.next
        return p1