class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        
        A = [0 for _ in range(26)]

        for i in range(len(s)) :
            A[ord(s[i])-ord('a')] += 1
            A[ord(t[i])-ord('a')] -= 1

        for i in A :
            if i != 0 :
                return False

        return True            


