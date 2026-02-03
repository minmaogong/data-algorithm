"""
    模拟数组数据结构
"""
class MyArray:
    def __init__(self):
        # 数组的初始化容量
        self.__capacity = 8
        # 数组中元素的歌树
        self.__size = 0
        # 真正存储数据的对象
        self.__items = [0] * self.__capacity

    # 获取数组中元素的个数
    @property
    def size(self):
        return self.__size

    # 判断数组是否为空
    def is_empty(self):
        return self.__size == 0

    # 扩容
    def __grow(self):
        # 创建新的数组 容量是原来的2倍
        self.__capacity *= 2
        new_items = [0] * self.__capacity

        # 将老数组数据 复制到新的数组中
        for i in range(self.__size):
            new_items[i] = self.__items[i]

        # 将数组存储数据的对象地址。指向新的数组
        self.__items = new_items

    # 打印输出数组元素
    def __str__(self):
        res_str = "["
        for i in range(self.__size):
            res_str += str(self.__items[i])
            if i != self.__size - 1:
                res_str += ", "
        res_str += "]"
        return res_str

    # 向数组指定的位置添加元素
    def insert(self, index, item):
        if index < 0 or index > self.__size:
            raise IndexError("index out of range")

        # 判断是否需要扩容
        if self.__size == self.__capacity:
            self.__grow()

        # while (i := self.__size - 1) >= index:
        #     self.__items[i+1] = self.__items[i]
        #     i -= 1
        for i in range(self.__size, index, -1):
            self.__items[i] = self.__items[i - 1]

        self.__items[index] = item

        self.__size += 1

    # 向数组中追加元素
    def append(self, item):
        self.insert(self.__size, item)

    # 从指定位置删除元素
    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        for i in range(index, self.__size - 1):
            self.__items[i] = self.__items[i+1]

        # self.__items[self.__size - 1] = 0

        self.__size -= 1

    # 修改数组中指定位置的元素
    def set(self, index, item):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        self.__items[index] = item

    # 获取数组中指定位置的元素
    def get(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        return self.__items[index]

    # 获取元素在数组中第一次出现的下标
    def find(self, item):
        for i in range(self.__size):
            if self.__items[i] == item:
                return i

        return -1

    # 遍历数组元素
    def for_each(self, func):
        for (index, item) in enumerate(self.__items):
            if index < self.__size:
                func(index, item)
            else:
                break



if __name__ == "__main__":
    arr = MyArray()
    arr.insert(0, 1)
    arr.insert(1, 2)
    arr.insert(2, 3)
    arr.append(4)
    # arr.insert(2, 5)
    # arr.remove(4)
    arr.append(5)
    arr.append(6)
    arr.append(7)
    arr.append(8)
    arr.append(9)
    # print(arr)
    arr.for_each(lambda index, item: print(index, item))