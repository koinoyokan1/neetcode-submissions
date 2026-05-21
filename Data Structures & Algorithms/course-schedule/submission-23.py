from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps = defaultdict(list)
        for prereq in prerequisites:
            before = prereq[0]
            after = prereq[1]
            deps[before].append(after)
        
        visited = set()
        for i in range(numCourses):
            if i in visited: continue
            stack = [(i, set([i]))]
            while stack:
                node, visiting = stack.pop()
                visited.add(node)
                for neigh in deps[node]:
                    if neigh in visiting: return False
                    if neigh in visited: continue
                    stack.append((neigh, visiting.union([neigh])))
        
        return True