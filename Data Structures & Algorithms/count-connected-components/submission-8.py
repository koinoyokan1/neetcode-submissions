class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = set()
        
        def dfs(start):
            print(start)
            for nei in graph[start]:
                if nei in visited: continue
                visited.add(nei)
                dfs(nei)
        
        cnt = 0
        for i in range(n):
            if i in visited: continue
            visited.add(i)
            dfs(i)
            cnt += 1
        
        return cnt