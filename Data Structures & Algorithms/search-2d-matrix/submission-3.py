class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1

        while 0 <= l < len(matrix) and 0 <= r < len(matrix[0]):
            if target == matrix[l][r]: return True
            if matrix[l][r] < target: l += 1
            else: r -= 1
        
        return False