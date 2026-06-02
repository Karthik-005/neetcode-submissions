# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None

        q = deque()
        q.append(root)

        while q :
            x = q.popleft()

            if x.left :
                q.append(x.left)

            if x.right :
                q.append(x.right)

            x.left, x.right = x.right, x.left
            

        return root            