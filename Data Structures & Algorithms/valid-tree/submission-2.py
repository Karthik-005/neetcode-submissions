class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        
        visited = set()
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(curr , par=None):
            if curr in visited:
                return False

            visited.add(curr)
            for v in graph[curr]:
                if v == par:
                    continue
                if not dfs(v, curr):
                    return False

            return True

        
        return dfs(0) and len(visited) == n 
