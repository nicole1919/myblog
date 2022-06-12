# 排序，包含整数、字母、浮点，去掉字母按照升序排列
# 2，3，a, e,3.5
def isChar(c):
    if ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('A'):
        return True
    return False

def sort1(a_list):
    l = len(a_list)
    if l == 0:
        return a_list
    for i in range(l):
        if isChar(a_list[i]):
            del a_list[i]
            continue

