# -*- coding: utf-8 -*-
# 快速排序(递归)


def quick_sort(array):
   if len(array) < 2:
       return array
   else:
       pivot = array[0]
       less = [i for i in array[1:] if i <= pivot]
       greater = [i for i in array[1:] if i >= pivot]
       return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    print(quick_sort([10, 5, 2, 3]))

