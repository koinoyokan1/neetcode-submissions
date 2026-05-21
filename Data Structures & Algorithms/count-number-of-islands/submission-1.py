class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def _hlp(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == '0': return
            
            grid[i][j] = '0'
            _hlp(i+1, j) 
            _hlp(i-1, j) 
            _hlp(i, j+1) 
            _hlp(i, j-1) 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0': continue
                if grid[i][j] == '1':
                    ans += 1
                    _hlp(i, j)
        
        return ans