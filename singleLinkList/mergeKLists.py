# 中等难度
# 合并k个已排序的链表
# 思路：使用分治法，将k个链表的合并，分拆成链表的两两合并，使用递归方法解决
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 先定义合并两个有序链表的方法
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

    # 划分合并区间函数
    def divideMerge(self, lists: List[ListNode], left: int, right: int) -> ListNode:
        if left > right:
            return None
        if left == right:
            return lists[left]
        # 从中间分成两段，再将合并好的两段合并
        mid = int((left + right) / 2)
        # 将划分的左边和右边按照合并两个有序链表的方法，依次递归合并
        return self.MergeList(self.divideMerge(lists, left, mid), self.divideMerge(lists, mid + 1, right))

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # k个链表归并排序
        return self.divideMerge(lists, 0, len(lists) - 1)

