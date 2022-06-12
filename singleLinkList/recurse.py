#反转链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def revLinkList(phead):
    if phead is None or phead.next is None:
        return phead
    pre = None
    head = phead
    while head:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre


if __name__ == "__main__":
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p1.next = p2
    p2.next = p3
    p = revLinkList(p1)
    while p:
        print(p.val)
        p = p.next
