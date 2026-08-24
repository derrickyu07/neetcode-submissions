# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if subRoot == None or self.sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) 

    def sameTree(self,root, subRoot):
        if subRoot is None and root is None:
            return True
        elif subRoot is None or root is None or root.val != subRoot.val:
            return False
        return self.sameTree(root.right,subRoot.right) and self.sameTree(root.left,subRoot.left)