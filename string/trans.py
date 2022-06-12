# 对于一个长度为 n 字符串，我们需要对它做一些变形。
# 首先这个字符串中包含着一些空格，就像"Hello World"一样，然后我们要做的是把这个字符串中由空格隔开的单词反序，同时反转每个字符的大小写。
# 比如"Hello World"变形后就变成了"wORLD hELLO"。


class Solution:
    def trans(self, s: str, n: int) -> str:
        if n == 0:
            return s
        res = ""
        for i in range(n):
            # 大小写转换
            if 'Z' >= s[i] >= 'A':
                res += chr(ord(s[i]) - ord('A') + ord('a'))
            elif 'a' <= s[i] <= 'z':
                res += chr(ord(s[i]) - ord('a') + ord('A'))
            else:
                # 空格直接复制
                res += s[i]
        # 单词反序
        res = list(res.split(' '))[::-1]
        return ' '.join(res)


if __name__ == "__main__":
    str1 = 'This is a sample'
    n = 16
    res1 = Solution().trans(str1, n)
    print(res1)
