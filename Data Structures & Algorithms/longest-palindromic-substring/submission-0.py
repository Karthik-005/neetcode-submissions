class Solution:
    def isPalindrome(self, s, i, j):
        p, q = i, j

        while p <= q:
            if s[p] != s[q]:
                return False

            p, q = p+1, q-1
        
        return True

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        maxLen = s[0]
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if self.isPalindrome(s, i, j):
                    maxLen = maxLen if len(maxLen) > (j-i+1) else s[i:j+1]

        return maxLen