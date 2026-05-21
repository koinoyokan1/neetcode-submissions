class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh  = 0
        rottenFruits = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: fresh += 1
                if grid[i][j] == 2: rottenFruits.append((i, j, 0))

        t = 0
        ans = 0

        while fresh:
            if not rottenFruits: return -1
            i, j, t = rottenFruits.popleft()

            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj

                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                    rottenFruits.append((ni, nj, t+1))
                    grid[ni][nj] = 2
                    fresh -= 1
            ans = t+1

        return ans
