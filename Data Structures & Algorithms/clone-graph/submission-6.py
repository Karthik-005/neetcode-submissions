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
            return None

        visit = {}
        visit[node.val] = Node(node.val)
        q = deque([node])

        while q:
            x = q.popleft()

            for neighbor in x.neighbors:
                if neighbor.val not in visit:
                    visit[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)

                visit[x.val].neighbors.append(visit[neighbor.val])

        return visit[node.val]
                        




