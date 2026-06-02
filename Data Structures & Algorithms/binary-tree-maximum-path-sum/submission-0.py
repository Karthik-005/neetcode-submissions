# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -float('inf')
        
        def dfs(root) :
            nonlocal maxSum
            leftVal = dfs(root.left) if root.left else 0
            rightVal = dfs(root.right) if root.right else 0

            maxSum = max(maxSum, leftVal+root.val+rightVal, root.val+leftVal, root.val+rightVal, root.val)

            return root.val + max(leftVal, rightVal, 0)

        
        dfs(root)
        return maxSum    

