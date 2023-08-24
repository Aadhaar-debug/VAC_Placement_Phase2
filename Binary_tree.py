class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class BinaryTree:
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
        else:
            self.root = None
 
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
 
    def _insert(self, value, node):
        if value < node.value:
            if node.left:
                self._insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(value, node.right)
            else:
                node.right = Node(value)
 
    def search(self, value):
        if not self.root:
            return False
        else:
            return self._search(value, self.root)
 
    def _search(self, value, node):
        if value == node.value:
            return True
        elif value < node.value and node.left:
            return self._search(value, node.left)
        elif value > node.value and node.right:
            return self._search(value, node.right)
        else:
            return False
 
    def inorder(self):
        if self.root:
            self._inorder(self.root)
 
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value)
            self._inorder(node.right)
            
    def preorder(self):
        if self.root:
            self._preorder(self.root)
 
    def _preorder(self, node):
        if node:
            print(node.value)
            self._preorder(node.left)
            self._preorder(node.right)
    
    def postorder(self):
        if self.root:
            self._postorder(self.root)
 
    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value)
            


# create a binary tree and insert some values
bt = BinaryTree()
bt.insert(8)
bt.insert(3)
bt.insert(10)
bt.insert(1)
bt.insert(6)
bt.insert(14)
bt.insert(4)
bt.insert(7)
bt.insert(13)

# print the inorder traversal of the tree
bt.inorder()
# Output: 1 3 4 6 7 8 10 13 14
 
# print the preorder traversal of the tree
bt.preorder()
# Output: 8 3 1 6 4 7 10 14 13
 
# print the postorder traversal of the tree
bt.postorder()
