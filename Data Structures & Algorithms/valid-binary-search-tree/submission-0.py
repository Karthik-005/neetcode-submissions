# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], upperBound=float('inf'), lowerBound=-float('inf')) -> bool:
        if not root :
            return True

        if root.val >= upperBound or root.val <= lowerBound :
            return False
        
        leftIsBST = self.isValidBST(root.left, upperBound=root.val, lowerBound=lowerBound)
        rightIsBST = self.isValidBST(root.right, upperBound, lowerBound=root.val)

        return leftIsBST and rightIsBST