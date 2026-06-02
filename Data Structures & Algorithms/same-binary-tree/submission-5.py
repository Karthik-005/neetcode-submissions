# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2 :
            x1 = q1.popleft()
            x2 = q2.popleft()

            if not x1 and not x2 :
                continue
                
            elif (x1 and not x2) or (not x1 and x2) or (x1.val != x2.val) :
                return False    
    
            q1.append(x1.left)
            q1.append(x1.right)
            q2.append(x2.left)
            q2.append(x2.right)

        return True        
