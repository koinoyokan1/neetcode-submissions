class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))

        dst = 0
        while queue:
            ln = len(queue)
            for _ in range(ln):
                i, j = queue.popleft()
                if grid[i][j] != 2147483647 and grid[i][j] != 0: continue
                grid[i][j] = dst

                for di, dj in [(0,1), (0,-1), (-1,0),(1,0)]:
                    i2, j2 = di + i, dj + j
                    if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]) and grid[i2][j2] == 2147483647:
                        queue.append((i2, j2))
            dst += 1
