from collections import defaultdict

class Solution:
    def sort_str(self, s) :
        A = [0]*26

        for i in s :
            A[ord(i)-ord("a")] += 1

        t = ''
        for i in range(len(A)) :
            t += chr(i+ord("a"))*A[i]

        return t

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for i in strs :
            s = str(sorted(i))
            seen[s].append(i)
        return list(seen.values())         
