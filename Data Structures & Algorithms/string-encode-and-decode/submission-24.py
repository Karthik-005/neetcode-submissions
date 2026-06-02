class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [0] * len(strs)

        for i in range(len(strs)):
            res[i] = str(len(strs[i])) + ',' + strs[i]
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i =0
        res = []

        while i < len(s):
            j = i

            while s[j] != ',':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res








"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs :
            res += str(len(s)) + "#" + s

        return res 

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s) :
            j = i

            while s[j] != "#" :
                j += 1

            n = int(s[i:j])    

            strs.append(s[j+1:j+1+n])
            i = j+1+n

        return strs
"""

