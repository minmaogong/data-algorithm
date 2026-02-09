"""
    二叉搜索树
"""
from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        # 树中元素的个数
        self.__size = 0
        # 树的根节点
        self.__root = None

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def print_tree(self):
        """打印树的结构"""

        # 先得到树的层数
        def get_layer(node):
            """递归计算树的层数"""
            if node is None:
                return 0
            else:
                left_depth = get_layer(node.left)
                right_depth = get_layer(node.right)
                return max(left_depth, right_depth) + 1

        layer = get_layer(self.__root)

        # 层序遍历并打印
        queue = deque([(self.__root, 1)])
        current_level = 1
        while queue:
            node, level = queue.popleft()
            if level > current_level:
                print()
                current_level += 1
            if node:
                print(f"{node.data:^{20 * layer // 2 ** (level - 1)}}", end="")
            else:
                print(f"{"N":^{20 * layer // 2 ** (level - 1)}}", end="")
            if level < layer:
                if node:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
                else:
                    queue.append((None, level + 1))
                    queue.append((None, level + 1))
        print()

    # 查找节点是否存在
    def search(self, item):
        return self.__search_pos(item)[0] is not None

    # 返回查找到的节点和其父节点
    def __search_pos(self, item):
        parent = None
        current = self.__root
        while current:
            if current.data == item:
                break

            parent = current
            current = current.left if item < current.data else current.right

        return current, parent

    # 插入节点
    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__root = node
        else:
            current, parent = self.__search_pos(item)
            if current: # 当前节点已经存在
                return
            else:
                if item < parent.data:
                    parent.left = node
                else:
                    parent.right = node
        self.__size += 1


    # 删除节点
    def remove(self, item):
        current, parent = self.__search_pos(item)
        if not current:
            return

        if not current.left and not current.right: # 如果删除的是叶子节点（没有子节点）
            if parent: # 如果parent不为空，说明current是子节点
                if current == parent.left:
                    parent.left = None
                else:
                    parent.right = None
            else: # 如果parent为none，说明current是根节点
                self.__root = None
        elif not current.left or not current.right: # 如果删除的节点只有一个子节点
            child = current.left if current.left else current.right
            if parent: # 删除的不是根节点
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else: # 删除的是根节点，删除后它的子节点作为根节点
                self.__root = child
        else: # 如果删除的节点有两个子节点
            # 找到右子树上最小节点
            successor = self.__get_min(current.right)
            # 找到右子树上最小节点对应的值
            successor_data = successor.data

            self.remove(successor_data)
            # 注意：这里我们只进行了替换，不需要元素-1
            self.__size += 1
            current.data = successor_data

        self.__size -= 1


    # 查找树的最小节点
    def __get_min(self, node):
        min_node = node
        while min_node.left:
            min_node = min_node.left

        return min_node

    # 二叉树遍历
    def for_each(self, func, order="inorder"):
        """遍历树，默认中序遍历"""
        match order:
            case "inorder": # 深度优先搜索：中序遍历
                self.__inorder_traversal(func)
            case "preorder": # 深度优先搜索：前序遍历
                self.__preorder_traversal(func)
            case "postorder": # 深度优先搜索：后序遍历
                self.__postorder_traversal(func)
            case "levelorder": # 广度优先搜索：层序遍历
                self.__levelorder_traversal(func)

    def __inorder_traversal(self, func):
        """深度优先搜索：中序遍历"""
        def inorder(node):
            if node:
                inorder(node.left)
                func(node.data)
                inorder(node.right)

        inorder(self.__root)

    def __preorder_traversal(self, func):
        """深度优先搜索：前序遍历"""
        def preorder(node):
            if node:
                func(node.data)
                preorder(node.left)
                preorder(node.right)
        preorder(self.__root)

    def __postorder_traversal(self, func):
        """深度优先搜索：后序遍历"""
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                func(node.data)
        postorder(self.__root)


    def __levelorder_traversal(self, func):
        """广度优先搜索：层序遍历"""
        queue = deque()
        queue.append(self.__root)
        while queue:
            node = queue.popleft()
            func(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(1)
    tree.add(6)
    tree.add(2)
    tree.add(5)
    tree.add(7)

    tree.print_tree()
    print("~~~~"*10)
    # tree.remove(3)
    # tree.print_tree()
    tree.for_each(print, order="inorder")