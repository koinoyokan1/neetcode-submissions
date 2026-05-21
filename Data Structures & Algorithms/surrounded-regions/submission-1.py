class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def markNotSurrounded(i, j):
            if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1: return
            if board[i][j] != 'O': return 
            
            board[i][j] = 'Y'
            markNotSurrounded(i+1, j)
            markNotSurrounded(i-1, j)
            markNotSurrounded(i,j+1)
            markNotSurrounded(i,j-1)

        for i in range(len(board)):
            if board[i][0] == 'O': markNotSurrounded(i, 0)
            if board[i][len(board[0])-1] == 'O': markNotSurrounded(i, len(board[0])-1)
        
        for i in range(len(board[0])):
            if board[0][i] == 'O': markNotSurrounded(0, i)
            if board[len(board)-1][i] == 'O': markNotSurrounded(len(board)-1, i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == 'Y': board[i][j] = 'O'
