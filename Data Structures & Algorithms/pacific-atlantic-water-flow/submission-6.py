class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        canReachPacific = set()
        canReachAtlantic = set()

        def dfs(i, j, reach):
            if (i, j) in reach: return
            reach.add((i,j))

            for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                i2, j2 = di + i, dj + j
                if 0 <= i2 < len(heights) and 0 <= j2 < len(heights[0]):
                    if heights[i2][j2] >= heights[i][j]:
                        dfs(i2, j2, reach)
            
        for i in range(len(heights)):
            dfs(i, 0, canReachPacific)
            dfs(i, len(heights[0])-1, canReachAtlantic)

        for i in range(len(heights[0])):
            dfs(0, i, canReachPacific)
            dfs(len(heights)-1, i, canReachAtlantic)
        
        return list(canReachPacific & canReachAtlantic)
