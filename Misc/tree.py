from collections import deque
from typing import Optional
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        pass

    def build(self, seq: list) -> Node:
        values = iter(seq)
        def helper(val):
            if val == None:
                return
            newNode = Node(val)
            newNode.left = helper(next(values))
            newNode.right = helper(next(values))
            return newNode

        return helper(next(values))

    def preOrder(self, root: Node):
        if root is None:
            return
        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def bfs(self, root: Node):
        queue = deque()
        queue.append(root)

        while queue:
            curr:Node = queue.popleft()
            if curr is None:
                continue
            print(curr.data, end=" ")
            queue.append(curr.left)
            queue.append(curr.right)
        
    def level(self, root: Node):
        lev = 0
        temp = 0
        def helper(r: Node):
            if r is not None:
                nonlocal temp
                temp += 1 #at each new node add 1 level to temp
                helper(r.left)
                helper(r.right)
                temp -= 1 #during backtracking recursively subtract 1
            else:
                nonlocal lev
                lev = temp - 1 if (temp - 1) > lev else lev
        helper(root)
        return lev

            
        
# preorder = [5, 12, 7, 17, None, None, 23, None, None, None, 13, 14, 27, None, None, 3,None, None,  2, 8, None, None, 11, None, None]
preorder = [
    1, 
    2, 4, None, None, 5, None, None,
    3, 6, None, None, 7, None, None
]
# root = [1,2,3,4,5,6,7]
t = tree()
r1 = t.build(preorder)
# t.preOrder(r1)
# print()
t.bfs(r1)
print()
level = t.level(r1)
print(level)
# t.bfs(r1) #Output: [5, 12, 13, 7, 14, 2, 17, 23, 27, 3, 8, 11]