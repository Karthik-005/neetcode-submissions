class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = [0]*len(nums)
        curr_sum = 0

        for i in range(-1, -len(nums)-1, -1):
            sums[i] = curr_sum
            curr_sum += nums[i]
        
        curr_sum = 0
        for i in range(len(nums)):
            sums[i] -= curr_sum
            
            if sums[i] == 0:
                return i
            
            curr_sum += nums[i]
        

        return -1