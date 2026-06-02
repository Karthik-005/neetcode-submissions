class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            j = 0
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
            
        visit = {}
        res = []

        def dfs(n):
            if n in visit:
                return visit[n]

            visit[n] = True

            for v in graph[n]:
                if dfs(v):
                    return True
                    
            visit[n] = False
            res.append(n)
        
        for n in graph:
            if  dfs(n):
                return ""
        
        return "".join(res[-1::-1])
        



