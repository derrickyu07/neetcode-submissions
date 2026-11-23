class Solution {
    Map<Integer,List<Integer>> adjMap = new HashMap<>(); 
    Set<Integer> visited = new HashSet<>();

    public boolean validTree(int n, int[][] edges) {
        if ((n - 1) <  edges.length){
            return false;
        }
        for (int i = 0; i < n; i++){
            adjMap.put(i,new ArrayList<>());
        }
        for (int[] edge: edges){
            adjMap.get(edge[0]).add(edge[1]);
            adjMap.get(edge[1]).add(edge[0]);
        }
        if(!dfs(0,-1)){
            return false;
        }
        return visited.size() == n;
    }

    private boolean dfs(int node, int par){
        if (visited.contains(node)){
            return false;
        }
        visited.add(node);
        for(int nei: adjMap.get(node)){
            if (par == nei){
                continue;
            }
            if (!dfs(nei,node)){
                return false;
            }
        }
        return true;
    }
}
