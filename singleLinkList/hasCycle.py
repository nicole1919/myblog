# 判断链表是否有环
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param head ListNode类
# @return bool布尔型


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p2

    p = Solution().hasCycle(p1)
    print(p)
