# 给定一个数组height，长度为n，每个数代表坐标轴中的一个点的高度，height[i]是在第i点的高度，请问，从中选2个高度与x轴组成的容器最多能容纳多少水
# 1.你不能倾斜容器
# 2.当n小于2时，视为不能形成容器，请返回0
# 思路：
# step 1：优先排除不能形成容器的特殊情况。
# step 2：初始化双指针指向数组首尾，每次利用上述公式计算当前的容积，维护一个最大容积作为返回值。
# step 3：对撞双指针向中间靠，但是依据贪心思想，每次指向较短边的指针向中间靠，另一指针不变。
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res

