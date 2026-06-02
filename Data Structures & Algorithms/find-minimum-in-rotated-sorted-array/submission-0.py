class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
            
        l, r = 0, len(nums)-1
        while l < r :
            m = (l+r)//2

            if nums[m] < nums[(m+1)%len(nums)] and nums[m] < nums[(m-1)%len(nums)] :
                return nums[m]

            if nums[m] > nums[(m+1)%len(nums)] and nums[m] > nums[(m-1)%len(nums)] :
                return nums[(m+1)%len(nums)]

            if nums[m] < nums[r] :
                r = m

            else :
                l = m        