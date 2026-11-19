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

    def depth(self,r:Node):
        if r is not None:
            left = self.depth(r.left)
            right = self.depth(r.right)
            return 1 + max(left, right)
        else:
            return 0
        
    def isBalanced(self, root: Optional[Node]) -> bool:
        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        diff = left - right
        if abs(diff) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def preOrd(self, root:Node):
        arr = []
        def helper(r:Node):
            if r is not None:
                arr.append(r.data)
                helper(r.left)
                helper(r.right)
            else:
                arr.append(None)
        helper(root)
        return arr
    def isSameTree(self, p: Node | None, q: Node | None) -> bool:
        x = []
        y = []
        self.preOrd(p, x)
        self.preOrd(q, y)
        return x == y
        
    def levelOrder(self, root: Node | None) -> list[list[int]]:
        if root is None:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            temp = []
            for _ in range(len(q)):
                curr:Node = q.popleft()
                if curr is None:
                    continue
                q.append(curr.left)
                q.append(curr.right)
                temp.append(curr.data)
            if temp:
                ans.append(temp)

        return ans
    
    def dfs(self, root:Node)->list:
        ans = []
        def helper(root:Node, arr):
            if root is None:
                return
            ans.append(root.data)
            helper(root.left, ans)
            helper(root.right, ans)
        helper(root, ans)
        return ans

    def isValidBST(self, root: Optional[Node]) -> bool:
        values = self.dfs(root) # list contain preord seq of bst
        for x in values:
            def helper(rt:Node):
                if rt is None:
                    return True
                if x != rt.data:
                    return False
                elif x < rt.data:
                    helper(rt.left)
                elif x > rt.data:
                    helper(rt.right)

            if not helper(root):
                return False
        return True






# preorder = [10,
#             5, 2, None, 6, None, None,
#             8, 11, None, None, None,
#             15, None, 1, None, None]
preorder = [2,1,None, None,3,None,None]
t = tree()
root = t.build(preorder)
t.bfs(root) 
print()
arr = t.dfs(root)
print(arr)
print(t.isValidBST(root))
# print(t.isValidBST(root))
# # preorder = [5, 12, 7, 17, None, None, 23, None, None, None, 13, 14, 27, None, None, 3,None, None,  2, 8, None, None, 11, None, None]
# preorder = [
#     1,
#     2, None, None,
#     3, 4, None, None, None
# ]
# # root = [1,2,3,4,5,6,7]
# t = tree()
# r1 = t.build(preorder)
# t.preOrder(r1)
# print()
# print(t.isBalanced(r1))
# # print()
# # t.bfs(r1) #Output: [5, 12, 13, 7, 14, 2, 17, 23, 27, 3, 8, 11]

# tree1 = [1, 2, None, None, None]
# p = t.build(tree1)
# tree2 = [1, None, 2, None, None]
# q = t.build(tree2)
# t.preOrder(p)
# print()
# arr = t.preOrd(p)
# print(arr)
# # t.preOrder(q)
# # print()
# # print(t.isSameTree(p,q))
