"""
    动态规划算法案例：爬楼梯
"""
# 自上而下递归
def climb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb(n - 1) + climb(n - 2)

# 自下而上迭代
def climb2(n):
    pre = 1
    cur = 1
    for _ in range(1, n):
        pre, cur = cur, pre + cur

    return cur

print(climb(5))
print(climb2(10))