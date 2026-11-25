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


g1 = Graph(4)

g1.add_edges('A', 'B')
g1.add_edges('B', 'A')

g1.add_edges('C', 'D')
g1.add_edges('D', 'C')

# F is disconnected

g1.view_graph()
print(g1.dfs())
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