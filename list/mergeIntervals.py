# 给出一组区间，请合并所有重叠的区间。
# 请保证合并后的区间按区间起点升序排列。
# 输入： [[10,30],[20,60],[80,100],[150,180]]
# 返回值： [[10,60],[80,100],[150,180]]
# ==========cmp_to_key的用法=============

from functools import cmp_to_key
class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        res = list()
        if len(intervals) == 0:
            return res
        # 对整体列表，按照区间首排序
        intervals.sort(key=cmp_to_key(lambda a, b: a.start - b.start))
        res.append(intervals[0])
        for i in range(len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(intervals[i].end, res[-1].end)
            else:
                res.append(intervals[i])
        return res









