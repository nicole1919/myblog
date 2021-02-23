# -*- coding: utf-8 -*-
# 冒泡排序


def bubble_sort(arrlist):
    if len(arrlist) <= 1:
        return arrlist
    for i in range(1, len(arrlist)-1):
        flag = False  #设置置换标识
        for j in range(0, len(arrlist) - i - 1):
            if arrlist[j] > arrlist[j+1]:
                arrlist[j], arrlist[j+1] = arrlist[j+1], arrlist[j]
                flag = True
        if not flag:
            print(flag)
            break  #如果第一趟循环没有发生置换，直接退出


if __name__ == "__main__":
    mylist = [1, 2, 3, 4, 5, 6, 7]
    bubble_sort(mylist)
    for i in range(len(mylist)):
        print(mylist[i])

