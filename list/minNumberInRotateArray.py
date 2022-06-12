# 旋转数组的最小数字
# 有一个长度为 n 的非降序数组，比如[1,2,3,4,5]，将它进行旋转，即把一个数组最开始的若干个元素搬到数组的末尾，
# 变成一个旋转数组，比如变成了[3,4,5,1,2]，或者[4,5,1,2,3]这样的。请问，给定这样一个旋转数组，求数组中的最小值。
# @param rotateArray int整型一维数组
# @return int整型
from typing import List


class Solution:
    def minNumberInRotateArray(self, rotateArray: List[int]) -> int:
        l = len(rotateArray)
        if l == 0:
            return False
        left, right = 0, l - 1
        while left < right:
            mid = int((left + right) / 2)
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            # 等于的场景，应该逐渐缩小右边结界
            else:
                right = right - 1
        return rotateArray[left]
