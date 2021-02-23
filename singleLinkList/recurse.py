# -*- coding: utf-8 -*-
# 反转单链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def recurse(head):
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    h = head  #for return
    while cur:
        h = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return h


if __name__ == "__main__":
    head = ListNode(1)    #测试代码
    p1 = ListNode(2)      #建立链表1->2->3->4->None;
    p2 = ListNode(3)
    p3 = ListNode(4)
    head.next = p1
    p1.next = p2
    p2.next = p3
    p = recurse(head)   #输出链表 4->3->2->1->None
    while p:
        print(p.val)
        p = p.next




