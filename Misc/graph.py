from collections import deque
class Graph:
    def __init__(self, V):
        self.vertices = V
        self.graph:dict[str|int, list[str|int]] = {}

    def add_edges(self,v1, v2):
        if v1 not in self.graph:
            self.graph.update({v1 : []})
        if v2 not in self.graph:
            self.graph.update({v2 : []})
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    def bfs(self):
        queue = deque()
        it = iter(self.graph)
        queue.append(next(it))
        visited = []
        path = []
        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            path.append(curr)
            visited.append(curr)
            for neighbour in self.graph[curr]:
                if neighbour in visited:
                    continue
                queue.append(neighbour)
        return path


    


    def dfs(self):
        visited = {v: False for v in self.graph}
        it = iter(self.graph)
        nodes = []
        def backt(v, graph):
            nodes.append(v)
            visited[v] = True
            for i in graph[v]:
                if visited[i]:
                    continue
                backt(i, graph)

        for vertex in self.graph:
            if not visited[vertex]:
                backt(vertex, self.graph)
        return nodes
    
    def view_graph(self):
        for i, j in enumerate(self.graph):
            print(f"{j} : {self.graph[j]}")


class Solution:
    def __init__(self):
        pass
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        choices = [
            (0,1),#right
            (0,-1),#left
            (1,0),#down
            (-1,0)#up
        ]
        ans = []
        path = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                def backt(dr, dc):
                    if grid[dr][dc] == "0":
                        return
                    visited[dr][dc] = True
                    path.append(grid[dr][dc])
                    for r, c in choices:
                        row = dr + r
                        col = dc + c
                        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                            continue
                        if visited[row][col]:
                            continue
                        backt(row, col)
                    # path.pop()
                    # visited[dr][dc] = False
                backt(i, j)
                ans.append(path.copy())
                path.clear()
        return len(ans)


grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"], 
        ["0", "0", "1", "0", "0"], 
        ["0", "0", "0", "1", "1"]]
s = Solution()
print(s.numIslands(grid))
# g1 = Graph(4)

# g1.add_edges('A', 'B')
# g1.add_edges('A', 'C')
# g1.add_edges('B', 'D')
# g1.add_edges('B', 'E')
# g1.add_edges('C', 'F')
# g1.add_edges('E', 'F')




# F is disconnected

# g1.view_graph()
# print("dfs: ", g1.dfs())
# print("bfs: ", g1.bfs())
# test = {
#     'A' : ['B', 'C', 'E'],
#     'B' : ['A', 'C', 'D'],
#     'C' : ['A', 'B', 'E'],
#     'E' : ['A', 'C', 'D'],
#     'D' : ['B', 'E']
# }
# it = iter(test)
# print(next(it))
# print(next(it))