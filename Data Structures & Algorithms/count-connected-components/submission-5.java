class Solution {
    Map<Integer, List<Integer>> edgeMap;
    boolean[] visit;

    public int countComponents(int n, int[][] edges) {
        edgeMap = new HashMap();
        visit = new boolean[n];
        int res = 0;
        for (int i = 0; i < n;i++){
            edgeMap.put(i,new ArrayList<>());
        }    
        for (int[] edge: edges){
            edgeMap.get(edge[0]).add(edge[1]);
            edgeMap.get(edge[1]).add(edge[0]);
        }

        for (int i = 0; i < n; i++){
            if (!visit[i]){
                visit[i] = true;
                res++;
                dfs(i);
            }
        }
        return res;
    }
    private void dfs(int node){
        
        for (int nei:edgeMap.get(node)){
            if (!visit[nei]){
                visit[nei] = true;
                dfs(nei);
            }
        }
        return;
    }
}
