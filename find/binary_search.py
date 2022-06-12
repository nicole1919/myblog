# -*- coding: utf-8 -*-
# 二分查找,给定有序集合list，查找元素item


def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == "__main__":
    mylist = [1, 2, 3, 4, 5, 6, 7]
    h = binary_search(mylist, 3)
    print(h)
