# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        c = 0
        def dfs(node):
            nonlocal res, c
            if node == None: return
            dfs(node.left)
            c +=1
            if c == k:
                res = node.val
                return
            dfs(node.right)

            return
        dfs(root)
        return res