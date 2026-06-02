class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
            
        def rob_(i, start):
            if (i+1)%len(nums) == start:
                return 0
            
            if (i+2)%len(nums) == start:
                return nums[i]
            
            maxValue = 0
            j = (i+2)%len(nums)
            while j != start:
                if j not in mem:
                    mem[j] = rob_(j, start)
                
                maxValue = mem[j] if mem[j] > maxValue else maxValue

                j = (j+1)%len(nums)
            
            mem[i] = maxValue + nums[i]
            return mem[i]

        maxProfit = 0
        for i in range(len(nums)):
            mem = {}
            currProfit = rob_(i, i)
            maxProfit = currProfit if currProfit > maxProfit else maxProfit
        
        return maxProfit

