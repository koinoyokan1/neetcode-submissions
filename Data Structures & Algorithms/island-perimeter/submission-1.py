class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            # If we go out of bounds, we found a boundary/water edge -> perimeter + 1
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return 1
            
            # If we hit water, we found an internal water edge -> perimeter + 1
            if grid[i][j] == 0:
                return 1
            
            # If we already visited this land cell, don't count it again
            if (i, j) in visited:
                return 0
            
            # Mark the current land cell as visited
            visited.add((i, j))
            
            # Sum up the perimeter from all 4 directions
            return (dfs(i + 1, j) + 
                    dfs(i - 1, j) + 
                    dfs(i, j + 1) + 
                    dfs(i, j - 1))

        # Find the first piece of land and kick off the DFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # The problem guarantees exactly one island, so we can return immediately
                    return dfs(i, j)