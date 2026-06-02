# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, root: TreeNode, val: int) -> List[TreeNode]:
        q = deque([root])
        PotentialSubroots = []

        while q :
            for _ in range(len(q)) :
                x = q.popleft()

                if x.val == val :
                    PotentialSubroots.append(x)

                if x.left :
                    q.append(x.left)
                if x.right :
                    q.append(x.right)

        return PotentialSubroots

    def isSametree(self, p: TreeNode, q: TreeNode) -> bool :
        if not p and not q :
            return True

        if p and q and p.val == q.val:
            leftSame = self.isSametree(p.left, q.left)
            rightSame = self.isSametree(p.right, q.right)  

            return leftSame and rightSame 

        else :
            return False      

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        PotentialSubroots = self.search(root, subRoot.val)

        for node in PotentialSubroots :
            if self.isSametree(node, subRoot) :
                return True

        return False    