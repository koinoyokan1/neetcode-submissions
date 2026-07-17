from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def longest(prev, i, j):
            if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])): return 0
            curr = matrix[i][j]
            if prev >= curr: return 0

            return max(longest(curr, i+1, j), longest(curr, i-1, j), longest(curr, i, j+1), longest(curr, i, j-1)) + 1
    
        mx = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mx = max(mx, longest(-math.inf, i, j))
        return mx