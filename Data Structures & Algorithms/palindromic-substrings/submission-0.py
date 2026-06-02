class Solution:
    def countSubstrings(self, s: str) -> int:
        i = count = 0
        while i < len(s)-1:
            l = r = i
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                count += 1
                l -= 1
                r += 1

            i += 1
    
        return count+1