class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def _freshFruit(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]): return False
            return grid[i][j] == 1
        
        fresh = 0

        queue = deque()
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
            for _ in range(qsize):
                i, j = queue.popleft()
                for dx, dy in dirs:
                    ni, nj = i+dx, j+dy
                    if _freshFruit(ni, nj):
                        fresh -= 1
                        queue.append((ni, nj))
                        grid[ni][nj] = 2
            mins += 1
            if fresh == 0: return mins
        return -1




