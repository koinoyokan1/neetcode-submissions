from pprint import pprint

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pf_m = matrix
        pprint(matrix)

        r = len(matrix)
        c = len(matrix[0])

        for i in range(1, r):
            self.pf_m[i][0] += self.pf_m[i-1][0]
        
        for i in range(1, c):
            self.pf_m[0][i] += self.pf_m[0][i-1]
        
        for i in range(1, r):
            for j in range(1, c):
                self.pf_m[i][j] = self.pf_m[i][j] + self.pf_m[i-1][j] + self.pf_m[i][j-1] - self.pf_m[i-1][j-1]
        pprint(self.pf_m)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.pf_m[row2][col2]
        if row1 > 0:
            ans -= self.pf_m[row1-1][col2]
        
        if col1 > 0:
            ans -= self.pf_m[row2][col1-1]

        if row1 > 0 and col1 > 0:
            ans += self.pf_m[row1-1][col1-1]

        return ans



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)