# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q) :
            return False
        elif not p and not q:
            return True    

        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)

        while q1 and q2 :
            x1 = q1.popleft()
            x2 = q2.popleft()

            if (x1 and x2) :
                if x1.val != x2.val :
                    return False    
            else :
                return False
    

            if x1.left and x2.left :
                q1.append(x1.left)
                q2.append(x2.left)
            elif (x1.left and not x2.left) or (not x1.left and x2.left) :
                return False    

            if x1.right and x2.right :
                q1.append(x1.right)
                q2.append(x2.right)
            elif (x1.right and not x2.right) or (not x1.right and x2.right) :
                return False

        return True        
