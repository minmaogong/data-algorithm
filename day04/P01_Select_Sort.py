"""
    选择排序
    有序区间在前，无序区间在后，选择无序区间第一个元素作为最小值的索引，然后和无序区间的元素依次进行比较，找出最小值对应的索引，然后和第一个元素进行交换
"""

def select_sort(arr):
    for i in range(len(arr) - 1):# 最后一个元素不需要比较
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


print(select_sort([5, 3, 2, 6, 4, 1]))