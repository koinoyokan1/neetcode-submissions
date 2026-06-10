class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def calcParam(i, j, visiting):
            if (i,j) in  visiting: return 0
            visiting.add((i,j))
            ans = 0
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]):
                return ans
            if grid[i][j] == 0: return 0
            
            if i == 0: ans += 1
            if i == len(grid) - 1: ans += 1
            if j == 0: ans += 1
            if j == len(grid[0]) - 1: ans += 1

            if i > 0 and grid[i-1][j] == 0: ans += 1
            if j > 0 and grid[i][j-1] == 0: ans += 1

            if i < len(grid)-1 and grid[i+1][j] == 0: ans += 1
            if j < len(grid[0])-1 and grid[i][j+1] == 0: ans += 1

            return ans + calcParam(i+1, j, visiting) + calcParam(i-1, j, visiting) + calcParam(i, j+1, visiting) + calcParam(i, j-1, visiting)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return calcParam(i, j, set())