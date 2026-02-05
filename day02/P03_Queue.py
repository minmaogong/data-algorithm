"""
    队列数据结构
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyQueue:
    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.__head = self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        else:
            data = self.__head.data
            self.__head = self.__head.next
            self.__size -= 1
            return data

    def for_each(self, func):
        node = self.__head
        while node:
            func(node.data)
            node = node.next

if __name__ == '__main__':
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.for_each(print)

    q.dequeue()
    q.for_each(print)

