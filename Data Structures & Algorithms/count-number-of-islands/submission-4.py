class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def markLandAsWater(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                markLandAsWater(i+1, j)
                markLandAsWater(i-1, j)
                markLandAsWater(i, j+1)
                markLandAsWater(i, j-1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': 
                    markLandAsWater(i, j)
                    cnt += 1
        
        return cnt