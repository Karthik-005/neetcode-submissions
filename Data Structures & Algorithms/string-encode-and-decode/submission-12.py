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
            n = ""

            while s[j] != "#" :
                n += s[j]
                j += 1

            print("->",n)
            n = int(n)
            
            j += 1

            word = ""
            a, b = j, j+n
            for j in range(a, b) :
                word += s[j]     

            strs.append(word)
            i = b

        return strs        