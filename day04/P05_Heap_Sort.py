"""
    堆排序
"""


# 堆化
# arr: 处理的数组
# n: 数组中元素的个数
# i: 当前需要进行堆化操作的子树的根节点索引
def heapify(arr, n, i):
    # 默认设置当前堆化的节点位置 为最大值对应的下标
    largest = i
    # 获取左子节点下标
    left = 2 * i + 1
    # 获取右子节点下标
    right = 2 * i + 2

    # 如果左子节点大于父节点，最大节点指向左子节点
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点大于当前最大节点，最大节点指向右子节点
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大节点不是父节点，则交换并递归堆化
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 如果交换位置后，largest节点对结构进行了破坏，需要重新对其进行堆化
        heapify(arr, n, largest)



def heap_sort(arr):

    # 获取数组元素的个数
    n = len(arr)

    # 从最后一个非叶子节点构建大顶堆-----自底向上
    for i in range(n // 2 - 1, -1, -1):
        # 堆化
        heapify(arr, n, i)

    # 依次将堆顶元素放在末尾，并重新堆化
    for j in range(n - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, j, 0) # 自顶向下堆化

    return arr


print(heap_sort([12, 11, 13, 5, 6, 7]))