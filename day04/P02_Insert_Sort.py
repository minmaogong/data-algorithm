"""
    插入排序
"""

def insert_sort(arr):
    for i in range(1, len(arr)): # 从无序区间一个一个取出元素
        for j in range(i, 0, -1): # 从有序区间从后往前一个一个取出元素，用无序区间中的元素，和有序区见中的元素进行比较
            if arr[j] >= arr[j-1]:
                break
            arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


print(insert_sort([5, 3, 2, 6, 4, 1]))