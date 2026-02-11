"""
    选择排序
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