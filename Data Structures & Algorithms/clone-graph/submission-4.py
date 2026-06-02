"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        visit = {}

        def dfs(node):
            clone_node = Node(val=node.val)
            visit[node.val] = clone_node 
       
            for neighbor in node.neighbors:

                if neighbor.val not in visit:
                    neighbor_clone = dfs(neighbor)
                else:
                    neighbor_clone = visit[neighbor.val]

                clone_node.neighbors.append(neighbor_clone)

            return clone_node
        return dfs(node)