"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
            
        visit = {}
        q = deque([node])
        clone_node = Node(node.val)
        o = deque([clone_node])

        while q:
            x = q.popleft()
            y = o.popleft()
            visit[x.val] = y

            for neighbor in x.neighbors:
                if neighbor.val not in visit:
                    clone = Node(neighbor.val)
                    q.append(neighbor)
                    o.append(clone)
                    visit[neighbor.val] = clone 
                else:
                    clone = visit[neighbor.val]

                y.neighbors.append(clone)

        return clone_node
                        




