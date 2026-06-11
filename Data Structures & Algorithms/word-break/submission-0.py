class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        max_len = len(max(wordDict, key=lambda s: len(s)))
        info = set(wordDict)
        seen = {}

        def func(i, st=""):
            if (i, st) in seen:
                return seen[(i, st)]
                
            if i == len(s):
                return not st

            st += s[i]

            if len(st) > max_len:
                return False
            
            if st in info:
                seen[(i+1, '')] = func(i+1, '') 
                seen[(i+1, st)] = func(i+1, st)
                return seen[(i+1, '')] or seen[(i+1, st)]
            
            seen[(i+1, st)] = func(i+1, st)

            return seen[(i+1, st)]
        
        return func(0)
        