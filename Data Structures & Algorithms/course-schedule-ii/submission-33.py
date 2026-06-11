from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        graph = defaultdict(list)

        for p in prerequisites:
            graph[p[0]].append(p[1])
        
        UNVISITED, VISITING, VISITED = 0, 1, 2 
        status = [UNVISITED] * numCourses
        ans = []

        def dfs(n):
            if status[n] == VISITED: return True
            if status[n] == VISITING: return False

            status[n] = VISITING

            for nei in graph[n]:
                if not dfs(nei): return False

            status[n] = VISITED
            ans.append(n)

            return True

        for i in range(numCourses):
            if not dfs(i): return []
        
        return ans