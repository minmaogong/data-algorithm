"""
    摩尔投票法/半数查找法
    找出数组中过半的元素
    返回数组中数量超过半数的元素，要求时间复杂度O(n)，空间复杂度O(1)
    示例：
        输入: nums = [2, 2, 1, 1, 1, 2, 2]
        输出: 2
"""
def majority_element(nums):
    candidate = nums[0]
    count = 1
    for num in nums[1:]:
        if num == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = num
                count = 1

    return candidate

if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element(nums))