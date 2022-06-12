# 179. 最⼤数
# 给定⼀组⾮负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成⼀个最⼤的整数。
# 注意：输出结果
# ⽰例 1：输⼊：nums = [10,2]     输出：“210”
# ⽰例 2：输⼊：nums = [3,30,34,5,9]     输出：“9534330”
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(lambda x, y: int(str(x)+str(y)),int(str(y)+str(x))))
        ans = ''.join([str(num) for num in nums])
        return str(int(ans))
