"""
    链表数据结构
"""

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.__size = 0
        self.__head = None

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def __str__(self):
        res_list = []

        node = self.__head
        while node:
            res_list.append(str(node.data))
            node = node.next

        return "->".join(res_list)

    def insert(self, index, item):
        if index < 0 or index > self.__size:
            raise IndexError("index out of range")

        # 判断是否插入的是头节点
        if index == 0:
            self.__head = Node(item, self.__head)
        else:
            # 如果插入的不是头节点，需要先获取要插入的位置前一个节点
            pre_node = self.__head
            for i in range(index-1):
                pre_node = pre_node.next

            pre_node.next = Node(item, pre_node.next)

        self.__size = index + 1

    def append(self, item):
        self.insert(self.__size, item)

    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        if index == 0:
            self.__head = self.__head.next
        else:
            pre_node = self.__head
            for i in range(index-1):
                pre_node = pre_node.next

            pre_node.next = pre_node.next.next

        self.__size -= 1

    def set(self, index, item):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        node = self.__head
        for i in range(index):
            node = node.next

        node.data = item

    def get(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        node = self.__head
        for i in range(index):
            node = node.next

        return node.data

    def find(self, item):
        node = self.__head
        for i in range(self.__size):
            if node.data == item:
                return i
            node = node.next
        return -1

    def for_each(self, func):
        node = self.__head
        while node:
            func(node.data)
            node = node.next

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.insert(0, 1)
    ll.insert(1, 2)
    ll.insert(2, 3)
    ll.append(4)
    ll.remove(1)
    ll.set(1, 200)
    print(ll.get(2))
    print(ll.find(4))
    ll.for_each(print)
    print(ll)