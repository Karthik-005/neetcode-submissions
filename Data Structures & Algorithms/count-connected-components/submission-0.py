class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        graph = defaultdict(set)

        # Create an adjacency.
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        notVisited = {x for x in range(n)}
        print(notVisited, graph, sep='\n')

        def dfs(curr):
            if curr not in notVisited:
                return
            
            notVisited.remove(curr)
            for v in graph[curr]:
                dfs(v)

        numComp = 0
        while notVisited:
            numComp += 1
            node = notVisited.pop()
            notVisited.add(node)
            dfs(node)

        print(notVisited)
        return numComp
            

