class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0

        for num in nums :
            if num-1 not in numSet :
                len_ = 0
                while num+len_ in numSet :
                    len_ += 1

                max_len = max(len_, max_len)

        return max_len            

            
        