class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2

            cond = (m == len(nums) - 1) or ((m == 0) and (nums[m] > nums[m+1])) or (nums[m] > nums[m+1] and nums[m] > nums[m-1])

            if cond:
                return m
            
            if nums[m] < nums[m+1]:
                l = m + 1
            
            elif nums[m] < nums[m-1]:
                r = m - 1
        

            
            
            
