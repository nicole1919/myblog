# 给定一个长度为 n 的字符串，请编写一个函数判断该字符串是否回文。如果是回文请返回true，否则返回false。
# 字符串回文指该字符串正序与其逆序逐字符一致。

class Solution:
    def judgeHuiWen(self, str: str) -> bool:
        l = len(str)
        if l == 0:
            return True
        left, right = 0, l-1
        while left < right:
            if str[left] != str[right]:
                return False
            else:
                left +=1
                right -=1
        return True