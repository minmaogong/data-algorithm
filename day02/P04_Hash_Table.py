"""
    哈希表
"""
class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashTable:
    def __init__(self):
        # 哈希表中元素的个数
        self.__size = 0
        # 哈希表的数组容量
        self.__capacity = 8
        # 哈希表
        self.__table = [None] * self.__capacity
        # 负载因子
        self.__load_factor = 0.7

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    # 将hash表所有元素展示出来
    def display(self):
        for (index, node) in enumerate(self.__table):
            print(f"当前下标是{index}:", end="")
            current_node = node
            while current_node:
                print(f"({current_node.key}:{current_node.value}),", end="")
                current_node = current_node.next
            print()

    # 扩容
    def __grow(self):
        # 容量变为原来的2倍
        self.__capacity *= 2
        # 备份老数组的数据
        old_table, self.__table = self.__table, [None] * self.__capacity

        # 搬家
        self.__size = 0
        # 对老数组进行遍历
        for node in old_table:
            current_node = node
            while current_node:
                # 调用hash表的添加元素的方法，将当前节点添加到新的数组上
                self.put(current_node.key, current_node.value)
                current_node = current_node.next

    # 根据哈希值获取对应的数组下标
    def __hash(self, key):
        return hash(key) % self.__capacity

    # 添加元素
    def put(self, key, value):
        # 判断是否需要扩容
        if self.__size / self.__capacity >= self.__load_factor:
            self.__grow()

        index = self.__hash(key)
        node = Node(key, value)

        # 如果当前位置为空，直接插入
        if self.__table[index] is None:
            self.__table[index] = node
        else:
            # 否则，发生哈希冲突，链式存储
            current_node = self.__table[index]
            while current_node:
                # 如果键已存在，更新值
                if current_node.key == key:
                    current_node.value = value
                    return
                if not current_node.next:
                    break
                current_node = current_node.next
            # 如果键不存在，插入到链尾部
            current_node.next = node
        self.__size += 1

    # 从哈希表中删除数据
    def remove(self, key):
        index = self.__hash(key)

        if self.__table[index] is None:
            return False
        else:
            # 定义一个变量，存储当前删除节点的上一个节点
            pre_node = None
            current_node = self.__table[index]
            while current_node:
                if current_node.key == key:
                    # 判断删除的是不是头节点
                    if pre_node:
                        #删除的不是头节点
                        pre_node.next = current_node.next
                    else:
                        # 删除的是头节点
                        self.__table[index] = current_node.next
                    self.__size -= 1
                    return True

                pre_node = current_node
                current_node = current_node.next

            return False


    # 获取元素
    def get(self, key):
        if self.is_empty():
            return None

        index = self.__hash(key)
        current_node = self.__table[index]
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return None

    def for_each(self, func):
        for node in self.__table:
            current_node = node
            while current_node:
                func(current_node.key, current_node.value)
                current_node = current_node.next


if __name__ == '__main__':
    hash_table = MyHashTable()
    hash_table.put(1, "zhangsan")
    hash_table.put(2, "lisi")
    hash_table.put(10, "wangwu")
    hash_table.display()
    hash_table.for_each(print)
    print(hash_table.get(2))
    hash_table.remove(10)
    hash_table.display()







