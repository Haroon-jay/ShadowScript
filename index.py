class Node ():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree ():
    def __init__(self, root):
        self.root = Node(root)
    
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


