"""
    归并排序
    分解 + 合并
"""

# 对两个数组进行和平==>得到一个有序的数据
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:]) # i 后面剩余的元素添加到merged列表中
    merged.extend(right[j:]) # j 后面剩余的元素添加到merged列表中
    return merged


def merge_sort(arr):
    """归并排序"""
    # 数组长度为1时，不再分割
    if len(arr) <= 1:
        return arr

    # 获取切分的分割点
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(merge_sort([3, 1, 4, 2, 5]))