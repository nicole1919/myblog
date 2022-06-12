# -*- coding: utf-8 -*-
# 判断单链表是否有环
# 思路：1）无穷遍历，直到有指向null的指针，限制时间0.5s或者1s
#      2）借助set集合，查看是否重复，浪费空间，时间复杂度O(n)
#      3) 快慢指针，一个走两步，一个走一步，看是否会相遇

class solution:
    def hascycle(self, head):
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


