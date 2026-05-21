class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        def _hlp(i, j, see=set(), wordi=0):
            if wordi == len(word): 
                return True
            if i >= len(board) or j >= len(board[0]): return False
            if i < 0 or j < 0: return False

            if board[i][j] != word[wordi]: return False
            if (i,j) in see: return False
            seen = see
            a = _hlp(i, j+1, seen.union({(i,j)}), wordi+1)
            b = _hlp(i, j-1, seen.union({(i,j)}), wordi+1)
            c = _hlp(i+1, j, seen.union({(i,j)}), wordi+1)
            d = _hlp(i-1, j, seen.union({(i,j)}), wordi+1)

            return a or b or c or d

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]: continue

                if _hlp(i, j): return True
        
        return False