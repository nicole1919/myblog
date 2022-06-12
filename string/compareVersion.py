# 牛客项目发布项目版本时会有版本号，比如1.02.11，2.14.4等等
# 现在给你2个版本号version1和version2，请你比较他们的大小
# 版本号是由修订号组成，修订号与修订号之间由一个"."连接。1个修订号可能有多位数字组成，修订号可能包含前导0，且是合法的。例如，1.02.11，0.1，0.2都是合法的版本号
# 每个版本号至少包含1个修订号。
# 修订号从左到右编号，下标从0开始，最左边的修订号下标为0，下一个修订号下标为1，以此类推。
#
# 比较规则：
# 一. 比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较忽略任何前导零后的整数值。比如"0.1"和"0.01"的版本号是相等的
# 二. 如果版本号没有指定某个下标处的修订号，则该修订号视为0。例如，"1.1"的版本号小于"1.1.1"。因为"1.1"的版本号相当于"1.1.0"，第3位修订号的下标为0，小于1
# 三.  version1 > version2 返回1，如果 version1 < version2 返回-1，不然返回0.

class Solution:
    def compare(self, version1: str, version2: str) -> int:
        n1 = len(version1)
        n2 = len(version2)
        i, j = 0, 0
        while i < n1 or j < n2:
            num1 = 0
            while i < n1 and version1[i] != ".":
                num1 = num1 * 10 + int(version1[i])
                i += 1
            i += 1
            num2 = 0
            while j < n2 and version2[j] != ".":
                num2 = num2 * 10 + int(version2[j])
                j += 1
            j += 1
            if num1 > num2:
                return 1
            if num1 < num2:
                return -1
        return 0