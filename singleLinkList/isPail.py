# 判断一个链表是否为回文结构
# 给定一个链表，请判断该链表是否为回文结构。
# 回文是指该字符串正序逆序完全一致。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param head ListNode类 the head
# @return bool布尔型
#

class Solution:
    # 链表反转
    def reverse(self, head: ListNode):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev


    def isPail(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = fast = head
        # 快慢指针遍历链表，找到中心点（slow节点最后到达中心点）
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow开头的链表逆置
        slow = self.reverse(slow)
        fast = head
        # 从两头开始遍历，判断值是否相等
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True
