"""
    算法的时间复杂度
    时间复杂度用来描述一个算法所需时间资源的多少。
    为了屏蔽计算机硬件差异对评估结果的影响。我们不适用算法运行的绝对运行时间，
    而是使用运行算法时执行的基本指令数量来衡量其所需的时间资源
"""
import time


"""
# 使用绝对时间 计算算法运行花费时间多少
def seq_sum(sums):
    start_time = time.time()
    res_sum = 0
    i = -1
    while (i := i + 1) < len(sums):
        res_sum += sums[i]
    end_time = time.time()
    print(f"总耗时：{end_time - start_time}")
    return res_sum

print(seq_sum(range(100000000)))
"""
"""
# 分析算法运行的时候，执行指令
def seq_sum(sums):
    # 1次赋值指令
    res_sum = 0

    # 1次赋值指令
    i = -1
    # n + 1运算  n+1  赋值      n+1次比较
    while (i := i + 1) < len(sums):
        # n次运算      n次赋值
        res_sum += sums[i]
    return res_sum

print(seq_sum(range(100000000)))
"""

def find_max(nums):
    max_num = nums[0] # 1次赋值操作
    i = 0 # 1次赋值操作
    while (i := i + 1) < len(nums): # n次加法运算 + n次赋值操作 + n次比较运算
        if nums[i] > max_num: # n-1次比较运算
            max_num = nums[i] # 0~(n-1)次赋值操作
    return max_num