class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def _invalid(neighbori, neighborj):
                    if neighbori >= 0 and neighbori < len(grid) and neighborj >= 0 and neighborj < len(grid[0]) and grid[neighbori][neighborj] == 1: return False
                    return True

        queue = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0: return 0
        if len(queue) == 0: return -1

        mins = 0
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while queue:
            qsize = len(queue)
            for x in range(qsize):
                i, j = queue.popleft()
                for dx, dy in dirs:
                    ni, nj = i+dx, j+dy
                    if _invalid(ni, nj): continue
                    grid[ni][nj] = 2
                    fresh -= 1
                    queue.append((ni, nj))

            mins += 1
        
            if fresh == 0: return mins
        return -1
        