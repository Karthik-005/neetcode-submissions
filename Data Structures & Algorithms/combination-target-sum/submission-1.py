class Solution:

    def combinationSum(self, nums: List[int], target: int, curr_sum=0, curr_comb=[]) -> List[List[int]]:
        combs = set()

        def findCombination(nums, target, curr_sum, curr_comb=[]) :
            nonlocal combs
            
            for i in range(len(nums)) :
                if (curr_sum+nums[i] > target) :
                    continue

                curr_comb.append(nums[i])
                if curr_sum+nums[i] == target :
                    combs.add(tuple(sorted(curr_comb)))
                    curr_comb.pop()
                    continue

                
                findCombination(nums[i:], target, curr_sum+nums[i], curr_comb)
                curr_comb.pop()

        findCombination(nums, target, 0)
        return [list(i) for i in combs]        
                