class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        ln = len(edges)

        degree = [0] * (ln+1)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
            degree[e[0]] += 1
            degree[e[1]] += 1

        queue = deque()
        for i in range(1, ln + 1):
            if degree[i] == 1:
                queue.append(i)

        visited = set()
        while queue:
            n = queue.popleft()
            degree[n] = 0
            if n in visited: continue
            visited.add(n)
            for nei in graph[n]:
                if degree[nei] > 0:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        queue.append(nei)
        

        cycle = set(i for i in range(1, ln + 1) if degree[i] >= 2)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]