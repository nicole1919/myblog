# 最长无重复子数组
# 思路：step 1：构建一个哈希表，用于统计数组元素出现的次数。
# step 2：窗口左右界都从数组首部开始，每次窗口优先右移右界，并统计进入窗口的元素的出现频率。
# step 3：一旦右界元素出现频率大于1，就需要右移左界直到窗口内不再重复，将左边的元素移除窗口的时候同时需要将它在哈希表中的频率减1，保证哈希表中的频率都是窗口内的频率。
# step 4：每轮循环，维护窗口长度最大值。

class Solution:
    def maxLength(self , arr: List[int]) -> int:
        count = {}
        res = 0
        left = 0
        for right in range(len(arr)):
            if arr[right] in count:
                count[arr[right]] += 1
            else:
                count[arr[right]] = 1
            while count[arr[right]] > 1:
                count[arr[left]] -= 1
                left += 1
            # 每一轮维护最大值，res一直保持最大值
            res = max(res, right - left + 1)
        return res