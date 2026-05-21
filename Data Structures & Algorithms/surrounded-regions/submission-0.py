class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def _recursiveMarkY(i, j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]): return
            if board[i][j] != 'O': return

            board[i][j] = 'Y'
            _recursiveMarkY(i+1, j)
            _recursiveMarkY(i-1, j)
            _recursiveMarkY(i, j+1)
            _recursiveMarkY(i, j-1)

        for i in range(len(board)):
            _recursiveMarkY(i, 0)
            _recursiveMarkY(i, len(board[0])-1)

        for i in range(len(board[0])):
            _recursiveMarkY(0, i)
            _recursiveMarkY(len(board)-1, i)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'Y': 
                    board[i][j] = 'O'
                    continue
                board[i][j] = 'X'

