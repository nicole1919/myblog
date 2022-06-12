# 对于一个长度为 n 字符串，我们需要对它做一些变形。
# 输入"123 abc 456" ，输出"321 cba 654"


class Solution:
    # 方法1：字符串按照空格切分成list，然后将每个list值反转，最后拼接
    def trans2(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return s
        list1 = s.split(" ")
        for i in range(len(list1)):
            list1[i] = (list1[i])[::-1]
        res = " ".join(list1)
        return res

if __name__ == "__main__":
    str1 = '123 abc 456'
    res1 = Solution().trans2(str1)
    print(res1)
