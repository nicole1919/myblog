
class Solution:
    dict1 = {')': '(', ']': '[', '}': '{'}
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l <= 1:
            return False
        for i in range(0, l - 1, 2):
            if i == l - 1 or s[i] != self.dict1.get(s[i + 1]):
                return False
        return True

if __name__ == '__main__':
    s = '[])'
    print(Solution().isValid(s))
