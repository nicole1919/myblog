# 链表的奇偶重排，
# 给定一个单链表，请设定一个函数，将链表的奇数位节点和偶数位节点分别放在一起，重排后输出。
# 注意是节点的编号而非节点的数值。
# 输入：{1,2,3,4,5,6}
# 返回值：{1,3,5,2,4,6}
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param head ListNode类
# @return ListNode类
#
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        even = head.next
        odd = head
        evenhead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head