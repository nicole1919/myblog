# 删除有序链表中所有出现过的重复节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# @param head ListNode类
# @return ListNode类

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        res = ListNode(-1)
        res.next = head
        cur = res
        flag = 0
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                flag = cur.next.val
                while cur.next is not None and cur.next.val == flag:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return res.next