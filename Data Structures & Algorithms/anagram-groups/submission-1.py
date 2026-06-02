from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for i in strs :
            s = str(sorted(i))
            seen[s].append(i)
        return list(seen.values())         
