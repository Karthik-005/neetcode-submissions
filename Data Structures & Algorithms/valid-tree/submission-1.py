class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited_nodes = set()
        visited_edges = set()
        cycle = 0
        graph = defaultdict(set)

        # Create an adjacency list.
        for u, v in edges:
            if u == v:
                return False
            graph[u].add(v)
            graph[v].add(u)
        
        def dfs(currNode, parNode=None):
            nonlocal cycle
            if currNode in visited_nodes:
                if (currNode, parNode) not in visited_edges:
                    cycle = 1
                return

            visited_nodes.add(currNode)

            for v in graph[currNode]:
                visited_edges.add((currNode, v))
                dfs(v, currNode)


        dfs(0)
        print(cycle)
        return (n == len(visited_nodes)) and (cycle == 0) 
            

