import copy
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        def dfs(subject, visit):
            nonlocal accepted, discarded, preq, visited
            
            if (subject in visit) or (subject in discarded):
                discarded |= visit
                return

            visit.add(subject)
            if (subject not in preq) or (subject in accepted):
                accepted |= visit 
                
            else:
                for p in preq[subject]:
                    dfs(p, copy.copy(visit))

        preq = defaultdict(list)
        for x, y in prerequisites:
            preq[x].append(y)

        accepted = set()
        discarded = set()
        for course in range(numCourses):
            if (course in discarded) or (course in accepted):
                continue
            visited = set()
            dfs(course, visited)
        
        return len(accepted - discarded) == numCourses