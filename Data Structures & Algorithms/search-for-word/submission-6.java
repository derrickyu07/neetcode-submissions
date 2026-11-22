class Solution {
    public boolean exist(char[][] board, String word) {
        int ROWS = board.length;
        int COLS = board[0].length;
        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c <COLS;c++){
                if (dfs(r,c,board,word,0)){
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(int r,int c,char[][] board,String word,int i){

        if (word.length() == i){
            return true;
        }
        int ROWS = board.length;
        int COLS = board[0].length;
        
        if (r < 0 || c < 0 || ROWS <= r || COLS <= c || board[r][c] != word.charAt(i)){
            return false;
        }
        board[r][c] = '#';
        boolean res = dfs(r+1,c,board,word,i+1) || dfs(r-1,c,board,word,i+1) || dfs(r,c+1,board,word,i+1) || dfs(r,c-1,board,word,i+1);
        board[r][c] = word.charAt(i);
        return res;
    }
}
