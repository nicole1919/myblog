# 单链表排序
# 思路：将链表按照中心拆分，递归拆分成单个元素的链表，按照合并有序链表方法在逐个合并
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 合并两个有序链表
    def mergeList(self, list1, list2):
        if list1 and not list2:
            return list2
        if list2 and not list1:
            return list1
        # 加一个表头
        head = ListNode(0)
        cur = head
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        # 链表的剩余部分
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        # 返回时去掉表头
        return head.next


    def sortInList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # 分割链表为两部分
        left = head
        mid = right = head.next
        # 右边的指针到达末尾时，中间的指针指向该段链表的中间
        while right and right.next:
            left = left.next
            mid = mid.next
            right = right.next.next
        # 左边指针指向左段的左右一个节点，从这里断开
        left.next = None
        return self.mergeList(self.sortInList(head), self.sortInList(mid))



