class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" :
            return ""

        res, resLen = [-1, -1], float('inf')
        countT, window = defaultdict(int), defaultdict(int)
        l = 0

        # Get the frequencies of all the chars in t.
        for i in t :
            countT[i] += 1
        
        # To do O(1) checkups for determining whether a substring is valid or not.
        have, need = 0, len(countT)

        for r in range(len(s)) :
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]] :
                have += 1
            
            # Store the indices' range of potential solution.
            while have == need :
                if (r-l+1) < resLen :
                    res[0], res[1] = [l, r]
                    resLen = r-l+1
                
                window[s[l]] -= 1
                if (s[l] in countT) and (window[s[l]] < countT[s[l]]) : 
                    have -= 1
                
                l += 1    
                          
            
        return s[res[0] : res[1]+1]