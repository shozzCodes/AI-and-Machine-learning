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
        path:list = []
        sol = []
        def dfs(r:TreeNode, t:int):
            if r is None:
                return 
            sol.append(r.val)
            if r.val == t:
                path.append(sol[:])
            dfs(r.left, t)
            dfs(r.right, t)
            sol.pop()
            
        dfs(root,tar)
        return path

    def goodNodes(self, root: TreeNode) -> int:
            good = 0
            l = [float('-inf')]
            def dfs(r:TreeNode):
                nonlocal good
                if r is None:
                    return
                if r.val >= l[-1]:
                     good += 1
                l.append(max(r.val, l[-1]))
                dfs(r.left)
                dfs(r.right)
                l.pop()
            dfs(root)

            return good
                 


t = Tree()
# preorder = [6, 2, 0, None, None, 4, 3, None, None, 5, None, None, 8, 7, None, None, 9, None, None]
preorder = [1,None,None]
root = t.build(preorder)
t.bfs(root)
print()
print(t.goodNodes(root))
