from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            degree[e[0]] += 1
            degree[e[1]] += 1

        print(degree)
        queue = deque()
        for v in degree.keys():
            if degree[v] == 1: queue.append(v)
        while queue:
            v = queue.popleft()
            for nei in graph[v]:
                if degree[nei] == 0: continue
                degree[nei] -= 1
                if degree[nei] == 1: queue.append(nei)
            degree[v] -= 1
        
        print({k:v for k,v in degree.items() if v != 0})
        for e in edges[::-1]:
            if degree[e[0]] != 0 and degree[e[1]] != 0: return e
        