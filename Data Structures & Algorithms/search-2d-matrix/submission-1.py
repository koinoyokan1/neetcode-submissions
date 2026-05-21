class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False

        i, j = 0, len(matrix[0]) - 1

        while i < len(matrix) and j > -1:
            num = matrix[i][j]
            if num == target: return True
            if num < target: i += 1
            else: j -= 1
        
        return False