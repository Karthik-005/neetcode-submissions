# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root :
            return ''

        code = []
        
        def dfs(root) :
            nonlocal code

            if not root :
                code.append('?')
                return

            code.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        
        return ','.join(code)     
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data :
            return None

        code = data.split(',')
        print(code)
        i=0
        def dfs() :
            nonlocal code, i

            if code[i] == '?' :
                return None

            root = TreeNode(val=int(code[i]))
            i += 1
            root.left = dfs()
            i += 1
            root.right = dfs()

            return root 

        return dfs()    

