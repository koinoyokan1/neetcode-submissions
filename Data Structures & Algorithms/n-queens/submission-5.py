class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colQueen, diagQueen, antiDiagQueen = set(), set(), set()
        pos = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        def _solve(row=0):
            nonlocal pos

            if row == n:
                strings = [''.join(row) for row in pos]
                ans.append(strings)
                return

            for col in range(n):
                if col in colQueen or row+col in diagQueen or col-row in antiDiagQueen: continue
                
                colQueen.add(col)
                diagQueen.add(row+col)
                antiDiagQueen.add(col-row)
                pos[row][col] = 'Q'
                _solve(row+1)
                pos[row][col] = '.'
                colQueen.remove(col)
                diagQueen.remove(row+col)
                antiDiagQueen.remove(col-row)

        _solve()
        return ans
