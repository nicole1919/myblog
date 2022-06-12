# 链表相加（未通过ac）
# 假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
# 给定两个这种链表，请生成代表两个整数相加值的结果链表。
# 数据范围： 10000000≤n,m≤1000000，链表任意值 90≤val≤9
# 要求：空间复杂度 O(n)，时间复杂度 O(n)
# 例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类


class Solution:
    def ReverseList(self, pHead: ListNode):
        if pHead is None:
            return None
        cur = pHead
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def addInList(self, head1: ListNode, head2: ListNode) -> ListNode:
        # 任意一个链表为空，返回另一个
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        head1 = self.ReverseList(head1)
        head2 = self.ReverseList(head2)
        res = ListNode(-1)
        head = res
        carry = 0  # 进位符号
        while head1 is not None or head2 is not None or carry != 0:
            val1 = 0 if head1 is None else head1.val
            val2 = 0 if head2 is None else head2.val
            tmp = val1 + val2 + carry
            carry = int(tmp / 10)
            tmp = tmp % 10
            head.next = ListNode(tmp)
            head = head.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        return self.ReverseList(res.next)

