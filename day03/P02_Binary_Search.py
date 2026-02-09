"""
    折半查找｜二分查找法
"""

# nums: 要查找的数组(list)
# target: 要查找的目标数据
# 前提: 排好序的有序列表
def binary_search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
