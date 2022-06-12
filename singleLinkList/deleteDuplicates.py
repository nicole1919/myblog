# 删除有序链表中重复的元素-I
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        cur = head
        while cur and cur.next:
            tmp = cur.next
            if tmp.val == cur.val:
                cur.next = tmp.next
            else:
                cur = cur.next
        return head

