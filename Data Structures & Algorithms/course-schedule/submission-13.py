class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps = defaultdict(list)

        for p in prerequisites:
            deps[p[0]].append(p[1])
        visited = set()
        needsVisiting = set([i for i in range(numCourses)])

        while len(visited) != len(needsVisiting):
            e = list(needsVisiting - visited)[0]
            queue = deque([(e,{e})])

            while queue:
                n, visiting = queue.popleft()
                if n in visited: continue
                visited.add(n)
                for nei in deps[n]:
                    if nei in visiting: return False
                    queue.append((nei, visiting.union([nei])))
            
        return True