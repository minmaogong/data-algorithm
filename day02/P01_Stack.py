"""
    栈数据结构
"""

class MyStack:
    def __init__(self):
        self.__size = 0
        self.__items = []

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    # 压栈
    def push(self, item):
        self.__items.append(item)
        self.__size += 1

    # 弹栈
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self.__items.pop()
        self.__size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.__items[self.__size - 1]


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack._MyStack__items)

    print(stack.peek())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())

