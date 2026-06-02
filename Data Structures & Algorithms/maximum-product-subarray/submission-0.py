class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = -float('inf')

        for i in range(len(nums)):
            curr = 1
            for j in range(i, len(nums)):
                curr *= nums[j]
                maxProduct = curr if maxProduct < curr else maxProduct 
        
        return maxProduct