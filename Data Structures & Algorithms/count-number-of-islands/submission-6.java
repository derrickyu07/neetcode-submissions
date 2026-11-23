class Solution {
    public int numIslands(char[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length; 

        int res = 0;
        for (int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                if (grid[r][c] == '1'){
                    res++;
                    dfs(r,c,grid);
                }
            }
        }
        return res;
        
    }

    private void dfs(int r, int c, char[][] grid){
        int ROWS = grid.length;
        int COLS = grid[0].length;

        if (r < 0 || c < 0 || COLS <= c || ROWS <= r || grid[r][c] == '0'){
            return;
        }
        grid[r][c] = '0';
        dfs(r+1,c,grid);
        dfs(r-1,c,grid);
        dfs(r,c+1,grid);
        dfs(r,c-1,grid);
        return;
    }
}
