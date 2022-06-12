# 给定一个长度为 n 的可能有重复值的数组，找出其中不去重的最小的 k 个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4(任意顺序皆可)。
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
from heapq import *
from typing import List


class Solution:
    def GetLeastNumbers(self, input: List[int], k: int) -> List[int]:
        res = []
        if len(input) >= k and k != 0:
            # 定义堆
            heap1 = []
            heapify(heap1)
            for i in range(0, k):
                heappush(heap1, (-1 * input[i]))
            for i in range(k, len(input)):
                if (-1 * heap1[0]) > input[i]:
                    heapreplace(heap1, (-1 * input[i]))
            for i in range(k):
                res.append(-1 * heap1[0])
                heappop(heap1)
        return res


if __name__ == "__main__":
    a_list = [1, 5, 2, 3, 7, 8, 9, 10]
    print(Solution().GetLeastNumbers(a_list, 3))
