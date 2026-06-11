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

            for nei in graph[n]:
                if status[nei] == VISITING: 
                    return False

                if status[nei] == UNVISITED: 
                    status[nei] = VISITING
                    if not dfs(nei): return False

            status[n] = VISITED
            ans.append(n)
            return True

        for i in range(numCourses):
            if status[i] != VISITED:
                status[i] = VISITING
                if not dfs(i): return []
        
        return ans