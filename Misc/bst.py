from collections import deque

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        pass
    def build(self, seq: list) -> TreeNode:
            values = iter(seq)
            def helper(val):
                if val == None:
                    return
                newNode = TreeNode(val)
                newNode.left = helper(next(values))
                newNode.right = helper(next(values))
                return newNode
    
            return helper(next(values))
    def preOrder(self, root: TreeNode):
            if root is None:
                return
            print(root.val, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def bfs(self, root: TreeNode):
        queue = deque()
        queue.append(root)

        while queue:
            curr:TreeNode = queue.popleft()
            if curr is None:
                continue
            print(curr.val, end=" ")
            queue.append(curr.left)
            queue.append(curr.right)

    def node_path(self, root: TreeNode, tar: int)-> list:
        path = []
        def dfs(r:TreeNode, t:int):
            if r is None:
                return False
            path.append(r.val)
            if r.val == t:
                return True
            if dfs(r.left,t):
                return True
            if dfs(r.right,t):
                return True
            path.pop()
            
        dfs(root,tar)
        return path



t = Tree()
# preorder = [6, 2, 0, None, None, 4, 3, None, None, 5, None, None, 8, 7, None, None, 9, None, None]
preorder = [3, 5, 6, None, None, 2, 7, None, None, 4, None, None, 1, 0, None, None, 8, None, None]
root = t.build(preorder)
t.bfs(root)
print()
path = t.node_path(root, 4)
print(path)
