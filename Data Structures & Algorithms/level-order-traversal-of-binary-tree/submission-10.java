/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> levelOrder(TreeNode root) {

        dfs(root,0);
        return res;
    }
    private void dfs(TreeNode node,int limit){
            if (node == null){
                return;
            }
            if (limit == res.size()){
                res.add(new ArrayList<>());
            }
            res.get(limit).add(node.val);
            dfs(node.left,limit+1);
            dfs(node.right,limit+1);
            return;
        }
}
