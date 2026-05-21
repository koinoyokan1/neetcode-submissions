from collections import Counter

class Solution:
    def isRowValid(self, vals):
        cntr = Counter(vals)
        for val in cntr.keys():
            if val == '.': continue
            if cntr[val] > 1: return False
        return True

    def isColValid(self, rows, i):
        vals = [row[i] for row in rows]
        cntr = Counter(vals)
        for val in cntr.keys():
            if val == '.': continue
            if cntr[val] > 1: return False
        return True

    def isCellValid(self, board, x, y):
        vals = []
        for i in range(x, x+3):
            for j in range(y, y+3):
                vals.append(board[i][j])
        cntr = Counter(vals)
        for val in cntr.keys():
            if val == '.': continue
            if cntr[val] > 1: return False
        return True        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isRowValid(board[i]): return False
            if not self.isColValid(board, i): return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isCellValid(board, i, j): return False
        
        return True
        