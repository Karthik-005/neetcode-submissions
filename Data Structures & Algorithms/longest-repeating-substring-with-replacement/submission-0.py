class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        count = defaultdict(int)
        i = 0

        for j in range(len(s)) :
            count[s[j]] += 1
            while (j-i+1) - max(count.values()) > k :
                count[s[i]] -= 1
                i += 1

            maxLen = max(maxLen, j-i+1)
            
        return maxLen        
