class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        topRowZero = False
        leftColZero = False

        if 0 in matrix[0]: topRowZero = True
        if 0 in [col[0] for col in matrix]: leftColZero = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if leftColZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        if topRowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

                
        