class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i,j,c):
            if c == len(word):
                return True
            if i >= ROWS or i < 0 or j >= COLS or j < 0 or word[c] != board[i][j] or board[i][j] == '#':
                return False
            board[i][j] = '#'
            res = (dfs(i+1,j,c+1) or 
            dfs(i-1,j,c+1) or
            dfs(i,j+1,c+1) or
            dfs(i,j-1,c+1))
            board[i][j] = word[c]
            return res
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False