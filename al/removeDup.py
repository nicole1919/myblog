'''列表去重'''


def removeDup(list1):
    return set(list1)

'''求多个列表的最大值'''


def maxOfMulList(list1, list2, list3):
    return max(max(list1, list2, list3, key=lambda v: max(v)))


if __name__ == "__main__":
    print(removeDup([1, 2, 2, 3, 3, 4]))
    print(maxOfMulList([1, 2, 3], [4], [5, 6, 7]))  #返回7
