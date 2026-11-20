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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int[] tmp = new int[2];
        return dfs(preorder, inorder,Integer.MAX_VALUE , tmp);
    }

    private TreeNode dfs(int[] preorder, int[] inorder,int limit, int[] tmp){
        if (tmp[0] > preorder.length - 1){
            return null;
        }
        if(inorder[tmp[1]] == limit){
            tmp[1]++;
            return null;
        }
        TreeNode root = new TreeNode(preorder[tmp[0]]);
        tmp[0]++;
        root.left = dfs(preorder,inorder,root.val,tmp);
        root.right = dfs(preorder,inorder,limit,tmp);
        return root;
    }
}
