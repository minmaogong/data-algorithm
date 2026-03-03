"""
    汉诺塔
"""

def print_abc():
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print()

# n: 圆盘的数量
# source: 源柱
# target: 目标柱
# buffer: 缓冲柱
def hanota(n, source, target, buffer):
    # 如果只有一个圆盘，直接将圆盘从源柱移动至目标柱上
    if n == 1:
        target.append(source.pop())
        return

    # 使用f(n-1)的方法借助目标柱将n-1个圆盘从源柱移动至缓冲柱
    hanota(n - 1, source, buffer, target)
    print_abc()

    # 使用f(1)的方法将1个圆盘从源柱移动至目标柱
    hanota(1, source, target, buffer)
    print_abc()

    # 使用f(n-1)的方法借助源柱将n-1个圆盘从缓冲柱移动至目标柱
    hanota(n -1 , buffer, target, source)
    print_abc()

if __name__ == '__main__':
    n = 3 # 圆盘数量
    a = list(range(n, 0 , -1)) # 源柱上的圆盘
    b = [] # 缓冲注
    c = [] # 目标注
    hanota(n, a, c, b)