# -*- coding: utf-8 -*-
# 链表交换两个相邻元素
# 输入1->2->3->4，输出2->1->4->3
# 输入1->2->3->4->5，输出2->1->4->3->5

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swappairs(head):
    if head is None or head.next is None:
        return head
    pre = ListNode(0)
    pre.next = head
    tmp = pre
    while tmp and tmp.next:
        a = tmp.next
        b = a.next
        tmp.next, b.next, a.next = b, a, b.next
        tmp = a
    return pre.next

if __name__ == "__main__":
    p1 = ListNode(1)      #建立链表1->2->3->4->None;
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p = swappairs(p1)
    while p:
        print(p.val)
        p = p.next



