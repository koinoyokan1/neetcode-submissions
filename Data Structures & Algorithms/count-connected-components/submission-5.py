class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = set()
        
        def dfs(start):
            if start in visited: return
            visited.add(start)
            for nei in graph[start]:
                dfs(nei)
        
        cnt = 0
        for i in range(n):
            if i in visited: continue
            dfs(i)
            cnt += 1
        
        return cnt