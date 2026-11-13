class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class binaryTree:
    def __init__(self):
        self.head : Node = None
        self.h = 0

    def build_tree(self,seq):
        it = iter(seq)

        def build(val):
            if val is None:
                return
            newNode = Node(val)
            newNode.left = build(next(it))
            newNode.right = build(next(it))
            return newNode

        root = build(next(it))
        return root

    def print_tree(self, root: Node):
        if root == None:
            return
        print(root.data, end=" ")
        self.print_tree(root.left)
        self.print_tree(root.right)

    def height(self,root):
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)
            


preorder = [1, 2, 4, None, None, 5, None, None, 3, 6, None, None, 7, None, None]
t1 = binaryTree()
r1 = t1.build_tree(preorder)
t1.print_tree(r1)
print()
print(t1.height(r1))