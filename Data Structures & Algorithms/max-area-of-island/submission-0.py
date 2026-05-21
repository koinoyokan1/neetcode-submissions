class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mxLen = 0

        def _hlp(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == 0: return 0
            
            grid[i][j] = 0
            
            a = _hlp(i+1, j) 
            b = _hlp(i-1, j) 
            c = _hlp(i, j+1) 
            d = _hlp(i, j-1) 
            return 1 + a + b + c + d

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: continue
                if grid[i][j] == 1:
                    mxLen = max(mxLen, _hlp(i, j))
        
        return mxLen