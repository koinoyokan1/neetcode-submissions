class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(n, visiting, parent):
            for nei in graph[n]:
                if nei == parent: continue
                if nei in visiting: return True
                res = dfs(nei, visiting.union({nei}), n)
                if res: return res
            return False

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
            visiting = {e[0]}
            if dfs(e[0], visiting, -1): return e
            print(visiting)