class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()

        for i in s : 
            if (i == '(') or (i == '{') or (i == '[') :
                q.append(i)
        
            else :
                if not q :
                    return False
                x = q.pop()
                if not (ord(x)+2 == ord(i) or ord(x)+1 == ord(i)) :
                    return False


        return not q                

