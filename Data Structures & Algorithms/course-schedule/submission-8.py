class Graph:
    def __init__(self, vertexCnt, edges):
        self.graph = defaultdict(list)
        self.vertexCnt = vertexCnt

        for edge in edges:
            self.graph[edge[0]].append(edge[1])

    def hasCycle(self):
        visited = set()

        for i in range(self.vertexCnt):
            stack = [(i, set([i]))]
            while stack:
                node, visiting = stack.pop()

                for nei in self.graph[node]:
                    if nei in visiting: return True
                    stack.append((nei, visiting.union([nei])))
            
        return False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = Graph(numCourses, prerequisites)
        return not g.hasCycle()
