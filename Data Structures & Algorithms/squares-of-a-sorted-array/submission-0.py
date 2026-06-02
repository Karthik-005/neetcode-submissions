class Solution:
    # Start the pointers at the extremes
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, -1
        res = deque([])

        while l <= r :
            if abs(nums[l]) >= abs(nums[r]) :
                res.appendleft(nums[l]**2)
                l += 1
            else :
                res.appendleft(nums[r]**2)
                r -= 1

        return list(res)    


#Start the pointers in the middle
"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        res = [0]*len(nums)

        while i < len(nums) and nums[i] < 0 :
            i += 1

        j = i-1
        k = 0
        while j>=0 and i < len(nums) :
            if nums[i]**2 <= nums[j]**2  :
                res[k] = nums[i]**2
                i= i+1

            elif nums[i]**2 > nums[j]**2 :
                res[k] = nums[j]**2
                j = j-1
            
            k += 1

        while j >= 0 :
            res[k] = nums[j]**2
            j, k = j-1, k+1           

        while i < len(nums) :
            res[k] = nums[i]**2
            i, k = i+1, k+1

        return res      
        """

