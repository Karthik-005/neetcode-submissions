class Solution:
    def numDecodings(self, s: str) -> int:
        
        seen = {len(s):1}

        def func(i):
            if i in seen:
                return seen[i]

            if (i < len(s) and s[i] == '0') or i > len(s):
                return 0

            num1 = func(i+1)
            num2 = 0 if (i+1 < len(s) and s[i]+s[i+1] >= '27') else func(i+2)
            
            seen[i] = num1 + num2

            return seen[i]
        
        return func(0)