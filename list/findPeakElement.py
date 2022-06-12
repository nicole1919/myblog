# 寻找数组峰值
# 给定一个长度为n的数组nums，请你找到峰值并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个所在位置即可。
# 1.峰值元素是指其值严格大于左右相邻值的元素。严格大于即不能有等于
# 2.假设 nums[-1] = nums[n] = −∞
# 3.对于所有有效的 i 都有 nums[i] != nums[i + 1]
# 4.你可以使用O(logN)的时间复杂度实现此问题吗？
# @param nums int整型一维数组
# @return int整型
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return None
        left = 0
        right = l - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return right

