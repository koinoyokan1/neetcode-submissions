class Graph:
    def __init__(self, n, edges):
        self.graph = defaultdict(list)
        self.n = n
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

    def isValidTree(self):
        visited = set()
        components = 0
        for i in range(self.n):
            if i in visited: continue
            print('failed: ', i)
            if components != 0: return False
            components += 1
            stack = [(i, None, set([i]))]
            while stack:
                node, prev, visiting = stack.pop()
                print(node)
                for nei in self.graph[node]:
                    if nei == prev: continue
                    if nei in visiting: return False
                    visited.add(nei)
                    stack.append((nei, node, visiting.union([nei])))

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = Graph(n, edges)
        return graph.isValidTree()
        