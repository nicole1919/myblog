#输入列表[1,2,3,4,5,6,7,8],整数3，将列表的后3位移动到前面去


def move(list1, n):
    k = len(list1)-n
    listNew = list1[k:len(list1)]+list1[0:k]
    return listNew


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = move(list1, 3)
    print(list2)