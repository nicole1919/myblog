# 给定一个长度为 n 的数组 nums 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。
# 输入：[2,3,4,2,6,2,5,1],3
# 返回值：[4,4,6,6,6,5]
from collections import deque
from typing import List


class Solution:
    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        if not num:
            return []
        window = deque()
        res = []
        for i, x in enumerate(num):
            # 超出范围的直接出队
            if i >= size and window[0] <= i - size:
                window.popleft()
            while window and num[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= size - 1:
                j = window.popleft()
                res.append(num[j])
                window.appendleft(j)
        return res




