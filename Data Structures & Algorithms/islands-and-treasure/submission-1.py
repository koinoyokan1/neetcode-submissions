import math
from functools import lru_cache

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def _valid(i, j):
            if i < 0 or j < 0 or i  == len(grid) or j == len(grid[0]): return False
            return grid[i][j] == 2147483647

        ans = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: 
                    queue.append((i, j, 0))
        
        dirs = [(-1,0),(1,0),(0,1),(0,-1)] 
        seen = set()
        while queue:
            qsize = len(queue)
            for _ in range(qsize):
                i, j, dist = queue.popleft()
                if (i, j) in seen: continue
                seen.add((i, j))
                ans[i][j] = dist
                for dirx, diry in dirs:
                    ni, nj = i + dirx, j + diry
                    if _valid(ni, nj) and (ni, nj) not in seen:
                        queue.append((ni, nj, dist+1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = ans[i][j]



