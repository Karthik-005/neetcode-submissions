class Solution:

    def combinationSum(self, nums: List[int], target: int, curr_sum=0, curr_comb=[]) -> List[List[int]]:
        combs = set()

        def findCombination(nums, target, curr_sum, curr_comb=[]) :
            nonlocal combs
            if curr_sum == target :
                combs.add(tuple(sorted(curr_comb)))
                return
            
            if curr_sum > target :
                return
            
            for i in nums :
                curr_comb.append(i)
                findCombination(nums, target, curr_sum+i, curr_comb)
                curr_comb.pop()

        findCombination(nums, target, 0)
        return [list(i) for i in combs]        
                