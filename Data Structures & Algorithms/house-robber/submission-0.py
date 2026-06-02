class Solution:
    def rob(self, nums: List[int]) -> int:
        
        robValue = {}

        def rob_(i):
            if i+2 >= len(nums):
                return nums[i]
            
            maxMoney = 0
            for j in range(i+2, len(nums)):
                if j not in robValue:
                    robValue[j] = rob_(j)
                
                maxMoney = robValue[j] if robValue[j] > maxMoney else maxMoney

            robValue[i] = nums[i] + maxMoney
            return  robValue[i]
        
        maxProfit = 0
        for j in range(len(nums)):
            if j not in robValue:
                currProfit = rob_(j)
            
            maxProfit = currProfit if currProfit > maxProfit else maxProfit
        
        return maxProfit
