"""
    冒泡排序
    比较 n-1 轮
    for i in range(n-1)
    每轮比较 n-1-i 次

    无序区间在前，有序区间在后，相邻两个元素比较，把大的放后面
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == '__main__':
    print(bubble_sort([5, 4, 3, 2, 1]))