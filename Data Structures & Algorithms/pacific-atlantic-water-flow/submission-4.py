class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def _valid(i, j):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]): return False
            return True

        queue = deque()

        for i in range(len(heights)):
            queue.append((i, 0))
        for i in range(len(heights[0])):
            queue.append((0, i))
        
        pacific = set()
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            i, j = queue.popleft()
            if (i, j) in pacific: continue
            pacific.add((i, j))
            for dx, dy in dirs:
                ni, nj = i+dx, j+dy
                if _valid(ni, nj) and heights[ni][nj] >= heights[i][j] and (ni, nj) not in pacific:
                    queue.append((ni, nj))


        queue = deque()

        for i in range(len(heights)):
            queue.append((i, len(heights[0])-1))
        for i in range(len(heights[0])):
            queue.append((len(heights)-1, i))
        
        atlantic = set()
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            i, j = queue.popleft()
            if (i, j) in atlantic: continue
            atlantic.add((i, j))
            for dx, dy in dirs:
                ni, nj = i+dx, j+dy
                if _valid(ni, nj) and heights[ni][nj] >= heights[i][j] and (ni, nj) not in atlantic:
                    queue.append((ni, nj))
        
        ans = list(atlantic.intersection(pacific))
        ans.sort()
        return ans
