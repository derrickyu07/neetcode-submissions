class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        int ROWS = heights.length;
        int COLS = heights[0].length;
        boolean[][] pac = new boolean[ROWS][COLS];
        boolean[][] atl = new boolean[ROWS][COLS];
        for (int r = 0; r < ROWS; r++){
            dfs(r,0,heights,pac,heights[r][0]);
            dfs(r,COLS-1,heights,atl,heights[r][COLS-1]);
        }
        for (int c = 0; c < COLS; c++){
            dfs(0,c,heights, pac,heights[0][c]);
            dfs(ROWS-1,c,heights,atl,heights[ROWS-1][c]);
        }

        for (int r = 0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (pac[r][c] && atl[r][c]){
                    res.add(Arrays.asList(r,c));
                }
            }
        }
        return res;
    }

    private void dfs(int r, int c, int[][] heights, boolean[][] ocean, int prev){
        int ROWS = heights.length;
        int COLS = heights[0].length;

        if(r < 0 || c < 0 || ROWS <= r || COLS <= c || ocean[r][c] || prev > heights[r][c]){
            return;
        }
        ocean[r][c] = true;
        dfs(r+1,c,heights,ocean, heights[r][c]);
        dfs(r-1,c,heights,ocean, heights[r][c]);
        dfs(r,c+1,heights,ocean, heights[r][c]);
        dfs(r,c-1,heights,ocean, heights[r][c]);
        return;
    }
}
