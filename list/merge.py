# 合并两个有序数组
# 给出一个有序的整数数组 A 和有序的整数数组 B ，请将数组 B 合并到数组 A 中，变成一个有序的升序数组
# 1.保证 A 数组有足够的空间存放 B 数组的元素， A 和 B 中初始的元素数目分别为 m 和 n，A的数组空间大小为 m+n
# 2.不要返回合并的数组，将数组 B 的数据合并到 A 里面就好了，且后台会自动将合并后的数组 A 的内容打印出来，所以也不需要自己打印
# 3. A 数组在[0,m-1]的范围也是有序的
class Solution:
    def merge(self, A, m, B, n):
        i, j = m - 1, n - 1
        flag = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[flag] = A[i]
                flag -= 1
                i -= 1
            elif A[i] == B[j]:
                A[flag] = A[i]
                A[flag - 1] = B[j]
                flag -= 2
                i -= 1
                j -= 1
            else:
                A[flag] = B[j]
                flag -= 1
                j -= 1
        if j >= 0:
            for i in range(j + 1):
                A[i] = B[i]
        return A
