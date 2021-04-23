# Binary Search Tree
# Insert Order Matters.

class Node:
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node               # Lt root node
        self.right_node = right_node             # Gt root node

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None                         # Top Node in tree

    def __str__(self):
        return str(self.get_all())

    def __set_node(self, value, root_node):
        if value < root_node.value:                                      # Left Node
            if root_node.left_node is None:
                root_node.left_node = Node(value)
            else:
                # recursive left
                self.__set_node(value, root_node.left_node)

        elif value > root_node.value:                                    # Right Node
            if root_node.right_node is None:
                root_node.right_node = Node(value)
            else:
                # # recursive right
                self.__set_node(value, root_node.right_node)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__set_node(value, self.root)

    def __find(self, value, root_node):
        if root_node.value == value:
            return True

        if root_node.left_node is None and root_node.right_node is None:
            return False

        if value < root_node.value:
            return self.__find(value, root_node.left_node)
        elif value > root_node.value:
            return self.__find(value, root_node.right_node)

    def find(self, value):
        if self.root is None:
            return False
        return self.__find(value, self.root)

    def __get_all(self, root_node):
        result = [root_node.value]

        if root_node.left_node:
            result.extend(self.__get_all(root_node.left_node))

        if root_node.right_node:
            result.extend(self.__get_all(root_node.right_node))
        return result

    def get_all(self):
        if self.root is None:
            return None
        else:
            return self.__get_all(self.root)


bs = BinarySearchTree()
bs.insert(10)
bs.insert(2)
bs.insert(15)
bs.insert(14)
bs.insert(3)
bs.insert(0)
bs.insert(100)
bs.insert(-30)


print(bs.root.left_node)   # 2
print(bs.root.right_node)  # 15

print(bs)  # [10, 2, 0, -30, 3, 15, 14, 100]

print(bs.find(-30))   # True
print(bs.find(100))   # True
print(bs.find(400))   # False

print(bs.get_all())   # [10, 2, 0, -30, 3, 15, 14, 100]
