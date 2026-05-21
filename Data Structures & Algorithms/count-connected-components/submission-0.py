class Graph:
    def __init__(self, n, edges):
        self.graph = defaultdict(list)
        self.n = n
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

    def countComponents(self):
        components = 0
        visited = set()
        for i in range(self.n):
            if i in visited: continue
            components += 1
            stack = [i]
            while stack:
                node = stack.pop()
                for nei in self.graph[node]:
                    if nei in visited: continue
                    visited.add(nei)
                    stack.append(nei)

        return components            

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = Graph(n, edges)
        return graph.countComponents()