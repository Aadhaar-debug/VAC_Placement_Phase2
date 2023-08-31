# program to write the dimensions of a binary tree ?


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1


def width(node, level):
    if node is None:
        return 0
    if level == 1:
        return 1
    return width(node.left, level-1) + width(node.right, level-1)


def print_dimensions(node):
    h = height(node)
    for i in range(1, h+1):
        print("Level", i, ":", width(node, i))

root = Node(1)

root.left = Node(2)

root.right = Node(3)

root.left.left = Node(4)

root.left.right = Node(5)
print_dimensions(root)

