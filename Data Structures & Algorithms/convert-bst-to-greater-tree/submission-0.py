# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def sum_(node):
            if not node:
                return 0
            
            return node.val + sum_(node.left) + sum_(node.right)
        
        totalSum = sum_(root)
        print(totalSum)

        def dfs(node):
            nonlocal totalSum
            if not node:
                return
            
            dfs(node.left)
            totalSum -= node.val
            node.val += totalSum
            dfs(node.right)
        
        dfs(root)

        return root