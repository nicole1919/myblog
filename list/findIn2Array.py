# 二维数组中的查找
# 在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# [
# [1,2,8,9],
# [2,4,9,12],
# [4,7,10,13],
# [6,8,11,15]
# ]
# 给定 target = 7，返回 true。
# 给定 target = 3，返回 false。
# 思路，从左下角开始遍历，小于目标的话，向右移动，大于目标的话，向左移动

from typing import List

class Solution:
    def findInArray(self, target: int, array: List[List[int]]) -> bool:
        n = len(array)
        if n == 0:
            return False
        m = len(array[0])
        if m == 0:
            return False
        i = n - 1
        j = 0
        while i >= 0 and j < m:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                j = j + 1
            else:
                i = i - 1
        return False




