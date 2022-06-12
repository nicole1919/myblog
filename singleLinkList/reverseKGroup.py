'''描述
将给出的链表中的节点每 k 个一组翻转，返回翻转后的链表
如果链表中的节点数不是 k 的倍数，将最后剩下的节点保持原样
你不能更改节点中的值，只能更改节点本身。

数据范围： 0≤n≤2000 ，20001≤k≤2000 ，链表中每个元素都满足 10000≤val≤1000
要求空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)
例如：
给定的链表是 1\to2\to3\to4\to51→2→3→4→5
对于 k = 2k=2 , 你应该返回 2\to 1\to 4\to 3\to 52→1→4→3→5
对于 k = 3k=3 , 你应该返回 3\to2 \to1 \to 4\to 53→2→1→4→5'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可

# @param head ListNode类
# @param k int整型
# @return ListNode类

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        # 找到每次翻转的尾部
        tail = head
        for i in range(0, k):
            if tail is None:
                return head
            tail = tail.next
        # 反转k个节点
        pre = None
        cur = head
        while cur != tail:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        head.next = self.reverseKGroup(tail, k)
        return pre


if __name__ == "__main__":
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    p6 = ListNode(6)
    p7 = ListNode(7)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p6
    p6.next = p7
    p = Solution().reverseKGroup(p1, 3)
    while p:
        print(p.val)
        p = p.next