class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq = defaultdict(list)

        for p in prerequisites:
            prereq[p[1]].append(p[0])

        def isPrereq(start, pre, visiting):
            if start == pre: return True
            if start in visiting: return False
            visiting.add(start)

            for c in prereq[start]:
                if isPrereq(c, pre, visiting): return True
            
            return False

        ans = []
        for q in queries:
            ans.append(isPrereq(q[1], q[0], set()))
        
        return ans