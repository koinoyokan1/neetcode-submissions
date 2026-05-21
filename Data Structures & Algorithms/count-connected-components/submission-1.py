class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = set()

        def dfs(i):
            stack = [i]

            while stack:
                n = stack.pop()
                if n in visited: continue
                visited.add(n)
                for nei in graph[n]:
                    stack.append(nei)

        ans = 0
        for i in range(n):
            if i in visited: continue
            ans += 1
            dfs(i)
        return ans