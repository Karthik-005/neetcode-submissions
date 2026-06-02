class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        match_ = {')':'(', '}':'{', ']':'['} 

        for i in s : 
            if i in match_ :
                if not q :
                    return False
                    
                if match_[i] != q.pop() :
                    return False

            else :
                q.append(i)

        return not q                

