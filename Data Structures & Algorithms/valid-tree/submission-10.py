class Solution:
    def validTree(self, num: int, edges: List[List[int]]) -> bool:
        if num == 0: return None

        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = set()
        cycle = False

        def dfs(start, parent, visiting):
            nonlocal cycle
            if cycle: return
            if start in visited: return
            visited.add(start)

            for nei in graph[start]:
                if nei == parent: continue
                if nei in visiting:
                    cycle = True
                    return
                visiting.add(nei)
                dfs(nei, start, visiting)
                visiting.remove(nei)

        dfs(0, -1, set([0]))
        print(visited)
        return not cycle and len(visited) == num