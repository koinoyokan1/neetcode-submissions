from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        while queue:
            i, j, dst = queue.popleft()
            for (di, dj) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and grid[newi][newj] == 2147483647:
                    grid[newi][newj] = dst + 1
                    queue.append((newi, newj, dst + 1))
        
                     