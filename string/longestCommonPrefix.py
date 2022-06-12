# 给你一个大小为 n 的字符串数组 strs ，其中包含n个字符串 , 编写一个函数来查找字符串数组中的最长公共前缀，返回这个公共前缀。
# 输入：["abca","abc","abca","abc","abcc"]
# 返回值："abc"
# 思路：最长公共字串属于所有字符串的字串，以第一个字串为标准，遍历数组的每一个字串，遇到空或不一样字符，结束
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        for i in range(len(strs[0])):
            tmp = strs[0][i]
            for j in range(1, n):
                # 注意判断条件的顺序，先比较长度，再比较数值，不会造成数组越界
                if i == len(strs[j]) or strs[j][i] != tmp:
                    return strs[0][:i]
        return strs[0]