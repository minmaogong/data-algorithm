"""
    快速排序
    按照基准进行划分，小的在基准左边，大的在基准右边
"""

# 按照基准进行划分
def partition(arr, left, right):
    # 选择基准
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]

        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]

    arr[left] = pivot
    return left # 划分后基准的索引


# arr: 待排序数组
# left: 左指针
# right: 右指针
def quick_sort(arr, left, right):
    if left < right:
        # 选择基准 按照基准进行划分
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)

    return arr


print(quick_sort([3, 1, 5, 4, 2], 0, 4))

    
    